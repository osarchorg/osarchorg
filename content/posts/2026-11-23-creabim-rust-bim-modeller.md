---
title: "CreaBIM publishes a GPL-licensed BIM modeller written in Rust with IFC exchange"
date: "2026-11-23 00:00:00"
lastmod: "2026-11-23 00:00:00"
slug: "creabim-rust-bim-modeller"
draft: true
author: "Moult"
description: "CreaBIM is a new GPL-3.0 BIM modeller written in Rust that derives plans, sections, sheets and schedules from one model, with IFC import and IFC4 export."
tags: ["CreaBIM", "Bonsai", "Architecture"]
cover:
  image: "/uploads/2026/11/creabim-plan-and-3d-view.webp"
  alt: "CreaBIM interface showing a ground floor plan beside a 3D view of a two-storey sample house, with the project browser and view settings"
  hiddenInSingle: false
  hiddenInList: false
---
[CreaBIM](https://github.com/chopinregis/CreaBIM) is a free software BIM modeller for architects, written in Rust and published under GPL-3.0 in November 2026 by its developer, Regis Benoit Brice Nde Tene. Plans, sections, elevations, sheets, schedules and quantity take-offs are derived from a single 3D model, and editing borrows Blender conventions such as an Edit mode and the G, R and S transform keys. Version 1.1.1 provides packages for Windows, Linux and macOS.

The project documents import of IFC2X3, IFC4 and IFC4X3 files and export to IFC4, with experimental support for buildingSMART's alpha IFC5 (IFCX) format. On import, straight walls, slabs, doors and windows become native editable elements, while other elements arrive as meshes that keep their IFC class. Other outputs include vector PDF sheets, SVG plans, CSV and XLSX schedules, glTF for Blender and FreeCAD documents, and `.blend` and `.FCStd` files can be linked into a model.

The developer describes version 1.1 as ready to explore but not yet for production work, and lists current limitations in a [known gaps document](https://github.com/chopinregis/CreaBIM/blob/main/docs/KNOWN_GAPS.md). CreaBIM keeps its own project file and translates IFC in and out, so drawings and sheets are not carried in the IFC export. An [OSArch community thread](https://community.osarch.org/discussion/3801/creabim-bonsai-round-tripping-models-and-drawings-through-ifc) is discussing how models and drawings could round-trip between CreaBIM and Bonsai through IFC, starting with preserving data CreaBIM does not recognise.
