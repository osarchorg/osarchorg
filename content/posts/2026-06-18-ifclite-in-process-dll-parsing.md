---
title: "IFClite gets a native DLL for in-process IFC parsing in Rhino, Grasshopper, and Revit"
date: "2026-06-18 09:00:00"
lastmod: "2026-06-18 09:00:00"
slug: "ifclite-in-process-dll-parsing"
draft: false
author: "Louis Trümpler"
description: "A C FFI turns IFClite into a pure-Rust DLL that parses IFC in-process inside Rhino, Grasshopper, and Revit. Three functions, no server, no port."
tags: ["IFClite", "Architecture", "Structure", "Construction"]
cover:
  image: "/uploads/2026/06/ifclite-in-process-dll-parsing.jpg"
  alt: "IFClite.dll wiring Rhino, Grasshopper, and Revit to an IFC file in-process while an IT security dashboard stays quiet"
  hiddenInSingle: false
  hiddenInList: false
---

[IFClite merged PR #1182](https://github.com/LTplus-AG/ifc-lite/pull/1182), a contribution from Mathias Sønderskov Schaltz that lets IFClite parse IFC inside the CAD process — as a plain DLL.

The clean way to call a Rust engine from Grasshopper or Revit used to mean running a local server and talking to it over HTTP. But the moment something opens a port on a managed machine, enterprise IT lights up: firewall rules, security reviews, the whole dance. The FFI wires IFClite straight into the process instead. A new `ifc-lite-ffi` crate builds with `crate-type = ["cdylib"]` to `ifc_lite_ffi.dll`, and the host loads it like any other library. No server. No port. No network. Just a function call.

The surface is three `extern "C"` functions. `ifc_lite_parse` takes a UTF-8 path and writes back a heap buffer of JSON. `ifc_lite_parse_ex` adds one flag for opening handling — cut all voids, ignore every window and door, or keep only glazed ones. `ifc_lite_free` hands the buffer back to Rust. Rust allocates, the C# caller frees, exactly once. Failures come back as status codes, not exceptions: `0` ok, `1` bad pointer, `2` unreadable file, `3` parse panic, `4` serialization. The payload is IFClite's full `ParseResponse` — per-element meshes, schema metadata, stats, and site and building transforms.

The hard part is making it safe to embed. IFC geometry recurses deep: BSP-tree CSG and walls with hundreds of openings blow past the default ~1 MiB worker stack, and an overflow takes the host down with a bare `STACK_OVERFLOW` (0xC00000FD) that nothing can catch. So parsing runs in a dedicated rayon pool with 256 MiB stacks, wrapped in `catch_unwind` so a panic returns code `3` instead of killing Rhino. That only works if panics unwind, so the DLL must build with `--profile server-release`, which restores `panic = "unwind"`. Every panic also logs to `%TEMP%/ifc_lite_panic.log`.

The smoke tests followed in [PR #1183](https://github.com/LTplus-AG/ifc-lite/pull/1183), and `ifc-lite-ffi` now [ships on crates.io](https://github.com/LTplus-AG/ifc-lite/pull/1187) at v4.1.0 under MPL-2.0, ready to P/Invoke from a Grasshopper or Revit add-in. See the [pull request](https://github.com/LTplus-AG/ifc-lite/pull/1182) and the [IFClite project site](https://ifclite.dev/) for details.
