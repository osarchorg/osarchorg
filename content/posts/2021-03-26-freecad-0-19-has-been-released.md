---
title: "FreeCAD 0.19 has been released"
date: "2021-03-26 13:36:07"
lastmod: "2021-03-26 13:36:09"
slug: "freecad-0-19-has-been-released"
draft: false
author: "Bruno Perdigao"
description: "One of the most expected releases if finally here. FreeCAD 0.19 has been released with a lot of improvements and new features in all workbenches."
categories: ["All Disciplines"]
tags: ["FreeCAD", "Architecture", "Structure", "Services"]
wordpress_id: 606
wordpress_guid: "https://osarch.org/?p=606"
cover:
  image: "/uploads/2021/03/freecad-0-19-has-been-released.png"
  alt: "FreeCAD 0.19 has been released"
  hiddenInSingle: false
  hiddenInList: false
---
One of the most expected releases is finally here. FreeCAD 0.19 has been released with a lot of improvements and new features in all workbenches. The list is long, so let's go.

First, some general highlights. There area a few UI improvements such as the inclusion of more dark themes, new icon themes and few retouches in the navigation cube. Furthermore, an option was added to display a checkbox for every item in the document tree, so it's easier to use with a touchscreen.

In this release it was introduced the App Link Component, which is a system that allows objects to use data from another object. This is the core functionality to prepare FreeCAD to work with assemblies. Some of its functions were already being used by the Arch and BIM workbenches, but the new the App Link is merged to the master and can be used by all workbenches, which powers up its possibilities.

The Arch Workbench has also been improved and presents some new features. The Arch Site tool is now able to produce sun path diagrams for solar analysis. It also has the option to show a compass pointing towards the true north of the project, when working with coordinates. This can be combined with the new Shapefile importer, which allows you to work with a GIS base.

The Arch Section Plane tool has two major improvements. Now you can set the limits of the plane, working like a camera clipping view. That way you have more control over what is shown in your sections. Also, a new render mode was added to how the section is displayed in the TechDraw Workbench. It is a faster render but with less precision, which can be helpful in some use cases.

Two new important tools were added to the Arch Workbench. The Arch Truss Tool allow you to create trusses from a baseline and with a variety of options and configurations. The new Arch CurtainWall Tool does what it says, creating curtains wall from a base surface as dividing it in quadrangular shapes.

Besides all that, there were also improvements in other workbenches that are related with AEC workflow. New features in Draft, Sketch and TechDraw workbenches are also worth checking out. Also, you might be interested in the Macro that creates automatic light-gauge steel frame and the new Arch Texture module that powers up your model visualization.

More reading:

- FreeCAD 0.19 has been released. Full release notes [here](https://wiki.freecadweb.org/Release_notes_0.19).
- [Download](https://www.freecadweb.org/) the new release.
- News about the BIM/Arch workbench for Freecad, see Yorik's [blog](http://yorik.uncreated.net/blog/freecad).
