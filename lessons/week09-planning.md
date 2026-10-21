# SD5913 Week 9 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week09`, not a finished deck or an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Connected interactions and state**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 9 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. Historical slides are being requested separately.
- This PR adds planning text only. It does not register a deck, change the course site, set assessment requirements or publish learning material.

2026 Week 4 already introduces Streamlit, browser events and FastAPI; Week 6 adds browser speech. The 2025 Week 9 archive contains HTTP and WebSocket examples. This is a proposed continuation, not a confirmed 2026 topic.

## Proposed learning outcome

Trace a message from a user control through a service and back. Explain what state must survive between messages and what the interface should do when the connection fails.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Retrieve the Week 4 input → function → output model and ask what changes when another process owns the function.
2. Compare one HTTP exchange with an ongoing message connection using a large, stepwise diagram.
3. Use a loopback-only echo demonstration to inspect message content, state and ordering.
4. Interrupt the connection deliberately; let students predict and improve the visible error/retry behaviour.
5. Teams decide whether their prototype actually needs networking and sketch one contract or a local-only alternative.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Agent tool protocols, realtime APIs or collaboration tools. Require a concrete request/message trace and distinguish a product announcement from a verified classroom integration.

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

- Supply the Week 9 slides and confirm how much networking remains after the revised Week 4 and Week 6 lessons.
- Choose a supported, pinned contemporary API example only after testing it.
- Confirm classroom connectivity before proposing any cross-device exercise; keep a loopback alternative.

## Guardrails specific to this week

Archive README is historical evidence, not a validated current setup. Its previously advertised WebRTC files never existed. Do not copy its network/firewall exercise as a required step or infer that REST services cannot store state.

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

Planning stage only: source paths, current-course boundaries and duplicate-PR inventory reviewed. No deck or runnable example is added, so no deck build, rendered-slide review, model/device test or full repository test pass is claimed. Before a later implementation is called ready, run the repository's applicable tests, build the affected outputs, inspect diagrams at presentation size, verify practical links and record exactly what remains untested.
