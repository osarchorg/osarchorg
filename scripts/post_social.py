#!/usr/bin/env python3
"""Cross-post an OSArch Hugo post or prepare manual social copy."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib import error, parse, request

BASE_URL = "https://osarch.org"
DEFAULT_MASTODON_INSTANCE = "https://fosstodon.org"
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


@dataclass(frozen=True)
class Post:
    title: str
    description: str
    slug: str
    date: datetime
    path: Path
    cover_image: str | None
    cover_alt: str | None

    @property
    def url(self) -> str:
        return (
            f"{BASE_URL}/{self.date.year:04d}/{self.date.month:02d}/"
            f"{self.date.day:02d}/{self.slug}/"
        )

    @property
    def cover_path(self) -> Path | None:
        if not self.cover_image:
            return None
        return Path("static") / self.cover_image.lstrip("/")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Post an OSArch Hugo article to Mastodon/X, or print LinkedIn copy."
        )
    )
    parser.add_argument("post", type=Path, help="path to content/posts/*.md")
    parser.add_argument(
        "-p",
        "--platform",
        action="append",
        choices=("mastodon", "linkedin", "x"),
        help="platform to post to; repeatable; defaults to all configured platforms",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="actually post for API-backed platforms instead of printing payloads",
    )
    parser.add_argument(
        "--text-file",
        type=Path,
        help="use custom post text from a file instead of generated text",
    )
    parser.add_argument(
        "--env-file",
        type=Path,
        default=Path(".env.local"),
        help="load credentials from an env file (default: .env.local)",
    )
    return parser.parse_args()


def load_post(path: Path) -> Post:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise SystemExit(f"Could not find YAML front matter in {path}")

    data = parse_simple_yaml(match.group(1))
    missing = [key for key in ("title", "date", "slug") if not data.get(key)]
    if missing:
        raise SystemExit(f"{path} is missing required front matter: {', '.join(missing)}")

    return Post(
        title=str(data["title"]),
        description=str(data.get("description", "")),
        slug=str(data["slug"]),
        date=parse_datetime(str(data["date"])),
        path=path,
        cover_image=cover_value(data, "image"),
        cover_alt=cover_value(data, "alt"),
    )


def cover_value(data: dict[str, object], key: str) -> str | None:
    cover = data.get("cover")
    if not isinstance(cover, dict):
        return None
    value = cover.get(key)
    return str(value) if value else None


def load_env_file(path: Path) -> None:
    if not path.exists():
        return

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            raise SystemExit(f"{path}:{line_number}: expected NAME=value")

        name, value = stripped.split("=", 1)
        name = name.strip()
        value = value.strip().strip("\"'")
        if name and name not in os.environ:
            os.environ[name] = value


def parse_simple_yaml(raw: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_map: dict[str, object] | None = None

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


def parse_yaml_value(value: str) -> object:
    value = value.strip()
    if value in {"true", "false"}:
        return value == "true"
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


def parse_datetime(value: str) -> datetime:
    text = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def default_text(post: Post, platform: str) -> str:
    if platform == "x":
        text = f"{post.title}\n\n{post.description}\n\n{post.url}"
        return text if len(text) <= 280 else f"{post.title}\n\n{post.url}"

    hashtags = "\n\n#AEC #OpenSource #FreeSoftware" if platform == "mastodon" else ""
    return f"{post.title}\n\n{post.description}\n\n{post.url}{hashtags}"


def configured_platforms(requested: list[str] | None) -> list[str]:
    if requested:
        return requested

    platforms: list[str] = []
    if os.getenv("MASTODON_ACCESS_TOKEN"):
        platforms.append("mastodon")
    if os.getenv("X_ACCESS_TOKEN"):
        platforms.append("x")
    if not platforms:
        return ["mastodon", "linkedin", "x"]
    return platforms


def post_mastodon(text: str, post: Post, live: bool) -> None:
    instance = os.getenv("MASTODON_INSTANCE", DEFAULT_MASTODON_INSTANCE)
    token = required_env("MASTODON_ACCESS_TOKEN")
    url = f"{instance.rstrip('/')}/api/v1/statuses"

    media_id = upload_mastodon_cover(instance, token, post, live)
    payload = {"status": text, "visibility": "public"}
    if media_id:
        payload["media_ids[]"] = media_id

    body = parse.urlencode(payload).encode()
    headers = {"Authorization": f"Bearer {token}"}
    send("mastodon", url, body, headers, live)


def upload_mastodon_cover(
    instance: str,
    token: str,
    post: Post,
    live: bool,
) -> str | None:
    cover_path = post.cover_path
    if not cover_path:
        return None
    if not cover_path.exists():
        raise SystemExit(f"Cover image not found: {cover_path}")

    url = f"{instance.rstrip('/')}/api/v2/media"
    alt_text = post.cover_alt or post.title
    fields = {"description": alt_text}
    files = {"file": cover_path}
    body, content_type = multipart_form_data(fields, files)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": content_type,
    }

    if not live:
        print(f"\n[mastodon media] DRY RUN")
        print(f"POST {url}")
        print(
            json.dumps(
                {
                    "Authorization": "Bearer ...",
                    "Content-Type": content_type,
                },
                indent=2,
            )
        )
        print(f"file={cover_path}")
        print(f"description={alt_text}")
        return "dry-run-media-id"

    response_body = send("mastodon media", url, body, headers, live, return_body=True)
    media = json.loads(response_body)
    media_id = media.get("id")
    if not media_id:
        raise SystemExit(f"Mastodon media upload did not return an id: {response_body}")
    return str(media_id)


def multipart_form_data(
    fields: dict[str, str],
    files: dict[str, Path],
) -> tuple[bytes, str]:
    boundary = "osarch-social-boundary"
    chunks: list[bytes] = []

    for name, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
                value.encode(),
                b"\r\n",
            ]
        )

    for name, path in files.items():
        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        chunks.extend(
            [
                f"--{boundary}\r\n".encode(),
                (
                    f'Content-Disposition: form-data; name="{name}"; '
                    f'filename="{path.name}"\r\n'
                ).encode(),
                f"Content-Type: {content_type}\r\n\r\n".encode(),
                path.read_bytes(),
                b"\r\n",
            ]
        )

    chunks.append(f"--{boundary}--\r\n".encode())
    return b"".join(chunks), f"multipart/form-data; boundary={boundary}"


def print_linkedin_copy(text: str, post: Post) -> None:
    print("\n[linkedin] COPY/PASTE")
    print("Post text:")
    print()
    print(text)
    print()
    if cover_path := post.cover_path:
        print(f"Image: {cover_path}")
        if post.cover_alt:
            print(f"Alt text: {post.cover_alt}")
    else:
        print("Image: none")


def post_x(text: str, live: bool) -> None:
    token = required_env("X_ACCESS_TOKEN")
    payload = {"text": text}
    body = json.dumps(payload).encode()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    send("x", "https://api.x.com/2/tweets", body, headers, live)


def mask_headers(headers: dict[str, str]) -> dict[str, str]:
    return {
        key: ("Bearer ..." if key.lower() == "authorization" else value)
        for key, value in headers.items()
    }


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def send(
    platform: str,
    url: str,
    body: bytes,
    headers: dict[str, str],
    live: bool,
    return_body: bool = False,
    method: str = "POST",
) -> str:
    printable_headers = mask_headers(headers)

    if not live:
        print(f"\n[{platform}] DRY RUN")
        print(f"{method} {url}")
        print(json.dumps(printable_headers, indent=2))
        if body:
            try:
                print(body.decode())
            except UnicodeDecodeError:
                print(f"<{len(body)} binary bytes>")
        return ""

    req = request.Request(url, data=body, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=30) as response:
            response_body = response.read().decode("utf-8", errors="replace")
            print(f"[{platform}] {response.status} {response.reason}")
            if response_body:
                print(response_body)
            return response_body
    except error.HTTPError as exc:
        response_body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"[{platform}] {exc.code} {exc.reason}\n{response_body}")

    return ""


def main() -> int:
    args = parse_args()
    load_env_file(args.env_file)
    post = load_post(args.post)
    custom_text = args.text_file.read_text(encoding="utf-8").strip() if args.text_file else None

    for platform in configured_platforms(args.platform):
        text = custom_text or default_text(post, platform)
        if platform == "mastodon":
            post_mastodon(text, post, args.live)
        elif platform == "linkedin":
            print_linkedin_copy(text, post)
        elif platform == "x":
            post_x(text, args.live)

    return 0


if __name__ == "__main__":
    sys.exit(main())
