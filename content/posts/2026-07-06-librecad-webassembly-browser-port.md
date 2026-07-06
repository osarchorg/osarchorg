---
title: "LibreCAD now runs in the browser through a WebAssembly port"
date: "2026-07-06 09:00:00"
lastmod: "2026-07-06 09:00:00"
slug: "librecad-webassembly-browser-port"
draft: false
author: "Moult"
description: "A WebAssembly port of LibreCAD runs the full GPL-licensed 2D CAD application in Chromium-based browsers, with DXF editing, DWG reading, PDF export, and browser-based file handling."
tags: ["LibreCAD", "Architecture", "Construction"]
cover:
  image: "/uploads/2021/01/librecad-has-a-new-release-candidate-for-the-version-2-2-0.jpg"
  alt: "LibreCAD interface"
  hiddenInSingle: false
  hiddenInList: false
---

Magik has published [LibreCAD in your browser](https://magik.net/librecad/), a WebAssembly port that runs the full GPL-licensed [LibreCAD](https://librecad.org/) desktop application in a browser tab rather than a reduced viewer or JavaScript reimplementation. The demo loads the C++ and Qt application through Emscripten and Qt for WebAssembly, with the fork available as [LibreCAD-Web](https://github.com/magik6k/LibreCAD-Web).

The port supports opening, editing, and saving DXF files, reading DWG files through libdxfrw, layers, blocks, dimensions, hatching, drawing and modification tools, SVG export, PDF export, bundled fonts and hatch patterns, settings persistence, and browser-based file open and download flows. The initial Brotli-compressed transfer is reported at about 18 MB, and the current build requires a recent Chromium-based browser because it depends on WebAssembly JavaScript Promise Integration for nested Qt dialogs.

For OSArch readers, the interesting part is not only that LibreCAD can be tested without installing a desktop package, but that a mature Qt-based CAD application can now be compiled for the web with relatively small application-level changes. The write-up also documents practical issues around nested modal dialogs, browser file handling, WebAssembly exceptions, and Qt canvas performance that are relevant to other free software CAD and AEC tools considering browser delivery.
