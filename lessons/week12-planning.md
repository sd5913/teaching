# Week 12 planning: build, check and film a tiny world

29 October 2026 production revision for 26 November. Approved scope: complete
120-minute lecture and separate complete 120-minute tutorial. The genuine model
failure/adaptation/pass/stop episode, later real film of its unchanged final
source and timed Linux operator bootstrap now pass. `deck/week12.py` replaces
the historical addition/MCP draft with the actual tiny-world lesson. The 44-slide
replacement uses real screenshots, numbered diagrams, source excerpts and rich
speaker notes. Independent review/classroom preflight remain separate.

Runnable companion pin:
https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12 .
See [run sheet](week12-lesson-plan.md) for exact allocations and commands.
The short W10 source/index handoff now uses its verified real bundle and result.

## Lesson contract

Audience: artists, designers and game-design students. Tangible outcome: one
player collects three lights and reaches an exit, with a failed check, a bounded
revision, real behavior evidence, a decision trace and an inspected short film.
These are practice artifacts, not a new Canvas submission or a group-project
engine/AI requirement. Python explains the host/tool/process boundary; Godot's
small GDScript scene supplies actual simulation. We do not disguise a browser
simulation or a fixed repair script as an agent controlling a creative app.

Learning outcomes:

1. Explain goals, observations, mutable state, allowed actions and stopping
   conditions using actual fields and methods in the supplied world.
2. Trace a bounded Python update through stored JSON, a fresh Godot process,
   scene behavior and structured check output; locate a failed boundary.
3. Justify a changed action from observed failure and stop when checks pass or
   when budget/external failure requires human help.
4. Distinguish a live model episode, human tool use, a recorded trace and a
   deterministic film workflow; compare behavioral and visual evidence.

## Knowledge ledger

| Already taught | Reused now | New computing work this week |
| --- | --- | --- |
| W7 Ball objects, attributes, methods, delta time and two views of one simulation | `advance` updates one world's player/collection/win state; checks and graphics share that behavior | Feedback loop separates observation from action selection; a goal determines which state matters. No basic class replay. |
| W8 small increments, Git review, Codex environments and CI, tests versus deployed/usable output | One config diff, a fresh process and evidence a teammate can inspect | Bounded action/write/time budgets, explicit stopping and limits of autonomous claims. Docker is not restored. |
| W9 messages and process boundaries, structured inputs and failures | Python starts an engine and reads its structured result; stdout/stderr/exit status have distinct jobs | A tool observation may be failure evidence; successful process startup is weaker than successful behavior. |
| W10 persistent records, exact queries, real embeddings/source-backed retriever, conversation memory and speech | Config persists while runtime player state resets; short source-backed retriever handoff uses the same verified index | World action selection and scene checks; do not conflate config, conversation history and handbook knowledge. W10 supplies the separate verified knowledge source. |
| W11 creative application API/tool boundary, real scene changes, MCP roles and application cleanup | Supplied real Godot scene/helper contract; MCP is one possible transport, not the lesson itself | Model-selected adaptation over observations versus deterministic replay/capture; enough frames and visual validation. |

## Concept, source, failure and evidence ledger

| Concept | Actual source path in paired PFAD `week12/` | Student question/failure | Evidence required |
| --- | --- | --- | --- |
| Goal and state | `godot/world.gd`: `player`, `collected`, `won`, `ticks`, `advance` | If the player reaches the exit without all lights, is the goal met? | Actual 0/1/2 pickup exit probes reject a win; normal route needs all 3 within 180 ticks. |
| Tool contract | `world.py`: `BOUNDS`, `update_config`, `execute`, `check` | Does `set exit_x 2000` write anyway? Does a successful set prove motion? | Error before config write; compare unchanged file and later engine observation. |
| Bounded host | `loop.py`: `Session.run` | Should a passing check trigger another edit? What happens on the ninth action? | Host records observations, refuses action/write/time overflow and further actions after pass; no automatic repair choice. |
| Feedback and next action | `model-episode.json`: original model reasons and raw outputs | Why 275 after 125 failed? Could the logger have chosen the repair? | Genuine successive model/tool observations; logger has no repair loop; preserve observation fidelity and provenance. |
| Persistent versus runtime state | `world.json`, `world.gd._ready`, `world.py.execute` | Why is a running editor/game unchanged after a file write? | Restart reloads config; player starts at 80 again. Do not treat a file-only inspect as editor observation. |
| Tests as a limited acceptance model | `check_world.gd`, `test_engine.py` | Can a checker that only inspects the initial flag miss a broken exit rule? | Actually position at exit; run simulation and evaluate outcomes. State what manual control/visuals remain untested. |
| Deterministic playback | `world.gd._physics_process`, `world.py.capture` | Is following the same known route a model decision? | Same `advance`, fixed 30 render fps/60 physics ticks; current real headless replay reaches 166 ticks. It is not a film. |
| Film and visual verification | `world.py.validate_movie`/`capture` | Can a 120-frame valid MP4 show a black or wrong scene? | Full decode, metadata, samples and actual playback showing movement, three pickups, exit and COMPLETE. Passed on real Xvfb/Mesa graphics, 29 October. |
| Source-supported retrieval transfer | W10's verified bundle/real tool, with its verified bundle | What actual handbook chunk/source did the model inspect? | Same compatible encoder/space, page/chunk metadata and real tool observation. No nonexistent-bundle claim. |

## Actual model episode and provenance

The coordinator supplied a genuine current authorized Codex CLI episode dated
29 October HKT. Assistant identity reported by the runtime: GPT-6; exact backend
model ID unavailable. It used no separate billed endpoint, new account or paid
media generation. Its one-action logger records observations; it does not
retry or select changes. Public fixture preserves all action arguments, model
reasons and raw outputs, replacing only machine-specific executable/project
paths. Raw timestamps are UTC 28 October 16:xx, which is 29 October HKT. Source
manifest identifies the exact original files and starter commit
`3bbb871d1ba0583c8a2e0391aa286740f4896acb`.

The observed sequence is inspect 125 -> real check fails with 2 lights/x455.0007/
180 ticks -> model reasons from 375 units/3 seconds and chooses 275 -> unchanged
real 4.7.2 check passes 3 lights/x840.8323/166 ticks -> stop edits. Capture's socket
creation observation was later corrected with an actual connection test:
Wayland connect returned EPERM. This correction remains in the public replay;
do not turn socket creation into graphics proof.

Current W12 improves the checker with actual premature-exit probes and
stop-after-win tests, and adds a replay completion log. These were not
observations the model had in the original episode. Human-selected test
sweeps/rehearsals are separate from that episode, and the public README labels
the local tools route human-directed. No standalone client or automatic agent
loop is claimed. The same tools can support a configured model later, but this
fallback does not require an unused paid client or bridge installation.

## Historical crosswalk

Read the actual 2025 Week 12 PDF, 65 pages: pp. 4-19 and 21-65 were extracted; pp. 51-53
include the old tool/adapter/application examples. Read archived PFAD
`week12/bot.py`, `tools.py`, `app.py` from `origin/2025` (archive commit
`512edb07927c5d77cacc7279ba6be601b33dc601`). Page numbers below are 1-based
**PDF pages**, not PPTX slide numbers or calendar weeks. The teacher-owned
archive binaries are not copied to public course repos.

| Historical source | Concept and decision | 2026 destination/status |
| --- | --- | --- |
| W12 PDF pp. 4-7; W11 PDF pp. 18-30 | Orange/classic data-mining/visual workflows | **Removed by explicit instructor decision**, including t-SNE/matrix/projection requirements. Preserve embeddings/source retrieval in W10, not Orange in W12. |
| W12 PDF pp. 8-11; W11 PDF pp. 31-39 | Real creative-app scripting, camera, render | **Updated/reused:** W11 covers real Blender/Godot application boundaries. W12 reuses one actual Godot scene and its engine checks/capture rather than another application setup tour. |
| W12 PDF pp. 12-19 | TouchDesigner, NDI and OSC as creative process/protocol examples | **Moved/reused:** W9 control-message/OSC bridge; W11 creative-application optional extensions. No new TouchDesigner/NDI installation in W12. |
| W12 PDF p. 21 | Repository hygiene, portable paths, README, meaningful commits | **Retained:** self-contained starter, no sibling imports, named evidence and delivery-candidate tutor support. Historical student feedback is not this year's feedback. |
| W12 PDF pp. 25-26 | DRY and useful automation | **Retained:** one shared `advance` behavior for check/play/replay and Python automation with visible results. |
| W12 PDF pp. 27-29 | Errors, debugging/tests and reference/autocompletion | **Retained/updated:** actual failed behavior versus missing engine/display, structured observations, current Godot docs and meaningful tests. Not a new LSP lesson. |
| W12 PDF p. 30 | Rewrite when learning reveals a simpler architecture | **Retained as judgement:** make one bounded config revision first; a rewrite is optional project discussion, not permission to evade checks. |
| W12 PDF pp. 31-34 | User testing, small steps, docs and reading code | **Retained:** inspect source, predict, change/check, partner observation and exact evidence retrieval; use current docs before API changes. |
| W12 PDF pp. 35-47 | Generative-AI research, six hats and cognitive presence | **Moved to optional sourced discussion:** compare what a model appears to do with observed actions. No research survey, unsupported causal claim or quiz requirement consumes core loop time. |
| W12 PDF pp. 48-52 | MCP/tools, tiny FastMCP addition and agent adapter | **Updated:** transport is brief W11 recall; main actions are inspect/bounded set/check, followed by replay/capture. Old add/protocol files remain historical smoke tests, not the Week 12 outcome. |
| W12 PDF p. 53 and pp. 55-63 | ComfyUI/submodules/remote generation stack | **Replaced for approved tiny-world spine:** official Godot Movie Maker and Python helpers, no mandatory GPU, submodule/model setup, paid generation or LAN service. ComfyUI remains optional historical context. |
| W12 PDF pp. 64-65 | Team updates | **Retained:** final 20 tutorial minutes for existing delivery-candidate review/support, including unfinished work. No new assessed artifact. |
| Archive `tools.py`, `bot.py`, `app.py`; `ERRATA.md` | Agent/tool/observed result and async lifetime | **Updated:** preserve real action/result trace, no import-time event loop or opaque model client required. Historical tools bind through `asyncio.run` at import; do not copy the dead-loop bug. |
| W10 PDF p. 54 -> later agent/tool lessons | Retriever is an agent tool | **Retained/verified short handoff:** actual W10 prepared-vector lookup with PDF/chunk/encoder provenance; the world core remains independent. |
| 2026 W7 Ball and W8 reviewed material | Shared simulation, small tested changes, Git/CI evidence | **Reused:** scene behavior is shared; test evidence and visible experience are separately checked. W8 uses Codex environments/CI, not Docker setup. |

The historical abstract tool-call concept is preserved and deepened through
actual state and feedback. It is not enough to keep the old pure addition
example and relabel it “build/test/film.” Modernizing tools does not authorize
silently dropping the source-backed retriever concept; its dependency is
explicitly open. Orange removal is instructor-approved and is not a gap.

## Complete tutorial and platform contract

PFAD `week12/README.md` gives exact 0-20/20-35/35-55/55-65/65-85/85-100/100-120
blocks. First-time Godot students receive download/prerequisite/version checks,
Project Manager Import of `godot/project.godot`, visible orientation, baseline
failure and a prepared partner handoff at minute 20. Both partners operate a
config change and check, then capture/copy their own config/check/session/report/
clip/sample frames before swapping. Recording alone is not a substitute.

Latest verified stable is Godot 4.7.2. The fresh official Linux standard ZIP
(77,860,424 bytes, SHA256 cadd3204e728a35d3f13adb7fd0d7902636b79f6b95c40c265eb73b6c35329e4)
downloaded in 9.484 seconds. An isolated no-W11-project/bridge/import-cache route
completed actual import, supplied baseline, human config/check/capture and two
simulated learner evidence turns in 31.215 active seconds including download.
A fully initialized editor/2D orientation and normal Ctrl+Q/Enter exit took
29.312 seconds in a follow-up stage; total measured active work 60.528 seconds.
The stages are not a continuous novice trial. Existing uv/Python/FFmpeg/Xvfb/Mesa
were prerequisites. Windows/macOS, cold prerequisite installation, slow networks
and novice reading/orientation remain unmeasured. Prepare the actual partner
machine before class. Software rendering is actually verified, with no dedicated
GPU or paid model required. Public sanitized source hashes/film/stills/timings:
PFAD `week12/evidence/provenance.json`; full record `week12/verification.md`.

The exact original model-selected final source yielded a real 960x540/4.000s/
120-frame clip, fully decoded and played. Samples show 0 lights, 2 lights/player
movement, 3 lights/mint exit/COMPLETE. The current stronger capture helper passed
separately. Later recording is deterministic and is not a new model episode.
The CI candidate remains an unrun proposal, not a successful public workflow.

## Current sources and news discipline

Focused Context7 resolve/query calls 29 October selected
`/godotengine/godot-docs/__branch__4.7` (official/high-reputation source).
Queries covered Movie Maker/fixed FPS/quit-after and actual SceneTree/node
processing. Primary sources:

- [Godot 4.7 Movie Maker](https://docs.godotengine.org/en/4.7/tutorials/animation/creating_movies.html): official recording and container/encoding limits.
- [Godot 4.7 CLI](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html): `--write-movie`, `--fixed-fps`, `--quit-after` rendered-frame semantics.
- [Node processing](https://docs.godotengine.org/en/4.7/classes/class_node.html) and [Engine ticks](https://docs.godotengine.org/en/4.7/classes/class_engine.html): physics callback versus render frames; default 60 ticks/s.
- [Official 4.7.2 release](https://github.com/godotengine/godot-builds/releases/tag/4.7.2-stable) and [download](https://godotengine.org/download/): current release rechecked near class, not an old cache.
- [Paired PFAD draft](https://github.com/sd5913/pfad/pull/15): actual starter/tools/trace/tests and complete tutorial; final source commit pinned after independent review.

Opening news is the official Godot 4.7.2 maintenance release, published
18 August 2026 at 15:56:46 UTC, verified latest 29 October. Source is the official
release API/page, not a binary build timestamp. The supported claim is stability/
usability fixes; observed behavior is this actual engine/scene/capture, not all
release claims. Ask what a designer should recheck after an engine update.
Refresh this three-minute item near 26 November; news stays outside quiz scope.

## Authoring and acceptance checklist

The model, film and operator-bootstrap gate passed before replacement authoring.
The incumbent palette/type/layouts are preserved. Primary diagram labels are
40-52px or larger on a 1680 px-wide figure rendered at full slide width. Actual
screen captures identify their source/date; runtime drawing explains the empty
editor canvas. Short visible text and canonical `deckgen.CODE` excerpts leave
explanations, prompts, failure handling and minute allocations in notes.

The author read Impeccable's craft floor before editing, applied it within the
existing course visual system and inspected actual PDF/native render evidence.
Build/export verification is recorded in the private author report; independent
review and instructor classroom preflight remain. The exact W10 result/encoder/source metadata are retained in the paired
`handbook-handoff.json`; coordinator retains the final companion source pins. The local loop core does not depend on that retrieval bundle. The direct retriever check is labeled separately from a fresh model call.

Preserve project policy: 40% weighting, 25% idea / 50% code / 25% execution, 6 December 2026
23:59 HKT deadline; public `sd5913`-owned team repository and teammate Write
access; recommended GitHub Projects or equivalent accessible progress record.
No new upload, grade, compulsory defence, technical practical in W13, model
account or engine requirement is introduced. No merge/publish/presenter/class
or student/tutor messaging occurs in this authoring work.

## Verified three-minute handbook handoff (101-104)

The author directly ran W10 `handbook.py` for its exact prepared lost-card
question. Actual results: `hb2026-p020-replacement`, PDF position20 / printed9,
cosine0.815428; return chunk0.763087. The paired PFAD `handbook-handoff.json`
retains source/encoder/query/bundle hashes and the actual passage observations.
This is a direct retriever check, not a new model call or a claim that the world
searched the PDF. W10 exposes `retrieve_handbook` to its agent; its final source
pin is `c59fae0df42e316a431c308bfe582a84411d5887`.

Official2026/27 handbook PDF SHA256:
`108956feb2ffac665f8ca0f5a8f68d7150a85fda15e219916785ec50331a4e94`.
Encoder: `sentence-transformers/all-MiniLM-L6-v2`, revision
`1110a243fdf4706b3f48f1d95db1a4f5529b4d41`,384dimensions, attention-masked
mean pooling/L2-normalized,max_tokens256. Preserve the same query/document
space; fixture mode uses its stored genuine query vector and rejects an
unprepared question. Six short extracts from PDF20/25/76 are not a full index.
Distinguish four lifetimes: indexed knowledge, persisted isolated conversation
rows, ephemeral assembled prompt and derived spoken output. World config is
separate. The core tiny-world practical needs no W10 import or model account.
