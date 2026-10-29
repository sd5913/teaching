# Week 11 authoring plan: real creative applications

Approved scope: 19 November 2026, 120-minute lecture and separate 120-minute
PFAD tutorial. The instructor authorized the reviewed Weeks 9-13 design on
29 October. This replaces the old synthetic-opacity proposal. The replacement deck now follows the accepted real-application spine; the old
browser exercise remains historical companion material, outside the core route.

## Outcomes and knowledge ledger

Students inspect/change actual scene data, distinguish API/CLI/MCP boundaries,
run or render the result, and diagnose a missing object or failed behavior check.
Each student completes one application path; both appear in the lecture.

Already taught: Week 7 object state/methods and one model/two views; Week 8
program verification/team delivery; Week 9 messages/processes; Week 10 persistent
models, embeddings, source-backed retriever tools and talking-agent memory.
Reused here: names/properties, method calls, JSON messages, ownership of state,
file persistence and explicit evidence. New: application APIs and context,
live scene versus file, MCP discovery/call/result, programmatic camera/render
control, scene operations and application-level acceptance. Do not repeat the
Ball class or a general permissions lesson.

## Source-to-lesson crosswalk

All historical references mean 1-based PDF pages of the 78-page 2025 Week 11
PDF. The PPTX has 79 slides; after its extra slide31, numbering differs.

| Historical source | Status | 2026 destination |
| --- | --- | --- |
| pp4-17 objects/storage recap | Reused, shortened | Named scene property; persistence/file versus running app, building on W7/W10 |
| p22 previous week's embeddings | Retained dependency | Same handbook index/retriever in W10; optional brief tool handoff here |
| pp18-30 Orange/t-SNE/projection | Removed by instructor | No Orange, matrix or projection task/quiz requirement; time assigned to real tools |
| pp31-33 Python-enabled Blender | Updated | Actual bpy scene inspect/change/save/render |
| pp34-39 multi-angle dataset | Retained/updated | Camera direction/position and systematic small rendered variants; no required generated mesh |
| pp40-44 TouchDesigner/Python | Retained as extension | Linked archive: operators/data mapping; no additional install |
| pp45-48 NDI | Retained as extension | Audio/video transport contrasted with numeric controls |
| pp49-55 MediaPipe/OSC | Moved/retained | W9 vision-to-message bridge; W11 process responsibility comparison |
| pp56-60 physics server/clients/async | Moved/retained | W9 server-owned state; W11 application-owned scene state comparison |
| pp61-78 tutorial/project update | Updated | Full timed README; 19Nov playtest/feedback support, no new assessment |

Archive PFAD source inspected: origin/2025 at
512edb07927c5d77cacc7279ba6be601b33dc601, week11 README/ARCHITECTURE,
osc_demo and Blender datasetbuilder inventory. The archive ships no standalone
Python file for the embedded Blender script. Read the W7 Ball/two-view material
and current reviewed W8 lecture/tutorial before preparing this plan.

## Runtime choice and honest gaps

Use the latest stable installed engine: Godot 4.7.2, Blender 5.2.3 LTS, current
29 October check. Earlier cached 4.5.1 results are historical, superseded evidence.
Godot is the primary tutorial; Blender is an alternative, not a second required
installation. Blender-only students receive W12's first-time Godot block0-20
and prepared partner handoff at minute20.

Coding-Solo/godot-mcp source 1209744 (v0.1.1) is a third-party MCP stdio server
using Godot CLI/GDScript. Its declared SDK 0.6 was adapted to tested SDK 1.30.0
with Node 26's native TypeScript support. Real discovery/metadata/create/add-node
passed in actual 4.7.2. Source is unchanged; runtime adaptation is explicit.
Current mcp-for-blender2.2.6 source 8782963 is a separate third-party Python
server plus live socket add-on. It passed real startup/discovery/scene inspection/
scale1.5/reinspection/CPU render/save/client closure/add-on stop/Blender exit0/
socket closed. The bounded Blender CLI MCP adapter is course-owned and named
separately; its actual render and exit0 also pass under full host permissions.

Godot4.7.2 actual headless behavior passes, speed120 fails and restoring300
recovers. Its graphical software-rendered Movie Maker route produced a playable
4s960x540120frame H264 clip, fully decoded with start/middle/end inspected.
Fresh public installation of Godot bridge (3.606s) and Blender bridge (4.602s)
passed with empty package caches on29October; applications were already installed.
These times are not first-time application bootstrap measurements.

Windows/macOS, actual projected keyboard play and classroom rehearsal remain
instructor checks. Week12 owns first-time Godot bootstrap and actual live-model
loop acceptance; today's fixed human-directed requests are not model-loop proof.

## Sources and news

Sources checked29 October: current Blender API; official Godot CLI/Movie Maker;
MCP SDK lifecycle/stdio docs through Context7, then primary community README,
package metadata and source. Godot MIT; Blender GPL; community bridges/SDK MIT.
No asset-generation calls or paid model APIs were used.

Opening news: Godot4.7.2 stable release,18August2026. Primary GitHub tag
metadata checked29October: published_at2026-08-18T16:12:28Z. Source and claim
limits in week11-news-20261029.md. Keep outside quiz scope and refresh near class.

## Completion status

The full replacement deck covers the approved120-minute lecture with actual
Blender renders and Godot capture frames, large numbered process diagrams,
short CODE panels and substantive notes. PFAD supplies a separate complete
120-minute README and real examples/failure paths, including two controlled
camera variants. It uses no paid generation/model account. Final exact companion
commit, builds/render inspection and independent review are recorded in the
private production report. Paired PR14 remains open; no presenter/shared
registrations changed.
