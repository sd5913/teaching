# SD5913 Week 12 lesson planning

Planning draft started 21 October 2026. This is the continuing review home for content `week12`, not a finished deck or an announcement to students. Keep this week's changes in the same draft PR.

## Status and source limits

- Teaching date: unconfirmed. Content week numbers must not be converted into calendar dates by simple addition after the 1 October holiday.
- Candidate focus: **Agents tools and project review**. The instructor's later slides and current course sequence take precedence.
- No 2026 Week 12 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The supplied historical PDFs are source evidence, not an approved 2026 timetable.
- This PR adds planning text only. It does not register a deck, change the course site, set assessment requirements or publish learning material.

The supplied Week 12 PDF combines project/code review, programming principles, optional generative-AI research and MCP. Its own small FastMCP addition example supplies a direct foundation for the requested safe agent → server → tool practical, without making ComfyUI infrastructure the starting point.

## Supplied historical slide evidence

SD5913 - PFAD - Week 12.pdf (65 pages): pp. 4–19 recap; 21 repository feedback; 24–34 programming principles (DRY, error handling, testing, user testing and small steps); 35–47 generative-AI research; 48–53 MCP, including the small add(a,b) server on p. 51, adapter on p. 52 and ComfyUI on p. 53; 54–65 tutorial. Text and screenshot contact sheets reviewed.

Page numbers are 1-based PDF pages. These are historical materials supplied for review; the PDF itself is not copied into this public repository. Historical dates, marks and team arrangements are not adopted.

## Proposed learning outcome

Distinguish a model's suggestion from an executed tool action. Trace a bounded tool call, inspect its result, and demonstrate a safe stopping or approval boundary.

## Proposed classroom sequence

This is a sequence for discussion, not a timed run sheet. Confirm the class duration and topic before allocating minutes. Preserve substantial explanation, a concrete example, a prediction or inspection activity and project application rather than turning the lesson into a list of tools.

1. Review one small project change through repeated code, an error case, a test and a user's response, drawing on archive pp. 24–34.
2. Draw the agent, MCP server and tool as separate parts. Follow one request with explicit arguments into the server and one result back.
3. Use the archive's tiny addition tool as the no-side-effect baseline. Inspect the tool schema, expected result and invalid input before adding any model choice.
4. Add a permission exercise with a clearly simulated or blocked side-effecting request: decide what is allowed, refuse what is outside scope, and inspect the log. Do not implement unrestricted file writes or network actions.
5. Teams test one representative interaction and identify their next useful fix. Keep ComfyUI, submodules, async orchestration and research-model surveys optional.

## Weekly AI news

Reserve an optional short opening discussion, trimmed before core teaching or assessment time. Suggested relevance filter: Agent tool use, MCP, evaluation or permission controls. Compare advertised autonomy with observable actions, logs, failure handling and human review.

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

- Confirm whether agent/tool fundamentals need a short earlier bridge; this plan does not silently move the current course sequence.
- Select and pin a minimal supported MCP runtime, then verify the addition tool and explicit allow/deny behaviour using current primary documentation.
- Confirm the project-review time and existing brief. No new submission, compulsory AI component or assessment criterion is introduced.

## Guardrails specific to this week

ERRATA records a dead-event-loop problem from asyncio.run at import and again inside Streamlit in the archive. Rebuild and test the lifecycle rather than copy it. No real credentials, paid actions, public posting or unrestricted filesystem tool should be needed.

Across every week, preserve the existing assessment weights and confirmed dates. Individual Assignment 3 is separate from the group project. Do not add team-size rules, compulsory AI/audio, new grading criteria, submission formats or deadlines. Never commit student records, private submissions, quiz questions/keys or credentials. Do not merge, publish to Canvas, deploy the course, or change automation as part of this plan.

## Source record

Current-course anchors inspected for this plan:

- [Teaching README](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/README.md): source layout, builds, numbering/date caution and privacy rules.
- [Current Week 1 deck](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/deck/week01.py): assessment structure, Week 8 scope agreement and Week 13 final quiz.
- [Week 6 instructor plan](https://github.com/sd5913/teaching/blob/29a92068d2029c1b8c86d9e75cc02f38da71ceac/lessons/week06-lesson-plan.md): established depth, progression, fallbacks and verification conventions.
- [Week 7 draft PR](https://github.com/sd5913/teaching/pull/10), reviewed at `31c675b4085f771da6340878f3a54d7018f1015d`: team ideation and separate individual/group assessment framing.
- [Current student index](https://github.com/sd5913/pfad/blob/2026/README.md): this year's material, not the archive syllabus.

Historical candidates, inspected as source inventory only; not claimed to run on current dependencies:

- [2025 week07/1_langgraph_chat.py](https://github.com/sd5913/pfad/blob/2025/week07/1_langgraph_chat.py)
- [2025 week07/2_tool_calling.py](https://github.com/sd5913/pfad/blob/2025/week07/2_tool_calling.py)
- [2025 week07/3_graph_agent.py](https://github.com/sd5913/pfad/blob/2025/week07/3_graph_agent.py)
- [2025 week12/app.py](https://github.com/sd5913/pfad/blob/2025/week12/app.py)
- [2025 week12/bot.py](https://github.com/sd5913/pfad/blob/2025/week12/bot.py)
- [2025 week12/tools.py](https://github.com/sd5913/pfad/blob/2025/week12/tools.py)
- [2025 errata](https://github.com/sd5913/pfad/blob/2025/ERRATA.md): known code, slide and assessment inconsistencies.

## Verification record

Planning stage only: supplied PDF text and selected screenshot/diagram pages, repository source paths, current-course boundaries and duplicate-PR inventory reviewed. No deck or runnable example is added, so no deck build, rendered-slide review, model/device test or full repository test pass is claimed. Before a later implementation is called ready, run the repository's applicable tests, build the affected outputs, inspect diagrams at presentation size, verify practical links and record exactly what remains untested.
