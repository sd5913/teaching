# SD5913 Week 10 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week10`, not a finished deck or an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Memory retrieval and useful data**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 10 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. Historical slides are being requested separately.
- This PR adds planning text only. It does not register a deck, change the course site, set assessment requirements or publish learning material.

The 2025 Week 10 folder contains embeddings, a Qdrant handbook app and a login example. These are candidate concepts for this year's project support, not approved production recipes.

## Proposed learning outcome

Distinguish application state, stored records and retrieved context. Inspect where an answer came from, and explain one case in which retrieval should return no useful evidence.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Start with a project question that needs remembered or retrieved information, rather than installing a database first.
2. Compare an exact lookup with a similarity search using a small teacher-owned corpus.
3. Inspect retrieved passages before any optional model response; show a deliberately irrelevant question.
4. Pairs change one input, predict which records should be returned, and explain a failure.
5. Teams choose a minimal storage/retrieval design or justify why their project needs neither.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Agent memory, grounded search or retrieval evaluation. Discussion should test provenance, stale context and unsupported answers rather than repeat benchmark claims.

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

- Supply Week 10 slides and confirm whether search, persistence or authentication is the intended emphasis.
- Select a small corpus with permission to use it and decide whether an entirely offline exercise is sufficient.
- Review current dependencies and any chosen service costs before producing runnable examples.

## Guardrails specific to this week

The archived login app hashes passwords with bare unsalted SHA-256; ERRATA explicitly says not to ship it. Do not copy it into the new tutorial or collect student passwords. Use invented records and teacher-owned text; no student submissions or personal data.

Across every week, preserve the existing assessment weights and confirmed dates. Individual Assignment 3 is separate from the group project. Do not add team-size rules, compulsory AI/audio, new grading criteria, submission formats or deadlines. Never commit student records, private submissions, quiz questions/keys or credentials. Do not merge, publish to Canvas, deploy the course, or change automation as part of this plan.

## Source record

Current-course anchors inspected for this plan:

- [Teaching README](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/README.md): source layout, builds, numbering/date caution and privacy rules.
- [Current Week 1 deck](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/deck/week01.py): assessment structure, Week 8 scope agreement and Week 13 final quiz.
- [Week 6 instructor plan](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/lessons/week06-lesson-plan.md): established depth, progression, fallbacks and verification conventions.
- [Week 7 draft PR](https://github.com/sd5913/teaching/pull/10), reviewed at `31c675b4085f771da6340878f3a54d7018f1015d`: team ideation and separate individual/group assessment framing.
- [Current student index](https://github.com/sd5913/pfad/blob/2026/README.md): this year's material, not the archive syllabus.

Historical candidates, inspected as source inventory only; not claimed to run on current dependencies:

- [2025 week10/word2vec_example.py](https://github.com/sd5913/pfad/blob/2025/week10/word2vec_example.py)
- [2025 week10/handbook_app/handbook_app.py](https://github.com/sd5913/pfad/blob/2025/week10/handbook_app/handbook_app.py)
- [2025 week10/handbook_app/qdrant_store.py](https://github.com/sd5913/pfad/blob/2025/week10/handbook_app/qdrant_store.py)
- [2025 week10/login_app/app.py](https://github.com/sd5913/pfad/blob/2025/week10/login_app/app.py)
- [2025 errata](https://github.com/sd5913/pfad/blob/2025/ERRATA.md): known code, slide and assessment inconsistencies.

## Verification record

Planning stage only: source paths, current-course boundaries and duplicate-PR inventory reviewed. No deck or runnable example is added, so no deck build, rendered-slide review, model/device test or full repository test pass is claimed. Before a later implementation is called ready, run the repository's applicable tests, build the affected outputs, inspect diagrams at presentation size, verify practical links and record exactly what remains untested.
