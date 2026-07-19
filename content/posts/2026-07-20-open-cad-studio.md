---
title: "Open CAD Studio develops native DWG and DXF support in an open source CAD application"
date: "2026-07-20 08:27:45"
lastmod: "2026-07-20 08:27:45"
slug: "open-cad-studio"
draft: false
author: "Moult"
description: "Open CAD Studio is a GPL-licensed 2D and 3D CAD application written in Rust with native DWG and DXF reading and writing."
tags: ["Open CAD Studio", "Architecture", "Construction", "Structure"]
cover:
  image: "/uploads/2026/07/open-cad-studio.jpg"
  alt: "Open CAD Studio displaying a detailed infrastructure drawing"
  hiddenInSingle: false
  hiddenInList: false
---

[Open CAD Studio](https://github.com/HakanSeven12/OpenCADStudio) is a GPL-3.0-licensed 2D drafting and 3D modelling application written in Rust. Its central goal is native reading and writing of DWG and DXF files from R13 through R2018, without depending on proprietary CAD libraries or a separate conversion workflow.

The project includes familiar drafting, editing, snapping, annotation, dimensioning, block, XREF, paper-space, layout, plotting, and PDF export tools. Its 3D functionality covers primitives, extrude, revolve, loft, sweep, STEP and STL export, OBJ import, and tessellation of ACIS solid entities, with GPU-accelerated rendering through wgpu.

Open CAD Studio provides desktop builds for Windows, macOS, and Linux as well as a browser version, while remaining under active beta development. More details and downloads are available on the [OpenAEC project page](https://www.open-aec.com/open-cad-studio/), and the developer is answering implementation and interoperability questions in the [OSArch community discussion](https://community.osarch.org/discussion/3472/open-cad-studio-with-native-dwg-dxf-support).
