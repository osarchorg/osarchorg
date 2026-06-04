---
title: "IFC Georeferencer brings browser-based georeferencing to IFC"
date: "2026-06-04 00:00:00"
lastmod: "2026-06-04 00:00:00"
slug: "ifc-georeferencer-browser-based-georeferencing"
draft: false
author: "Moult"
description: "IFC Georeferencer is a client-side browser tool from buildingSMART Nederland and Bedrock.engineer for placing IFC models in real-world coordinate reference systems."
tags: ["IFC Georeferencer", "Architecture", "Construction", "Operations"]
cover:
  image: "/uploads/2026/06/ifc-georeferencer-browser-based-georeferencing.png"
  alt: "IFC Georeferencer browser-based BIM georeferencing preview"
  hiddenInSingle: false
  hiddenInList: false
---

[IFC Georeferencer](https://geo.buildingsmart.nl/) is a browser-based tool for giving IFC models real-world coordinates. Developed by [Bedrock.engineer](https://github.com/bedrock-engineer/ifc-georeferencer) for buildingSMART Nederland's Georefereren IFC initiative, it runs client-side so IFC files are processed in the browser rather than uploaded to a server.

The tool can read existing georeferencing data such as `IfcSite`, `TrueNorth`, `IfcMapConversion`, `IfcProjectedCRS`, IFC4.3 `IfcRigidOperation`, and IFC2X3 property-set fallbacks, then write updated IFC georeferencing back into the downloaded file. Users can choose a target EPSG coordinate reference system, anchor a model from `IfcSite`, a map point, or surveyed correspondences, solve a Helmert fit, inspect residuals, and preview the result on basemaps with optional Dutch geodata overlays.

The project is relevant for openBIM workflows that need IFC models to align with GIS, survey, site planning, digital twin, or multi-building coordination data without relying on proprietary authoring tools to get georeferencing right. The source code is available on [GitHub](https://github.com/bedrock-engineer/ifc-georeferencer) under the Apache-2.0 license.
