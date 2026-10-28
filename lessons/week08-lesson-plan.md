# Week 8 run sheet — Thursday 29 October 2026

Two-hour lecture plus a two-hour TA-led PFAD tutorial. Week 8 is the source
module; do not rename it to match the calendar week.

| Minutes | Lecture | Action |
| --- | --- | --- |
| 0–10 | Project, opening and news | Poll: game, app, installation or another direction; brief news discussion; explain Canvas repository submission and 25/50/25 group rubric. |
| 10–30 | Agile, Scrum and tracking | Brief Week 1 Manifesto recap; iterative/incremental development; Scrum pillars, accountabilities, artifacts/commitments and events. Show the iterative course Project template, tutor delivery dates and issue-to-PR link. Connect the evidence to the 25% execution mark. |
| 30–45 | Git teamwork | Work through branch, edit, commit, push, PR, teammate review, merge and updating main. Resolve the simple same-line conflict. |
| 45–60 | Codex cloud | Use prepared repositories and setup commands: five minutes each to create Capacitor and Godot environments, five minutes for one task/check/review. Mention the Python option; retain a prepared-environment fallback. |
| 60–70 | Break | Set up the camera and light. |
| 70–85 | Actions and delivery | Follow CI to artifacts; use Tetrilaunch's OS matrix and mobile workflows; show secret creation with fake values and provider deployment token. |
| 85–93 | Frames and Python objects | Connect pixels, channels, the camera object and its read method to Week 7 classes; introduce the tracker and model asset. |
| 93–105 | Landmarks to interaction | Run face/hand and fingertip-to-tile; trace the result, no-hand case, threshold and pixel coordinates. Ask students to predict the threshold outputs. |
| 105–115 | Other model outputs | Show gesture and pose or segmentation; compare outputs, tracking loss and limitations. Choose the second demo according to time. |
| 115–120 | Tutorial handoff | Open PFAD README; explain the nine examples and optional group cloud work. |

## Preflight

- Reconcile registered GitHub accounts and submission verification against sd5913
  membership; have students accept the organization invitation. Members can
  currently create public repositories. Demonstrate **Owner: sd5913** when
  using a template and give teammates Write access to their own repository.
  Preserve history when helping transfer an existing personal repository.
- Prepare a GitHub Projects Board demonstration with repository issues, assignees,
  Status and weekly Iteration. Use the [Group Project 2026 template](https://github.com/orgs/sd5913/projects/1):
  students choose it in sd5913 > Projects > New project. Show Current iteration,
  Next iteration, Team board and Delivery dates. Use a prepared group copy for
  changes. Repository links and collaborators are not copied from the template.
  Check board access separately from repository
  access. The slide board is illustrative. Inspect built-in workflows before
  claiming automatic status updates; closing keywords apply to PRs targeting the
  default branch. Do not create or modify student tracking during the lecture.
  Create any demonstration copy under sd5913. Students give their teammates
  Write access to the group's Project separately from repository access; set
  each Project's base access for other members to Read or No access.
- Verify the three template repos and Actions artifacts, GitHub account permissions,
  setup and a pre-created Codex cloud environment. Publishing the environment is
  not a deployment. Check external links and current account UI.
- Prepare the PFAD Week 8 environment and download models from its README. On
  the presentation machine, test real camera, lighting, display, q-to-quit,
  hand-tile model and transitions between examples. Prepare a short recording
  or screenshots as a fallback; do not call a headless inference test a camera
  rehearsal. Never capture or show identifiable people without consent.
- Confirm Canvas group assignment, Website URL submission, actual link and
  availability. Deadline: 6 December 2026, 23:59 HKT. Link the real Canvas
  page when available; the public brief is in PFAD. Do not disclose keys.
- Opening ClassPoint question has a show-of-hands fallback. TA exercises do not
  depend on the instructor's account. No new tutorial submission is required.

## Agile/Scrum learning and quiz scope

The Manifesto's four values appeared in Week 1. Revisit them briefly, including
the fact that the right-hand items still have value, then apply the concepts to
the team project. Teach iterative versus incremental development; transparency,
inspection and adaptation; Product Owner, Developers and Scrum Master; Product
Backlog/Product Goal, Sprint Backlog/Sprint Goal, Increment/Definition of Done;
and the Sprint containing Planning, Daily Scrum, Review and Retrospective.
Distinguish the product review from improving how the team works. A Sprint is
one month or less; the Daily Scrum is a 15-minute event for Developers.

GitHub Projects and Issues support the process; they do not define Agile or
Scrum. Show an issue's intended outcome and check, owner, Status, optional
Iteration, linked PR and review evidence. Use the final scenario to check that
students can distinguish closed cards from a usable, verified Increment.

Execution remains exactly 25% of the group-project mark: small, steady
increments and documented weekly progress, explained through planning,
contributions, review and adaptation. Recommend GitHub tracking or an equivalent
accessible record linked from the README. Do not grade raw commit/card counts,
formal job titles or ceremony attendance. No extra Canvas upload is introduced.
Student revision and setup guide: PFAD `week08/teamwork.md`.

## Remaining tutor delivery reviews

The [course Project template](https://github.com/orgs/sd5913/projects/1) adapts
the iterative-development structure to one-week cycles from 29 October. It
includes dated draft cards that copy into each group's Project with their field
values. Students add repository issues for feature work and select the relevant
Iteration; record the shared goal as well as moving cards.

| Thursday class week | Delivery focus |
| --- | --- |
| 5 November | First working interaction |
| 12 November | Integrated core experience |
| 19 November | Playtest and feedback |
| 26 November | Delivery candidate |
| 3 December | Final tutor delivery review |

These identify teaching weeks, not additional appointment times. Each group
meets its assigned tutor in its scheduled tutorial slot; the tutor confirms the
exact time. Bring a usable increment, evidence and blockers. Update the review
card with tutor feedback and the next goal with owners. Adapt the focus with the
tutor where appropriate to the project. The final 6 December, 23:59 HKT card is
a separate Canvas deadline. Reviews support the existing execution criterion;
there is no extra grade component, attendance score or Canvas upload. Keep this
template walkthrough within the existing 20-minute block.

Primary sources: [Agile Manifesto](https://agilemanifesto.org/), its
[principles](https://agilemanifesto.org/principles.html), the
[2020 Scrum Guide](https://scrumguides.org/scrum-guide.html), and
[GitHub Projects quickstart](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects).

## Tutorial: 120 minutes

TA uses `pfad/week08/README.md`: setup and camera 15 min, face/hand/pose 25,
mesh/gesture 20, break 10, combined/segmentation 20, multi 10, separate emotion
classifier 10, optional inspiration discussion and team setup 10. Modern MediaPipe Tasks
replace archived `mp.solutions`; 2025 sources are linked for comparison. Explain
that classifier labels do not establish a person's feelings. If someone has no
camera, work with a consenting partner and use the sample-coordinate fallback.
