# Week 11 authoring plan: real creative applications

Approved scope: 19 November 2026, 120-minute lecture and separate 120-minute
PFAD tutorial. The instructor authorized the reviewed Weeks 9-13 design on
29 October. This replaces the old synthetic-opacity proposal. The old deck is
retained temporarily as an unreleased historical draft while application
acceptance remains incomplete; it must not be used as this revised lesson.

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
server plus live socket add-on; documentation/source only, not runtime accepted.
The supplied bounded Blender CLI MCP adapter is course-owned and named as such.

Real4.7.2 headless behavior and failure/recovery pass. Blender produces actual
640x480 CPU renders and .blend/inspection, visually inspected. Restricted-host
Blender shutdown remains unaccepted (90-second adapter timeout after render). Godot
window/movie and first-time graphical bootstrap remain unaccepted. A launch
acknowledgement is not visual evidence. Do not author the long replacement
slide deck or claim classroom readiness before closing these gates.

## Sources and news

Sources checked29 October: current Blender API; official Godot CLI/Movie Maker;
MCP SDK lifecycle/stdio docs through Context7, then primary community README,
package metadata and source. Godot MIT; Blender GPL; community bridges/SDK MIT.
No asset-generation calls or paid model APIs were used.

Opening news candidate: the inspected MCP for Blender README announces its
package rename from blender-mcp to mcp-for-blender and links issue366. Treat
29 October as source-check date, not an invented announcement date. Before teaching,
verify a dated primary announcement or refresh with another dated creative-tool
story. Keep the news discussion outside quiz scope. No verified dated news
slide has been authored yet.

## Completion status

PFAD supplies actual scene, config adapter, direct Blender API, bounded MCP
adapter, community bridge setup/client, tests and a complete timed README.
The lecture run sheet below is prepared. Replacement deck, visual application
acceptance, fresh bridge install, student-platform rehearsal, rendered slide
inspection and final companion pin remain open. Existing paired PR14 stays
open for coordinator review. No presenter or shared registrations were changed.
