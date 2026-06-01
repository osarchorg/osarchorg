---
title: "BabylonJS 5.0 release makes 3D web apps easier than ever"
date: "2022-05-28 06:39:34"
lastmod: "2022-05-28 06:39:37"
slug: "babylonjs-5-0-release-makes-3d-web-apps-easier-than-ever"
draft: false
author: "Moult"
description: "BabylonJS is an open source library to build 3D webapps. The 5.0 release includes WebGPU, cross platform native apps, performance profiler, GUI and more."
tags: ["BabylonJS"]
wordpress_id: 1643
wordpress_guid: "https://osarch.org/?p=1643"
cover:
  image: "/uploads/2022/05/babylonjs-5-0-release-makes-3d-web-apps-easier-than-ever-4.png"
  alt: "BabylonJS 5.0 release makes 3D web apps easier than ever"
  hiddenInSingle: false
  hiddenInList: false
---
BabylonJS is an open source web developer library to build rich 3D apps on the browser. The new version 5.0 release is one of the largest releases ever made for BabylonJS. This includes full support for WebGPU, the ability to build cross platform, web, and native apps, performance profiler, GUI editor, WebXR light estimation, node based materials, full glTF support, and more.

You might've heard of ThreeJS before, which is the web developer library that powers IFC.JS. BabylonJS is similar to ThreeJS, but differentiates itself by offering a structured framework to build 3D content, more akin to a game engine than the more granular approach by ThreeJS. Both libraries are mature and pack a lot of features, making the choice between them less clear cut. For beginners to web development who want to quickly get going with powerful visual tools, intuitive camera movements out of the box, and pretty visuals, BabylonJS is an excellent choice.

BabylonJS is not new to applications in AEC, being used in the open source Vi-sense prototype to display IoT sensor data alongside building plant rooms.

!

Being backed by Microsoft, BabylonJS isn't limited to prototypes. BabylonJS is mature open source software powering proprietary offerings like Microsoft Azure Digital Twins. With this foundation, it's a pretty safe bet to use it for your own digital twin, CDE, or online BIM viewer. Here's an example from Teia Solution, visualising a federated model BIM model broken down into disciplines, with the spatial tree shown and information callouts. This demo is available on the BabylonJS website.

!

As an equivalent of IFC.JS doesn't yet exist for BabylonJS, getting BIM data into BabylonJS takes a couple of steps. The first step is bringing in geometry. Supported 3D formats include OBJ and glb / glTF. Using the open source IfcConvert tool by IfcOpenShell, you can easily automate the conversion of IFC data into either OBJ or glb / glTF. For those not working with IFC, geometry can come in through the integration with Blender. For bringing in data, IfcConvert can convert IFC data into XML, or IfcJSON may convert IFC data into JSON, both of which can be extracted by JavaScript. Alternatively, tools like Speckle may help extract data from proprietary software.

Other inspiring examples available on the BabylonJS website include the College Room Planner by Target:

!College Room Planner by Target

... as well as this Apartment Configurator by Axeon Software.

!

What does the new version 5.0 release bring for AEC? Support for web GPU means more speed for beautiful textured models. Cross platform support means you can support native software, even on iPhone and Android. The performance profiler helps you scale up to the large models typical of the BIM world. The new GUI editor means that it's much more user friendly to prototype visual model interfaces, without getting stuck into the code.

- Visit the [BabylonJS website](https://www.babylonjs.com/)
- Watch the [BabylonJS release feature trailer video](https://www.youtube.com/watch?v=zELYw2qEUjI)
- Read the [BabylonJS 5.0 release notes](https://babylonjs.medium.com/babylon-js-5-0-beyond-the-stars-2d11d4c3d07)
- See the [demo BIM project by Teia Solution](http://microsoft.teia-solution.com/View3d/building)
- Check out the [College Room Planner by Target](https://www.target.com/room-planner/college)
- View the [Apartment Configurator by Axeon Software](http://www.axeon.fr/CLIENT/INFIME/Virtual_Staging_V2/)
