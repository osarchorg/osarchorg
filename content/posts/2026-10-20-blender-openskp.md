---
title: "OpenSKP brings SketchUp import and export to Blender"
date: "2026-10-20 00:00:00"
slug: "blender-openskp"
draft: true
author: "Moult"
description: "OpenSKP Import/Export adds SketchUp file exchange to Blender without the Trimble SDK, with component instancing and textured material import."
tags: ["OpenSKP", "Blender", "Architecture"]
cover:
  image: "/uploads/common/blender-logo.png"
  alt: "Blender logo"
  hiddenInSingle: false
  hiddenInList: false
---
[OpenSKP Import/Export](https://github.com/iamahsanmehmood/blender-openskp) is a free software extension for Blender 4.2 and later that reads and writes SketchUp `.skp` files without the Trimble SDK or a SketchUp installation. The extension is GPL-3.0-or-later, while the bundled OpenSKP reader and writer remains MIT-licensed. It works independently of BIM add-ons and is available for manual installation from the repository.

Import preserves repeated components and groups through Blender collection instances, sharing geometry between placements. Materials, opacity, embedded textures and UV coordinates are imported, while SketchUp tags become collections with their visibility retained. Export writes triangulated mesh geometry, solid material colours and named collections as SketchUp tags.

There are limits to model exchange: texture images are import-only, and exporting imported geometry does not yet automatically preserve its original tags and materials across placements. Editing an imported component requires accessing its source mesh, which updates all instances. The [project documentation](https://github.com/iamahsanmehmood/blender-openskp#what-it-does) explains these workflows and the current export restrictions.
