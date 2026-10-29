# News publishing queue

Last reviewed: 30 October 2026. These posts are drafts, not scheduled publications.
The order below follows their draft dates and does not set a publishing priority.
Review each post and set its publication date when approving it for publication.

| Draft | Source |
| --- | --- |
| FreeCAD now runs in the browser through WebAssembly | [Read draft](content/posts/2026-07-27-freecad-webassembly-browser-port.md) |
| TopologicPy adds space syntax analysis in Python | [Read draft](content/posts/2026-10-20-topologicpy-space-syntax.md) |
| OpenSKP brings SketchUp import and export to Blender | [Read draft](content/posts/2026-10-20-blender-openskp.md) |
| OpenSeesPy framework compares concrete frame retrofit strategies | [Read draft](content/posts/2026-10-20-openseespy-concrete-frame-optimizer.md) |
| acadrust provides DWG and DXF file handling in Rust | [Read draft](content/posts/2026-10-20-acadrust-dwg-dxf-library.md) |
| IFCCAD explores an open drawing format built on IFCX | [Read draft](content/posts/2026-10-25-ifccad-open-cad-drawing-format.md) |
| BIMCraft develops a Rust BIM authoring application with IFC exchange | [Read draft](content/posts/2026-10-30-bimcraft-rust-bim-authoring.md) |

## Next newsletter

**8 of 10 new posts published. Send the next newsletter after any 2 more news
posts are published.** Drafts do not count, and the newsletter does not depend on
which two posts are selected from the queue.

The last issue included [FreeCAD announces three grants for Q2 2026](content/posts/2026-07-11-freecad-q2-2026-grants-announced.md)
(11 July 2026). The shared cutoff and ten-post target live in
[data/newsletter.toml](data/newsletter.toml).

Check the current count before preparing an issue:

```sh
python scripts/generate_newsletter.py --status
```

The command is authoritative if this snapshot is out of date. After publishing a
post, remove its row and update the count and review date here. After sending a
newsletter, update the cutoff to its newest included post, then refresh this
list's count. Generating newsletter files does not send an issue or move the
cutoff. See the [newsletter workflow](README.md#newsletter-schedule).

To preview drafts locally:

```sh
hugo server --buildDrafts
```
