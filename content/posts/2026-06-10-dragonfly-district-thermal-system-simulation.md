---
title: "Dragonfly adds district thermal system simulation workflows"
date: "2026-06-10 00:00:00"
lastmod: "2026-06-10 00:00:00"
slug: "dragonfly-district-thermal-system-simulation"
draft: false
author: "Moult"
description: "Ladybug Tools has added Dragonfly workflows for district thermal system simulation, including fourth- and fifth-generation district systems, OpenStudio/EnergyPlus models, and ground heat exchanger sizing."
tags: ["Ladybug Tools", "EnergyPlus", "Services", "Sustainability"]
cover:
  image: "/uploads/2026/06/dragonfly-district-thermal-system.png"
  alt: "Sample Dragonfly district thermal system with a ground heat exchanger"
  hiddenInSingle: false
  hiddenInList: false
---

[Ladybug Tools has announced new Dragonfly district thermal system simulation workflows](https://discourse.ladybug.tools/t/new-dragonfly-district-thermal-system-simulation/40428), developed through several years of collaboration with teams at the National Renewable Energy Laboratory, now the National Lab of the Rockies, around the [URBANopt SDK](https://docs.urbanopt.net/). The new Dragonfly District Thermal components are aimed at feasibility studies for fourth- and fifth-generation district energy systems.

The workflows set up OpenStudio/EnergyPlus models that can estimate energy savings for different district system configurations, forecast average loop temperatures, and support ground heat exchanger sizing for fifth-generation systems where land constraints matter. The update includes components for fourth-generation systems with heating and cooling plants, heat recovery chillers sized against simultaneous heating and cooling load overlap, fifth-generation ambient loop systems that move waste heat between buildings, and autosizing workflows for ground heat exchangers.

The components are available through the latest [Pollination Grasshopper/Rhino plugins installer](https://app.pollination.solutions/cad-plugins) or the [LB Versioner](https://docs.ladybug.tools/ladybug-primer/components/5_version/versioner). Ladybug Tools has also published a tutorial playlist and sample files in the [dragonfly-grasshopper repository](https://github.com/ladybug-tools/dragonfly-grasshopper/tree/master/samples), with the district system samples using the `des_` prefix.
