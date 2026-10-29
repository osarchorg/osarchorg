---
title: "acadrust provides DWG and DXF file handling in Rust"
date: "2026-10-20 00:00:00"
slug: "acadrust-dwg-dxf-library"
draft: true
author: "Moult"
description: "acadrust is an MPL-2.0 Rust library for reading, writing and inspecting DWG and DXF files without an installed CAD application."
tags: ["acadrust", "Architecture", "Structure", "Services", "Construction"]
cover:
  image: "/uploads/2026/10/acadrust-repository.png"
  alt: "acadrust GitHub repository preview describing a Rust crate for reading, writing and inspecting CAD files"
  hiddenInSingle: false
  hiddenInList: false
---
[acadrust](https://github.com/hakanaktt/acadrust) is a free software Rust library for reading, writing and inspecting CAD files without an installed CAD application. Licensed under MPL-2.0, it handles ASCII and binary DXF and native binary DWG, with reader and writer support spanning R12 through the R2018+ format family.

Its document model covers drawing geometry, annotations, dimensions, meshes and solids, alongside layers, styles, layouts, materials and dynamic blocks. Optional features add document serialization and imports from STL, COLLADA, OBJ, glTF/GLB and FBX. Recovery options provide structured diagnostics for recoverable read errors. The repository lists Open CAD Studio and CADCraft as applications using the library, illustrating its role as a reusable file-handling component for free CAD tools.

Compatibility depends on the drawing version and entities involved. The project's [R12 support notes](https://github.com/hakanaktt/acadrust/blob/main/src/docs/ac1009_support.md) identify remaining fidelity gaps and explain that successfully reading a file does not establish that every field survives saving. Source code, examples and [API documentation](https://docs.rs/acadrust/) are available for developers building CAD exchange and inspection workflows.
