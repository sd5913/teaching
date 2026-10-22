# SD5913 Week 8 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week08`, not an announcement to students. The deck and instructor run sheet are authored in this draft PR; confirm companion release and classroom conditions before teaching.

## Status and source limits

- Teaching date: Thursday 29 October 2026 (confirmed by gio). Content week numbers are not calendar-week numbers after the 1 October holiday; this is not an assignment deadline.
- Candidate focus: **Team workflow and reproducible projects**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 8 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This PR now registers a Week 8 deck and site card **in source only**; no deployment, assessment change or publication has occurred.

The supplied historical PDF is titled Goal-setting and Teamwork. Its progression was project goals → Scrum → Git teamwork → Docker → vision. Gio's 2026 direction retains team planning and Git review, replaces Docker with a safe environment/secrets comparison, and makes one MediaPipe hand-to-tile input exercise concrete. The course still requires scope agreement by Week 8.

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
4. Inspect repeatable run instructions and compare GitHub Actions environment secrets with Codex cloud environment settings using invented labels, not actual credentials.
5. Map a MediaPipe index fingertip position to a visible tile choice, then test the same mapping with a supplied no-camera trace. Teams leave with one next test and a runnable-project checklist.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Visual-input agents, multimodal interfaces or agent-assisted prototyping. Tie any item to what inputs a program can inspect and how a student would test its claims.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Keep Scrum and Git teamwork here; networks follow in Week 9 and saved data in Week 10. The agent → MCP server → tool trace belongs later in the sequence; a model suggestion alone is not permission to act. AI need not be inside every team project.

## Materials to develop in this PR

- [x] Reconcile the supplied slide record with the current 2026 sequence and identify what is retained, replaced or moved in `lessons/week08-lesson-plan.md`.
- [x] Draft the learning outcome and an adjustable two-hour run sheet; **actual duration and scope-agreement procedure remain unconfirmed**.
- [x] Author a progressive full-slide diagram deck with short labels and detailed notes. Follow AGENTS.md; primary diagram labels target at least 40 design pixels on a 1920 × 1080 slide.
- [x] Include a worked example, prediction/inspection activities and failure cases (merge conflict, exposed key, missing hand).
- [ ] Confirm the final commands and fallback of the updated [PFAD companion PR #11](https://github.com/sd5913/pfad/pull/11). Its release is pending.
- [ ] Select and verify the week's news using the criteria above.
- [x] Review story order, tests and diagrams in this same PR; reserve workshop and discussion time.
- [ ] Rebuild the revised draft with pinned deckgen and inspect diagram previews; classroom camera preflight remains pending.

## Gaps and decisions

- Confirm the classroom camera and MediaPipe installation before promising a live demonstration; the offline coordinate trace remains the baseline.
- Confirm the scope-agreement procedure and existing group brief; do not import the archived Dec 1 deadline, maximum-three team rule or Blackboard workflow.
- Use a fake configuration/secret classification; never require students to set up a GitHub or Codex account or handle a real key. Retain the existing uv/local route.

## Guardrails specific to this week

Archived team size, dates and Blackboard instructions are not current policy. The Docker/Compose content is archival rather than a Week 8 requirement. A no-camera trace tests the coordinate mapping, not MediaPipe detection; do not record or upload footage, infer emotion, or show actual secrets in logs.

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

The original 39-slide draft was reviewed with targeted builds. After Gio's 22 October change of direction, that verification is stale for the revised content. Before classroom release, verify the latest commit's tests and affected exports, inspect presentation-size diagrams, and preflight the matching PFAD practical. No live camera or classroom-device result is claimed here.
