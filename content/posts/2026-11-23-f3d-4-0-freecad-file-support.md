---
title: "F3D 4.0 viewer adds support for FreeCAD files"
date: "2026-11-23 00:00:00"
lastmod: "2026-11-23 00:00:00"
slug: "f3d-4-0-freecad-file-support"
draft: true
author: "Moult"
description: "F3D 4.0, a free 3D viewer, can open FreeCAD FCStd files on the desktop and in its web viewer, and adds a scene hierarchy widget, an animation bar and video export."
tags: ["F3D", "FreeCAD"]
cover:
  image: "/uploads/2026/11/f3d-4-0-freecad-file-viewer.webp"
  alt: "F3D displaying a FreeCAD model of a planetary gear assembly with the scene hierarchy widget listing its parts"
  hiddenInSingle: false
  hiddenInList: false
---
[F3D](https://f3d.app/), a free and open source 3D viewer, can open FreeCAD `.FCStd` files as of [version 4.0.0](https://github.com/f3d-app/f3d/releases/tag/v4.0.0), released on 20 October 2026. The FreeCAD project [highlighted the addition](https://blog.freecad.org/2026/11/05/f3d-updated-now-supports-freecad-files/), noting that FreeCAD files can be viewed in F3D's [public web viewer](https://f3d.app/viewer) as well as in the desktop application, which has packages for many operating systems.

The release adds a scene hierarchy widget in which the visibility of parts can be toggled, an animation bar showing key frames, export of animations to a video stream, and a reworked Android application. An HTML custom element, `<f3d-viewer>`, allows a model to be embedded in a web page. As a major release, 4.0 also removes deprecated command line options and reworks some interactions, which are covered in a migration guide.

According to the FreeCAD announcement, FreeCAD itself uses F3D to generate thumbnails of STEP files, and the self-hosted 3D file hosting system [Manyfold](https://manyfold.app/news/2026/11/05/release-v0-154-0.html) uses it to render previews of FreeCAD files. For FreeCAD users, F3D provides a lightweight way to inspect and share models without opening them in FreeCAD.
