# SD5913 Week 9 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week09`, not a finished deck or an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Connected interactions and state**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 9 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This PR adds planning text only. It does not register a deck, change the course site, set assessment requirements or publish learning material.

The supplied historical PDF confirms Networks and APIs as the Week 9 backbone, after a Scrum/Git/Docker recap. Current Week 4 already teaches basic APIs and Week 6 speech, so this plan deepens the connection and debugging model without repeating those introductions or requiring advanced asyncio.

## Supplied historical slide evidence

SD5913 - PFAD - Week 9.pdf (60 pages): pp. 3–9 historical project/rubric material; 11–21 Scrum/Git/Docker recap; 23–35 network layers, IP, transport and ports; 36–45 APIs and HTTP/WebSocket examples; 46–58 speech service, setup and async audio screenshots; 59 project foundations. Text extracted throughout; pages 10, 26, 29–30, 43–45, 47 and 53–58 visually inspected.

Page numbers are 1-based PDF pages. These are historical materials supplied for review; the PDF itself is not copied into this public repository. Historical dates, marks and team arrangements are not adopted.

## Proposed learning outcome

Trace a message from a user control through a service and back. Explain what state must survive between messages and what the interface should do when the connection fails.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Recall one Week 4 API request, then locate client, server, hostname/address and port on a clear diagram.
2. Explain just enough network layering to distinguish an unreachable service, a wrong route and an application error. Keep transport trade-offs tied to a design example rather than a protocol survey.
3. Inspect a small local request/response or instructor-prepared echo demo. Students predict the message and visible result; they do not need to write an asyncio event loop.
4. Pause the service deliberately and compare the resulting error with malformed input; design useful feedback and a bounded retry.
5. Teams decide whether networking is necessary for their prototype and document the smallest service boundary or a local-only alternative.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Agent tool protocols, realtime APIs or collaboration tools. Require a concrete request/message trace and distinguish a product announcement from a verified classroom integration.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Retain a visible map of Scrum, Git teamwork, Docker and networks before changing their sequence. Include an agent → MCP server → tool explanation and a bounded permission-aware practical at the appropriate point; a model suggestion alone must not be treated as permission to act. This does not require AI inside every team project.

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

- Agree the retained network depth after the revised Week 4 API introduction; no current-year resequencing is assumed.
- Choose a supplied wrapper or synchronous example so async/await and callback queues are not prerequisites.
- Confirm classroom connectivity before any opt-in paired-device task; keep the default loopback-only.

## Guardrails specific to this week

Review the archival technical shortcuts before reuse: UPDATE is not the intended standard HTTP update verb; a port is not restricted to one connection; TCP is not immune to all errors or fixed at three times the packets; REST statelessness does not prohibit stored application data. The old audio callbacks/queues are advanced and not a core exercise. Do not copy absent WebRTC files or historical rubric values.

Across every week, preserve the existing assessment weights and confirmed dates. Individual Assignment 3 is separate from the group project. Do not add team-size rules, compulsory AI/audio, new grading criteria, submission formats or deadlines. Never commit student records, private submissions, quiz questions/keys or credentials. Do not merge, publish to Canvas, deploy the course, or change automation as part of this plan.

## Source record

Current-course anchors inspected for this plan:

- [Teaching README](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/README.md): source layout, builds, numbering/date caution and privacy rules.
- [Current Week 1 deck](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/deck/week01.py): assessment structure, Week 8 scope agreement and Week 13 final quiz.
- [Week 6 instructor plan](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/lessons/week06-lesson-plan.md): established depth, progression, fallbacks and verification conventions.
- [Week 7 draft PR](https://github.com/sd5913/teaching/pull/10), reviewed at `31c675b4085f771da6340878f3a54d7018f1015d`: team ideation and separate individual/group assessment framing.
- [Current student index](https://github.com/sd5913/pfad/blob/2026/README.md): this year's material, not the archive syllabus.

Historical candidates, inspected as source inventory only; not claimed to run on current dependencies:

- [2025 week09/README.md](https://github.com/sd5913/pfad/blob/2025/week09/README.md)
- [2025 week09/fastapi_example.py](https://github.com/sd5913/pfad/blob/2025/week09/fastapi_example.py)
- [2025 week09/websocket_server_echo.py](https://github.com/sd5913/pfad/blob/2025/week09/websocket_server_echo.py)
- [2025 week09/websocket_client_example.py](https://github.com/sd5913/pfad/blob/2025/week09/websocket_client_example.py)
- [2025 errata](https://github.com/sd5913/pfad/blob/2025/ERRATA.md): known code, slide and assessment inconsistencies.

## Verification record

Planning stage only: supplied PDF text and selected screenshot/diagram pages, repository source paths, current-course boundaries and duplicate-PR inventory reviewed. No deck or runnable example is added, so no deck build, rendered-slide review, model/device test or full repository test pass is claimed. Before a later implementation is called ready, run the repository's applicable tests, build the affected outputs, inspect diagrams at presentation size, verify practical links and record exactly what remains untested.
