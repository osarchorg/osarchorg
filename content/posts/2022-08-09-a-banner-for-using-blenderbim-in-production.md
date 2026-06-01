---
title: "A 'Banner' for Using BlenderBIM in Production"
date: "2022-08-09 21:37:50"
lastmod: "2022-08-09 21:37:53"
slug: "a-banner-for-using-blenderbim-in-production"
draft: false
author: "theoryshaw"
description: "OSArch has a new banner image! The BlenderBIM image is courtesy of a collaboration between Ioannis Christovasilis of Aether Engineering and Ryan Schultz of OpeningDesign. Read more about the project ..."
tags: ["Bonsai", "Blender", "FreeCAD", "Architecture", "Structure", "Services", "Construction"]
wordpress_id: 2460
wordpress_guid: "https://osarch.org/?p=2460"
cover:
  image: "/uploads/2022/08/a-banner-for-using-blenderbim-in-production-2.png"
  alt: "A 'Banner' for Using BlenderBIM in Production"
  hiddenInSingle: false
  hiddenInList: false
---
OSArch has a new banner image! The image is courtesy of a collaboration between Ioannis Christovasilis of [Aether Engineering](https://www.aethereng.com) and Ryan Schultz of [OpeningDesign](http://openingdesign.com/). These two companies are known for applying an open source approach to the AEC industry.

## A round-tripping IFC

The collaboration used [BlenderBIM](https://blenderbim.org/) to model an external three story porch for a multifamily project in Bryan, Texas, USA. Ioannis works from Italy, and Ryan works from the United States. BlenderBIM's native [IFC file(s)](https://hub.openingdesign.com/OpeningDesign/Marco_Polo/src/branch/master/Models%20and%20CAD/IFC) followed the sun as it was _roundtripped_ back and forth over the Atlantic.

Although 2D documentation functionality in BlenderBIM is steadily maturing, the plan for this project was to import the BlenderBIM IFC file into Revit to complete the documentation. This is similar to how OpeningDesign and OpeningDetail have worked in the past by round-tripping, via IFC, large scale details back and forth between FreeCAD, BlenderBIM, and Revit _(see illustrations below)_.

## Documentation is hard

Although their past experience modeling these isolated details in FreeCAD/BlenderBIM worked surprisingly well (and they will continue exploring this approach), modeling the balcony's larger scope, with so many repetitive parts, proved less efficient. For example Blender's collection instances did not survive the IFC roundtrip, instead the models objects lost too much data to accommodate design changes. For now they abandoned their intention to annotate the model in Revit. This was not necessarily a shortcoming of BlenderBIM, but was more related to the current IFC schema--a shortcoming they hope will be [addressed](https://github.com/buildingSMART/IFC4.4.x-development/issues/17) in the near future.

Having talked to the team, they will continue to explore round-tripping these large scale details, as the scope is more manageable when using BlenderBIM in its alpha state. They have high hopes for the future as the platform matures.

## Ways forward for distributed work

The team are especially excited to adopt [Bruno Postle's](https://twitter.com/brunopostle) new [IFCmerge](https://github.com/brunopostle/ifcmerge) tool in the future. This tool will allow distributed version and merge control of IFC files. Suddenly it will be possible for the team to work on the same model at the same time. The future is bright.

_This project, like most OpeningDesign's projects, is open source (Attribution-ShareAlike 4.0 International--CC BY-SA 4.0)--freely available to any party for future use, assuming the terms such as Attribution and ShareAlike are honored. The project files are located here:<https://hub.openingdesign.com/OpeningDesign/Marco_Polo>_

!These details were a collaboration with [Regis Tene](https://www.linkedin.com/in/regis-nde-tene/), [Maíra Zasso](https://twitter.com/mairocas), [Bruno Perdigão de Oliveira](https://www.linkedin.com/in/perdigao-bruno/), [Yorik van Havre](https://twitter.com/yorikvanhavre) and [Ryan Schultz](https://twitter.com/theoryshaw) ! ! ! !
