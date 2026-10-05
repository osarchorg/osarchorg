---
title: "CADBase Brings Version Control to FreeCAD and Blender"
date: "2026-10-03 00:00:00"
lastmod: "2026-10-03 00:00:00"
slug: "cadbase-version-control-freecad-blender"
draft: false
author: "mnnxp"
description: "CADBase brings version control, openBIM support, and browser-based 3D visualization to FreeCAD and Blender."
tags: ["FreeCAD", "Blender", "Architecture", "Construction", "CADBase"]
cover:
  image: "/uploads/2026/10/cadbase-ifc-viewer.jpg"
  alt: "CADBase web viewer displaying a 3D IFC bridge model with file revision history"
  hiddenInSingle: false
  hiddenInList: false
---

[CADBase](https://cadbase.rs) is an open-source data exchange platform designed to streamline collaboration among teams using different open-source design tools. Operating as a centralized infrastructure, it provides engineering-tailored version control and fills a gap for workflows utilizing both FreeCAD and Blender. Through native library add-ons, the platform lets users store, track, and share 3D models and manufacturing data across a project lifecycle, eliminating messy shared folders and untracked file iterations.

The platform's architecture uses a three-level model (Components, Modifications, and File Sets), where model files are versioned in the context of a modification — covering both parametric CAD models and polygonal meshes. It is built on Rust and WebAssembly, with a web viewer powered by OCCT and Three.js that natively supports engineering and openBIM formats such as STEP, IFC, and STL. Engineers editing parametric parts in FreeCAD can seamlessly publish new revisions and sync their native workspace files, while visualizers or BIM managers review the geometry directly in a browser via WebGL/WebGPU without a local CAD install. From there, the same verified datasets can be pulled into Blender, keeping parametric and visual workflows on a single version.

For AEC teams focused on data sovereignty, the entire platform is built for self-hosting via Docker Compose or Kubernetes, connecting easily to internal PostgreSQL databases and S3-compatible storage. Step-by-step deployment instructions are available in the [CADBase Self-Hosting Guide](https://cadbase.rs/en/overviews/self-hosting/). The underlying repositories and tools are fully open-source and hosted publicly within the [CADBase GitLab organization](https://gitlab.com/cadbase/).

Extensions:
- FreeCAD workbench: https://github.com/mnnxp/cadbaselibrary-freecad/
- Blender add-on: https://extensions.blender.org/add-ons/cadbase-library/
