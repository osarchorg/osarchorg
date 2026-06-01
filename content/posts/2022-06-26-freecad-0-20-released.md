---
title: "FreeCAD 0.20 released!"
date: "2022-06-26 10:00:37"
lastmod: "2022-06-26 10:00:40"
slug: "freecad-0-20-released"
draft: false
author: "Moult"
description: "FreeCAD 0.20 has been released with tree view improvements, multiple edit modes, section tool, documentation, new add-ons, and improved 2D BIM support."
tags: ["FreeCAD", "Architecture", "Structure", "Services"]
wordpress_id: 2009
wordpress_guid: "https://osarch.org/?p=2009"
cover:
  image: "/uploads/2022/06/freecad-0-20-released-3.jpg"
  alt: "FreeCAD 0.20 released!"
  hiddenInSingle: false
  hiddenInList: false
---
Please welcome the new release of FreeCAD, version **0.20**! Installers and images available for Windows, MacOS and Linux on the [FreeCAD website](https://freecad.org/downloads.php) and on [GitHub](https://github.com/FreeCAD/FreeCAD/releases/tag/0.20).

https://www.youtube.com/embed/-Mqh4-irSO4

This version is pretty much a "stable version", and a continuation of the work done on the **0.19** version. It is backwards-compatible with it, which means the files you produce with 0.20 are still openable with 0.19.

!

Here is a short overview of some of the most interesting features. Check the full [release notes](https://wiki.freecadweb.org/Release_notes_0.20) for more!

!

- **Tree view improvements** : The Tree and Properties views have seen a number of new features and fixes. With a right-button click, you can now add and remove custom properties, or select group contents or dependent objects.
- **Multiple edit modes implementation** : Although FreeCAD supported multiple edit modes since the start, it was never used a lot. Now, you can choose which edit mode to use, which one is the default one, and workbenches are progressively implementing support for it too.
- A shiny new **section cut tool** allows you to make gorgeous, solid-based section views of your models.
- The **add-ons manager** has been almost completely recoded, and shows a much better preview of add-ons. It also allows to search and bulk-update your addons. A new structure now also allows addons to provide preference packs, which can set many FreeCAD preferences at once. This also allows you to easily export your preferences settings.
- he **documentation system** of FreeCAD has also been completely recoded. Although it is still based on the FreeCAD wiki, it prepares the way for a possible migration to a markdown-based system. It also gives much more flexibility, such as offering you to choose between an online or offline version, or to use a specific translated version of the documentation.
- An improved **BIM-to-2D** workflow, as I [documented earlier](http://yorik.uncreated.net/blog/2022-001-freecad-january), with support for hatches, section marks, and much more.
- Support for **2D elements in IFC files**. This is done in collaboration with [BlenderBIM](https://blenderbim.org) devs.

!

More info:

- [Official 0.20 release notes](https://wiki.freecadweb.org/Release_notes_0.20)
- [FreeCAD 0.20 announcement on Yorik's blog](https://yorik.uncreated.net/blog/2022-004-freecad-020)
