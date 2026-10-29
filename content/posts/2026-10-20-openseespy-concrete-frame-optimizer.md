---
title: "OpenSeesPy framework compares concrete frame retrofit strategies"
date: "2026-10-20 00:00:00"
slug: "openseespy-concrete-frame-optimizer"
draft: true
author: "Moult"
description: "An OpenSeesPy research framework combines seismic assessment of concrete frames with shear-wall and jacketing retrofit comparisons and cost evaluation."
tags: ["OpenSeesPy", "Structure", "Construction"]
cover:
  image: "/uploads/2026/10/openseespy-concrete-frame.png"
  alt: "Two-storey, two-bay concrete frame with numbered nodes and members"
  hiddenInSingle: false
  hiddenInList: false
---
Giuseppe Carlo Marano and Arman Hajiha of Politecnico di Torino have shared an [OpenSeesPy-based research framework](https://github.com/ArtISte-Research-Group/OpenseesPy-concrete-2D-frame-optimizer-) for seismic assessment and retrofit optimization of existing reinforced-concrete frames. The project combines structural modelling, linear static and optional dynamic analysis, Eurocode-based member and drift checks, comparative costs and automated reporting.

The described optimization workflow compares complete interventions: candidate shear-wall layouts address excessive drift, then concrete jacketing strengthens beams and columns that remain deficient. Alternatives are reassessed against structural, detailing and constructability constraints, with lower-cost feasible strategies prioritised within the evaluated search space. Users can adjust unit costs and export ranked alternatives and analysis results.

Code and documentation are available through GitHub and the [Zenodo record](https://zenodo.org/records/22812754). The supplied beta_03 manual covers modelling and verification, reserving automated optimization for a subsequent volume. The framework targets research and preliminary comparison of two-dimensional frames, relying mainly on linear analysis; it does not represent full building torsion or nonlinear collapse behaviour. Illustration: frame geometry from the authors' manual, Figure 2.
