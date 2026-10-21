"""Week 12: review one project change, then trace and bound an MCP tool call.

The companion includes an optional tested local MCP stdio smoke test, not a promised classroom live demo:
https://github.com/sd5913/pfad/pull/15
Historical reference: 2025 Week 12 PDF pp. 21, 25-34, 48-53, 55-65.
No historical assessment dates or installation instructions are adopted.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from deckgen import attach_reports
from deckgen.layouts import (title, agenda, section, statement, content,
                             figure_slide, code_panel, question, two_col, end)
import week12_figures as F

EYE = 'SD5913 · WEEK 12 · THU 26 NOV 2026'
COMPANION = 'https://github.com/sd5913/pfad/pull/15/files'
S = []

S.append(title(EYE, 'Review, then act',
    'A project check and one bounded agent tool call.',
    notes='Class date: Thursday 26 November 2026. Frame this as two halves: improve a project through evidence, '
    'then distinguish an agent suggestion from an executed action. No AI feature is required '
    'in any group project. Prepared traces are the core route; do not install a server in class.'))

S.append(agenda(EYE, [
    'Review one small project change',
    'Agent host, MCP server and tool: different jobs',
    'Predict and inspect add(3, 4)',
    'Stop a call outside the allowed scope',
    'Apply one useful check to your own project',
], notes='Keep news optional and undated; no preselected 2026 item is verified for the '
    'eventual lesson date. If an item is used later, record primary source, event and '
    'publication dates, exact claim, relevance and whether behavior was tested. Drop news '
    'before shortening the trace or the project review.'))

S.append(section('01 · PROJECT REVIEW', 'Make one change easier to trust',
    'A small piece of working software beats a big promise.',
    notes='Do not present archive feedback as feedback about this year\'s submissions. '
    'Ask teams to choose a representative interaction in their own work.'))

S.append(content('01 · BEFORE A NEW FEATURE', 'Choose one interaction', [
    '- What does a person do?',
    '- What should the program return or show?',
    '- What happens with an empty or wrong input?',
    '- Can another person run it from the README?',
], notes='Use a fictional example such as a button asking for two numbers, not an '
    'individual student repository. This is a review lens, not a new assessment rubric. '
    'Keep Scrum, Git collaboration, Docker and networks visible as relevant paths: '
    'who owns the fix, which branch records it, what environment runs it, and which '
    'boundary it crosses. None needs a new setup lesson here.'))

S.append(two_col('01 · A SMALL TEST', 'A review you can explain', [
    'One repeated calculation becomes one function.',
    'One normal case and one error case are enough to start.',
    'Ask a person to try the interface without instructions.',
], [
    'def add(a, b):', '    return a + b', '',
    'assert add(3, 4) == 7', 'assert add(-2, 2) == 0',
], notes='The tiny function is deliberately ordinary: DRY is about a useful shared '
    'rule, not forcing abstraction. Two assertions do not prove the entire app works. '
    'Have students name an invalid-input behavior separately; do not claim Python\'s '
    'operator alone gives the user a helpful message. Archive pp. 25-29, 31-34 motivate '
    'reuse, debugging, testing, user testing and small steps.'))

S.append(question('short_answer', 'What is the next smallest useful check?',
    hint='Pick a real interaction: expected result + one failure + a person who tries it.',
    notes='Pair discussion, then hear two examples. This question is a formative '
    'prompt; do not require a ClassPoint login. One possible answer is checking an '
    'empty input before adding a feature. Do not share private project data.'))

S.append(section('02 · TOOL CALLS', 'Who actually runs the function?',
    'Separate the proposal, the transport and the action.',
    notes='Transition: direct code calling add() is enough for many products. An agent '
    'can propose a call, but that adds another decision and trust boundary.'))

S.append(figure_slide('02 · THREE ROLES', 'Not one magic box', F.roles(),
    notes='The model proposes a tool name and arguments. The host application contains '
    'an MCP client and decides whether to dispatch, subject to its permissions. The '
    'MCP server advertises tools and handles calls; add(a,b) is the implementation. '
    'MCP standardizes messages; it does not make a server trustworthy or confer '
    'permission. Companion: ' + COMPANION))

S.append(content('02 · BEFORE EXECUTION', 'Read the proposed call', [
    'Person: {mono:add 3 and 4}',
    'Proposed tool: {mono:add}',
    'Arguments: {mono:{"a": 3, "b": 4}}',
    'Predict the result. Has anything run yet?',
], notes='Answer: 7 is the predicted result, but at this point the call is only '
    'a proposal. Ask who checks the tool name, types and permissions before it '
    'crosses into the server. No model or server is required for this static trace.'))

S.append(figure_slide('02 · THE OUTBOUND CALL', 'Call after checking', F.outbound(),
    notes='For the prepared allowed trace, the host checks an allowlist containing '
    'only add and dispatches a valid call through its MCP client to the server. '
    'The server resolves add and validates its arguments before running it. '
    'The illustration is a teaching trace, not evidence that a live MCP client ran.'))

S.append(figure_slide('02 · THE RESULT', 'Inspect before answering', F.inbound(),
    notes='Result 7 travels from the pure tool through the server to the host. The '
    'assistant should say 7 only after seeing a successful result. A tool error, '
    'missing result or refusal is not a successful action. Keep the diagram '
    'geometry aligned with the outbound slide so the reversal is obvious.'))

S.append(code_panel('02 · THE PURE FUNCTION', 'Nothing outside the two inputs', [
    'def add(a: int, b: int) -> int:',
    '    return a + b',
    '',
    'assert add(3, 4) == 7',
], caption='The function is real Python; the MCP exchange is a prepared trace.',
    notes='The historical PDF p. 51 shows the tiny add(a,b) FastMCP example. '
    'We keep its no-side-effect function, but do not claim this excerpt starts '
    'an MCP server. A runnable MCP integration would need a pinned SDK, '
    'transport and lifecycle preflight; the companion PR includes an optional tested '
    'local MCP stdio smoke test, but classroom live use needs separate preflight. '
    'Python bools are ints, and this function alone does not reject '
    'them; for this exercise the advertised input contract is integer values.'))

S.append(question('multiple_choice', 'Is a proposed call proof that it ran?',
    choices=['Yes, the model named a tool', 'No, inspect the result or refusal',
             'Yes, MCP is a permission system'],
    hint='Which evidence would you ask to see?',
    notes='Correct: inspect the actual result or refusal. Do not score this '
    'as an assessment. Invite an explanation: a model can describe actions '
    'that never happened; the host must mediate execution.'))

S.append(section('03 · TRUST BOUNDARY', 'Permission is a separate decision',
    'A schema tells us how to call. It does not say we should.',
    notes='Show allowed and blocked diagrams consecutively. Keep the same '
    'layout so the only change is the gate outcome. The host policy is illustrative '
    'and must exist in a real application; MCP alone does not enforce it.'))

S.append(figure_slide('03 · ALLOWED', 'Allow only add', F.permission(True),
    notes='The fictional host permits add(3,4) only: known name, two integer '
    'arguments, no side effects. It then inspects the actual result 7. '
    'An allowlist should live in host policy, not in model prose. The '
    'vertical line marks the boundary from host decision to server execution.'))

S.append(figure_slide('03 · BLOCKED', 'Do not send an overwrite request',
    F.permission(False),
    notes='The same fictional host blocks a proposal to overwrite a file. '
    'The server exposes only add; no file-write tool is provided. If future '
    'tools with side effects are added, require explicit human review of '
    'target and content before paid generation, external sending or overwrite. '
    'No file, account or network action is executed in this exercise.'))

S.append(two_col('03 · PAUSE OR REFUSE', 'Which check stopped it?', [
    'Missing argument: schema / input validation.',
    'Tool returned an error: report failure, not success.',
    'Overwrite request: host policy blocks dispatch.',
], [
    'add(a=3)     # missing b',
    'add(a="3", b=4)  # wrong type',
    'overwrite("work.txt")',
    '',
    '# Is None a successful result?',
], notes='The last line asks students to challenge a missing result: None is '
    'NOT a successful addition result. Do not execute these pseudo-calls; they show '
    'unvalidated proposals, not legal Python calls to the pure function. '
    'Missing/wrong types may be rejected by the client/server schema, '
    'depending on runtime; the host still owns the allow/deny decision.'))

S.append(question('short_answer', 'Where must this trace stop?',
    hint='Choose one: missing b, failed tool result, or a request to overwrite a file.',
    notes='Pairs label the person, proposal, host check, server, tool, result '
    'and final response, then circle a stopping point. Compare with the '
    'companion PR trace. Expected: missing b -> fix input before execution; '
    'tool failure -> disclose error; overwrite -> no dispatch, ask a person. '
    'Working evidence: one labelled call/result trace and one failure case; '
    'this is practice, not a new assessed deliverable.'))

S.append(content('04 · BACK TO YOUR PROJECT', 'Is an agent needed here?', [
    '- Direct button to a known function: often clearer.',
    '- Tool-using agent: only if choice among actions adds value.',
    '- Both need a test, an error path and a user response.',
    '- Who reviews the next change before your team ships it?',
], notes='Ask each team to name one next useful fix to its representative '
    'interaction. Connect task ownership (Scrum), reviewable Git change, '
    'repeatable environment (Docker only where already relevant), and '
    'network access decisions; do not turn this into a Docker or async tutorial. '
    'AI is optional in the group project.'))

S.append(content('WORKSHOP · USE THE PREPARED TRACE', 'Keep the boundary visible', [
    '[Open the proposed Week 12 PFAD activity](' + COMPANION + ')',
    'Label call -> result -> final answer; inspect one failure.',
    'No account, paid API, model download or live MCP server required.',
], notes='The companion PR now includes a paper/static trace, tested stdlib '
    'simulation and optional tested local MCP stdio smoke test. The static trace '
    'remains the classroom default; the /2026/week12 link is not a published '
    'dependency until the PR merges. Classroom live use remains optional and '
    'needs separate preflight.'))

S.append(end('What actually happened?',
    'Show the check, the result and the stopping point.',
    'sd5913.github.io/teaching',
    notes='End with one group-project check and one tool-call boundary. '
    'Archive pp. 55-65 introduced submodules and ComfyUI setup; these are '
    'optional historical context, not steps for this activity.'))

attach_reports(S, HERE / 'week12-reports.json')
DECK = {'title': 'SD5913 · Week 12 · Review, then act',
        'pdf': 'SD5913-week12.pdf', 'slides': S}
