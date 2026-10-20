---
title: "Bonsai 0.9.0 released"
date: "2026-10-20 00:00:00"
slug: "bonsai-0-9-0-released"
draft: false
author: "Moult"
description: "Bonsai 0.9.0 brings Bonsai Viewer, an overhauled IfcOpenShell engine, interactive authoring tools, autosave, and drawing and quantity take-off improvements."
tags: ["Bonsai", "IfcOpenShell", "Blender", "Architecture", "Structure", "Services", "Construction", "Operations"]
cover:
  image: "/uploads/2026/10/bonsai-0-9-0-release.png"
  alt: "Bonsai release artwork showing a rabbit with the Bonsai logo"
  hiddenInSingle: false
  hiddenInList: false
---
[Bonsai 0.9.0](https://community.osarch.org/discussion/comment/30246/#Comment_30246) has been released with 2,070 new features and fixes. The free software BIM authoring tool gains a redesigned IfcOpenShell engine: the release team's fourteen-model benchmark reports IFC opening 2.5–3.4 times faster, with less than half the memory used by 0.8.5.

The release introduces Bonsai Viewer, a standalone IFC viewer for Windows, Linux and Apple Silicon macOS. It supports model federation, georeferencing, property inspection, section planes and measurements, with geometry caches for faster reopening. Its initial feature set focuses on viewing; clash detection is not yet included.

Authoring improvements include draggable wall and MEP dimensions, a section box, opt-in IFC autosave and GPU snapping. Drawing generation can now run with Blender in the background, while schedule imports, quantity take-off and unit handling receive fixes. Developers gain a modular engine and editable RocksDB-backed models. Download from [bonsaibim.org](https://bonsaibim.org/) and see the [full release notes](https://community.osarch.org/discussion/comment/30246/#Comment_30246) for platform support and API migration details.
