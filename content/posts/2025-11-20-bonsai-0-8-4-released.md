---
title: "Bonsai 0.8.4 released"
date: "2025-11-20 11:46:49"
lastmod: "2025-11-20 11:46:49"
slug: "bonsai-0-8-4-released"
draft: false
author: "Moult"
description: "Bonsai 0.8.4 has been released with 1111 new features and fixes, including Blender 5.0 support, IfcTester.org, RocksDB IFC model handling, and web-focused IfcOpenShell packaging."
tags: ["Bonsai", "IfcOpenShell", "Blender", "Architecture", "Structure", "Services", "Construction", "Operations"]
cover:
  image: "/uploads/2025/11/bonsai-0-8-4-release.png"
  alt: "Bonsai 0.8.4 release"
  hiddenInSingle: false
  hiddenInList: false
---

[Bonsai v0.8.4](https://community.osarch.org/discussion/comment/27144/#Comment_27144) has been released with 1111 new features and fixes. The release brings Bonsai compatibility with Blender 5.0, which matters because Blender 5.0 is a major platform update and required compatibility work throughout the add-on.

The largest user-facing addition is [IfcTester.org](https://ifctester.org/), a browser-based IDS editor and checker created by Sayan Das during Google Summer of Code. It can create and edit IDS files, load IFC models locally in the browser, and audit them as the IDS changes. Bonsai integrates the same interface so users can launch a local IDS editor against the currently loaded IFC model.

On the IfcOpenShell side, 0.8.4 adds early RocksDB support for handling very large IFC models using a streaming parser and `.rdb` serialisation, along with Pyodide wheels for easier web app deployment, Linux ARM64 builds, shared library availability, and build system upgrades. Other notable improvements include snapping upgrades, curve object support, xeokit JSON serialisation, drawing and section annotation fixes, Mac crash fixes, work schedule improvements, zone property editing, an AGS-to-IFC IfcPatch recipe, alignment authoring API work, and better linked IFC path handling. Download Bonsai from [bonsaibim.org](https://bonsaibim.org/) and read the [full release notes](https://community.osarch.org/discussion/comment/27144/#Comment_27144).
