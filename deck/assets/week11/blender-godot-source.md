# Same Blender object in Godot: actual capture provenance

Generated 18 November 2026 on Linux x86_64 using Blender 5.3.0 and Godot 4.7.2.
Original course scene/mesh/material; no external asset or generation service.
These are prepared author rehearsals, not a model-session transcript.

Source: PFAD Week 11 `blender_scene.py`, `blender_export.py`,
`asset_handoff.py` and `godot3d/preview.gd`. The integrated tested companion
revision is pinned in `deck/week11.py`. See the companion's
`week11/asset-handoff-20261118.md` for commands/checks and source hashes.

| Asset | Actual output and properties |
| --- | --- |
| blender-baseline.png | `.output/blender/before/sculpture-1.25.png`, uniform scale 1.25, dimensions [2.5,2.5,2.5] |
| blender-first.png | `.output/blender/first/sculpture-1.25.png`, scale [2,.9375,1.25], dimensions [4,1.875,2.5] |
| blender-revised.png | `.output/blender/revised/sculpture-1.25.png`, scale [1.625,.9375,1.25], dimensions [3.25,1.875,2.5] |
| godot-revised.png | `.output/godot3d-revised.png`, actual engine renderer/movie PNG frame, 960x720, imported dimensions [3.25,2.5,1.875] |

Blender images are 640x480 CPU Cycles renders, eight samples. Author rehearsal
uses temporary copies of the existing script for the two focused proportion
changes. Camera [7,-9,6], light, material, centre height and vertical scale
stay fixed; the source lesson script remains the uniform baseline for students
to edit. The separate output folders contain current inspection JSON/.blend.

Godot imports the GLB from the SAME revised saved `.blend`; it does not rebuild
a replacement cube. Export includes only Sculpture and its Terracotta material,
bakes scale, and normalizes the origin to the bottom centre in export memory.
The source `.blend` stays byte-identical. Exporter converts Blender Z-up to
Godot Y-up. Actual engine import/instantiation checks one mesh/material,
source-to-engine dimensions, identity instance transform and bottom y near 0.

Revised GLB SHA256:
`f20ee16a31480412f7c0a5ab83c2bdd586d43b7dc75d01ef646f27d2058a46e2`.

Godot capture uses the actual Compatibility renderer on an isolated Xvfb
display. It has its own floor, camera, light and environment, so matching
material data does not imply pixel-identical shading. No collision, texture,
animation, live model decisions, Windows/macOS or classroom projection check
is claimed by these images.
