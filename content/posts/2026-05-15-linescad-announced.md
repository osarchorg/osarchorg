---
title: "LinesCAD announced as a new free software BIM and CAD experiment"
date: "2026-05-15 00:00:00"
lastmod: "2026-05-15 00:00:00"
slug: "linescad-announced"
draft: false
author: "Moult"
description: "Yorik van Havre has announced LinesCAD, an early Python-based free software BIM and 2D CAD project built around IFC, IfcOpenShell, Qt, and Coin/Pivy."
tags: ["LinesCAD", "IfcOpenShell", "FreeCAD"]
cover:
  image: "/uploads/2026/05/linescad-ifc-viewer-proof-of-concept.jpg"
  alt: "LinesCAD proof-of-concept IFC viewer"
  hiddenInSingle: false
  hiddenInList: false
---

[Yorik van Havre has announced LinesCAD](https://community.osarch.org/discussion/3456/announcing-linescad), a new side project exploring a simpler free software BIM and 2D CAD application. The first public code is a proof-of-concept IFC viewer in a single Python file, using IfcOpenShell, Pivy/Coin3D, and PySide/Qt to open IFC files without FreeCAD's OpenCASCADE and C++ application stack.

The idea is not to replace FreeCAD or Bonsai, but to test a different shape of tool: fast, lightweight, native-IFC, non-parametric except where IFC itself supports it, and closer to a traditional drawing workflow. Yorik's [project manifesto](https://yorik.uncreated.net/?blog%2F2026%2F2026-001-hi-again) describes a 2D/3D hybrid application that can handle large models and drawings, preserve IFC as the model itself, support DXF import and export, and keep the codebase small enough for users and architects to understand and modify.

LinesCAD is very early, but the direction is interesting because it deliberately separates the BIM/CAD editing experience from heavyweight modelling kernels and complex object structures. If the viewer and scene graph approach proves fast enough, it could open another path for native IFC workflows alongside FreeCAD, Bonsai, and other IfcOpenShell-based applications.
