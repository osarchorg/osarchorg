---
title: "IFClite adds federated loading support"
date: "2026-01-28 07:44:40"
lastmod: "2026-01-28 07:44:40"
slug: "ifclite-adds-federated-loading-support"
draft: false
author: "Louis Trümpler"
description: "IFClite, a browser-native IFC viewer built with WebGPU and Rust/WASM, has added federated loading support for IFC4, IFC4X3, and IFC5 workflows."
tags: ["IFClite", "Architecture", "Structure", "Services", "Construction"]
cover:
  image: "/uploads/2026/01/ifclite-federated-loading-support.jpg"
  alt: "IFClite federated loading support demonstration"
  hiddenInSingle: false
  hiddenInList: false
---
[Louis Trümpler announced](https://www.linkedin.com/posts/louistrue_bim-openbim-ifc-activity-7422182816823635969-s16S) federated loading support in [IFClite](https://ifclite.dev/), a browser-native IFC viewer and toolkit built with WebGPU and Rust/WASM. For IFC4.3 and earlier workflows, federation means loading multiple IFC models side by side with collision-safe IDs, per-model visibility, unified spatial hierarchy handling, and selection across model boundaries.

The larger change is IFC5 support, where layered model composition can bring separate files together into a coherent model instead of simply displaying them alongside each other. That points toward workflows where base geometry, discipline additions, and property enrichment can live in separate files while still composing into one project view.

IFClite is open source under the MPL-2.0 license and supports IFC2X3, IFC4, IFC4X3, and IFC5, with WebGPU rendering and a small browser-delivered WASM core. See the [LinkedIn announcement](https://www.linkedin.com/posts/louistrue_bim-openbim-ifc-activity-7422182816823635969-s16S) and the [IFClite project site](https://ifclite.dev/) for more details.
