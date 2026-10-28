# Week 12: an agent builds, checks and films a tiny world

26 November 2026. **120-minute lecture, plus a separate 120-minute PFAD tutorial.**
Authoring status 29 October: **the full feasibility gate remains incomplete**.
`deck/week12.py` and its figures are the incumbent 21-slide addition/permission
lesson, retained unchanged as historical draft material. They do not deliver
this approved tiny-world lesson. Do not present their prior build evidence as
acceptance of this run sheet. No long replacement deck is authorized until the
actual model/check/adapt/stop episode also has a playable, inspected film and
the first-time graphical Godot bootstrap has been timed.

The independent preparation below is complete enough to review and rehearse;
it is not a classroom-readiness claim. Paired PFAD draft:
https://github.com/sd5913/pfad/pull/15 . The coordinator pins its final reviewed
commit before new slide authoring. No live presenter or remote class is needed
for these checks.

## What students should be able to explain

1. Identify a goal, mutable scene state, available tool actions, observations
   and a checkable stopping condition in one small world.
2. Trace a Python tool call through a config file and an engine process to an
   actual observation; distinguish a successful write from working behavior.
3. Use a failed check to justify a bounded revision, then stop when evidence
   satisfies the goal or when the action/time budget or an external failure
   requires human help.
4. Distinguish model selection, human selection, recorded trace replay and
   deterministic movie recording; inspect a clip separately from its test log.

Classes/methods, Git teamwork, ordinary process boundaries and MCP roles are
reused. Do not repeat the Ball lesson or the generic permission-card lesson.
The new subject is feedback: observing state and selecting the next action.

## Exact lecture allocation: 120 minutes

| Minutes | Teaching move, concrete source and evidence |
| --- | --- |
| 0-10 | Opening: “What evidence would make you trust a game built by an agent?” Give the one-player/three-lights/exit brief. Reserve at most 3 minutes for dated sourced news only after its event/publication date is verified. The remaining time lets pairs name a behavior check and a visual check. |
| 10-30 | Agent versus workflow: use the scene/config/process/output map and Python excerpts below. Distinguish choosing a next action from executing a fixed list. Predict speed 125 over 180 ticks; explain eight actions/four mutations/180 seconds and the stop rule. Give the diagram the slide in the future deck. |
| 30-50 | Actual bounded demonstration after the gate closes: inspect supplied 125 config, check, let the configured model choose a changed action from the observation, check unchanged rules and stop. Read observations aloud. If model access fails, label the supplied actual episode replay, then use the same local tools human-directed. This fallback does not retroactively pass production acceptance. |
| 50-60 | Read the real recorded trace: students label proposed action, applied write, engine result and stop decision. Predict what reaching the exit with 0/1/2 lights should do; run those checker cases. Ask what the successful check still does not establish. |
| 60-70 | Break. Stop visible playback; keep sources/evidence available. |
| 70-95 | Deterministic replay and capture, only on a verified graphics path. Predict 120 rendered frames at 30 fps versus 60 physics ticks/s, then run the commands below. Decode/check metadata and inspect beginning/middle/end images plus the playable clip. Trace the same `advance` method. Ask why a valid MP4 can still show the wrong result. |
| 95-110 | Compare evidence and limitations: fixture versus current run, real checks versus visible result, stale file versus restarted state, timeout/display failure versus behavior failure. Optional frontier comparison fits at most 3 minutes and needs a fresh primary source; otherwise spend this time on a partner's unsupported-success challenge. W10 handoff is conditional on the real source/index proof below. |
| 110-120 | Recap the loop and exact PFAD handoff. Show the complete tutorial timing and minute 20 prepared-machine route. Optional project question: could a bounded tool/check help your workflow? Reserve questions; no AI/Godot feature becomes mandatory in a group project. |

The table totals 120 minutes including the 10-minute break. A model's wall-clock
latency is included in 30-50, not granted extra time. If a tool blocks, show its
error, stop the attempt and continue the honestly labeled trace analysis.

## Detailed source-to-observation demonstration

Work from the **paired PFAD checkout**, then `cd week12`. The folder is
self-contained: it copies course-owned W11 starter commit
`3bbb871d1ba0583c8a2e0391aa286740f4896acb`, with no sibling imports. The
supplied speed 125 intentionally fails. Do not edit the three light positions
or the acceptance checker while trying to satisfy it.

```bash
uv run python world.py inspect
uv run python world.py check
uv run python replay.py
```

Inspection says `file_state_only: true`; it has not observed an open editor.
The baseline check exits 1 with two lights, x455.000732421875 at 180 ticks. The
actual recorded model used that observation to select 275; the unchanged engine
check then reached three lights and x840.832336425781 at 166 ticks and exited 0.
This genuine episode used the current authorized Codex CLI session; the
runtime reported GPT-6 but did not expose an exact backend model ID. It used
no separately paid API. The sanitized fixture includes original reasons,
outputs, source hashes, UTC timestamps and HKT date conversion. Do not claim
the current stronger checker was part of that older observation.

For a **human-directed** live tools demonstration, explicitly say who chooses
the action. Keep its logs separate from the recorded model evidence:

```bash
uv run python world.py set speed 125
uv run python loop.py start
uv run python loop.py inspect
uv run python loop.py check
uv run python loop.py set speed 275
uv run python loop.py check
uv run python loop.py status
```

A failed check is an expected nonzero exit, so do not chain through it with
`&&`. The host stops further actions after the passing check. `loop.py` does
not adapt, retry or call a model. It records config hashes and actual results
in `.output/session.json`, with eight tool actions/four writes/180 seconds;
checks are bounded to 15 seconds. A 30-second per-decision target is instructional
and is not falsely described as an enforced model timer. Invalid tools or
external failure stop with a visible error. Starting a new session replaces
its local journal; retain prior evidence before doing so.

Explain these short Python paths using `deckgen.CODE` in the eventual deck:

```python
# world.py: allowlisted file update, not arbitrary generated code execution
low, high = BOUNDS[key]
if not low <= value <= high:
    raise ValueError(...)
config[key] = value
```

```python
# loop.py: host execution; the next-action choice happens outside this function
if action == "check" and result["passed"]:
    state["status"] = "passed"
    state["stop_reason"] = "behavior checks passed; stop edits, inspect evidence before capture"
```

These are actual excerpts, not standalone runnable files. The tool implementation
checks structured output and process exit; a printed “started” cannot pass.

Godot's `advance(delta, automatic)` owns movement, collection and win state.
The checker instantiates the actual scene, disables automatic physics callbacks
and explicitly advances 180 ticks at 1/60 s. The graphical game/replay calls the
same method from real physics callbacks. Each instance has independent state;
the file supplies config at startup, not a running object snapshot. Reuse W7's
one-model/multiple-views reasoning without re-teaching basic class syntax.

```bash
uv run python -m unittest discover -p 'test_*.py' -v
```

Real engine tests cover 125 fail, 275 recover, 60 fail and 480 pass; they place the
player at the exit with 0/1/2 lights and require no win, require three collected
lights/time-bound completion and verify a win stops state changes. A
fixed-frame real headless replay reaches 166 ticks. These checks are stronger
than inspecting a `won` flag before moving. They prove no graphical rendering.

## Film demonstration and evidence interpretation

Only after the actual graphics acceptance, use:

```bash
uv run python world.py replay
uv run python world.py capture
```

Replay is the known route toward each light and exit. Godot Movie Maker writes
AVI with `--write-movie`, `--fixed-fps 30` and `--quit-after 120`; FFmpeg makes
H.264/yuv420p MP4. Capture checks completion within 180 ticks, ffprobe expects
960x540/about 4 seconds/120 frames, FFmpeg decodes all frames and samples 0/1.5/3.9s.
The helper passes each argument separately. Completion freezes the simulation so the
film includes an ending hold. Play the actual MP4 and inspect all sample PNGs.

Expected visible sequence: pale player starts left; three gold lights disappear
in order; exit becomes mint; COMPLETE is visible at the ending. A filename,
engine process acknowledgement, valid container or different image hash does
not establish this sequence. The report deliberately retains
`visual_inspection_required: true`; a person must inspect the result.

No full film was obtained here. The display connection returned EPERM. No
additional graphical attempts or dummy/headless video were used. Full
production acceptance remains open. PFAD's `ci-capture-candidate.md` supplies
a precise normal public-runner proposal; it is evidence only after it runs and
a reviewer views the artifact.

## Conditional handbook-tool handoff:95-110 block

The historical progression includes W10's handbook embedding index and
retriever tool. Keep this dependency visible, with a maximum 3-minute handoff:
if W10 has supplied its verified current PDF/chunks, real encoder identity,
dimension/source metadata and actual retriever observations, show one exact
source-backed tool result before choosing a scene action or answering a
question. The same compatible embedding space must survive the handoff. Keep
knowledge/index separate from conversation history and current scene config.

At this authoring point the source/index proof has not been supplied. Do not
invent a bundle, quote a fake page, describe keyword matching as semantic
retrieval or claim this starter searched the handbook. Mark that handoff
**unverified dependency**, then use the reserved time for evidence comparison.
This preserves the approved concept and records the gap; it does not quietly
remove retrieval from the course. The tiny-world core remains independent.

## Separate tutorial: 120 minutes

The paired `week12/README.md` is the full student/tutor route:

| Minutes | Activity |
| --- | --- |
| 0-20 | Latest standard Godot first-time bootstrap or installed check; orientation/visible play/baseline; minute 20 move to PREPARED verified partner if unfinished. |
| 20-35 | Bounded brief and actual supplied model trace; predict a check. |
| 35-55 | Human-directed bounded scene/config change and inspect observations. |
| 55-65 | Break. |
| 65-85 | Deliberate failure, reasoned adaptation, real check and stop. |
| 85-100 | Replay/capture/visual inspection; each partner retrieves own config/check/clip. |
| 100-120 | Delivery-candidate tutor support, including stragglers and existing progress-record feedback. |

A student who used Blender in W11 is explicitly supported. The first 20 minutes
include Godot installation, renderer/prerequisites and orientation; no unused
model client or bridge is installed. Warm installed Linux results are not a
cold setup measurement. Prepared-machine instructions specify Import of
`godot/project.godot`, terminal working directory, operator/observer swaps,
each learner's own check/capture, copying config/check/session/report/clip/
frames and opening the copied result on their own laptop. A recording alone
never replaces operating the tools. Rehearse this handoff before class.

## Instructor preflight and remaining gates

- Verify latest stable Godot again near 26 November. 29 October's tested runtime is
  `/usr/bin/godot` 4.7.2.stable.arch_linux.ed1daf0bf; no 4.5.1 current claim.
- Actual model/check/adapt/stop evidence exists. Complete its graphical film,
  ffprobe/decode/sample inspection and playable viewing before replacing deck.
- Time a fresh first-time graphical route on a representative machine with
  no W11 Godot/bridge setup; record platform, cold/warm assumptions, download,
  visible baseline and capture. Official Linux 4.7.2 ZIP size is 77,860,424 bytes;
  other platform sizes and all cold times remain unmeasured.
- Prepare a verified partner machine and rehearse both learners' own evidence
  retrieval. Verify Windows/macOS claims separately; no dedicated GPU needed
  is a compatibility/design intent until the graphics route is checked.
- Source and date the opening news. No release date has been inferred from
  the engine's build string. News is separate from quiz scope.
- After the gate closes, author the long deck with established fonts/palette,
  primary diagram labels >=40 design pixels, numbered flows, rich notes and real
  UI screenshots. Build/inspect HTML/PDF/plain and ClassPoint PPTX, including
  overflow checks and actual PDF. No such replacement exports exist yet.
- Keep private model-session paths/evidence out of public source. The supplied
  sanitized trace contains no credentials, student records or external sends.

The project remains 40% with 25/50/25 idea/code/execution and 6 December 2026,
23:59 HKT deadline. A public `sd5913`-owned repository with teammate Write access
is required; GitHub Projects is recommended and an equivalent accessible
record valid. Canvas is the submission system. No new grade/upload/defence,
AI feature or engine requirement is introduced. No live class or presenter
changes form part of this preparation.
