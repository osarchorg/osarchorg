---
title: "New BlenderBIM Add-on release v0.0.201115"
date: "2020-11-15 05:42:10"
lastmod: "2020-11-28 06:24:48"
slug: "new-blenderbim-add-on-release-v0-0-201115"
draft: false
author: "Moult"
description: "The BlenderBIM Add-on release v0.0.201115 comes with 52 new features and fixes, including improved materials, layers, geolocation, and vendor workarounds."
categories: ["All Disciplines"]
tags: ["Bonsai", "Blender", "Architecture", "Structure", "Services", "Construction"]
wordpress_id: 54
wordpress_guid: "https://osarch.org/?p=54"
cover:
  image: "/uploads/2020/11/new-blenderbim-add-on-release-v0-0.png"
  alt: "New BlenderBIM Add-on release v0.0.201115"
  hiddenInSingle: false
  hiddenInList: false
---
There's been a new BlenderBIM Add-on release! The BlenderBIM Add-on **v0.0.201115** comes with 52 new features and fixes. The BlenderBIM Add-on is 100% free and open source software that lets you author and document BIM data fully to ISO standards. Highlights include improved material and presentation layer support, improved geolocation support, and many more vendor workarounds.

We'll talk about our three favourite new features here!

An **improved IFC material UI** tops our list.

IFC materials are complicated, and though the BlenderBIM Add-on has always supported IFC materials and styles, the ability for the user to set them was never exposed explicitly in the user interface. Instead, the user had to set Blender material slots and choose between dropdowns that were difficult to discover.

Now, the new interface includes a dedicated IFC object materials panel! This panel shows whether the object has a single material, or a material set. Material sets are composite materials, that show layers, constituents, and profiles. This makes it really clear what materials are set on each IFC object.

Our second favourite is the new support for **IFC presentation layers**.

Did you know that IFC can store CAD layers? The new BlenderBIM Add-on release allows you to import and export these CAD layers, and see a list of layers. This allows you to integrate BIM data with existing CAD standards!

Our third favourite is the new **IFC inspector feature**.

If you've ever needed to check whether or not your IFC data is correctly stored, tucked away in the IFC Debug panel in the scene properties is the new IFC inspector feature. This lets you inspect any IFC object and dig through its IFC attributes (both direct and inverse).

Just like how the web inspector in a browser is vital for any web developer, this new feature in this BlenderBIM Add-on release is vital for any BIM developer, allowing them to debug and inspect IFC data without any processing.

See more reading on this new BlenderBIM Add-on release:

- See the [full release notes](https://community.osarch.org/discussion/comment/3842/#Comment_3842).
- Learn more on the [BlenderBIM Add-on Wiki page](https://wiki.osarch.org/index.php?title=BlenderBIM_Add-on).
- Get the new [BlenderBIM Add-on release](https://blenderbim.org/) today!
