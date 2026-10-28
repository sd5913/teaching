# Week 13: revision, final quiz and delivery support

Prepared 29 October 2026 under the approved remaining-course production plan.
**Final class date and tutorial arrangements TBC.** Instructor confirms the
final Canvas quiz **10:00-10:30 HKT, 30 minutes**, matching the midterm. This
confirmation establishes neither question count/format nor tool permissions.
The class is 120 minutes; the separate PFAD final-support tutorial is also
120 minutes. No new technical practical or compulsory project defence.

## Outcomes and boundaries

Students diagnose state, messages, persistence, source/context and tool/check
boundaries using taught examples; explain why evidence supports a result; and
identify a small, reproducible project fix. Public traces are ungraded revision
examples, not copied/private quiz questions or keys. News is outside quiz scope.

**Delivery gate:** Week 7 classes and Week 8 teamwork/vision are merged. Weeks
9-12 are approved production drafts at preparation, not yet delivered or fully
readiness-proven. Before class, reconcile the scope in `week13-planning.md`
with actual delivered lessons and evidence. Do not treat a future draft as
proof of teaching, or use a replay to claim a live agent was verified.

## Full 120-minute class

This **example assumes a 09:30 start** so the confirmed quiz falls at minutes
30-60. Final date/start and any changed tutorial arrangement must be confirmed.
Only 10:00-10:30 HKT is a confirmed clock-time instruction.

| Minutes | Example clock | Material and teaching action |
| --- | --- | --- |
| 0-15 | 09:30-09:45 | Slides 1-5: orient; state alias prediction (7 min including opening), uncertain message (4), Git handoff (4). Optional sourced news, if refreshed, takes at most 90 seconds from opening, never quiz time. |
| 15-30 | 09:45-10:00 | Slide 6: protected AMA. Sort questions into trace/setup/project issues; park longer paths for after break. |
| 30-60 | **10:00-10:30** | Slide 7: existing Canvas final quiz, following actual instructor/Canvas instructions. |
| 60-70 | 10:30-10:40 | Slide 8: ten-minute break. |
| 70-100 | 10:40-11:10 | Slides 9-17: choose up to three useful diagnostic routes (about 6 min each), then remaining 12 min on concrete project blockers; adapt question/support balance to need. |
| 100-115 | 11:10-11:25 | Slides 18-20: fresh-run evidence (5), access/README (5), build/credits/limits (5). |
| 115-120 | 11:25-11:30 | Slides 21-22: owners, next recheck and unchanged deadline; close. |

Do not march through all diagnostic routes after the break. Keep unused slides
as reference answers to questions. This is lean revision with real AMA/support
time, not another survey of definitions. If start differs from 09:30, reconcile
the 120-minute allocation around the fixed quiz before teaching, rather than
silently shifting the quiz window.

## Diagnostic routes and evidence

- **State:** slide 3 uses actual Week 7 `Ball(x,y,vx,vy)`. Predict whether
  assignment constructs another ball. Trace shared object state through
  `selected.update(0.1)`, then inspect `red.x`. This is aliasing, not another
  introduction to classes. The excerpt is illustrative; use the existing
  source rather than promise a new Week 13 script.
- **Messages:** slide 4 asks what a missing acknowledgement establishes.
  Draw both timelines (applied/reply lost, never applied); distinguish retry
  safety from mere reconnect. No claim that the demo implements durable
  deduplication. Invalid payload and unavailable server are different failures.
- **Rows and storage:** slides 9-11 trace a scoped SQL result, then model
  method -> committed row -> new instance after restart. Compare row identity,
  parent reference and lookup acceleration, plus storage/write cost. Transfer
  to SaveFile ownership or membership without implementing another app.
  Related rows, nested documents and source-backed vectors answer different
  retrieval questions, not rigid database product categories.
- **Retrieval/context/audio:** slides 12-13 trace compatible encoder/space,
  source IDs/text, relevance and four lifetimes. Ask why forgetting a follow-up
  differs from wrong handbook retrieval or failed audio playback. History
  must reach the subsequent model call, survive restart and remain isolated;
  a thread ID alone is insufficient. Never invent a handbook page citation.
- **Tools/agents:** slides 14-15 distinguish request, validated action, result,
  saved state, observed running app and feedback. Use the actual delivered
  tiny-world trace only after its live check/adapt/stop gate passes. Diagram
  and illustrative trace are not themselves a live model run. Compare a fixed
  workflow to model choice driven by observations and a stated stop/budget.
- **Agile/Scrum/Git:** slides 5/16 connect local/shared code, review/test,
  sprint goal, increment, review and retrospective. Ask what feedback changed
  the next decision. Progress records and commit counts are different evidence.

Each route: quiet prediction, one student's reasoning, inspect code/data,
resolve disagreement using evidence, then one transfer question. If the topic
was not delivered, omit that route from revision/quiz preparation; do not teach
it for the first time on final day.

## Existing commands and fallbacks

From the **PFAD root** (merged course checkout):

```bash
uv run week07/ball.py
```

Expect the explicit red-only update followed by blue's update. Inspect
`week07/ball.py`, `Ball.update()` and the constructor. Running the alias excerpt
with that class prints matching x values. No GUI, accounts or model download.
From PFAD `week08`, the already taught no-camera route is:

```bash
uv run python hand_tiles.py
```

Use its README to inspect sample coordinate mapping, including no-hand input.
Stop before adding a camera requirement. For later-week recovery use the
**delivered** Week 9/10/11/12 README, not guessed filenames/version commands.
Do not add engine/model downloads to final support.

The existing optional Week 13 loop remains in PFAD, outside the core class:

```bash
cd week13
uv run loop.py
uv run loop.py 0
python3 -m unittest discover -s . -p test_loop.py
```

Normal output is `0`, `1`, `2`, `done`, each on its own line; zero prints
`done`. The two existing tests run real subprocesses. Removing the increment
is a paper-only nontermination prediction. The support route does not require
this exercise. If any run is unavailable, trace source and instructions and
record the limitation; that does not count as a verified fresh/live run.

## Separate 120-minute final support tutorial

PFAD `week13/README.md` is the complete student/TA route: 0-15 triage; 15-45
setup/run/core blockers; 45-60 peer fresh-run; 60-70 break; 70-100 final tutor
review/fixes; 100-115 README/build/access/credits; 115-120 owners/actions.
Scheduling remains TBC, including possible tutorial moves. Tutors prioritize
startup/core blockers, while working teams test and improve instructions.
No instructor login/ClassPoint session, new upload or defence is required.

## Assessment and delivery

Group project 40%; project rubric 25% idea / 50% code / 25% execution; deadline
**6 December 2026, 23:59 HKT**. Shared public `sd5913`-owned repository,
teammate Write access. GitHub Projects is recommended; equivalent accessible
progress record valid. Project permissions are separate from repo permissions.
Canvas remains the submission system; open the actual assignment and check
submitted URL, without inventing a link or settings. No new grade, mandated
technology, video, app-store release or compulsory defence.

## Before classroom use

Confirm final class date/start and tutorial arrangements; verify Canvas quiz
availability and instructor instructions; reconcile delivered scope; refresh
optional dated news or omit it; verify pinned companion/source links; rehearse
selected existing command and actual display/audio if used; inspect final
HTML/PDF and both PowerPoints. Native previews are not browser/PDF proof.
No remote class or student project was run during this authoring task.
