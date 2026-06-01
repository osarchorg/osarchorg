---
title: "Funding for a GIT/IFC Interface in BlenderBIM."
date: "2023-03-27 17:46:58"
lastmod: "2023-03-29 19:39:00"
slug: "funding-for-a-git-ifc-interface-in-blenderbim"
draft: false
author: "theoryshaw"
description: "Imagine GIT for IFC files. That is, imagine a tool that keeps track of changes to an IFC file over the duration of a design project--a tool that allows branching or forking of different design options from a distributed team, and tool that "
tags: ["Bonsai", "FreeCAD", "Architecture", "Structure", "Services", "Construction"]
wordpress_id: 5835
wordpress_guid: "https://osarch.org/?p=5835"
cover:
  image: "/uploads/2023/03/funding-for-a-git-ifc-interface-in-blenderbim.jpg"
  alt: "Funding for a GIT/IFC Interface in BlenderBIM."
  hiddenInSingle: false
  hiddenInList: false
---
Imagine GIT for IFC files.

That is, imagine a tool that keeps track of changes to an IFC file over the duration of a design project--a tool that allows branching or forking of different design options from a distributed team, and tool that can asynchronously merge these revisions together.

[Bruno Postle](https://community.osarch.org/profile/brunopostle) has created the seeds of such a tool--an IFC/GIT interface inside BlenderBIM.

Code base here: <https://github.com/brunopostle/ifc-git>

https://www.youtube.com/embed/-Y5-LR4oik8

Funding for this project will go toward further refinement of the tool, as well as additional functionality such as visual diffing and atomized conflict resolution--as reflected in the following mock up.

https://www.youtube.com/embed/EYqT5EceA_g

Please note, however, this tool will only work on IFC files that were created using a NativeIFC approach. That is, tools that do not rewrite the entire IFC file when exported, but instead only change the portion of the IFC file that was modified at any one commit. Currently only [BlenderBIM](https://blenderbim.org/) and [FreeCAD](https://www.freecad.org/) provide NativeIFC support. See the [NativeIFC white paper](https://github.com/brunopostle/ifcmerge/blob/main/docs/whitepaper.rst) for a more nuanced description.

Since this project [won the most community votes](https://community.osarch.org/discussion/comment/13682/#Comment_13682) as a project OSArch should center a funding campaign around, OSArch will use their current funds to match any outside funding, up to $1000.

Not only is this a call for funding this project, it is also a general call for any developers that might be interested to help extend what Bruno has started already. It is our hope that these funds could help bring on additional developers. If you'd like to help, please [create an issue](https://github.com/brunopostle/ifc-git) on the repo to share your thoughts and proposed intentions.

[To Fund Project](https://opencollective.com/osarch/projects/git_ifc)
