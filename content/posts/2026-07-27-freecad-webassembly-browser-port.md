---
title: "FreeCAD now runs in the browser through WebAssembly"
date: "2026-07-27 18:14:48"
lastmod: "2026-07-27 18:14:48"
slug: "freecad-webassembly-browser-port"
draft: true
author: "Moult"
description: "A WebAssembly port runs the FreeCAD desktop application in recent Chromium-based browsers, including its modelling workbenches, Python console, and local file handling."
tags: ["FreeCAD", "Architecture", "Construction"]
cover:
  image: "/uploads/2026/07/freecad-webassembly-browser.webp"
  alt: "FreeCAD running in a web browser with an architectural wall section open"
  hiddenInSingle: false
  hiddenInList: false
---

Magik has published [FreeCAD in your browser](https://magik.net/freecad/), a WebAssembly port that runs the FreeCAD desktop application in a browser tab. The build combines Qt, OpenCASCADE, Coin3D, CPython, PySide6, VTK, and SMESH, and includes workbenches for Part, Part Design, Sketcher, Draft, TechDraw, BIM, CAM, FEM, Assembly, and other workflows.

The port supports opening and saving FCStd files, importing STEP, IGES, and BREP files, interacting with the 3D viewport, and using FreeCAD's Python console and PySide6 GUI scripting. User settings persist in IndexedDB. For AEC users, the browser build provides access to FreeCAD's BIM tools without a desktop installation, although IFC support is not included in the current build.

The initial download is approximately 96 MB compressed and currently requires Chrome or Edge 137 or newer because it depends on WebAssembly JavaScript Promise Integration. The build is single-threaded, external FEM meshers and solvers cannot run inside the browser sandbox, and some interface and rendering issues remain. Source code and build material are available from the [freecad-web repository](https://github.com/magik6k/freecad-web).
