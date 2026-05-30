---
title: "LibreDWG 0.12 is released. A free C library to read DWG file."
date: "2021-01-12 12:27:04"
lastmod: "2021-01-12 12:32:49"
slug: "libredwg-0-12-is-released-a-free-c-library-to-read-dwg-file"
draft: false
author: "Bruno Perdigao"
description: "LibreDWG 0.12 is now released. LibreDWG is a free C library to suppport softwares to handle DWG files, the native file format from AutoCAD."
categories: ["All Disciplines"]
tags: ["LibreDWG", "Architecture", "Structure", "Services"]
wordpress_id: 420
wordpress_guid: "https://osarch.org/?p=420"
cover:
  image: "/uploads/2021/01/libredwg-0-12-is-released-a-free-c-library-to-read-dwg-file-libredwg-one-line-small-head.png"
  alt: "LibreDWG 0.12 is released. A free C library to read DWG file."
  hiddenInSingle: false
  hiddenInList: false
---
LibreDWG 0.12 is released. LibreDWG is a free C library to handle DWG files, the native file format from AutoCAD.

This library aims to create an API to support softwares to work with DWG. It is currently in the beta stage, so it doesn't have all the features implemented. However, it already handles reading, converting and writing files from scratch. It also features "SVG and Postscript conversion, converters from and to DXF and JSON, dwggrep to search for text, and dwglayer to print the list of layers."

The 2D CAD file format is an important topic in the OSArch community, since it is mostly dominated by Autodesk. DWG format is very common and widely used. Although it is a proprietary format, it is important for many open source software users. In the AEC, for example, DWG is commonly specified as the default file format by the contractors. Even someone who works with open source software may need to be able to read and write DWG to meet these specifications. LibreDWG aims to fill this gap. However, it is also important to highlight the effort to [make DXF the default file format](https://wiki.osarch.org/index.php?title=Getting_started_with_2D_CAD_drafting), since it is more compatible with open source softwares.

LibreDWG is already supported in FreeCAD, so you can use it to test it out. It is always important to remind that testing and reporting issues is a contribution that every open source project can benefit on.

This new release of LibreDWG features highlights are:

- New add API to easily create new DWGs (or DXFs) from scratch, for CAD programs.
- New dwgadd helper.
- Removed deprecated old API functions.


For more details you can check the full [release notes.](https://savannah.gnu.org/forum/forum.php?forum_id=9906)

More reading:

- Visit [LibreDWG page](https://www.gnu.org/software/libredwg/).
- Join the [OSArch discussion](https://community.osarch.org/discussion/394/dwg-dxf-support-in-foss/p1) about DWG/DXF support in FOSS.
- [Check out](https://wiki.freecadweb.org/FreeCAD_and_DWG_Import) how you can use FreeCAD to test LibreDWG.
