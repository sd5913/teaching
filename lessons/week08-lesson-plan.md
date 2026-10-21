# Week 8 instructor run sheet — one piece that works

**Status:** teaching draft for Thursday 29 October 2026, not a release or assessment announcement. Confirm
class length, Week 7 hand-off and group scope-agreement procedure before
teaching. The current companion is [PFAD draft PR #11](https://github.com/sd5913/pfad/pull/11)
(original head `3b7c77b8dbc4d2ef759561391d94e7917199e688` at drafting); it contains
one team activity, a tested stdlib Tile demo and an environment-inspection fallback;
Docker is an optional paper exercise, **not** a tested Docker/Compose project.
Use its merged 2026 path only after the PR is released.

## Outcome and preparation

Students should leave able to state one small user/action/response promise,
organise it as a goal and a usable increment, explain how a branch and peer
review protect the team's working version, and tell another person what code,
dependencies and safe data are needed to reproduce a run. No new submission
is created by these working notes. The existing course plan asks for agreement
on group scope by Week 8; confirm how to do that with the instructor.

Open the Week 7 mock-up and a working project's existing README. Have the deck
PDF as a no-network backup. ClassPoint is optional: the three prediction votes
also work in pairs or by show of hands. No news item has been verified for the
actual teaching date, so skip the optional news slot. No Docker access, camera,
live model, MCP installation or new student account is required.

## Suggested pacing if this meeting lasts two hours

Adjust to the confirmed schedule; the numbers are **proposed**, not the
course timetable. For a shorter meeting, cut optional containers and vision,
not the goal, review and reproducibility workshop.

| Minutes | Slide block | Ask and demonstrate |
|---|---|---|
| 0–15 | 1–8 | Recall one Week 7 mock-up. Trace visitor → tile → visible selection; inspect the tiny Tile class; have pairs choose the strongest success evidence. |
| 15–38 | 9–14 | Build goal → ordered backlog → usable increment in three consistent diagrams. Teams voice one first test. |
| 38–60 | 15–21 | Trace main → branch → PR → review → merge. Predict the same-line conflict and distinguish a text conflict from a broken combined behaviour. |
| 60–70 | — | Break / questions; move if the actual session differs. |
| 70–92 | 22–29 | Inspect a real README's code, dependencies and sample data. Predict stop vs remove and whether a mount survives; show prepared trace, not unverified commands. |
| 92–102 | 30–34 | Agent → MCP server → tool, permission check. Vision is an optional input example only. |
| 102–120 | 35–39 | Teams choose one increment, peer review path, repeatable run steps and next test; ask a few to explain a limitation. |

The colour-tile example on slide 5 uses a Python function returning a dictionary;
slide 6 adds a tiny runnable Tile class with individual state. Neither is a
complete interactive/audio application. Ask
what a second visitor must actually see and how to tell a failed speaker from
a failed click. Slide 7 is a prediction activity before the answer appears.
Slides 10–12 and 16–18 use stable geometry to reveal one relationship at a
time; keep detailed explanations in notes rather than on the drawings.

## Environment activity / honest fallback

For slide 24, choose one project with known local run steps. Partners locate
the entry command and a shareable sample input, predict a missing dependency,
then edit the instructions to make one observation repeatable. Local uv is a
valid route. Slides 25–29 show a **conceptual**, not measured, Docker trace:
stop/restart the same container retains its writable layer; removing and
recreating loses unmounted writes; reconnecting the same bind mount or volume
preserves mounted data. An explicitly removed volume does not survive. A
volume exists independently of a running container. Show the trace/diagram
if the classroom host has no preflighted Docker example. Never ask students
to join a privileged Docker group or mount personal folders/secrets. Service
start order does not establish readiness: verify with a successful request or
health check if a later live example is prepared.

For slides 31–33, describe an illustrative read-only request on a safe sample
README. A tool advertisement or model proposal does not grant permission to
delete files. No real destructive call is part of this lesson. For slide 34,
a pointer or supplied coordinate sequence can replace a camera; capture is
opt-in, no upload by default, and visual input is not evidence of emotion.

## Source reconciliation

The supplied 2025 Week 8 PDF (62 pages) is historical evidence. Retained:
goal questions (p. 9), Scrum goal/backlog/increment vocabulary (pp. 19–23),
branch/review choices (pp. 24–29), image/container/volume ideas (pp. 30–43).
Replaced: the archived Dec 1 deadline, team-size/Blackboard instructions
(pp. 4–8); mandatory Docker installation and multi-container model commands
without preflight (pp. 30–43); the inaccurate statement that a volume needs
a running container to be accessible (p. 34). Moved to optional connection:
OpenCV/MediaPipe/diffusion (pp. 44–49, 51–61), not a parallel practical.
The 2026 Week 7 idea/mock-up and current PFAD PR #11 supply the immediate
student task. Agent → MCP → tool and explicit permission boundaries extend
the historical agent recap (pp. 11–16) for the current teaching direction;
they are illustrative, not a compulsory project architecture.

## Release checks still needed

- Confirm class duration, group-scope process and Week 7 hand-off; class date is Thursday 29 October 2026.
- Confirm student companion PR release and update the draft link in speaker notes
  if its destination or instructions change.
- If a live Docker example is added, preflight image, commands, storage and
  cross-platform permissions on the classroom machine; the deck deliberately
  promises only a prepared trace.
- Optional news needs event/publication dates, primary source and a tested/not-
  tested distinction close to class; omit if none qualifies.
