# Camera revision render

Actual Blender 5.2.3 LTS CPU Cycles render, 15 November 2026, 640 x 480,
eight samples. Original course geometry/material/light; no external artwork.

Source: PFAD `week11/blender_scene.py`, unchanged from verified companion
`41108250bcf2ae428dc819363bb32212b8f19fe7`.
Source file SHA-256:
`69a64aa943dfa98ebc4f41e3f2736c8580c0c2f5ad51e04190f61ce399456173`.

From the PFAD checkout:

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python week11/blender_scene.py -- --scale 1.25 --camera-x 5 --camera-y -10 --output /tmp/sd5913-week11-pr-revision-20261115
```

The process exited 0. The inspection records target `Sculpture`, before scale
`[1, 1, 1]`, after scale `[1.25, 1.25, 1.25]`, camera `[5, -10, 6]`.
Camera direction still targets `(0, 0, 1.1)`; the script also raises the cube
center to z=1.25 to preserve floor contact. The original second camera view
was `(9, -7, 6)`; first view remains `(7, -9, 6)`.

Output `sculpture-1.25.png` is copied as `camera-revision.png`, SHA-256
`812c25732f1074c055dc4fd129dfb9bccd84bc3b45590a291cfbcc182ea9722b`.
The render is actual application evidence. The accompanying reviewer wording
is a worked teaching example, not a captured public PR or live autonomous run.
