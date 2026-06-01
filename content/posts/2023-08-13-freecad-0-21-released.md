---
title: "FreeCAD 0.21 released"
date: "2023-08-13 12:20:37"
lastmod: "2023-08-13 12:20:39"
slug: "freecad-0-21-released"
draft: false
author: "Yorik van Havre"
description: "Last week, a new stable release of FreeCAD has been published, tagged 0.21. This release is mostly there to provide a stable point before implementing Toponaming resolution functionality. Toponaming is how we call the problem of unstable re"
tags: ["FreeCAD", "Architecture", "Structure", "Services"]
wordpress_id: 6833
wordpress_guid: "https://osarch.org/?p=6833"
cover:
  image: "/uploads/2023/08/freecad-0-21-released-banner.jpg"
  alt: "FreeCAD 0.21 released"
  hiddenInSingle: false
  hiddenInList: false
---
Last week, a new stable release of [FreeCAD](https://freecad.org) has been published, tagged 0.21. This release is mostly there to provide a stable point before implementing Toponaming resolution functionality. Toponaming is how we call the problem of unstable reference names in FreeCAD (Edge1 might become Edge5 after a shape recompute), it is the last big issue the development team wants to solve before deeming FreeCAD good for the mythical 1.0 release.

Nevertheless, this release brings a number of interesting improvements for BIM users, among which are:

- New spline tools for the sketcher
- A new, easy-to-use section tool that works interactively, and works for Arch/BIM objects too
- Better styling tools for texts and dimensions, which now use an unified structure
- The BIM layer manager is now in Draft too
- FreeCAD now supports several different DWG converters to import and export DWG files
- The FEM workbench has received a lot of improvements, and is now more and more fit for civil engineering (see this [post](https://twitter.com/ERaeiat/status/1687075996455899137) and [the work of Ebrahim](https://twitter.com/ERaeiat))
- Revamped addons manager


More about these features and much more can be found in the [release notes](https://wiki.freecad.org/Release_notes_0.21).

In parallel to the work being done in FreeCAD itself, many things have happened on the [BIM workbench](https://github.com/yorikvanhavre/BIM_Workbench), namely the arrival of a new [NativeIFC](https://github.com/yorikvanhavre/FreeCAD-NativeIFC) module, that allows FreeCAD to open, manipulate and save IFC files natively. This turns FreeCAD the second NativeIFC-enabled authoring application, after BlenderBIM (Both actually share a lot of code). The NativeIFC structure is progressively being integrated into the BIM workbench, and a lot of it is already directly usable by BIM users. Check the [documentation](https://github.com/yorikvanhavre/FreeCAD-NativeIFC/blob/main/doc/README.md) to know more, of follow this [osarch discussion thread](https://community.osarch.org/discussion/comment/16772) to keep updated on the progresses.
