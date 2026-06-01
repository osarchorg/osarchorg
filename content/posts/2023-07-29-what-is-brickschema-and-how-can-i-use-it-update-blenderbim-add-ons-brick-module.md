---
title: "What is Brickschema and how can I use it? Update: BlenderBIM Add-on's Brick module."
date: "2023-07-29 06:49:17"
lastmod: "2023-07-29 06:57:12"
slug: "what-is-brickschema-and-how-can-i-use-it-update-blenderbim-add-ons-brick-module"
draft: false
author: "Riley Wong"
description: "For the past 8 weeks, I've been working on the BlenderBIM Add-on's Brickschema authoring module as part of the Google Summer of Code Program . I’m pretty new to the schema, but I’ve learned a lot about its usage and implications! I’ve liste"
tags: ["Bonsai", "Architecture", "Structure", "Services", "Construction", "Operations"]
wordpress_id: 6662
wordpress_guid: "https://osarch.org/?p=6662"
cover:
  image: "/uploads/2023/07/what-is-brickschema-and-how-can-i-use-it-update-blenderbim-add-ons-brick-module-logo-1b8337e-17fbd11f6373a10ee.png"
  alt: "What is Brickschema and how can I use it? Update: BlenderBIM Add-on's Brick module."
  hiddenInSingle: false
  hiddenInList: false
---
For the past 8 weeks, I've been working on the BlenderBIM Add-on's Brickschema authoring module as part of the [Google Summer of Code Program](https://osarch.org/2023/03/09/google-summer-of-code-2023-starting-soon/). I’m pretty new to the schema, but I’ve learned a lot about its usage and implications!

I’ve listed some resources that have helped me familiarize myself with the ontology below:

- <https://wiki.osarch.org/index.php?title=Brick_Schema>
- <https://groups.google.com/g/brickschema>
- <https://brickschema.org/>
- <https://www.esmagazine.com/articles/101566-how-brick-schema-defines-the-digital-landscape-of-smart-buildings>
- <https://www.youtube.com/watch?v=5w3uu_vevCA>
- <https://www.youtube.com/watch?v=hetd6cIKueA>
- <https://itc.scix.net/pdfs/w78-2021-paper-037.pdf>
- <https://brickschema.readthedocs.io/en/latest/index.html>
- <https://github.com/BrickSchema>

!

Brick is a semantic structure and ontology designed to represent the relationships between building services. Compared to IFC’s generic descriptions for some smart building equipment relations, Brick is a format that is more scalable, fine-tuned, and targeted. Specifically, Brickschema targets building automation and control systems. Demonstrated in the images above and below, Brick’s standardized framework for describing building components and behaviors includes sensors, systems, locations, and more.

!

Brick is open-source under the BSD license, which makes it the perfect option to integrate with other open-source applications. In regards to the BlenderBIM Add-on’s mission to cover full building lifecycles, Brick will contribute to enhancing its facility management features. In fact, Brick is largely complementary to IFC, so combining the Add-on’s native IFC authoring tools and Brickschema will prove particularly crucial in enriching the standard exchange of BIM. Here, Brick helps to interface with smart sensor time-series databases, large interconnected equipment graphs, and the machine-readable formatting of building data.

!

Currently, in the BlenderBIM Add-on, most of the basic features necessary for authoring Brick models are implemented. This includes adding/removing Brick entities in a project, prefixing entities with custom namespaces to identify them, and (most complicated of all) adding/removing relationships between the entities. Meanwhile, other quality-of-life features have been implemented such as undo/redo and hierarchy options for viewing a Brick graph. There are still more features to come, and community feedback and support will prove crucial in turning the module into a practical utility!

!

Brick has far-reaching implications for the industry as a whole. For one, Brick universalizes the building management workflow whilst many industry building systems remain unstructured and non-standardized, often using new systems designed only once for a particular building. With Brick's focus on portability and standardization, the logic for analyzing a Brick building's system can be applied to multiple sites. Furthermore, Brick enables efficient data integration, analytics, and interoperability which helps to better design IoT applications. This in turn helps with calculating richer building diagnostics, meeting sustainability goals, and improving budgeting accuracy.

Stay tuned as the Brick module continues to develop!
