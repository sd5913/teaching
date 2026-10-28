# Week 12 planning: build, check and film a tiny world

29 October 2026 production revision for 26 November. Approved scope: 120-minute
lecture and separate 120-minute tutorial. **Incomplete production acceptance:**
actual model-selected failure/adaptation/pass/stop is recorded; graphical film
and a timed first-time graphical Godot bootstrap remain missing. The incumbent
`deck/week12.py` addition/MCP lesson stays unchanged and unaccepted for this
new scope. Its old 21-slide tests/exports cannot establish the new lesson.
See [run sheet](week12-lesson-plan.md) for all minute allocations and commands.
No outline approval is being reopened; this executes the instructor's reviewed
tiny-world direction while respecting the explicit film/bootstrap gate.

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
| W10 persistent records, exact queries, real embeddings/source-backed retriever, conversation memory and speech | Config persists while runtime player state resets; conditional source-backed retriever handoff uses the same verified index | World action selection and scene checks; do not conflate config, conversation history and handbook knowledge. W10 proof is still a separate dependency. |
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
| Film and visual verification | `world.py.validate_movie`/`capture` | Can a 120-frame valid MP4 show a black or wrong scene? | Full decode, metadata, samples and actual playback showing movement, three pickups, exit and COMPLETE. Still missing. |
| Source-supported retrieval transfer | W10's verified bundle/real tool, once supplied | What actual handbook chunk/source did the model inspect? | Same compatible encoder/space, page/chunk metadata and real tool observation. No nonexistent-bundle claim. |

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
| W10 PDF p. 54 -> later agent/tool lessons | Retriever is an agent tool | **Retained dependency, unverified handoff:** brief sourced example only after W10's actual PDF/index/encoder/tool evidence exists; no false handbook search. |
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

Latest installed 29 October runtime: Godot 4.7.2, replacing old 4.5.1. Standard
Godot requires no .NET SDK; direct helpers use only Python standard library.
No paid model, bridge or dedicated GPU required. Graphics still needs a
working desktop/driver or verified software path. Only Linux x86_64 headless
checks are accepted here. Windows/macOS graphics, fresh downloads, renderer
orientation, partner retrieval and all cold timings remain untested.
Official Linux 4.7.2 ZIP 77,860,424 bytes; others unmeasured. The warm installed
engine does not satisfy first-time setup. Exact normal public-CI proposal lives
in PFAD `week12/ci-capture-candidate.md`; no workflow was silently changed.

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

Opening news remains a reserved, **unverified** 3-minute item until a dated
primary source is selected near 26 November. Record event and publication dates,
exact supported claim, why designers care, prompt and tested-versus-reported
behavior. Engine build timestamps are not release publication dates. News,
frontier demonstrations and optional project inspiration stay outside quiz
scope; do not invent a verified current-news item to fill the slot.

## Authoring and acceptance checklist

The long replacement deck remains blocked by film/bootstrap evidence. After
those pass, use the incumbent visual language: large actual scene/feedback
diagrams, numbered arrows, primary labels >=40 design pixels, brief visible text,
rich notes and actual contiguous source excerpts through `deckgen.CODE`. Read
Impeccable's craft floor immediately before UI edits. Inspect actual
HTML/PDF/plain/ClassPoint PPTX outputs, overflows, sources and notes. None of
that replacement export evidence exists yet; old exports are only historical.

Before accepting the lesson, separately require the actual model loop, playable
film/full decode/visual inspection, timed first-time graphical bootstrap,
prepared-machine pair rehearsal, W10 source/index handoff proof and final
companion commit pin. The unresolved core gates cannot be marked merely
“classroom rehearsal remaining” and cannot be closed by mocks or trace replay.
Independent reviewers and instructor approval still follow this local work.

Preserve project policy: 40% weighting, 25% idea / 50% code / 25% execution, 6 December 2026
23:59 HKT deadline; public `sd5913`-owned team repository and teammate Write
access; recommended GitHub Projects or equivalent accessible progress record.
No new upload, grade, compulsory defence, technical practical in W13, model
account or engine requirement is introduced. No merge/publish/presenter/class
or student/tutor messaging occurs in this authoring work.
