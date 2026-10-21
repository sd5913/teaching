# SD5913 Week 8 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week08`, not a finished deck or an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Project scope and visual input**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 8 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. Historical slides are being requested separately.
- This PR adds planning text only. It does not register a deck, change the course site, set assessment requirements or publish learning material.

The current Week 1 deck and Week 7 run sheet require group-project scope agreement by Week 8. The 2025 Week 8 code explores camera input and landmarks. Project scope is confirmed; the vision lesson placement is a candidate.

## Proposed learning outcome

Describe one intended user action, the program's response, and the smallest version the team can test. For the optional vision path, distinguish camera pixels, model-predicted landmarks and a chosen interaction.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Revisit the Week 7 team idea and image mock-up; identify one user action and observable response.
2. Instructor shows a tiny visual-input pipeline, then a failure case such as occlusion or low light. Use prerecorded or synthetic input if camera access is unsuitable.
3. Pairs predict what changes when one landmark or threshold changes, then inspect the result.
4. Teams narrow one project interaction and identify its main unknown; discuss scope with the instructor under the existing Week 8 agreement.
5. Finish with a concrete next test and a record of what the team will not build yet.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Visual-input agents, multimodal interfaces or agent-assisted prototyping. Tie any item to what inputs a program can inspect and how a student would test its claims.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Materials to develop in this PR

- [ ] Reconcile the supplied slide record with the current 2026 sequence and identify what is retained, replaced or moved.
- [ ] Agree the learning outcome and teacher run sheet, with actual timing.
- [ ] Author the deck with readable full-slide diagrams, short labels and supporting detail in notes. Follow AGENTS.md; primary diagram labels should target at least 40 design pixels at 1920 × 1080.
- [ ] Include a worked example, a purposeful student prediction/inspection activity and a failure or limitation worth discussing.
- [ ] Align the matching PFAD/2026 practical README and runnable examples without promising files that do not exist. Record the companion PR link once verified.
- [ ] Select and verify the week's news using the criteria above.
- [ ] Review the lesson for coherent progression, accuracy, appropriate depth and time for questions; revise in this same PR.
- [ ] Build and visually inspect the actual finished deck before calling it classroom-ready.

## Gaps and decisions

- Confirm whether vision belongs in Week 8 this year and supply the later slide record.
- Confirm the scope-agreement procedure and any existing project brief; do not invent a new graded submission.
- Decide the supported camera/model route and rehearse permissions, missing-camera and low-confidence fallbacks.

## Guardrails specific to this week

Do not reuse the archive's conflicting maximum team sizes. Do not present facial-emotion inference as a reliable judgement of people. Camera use must be opt-in, with no retained student imagery.

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

Planning stage only: source paths, current-course boundaries and duplicate-PR inventory reviewed. No deck or runnable example is added, so no deck build, rendered-slide review, model/device test or full repository test pass is claimed. Before a later implementation is called ready, run the repository's applicable tests, build the affected outputs, inspect diagrams at presentation size, verify practical links and record exactly what remains untested.
