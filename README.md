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
