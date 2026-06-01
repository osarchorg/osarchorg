---
title: "Bonsai Viewer is coming"
date: "2026-05-29 00:00:52"
lastmod: "2026-05-29 00:00:52"
slug: "bonsai-viewer-is-coming"
draft: false
author: "Moult"
description: "Bonsai Viewer is being developed as a free software IFC coordination and review viewer, addressing the gap left by commercial tools such as Revizto, BIMcollab, and Solibri."
tags: ["Bonsai", "IfcOpenShell", "Architecture", "Structure", "Services", "Construction", "Operations"]
cover:
  image: "/uploads/2026/05/bonsai-viewer-ui-preview.png"
  alt: "Bonsai Viewer user interface preview"
  hiddenInSingle: false
  hiddenInList: false
---
Work is underway on [Bonsai Viewer](https://community.osarch.org/discussion/3386/addressing-some-core-ifcopenshell-issues/p1), a dedicated free software IFC viewer for model coordination and review. The gap is straightforward: there is no mature free software equivalent of Revizto, BIMcollab, Solibri, and similar coordination viewers. Bonsai Viewer aims to fill that gap, while also making it easier for others to build their own desktop, tablet, kiosk, on-site screen, or web-based IFC viewer applications on top of IfcOpenShell.

The project is part of a wider push to address core IfcOpenShell issues around performance, web support, TypeScript support, faster model loading, and practical viewer application scaffolding. Blender remains important for authoring, but it is not optimised as a high-speed coordination viewer; separating viewer workflows from Blender opens the door to faster model review, federation, georeferencing, and lighter deployment targets.

Early Bonsai Viewer builds are now available for testing on the [IfcOpenShell builds website](https://builds.ifcopenshell.org/), with Linux and Windows builds already hooked into the build system. The current UI is still early, with properties and the spatial tree shown as mockups, but georeferencing support has already landed. Coming work includes macOS builds, web support, actual model data in the panels, more speedups, streaming, and continued stability and geometry correctness improvements.
