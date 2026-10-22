# SD5913 Week 9 lesson planning

Planning draft started 21 October 2026. This remains the review home for content `week09`, not an announcement to students. A 29-slide teaching draft now lives in `deck/week09.py`; class date is Thursday 5 November 2026, while duration and classroom live demo remain unconfirmed. Keep revisions in the same draft PR.

## Status and source limits

- Teaching date: Thursday 5 November 2026 (confirmed by gio). Content week numbers are not calendar-week numbers after the 1 October holiday; this is not an assignment deadline.
- Candidate focus: **Connected interactions and state**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 9 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This PR registers a draft deck and adds a preview-site card. A branch preview is not the live course; it does not set assessment requirements or authorize a merge.

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
3. Inspect a small local request/response and a two-message echo trace. Students predict the message and visible result; they do not need to write an asyncio event loop.
4. Stop the echo service after the first reply. Compare a failed existing connection with a refused new connection and a server's HTTP 404; design useful feedback and a manual retry.
5. Teams decide whether networking is necessary for their prototype and document the smallest service boundary or a local-only alternative.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Agent tool protocols, realtime APIs or collaboration tools. Require a concrete request/message trace and distinguish a product announcement from a verified classroom integration.

Refresh near the actual class rather than filling future weeks with today's news. For each selected item record: event date and publication date, primary-source URL, exact supported claim, classroom connection, one discussion prompt, and whether the behaviour was personally tested or only reported by the source. If there is no useful verified item, omit the slot. News must not silently become assessed content.

## Current teaching direction

Prioritise accessible classes and objects over advanced asyncio. Retain a visible map of Scrum, Git teamwork, Docker and networks before changing their sequence. Include an agent → MCP server → tool explanation and a bounded permission-aware practical at the appropriate point; a model suggestion alone must not be treated as permission to act. This does not require AI inside every team project.

## Instructor run sheet (sequence, not minutes)

- **Tutorial handoff to MJ (Jie Ma):** MJ leads the companion practical; use [PFAD Week 9](https://github.com/sd5913/pfad/pull/12) as the student-facing script. Start with the two-box prediction, run the loopback server in terminal A and ordinary client in B, then pause before blue, stop A, and ask students to identify the missing reply and draw waiting/error/manual-retry states. Restart A for a deliberate retry. If the terminals fail, use the same paper trace. Do not require students to build an async or WebSocket server, or treat this practice as a submission.
- **Before class:** check the Week 4 `/tides?month=9` example and load the deck PDF as an offline backup. If using the optional live echo, start `python3 week09/echo_server.py` from a clean PFAD Week 9 PR checkout in terminal A, then run the ordinary client in B; verify red, blue and green before anyone joins. Leave all devices on loopback. If the room or installation is uncertain, use the paper trace instead.
- **Slides 1–11, locate and diagnose:** collect one answer to the opening question before explaining. Draw browser, host, port and route; use `/tidess` to elicit a reachable-server 404, then compare a stopped server with no HTTP response. The Week 4 tide API is recall, not a new install task.
- **Slides 12–20, state and failure:** contrast HTTP request/response with an ongoing WebSocket conversation, then say explicitly that the runnable companion uses newline-framed TCP, not WebSocket. Predict red and blue on one connection; green arrives after reconnect in the companion. For the optional live failure, run `python3 week09/echo_client.py --pause-before-blue`; after `received: red`, stop A with Ctrl+C, then press Enter in B. The resulting `No reply` is not a successful blue reply. Ask for waiting/error/manual-retry UI states. In this controlled sequence blue was not sent before shutdown; that is not a general delivery guarantee for in-flight messages.
- **Slides 21–24, authority boundary:** on paper only, assign agent, MCP server, tool and human roles. Suggest listing names in an invented sketches folder; check the human's scope before any action, deny file contents, and report a result only if permission was granted. Do not open real folders, accounts or student data.
- **Slides 25–29, prototype choice:** teams sketch one local-only, HTTP or live interaction, plus a useful failure message. Invite a reason for the boundary, not a technology checklist; accept a local-only answer. End with the smallest-boundary exit ticket; this is not graded evidence or a new submission.
- **Fallback and close:** if sockets, Python, permissions or time prevent a live demo, run the same red/blue/green trace on paper and cross out the server before blue. Do not present a stopped-listener refusal as an HTTP 404 or claim that a sent message was processed without a reply. Leave questions and transition time flexible until the class duration is confirmed.

## Materials to develop in this PR

- [x] Reconcile the supplied slide record with the current 2026 sequence and identify what is retained, replaced or moved.
- [ ] Agree the learning outcome and teacher run sheet, with actual timing.
- [x] Author the deck with readable full-slide diagrams, short labels and supporting detail in notes. Follow AGENTS.md; primary diagram labels should target at least 40 design pixels at 1920 × 1080.
- [x] Include a worked example, a purposeful student prediction/inspection activity and a failure or limitation worth discussing.
- [x] Align the deck with [PFAD Week 9 companion PR #12](https://github.com/sd5913/pfad/pull/12) (originally at `b43632e`); it now includes tested stdlib loopback TCP echo code, not WebSocket. The deck retains a paper trace; classroom live use needs preflight.
- [ ] Select and verify the week's news using the criteria above.
- [ ] Review the lesson for coherent progression, accuracy, appropriate depth and time for questions; revise in this same PR.
- [x] Build and visually inspect the teaching draft. Classroom readiness still depends on date/duration confirmation and any live starter preflight.

## Gaps and decisions

- Agree the retained network depth after the revised Week 4 API introduction; no current-year resequencing is assumed.
- Choose a supplied wrapper or synchronous example so async/await and callback queues are not prerequisites.
- Confirm classroom connectivity before any opt-in paired-device task; keep the default loopback-only.

## Draft reconciliation, 21 October 2026

- Retained from the supplied Week 9 PDF: the practical distinction between address, port and service (pp. 23–35); APIs, HTTP and WebSockets as communication patterns (pp. 36–45). The Week 4 tide service supplies the current-year worked request/response instead of repeating an API introduction.
- Replaced: a speculative live server demonstration becomes an explicit paper echo trace and disconnect inspection even with the tested stdlib loopback TCP starter; classroom live use needs preflight. The 2025 paired-LAN setup and installation screenshots (pp. 47–52) are not instructions for 2026.
- Moved out of core: 2025 speech-service/audio-queue material (pp. 46, 53–58), protocol survey and advanced asyncio. The deck adds a permission-scoped agent → MCP server → tool explanation as a current teaching direction, not as archival evidence.
- Corrected archive shortcuts: use standard HTTP methods rather than `UPDATE`; one port may serve multiple connections; TCP does not make an application infallible; REST statelessness does not forbid stored server data. Do not import the historical project/rubric dates and rules (pp. 3–9).
- Suggested facilitation: opening prediction, address/route diagnosis, two-step tide diagram, message-order paper trace, disconnect feedback, bounded tool role-play, team boundary sketch and exit ticket. Allocate actual minutes only when class duration is confirmed. The optional AI news slot is empty pending near-class source verification.

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

The supplied PDF text and selected screenshot/diagram pages, repository source paths and current-course boundaries were reviewed. The Week 9 deck has been built with pinned deckgen v0.11.2 to HTML, PDF and plain/ClassPoint PPTX; its 29-slide preview sheets and full-size address, echo and MCP diagram previews were inspected. PFAD PR #12 now includes a tested stdlib loopback TCP echo starter, not WebSocket; classroom device and live use have not been preflighted here. Source tests and diff checks are tracked in the implementation review, not evidence of a classroom run.
