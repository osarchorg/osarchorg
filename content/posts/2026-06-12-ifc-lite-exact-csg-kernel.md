---
title: "IFClite ships one pure-Rust exact CSG kernel across native and WASM"
date: "2026-06-12 09:00:00"
lastmod: "2026-06-12 09:00:00"
slug: "ifc-lite-exact-csg-kernel"
draft: false
author: "Louis Trümpler"
description: "IFClite has merged a clean-room exact-arithmetic mesh-arrangement CSG kernel that replaces separate Manifold (browser) and BSP (server) backends, giving bit-identical boolean output on x86_64, aarch64, and wasm32."
tags: ["IFClite", "IfcOpenShell", "Construction", "Structure"]
---

[IFClite has merged PR #1024](https://github.com/LTplus-AG/ifc-lite/pull/1024), replacing its two boolean backends with a single pure-Rust exact CSG kernel. The browser build previously relied on the C++ Manifold library via WASM cross-compilation; the native server path used an in-tree BSP port. Both are gone. The new kernel is a clean-room mesh-arrangement implementation: operand meshes are intersected conformingly (shared symbolic vertices for line-plane and triple-plane intersection points), re-triangulated under exact predicates, then classified for difference, union, or intersection. Every topology decision routes through a predicate cascade (interval filter, fixed-width tier, `BigRational` oracle) built on Shewchuk adaptive predicates for explicit coordinates and Cherchi-style indirect predicates (Attene 2020) for implicit intersection geometry. The public API (`processGeometryBatch`, SDK surface) is unchanged; consumers see different triangulations wherever booleans fire.

For IFC geometry this matters at the places export models actually stress boolean kernels. Wall openings (`IfcRelVoidsElement`), solid-solid `IfcBooleanResult` chains, and deep `IfcBooleanClippingResult` stacks (Tekla flush recesses, tilted `IfcPolygonalBoundedHalfSpace` cutters, segmented roof clips) now run through the same code on every target. Coplanar host and cutter faces, which previously needed perturbation epsilons or produced boundary cracks and seam slivers, are handled on an exact coplanar path. Multiple void cutters in one host can be unioned and subtracted in a single arrangement instead of sequential clipping that accumulated error. Regression tests pin volume invariants against the former Manifold oracle and enforce a cross-platform predicate fingerprint (verified on x86_64, aarch64, and wasm32; CI includes a weekly ARM64 determinism check).

The build simplification is equally significant for contributors: WASM no longer needs the LLVM 20 / libc++ / emsdk toolchain that Manifold required. Native and browser builds are pure Rust end to end. `geomHash` values for boolean-cut elements will change relative to prior releases because triangulation topology improves; in-session compare flows are unaffected because both sides hash with the same kernel. See the [IFClite project site](https://ifclite.dev/) and the [pull request](https://github.com/LTplus-AG/ifc-lite/pull/1024) for more details.
