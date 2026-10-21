# SD5913 Week 11 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week11`, not a finished deck or an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Connecting creative tools**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 11 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This draft includes a Week 11 deck, site/nav registration and instructor run sheet for review. None is published; no assessment requirement is added.

The supplied Week 11 PDF, Python-powered apps, genuinely spans Orange, Blender, TouchDesigner, NDI, hand tracking/OSC and a networked game. The repository index and README describe different parts of that broad lecture. Preserve the map, but propose one focused creative-tool path for this year's class rather than recreating every installation.

## Supplied historical slide evidence

SD5913 - PFAD - Week 11.pdf (78 pages): pp. 4–17 object/storage recap; 18–30 Orange; 31–39 Blender; 40–44 TouchDesigner; 45–48 NDI; 49–55 hand tracking/OSC; 56–60 networked game; 61–78 tutorial. Text and screenshot contact sheets reviewed, including Orange pipeline/code, Blender camera/light/render, OSC and game examples.

Page numbers are 1-based PDF pages. These are historical materials supplied for review; the PDF itself is not copied into this public repository. Historical dates, marks and team arrangements are not adopted.

## Proposed learning outcome

Follow one value across two creative tools, explain its range and meaning, and show how the receiving work behaves when input pauses or disappears.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Begin with one Python-controlled creative result and identify its object, attributes and method calls using the accessible classes/objects bridge.
2. Map the archive's alternative tools briefly, then choose one route: change a Blender object property and render, or send a prepared numeric value to an OSC receiver.
3. Explain the chosen tool boundary with successive large diagrams and deterministic inputs before any optional camera or network.
4. Pairs change one value, predict the result and test missing/invalid input or a disconnected receiver.
5. Teams decide whether this integration serves their project's goal; preserve time for a usable increment rather than installing multiple ecosystems.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Creative-tool APIs, interoperable agent tools or inspectable generated workflows. Ask what crosses the boundary, what can fail and how a designer stays in control.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Retain a visible map of Scrum, Git teamwork, Docker and networks before changing their sequence. Include an agent → MCP server → tool explanation and a bounded permission-aware practical at the appropriate point; a model suggestion alone must not be treated as permission to act. This does not require AI inside every team project.

## Materials to develop in this PR

- [x] Reconcile the supplied slide record with the current 2026 sequence and identify what is retained, replaced or moved.
- [ ] Agree the learning outcome and teacher run sheet, with actual timing.
- [x] Author the deck with readable full-slide diagrams, short labels and supporting detail in notes. Follow AGENTS.md; primary diagram labels should target at least 40 design pixels at 1920 × 1080.
- [x] Include a worked example, a purposeful student prediction/inspection activity and a failure or limitation worth discussing.
- [ ] Align the PFAD/2026 practical with runnable examples if a receiver is chosen. Its current [companion draft PR #14](https://github.com/sd5913/pfad/pull/14) is a planning README only; the slide baseline uses printed Python instead.
- [ ] Select and verify the week's news using the criteria above.
- [x] Review the lesson for coherent progression, accuracy, appropriate depth and time for questions; revise in this same PR.
- [x] Build and visually inspect the draft deck; live receiver and classroom preflight still pending before calling it classroom-ready.

## Gaps and decisions

- Choose one core tool route and verify it is available to the class. Keep other archive tools as optional references.
- Confirm whether a short team-progress check belongs here; do not turn the archive's five-minute update into a new assessed presentation.
- Rehearse the selected route, including Stop, missing receiver and permission failure, without making asyncio or an advanced multiplayer stack a prerequisite.

## Guardrails specific to this week

Do not claim stable hand identity or low latency without measuring the chosen implementation. Keep synthetic/loopback input as the baseline; real-camera and external-device transmission need the appropriate consent and setup.

Across every week, preserve the existing assessment weights and confirmed dates. Individual Assignment 3 is separate from the group project. Do not add team-size rules, compulsory AI/audio, new grading criteria, submission formats or deadlines. Never commit student records, private submissions, quiz questions/keys or credentials. Do not merge, publish to Canvas, deploy the course, or change automation as part of this plan.

## Source record

Current-course anchors inspected for this plan:

- [Teaching README](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/README.md): source layout, builds, numbering/date caution and privacy rules.
- [Current Week 1 deck](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/deck/week01.py): assessment structure, Week 8 scope agreement and Week 13 final quiz.
- [Week 6 instructor plan](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/lessons/week06-lesson-plan.md): established depth, progression, fallbacks and verification conventions.
- [Week 7 draft PR](https://github.com/sd5913/teaching/pull/10), reviewed at `31c675b4085f771da6340878f3a54d7018f1015d`: team ideation and separate individual/group assessment framing.
- [Current student index](https://github.com/sd5913/pfad/blob/2026/README.md): this year's material, not the archive syllabus.

Historical candidates, inspected as source inventory only; not claimed to run on current dependencies:

- [2025 week11/README.md](https://github.com/sd5913/pfad/blob/2025/week11/README.md)
- [2025 week11/ARCHITECTURE.md](https://github.com/sd5913/pfad/blob/2025/week11/ARCHITECTURE.md)
- [2025 week11/osc_demo.py](https://github.com/sd5913/pfad/blob/2025/week11/osc_demo.py)
- [2025 week11/ndi_hand_tracking.py](https://github.com/sd5913/pfad/blob/2025/week11/ndi_hand_tracking.py)
- [2025 week11/orange/qdrant_to_orange.py](https://github.com/sd5913/pfad/blob/2025/week11/orange/qdrant_to_orange.py)
- [2025 errata](https://github.com/sd5913/pfad/blob/2025/ERRATA.md): known code, slide and assessment inconsistencies.

## Verification record

Teaching draft stage: supplied PDF text and archive provenance, current course boundaries, and companion PR reviewed. The Week 11 deck has a 29-slide targeted build and rendered-preview inspection; see lessons/week11-lesson-plan.md for pacing and source decisions. The printed Python example is synthetic and works without a receiver; no actual OSC receiver, Blender render, MCP tool, camera or external device has been tested. Teaching date and live tool choice remain unconfirmed; this is not published or claimed classroom-ready for the optional live route.
