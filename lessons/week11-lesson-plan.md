# Week 11: Python controls creative software

**Thursday19November2026.** Complete120-minute lecture, then a separate120-minute
PFAD tutorial. The replacement51-slide deck uses actual Blender/Godot outputs,
current APIs and real MCP operations. Both apps appear in the lecture; students
complete **one** application path during the tutorial.

## Lecture: approved120-minute blocks

| Minutes | Slides | Teaching work and actual evidence |
| --- | --- | --- |
| 0-10 | 1-5 | Opening automation question; dated18August Godot release news outside quiz scope; short W10 handbook-tool handoff. |
| 10-35 | 6-19 | Actual Blender scale comparison; process/API boundary; named object/property; save versus render; two controlled camera variants; missing-object failure. |
| 35-60 | 20-29 | API/CLI/MCP; discover/call/result; stdio/socket/live add-on diagram; real community bridge changes/reinspects/renders; course adapter distinction; evidence and stop. |
| 60-70 | 30 | Full ten-minute break. |
| 70-95 | 31-40 | Actual Godot world; Python validation/file versus running GDScript; fixed-step behavior; direct check/play; community MCP scene/node/property action. |
| 95-110 | 41-46 | Speed120 failure/read fields/recover300; rejected config unchanged; actual graphical film frames; capture/graceful quit; OSC/NDI/archive transfer. |
| 110-120 | 47-51 | Project evidence question, complete tutorial handoff,19November tutor support, policy and questions. |

Speak from notes; keep diagrams visible while tracing the real data/process
boundary. The deck does not reteach Ball classes or generic permission cards.
Primary diagram labels are42-46design pixels on the1920x1080 canvas; code uses
`deckgen.CODE` through standard code_panel. Native and actual PDF were built
with overflow checking enabled. See the private author report for render and
export inspection evidence rather than treating automated tests as rehearsal.

## Exact companion and environment

[Verified companion Week11 sources](https://github.com/sd5913/pfad/tree/41108250bcf2ae428dc819363bb32212b8f19fe7/week11).
Open this exact revision while its paired PR14 is unmerged. All commands below
run from `week11/`; uv discovers its separate environment/lockfile. Linuxx86_64
verified29October2026: Godot4.7.2.stable.arch_linux.ed1daf0bf, Blender5.2.3LTS,
Node26.12.1, Python3.13.16, community MCP for Blender2.2.6 and Godot source
1209744v0.1.1 with the explicit JS SDK0.6->1.30.0 compatibility adaptation.
Do not use old cached Godot4.5.1. Rerun checks after latest-stable updates.

## Blender live sequence10-35

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1.5
uv run python blender_variants.py
```

Show actual `.output/blender/sculpture-1.png`/`sculpture-1.5.png` and inspect.json.
The script raises centerz with scale so the bottom stays on the floor. Distinguish
live object data, `.blend` and PNG. `bpy` executes inside Blender's own Python.
Camera comparison writes `angle-1/` and `angle-2/` below `.output/blender/` at
scale1.25; only camera position changes. Read recorded coordinates and compare
visible faces. The two-pose loop retains the2025 dataset concept at useful scale.

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --target MissingObject
```

Expect nonzero exit and `Missing object: MissingObject; use Sculpture`, before
new save/render. An old PNG on disk does not make this failed run successful.
Remove the incorrect target and restore a known successful render.

## Actual MCP35-60

```bash
uv run python setup_blender.py
uv run python blender_live.py
```

This is the actual **third-party MCP for Blender**, not a Blender Foundation
feature. The setup uses pinned MIT add-on source8782963/package2.2.6 in ignored
.tools, without global client/add-on config. The disposable Blender window has
its own free loopback port; the stdio MCP server connects to that add-on.
Discovery -> live inspect -> code change to1.5 -> live reinspect -> CPU render/
save -> Enter in terminal -> client close/add-on stop/Blender quit/socket closed.
Show `.output/blender-live-result.json` and the actual image/scene. Do not open
personal work in this disposable process. Telemetry/update checks disabled;
asset/generation services never invoked. For automatic preflight closure:

```bash
uv run python blender_live.py --verify
```

Compare the bounded **course-owned Blender CLI MCP adapter**:

```bash
uv run python mcp_client.py --blender list
uv run python mcp_client.py --blender render_scene '{"scale":1.25}'
uv run python mcp_client.py --blender inspect_scene
uv run python mcp_client.py --blender render_scene '{"scale":5}'
```

First render succeeds and exits cleanly. Last tool rejects before launch with
isErrortrue/nonzero client exit. inspect_scene reads saved inspection JSON,
not the state of any open editor. The community live get_scene_info reads the
running Blender scene. Check protocol, scene/render and process cleanup separately.

## Godot70-110

```bash
uv run python world.py inspect
uv run python world.py check
uv run python world.py play
```

The file inspection says file_state_onlytrue. Python validates/writes config;
Godot loads it on startup and runs GDScript. Arrow keys move the player. Close
the window before changes and restart to load the new file. Actual default:
speed300, three pickups, playerx840, win at tick152. Check uses180steps at1/60s,
not a wall-clock/keyboard/graphics benchmark.

```bash
uv run python setup_bridge.py
uv run python mcp_client.py demo
```

Third-party Coding-Solo source1209744, version0.1.1. demo saves a separate
probe.tscn with Marker and Caption Label textTHREE LIGHTS; inspect it in the
editor. The main project it runs is world.tscn, not that probe. CLI/GDScript
operations are not a live-editor remote-control socket. Read debug output,
observe actual window, stop_project and close stdio. The helper now treats
isError as failure. A project-start acknowledgement does not prove readiness.
After a launch attempt, stop_project is attempted in finally with a five-second
deadline; bounded process-group cleanup handles a broken transport without
replacing the original error. The tutorial's next manual call adds RouteHint
with text COLLECT THREE, THEN EXIT, preserving the demo's Caption/THREE LIGHTS.
If bridge close fails after a successful request, the CLI exits nonzero. If a
request already failed, it keeps the original exception and reports cleanup
failure separately.

```bash
uv run python world.py set speed 120
uv run python world.py check
uv run python world.py set speed 300
uv run python world.py check
uv run python world.py set exit_x 2000
```

Slow case fails: two pickups,x440,tick180. Restore300: three,x840,tick152. Last
invalid request rejects and preserves exit860. Read each actual result before
choosing the next mutation. This is human-directed; it is not a live model loop.

```bash
uv run python world.py capture
```

Needs a working graphical renderer and FFmpeg/ffprobe. Verified Linux software
renderer route: `xvfb-run -a uv run python world.py capture`; actual H264/yuv420p
MP4 is960x540,4.000s,120frames, full FFmpeg decode and start/middle/end frame
inspection. Graceful --quit-after120 closes AVI metadata; do not interrupt with
Ctrl+C. The deterministic replay demonstrates application rendering, not an
agent choosing actions. Actual keyboard play/projected classroom rehearsal
remain instructor checks. Week12 owns live-model gate and first-time bootstrap.

## Separate120-minute tutorial

| Minutes | Student work |
| --- | --- |
| 0-15 | One chosen app baseline; prepared-partner handoff at15 if unavailable. |
| 15-35 | Predict/inspect/change through actual API/CLI. |
| 35-55 | Trace real MCP request and verify the scene effect. |
| 55-65 | Full break. |
| 65-85 | Purposeful config/camera variant; run/render and compare. |
| 85-100 | Failure, diagnose from evidence, recover. |
| 100-120 |19November playtest/feedback tutor review and project support. |

README is self-contained for students/TAs and needs no instructor/ClassPoint
account. Prepared partner: open same week11 starter, take turns operating and
retain own config/scene/check/image/playtest note; watching a recording alone
is not core application practice. Blender-only students receive first-time
Godot bootstrap/orientation next week0-20, then prepared partner handoff at20.

## Preflight, sources and limits

```bash
uv run python -m unittest test_world test_mcp_transport test_engine
uv run python -m unittest test_blender_live
```

Last test is opt-in real GUI application acceptance; needs installed bridge/
Blender/display. With Xvfb: `xvfb-run -a uv run python -m unittest test_blender_live`.
Fresh public bridge installation passed with empty package caches (Godot3.606s,
Blender4.602s); desktop apps were already installed. These are author-machine
bridge times, not cold application download/bootstrap measurements.
Windows/macOS, actual projected keyboard play and classroom rehearsal remain
unverified. No paid API, asset generation or model account was used. Source
API docs fetched via Context7 and primary release/community code checked29Oct.
News claim/source boundaries: week11-news-20261029.md. Crosswalk: week11-planning.md.

## Project boundary

40% group project;25%idea/50%code/25%execution;6December2026,23:59HKT.
Public sd5913-owned team repo with teammateWrite; Projects recommended or
an equivalent accessible progress record. Canvas submission. No new upload,
engine/AI requirement, grade or defence. Orange/t-SNE/matrix requirements
explicitly removed; the W10 handbook embedding/retriever path remains core.
