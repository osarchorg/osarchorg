---
title: "Blender 5.3 released with native 3D Gaussian splat support"
date: "2026-11-23 00:00:00"
lastmod: "2026-11-23 00:00:00"
slug: "blender-5-3-released"
draft: true
author: "Moult"
description: "Blender 5.3 adds native 3D Gaussian splat import, asset libraries shared as extensions, custom Outliner sorting, and Vulkan as the default backend on Windows and Linux."
tags: ["Blender", "Architecture"]
cover:
  image: "/uploads/2026/11/blender-5-3-release-splash.webp"
  alt: "Blender 5.3 splash artwork by Blender Studio showing two animal characters from the Overgrown teaser"
  hiddenInSingle: false
  hiddenInList: false
---
[Blender 5.3](https://www.blender.org/press/blender-5-3-release/) was released on 10 November 2026. Its headline feature is native support for 3D Gaussian splats, which can be imported from PLY and SPZ files as point clouds, edited and processed with Geometry Nodes, and relit and rendered in Workbench, EEVEE and Cycles.

Asset libraries can now be shared as extensions, and the Blender Extensions platform accepts asset libraries containing public domain (CC0) assets. The Outliner allows objects to be arranged with custom sorting, and an optional project system makes Blender aware of context beyond the open `.blend` file. Vulkan is now the default graphics backend on Windows (except ARM) and Linux, with lower minimum requirements.

Other changes include dispersion and anisotropic roughness for glass in Cycles, panoramic cameras in EEVEE, new volume grid nodes in Geometry Nodes, and ripple editing and initial OpenTimelineIO support in the Video Sequencer. For AEC users, Gaussian splat import brings reality capture data such as site and building scans into Blender alongside models, and shared asset libraries offer a way to distribute office content. See the [full release notes](https://developer.blender.org/docs/release_notes/5.3/) for details.
