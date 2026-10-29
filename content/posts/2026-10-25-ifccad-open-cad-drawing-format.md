---
title: "IFCCAD explores an open drawing format built on IFCX"
date: "2026-10-25 00:00:00"
slug: "ifccad-open-cad-drawing-format"
draft: true
author: "Moult"
description: "OpenAEC's experimental IFCCAD profile combines an open drawing model, DWG/DXF conversion and a browser explorer, with future links to BIM."
tags: ["IFCCAD", "OpenAEC", "Architecture", "Construction"]
cover:
  image: "/uploads/2026/10/ifccad-format-explorer.png"
  alt: "IFCCAD Format Explorer showing drawing structure alongside a house floor plan in Open CAD Studio"
  hiddenInSingle: false
  hiddenInList: false
---
[IFCCAD](https://www.open-aec.com/en/ifccad/) is an experimental OpenAEC drawing profile built on IFCX, intended as an open alternative for CAD working files and exchange. It describes geometry, layers, blocks, text, layouts and presentation as application-independent information. Drawings can stand alone, while future development aims to connect BIM-generated geometry with dimensions, annotations and manual drawing edits.

The [MPL-2.0 Rust implementation](https://github.com/OpenAEC-Foundation/ifccad) provides validation, readers and writers, and conversion of supported DWG/DXF content through opencadcodec. The [browser-based Format Explorer](https://ifccad-explorer.open-aec.com/) processes files locally, showing drawing structure, properties and conversion diagnostics alongside an Open CAD Studio view. Users can open their own files or inspect examples, including a house floor plan and an entity catalogue.

IFCCAD is still in development and is not an official buildingSMART CAD standard. Conversion coverage is qualified for specific content and workflows; complete dimensions, broader object support and stable associative BIM regeneration remain development work. The project reports conversion losses rather than claiming lossless exchange for arbitrary drawings. The Explorer and source repository offer ways to test practical CAD files and contribute feedback.
