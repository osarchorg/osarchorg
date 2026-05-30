---
title: "New Tissue for Blender 2.91 add-on v0.3.48 released"
date: "2020-12-02 12:54:25"
lastmod: "2020-12-02 12:54:27"
slug: "new-tissue-for-blender-2-91-add-on-v0-3-48-released"
draft: false
author: "Bruno Perdigao"
description: "Alessandro Zomparelli just released a new version of his Tissue for Blender add-on featuring the new Convert to Curve tool.."
categories: ["All Disciplines", "Architecture"]
tags: ["Tissue", "Blender", "Architecture"]
wordpress_id: 131
wordpress_guid: "https://osarch.org/?p=131"
cover:
  image: "/uploads/2020/12/new-tissue-for-blender-2-91-add-on-v0-3-48-released.jpg"
  alt: "New Tissue for Blender 2.91 add-on v0.3.48 released"
  hiddenInSingle: false
  hiddenInList: false
---
Alessandro Zomparelli just released a new version of his Tissue for Blender add-on. Tissue v.0.3.48 is now available for Blender 2.91 and features a new tool and a few fixes.

Tissue is an add-on for computational design in Blender developed by Co-de-iT. With this add-on, you can easily create tessellations based on a mesh and get creative. All you have to do is make a component object that will be repeated over the faces of a base object. It has a straight-forward workflow that allows you to explore several possibilities of complex shapes in a quick way.

This release brings the Convert to Curve tool that can detect the edges of a mesh and convert them to curves. It has three different Conversion Modes and supports three different types of curves: polyline, bezier and nurbs.

Let's look at an example to understand how Tissue can be used in an architecture workflow. For a facade design, you can create the overall shape of the building with a simple subdivided mesh. It will work as the base object. Then you model the panel to work as the component object. The Tessellate tool will create copies of the panel over every face of the subdivided mesh and adapt it to the shape of the face, composing your facade.

It is easy to edit your result by changing the base mesh and pressing the update button. In addition, there are also a few options that you can tweak and refresh to get better results. After that, you can create the curves from the mesh using the Convert to Curve and use them to model beams or mullions to add more detail to your facade design.

Regarding computational design, Tissue is more accessible to those that doesn't necessarily want to use code or node based workflow. You can combine the Tessellate and Convert to Curve tools to create useful solutions for architects in a variety of approaches.

More reading:

- Tissue [official website.](http://www.co-de-it.com/wordpress/code/blender-tissue)
- A [video tutorial](https://www.youtube.com/watch?v=fagGK8jYTJo&t) by Dimitar on using Tissue for architecture.
- Check out their [discussion group](https://www.facebook.com/groups/1396995897211561)
- [Support](https://www.patreon.com/alessandrozomparelli) this add-on's development!
