#!/usr/bin/env python3
"""Generate OSArch HTML and plaintext newsletters from Hugo content."""

from __future__ import annotations

import argparse
import html
import re
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - fallback for systems without PyYAML
    yaml = None


BASE_URL = "https://osarch.org"
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


@dataclass(frozen=True)
class Page:
    data: dict[str, Any]
    body: str
    path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate OSArch newsletter HTML and plaintext files."
    )
    parser.add_argument(
        "-n",
        "--news-count",
        type=int,
        default=10,
        help="number of latest news entries to include (default: 10)",
    )
    return parser.parse_args()


def load_front_matter(text: str) -> tuple[dict[str, Any], str] | None:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None

    raw_front_matter, body = match.groups()
    if yaml:
        data = yaml.safe_load(raw_front_matter) or {}
    else:
        data = parse_simple_yaml(raw_front_matter)

    return data, body.strip()


def parse_simple_yaml(raw: str) -> dict[str, Any]:
    """Small fallback parser for the front matter shapes used in this repo."""
    data: dict[str, Any] = {}
    current_map: dict[str, Any] | None = None

    for line in raw.splitlines():
        if not line.strip():
            continue

        if line.startswith("  ") and current_map is not None:
            key, value = split_yaml_line(line.strip())
            current_map[key] = parse_yaml_value(value)
            continue

        key, value = split_yaml_line(line)
        if value == "":
            current_map = {}
            data[key] = current_map
        else:
            current_map = None
            data[key] = parse_yaml_value(value)

    return data


def split_yaml_line(line: str) -> tuple[str, str]:
    if ":" not in line:
        return line.strip(), ""
    key, value = line.split(":", 1)
    return key.strip(), value.strip()


def parse_yaml_value(value: str) -> Any:
    value = value.strip()
    if value in {"true", "false"}:
        return value == "true"
    if value == "":
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_yaml_value(part.strip()) for part in inner.split(",")]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def load_pages(directory: Path) -> list[Page]:
    pages: list[Page] = []
    for path in directory.glob("*.md"):
        parsed = load_front_matter(path.read_text(encoding="utf-8"))
        if not parsed:
            continue
        data, body = parsed
        if data.get("draft") is True:
            continue
        pages.append(Page(data=data, body=body, path=path))
    return pages


def parse_dt(value: Any) -> datetime:
    if isinstance(value, datetime):
        dt = value
    elif not value:
        dt = datetime.min
    else:
        text = str(value).replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(text)
        except ValueError:
            dt = datetime.strptime(str(value), "%Y-%m-%d %H:%M:%S")

    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt


def display_date(dt: datetime) -> str:
    return dt.strftime("%d %B %Y").lstrip("0")


def display_event_time(dt: datetime, timezone_label: str | None, all_day: bool) -> str:
    if all_day:
        return f"All day, {display_date(dt)}"
    return f"{display_date(dt)}, {dt.strftime('%H:%M')} {timezone_label or ''}".strip()


def post_url(data: dict[str, Any]) -> str:
    dt = parse_dt(data.get("date"))
    return f"{BASE_URL}/{dt.year:04d}/{dt.month:02d}/{dt.day:02d}/{data.get('slug', '')}/"


def event_listing_url(data: dict[str, Any]) -> str:
    return f"{BASE_URL}/events/{data.get('slug', '')}/"


def absolute_url(url: str | None) -> str:
    if not url:
        return ""
    return url if url.startswith("http") else f"{BASE_URL}{url}"


def teaser(data: dict[str, Any], body: str) -> str:
    description = data.get("description")
    if description:
        return str(description)

    plain = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", body)
    plain = re.sub(r"[#*_`>\-]+", " ", plain)
    plain = re.sub(r"\s+", " ", plain).strip()
    words = plain.split()
    return " ".join(words[:42]) + ("..." if len(words) > 42 else "")


def tags_text(data: dict[str, Any]) -> str:
    tags = data.get("tags") or []
    if isinstance(tags, list):
        return ", ".join(str(tag) for tag in tags)
    return str(tags)


def latest_posts(root: Path, count: int) -> list[Page]:
    posts = load_pages(root / "content" / "posts")
    posts.sort(key=lambda page: parse_dt(page.data.get("date")), reverse=True)
    return posts[:count]


def upcoming_events(root: Path, today: datetime) -> list[Page]:
    events = load_pages(root / "content" / "events")
    upcoming = [
        event
        for event in events
        if parse_dt(event.data.get("event_start") or event.data.get("date")).astimezone(
            timezone.utc
        )
        >= today.astimezone(timezone.utc)
    ]
    upcoming.sort(
        key=lambda event: parse_dt(
            event.data.get("event_start") or event.data.get("date")
        ).astimezone(timezone.utc)
    )
    return upcoming


def render_news_card(page: Page) -> str:
    data = page.data
    cover = data.get("cover") if isinstance(data.get("cover"), dict) else {}
    cover_url = absolute_url(cover.get("image"))
    url = post_url(data)
    dt = parse_dt(data.get("date"))
    tags = tags_text(data)
    meta = display_date(dt) + (f" &middot; {html.escape(tags)}" if tags else "")

    image_html = ""
    if cover_url:
        image_html = f"""<a href="{html.escape(url)}" style="text-decoration:none;"><img src="{html.escape(cover_url)}" alt="{html.escape(cover.get('alt') or data.get('title') or '')}" width="176" style="width:176px;max-width:100%;height:auto;border:0;border-radius:6px;display:block;"></a>"""

    return f"""
      <tr>
        <td style="padding:10px;background:#f3f6f9;border-bottom:1px solid #eee;border-radius:5px;">
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;">
            <tr>
              <td class="stack" valign="top" width="176" style="width:176px;padding:0 18px 12px 0;">{image_html}</td>
              <td class="stack" valign="top" style="padding:0;">
                <p style="margin:0 0 6px 0;font-family:Arial,sans-serif;font-size:13px;line-height:18px;color:#aaa;">{meta}</p>
                <h3 style="margin:0 0 8px 0;font-family:Arial,sans-serif;font-size:21px;line-height:27px;color:#667d99;"><a href="{html.escape(url)}" style="color:#667d99;text-decoration:none;">{html.escape(data.get('title', 'Untitled'))}</a></h3>
                <p style="margin:0 0 12px 0;font-family:Arial,sans-serif;font-size:15px;line-height:23px;color:#667d99;">{html.escape(teaser(data, page.body))}</p>
                <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;"><a href="{html.escape(url)}" style="color:#e14658;text-decoration:underline;font-weight:bold;">Read the story</a></p>
              </td>
            </tr>
          </table>
        </td>
      </tr>"""


def render_event_card(page: Page) -> str:
    data = page.data
    start = parse_dt(data.get("event_start") or data.get("date"))
    external_url = data.get("event_url") or event_listing_url(data)
    listing_url = event_listing_url(data)
    timezone_label = data.get("timezone_abbr") or data.get("timezone")
    when = display_event_time(start, timezone_label, bool(data.get("all_day")))

    return f"""
      <tr>
        <td style="padding:10px;background:#f3f6f9;border-bottom:1px solid #eee;border-radius:5px;">
          <p style="margin:0 0 5px 0;font-family:Arial,sans-serif;font-size:13px;line-height:18px;color:#e14658;font-weight:bold;">{html.escape(when)}</p>
          <h3 style="margin:0 0 7px 0;font-family:Arial,sans-serif;font-size:19px;line-height:25px;color:#667d99;"><a href="{html.escape(external_url)}" style="color:#667d99;text-decoration:none;">{html.escape(data.get('title', 'Untitled event'))}</a></h3>
          <p style="margin:0 0 9px 0;font-family:Arial,sans-serif;font-size:15px;line-height:23px;color:#667d99;">{html.escape(teaser(data, page.body))}</p>
          <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;"><a href="{html.escape(external_url)}" style="color:#e14658;text-decoration:underline;font-weight:bold;">Event details</a> <span style="color:#aaa;">|</span> <a href="{html.escape(listing_url)}" style="color:#667d99;text-decoration:underline;">OSArch listing</a></p>
        </td>
      </tr>"""


def render_html(posts: list[Page], events: list[Page]) -> str:
    latest_date = parse_dt(posts[0].data.get("date")) if posts else datetime.now(timezone.utc)
    subject_date = latest_date.strftime("%B %Y")
    preheader = (
        f"The latest OSArch news plus {len(events)} upcoming "
        f"event{'s' if len(events) != 1 else ''}."
    )
    news_rows = "\n".join(render_news_card(post) for post in posts)
    event_rows = (
        "\n".join(render_event_card(event) for event in events)
        if events
        else '<tr><td style="padding:10px;background:#f3f6f9;border-bottom:1px solid #eee;border-radius:5px;font-family:Arial,sans-serif;font-size:15px;line-height:23px;color:#667d99;">No upcoming events are currently listed.</td></tr>'
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <title>OSArch Newsletter - {html.escape(subject_date)}</title>
  <style>
    @media only screen and (max-width: 620px) {{
      .container {{ width: 100% !important; }}
      .pad {{ padding-left: 20px !important; padding-right: 20px !important; }}
      .stack {{ display: block !important; width: 100% !important; padding-right: 0 !important; }}
      .logo {{ width: 32px !important; height: 32px !important; }}
      h1 {{ font-size: 30px !important; line-height: 36px !important; }}
    }}
  </style>
</head>
<body style="margin:0;padding:0;background:#ffffff;color:#667d99;">
  <div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">{html.escape(preheader)}</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;background:#ffffff;">
    <tr>
      <td align="center" style="padding:24px 12px;">
        <table role="presentation" class="container" width="640" cellpadding="0" cellspacing="0" style="width:640px;max-width:640px;border-collapse:collapse;background:#ffffff;border-radius:5px;overflow:hidden;">
          <tr>
            <td class="pad" style="padding:28px 34px 26px 34px;background:#e7edf3;border-bottom:1px solid #eee;">
              <a href="{BASE_URL}/" style="text-decoration:none;"><img class="logo" src="{BASE_URL}/logo.png" width="32" alt="OSArch" style="display:block;border:0;width:32px;height:32px;margin:0 0 24px 0;"></a>
              <p style="margin:0 0 8px 0;font-family:Arial,sans-serif;font-size:14px;line-height:20px;color:#e14658;text-transform:uppercase;letter-spacing:1px;">Newsletter</p>
              <h1 style="margin:0 0 12px 0;font-family:Arial,sans-serif;font-size:36px;line-height:42px;color:#667d99;font-weight:bold;">Latest open source AEC news</h1>
              <p style="margin:0;font-family:Arial,sans-serif;font-size:17px;line-height:26px;color:#667d99;">Community curated news and events for free software in AEC</p>
            </td>
          </tr>
          <tr>
            <td class="pad" style="padding:30px 34px 8px 34px;">
              <h2 style="margin:0 0 20px 0;font-family:Arial,sans-serif;font-size:24px;line-height:30px;color:#667d99;">News</h2>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:separate;border-spacing:0 10px;">
                {news_rows}
              </table>
            </td>
          </tr>
          <tr>
            <td class="pad" style="padding:24px 34px 10px 34px;background:#ffffff;">
              <h2 style="margin:0 0 4px 0;font-family:Arial,sans-serif;font-size:24px;line-height:30px;color:#667d99;">Upcoming Events</h2>
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border-collapse:separate;border-spacing:0 10px;">
                {event_rows}
              </table>
            </td>
          </tr>
          <tr>
            <td class="pad" style="padding:24px 34px 32px 34px;background:#ffffff;">
              <p style="margin:0 0 12px 0;font-family:Arial,sans-serif;font-size:15px;line-height:23px;color:#667d99;">Have news or an event to share? Post it on the community forum or join the live chat.</p>
              <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;line-height:22px;color:#667d99;"><a href="https://community.osarch.org/" style="color:#e14658;text-decoration:underline;">Forum</a> &middot; <a href="{BASE_URL}/chat/" style="color:#e14658;text-decoration:underline;">Live Chat</a> &middot; <a href="{BASE_URL}/events/" style="color:#e14658;text-decoration:underline;">Events Calendar</a> &middot; <a href="{BASE_URL}/" style="color:#e14658;text-decoration:underline;">OSArch News</a></p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""


def render_text(posts: list[Page], events: list[Page]) -> str:
    lines = [
        "OSArch Newsletter",
        "Latest open source AEC news",
        "Community curated news and events for free software in AEC",
        "",
        "NEWS",
        "",
    ]

    for index, post in enumerate(posts, start=1):
        data = post.data
        dt = parse_dt(data.get("date"))
        tags = tags_text(data)
        meta = display_date(dt) + (f" - {tags}" if tags else "")
        lines.extend(
            [
                f"{index}. {data.get('title', 'Untitled')}",
                meta,
                textwrap.fill(teaser(data, post.body), width=78),
                post_url(data),
                "",
            ]
        )

    lines.extend(["UPCOMING EVENTS", ""])
    if events:
        for index, event in enumerate(events, start=1):
            data = event.data
            start = parse_dt(data.get("event_start") or data.get("date"))
            timezone_label = data.get("timezone_abbr") or data.get("timezone")
            when = display_event_time(start, timezone_label, bool(data.get("all_day")))
            external_url = data.get("event_url") or event_listing_url(data)
            lines.extend(
                [
                    f"{index}. {data.get('title', 'Untitled event')}",
                    when,
                    textwrap.fill(teaser(data, event.body), width=78),
                    f"Event details: {external_url}",
                    f"OSArch listing: {event_listing_url(data)}",
                    "",
                ]
            )
    else:
        lines.extend(["No upcoming events are currently listed.", ""])

    lines.extend(
        [
            "Have news or an event to share?",
            "Forum: https://community.osarch.org/",
            f"Live Chat: {BASE_URL}/chat/",
            f"Events Calendar: {BASE_URL}/events/",
            f"OSArch News: {BASE_URL}/",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    today = datetime.now(timezone.utc)
    stem = f"newsletter-{today.strftime('%Y-%m-%d')}"

    posts = latest_posts(root, args.news_count)
    events = upcoming_events(root, today)

    html_output = Path.cwd() / f"{stem}.html"
    text_output = Path.cwd() / f"{stem}.txt"

    html_output.write_text(render_html(posts, events), encoding="utf-8")
    text_output.write_text(render_text(posts, events), encoding="utf-8")

    print(f"Wrote {html_output}")
    print(f"Wrote {text_output}")
    print(f"Included {len(posts)} news item(s) and {len(events)} upcoming event(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
