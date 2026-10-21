# SD5913 Week 13 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week13`; the slide deck is a draft for review, not an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Semester synthesis and final review**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 13 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This PR now contains a provisional 29-slide deck, a flexible instructor run sheet,
  deck registration and site navigation. They are draft sources, not a published
  class announcement or an assessment change. Review optional later-week slides
  against what was actually taught before presenting them.

The supplied Week 13 PDF is a recap and final-assessment class: its agenda says recap and a final at 10am, followed by AMA and a team/repository tutorial. That historical time is not a confirmed 2026 booking. Current Week 1 places the 10% final quiz in content Week 13; README expects that content week in December but withholds an exact date.

## Supplied historical slide evidence

SD5913 - PFAD - Week 13.pdf (28 pages): p. 2 historical recap/final agenda; 3–26 recap; p. 8 classes/objects, 13 sprint, 14 Docker, 15–17 networks/APIs, 25–26 MCP and the small addition tool; 27 AMA; 28 team/repository check and testing on another computer. Text and screenshot contact sheets reviewed. The unsafe password screenshot on p. 21 and inaccurate assignment wording on p. 5 must not be copied.

Page numbers are 1-based PDF pages. These are historical materials supplied for review; the PDF itself is not copied into this public repository. Historical dates, marks and team arrangements are not adopted.

## Proposed learning outcome

Explain a piece of the student's work through input, state, control flow, output and testing. Revisit the semester's evidence of progress without introducing new assessed concepts.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Select representative concepts from the actual taught 2026 slides, with source-week references and obsolete activity links removed.
2. Use one bounded semester-loop example to trace state and termination; preserve the conceptual connection to the opening class.
3. Invite unresolved questions and project reflection, without assuming a presentation format or inventing a submission.
4. Reserve the final assessment slot only once the instructor confirms its time and format; adapt review time around it.
5. Close with a practical account of what students can build, inspect and improve independently.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: A very short end-of-course comparison only if it helps synthesis. Do not add newly announced products or untaught news to assessed content.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Retain a visible map of Scrum, Git teamwork, Docker and networks before changing their sequence. Include an agent → MCP server → tool explanation and a bounded permission-aware practical at the appropriate point; a model suggestion alone must not be treated as permission to act. This does not require AI inside every team project.

## Materials to develop in this PR

- [x] Reconcile the supplied slide record with the current 2026 sequence and identify what is retained, replaced or moved; see `week13-lesson-plan.md`.
- [ ] Agree the learning outcome and teacher run sheet, with actual timing.
- [x] Author the draft deck with full-slide diagrams, short labels and supporting detail in notes. Follow AGENTS.md; primary diagram labels target at least 40 design pixels at 1920 × 1080.
- [x] Include a worked example, a purposeful student prediction/inspection activity and a failure or limitation worth discussing.
- [x] Align the draft with PFAD companion [PR #16](https://github.com/sd5913/pfad/pull/16), a documentation-only proposal with no runnable starter to promise.
- [ ] Select and verify the week's news using the criteria above.
- [x] Review the draft for progression, accuracy, depth and questions; keep the run sheet flexible pending confirmed duration.
- [x] Build and visually inspect the draft deck. Classroom readiness still depends on confirming taught later-week scope and assessment arrangements.

## Gaps and decisions

- Confirm the exact 2026 final-class and final-quiz date/time, duration, format and permitted tools; do not reuse the archive's 10am time.
- Confirm the current project hand-in/presentation arrangements and replace historical Blackboard instructions with the actual current route.
- Build the recap from what was actually taught in 2026, including approved later-week revisions, not the entire archive or today's candidate plans.

## Guardrails specific to this week

Do not recreate the already delivered midterm question bank, publish assessment questions/keys, or transfer the midterm's 40-question/30-minute format to the final quiz. The final quiz weight stays 10%; the group project stays 40%.

Across every week, preserve the existing assessment weights and confirmed dates. Individual Assignment 3 is separate from the group project. Do not add team-size rules, compulsory AI/audio, new grading criteria, submission formats or deadlines. Never commit student records, private submissions, quiz questions/keys or credentials. Do not merge, publish to Canvas, deploy the course, or change automation as part of this plan.

## Source record

Current-course anchors inspected for this plan:

- [Teaching README](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/README.md): source layout, builds, numbering/date caution and privacy rules.
- [Current Week 1 deck](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/deck/week01.py): assessment structure, Week 8 scope agreement and Week 13 final quiz.
- [Week 6 instructor plan](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/lessons/week06-lesson-plan.md): established depth, progression, fallbacks and verification conventions.
- [Week 7 draft PR](https://github.com/sd5913/teaching/pull/10), reviewed at `31c675b4085f771da6340878f3a54d7018f1015d`: team ideation and separate individual/group assessment framing.
- [Current student index](https://github.com/sd5913/pfad/blob/2026/README.md): this year's material, not the archive syllabus.

Historical candidates, inspected as source inventory only; not claimed to run on current dependencies:

- [2025 week13/semester.py](https://github.com/sd5913/pfad/blob/2025/week13/semester.py)
- [2025 errata](https://github.com/sd5913/pfad/blob/2025/ERRATA.md): known code, slide and assessment inconsistencies.

## Verification record

The 2025 PDF and archive provenance were reviewed as historical evidence only.
The 2026 Week 1–6 slides anchor the confirmed recap, while later-week prompts
are marked optional. A targeted Week 13 HTML/PDF/PPTX build and slide previews
were inspected locally; this does not publish anything. The companion PR is
documentation-only. No student project, second-device run, assessment format,
or later-week teaching scope has been verified. Rehearse the selected practical
and confirm the final-class arrangements before delivery. The focused Week 13
tests and `git diff --check` pass. The full repository suite has one unrelated
existing Week 6 student-module/source mismatch
(`test_week06_new_sketches.NewSketches.test_piano_harmonics_and_voice_surface_live_in_student_module_and_deck`);
it is not a Week 13 deck failure and is left unchanged.
