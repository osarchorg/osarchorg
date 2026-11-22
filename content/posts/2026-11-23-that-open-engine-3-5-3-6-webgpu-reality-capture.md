---
title: "That Open Engine 3.5 and 3.6 add WebGPU rendering, point clouds and Gaussian splats"
date: "2026-11-23 00:00:00"
lastmod: "2026-11-23 00:00:00"
slug: "that-open-engine-3-5-3-6-webgpu-reality-capture"
draft: true
author: "Moult"
description: "Versions 3.5 and 3.6 of That Open Engine's components add an opt-in WebGPU pipeline, a deferred renderer, point cloud and Gaussian splat loaders, adaptive resolution and IDS fixes."
tags: ["ThatOpenPlatform"]
cover:
  image: "/uploads/2026/11/that-open-engine-deferred-postproduction.webp"
  alt: "That Open Engine postproduction example showing a school building model rendered with the deferred pipeline beside a settings panel"
  hiddenInSingle: false
  hiddenInList: false
---
That Open Company released versions [3.5.0](https://github.com/ThatOpen/engine_components/releases/tag/v3.5.0) and [3.6.0](https://github.com/ThatOpen/engine_components/releases/tag/v3.6.0) of `@thatopen/components` and `@thatopen/components-front`, the libraries behind That Open Engine, on 22 October 2026. Both are minor releases whose new features are opt-in, with existing APIs and default behaviour unchanged.

Version 3.5 adds a deferred postproduction renderer and a WebGPU rendering pipeline, alongside the existing WebGL renderer, which remains the default. It also introduces reality capture components: a `PointCloudLoader` for Potree octrees, a `SplatLoader` for Gaussian splats, and converters for LAS, E57, Potree octree and splat tiling. Fixes include several IDS cases, covering entities without a PredefinedType, XML entities, type object property sets and properties without data.

Version 3.6 adds adaptive resolution, which lowers the postproduction resolution to hold a target frame rate, a lower resolution while the camera moves under WebGPU, a WebGPU pipeline cache, and a reworked outline pass. For developers of browser-based BIM tools, the releases allow point clouds and Gaussian splats from site capture to be displayed alongside models converted from IFC.
