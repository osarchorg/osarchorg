---
title: "New BlenderBIM Add-on release v0.0.201207"
date: "2020-12-08 07:45:28"
lastmod: "2020-12-08 08:26:15"
slug: "new-blenderbim-add-on-release-v0-0-201207"
draft: false
author: "Moult"
description: "The BlenderBIM Add-on release v0.0.201207 include improved IFC round-tripping, and stabilisation of the new material system."
tags: ["Bonsai", "Blender", "Architecture", "Structure", "Services", "Construction"]
wordpress_id: 172
wordpress_guid: "https://osarch.org/?p=172"
cover:
  image: "/uploads/2020/12/new-blenderbim-add-on-release-v0-0.png"
  alt: "New BlenderBIM Add-on release v0.0.201207"
  hiddenInSingle: false
  hiddenInList: false
---
There’s been a new BlenderBIM Add-on release! The BlenderBIM Add-on **v0.0.201207** comes with 50 new features and fixes. The BlenderBIM Add-on is 100% free and open source software that lets you author and document BIM data fully to ISO standards. Highlights include drastically improved material, geometry, and context IFC round-tripping, and stabilisation of the new material system.

Image credits go to the [Opening Design Aalseth Residence team](https://github.com/OpeningDesign/Aalseth_Residence) - available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

In this release, the focus has been on improving the ability to round-trip IFC data. Historically, many proprietary software have treated IFC as a transport format, usually for read-only view between applications. The native proprietary format remained as the primary source of truth. This mentality has led to the data quality in IFC being relatively poor.

With the improved ability to round-trip IFC data, this allows IFC to replace the native file format and be used as the primary source of truth. IFC can change from being seen as a transport method to a database where all BIM applications can connect to.

The improvements in round-tripping fall into three categories. The first is the ability to round-trip parametric geometry. IFC has the ability to store parametric geometry of all sorts of shapes. Building support for these shapes is complex, as often they do not directly map to parametric objects in existing authoring software. This results in loss of parametric geometry editing. This new BlenderBIM Add-on release now includes an experimental "native round-trip" mode which allows Blender to store a link to the original parametric IFC definition. Despite Blender being mesh-based, this allows Blender to modify IFC solids, CSGs, and parametric geometry without any loss in data. The user has the ability to bake parametric geometry to meshes if they wish, as Blender is exceptional in its ability to edit meshes, far surpassing proprietary applications in this regard.

The second is the ability to round-trip representation contexts. IFC allows an object to contain multiple representations. One representation might be the 3D geometry of its body, and another might be the 2D geometry of its annotation in a plan view, or section view. As you can see, this can be quite specific. This new release will preserve all representations upon import and export with no data loss, assuming the "native round-trip" mode is enabled.

Finally is the ability to migrate across different IFC schemas. The BlenderBIM Add-on tries to encourage production of IFC4 data, but this can lead to complications if users wish to upgrade or downgrade IFC datasets. A new built-in migration utility allows the BlenderBIM Add-on to gracefully convert between schemas, whilst retaining IFC data as much as possible.

These three round-tripping capabilities are unique in the industry and are a great demonstration of where free and open-source software far surpasses proprietary solutions.

See more reading on this new BlenderBIM Add-on release:

- See the [full release notes](https://community.osarch.org/discussion/comment/4349/#Comment_4349).
- Learn more on the [BlenderBIM Add-on Wiki page](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on).
- Get the new [BlenderBIM Add-on release](https://blenderbim.org/) today!
