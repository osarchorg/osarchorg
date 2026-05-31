# OSArch.org

This repository contains the source for [OSArch.org](https://osarch.org/), the OSArch community news and events website.

The site is built with [Hugo](https://gohugo.io/) and uses the PaperMod theme with local OSArch layout and CSS customisations.

## Local Development

Install Hugo, then run:

```sh
hugo server -b http://localhost:1313/
```

The local site is usually available at:

```text
http://localhost:1313/
```

To build the static site:

```sh
hugo --cleanDestinationDir
```

## Content

Main content lives in:

- `content/posts/` for news posts
- `content/events/` for events
- `content/chat.md` and `content/subscribe.md` for static pages

Images and other static files live in:

- `static/uploads/`
- `static/logo.png`
- `static/favicon.ico`

## News Sources

OSArch monitors and aggregates news, releases, and events from community sources relevant to free software for the built environment. Common sources include:

- [FreeCAD Blog](https://blog.freecad.org/)
- [Speckle Events](https://speckle.systems/speckle-events/)
- [Speckle Blog](https://speckle.systems/blog)
- [OSArch Community](https://community.osarch.org/)
- [That Open People](https://people.thatopen.com/)
- [Blender News](https://www.blender.org/news/)

## Images

Use dated upload folders for images that belong to a specific post or event:

```text
static/uploads/YYYY/MM/lowercase-semantic-name-with-hyphens.jpg
```

Use `static/uploads/common/` for reusable images such as project logos, organisation logos, and other assets that may be referenced by multiple posts or events:

```text
static/uploads/common/blender-logo.png
```

Name image files with lowercase, semantic words separated by hyphens. Avoid spaces, underscores, generic names, and source filenames such as `image1.png`, `screenshot.png`, or `download.jpg`.

Before committing images, resize them so the largest dimension is no more than 800px unless there is a specific reason to keep a larger source. Optimise images after resizing:

```sh
magick input.png -resize '800x800>' static/uploads/common/example-logo.png
optipng -o2 static/uploads/common/example-logo.png
```

For JPEG images:

```sh
magick input.jpg -resize '800x800>' static/uploads/YYYY/MM/example-image.jpg
jpegoptim --strip-all static/uploads/YYYY/MM/example-image.jpg
```

## Adding A News Post

Create a new Markdown file in `content/posts/`.

Use a filename based on the publication date and slug:

```text
content/posts/YYYY-MM-DD-post-title.md
```

Use front matter like this:

```yaml
---
title: "Post title"
date: "YYYY-MM-DD HH:MM:SS"
draft: false
author: "Author Name"
description: "Short description for search engines, feeds, and social previews."
categories: ["Architecture"]
tags: ["Blender", "Sustainability"]
cover:
  image: "/uploads/YYYY/MM/image-name.jpg"
  alt: "Short image description"
  hiddenInSingle: false
  hiddenInList: false
---
```

Write the post body in Markdown. Prefer Markdown syntax for headings, links, images, lists, tables, and emphasis. Use raw HTML only when Markdown cannot represent the content cleanly.

## Adding An Event

Create a new Markdown file in `content/events/`.

Use a filename based on the event date and slug:

```text
content/events/YYYY-MM-DD-event-title.md
```

Use front matter like this:

```yaml
---
title: "Event title"
date: "YYYY-MM-DD HH:MM:SS"
draft: false
description: "Short event summary."
event_start: "YYYY-MM-DDTHH:MM:SSZ"
event_end: "YYYY-MM-DDTHH:MM:SSZ"
event_url: "https://example.org/event"
location: "Online"
---
```

Write the event details in Markdown. Events are shown on the events page and included in the generated calendar feed.

## Tags

Tags should be used consistently so visitors can subscribe to topic-specific feeds.

### Software Tags

- Archipack
- BabylonJS
- Bonsai
- BRL-CAD
- CAD Sketcher
- Castle Game Engine
- CGAL
- COMPAS
- dotbim
- EnergyPlus
- Blender
- FreeCAD
- GIMP
- Godot
- IFClite
- IfcOpenShell
- Inkscape
- Krita
- Ladybug Tools
- LibreCAD
- LibreDWG
- OpenFOAM
- OpenProject
- OpenSCAD
- Open Source Ecology
- QCAD
- Radiance
- Speckle
- Sverchok
- ThatOpenPlatform
- Tissue
- Topologic
- VI-Suite
- Xeokit

### Discipline Tags

- Architecture
- Construction
- Structure
- Services
- Operations
- Sustainability

## Publishing

Before publishing, run:

```sh
hugo --cleanDestinationDir
```

Check the generated site locally and commit the source files. The generated `public/` directory is build output and should not be committed unless the deployment process explicitly requires it.
