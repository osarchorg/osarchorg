---
title: "Whitepaper published on Native IFC methodologies"
date: "2022-10-15 12:38:00"
lastmod: "2022-10-10 09:41:04"
slug: "whitepaper-published-on-native-ifc-methodologies"
draft: false
author: "Moult"
description: "A new whitepaper has been published on Native IFC methodologies, authored by Bruno Postle, developer of Native IFC software Homemaker, and co-authored by Thomas Krijnen and Dion Moult, developers of Native IFC libraries and interfaces. The "
tags: ["Bonsai", "ThatOpenPlatform", "Architecture", "Structure", "Services", "Construction"]
wordpress_id: 3310
wordpress_guid: "https://osarch.org/?p=3310"
cover:
  image: "/uploads/2022/09/whitepaper-published-on-native-ifc-methodologies.png"
  alt: "Whitepaper published on Native IFC methodologies"
  hiddenInSingle: false
  hiddenInList: false
---
A new whitepaper has been published on Native IFC methodologies, authored by Bruno Postle, developer of Native IFC software Homemaker, and co-authored by Thomas Krijnen and Dion Moult, developers of Native IFC libraries and interfaces. The whitepaper helps define Native IFC, and how applications can collaborate in a decentralised, distributed manner.

Bruno Postle writes:

After an eternity of stagnation where nothing seemed to change from one year to the next, the world of BIM is suddenly moving very fast. With Open-Source tools such as IFC.js and BlenderBIM throwing up new features and applications seemingly every week, it is hard to keep up – even for those of us who make it our business to track these things.

Finally, here in 2022, we are witnessing an explosion of new possibilities, of new ways of working.

Aside from being free to use, modify and redistribute, and free for others to build new applications on top, what links this new class of tool is what we call Native IFC authoring.

IFC is both a classification schema, a list of defined names so that we can all agree on what a door is, and it is a file format for BIM models. As a classification schema, IFC is the only game in town, even technologies such as COBie use IFC as a foundation.

You may also be familiar with IFC files as a way of not very successfully exporting and importing BIM models between different software; but IFC is much more than this – from the start IFC files were designed to be your primary store of BIM data.

! Native IFC modeling demonstration where distributed material changes were merged with a base model

Native IFC Applications that work with IFC files directly can access data very efficiently. A small alteration changes just a small part of the file, this means that we can use other Open-Source technologies to track our changes as we work, retrieving older versions instantly without consuming vast amounts of storage. More than that, the same tools allow us to ‘fork and merge’ BIM data, letting multiple users to work on copies of the same model, merging changes as we go – all using free tools that won’t get discontinued or priced out of reach, producing normal IFC files that can be imported into any old application that supports IFC.

Want to know more? These new ways of working are set out in this Native IFC Whitepaper: <https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst>
