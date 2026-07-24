---
title: "IFClite geometry is now available from Python"
date: "2026-07-24 15:34:00"
lastmod: "2026-07-24 15:34:00"
slug: "ifclite-python-api"
draft: false
author: "Moult"
description: "The new ifclite-geom Python package brings IFClite's Rust geometry kernel to CPython as prebuilt native wheels."
tags: ["IFClite", "Architecture", "Construction", "Structure"]
cover:
  image: "/uploads/2026/07/ifclite-python-api.png"
  alt: "IFClite logo"
  hiddenInSingle: false
  hiddenInList: false
---

[IFClite is now available to Python users](https://ltplus-ag.github.io/ifc-lite/api/python/) through `ifclite-geom`, a native wheel that runs the project's Rust geometry kernel in-process. It converts IFC data into per-entity triangle meshes without requiring Node.js, WebAssembly, a subprocess, or a local server.

The package accepts an IFC file as bytes and offers either efficient binary buffers for direct use with NumPy or a JSON representation made from ordinary arrays. Output meshes are welded and indexed, use IFC's Z-up orientation and world coordinates in metres, and are keyed by IFC STEP ID with metadata including IFC type, GlobalId, name, and colour.

Prebuilt wheels support CPython 3.9 and newer on Windows x64, macOS on Apple silicon and Intel, and Linux on x86_64 and aarch64. The package can be installed with `pip install ifclite-geom`; examples and the PyO3 binding source are linked from the [Python API documentation](https://ltplus-ag.github.io/ifc-lite/api/python/).
