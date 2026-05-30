---
title: "Inkscape 1.2 released with major improvements in vector design"
date: "2022-05-19 03:50:18"
lastmod: "2022-05-19 03:50:21"
slug: "inkscape-1-2-released-with-major-improvements-in-vector-design"
draft: false
author: "Moult"
description: "Inkscape 1.2 has been released with major improvements for alignments, multipage documents, gradients, markers, and text flow."
categories: ["All Disciplines"]
tags: ["Inkscape"]
wordpress_id: 1528
wordpress_guid: "https://osarch.org/?p=1528"
cover:
  image: "/uploads/2022/05/inkscape-1-2-released-with-major-improvements-in-vector-design.png"
  alt: "Inkscape 1.2 released with major improvements in vector design"
  hiddenInSingle: false
  hiddenInList: false
---
Inkscape 1.2 is the leading open source vector design program. Based on the SVG open standard, it has applications in AEC from early concept stage architectural design, sheet and technical drawing layouting, creating client presentations, PDF editing, and general graphic design for signage, design concepts, and fabricated textures on facades, panels, and coverings.

The developers have been extra busy and this release includes a number of game-changing new features in addition to about 80 major bugfixes and many more minor ones. The 5 most relevant to AEC are listed below.

All images have been taken from the official Inkscape website and release notes, linked at the end of this article.

## Multi-page documents now supported

Inkscape now has a new page tool which allows multiple pages of same or different sizes in the same document. Pages can then be used to export to a multi-page PDF. Objects can move from one page to another, pages can be labeled, added, and removed.

Note that pages are not a native SVG concept, so this behaviour is unique to Inkscape. Other SVG viewers will only see the first page in an Inkscape document, which correlates to the viewbox area of your SVG data.

!

## Alignment and distribution snapping

The alignment and distribution interface has been improved to make it clearer to new users on how to align and distribution items, with all the alignment options now merged into a single dialog. The best part is the new snapping menu which changes the snap options for a toolbar of 20 or so icons into a clear menu using snapping text jargon that users will recognise, like edges, corners, midpoints, centers, and so on.

Even better than the interface changes is the new on-canvas alignment. Just like proprietary software such as Adobe Illustrator or InDesign, snapping now occurs while dragging objects on the canvas itself, with hotspots and tooltips popping up to guide alignments and equal distributions between objects. This makes doing page layouts and presentations significantly much more user friendly.

!

## Text flow, padding inside shapes, and markers

Architects occasionally have to prepare presentation panels which include text columns and labels. Text editing in Inkscape previously did not lend itself well to encasing text in boxed frames the way Adobe InDesign does, but the new features in Inkscape make it much easier to create text layouts alongside the graphic designs.

When text is flowed into a shape, there is now a handle that lets you adjust the internal padding with that shape. This means you can use rectangles for text columns or box labels and the padding can be adjusted. You can then set an exclusion zone for text to flow around one or more other objects, such as images or features which overlap with the text column. This feature makes use of the new SVG shape-padding and shape-subtract features

Markers are a bit of a niche feature but are increasingly used (such as in the BlenderBIM Add-on and IfcOpenShell) for customising arrowheads, or architectural dimension ticks, datum marks, section markers, and other annotative markers. Markers can now be previewed, scaled, direction changed, offset, or edited directly on the canvas. For those generating drawings with IfcOpenShell, this is a great way to visually modify annotation symbols!

!

## Layers and object dialog

A new dialog merges the layers and objects into a hierarchical tree similar to what users may be used to in other design software. This makes it easy to see the entire structure of objects including names, visibility, locks, and masks. Layers and objects can be multi selected for bulk operations, as well as to isolate elements or affect all elements excluding an active selection.

!

## Improved gradient editing

If you've ever tried to work out how editing gradients work in Inkscape for any purpose whatsoever, you'd love the new updates to the gradient editor. The fill and stroke dialog now has gradient editing built in: this means you can add, remove, and slide the position of colour stops in one location.

!

- [Visit the official Inkscape website](https://inkscape.org/)
- [Read the Inkscape 1.2 release announcement](https://inkscape.org/release/inkscape-1.2/)
- [Read the Inkscape 1.2 release notes](https://media.inkscape.org/media/doc/release_notes/1.2/Inkscape_1.2.html)
- [Watch the Inkscape 1.2 release video trailer](https://www.youtube.com/watch?v=1U4hVbvRr_g)
- [Visit the Inkscape page on the OSArch Wiki](https://wiki.osarch.org/index.php?title=Inkscape)
