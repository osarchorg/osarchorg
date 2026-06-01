---
title: "dotbim - minimalist file format for BIM"
date: "2022-02-26 06:38:14"
lastmod: "2022-02-26 06:38:54"
slug: "dotbim-minimalist-file-format-for-bim"
draft: false
author: "Moult"
description: "An open-source, accessible, simple, minimalistic file format for BIM called dotbim that will allow you to store geometry and data with it."
tags: ["dotbim"]
wordpress_id: 1034
wordpress_guid: "https://osarch.org/?p=1034"
cover:
  image: "/uploads/2022/02/dotbim-minimalist-file-format-for-bim.png"
  alt: "dotbim - minimalist file format for BIM"
  hiddenInSingle: false
  hiddenInList: false
---
Wojciech Radaczyński shares:

A few days ago there was a release of a open-source, accessible, simple, minimalistic file format for BIM called dotbim (.bim as an extension), that will allow you to store geometry and data with it. The obvious question could be: what difference does it make to the existing work-flows or file formats?

Dotbim was built with an idea of having whole documentation of it on 1 page only. It was made on purpose to make it as minimalistic and as simple and it possibly can be. Yet still it allows to transfer geometries and data attached. Such approach can make a huge difference for the developers of different software. You'd spent much less time on building parsers, importers, exporter, and other tools around it. Think of it as the "markdown" of BIM - the bare minimum, but just enough structure for your content.

!

Such limited number of features can also help to make sure that you can get all of them, not only some part of it, which is something that many exporters and importers do actually: they accept only some % of all of the features that file format provides. And even if it would be 90% of it, then they can add new features in a new version, or break the user space within new version. In dotbim the goal was to keep it simple and minimalist all the time.

!

Such approach obviously has it's own drawbacks: dotbim doesn't have large number of features in comparison to the existing solutions. So yes, it is limited, but yes: that's what makes it powerful.

The goal was to provide a simple alternative. For many tasks using other file formats is an absolute overkill, and that's where .bim files can come in handy.

- Check out the repository here: <https://github.com/paireks/dotbim>
- See the introduction video here: <https://www.youtube.com/watch?v=-bpWEdWcHvw>
- Python library: dotbimpy - <https://github.com/paireks/dotbimpy>
- Grasshopper plugin: dotbimGH - <https://github.com/paireks/dotbimGH>
- dotbim-ifc, converts to and from IFC and dotbim: <https://github.com/Moult/dotbim-ifc>, Author: Dion Moult
- Online 3d Viewer, supports.bim files and converts to other file formats: <https://3dviewer.net/>, Author: Viktor Kovacs
