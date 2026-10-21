# SD5913 Week 10 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week10`; the draft deck and instructor run sheet now live alongside it in the same teaching PR. Nothing is published or announced to students by editing this PR.

## Status and source limits

- Teaching date: Thursday 12 November 2026 (confirmed by gio). Content week numbers are not calendar-week numbers after the 1 October holiday; this is not an assignment deadline.
- Candidate focus: **Classes objects and stored data**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 10 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- The draft now registers `deck/week10.py` in `deckgen.toml` and adds a Week 10 site card. Registration in source is not publication. It does not set assessment requirements; the class date is not an assignment deadline.

The supplied historical PDF is titled Data storage. It teaches object attributes and relationships before SQL/ORM and RAG, but assumes students can read class-based examples. The current instruction prioritises accessible classes and objects, so add an explicit concrete bridge before any database or agent framework.

## Supplied historical slide evidence

SD5913 - PFAD - Week 10.pdf (67 pages): pp. 13–24 object attributes and relationships with short prediction tasks; 25–31 IDs, schema, SQL and Peewee class examples; 32–38 database types and persistence; 39–43 authentication; 44–55 embeddings, retrieval and RAG; 56–67 tutorial and project work. Text extracted throughout; relationship diagrams 16–18 and code/screenshot pages 28–30, 33, 41–43 and 46–54 visually inspected.

Page numbers are 1-based PDF pages. These are historical materials supplied for review; the PDF itself is not copied into this public repository. Historical dates, marks and team arrangements are not adopted.

## Proposed learning outcome

Create two objects from one simple class, explain their separate attributes and one method, then relate those objects to records that can be saved and retrieved.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Start with one familiar project object such as a player, scene or message. Compare a class definition with two instances and predict which values belong to each instance.
2. Use a small constructor, attributes and one method; change one object and check that the other is unaffected. Keep inheritance and framework machinery optional.
3. Draw one-to-many and many-to-many relations using the archive's short prediction format, then introduce stable IDs only when needed.
4. Save and reload a tiny invented dataset using the simplest selected local route. Explain that in-memory objects and persisted records have different lifetimes.
5. Offer retrieval/RAG as a teacher demonstration only if the object/storage ideas are secure: inspect retrieved evidence before a response. Teams identify the minimum data their project needs.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Agent memory, grounded search or retrieval evaluation. Discussion should test provenance, stale context and unsupported answers rather than repeat benchmark claims.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Retain a visible map of Scrum, Git teamwork, Docker and networks before changing their sequence. Include an agent → MCP server → tool explanation and a bounded permission-aware practical at the appropriate point; a model suggestion alone must not be treated as permission to act. This does not require AI inside every team project.

## Materials to develop in this PR

- [x] Reconcile the supplied slide record with the current 2026 sequence; see `lessons/week10-lesson-plan.md` for page-by-page mapping.
- [ ] Confirm class duration before adding a timed run sheet; class date is Thursday 12 November 2026.
- [x] Author a draft deck with full-slide diagrams, notes, code traces and a 28-slide teaching route.
- [x] Include a runnable conceptual two-object example, student prediction, JSON save/restart demo and missing-file/broken-ID limitation.
- [x] Align executable examples with [PFAD/2026 companion PR #13](https://github.com/sd5913/pfad/pull/13). It now has tested stdlib fictional JSON save/reload code; the draft deck also supplies standalone snippets. Preflight classroom run steps.
- [ ] Select and verify the week's news using the criteria above.
- [ ] Review the lesson for coherent progression, accuracy, appropriate depth and time for questions; revise in this same PR.
- [ ] Obtain instructor approval of timing and content before calling the deck classroom-ready; targeted build and preview checks are part of this draft's review.

## Gaps and decisions

- Confirm the time available for the explicit classes/objects bridge before deciding how much ORM or RAG to keep.
- Choose one small local persistence route and an invented dataset; do not require students to deploy a database.
- Decide whether authentication should be omitted or treated only as a security critique; the archived implementation must not become a working student template.

## Guardrails specific to this week

The visually inspected archive pp. 42–43 contain bare SHA-256 password hashing, also flagged by repository ERRATA. Do not copy it or collect credentials. Explain classes and instances independently of ORM inheritance. Keep optional retrieval grounded in teacher-owned material and distinguish matching text from a guaranteed correct answer.

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

The archive was read as 2025 evidence; `lessons/week10-lesson-plan.md` maps its PDF pages to this draft. The companion PFAD PR #13 now includes tested stdlib fictional JSON save/reload code. Week 10 diagrams and code previews are rendered in the local targeted build, not deployed. A full course build, physical classroom projection, instructor timing approval and optional live retrieval/model paths remain unverified.
