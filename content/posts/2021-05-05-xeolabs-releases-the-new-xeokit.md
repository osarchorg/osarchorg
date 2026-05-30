---
title: "Xeolabs releases the new xeokit 1.8 3D graphics SDK."
date: "2021-05-05 14:24:09"
lastmod: "2021-05-05 22:42:41"
slug: "xeolabs-releases-the-new-xeokit"
draft: false
author: "Bruno Perdigao"
description: "Xeokit is an open source 3D graphics SDK for BIM development. They have recently released the new xeokit 1.8 with rendering improvements"
categories: ["All Disciplines"]
tags: ["Xeokit"]
wordpress_id: 666
wordpress_guid: "https://osarch.org/?p=666"
cover:
  image: "/uploads/2021/05/xeolabs-releases-the-new-xeokit.png"
  alt: "Xeolabs releases the new xeokit 1.8 3D graphics SDK."
  hiddenInSingle: false
  hiddenInList: false
---
Xeokit is an open source 3D graphics SDK for AEC and BIM development. It is provided by xeolabs which is a company specialized in providing graphics software for web-based BIM, Engineering and Medicine. They have recently released the new xeokit 1.8 version with a lot of rendering improvements.

With xeokit you have another option to display your models in any browser. It is production ready and used by a lot of companies. It also works in all major browsers. The BIM IFC viewer were developed in collaboration with Open Project team, and it is the viewer used by the [Open Project BIM](https://www.openproject.org/bim-project-management/) version. But you can also use it separately and load it in your own server, without the need of external cloud services and keeping your data safe.

Xeokit BIM viewer comes with a lot of interesting features. It has a variety of options for navigation, distance and angle measurement, annotation and BFC viewpoints for collaboration.

One of the highlights of this new release is that they implemented Percy for automated visual testing. This works by running tests every time someone sends a pull request to the project repository. That way, the PR will have a fast feedback and will reduce the time for PR reviews while maintaining the security.

The other highlights are rendering related. They use SAO (scalable ambient obscurance) that helps with the visualizations of edges and narrow openings. In this new version it shows improvement in performance, output quality and more control options. They also improved Edge Enhancement - the edges colors are now related to the mesh material - and the Backface Rendering now shows backfaces on non-solid triangles. In addition, they have added a plugin called FastNavPlugin, that automatically disables some rendering effects while moving the camera. This allows for a faster navigation while panning and orbiting.

In case you want to see how each of these rendering improvements affects visualization, there are a few examples on their release note pages. Also, the new xeokit 1.8 is already running in the xeokit BIM Viewer 2.1.0, which means you can test all these new features. Give it a try [here](http://xeokit.io/demo.html?projectId=OTCConferenceCenter&tab=storeys).

Related links:

- Full [release notes](https://www.notion.so/What-s-New-in-xeokit-1-8-09fb370ddbf44413afed5687d5c01549).
- xeokit official [website](https://xeokit.io/).
- Visit the xeokit [examples page](https://xeokit.github.io/xeokit-sdk/examples/) to see how it works in practice.
