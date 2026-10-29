---
title: "BIMCraft develops a Rust BIM authoring application with IFC exchange"
date: "2026-10-30 00:00:00"
slug: "bimcraft-rust-bim-authoring"
draft: true
author: "Moult"
description: "BIMCraft is an early-stage Rust BIM application with building elements, drawings, schedules, IFC exchange and command-based automation through MCP and a CLI."
tags: ["BIMCraft", "Architecture", "Structure", "Services"]
cover:
  image: "/uploads/2026/10/bimcraft-desktop.webp"
  alt: "BIMCraft desktop interface showing an annotated sample house floor plan, properties and project browser"
  hiddenInSingle: false
  hiddenInList: false
---
[BIMCraft](https://github.com/IPedrax/BIMCraft) is a free software BIM authoring application written in Rust, with a desktop interface inspired by Revit workflows. Available under MIT or Apache-2.0, it models levels, walls, hosted doors and windows, floors, roofs, rooms and other building elements, with plans, sections, elevations, sheets and schedules derived from the model.

The project documents IFC2x3 and IFC4 import and IFC4 export, alongside PDF sheets, PNG views and SVG plans. Modelling actions are exposed as commands through a CLI and an MCP server, allowing automation tools to inspect, edit and render models. Its own parametric family format supports reusable components; it does not load Autodesk's `.rfa` families.

BIMCraft remains in early development. Packages target Windows, Linux and macOS, though the developer notes that the macOS app has not yet been manually tested. IFC coverage and other workflows continue to evolve. The [repository](https://github.com/IPedrax/BIMCraft) provides source code, sample projects, installation instructions and a feature-by-feature account of current support.
