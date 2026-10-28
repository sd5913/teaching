# Week 8 run sheet — Thursday 29 October 2026

Two-hour lecture plus a two-hour TA-led PFAD tutorial. Week 8 is the source
module; do not rename it to match the calendar week.

| Minutes | Lecture | Action |
| --- | --- | --- |
| 0–10 | Project, opening and news | Poll: game, app, installation or another direction; brief news discussion; explain Canvas repository submission and 25/50/25 group rubric. |
| 10–30 | Teamwork | Work through branch, edit, commit, push, PR, teammate review, merge and updating main. Resolve a simple same-line conflict. |
| 30–55 | Codex cloud | Create environments for both starter repos, review setup, publish and start a small task. Keep a prepared environment available. |
| 55–65 | Break | Set up the camera and light. |
| 65–85 | Actions and delivery | Follow CI to artifacts; use Tetrilaunch's OS matrix and mobile workflows; show secret creation with fake values and provider deployment token. |
| 85–115 | OpenCV and MediaPipe | Live camera: preview, face, hand, fingertip-to-tile, gesture, pose or segmentation. Show tracking loss and source links. |
| 115–120 | Tutorial handoff | Open PFAD README; explain the nine examples and optional group cloud work. |

## Preflight

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

## Tutorial: 120 minutes

TA uses `pfad/week08/README.md`: setup and camera 15 min, face/hand/pose 25,
mesh/gesture 20, break 10, combined/segmentation 20, multi 10, separate emotion
classifier 10, application and optional team setup 10. Modern MediaPipe Tasks
replace archived `mp.solutions`; 2025 sources are linked for comparison. Explain
that classifier labels do not establish a person's feelings. If someone has no
camera, work with a consenting partner and use the sample-coordinate fallback.
