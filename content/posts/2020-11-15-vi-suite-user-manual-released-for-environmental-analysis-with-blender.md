---
title: "VI-Suite user manual released for environmental analysis with Blender"
date: "2020-11-15 06:54:00"
lastmod: "2020-11-28 09:55:01"
slug: "vi-suite-user-manual-released-for-environmental-analysis-with-blender"
draft: false
author: "Moult"
description: "The VI-Suite user manual has been released and is now available on the documentation page on the website. The VI-Suite is an open-source add-on to the 3D modelling and animation package Blender. It provides a set of tools for the analysis o"
categories: ["All Disciplines"]
tags: ["VI-Suite", "Blender", "Radiance", "EnergyPlus", "OpenFOAM", "Services", "Sustainability"]
wordpress_id: 75
wordpress_guid: "https://osarch.org/?p=75"
cover:
  image: "/uploads/2020/11/vi-suite-user-manual-released-for-environmental-analysis-with-blender-flovi1.png"
  alt: "VI-Suite user manual released for environmental analysis with Blender"
  hiddenInSingle: false
  hiddenInList: false
---
The VI-Suite user manual has been released and is now available on the documentation page on the website.

The VI-Suite is an open-source add-on to the 3D modelling and animation package Blender. It provides a set of tools for the analysis of environmental factors within and around buildings. It uses Blender’s node system to provide a user interface that allows quick and custom analyses to be created.

As of VI-Suite version 0.6 nodes exist for GIS height map import, sun path analysis, wind rose display, shadow and sky view factor studies, lighting metric prediction, energy performance with advanced airflow network creation and flow analysis with computational fluid dynamics (Linux only).

The lighting, energy and flow analyses are achieved with the three main VI-Suite components:

  1. LiVi, which acts as a pre/post-processor for the Radiance lighting simulation suite (version 5.3)
  2. EnVi, which does the same for the EnergyPlus thermal simulation engine (version 9.3)
  3. FloVi, which interfaces with the OpenFOAM CFD suite


VI-Suite is currently the most mature interface for building physics available only using free software. It is available for Linux, Windows and OS X.

The new user manual is a 59 page PDF that starts from the basics of installation and goes through each node. For each node, there is an image of the node as well as a description of how it works, and documentation for each property.

The documentation is suitable for beginners to Blender, but assumes some domain knowledge about building physics and running simulations for lighting, energy, and CFD.

VI-Suite v0.6 is by no means bug free, but bug reports are welcome and can be made at the Github page.

The author, Dr Ryan Southall, is working on video tutorials.

More reading:

- Read the new [VI-Suite v0.6 user manual](http://blogs.brighton.ac.uk/visuite/documentation/)
- Report bugs at the [Github site](https://github.com/rgsouthall/vi-suite06).
- [Start using the VI-Suite](http://blogs.brighton.ac.uk/visuite/) today!
