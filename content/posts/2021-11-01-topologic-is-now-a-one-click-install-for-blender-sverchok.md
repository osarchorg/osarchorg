---
title: "Topologic is now a one-click install for Blender/Sverchok"
date: "2021-11-01 21:49:37"
lastmod: "2021-11-01 21:49:38"
slug: "topologic-is-now-a-one-click-install-for-blender-sverchok"
draft: false
author: "Moult"
description: "Topologic offers topological analysis of geometry in architecture. A new milestone release offers an easy install for Blender and Sverchok."
tags: ["Topologic", "Blender", "Sverchok", "Architecture"]
wordpress_id: 857
wordpress_guid: "https://osarch.org/?p=857"
cover:
  image: "/uploads/2021/11/topologic-is-now-a-one-click-install-for-blender-sverchok.jpg"
  alt: "Topologic is now a one-click install for Blender/Sverchok"
  hiddenInSingle: false
  hiddenInList: false
---
Topologic has a new milestone release! One of the biggest hurdles for testing and adopting Topologic has been its relative difficult installation. This was due to the particular method we used to create python bindings for the C++ code. To ease the installation process, we had to completely re-write the python bindings using pybind11. This was a laborious process, and bugs may still exist. However, this new release of Topologic can be installed for Blender with Sverchok just as any other add-on: You download the ZIP file (and you do NOT unzip it), you launch Blender (with Sverchok pre-installed), you go to Preferences -> Add-ons and you install the ZIP file as usual. This release of Topologic is compatible with both Windows and Linux and with python 3.7, 3.8, and 3.9.

This installation contains optional visual nodes that require additional python modules to be installed and accessible from Blender. Topologic will install fine without them and if they are found, it will add the additional nodes automatically. So if you wish to explore extra functionality such as importing IFC files, conducting energy analysis, and working with blockchain technologies, you must install the following python modules and make sure you can access them (import them) from within Blender. The instructions to do so are usually available online and you need to be comfortable with installing python modules:

  1. The newest developer version of BlenderBIM add-on will give you access to importing IFC files through ifcopenshell
  2. The openstudio python module will give you access to energy analysis nodes
  3. ipfshttpclient and web3 python modules will give you access to blockchain related nodes


Please note that this is still beta software. Please test and report any bugs to the issues tracker on Github.

You can download from two possible locations:

- [Download from the official Topologic website](https://topologic.app/) (head to software then download)
- [Download from Github](http://url1679.osarch.org/ls/click?upn=UrOwTl5X1kyRhQG0ubmtleO6Q4L8bEX5LSP-2BKq7oFvF7B8JYGVUxEADayXuY7osxU1KZju0g0tHKAFtwzBmWEQ-3D-3DW5ad_zvst3UFYdxqhjI5upLrmv6UQQeuTE3-2BDRBc-2BBMB3-2BBq3eRrn-2Fxx2aizQAqgiOLNQt1q9bzHVuwQNHCfyDv4c7OR-2FTYuv56W2s-2BRzLbuqOpH-2BIYzy7Y0PkNdy1r3DWvHTnPpRe8tclxLghCSlxGsZUmGyzGBG-2BDD4jP-2BX8JPr0EC2rACcO4NjyZrgW-2BS0cP5D9iJw-2BUyF3eRLHLzrJlabZA-3D-3D) (click on Releases then Assets)


This has been a long road and we still have a long way to go. I look forward to seeing what you will do with Topologic. Please post and tag [@topologicBIM](https://twitter.com/topologicBIM)!
