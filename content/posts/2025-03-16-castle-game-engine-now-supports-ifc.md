---
title: "Castle Game Engine now supports IFC"
date: "2025-03-16 23:41:50"
lastmod: "2025-03-16 23:41:52"
slug: "castle-game-engine-now-supports-ifc"
draft: false
author: "Moult"
description: "The Castle Game Engine is a free, open source, cross-platform (desktop, mobile, console, web) 3D and 2D game engine. It comes with a powerful visual editor and support for open standards like glTF, X3D, ... and now IFC - a key open standard"
tags: ["Castle Game Engine", "Bonsai", "FreeCAD", "Architecture", "Structure", "Services", "Construction"]
wordpress_id: 10579
wordpress_guid: "https://osarch.org/?p=10579"
cover:
  image: "/uploads/2025/03/castle-game-engine-now-supports-ifc.png"
  alt: "Castle Game Engine now supports IFC"
  hiddenInSingle: false
  hiddenInList: false
---
The [Castle Game Engine](https://castle-engine.io/) is a free, open source, cross-platform (desktop, mobile, console, web) 3D and 2D game engine. It comes with a powerful visual editor and support for open standards like glTF, X3D, ... and now IFC - a key open standard used in BIM.

This now opens up IFC capabilities in Pascal! For the full implementation details, check out the [Castle Game Engine IFC Documentation](https://castle-engine.io/ifc). You can also watch a [video demonstration](https://www.youtube.com/watch?v=MJcMqfx6u98).

Here's the highlights:

- The engine can load, modify, and save 3D models in IFCJSON.
- Because it's IFC, you can create models with Bonsai or FreeCAD, and then use them as-is in the Castle Game Engine’s tools, such as the Castle Model Viewer. Our model viewer, <https://castle-engine.io/castle-model-viewer> (the "snapshot", 5.3.0 version) supports now viewing IFC files and converting between X3D, glTF, and IFC.
- IFC data is converted to X3D nodes for display. This includes support for various geometric entities (lines, meshes, extrusions, curves, etc.) and maintains a transformation hierarchy.
- IFC files can be loaded into a TCastleScene—either directly via its loading methods or by setting the scene’s URL. However, converting IFC to X3D nodes may lose some IFC details. For a full round-trip without loss, a native approach is recommended.
- Instead of relying solely on the X3D conversion, you can work directly with IFC entities using the provided Pascal classes (from the `CastleIfc` unit). Pascal classes and properties correspond 1-1 to IFC concepts. This “native BIM” approach lets you modify and update IFC data directly and then convert or save it back, preserving all the original information.
- A set of utility functions makes it easier to add, move, and manage elements (like walls or floors) within an IFC model.
- Future enhancements include additional support for textures, more curve types, STEP encoding, and performance optimizations for updating IFC-to-X3D conversions.


The project is sponsored by Sorpetaler Fensterbau GmbH.
