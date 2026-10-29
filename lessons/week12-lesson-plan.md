# Week 12: an agent builds, checks and films a tiny world

26 November 2026. **120-minute lecture, plus a separate 120-minute PFAD tutorial.**
Authoring status 29 October: the actual model/check/adapt/stop episode, later real
film and timed isolated Linux operator bootstrap pass. The replacement 44-slide
deck now implements this run sheet; the former 21-slide addition/permission
lesson is historical. Independent review/classroom preflight remain separate.

Runnable PFAD source is pinned at
https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12 .
The world core is self-contained and no live presenter or remote class is used.
The short W10 handoff now uses a verified real prepared-vector observation;
the world does not import or search that index.

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
| 0-10 | Opening: “What evidence would make you trust a game built by an agent?” Give the one-player/three-lights/exit brief. Use at most 3 minutes for the sourced Godot 4.7.2 release watch (18 August publication, verified 29 October; refresh near class). The remaining time lets pairs name a behavior check and a visual check. |
| 10-30 | Agent versus workflow: use the scene/config/process/output map and Python excerpts below. Distinguish choosing a next action from executing a fixed list. Predict speed 125 over 180 ticks; explain eight actions/four mutations/180 seconds and the stop rule. Full-width numbered diagrams carry the relationships; notes carry explanation. |
| 30-50 | Analyze the actual recorded model decisions from supplied125 through failure/revision/pass/stop, then run the same tools human-directed with the caller identified. Read each observation aloud. A fresh configured model is optional if already authorized/available; neither the recorded trace nor human choice is labeled a fresh model episode. |
| 50-60 | Read the real recorded trace: students label proposed action, applied write, engine result and stop decision. Predict what reaching the exit with 0/1/2 lights should do; run those checker cases. Ask what the successful check still does not establish. |
| 60-70 | Break. Stop visible playback; keep sources/evidence available. |
| 70-95 | Deterministic replay and capture, on the verified graphics path. Predict 120 rendered frames at 30 fps versus 60 physics ticks/s, then run the commands below. Decode/check metadata and inspect beginning/middle/end images plus the playable clip. Trace the same `advance` method. Ask why a valid MP4 can still show the wrong result. |
| 95-110 | Compare evidence and limitations: fixture versus current run, real checks versus visible result, stale file versus restarted state, timeout/display failure versus behavior failure. Optional frontier comparison fits at most 3 minutes and needs a fresh primary source; otherwise spend this time on a partner's unsupported-success challenge. The verified W10 handoff below uses the actual source/index result. |
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

Explain these short Python paths using `deckgen.CODE` in the deck:

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

On the preflighted graphics path, use:

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

Actual graphical film now passes. The exact original model-selected final
source was captured on real Godot 4.7.2/Xvfb/Mesa, then fully decoded, played and
sampled. The current stronger capture helper passed independently. Public
reference clip/stills and private-path-free provenance are in PFAD
`week12/evidence/`. The earlier display EPERM remains in the historical trace;
full local access later supplied a different working graphics path. No dummy
frames or scripted repair were substituted for the genuine model episode.
The public-CI candidate remains unrun; it is not evidence of a successful runner.

## Verified handbook-tool handoff:101-104 inside the95-110 block

Use at most3minutes to compare the two observations. W10's actual prepared
lost-card query returns `hb2026-p020-replacement` (PDF position20, printed9),
cosine0.815428; next is return chunk0.763087. The author independently ran the
real VectorIndex search, using its stored genuine query vector. This direct
retriever check is not a fresh model call. W10 exposes `retrieve_handbook` as
its agent tool; no world dependency or sibling import is introduced.

The paired `handbook-handoff.json` retains source, encoder identity/revision,
matching query-vector/bundle hashes and actual result text/page/score. Official
2026/27 PDF SHA108956feb2ffac665f8ca0f5a8f68d7150a85fda15e219916785ec50331a4e94;
encoder `sentence-transformers/all-MiniLM-L6-v2` revision
1110a243fdf4706b3f48f1d95db1a4f5529b4d41, dimension384, attention-masked mean,
L2-normalized,max_tokens256. Preserve this space for both document and query
vectors. Six short extracts from PDF20/25/76 are not the entire137-page PDF.

Trace four lifetimes: index knowledge persists across calls; scoped saved
conversation rows reopen; the current prompt assembles history and tool results;
spoken output is derived and checked separately. Current scene config is none
of those. This keeps the source-supported retrieval progression visible without
turning the tiny-world practical into another handbook installation.

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
model client or bridge is installed. A fresh official Linux engine download took 9.484 seconds. Active isolated
import/check/capture/pair turns took 31.215 seconds including that download;
full editor/2D orientation and normal quit added 29.312 seconds in a follow-up
stage. These are scripted operator feasibility measurements, not continuous
novice/student or Windows/macOS timing. Existing uv/Python/FFmpeg/Xvfb/Mesa were
prerequisites. The prepared-machine route still specifies import, terminal
working directory, operator/observer swaps, own config/check/capture and exact
evidence retrieval/opening on the learner's laptop. Both simulated learner
copies passed their own turn and copied-clip decode/config-identity checks.
A reference recording alone never replaces operating the tools.

## Instructor preflight and remaining gates

- Verify latest stable Godot again near 26 November. 29 October's tested runtime is
  `/usr/bin/godot` 4.7.2.stable.arch_linux.ed1daf0bf; no 4.5.1 current claim.
- Model/check/adapt/stop, exact final-source film and actual current helper
  capture passed. Each classroom run still needs fresh behavior and visual checks.
- Linux operator bootstrap passes within 20 minutes with a fresh 78 MB engine;
  existing Python/FFmpeg/software graphics are prerequisites. Other platforms,
  slow downloads and novice setup need instructor preflight and minute-20 handoff.
- Verify the actual prepared partner machine and each learner's own retrieval;
  the simulated two-turn route passed on isolated source copies.
- Refresh the dated release-watch item before 26 November; news is outside quiz.
- Keep the full 44-slide deck, useful notes and>=40 px diagram labels. Build and
  inspect HTML/PDF/plain/ClassPoint PowerPoint with overflow checks enabled.
- Retain the verified W10 source/index/tool observation and final source pin.
- Keep private paths, raw credentials and student records outside public source.
  Independent review, coordinator integration and classroom rehearsal follow.

The project remains 40% with 25/50/25 idea/code/execution and 6 December 2026,
23:59 HKT deadline. A public `sd5913`-owned repository with teammate Write access
is required; GitHub Projects is recommended and an equivalent accessible
record valid. Canvas is the submission system. No new grade/upload/defence,
AI feature or engine requirement is introduced. No live class or presenter
changes form part of this preparation.
