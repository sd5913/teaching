"""Week 11: one synthetic control across a local creative-tool boundary.

This deck does not imply a working OSC receiver ships with the companion PR.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import week11_figures as F
from deckgen import attach_reports
from deckgen.layouts import (title, agenda, section, statement, content, two_col,
                             code_panel, figure_slide, question, end)

S = []
E = 'SD5913 · WEEK 11'


def diagram(eye, heading, figure, notes):
    return figure_slide(eye, heading, figure, notes=notes)


S.append(title(E, 'Connecting creative tools', 'One value. Two programs. A safe stop.',
    notes='Content week 11; calendar teaching date and lesson length are not confirmed. '
    'Use the synthetic printed trace as the baseline. A prepared local OSC receiver is an optional '
    'teacher demonstration only after rehearsal; no camera, paid app, login or AI is required. '
    'Companion draft: https://github.com/sd5913/pfad/pull/14 (offline Canvas mapping; no OSC receiver).'))
S.append(agenda(E, ['An object: value and action', 'One value crosses a local boundary',
                    'Map it, inspect it, stop it', 'Optional tools and project application'],
    notes='No dated AI news item has been verified for this lesson; skip the optional news slot. '
    'Do not displace the core exercise with a product-news summary. '
    'See lessons/week11-lesson-plan.md for pacing and fallback.'))
S.append(statement('What changes when a value leaves your program?',
    eyebrow_text='OPENING QUESTION', notes='Invite students to point at two programs they already know. '
    'Ask who controls the receiving property and what should happen if the sender exits. '
    'This is a discussion, not an assessed question.'))
S.append(content('LEARNING GOAL', 'Trace a value; design the stop', [
    'Name the sender, receiver and value.',
    'Explain the value\'s range, meaning and mapping.',
    'Predict the visible result and test a missing update.',
    'Show a safe reset or deliberate hold.',
], notes='Evidence for the classroom activity is one labelled input/output sketch, one mapping '
    'and one absence-of-updates decision. No extra assessed submission is introduced.'))
S.append(section('01 · START HERE', 'An object is a thing we can change',
                 'A name, an attribute and an action',
                 notes='Connect to familiar Python data structures and Week 4 interface state. '
                 'An object is not necessarily a database row.'))
for step, heading, note in [
    (0, 'Find the object', 'A named cube is an example, not an actual Blender scene. Objects hold state.'),
    (1, 'Read one attribute', 'scale is a numeric property of the illustrative cube; name identifies it.'),
    (2, 'Call a method to change it', 'A method call applies behaviour. Later Blender uses assignment to change an actual property; '
     'set_scale here is illustrative, not a Blender API name.')]:
    S.append(diagram('01 · OBJECTS', heading, F.object_step(step), note))
S.append(two_col('01 · PYTHON MODEL', 'Make the idea concrete', [
    'An object keeps related values together.',
    'An attribute answers: what is its state?',
    'A method answers: what can it do?',
], ['class Shape:', '    def __init__(self):', '        self.scale = 1.0', '', '    def set_scale(self, value):', '        self.scale = value', '', 'cube = Shape()', 'cube.set_scale(2.0)', 'print(cube.scale)  # 2.0'],
    notes='Runnable standard Python, no creative app required. Inspect where the instance attribute '
    'is set. This is a teaching model, not the Blender bpy API. Ask students to predict print output.'))
S.append(section('02 · BOUNDARY', 'One value, two programs',
                 'Follow it before adding devices or networks',
                 notes='Archive surveyed Orange, Blender, TouchDesigner, NDI/OSC and a multiplayer game. '
                 'This lesson narrows the route to one synthetic numeric control.'))
for step, heading, note in [
    (0, 'Begin with a sender', 'Python produces a fixed numeric value. First print it; no network traffic.'),
    (1, 'Give the value a message', 'OSC is one possible way to send addressed numeric messages. '
     'This diagram is conceptual, not proof of a live receiver. Address /control and value 0.50 are teaching choices.'),
    (2, 'The receiver chooses the effect', 'A receiving creative tool must explicitly listen, parse the '
     'message and map the value. Sending alone does not update any artwork.')]:
    S.append(diagram('02 · TRACE', heading, F.path(step), note))
S.append(code_panel('02 · OFFLINE TRACE', 'Run the smallest honest version', [
    'value = 0.50', 'address = "/control"', '',
    'print(f"send {address} {value:.2f}")',
    'print(f"receive {address} {value:.2f}")',
    'print(f"opacity {value * 100:.0f}%")',
], caption='Printed simulation: these lines do not send OSC or change a visual tool.',
    notes='Run with plain Python in a scratch file or read together. Exact output: '
    'send /control 0.50; receive /control 0.50; opacity 50%. '
    'The second line represents a hypothetical receiver; make the simulation label audible. '
    'The PFAD companion now supplies an offline Canvas mapping exercise, not a runnable OSC receiver.'))
S.append(diagram('02 · MEANING', 'A number needs a mapping', F.mapping(),
    '0.0 means fully transparent and 1.0 fully opaque in this chosen design. '
    'The receiver clamps values to [0,1] before scaling, or rejects invalid values. '
    'The actual receiving property name depends on the chosen app; no particular app is promised.'))
S.append(question('multiple_choice', 'At 0.75, what does the artwork show?',
    choices=['75% opacity', '0.75% opacity', '75 separate objects', 'No visible change'],
    eyebrow_text='PREDICT · 0 TO 1 BECOMES 0 TO 100',
    notes='Answer A if the receiver implements the shown mapping. This is formative, not graded. '
    'Ask what happens if no receiver is attached: no visible change despite a valid printed value.'))
S.append(code_panel('02 · RECEIVER LOGIC', 'Validate before you use it', [
    'from math import isfinite',
    'def opacity(value):',
    '    if type(value) not in (int, float):',
    '        return 0  # reject strings and bools',
    '    if not isfinite(value):',
    '        return 0  # reject NaN and infinity',
    '    return round(max(0, min(1, value)) * 100)',
    '', 'for value in (0, 0.5, 1, 3, "oops"):',
    '    print(value, opacity(value))',
], caption='Predict: 0, 50, 100, 100, 0. Which two inputs needed a policy?',
    notes='Python bool is technically an int, so exact type checking rejects it here. '
    'isfinite rejects NaN and infinity before clamping. This is numeric validation, not OSC decoding. '
    'The value 3 is clamped and the string falls back to 0. A receiver should log invalid input.'))
S.append(section('03 · TEST THE EDGE', 'Stop is part of the design',
                 'A silent sender is not the same as a zero value',
                 notes='If connection is optional, its failure path must work without the device.'))
S.append(diagram('03 · MISSING UPDATES', 'What happens when sending stops?', F.silence(),
    'A receiving tool may hold the last value forever unless someone implements a timeout. '
    'For this hypothetical opacity control, reset to 0 after a chosen timeout; another artwork '
    'might deliberately hold the last frame. Decide this explicitly. The diagram is illustrative, '
    'not measured network behaviour.'))
S.append(content('03 · THREE TESTS', 'Inspect the boundary, not just the happy path', [
    '0.50 arrives: opacity becomes 50%.',
    '"oops" arrives: reject or use the safe fallback.',
    'No update arrives: after a timeout, reset or clearly hold.',
], notes='Pairs predict each result before showing the mapping code. If a prepared OSC receiver exists, '
    'disconnect it and verify the actual behaviour rather than assuming a timeout exists. '
    'Printed trace is the default path, so no ports need to be opened.'))
S.append(content('03 · PAIR LAB', 'Draw, predict, check, stop', [
    'Draw: sender  →  address + value  →  receiver  →  visible change.',
    'Choose 0.25 or 0.75. Predict the output before running the trace.',
    'Change one mapping or range. Compare the new result.',
    'Cross out a message. Sketch the safe result when updates stop.',
], notes='Use the companion planning activity at https://github.com/sd5913/pfad/pull/14. '
    'The companion supplies an offline Canvas mapping; the printed Python snippets here '
    'are the available baseline. In a 12-minute pair activity, allow 3 minutes to draw and predict, '
    '5 to edit/run or calculate, 2 to simulate absence, 2 to share. No assessed submission.'))
S.append(section('04 · CHOOSE THE TOOL', 'One boundary is enough',
                 'Other routes are references, not an installation checklist',
                 notes='2025 archive pp. 18-30 Orange, 31-39 Blender, 40-44 TouchDesigner, '
                 '45-55 NDI/OSC, 56-60 game. This year uses one focused route.'))
S.append(two_col('04 · LOCAL ALTERNATIVE', 'Blender: change one property', [
    'On a prepared disposable scene only:',
    'Find a cube by name.',
    'Predict a scale change.',
    'Compare two renders if Blender is available.',
], ['import bpy', 'cube = bpy.data.objects.get("Cube")', 'if cube is not None:', '    cube.scale = (2, 2, 2)', '    print(cube.scale[:])'],
    notes='Optional demonstration, not a required installation or promised runnable PFAD file. '
    'Only run inside Blender Python with a known disposable Cube scene; bpy is not standard Python. '
    'Setting scale changes the object in memory. A render additionally needs a prepared camera, '
    'light, render settings and an explicit render; this excerpt itself does NOT render. '
    'Avoid the archival dataset script that clears a scene before importing assets.'))
S.append(two_col('04 · TRANSPORT CHOICES', 'Do not confuse the boundaries', [
    'Local Python object: one process; change an attribute.',
    'Local HTTP API: request and response; check status and data.',
    'OSC: addressed messages; a receiver must listen.',
], [
    'Orange: inspect data in a visual workflow.',
    'TouchDesigner: map channels to visual properties.',
    'NDI: transports audio/video, not just one value.',
    'Multiplayer: state and timing across clients.',
], right_font='body', right_size=30, lang=None,
    notes='The archived examples are not prerequisites. An API is a contract, not automatically '
    'a network service; the Blender Python API is local. OSC often uses UDP: a send can succeed '
    'even if nobody listens, with no built-in receipt confirmation. HTTP commonly provides a '
    'response/status but cannot guarantee the creative result is correct. NDI/camera requires '
    'additional setup and appropriate consent. Do not claim low latency or stable hand identity.'))
S.append(diagram('04 · OPTIONAL AI TOOL', 'An agent can suggest a tool call', F.mcp(0),
    'Separate human intent and model suggestion. No agent is necessary for the core practical. '
    'A model may propose changing a property, but cannot infer authorization to edit a scene or '
    'send camera frames from the user asking a question.'))
S.append(diagram('04 · OPTIONAL AI TOOL', 'MCP exposes a bounded capability', F.mcp(1),
    'Conceptual agent to MCP server to tool chain. The server advertises a tool, and the client '
    'invokes it within allowed scopes. Start with a read-only inspection of an explicitly selected '
    'disposable scene. Ask for approval before a write; confirm target/path and show resulting diff. '
    'Never grant broad file-system/network access merely because a model asks. MCP is not OSC '
    'and does not by itself make a camera or creative app safe.'))
S.append(content('04 · OPTIONAL EXTENSIONS', 'Only if the boundary is prepared', [
    'OSC receiver: local/loopback first; check address, port and Stop.',
    'Camera or NDI: opt in, check consent, never stream by default.',
    'Agent tool: read-only first; approve a bounded write separately.',
], notes='If time or software is unavailable, use the paper/printed trace without penalty. '
    'A localhost service is accessible on the same machine; sharing with another machine entails '
    'network configuration and an additional security review. No unknown port-opening recipe.'))
S.append(content('PROJECT APPLICATION', 'Does this connection serve your idea?', [
    'What does the viewer do or notice when the value changes?',
    'Which tool owns the value and which owns the visible result?',
    'Can someone test an increment without this integration?',
    'What remains usable if the sender is absent?',
], notes='Short informal team check-in if appropriate: what works, what is blocked, and what can '
    'another person test? Do not convert the historical five-minute tutorial update into an '
    'assessed presentation or a new project requirement. Give teams independent build time.'))
S.append(end('One value. Two programs. A safe stop.',
             'Trace it, map it, test silence.',
             '[Course tutorials](https://github.com/sd5913/pfad/tree/2026)',
             notes='End with one pair sharing its sketch, predicted number and missing-update '
             'policy. The PFAD Week 11 companion now includes an offline Canvas mapping; '
             'it is not a live OSC integration. Do not announce a class date or new assessment.'))

attach_reports(S, Path(__file__).resolve().parent / 'week11-reports.json')
DECK = {'title': 'SD5913 · Week 11 — Connecting creative tools',
        'pdf': 'SD5913-week11.pdf', 'slides': S}
