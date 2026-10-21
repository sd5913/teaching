# SD5913 Week 8 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week08`, not an announcement to students. The 39-slide deck and instructor run sheet are now authored in this draft PR; confirm companion release and classroom conditions before teaching.

## Status and source limits

- Teaching date: Thursday 29 October 2026 (confirmed by gio). Content week numbers are not calendar-week numbers after the 1 October holiday; this is not an assignment deadline.
- Candidate focus: **Team workflow and reproducible projects**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 8 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This PR now registers a Week 8 deck and site card **in source only**; no deployment, assessment change or publication has occurred.

The supplied historical PDF is titled Goal-setting and Teamwork. Its main progression is project goals → Scrum → Git teamwork → Docker, followed by vision examples. The current course requires scope agreement by Week 8. Keep that backbone visible before deciding whether to redistribute its heavy optional material.

## Supplied historical slide evidence

SD5913 - PFAD - Week 8.pdf (62 pages): pp. 4–9 project and team framing; 11–18 agent/global-variable recap; 19–23 Scrum; 24–29 Git collaboration; 30–43 Docker and Compose; 44–49 visual-input/diffusion examples; 51–61 camera and container tutorial. Text extracted throughout; screenshot-heavy pages 12–13, 26–27, 32, 36–40, 45–46, 48–49 and 60 visually inspected.

Page numbers are 1-based PDF pages. These are historical materials supplied for review; the PDF itself is not copied into this public repository. Historical dates, marks and team arrangements are not adopted.

## Proposed learning outcome

Turn a team goal into one small usable increment, describe the branch/PR review path, and explain what must be reproducible for another person to run the project.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Revisit the Week 7 idea and mock-up. Define intended user, useful response, success evidence and the riskiest assumption before agreeing scope.
2. Use the archive's Scrum sequence to distinguish a product goal, ordered backlog, one short sprint goal and a usable increment. Adapt the vocabulary to a small student team without imposing formal roles or new grading rules.
3. Walk one change through a branch, small commits, a pull request and peer review. Students predict where two changes could conflict and what evidence a reviewer needs.
4. Explain image versus running container, host versus container, and code/data persistence with one minimal diagram and an instructor-prepared example. Docker is an option, not a new compulsory installation.
5. Keep OpenCV/MediaPipe or diffusion as a short optional connection to future interactions, not a second complete core lesson. Teams leave with one next test and a runnable-project checklist.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Visual-input agents, multimodal interfaces or agent-assisted prototyping. Tie any item to what inputs a program can inspect and how a student would test its claims.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Retain a visible map of Scrum, Git teamwork, Docker and networks before changing their sequence. Include an agent → MCP server → tool explanation and a bounded permission-aware practical at the appropriate point; a model suggestion alone must not be treated as permission to act. This does not require AI inside every team project.

## Materials to develop in this PR

- [x] Reconcile the supplied slide record with the current 2026 sequence and identify what is retained, replaced or moved in `lessons/week08-lesson-plan.md`.
- [x] Draft the learning outcome and an adjustable two-hour run sheet; **actual duration and scope-agreement procedure remain unconfirmed**.
- [x] Author a progressive full-slide diagram deck with short labels and detailed notes. Follow AGENTS.md; primary diagram labels target at least 40 design pixels on a 1920 × 1080 slide.
- [x] Include a worked example, prediction/inspection activities and failure cases (merge conflict, lost unmounted data, denied tool call).
- [x] Align to the draft [PFAD companion PR #11](https://github.com/sd5913/pfad/pull/11) (original head `3b7c77b8dbc4d2ef759561391d94e7917199e688`); it now has a tested stdlib Tile demo, while Docker remains an optional paper exercise, not a tested Docker example. The companion release is pending.
- [ ] Select and verify the week's news using the criteria above.
- [x] Review story order, tests and diagrams in this same PR; reserve workshop and discussion time.
- [x] Build the 39-slide draft with pinned deckgen and inspect diagram previews; classroom preflight remains pending.

## Gaps and decisions

- Confirm how much of Scrum/Git/Docker should stay together in this year's Week 8 before moving vision or containers to another week.
- Confirm the scope-agreement procedure and existing group brief; do not import the archived Dec 1 deadline, maximum-three team rule or Blackboard workflow.
- Select a minimal environment example and check classroom Docker access without requiring privileged account changes. Retain the existing uv/local route.

## Guardrails specific to this week

Archived team size, dates and Blackboard instructions are not current policy. Correct rather than repeat the claim that volumes require a running container. Keep privileged Docker-group changes out of the student task. Container start order is not proof a service is ready; a prepared fallback should work without live models or a camera.

Across every week, preserve the existing assessment weights and confirmed dates. Individual Assignment 3 is separate from the group project. Do not add team-size rules, compulsory AI/audio, new grading criteria, submission formats or deadlines. Never commit student records, private submissions, quiz questions/keys or credentials. Do not merge, publish to Canvas, deploy the course, or change automation as part of this plan.

## Source record

Current-course anchors inspected for this plan:

- [Teaching README](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/README.md): source layout, builds, numbering/date caution and privacy rules.
- [Current Week 1 deck](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/deck/week01.py): assessment structure, Week 8 scope agreement and Week 13 final quiz.
- [Week 6 instructor plan](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/lessons/week06-lesson-plan.md): established depth, progression, fallbacks and verification conventions.
- [Week 7 draft PR](https://github.com/sd5913/teaching/pull/10), reviewed at `31c675b4085f771da6340878f3a54d7018f1015d`: team ideation and separate individual/group assessment framing.
- [Current student index](https://github.com/sd5913/pfad/blob/2026/README.md): this year's material, not the archive syllabus.

Historical candidates, inspected as source inventory only; not claimed to run on current dependencies:

- [2025 week08/README.md](https://github.com/sd5913/pfad/blob/2025/week08/README.md)
- [2025 week08/2_hand_tracking.py](https://github.com/sd5913/pfad/blob/2025/week08/2_hand_tracking.py)
- [2025 week08/5_gesture_recognition.py](https://github.com/sd5913/pfad/blob/2025/week08/5_gesture_recognition.py)
- [2025 errata](https://github.com/sd5913/pfad/blob/2025/ERRATA.md): known code, slide and assessment inconsistencies.

## Verification record

The initial planning-only draft now includes the Week 8 deck, original diagrams, speaker notes and the small executable Tile example. The author reports targeted builds and visual review in this PR; those records must be distinguished from independent checks and classroom-device testing. The current review follow-up corrects this stale status paragraph. Before classroom release, verify the latest commit's applicable tests and affected exports, inspect presentation-size diagrams, and preflight the matching PFAD practical. No live model, camera or classroom-device result is claimed by this paragraph.
