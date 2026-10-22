# Week 8 instructor run sheet — one piece that works

**Status:** draft for Thursday 29 October 2026, not a release or assessment
announcement. Confirm class length, Week 7 hand-off and group scope-agreement
procedure before teaching. The [PFAD companion PR #11](https://github.com/sd5913/pfad/pull/11)
contains the student activity; use its merged 2026 path only after release.

## Outcome and preparation

Students should turn a Week 7 idea into one testable increment, describe a
branch/PR review path, and give another person safe repeatable run steps. They
should distinguish GitHub Actions environment secrets from Codex cloud task
settings, then map one hand position to a visible tile choice. No new graded
submission or required account is created. The existing course plan calls for
agreement on group scope by Week 8; confirm the actual route with Gio.

Open a Week 7 mock-up, a working project's README, and the Week 8 companion.
Use the deck PDF as a network fallback. The prediction votes also work in
pairs if ClassPoint is unavailable. No news item is verified for this date,
so omit the optional slot. Prepare the supplied coordinate trace; use a live
camera only after installation, permissions and the no-hand state have been
checked on the classroom machine. No real API key, paid service, Docker or
new student account is required.

## Suggested pacing if the meeting lasts two hours

Adjust to the confirmed timetable. For a shorter session, omit the live
camera, not the goal, review, safe-setup comparison or team workshop.

| Minutes | Block | Ask and demonstrate |
|---|---|---|
| 0–15 | From Week 7 to one loop | Trace visitor → tile → visible response. Read the tiny Tile class and ask what would test the idea. |
| 15–38 | Goal and increment | Order a short backlog and choose one usable slice. Teams state a first test. |
| 38–60 | Branch and review | Trace main → branch → PR → review. Predict a text conflict and a broken combined behaviour. |
| 60–70 | Break | Shift to fit the actual class. |
| 70–90 | Repeatable and safe setup | Inspect README run steps and sample data; sort invented public settings versus secrets. GitHub Actions and Codex cloud have separate environments. |
| 90–107 | MediaPipe input | Predict x = 0.2 and 0.8, try the supplied trace, then remove input. Compare an opt-in live camera only if preflighted. |
| 107–120 | Team workshop | Choose an increment, reviewer, repeatable steps and next test; ask teams to name one limitation. |

The tile function and tiny Tile class on the early slides show response and
per-object state, not a complete interactive/audio application. Ask what a
visitor must actually see; a sound is optional. The goal/backlog/increment
and branch/PR diagrams reveal one relationship at a time.

## Environment comparison

A GitHub Actions job explicitly targets a GitHub environment for its scoped
settings and any protection rules; a Codex cloud task uses its own environment
configuration. Neither receives the other's secrets automatically. An
environment variable is not automatically a secret. Work through fake labels
such as `DEMO_TOKEN` without putting any actual value into code, screenshots,
PRs or logs. No one needs to create an account or configure a secret today.
See [GitHub environments](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)
and [Codex cloud environments](https://developers.openai.com/codex/environments/cloud-environments).
If a real key is exposed, revoke/rotate it; deleting a commit is insufficient.

## Hand position to visible response

A consented camera frame can yield MediaPipe hand landmarks. The optional
camera mode mirrors the frame and takes landmark 8 (index fingertip) as a
normalized x coordinate: x < 0.5 selects blue; x >= 0.5
selects red. A missing or invalid hand is explicitly **no input**, not a new
detection or a fake success. Have pairs predict the supplied no-camera trace
before running `python -B week08/hand_tiles.py` from the PFAD repo root.
It exercises the mapping with 0.20, 0.49, 0.50, 0.80 and None, not the
MediaPipe detector. If the
camera demonstration was preflighted, compare the actual hand position and
visible feedback with that trace. A pointer control is also valid. Do not
record, upload or infer a person's emotions from a frame. Confirm the
companion's `--camera --model` command and device requirements before class;
the model is manually downloaded outside the repo, and `q` exits the tile
window. The course-node optional inference was blocked by missing
`libEGL.so.1`, so classroom camera behavior remains unverified.

## Source reconciliation

The 2025 Week 8 PDF (62 pages) supplies project goals (p. 9), Scrum vocabulary
(pp. 19–23), Git collaboration (pp. 24–29), and hand/visual input ideas
(pp. 44–49, 51–61). Its Docker/Compose block (pp. 30–43) is **omitted from the
2026 Week 8 core**, not adopted as a requirement; historical dates, team size
and Blackboard instructions also do not carry over. The GitHub/Codex
safe-setup comparison is a new current-year addition, not archived content.
The Week 7 idea/mock-up and current PFAD Week 8 PR supply the student task.

## Remaining release checks

- Confirm class duration and group-scope process without inventing a submission.
- Verify the student companion's final commands and updated draft links before
  classroom use; run its no-camera tests and preflight the optional camera.
- If adding near-class news, verify primary source, dates and what was tested.
