"""Week 09: connected interactions and state. Class: Thursday 5 November 2026."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import week09_figures as F

from deckgen import attach_reports
from deckgen.layouts import (agenda, cards, code_panel, content, end, figure_slide,
                             question, section, statement, title, two_col)

EYE = 'SD5913 · WEEK 09 · THU 5 NOV 2026'
PRACTICAL = 'https://github.com/sd5913/pfad/blob/plan/week09-companion-activity/week09/README.md'
S = []

S.append(title(EYE, 'Connected interactions', 'Messages, memory and useful failure.',
    notes='Learning outcome: trace a control through a service and back; say what persists '
          'between messages and design a visible response when the service fails. '
          'Class date: Thursday 5 November 2026; duration remains unconfirmed. This is the current teaching draft, '
          'not an assessment brief. No live service, login, microphone or student data is needed.'))
S.append(agenda(EYE, [
    'Recall the Week 4 API request', 'Find an address, a port and a route',
    'Compare one request with a continuing connection', 'Predict two messages and a disconnect',
    'Place an agent, MCP server and tool', 'Decide a boundary for your prototype',
], notes='Run prediction before explanation in each block. Keep the local paper trace '
          'if no prepared server is available. The optional historical speech-service '
          'examples are not core asyncio content. No news item is selected without '
          'near-class primary-source verification.'))
S.append(statement('What should the screen say when the other program disappears?',
    eyebrow_text='OPENING QUESTION', size=88,
    notes='Ask for two short responses. Keep them visible and revisit after the disconnect '
          'trace. Do not start with command-line networking tools.'))

S.append(section('01', 'Where does a message go?', 'Recall the tide API before adding a new connection',
    notes='Begin with the Week 4 tide request. First locate the destination; then show the request and response as separate steps.'))
S.append(content('01 · WEEK 4 RECALL', 'One choice, one request', [
    'In Week 4, the browser asks a FastAPI service for September tide records.',
    '', 'The server reads saved data and returns JSON. The browser draws a chart.',
    '', '**Question:** which program begins the conversation?',
], notes='Source: current Week 4 deck and pfad/week04. The frontend makes an '
          'HTTP request; the backend responds. Week 4 already introduced APIs, so '
          'this is a recall, not a repeat of API installation.'))
S.append(figure_slide('01 · A DESTINATION', 'A host and a port find a service', F.address(),
    notes='Conceptual local example, not a public server. 127.0.0.1 is loopback: '
          'both client and server can be separate programs on the same laptop. '
          '8000 is an illustrative port, not a requirement of the Week 9 practical. '
          'Many connections can share a listening port. A URL additionally names a route. '
          'Do not ask students to open a firewall or expose a listener.'))
S.append(cards('01 · THREE QUESTIONS', 'When a request fails, ask where', [
    ('HOST', 'Which machine?', '127.0.0.1 stays on this laptop.'),
    ('PORT', 'Which service?', 'A listener must be present at that port.'),
    ('ROUTE', 'Which resource?', 'The service must know the requested path.'),
], notes='Separate network reachability from application routing. An unreachable '
          'service is different from a reachable server returning 404 for a wrong route. '
          'Hostnames may resolve to addresses; these are roles, not one-to-one machines.'))
S.append(question('multiple_choice', 'The service is running, but /tidess is unknown. What changed?',
    choices=['A · host', 'B · port', 'C · route', 'D · nothing'],
    eyebrow_text='01 · PREDICT',
    notes='C. A server can be reachable and still reject an unknown path, commonly '
          'with 404. A stopped service usually means connection failure instead. '
          'This prediction does not require ClassPoint to teach: hands or discussion work.'))
S.append(figure_slide('01 · REQUEST', 'The browser asks for records', F.request(),
    notes='First half of one Week 4 exchange. GET requests a resource. The query '
          'parameter month=9 chooses September. A request goes to the server; '
          'a route is interpreted by the application, not by the network layer.'))
S.append(figure_slide('01 · RESPONSE', 'The server sends JSON back', F.response(),
    notes='Second half with geometry held constant. A successful example uses 200 OK '
          'and JSON; this does not imply that every request succeeds. The browser '
          'still has to parse the response and draw something visible.'))
S.append(two_col('01 · ONE ROUND TRIP', 'A response can still mean failure', [
    'The server may be reachable but reject a missing or invalid value.',
    '', 'Read the status and body before you draw a chart.',
    '', 'A network failure may have no HTTP response at all.',
], [
    'GET /tides?month=9',
    '200 OK  +  JSON data',
    '',
    'GET /unknown',
    '404 Not Found',
    '',
    'service stopped',
    'connection failed',
], notes='Illustrative outcomes, not captured logs. Distinguish HTTP error status '
          'from inability to connect. An invalid month may produce a validation error; '
          'do not assert an exact status without running the current Week 4 service.'))

S.append(section('02', 'What survives?', 'The difference between stored data and connection state',
    notes='Contrast a self-contained request with the state of an open conversation. Stored data is not the same as an active connection.'))
S.append(cards('02 · TWO WAYS TO TALK', 'Choose the shape of the exchange', [
    ('HTTP', 'Ask, then reply', 'Each request carries what it needs. Good for fetching records.'),
    ('WEBSOCKET', 'Keep talking', 'A live connection can carry messages both ways.'),
], notes='HTTP can also use persistent transport connections; the contrast is '
          'request/response semantics versus an ongoing two-way WebSocket exchange, '
          'not a claim that HTTP always opens a fresh TCP connection. REST statelessness '
          'does not prohibit a server from storing tide records or other data.'))
S.append(figure_slide('02 · A CONTINUING CONVERSATION', 'Two messages, one connection', F.echo(),
    notes='This illustrates a localhost echo service. PFAD PR #12 has a tested stdlib '
          'loopback TCP starter, not WebSocket. The client sends first. After hello '
          'returns, send another distinct string without reconnecting and record order. '
          'A server can track active connections; persistence does not guarantee delivery '
          'after a disconnect. No asyncio is required to read this trace.'))
S.append(code_panel('02 · PAPER TRACE', 'Predict before you reveal the replies', [
    'connect to local echo service',
    'send("red")',
    'receive()     # ?',
    'send("blue")',
    'receive()     # ?',
], caption='Pseudocode: not a runnable Python client.', lang=None,
    notes='Invite students to write the two expected replies and mark the connection '
          'that remains open. Reveal red, then blue for an ordered echo example. '
          'A protocol must define where each message begins/ends; a WebSocket message '
          'is framed. A raw TCP byte stream is not automatically one send per read.'))
S.append(question('short_answer', 'If the server stops after red, what can you conclude about blue?',
    hint='What was sent? What was acknowledged? What is unknown?',
    eyebrow_text='02 · DISCONNECT',
    notes='Acknowledge several possible timings. A local send call returning does not '
          'prove the server processed blue. If blue has no reply, its final status is '
          'unknown without an application-level acknowledgement. Reconnecting does '
          'not automatically resume the old connection. Ask students for a visible '
          'screen message instead of silently showing the last data as current.'))
S.append(cards('02 · NAME THE STATE', 'What must the interface remember?', [
    ('LOCAL', 'User choice', 'The selected value and unsent input.'),
    ('CONNECTION', 'Status', 'Connecting, open, closed or failed.'),
    ('SERVER', 'Shared data', 'Only if the design actually needs it.'),
], notes='Use the concrete two-message trace. The client should not present a stale '
          'reply as new. A server can keep records even for REST APIs; what matters '
          'is what each interaction assumes about previous messages.'))
S.append(statement('Do not turn a missing reply into a fake success.',
    eyebrow_text='02 · THE DESIGN RULE', size=88,
    notes='Use this to bridge the transport trace into UI feedback.'))
S.append(two_col('02 · FAILURE AS AN INTERACTION', 'Make waiting and failure legible', [
    'Show that a reply is pending.', '', 'Set a time limit, then show a useful error.',
    '', 'Offer a manual retry or a local-only alternative.',
], [
    'idle',
    '  -> waiting',
    '  -> reply OR error',
    '',
    'error',
    '  -> retry (once)',
    '  -> waiting',
], lang=None,
    notes='UI state sketch, not code or a mandatory retry policy. Avoid unbounded '
          'automatic retries, especially for actions that can have side effects. '
          'For a mutating action, retry only after deciding how duplicate requests '
          'will be handled. On paper, draw the error state and retry control.'))
S.append(content('02 · THE LOCAL ACTIVITY', 'Send, compare, disconnect', [
    'Draw **client -> server -> client** and label host, port and protocol.',
    '', 'Predict the replies to red and blue. Keep both on one connection.',
    '', 'Now stop the server: write the error the person should see.',
    '', f'[Current PFAD Week 9 echo practical]({PRACTICAL})',
], body_size=32, notes='PFAD PR #12 has a tested stdlib loopback TCP echo starter, not WebSocket. '
          'Do the paper trace by default; run the local TCP echo only after a '
          'classroom-machine preflight. Have pairs compare traces; '
          'collect one disconnect observation verbally. No assessed submission, '
          'external device, firewall change, microphone, account or personal data.'))

S.append(section('03', 'A tool is another boundary', 'An agent suggestion is not permission to act',
    notes='Shift from network message boundaries to authority boundaries. Keep the example local and invented.'))
S.append(figure_slide('03 · THREE ROLES', 'Agent, MCP server, tool', F.tool_boundary(),
    notes='Conceptual extension to the earlier client/service boundary. The agent '
          'can propose a tool call; an MCP server describes and brokers tools; '
          'the tool performs a bounded operation when permission/policy allows. '
          'A proposed call is not itself authorization or evidence of success. '
          'No live agent, integration or credential is required for this diagram.'))
S.append(question('multiple_choice', 'The agent suggests reading your local sketch folder. What happens first?',
    choices=['A · read everything', 'B · check permission and scope',
             'C · upload it', 'D · declare success'],
    eyebrow_text='03 · PERMISSION CHECK',
    notes='B. Ask what scope was approved and whether private files could be included. '
          'The bounded practical is a role-play: one student is the agent proposing '
          'list filenames in a made-up sketch folder, one is the server offering '
          'the operation, one is the human allowing only a harmless named folder. '
          'On denial, do not run the call; on approval, report only synthetic '
          'filenames. No actual file access or model account is necessary.'))
S.append(content('03 · A BOUNDED TOOL TRACE', 'Propose, check, act, report', [
    '**Propose:** “List names in the example sketches folder.”',
    '', '**Check:** “Only this invented folder? No file contents?”',
    '', '**Act:** run the allowed tool, or do nothing if denied.',
    '', '**Report:** distinguish a returned result from a suggested action.',
], body_size=33,
    notes='Use invented names, such as circle.svg and lines.svg, on paper. '
          'Permission covers a specific action and scope, not unrestricted future calls. '
          'Connect to the echo example: a message/request must be interpreted '
          'before any external effect is performed.'))

S.append(section('04', 'Choose the smallest boundary', 'Use a service only when the experience needs one',
    notes='Return to team prototypes. A local-only interaction is as valid as a service when it meets the design need.'))
S.append(cards('04 · PROJECT DESIGN', 'Three plausible architectures', [
    ('LOCAL', 'No network', 'One computer owns controls and data.'),
    ('HTTP', 'Request data', 'Fetch when a person asks for new records.'),
    ('LIVE', 'Push updates', 'Share changing events as they happen.'),
], notes='Scrum: name one small interaction to test. Git: agree who edits what '
          'and review a change. Docker can package a service later but does not '
          'make a network boundary necessary or solve permissions. A group project '
          'does not have to include AI, sound, Docker or live networking.'))
S.append(content('04 · TEAM CONVERSATION', 'Make the choice visible', [
    'Sketch **control -> state -> visible response** for one prototype interaction.',
    '', 'Decide: local-only, an HTTP request, or a continuing connection?',
    '', 'Name one failure and the feedback a person should see.',
    '', 'If there is a service: who starts it and what data can cross the boundary?',
], body_size=33,
    notes='Give teams time to draw and exchange with another team. Ask for a reason '
          'for the boundary, not a technology checklist. For a local-only design, '
          'describe a missing-file or invalid-input failure instead. This is '
          'design practice, not a new submission format or assessment rule.'))
S.append(question('short_answer', 'What is the smallest boundary your idea actually needs?',
    hint='Name the state, one message (or none), and one failure.',
    eyebrow_text='04 · EXIT TICKET',
    notes='Ask for one sentence per team, or collect on paper if ClassPoint '
          'is unavailable. A local-only answer is valid. Do not store names '
          'or treat this as graded evidence.'))
S.append(end('Trace the message. Design the silence.',
    'Keep the state that matters; make failure visible.',
    'sd5913.github.io/teaching',
    notes='Recap: address and port find a service, route finds a resource, '
          'a response may fail, a continuing connection has state, and '
          'a proposed tool call needs permission. The historical 2025 Week 9 '
          'PDF pp. 23-45 supplies topics, not 2026 schedules or policies; '
          'its pp. 46-58 speech/async demo remains optional context.'))

attach_reports(S, Path(__file__).resolve().parent / 'week09-reports.json')
DECK = {'title': 'SD5913 · Week 09 — Connected interactions',
        'pdf': 'SD5913-week09.pdf', 'slides': S}
