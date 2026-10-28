# Week 11: Python controls creative software

**Thursday 19 November 2026.** Revised 120-minute lecture and separate 120-minute
PFAD tutorial. This run sheet replaces the old 70-minute simulated-opacity
lesson. **Draft incomplete:** the existing deck still illustrates that old
proposal. Replace/render it only after application acceptance; do not use it
to deliver this run sheet.

## Lecture: exact approved blocks

| Minutes | Teaching work and evidence |
| --- | --- |
| 0-10 | Ask which creative operation a program could control. Brief W10 retriever-tool handoff; dated news after source verification. Compare a tool response with the observed artwork. |
| 10-35 | Live Blender: predict scale, inspect bpy object, change, save and CPU-render. Compare two actual images. Trace camera/light/output and a missing-object error. |
| 35-60 | Direct API versus actual MCP request: discover schema, inspect JSON, change scale, check saved scene/image and stop. Name course adapter versus unaccepted third-party live bridge. |
| 60-70 | Ten-minute break. |
| 70-95 | Live Godot: inspect scene/config, direct Python validation, create/change through real community MCP, run, check behavior. Compare file state and running state. |
| 95-110 | Fail at speed 120; read actual check fields before adapting. Diagnose missing parent/stale window. Contrast a launch ack, process logs and visual/behavior evidence. |
| 110-120 | Project possibilities, questions, explain one chosen app path and timed PFAD tutorial. |

Do not fill unaccepted live-demo blocks with invented success. If the host is
blocked, use inspected Blender image/scene plus truthful tool traces for
explanation, and a prepared partner desktop for hands-on application changes.
A trace is not an autonomous model. A recording alone is not a student's core
application exercise. Rehearse both visible application routes before class.

## Commands and demonstrations

Use the [verified companion Week 11 sources](https://github.com/sd5913/pfad/tree/3bbb871d1ba0583c8a2e0391aa286740f4896acb/week11)
in the companion review checkout. No unmerged sibling PR is a hidden
installation prerequisite. This commit is an incomplete acceptance draft,
not a classroom-ready release.

```bash
cd week11
uv run python -m unittest test_world test_mcp_transport test_engine
uv run python world.py inspect
uv run python world.py check
uv run python world.py play
```

Godot 4.7.2 is the latest installed verified engine; use latest stable rather
than the cached 4.5.1. Set GODOT_PATH if not found on PATH. `world.gd.advance`
implements the shared behavior. Default speed 300 / radius 24 / exit 860 wins with
three pickups, x=840 at 152 physics steps. Change speed 120: after 180 steps it
collects 2 and reaches x=440; restore 300 and check recovery. The check uses actual
Godot/GDScript, without a graphical claim. Restart the window after config edits.

```bash
uv run python setup_bridge.py
uv run python mcp_client.py list
uv run python mcp_client.py demo
```

Coding-Solo source 1209744 v0.1.1, adapted SDK 1.30.0/Node 26: actual discovery,
project metadata, scene creation, Node2D/Label creation passed. Inspect
`godot/probe.tscn`; the Label text is THREE LIGHTS. run_project responds before
window readiness. Inspect real display/debug output; stop_project then close
stdio. Fresh network installation and visible run are not accepted yet.

```bash
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1
blender --background --factory-startup -noaudio --python-exit-code 1 --python blender_scene.py -- --scale 1.5
uv run python mcp_client.py --blender list
uv run python mcp_client.py --blender render_scene '{"scale":1.25}'
```

Blender 5.2.3 LTS creates .output/blender/sculpture.blend, inspect.json and
scale-named PNG files. Visually compare geometry/shadow with fixed camera.
The actual CPU render was inspected; shutdown currently hangs under restricted
host audio and the 90-second adapter timeout returns isError. Preserve that failure;
an existing PNG does not prove a clean end. Missing target errors before save;
scale 5 is rejected before launching. Do not call the course CLI adapter the
third-party Blender MCP implementation. The latter's live socket/add-on path
is a remaining independent acceptance task.

## Tutorial: separate 120 minutes

| Minutes | Student work |
| --- | --- |
| 0-15 | Set up one chosen app and inspect supplied scene; use prepared partner if baseline unavailable. |
| 15-35 | Predict/inspect/change through actual API/CLI. |
| 35-55 | Trace real MCP/bridge request; verify saved scene effect. |
| 55-65 | Break. |
| 65-85 | Purposeful config/camera change, run/render and compare. |
| 85-100 | Missing node/object or failed time budget; diagnose and recover. |
| 100-120 |19 November playtest-feedback tutor review and project support. |

README gives exact commands, expected edits/outputs, platform conditions and
recovery. Students complete one path. For W12, Blender-only students get Godot
bootstrap0-20 and prepared partner handoff at 20; preserve break/final support.

## Preflight and review limits

Verify latest installed versions, process startup/discovery/change/result/stop,
actual desktop output, default paths and clean extraction/bridge installation.
Current actual evidence: 3 Python tests,4.7.2 engine pass/fail/recovery, actual
community MCP saved scene edits and stop protocol, inspected Blender CPU image.
Open: Godot visible play/movie, Blender clean exit/live third-party MCP,
fresh student setup and cross-platform/classroom rehearsal. Old 4.5.1 crashed
when appdata/logs could not be written; current helpers keep XDG_DATA_HOME in
.output for engine subprocesses. No further old-engine GUI attempts are allowed.

The replacement deck still needs rich notes, short readable visible copy,
large >=40px primary diagram labels, deckgen.CODE, exact source links and a
source-verified dated news item. Build HTML/plain/ClassPoint PPTX, check overflow
and inspect actual exports. Browser/PDF is blocked in the current sandbox;
report that rather than disabling checks or modifying the renderer.

## Project boundary

40% group project; 25% idea / 50% code / 25% execution; 6 December 2026, 23:59 HKT deadline.
Public sd5913-owned repo with teammate Write; Projects recommended/equivalent
accessible record valid. Canvas remains submission route. No new upload,
compulsory engine/AI feature, grade or defence. No live class or presenter action.
