# SD5913 Week 12 lesson planning

Planning draft started 21 October 2026. The Week 12 teaching deck and provisional run sheet now live in this same draft PR; they are not an announcement to students or a change to assessment dates. Class date: Thursday 26 November 2026.

## Status and source limits

- Teaching date: Thursday 26 November 2026 (confirmed by gio). Content week numbers are not calendar-week numbers after the 1 October holiday; this is not an assignment deadline.
- Candidate focus: **Agents tools and project review**. The instructor's later slides and current course sequence take precedence.
- At the start of planning, no 2026 Week 12 deck or complete future timetable was present in the inspected teaching/main or PFAD/2026 trees. The new draft deck does not confirm a timetable; historical PDFs are source evidence only.
- The initial planning-only PR now also includes `deck/week12.py`, original diagrams, a lesson plan, deck registration and site navigation in its working draft. Do not merge or publish without instructor review.

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

- [x] Reconcile archive topics in `lessons/week12-lesson-plan.md`; retain project review and small add tool, move ComfyUI setup to optional history.
- [ ] Agree actual duration with the instructor (class date: Thursday 26 November 2026); a flexible run sheet and learning outcome are drafted in `lessons/week12-lesson-plan.md`.
- [x] Author a diagram-led deck with notes, readable primary labels, a worked example and a permission boundary.
- [x] Include prediction, inspection, a missing input, a failed result and an out-of-scope side effect.
- [x] Align to [PFAD companion PR #15](https://github.com/sd5913/pfad/pull/15): it now has a paper/static trace, tested stdlib simulation and optional tested local MCP stdio smoke test. Classroom live use remains optional and unpreflighted.
- [ ] Select and verify the week's news using the criteria above.
- [ ] Review the lesson for coherent progression, accuracy, appropriate depth and time for questions; revise in this same PR.
- [x] Build the targeted deck and inspect slide sheets, full-size diagrams and a PDF diagram. Instructor approval and classroom-device check remain open.

## Gaps and decisions

- Confirm whether agent/tool fundamentals need a short earlier bridge; this plan does not silently move the current course sequence.
- If a classroom live MCP demo is requested, preflight the optional local stdio smoke test on that machine and verify host-side allow/deny behaviour. The static exercise does not require a runtime.
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

The 2025 Week 12 PDF (65 pages, SHA-256 in the archive manifest) was checked for review topics and its p. 51 add-tool screenshot; the original archive binaries remain outside this repo. Companion PR #15 now has a paper/static trace, tested stdlib simulation and optional tested local MCP stdio smoke test. The 21-slide 2026 Week 12 deck builds with the pinned deckgen toolchain to HTML, PDF and PowerPoints; preview sheets, full-size diagrams and one rendered PDF diagram were inspected. Four focused source/trace tests pass and `git diff --check` is clean. Not checked here: classroom live MCP use, any model or classroom device, the full course build, instructor timing approval or news near class.
