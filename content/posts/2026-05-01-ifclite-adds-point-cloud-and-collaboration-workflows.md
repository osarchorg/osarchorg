---
title: "IFClite adds point cloud and collaboration workflows"
date: "2026-05-01 06:28:46"
lastmod: "2026-05-02 09:54:14"
slug: "ifclite-adds-point-cloud-and-collaboration-workflows"
draft: false
author: "Louis Trümpler"
description: "IFClite is expanding from browser-native IFC viewing into point cloud workflows and real-time collaborative IFC editing in the browser."
tags: ["IFClite", "Architecture", "Structure", "Services", "Construction", "Operations"]
cover:
  image: "/uploads/2026/05/ifclite-point-cloud-openbim-workflow.jpg"
  alt: "IFClite point cloud and openBIM workflow demonstration"
  hiddenInSingle: false
  hiddenInList: false
---
[Louis Trümpler announced](https://www.linkedin.com/posts/louistrue_ifc-openbim-pointcloud-activity-7455865786197426176-HE2T) that point clouds are coming to [IFClite](https://ifclite.dev/) as part of the same browser-native openBIM workflow, rather than as a separate viewer or visual overlay. The first pass includes LAS / LAZ streaming, E57 / PLY / PCD readers, Web Worker decoding, WebGPU point rendering, colour modes for RGB, classification, intensity, height, and fixed colour, plus federation-aware point picking.

The goal is to load an IFC model and scan data together, then inspect, select, query, and eventually automate across both. That makes the work relevant to scan-to-BIM validation, as-built versus as-designed checks, existing condition review, browser-based progress inspection, and lightweight coordination without heavy desktop software.

A follow-up [LinkedIn post](https://www.linkedin.com/posts/louistrue_about-to-drop-a-bombshell-real-time-multiplayer-activity-7456279880155107329-Nt3-) teases real-time multiplayer on IFC in the browser: actual collaborative editing of the model itself, not a render stream. Together, these updates point to IFClite growing from a fast IFC viewer into a broader openBIM toolkit for browser-based model, scan, and collaboration workflows.
