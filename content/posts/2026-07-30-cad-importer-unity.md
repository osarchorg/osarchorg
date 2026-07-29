---
title: "CAD Importer brings CAD and BIM models into Unity"
date: "2026-07-30 00:00:00"
lastmod: "2026-07-30 00:00:00"
slug: "cad-importer-unity"
draft: false
author: "Moult"
description: "CAD Importer is an MIT-licensed Unity package for importing CAD and BIM models for robotics simulation and digital twins, with support for IFC, STEP, IGES, glTF, STL, PLY, and OBJ."
tags: ["Unity", "IFC", "FreeCAD", "Architecture", "Construction"]
cover:
  image: "/uploads/2026/07/cad-importer-unity.jpg"
  alt: "CAD Importer window in Unity showing mesh, level of detail, physics, and FreeCAD conversion settings"
  hiddenInSingle: false
  hiddenInList: false
---

[CAD Importer](https://github.com/Motawe3/CADImporter) is an MIT-licensed Unity package for bringing CAD and BIM models into real-time robotics simulations and digital twins. Written in pure C# without native plugins, it supports editor imports for STL, PLY, OBJ, glTF and GLB as well as STEP, IGES, and IFC, with asynchronous runtime loading available for the mesh formats.

The importer converts model units and coordinate systems for Unity, preserves assembly or spatial hierarchies and local pivots, and builds prefabs with welded geometry, smooth normals, level-of-detail chains, simplified physics colliders, materials, and metadata. Version 1.4.0 added IFC import through the IfcOpenShell library bundled with FreeCAD, retaining the project, site, building, storey, and element structure while using authored surface colours or a colour-by-material and category palette.

STEP, IGES, and IFC workflows require a local [FreeCAD](https://www.freecad.org/) installation, which CAD Importer uses for conversion and tessellation. The package requires Unity 6000.0 or newer and can be installed directly from its Git repository through Unity's Package Manager; installation instructions, settings, limitations, and sample-scene details are available in the [project documentation](https://github.com/Motawe3/CADImporter/tree/main/Packages/com.motawea.cad-importer).
