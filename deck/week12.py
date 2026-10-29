"""Week 12: actual model feedback, bounded Python tools and a filmed tiny world.

120 minutes including 60-70 break; separate PFAD tutorial keeps its 55-65 break.
Core verified 29 October 2026 on Godot 4.7.2, real Xvfb/Mesa graphics.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from deckgen import attach_reports
from deckgen.layouts import (title, agenda, section, statement, content,
                             figure_slide, code_panel, question, end)
import week12_figures as F

EYE = 'SD5913 · WEEK 12 · THU 26 NOV 2026'
PIN = '4f2864a02ca32a200cbf7da34a02d33ec917e80f'
SOURCE = f'https://github.com/sd5913/pfad/tree/{PIN}/week12'
BLOB = f'https://github.com/sd5913/pfad/blob/{PIN}/week12'
DOCS = 'https://docs.godotengine.org/en/4.7/'
RELEASE = 'https://github.com/godotengine/godot-builds/releases/tag/4.7.2-stable'
S = []

S.append(title(EYE, 'Build. Check. Film.',
    'An agent changes a tiny world. What evidence makes it trustworthy?',
    notes='0-2 min. This complete 120-minute lecture has a break at 60-70. The separate tutorial has its break at 55-65 and tutor support at 100-120. State the four outcomes: explain goal/state/actions/observations/stop; trace Python through JSON and a real engine process; justify adaptation from failure; distinguish model decisions, human choices, recorded replay and deterministic film. The genuine current Codex episode precedes the later film of its unchanged final source. The project does not require AI or Godot. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('OPENING · RELEASE WATCH', 'A current tool still needs a check', [
    'Godot 4.7.2 · maintenance release · 18 August 2026',
    'Latest stable verified 29 October; refresh before class.',
    'Why designers care: an engine update can change a production workflow.',
    '[Official release and notes]('+RELEASE+')',
], notes='2-5 min. Dated news, outside quiz scope. The official latest-release endpoint returned 4.7.2 on 29 October, published 18 August 2026 at 15:56:46 UTC. Its release note describes maintenance fixes for stability and usability. We tested this engine and scene, not every fixed issue or student platform. Ask what a designer should rerun after an engine update. Before 26 November, refresh the release, publication date, claim and practical checks. Source: https://github.com/godotengine/godot-builds/releases/tag/4.7.2-stable . Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('OPENING · THE ACTUAL RESULT', 'Three lights. One exit.', F.screenshot('frame-end.png'),
    notes='5-7 min. This is a real later Movie Maker frame from the exact original final source selected by the model, speed 275. It is not a generated mockup. Three lights, the mint exit and COMPLETE are visible. A final still does not establish the process: it could be stale or staged. Ask what sequence and checks would strengthen the claim. Open evidence/model-selected-world.mp4 and evidence/provenance.json in the pinned companion to inspect continuous motion and source hashes. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(question('short_answer', 'What would convince you it works?',
    hint='Name one behavior check and one thing you must see.',
    notes='7-10 min. Give pairs 90 seconds, then hear two answers. Useful behavior evidence: collect all three lights and win within 180 physics ticks; reject the exit with too few lights. Useful visual evidence: actual movement, ordered collection and COMPLETE in the film. A model saying done, a process starting or a valid MP4 container alone is insufficient. This is formative discussion; no ClassPoint login or new submission is required. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(agenda(EYE, ['A goal, a world and a bounded tool contract',
    'Actual model decisions from failed and passing checks',
    'One simulation: behavior checks and visible playback',
    'Film, inspect and retain evidence',
    'The tutorial route and prepared-machine handoff'],
    notes='10-12 min. Explain the lecture budget: 10-30 concepts, 30-50 worked demo, 50-60 trace/checking, 60-70 break, 70-95 capture, 95-110 comparison/transfer and 110-120 tutorial/questions. Reuse W7 shared simulation, W8 small tested changes and CI, W9 process messages, W10 persistence/retrieval and W11 actual creative tools. Do not repeat basic class syntax or generic MCP permissions. The new computing idea is selecting a bounded next action from actual observations. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(section('GOAL AND STATE', 'A small world is enough',
    'Observe a failure. Change one value. Keep the goal fixed.',
    notes='12-13 min. A supplied tiny world makes the feedback loop inspectable. This is configuration-based construction of supplied behavior, not arbitrary code generation or a commercial-game pipeline. State the constraints before anyone acts. Keep the three light positions and acceptance rules fixed so a changed result has a meaningful comparison. The model and the learner both need a measurable stopping point. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('THE BRIEF', 'Make the goal testable', [
    'Start x80; collect lights at x240, x420 and x600.',
    'Reach the exit at x860 within 180 physics ticks.',
    'Keep light positions and acceptance checks fixed.',
    'Change only bounded config, then check and stop.',
], notes='13-15 min. Default physics is 60 ticks per second, so 180 ticks means three simulated seconds. The win threshold is within 20 units of the exit; pickup radius 24 means the route need not hit exact centers. Ask what a goal such as make it fun would fail to specify. Editing the checker to always pass evades this brief. Trace the actual world.gd and check_world.gd rather than accepting a screenshot alone. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('STATE TRANSITIONS', 'Open is different from complete', F.state(),
    notes='15-17 min. Three collected lights unlock/color the exit; COMPLETE additionally needs the player within 20 units of it. With zero, one or two lights, even a player placed at the exit must not win. Once won, advance returns before tick increments or movement. Ask which state persists. Config survives in JSON, while player, collected, won and ticks belong to the current scene instance. This is a state-transition explanation, building on W7 rather than repeating classes. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('PERSISTENCE AND PROCESSES', 'A file write is one boundary', F.process(),
    notes='17-19 min. Python set validates and writes JSON. execute starts a new Godot process, whose scene _ready loads that file. An existing game keeps its loaded config, so close and relaunch it before judging an edit. inspect explicitly reports file_state_only true. Connect W10: stored values survive a process; an in-memory object is not a saved snapshot. Config, conversation history and an embedding index have different jobs. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(code_panel('PYTHON TOOL · ACTUAL EXCERPT', 'Reject the write before changing state', [
    'low, high = BOUNDS[key]',
    'if not low <= value <= high:',
    '    raise ValueError(f"{key} must be between {low} and {high}")',
    'config = load_config(path)',
    'config[key] = value',
], notes='19-21 min. This is a contiguous excerpt from update_config in world.py, not a standalone program. Earlier lines reject unknown keys, nonnumeric values and booleans. BOUNDS allows speed 60-480, pickup_radius 8-48 and exit_x 720-880; the comparison rejects nonfinite values. The following line writes JSON. Ask why validation occurs before loading/mutating/writing. Demonstrate set exit_x 2000 and inspect the unchanged config: a visible refusal is useful behavior. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('FEEDBACK', 'The next choice uses the observation', F.feedback(),
    notes='21-24 min. The recorded model chose 275 after the actual failed 125 check. The logger executed one requested action and contains no repair selection or retry loop. A deterministic workflow follows an already known sequence; it need not choose. The tutorial uses the same tools, with the learner explicitly making the choice. A real model may be another caller, but the current loop.py host does not call one. Explain where choosing stops and execution begins. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('HOST LIMITS', 'A bounded attempt has an ending', F.budgets(),
    notes='24-27 min. These are the current human-host limits: eight inspect/set/check actions, four mutations and 180 elapsed seconds. Reservation before dispatch means a failed tool consumes budget. Engine checks have a 15-second subprocess timeout. The 30-second decision target is instructional, not an enforced model timer. Missing structured output or tool errors stop the host; post-pass actions are refused. This is a small allowlist contract, not a sandbox for arbitrary code. The earlier Codex episode used its explicit brief and stop, not this later host. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(question('short_answer', 'A new speed is saved. Has the game changed?',
    hint='Distinguish stored config, an open scene and a new engine check.',
    notes='27-30 min. Allow one minute for a pair trace and two for discussion. Expected answer: the stored file changed, while the existing process may still use 125. A new process loads 275. The set return value establishes a write, not working motion. A real engine observation is needed for behavior, and the visible result still needs inspection. Resolve questions before the worked demonstration; do not turn this into another basic class lesson. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(section('ACTUAL MODEL EPISODE', 'Failure becomes useful information',
    'Read the observations before accepting the model’s conclusion.',
    notes='30-31 min. The genuine recorded episode used the current authorized Codex CLI session on 29 October HKT. The runtime reported GPT-6; an exact backend model ID was unavailable. No separately billed model endpoint or new account was used. The logger records one requested action, without choosing repairs. Reading replay.py today is a recorded replay, not a new model run. Keep that provenance explicit during the demo. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(code_panel('LIVE TOOLS · PAIRED PFAD CHECKOUT', 'Inspect, then run the engine', [
    'cd week12',
    'uv run python world.py inspect',
    'uv run python world.py check',
], lang='', notes='31-34 min. Run the exact commands individually from the pinned companion checkout. Restore supplied speed 125 before class. inspect returns file state only. The real check deliberately exits 1: two lights, x455.000732421875, tick 180, no win. Do not chain through this expected failure with &&. A missing executable, parser error or absent WORLD_CHECK is a setup/tool failure, distinct from this structured failed behavior. Let students read values before offering the repair. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('RECORDED OBSERVATIONS', 'What changed between these runs?', F.episode(),
    notes='34-37 min. Read the original observations exactly: 125 gives two lights, x455.000732421875, no win at 180 ticks; 275 gives three lights, x840.832336425781, win at 166 ticks. The model estimated from 375 units moved in three seconds and the exit threshold. Goal, pickups and original checker stayed fixed. Do not imply 275 is the only solution or that simple distance arithmetic exactly handles collection radii. The next engine check verifies the candidate. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('DECISION AND PROVENANCE', 'Preserve what the model actually saw', [
    'Model: inspect → failed check → choose 275 → pass → stop.',
    'Logger: one requested action; no repair choice.',
    'Later checks add premature-exit and stop probes.',
    'Later film uses the exact original final source.',
], notes="37-39 min. The fixture preserves seven original records, reasons, action arguments, stdout/stderr, exit codes and source hashes. Only machine-specific executable/project paths were sanitized. Raw UTC 28 October 16:xx is 29 October HKT. A later correction distinguishes successful socket creation from denied Wayland connection; that old restriction did not establish rendering. Full local access later enabled actual Xvfb/Mesa film. Current stronger probes and later capture are not retroactively attributed to the model's earlier observation. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

S.append(code_panel('HUMAN-DIRECTED ROUTE', 'Who chooses the next action here?', [
    'uv run python loop.py start',
    'uv run python loop.py inspect',
    'uv run python loop.py check',
    'uv run python loop.py set speed 275',
    'uv run python loop.py check',
    'uv run python loop.py status',
], lang='', notes='39-44 min. Rehearse the exact human-selected sequence on supplied 125. Say who chooses 275: the instructor here, not loop.py. Observe the expected first failure and passing second check. status reports passed, five actions and one mutation for this sequence. Inspect session.json observations and config hashes; then try a further set and show refusal. If an earlier session is active, explicitly stop/retain it before resetting. An optional fresh authorized model demonstration must be labeled separately from this human route and the recorded fixture. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(code_panel('PYTHON HOST · ACTUAL EXCERPT', 'Reserve the action before execution', [
    'state["actions"] += 1',
    'if action == "set":',
    '    state["mutations"] += 1',
    'event = {"action": action, "key": key, "value": value, "time": self.clock()}',
], notes='44-46 min. This actual contiguous excerpt reserves action/write counts before execution. Preceding checks reject expired time, action or mutation budgets. Subsequent code stores the event and before-config hash before calling the tool. Ask whether a Godot error should erase an attempted action: no, both the spent action and error should remain inspectable. The caller chooses action/key/value outside Session.run. No hidden retry or repair policy is implemented here. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('OBSERVATION TYPES', 'Not every failure means “try faster”', [
    'Structured no-win result: behavior missed the goal.',
    'Missing engine or parser error: the tool failed.',
    'Display denied: graphics is unverified.',
    'Budget expired: stop and ask for help.',
], notes='46-50 min. Give pairs two examples to classify: collected two at tick 180, versus absent WORLD_CHECK with stderr. A valid failed behavior observation can support a speed change; a missing engine cannot. Display denial means the visible route is unverified. Budget expiry requires stopping. The host records blocked/error status; direct tools preserve last-error.json. Blind retries hide faults and spend the budget. Ask for the next diagnostic action appropriate to each boundary. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(section('CHECK THE CHECKER', 'What could a green result miss?',
    'Test the rule by trying to break it.',
    notes='50-51 min. A test suite is an executable acceptance model with limits. A passed flag is not complete truth about the product. The current checker instantiates the actual scene and probes real state transitions. It does more than inspect an initial won flag. Ask which rule a programmer could accidentally weaken while retaining a superficially successful demo. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(code_panel('SHARED BEHAVIOR · ACTUAL GODOT EXCERPT', 'Winning stops the state update', [
    'func advance(delta: float, automatic: bool) -> void:',
    '    if won:',
    '        return',
    '    ticks += 1',
    '    var target := Vector2(float(config.exit_x), 300)',
], lang='', notes='51-53 min. Actual world.gd excerpt. Movement and ordered pickup logic follow below. Config loads at startup; ticks/won/player/collected live in the scene. The checker explicitly calls advance at 1/60 second; manual and replay physics callbacks call the same function. This is DRY with a purpose: one shared behavior with several observations. Ask why the win guard precedes ticks += 1. The post-win test requires both position and ticks to stay fixed. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('REAL ENGINE CHECKS', 'Try the exit before the lights', [
    'Place the player at the exit with 0, 1 and 2 lights.',
    'All three transitions must reject a premature win.',
    '125 fails; 275 recovers; 60 and 480 test boundaries.',
    'After a win, advancing again must keep state fixed.',
], notes="53-56 min. Run uv run python -m unittest discover -p 'test_*.py' -v from week12. Twelve tests passed in author verification, including two actual engine cases. Disposable mutants removing collected == 3 or the won guard were rejected: premature_exit_rejected false or stopped_after_win false, both exit 1. These are human-selected verification experiments, not original model decisions. The suite does not prove every manual-control, game-feel or graphics property. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

S.append(question('short_answer', 'The engine check passes. Can the film still be wrong?',
    hint='Give a concrete counterexample, then propose another observation.',
    notes='56-60 min. Give pairs two minutes and discuss for two. Concrete counterexamples: black rendering, wrong scene/camera, stale config film, unreadable labels or an ending that never reaches COMPLETE. Need fresh capture provenance, metadata/decode and actual viewing. Another behavior assertion alone cannot settle black frames. Close visible games before the full break; leave the passing config/evidence available for the capture demonstration. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(section('60–70 · BREAK', 'Back in ten minutes',
    'Next: one simulation becomes a visible, checked film.',
    notes='60-70 min. Full ten-minute lecture break. Stop visible playback. Keep sources/evidence ready without adding installations during the break. The separate tutorial break is 55-65; these are different sessions. Resume at minute 70 with the known automatic route and the two clocks. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(section('REPLAY AND FILM', 'Playback follows a known route',
    'The model’s decision and the camera’s output are different work.',
    notes="70-71 min. Re-establish the distinction between the model choosing a revised config and playback following a known route. The supplied automatic motion targets the next light and then the exit. No model chooses actions during replay or Movie Maker recording. Keeping filming deterministic makes the chosen world's behavior easier to inspect, but does not itself prove model adaptation. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

S.append(figure_slide('TWO CLOCKS', 'Ticks are not rendered frames', F.timing(),
    notes='71-74 min. Physics defaults to 60 ticks/s and the check explicitly advances 180 ticks. Movie Maker captures 30 rendered frames/s for 120 frames: four seconds. At speed 275, tick 166 is about 2.77 simulated seconds, leaving a completion hold. This is neither 180 rendered frames nor the wall-time action budget. Recording may run faster/slower than real time; fixed fps preserves simulated movie timing. Source: https://docs.godotengine.org/en/4.7/tutorials/animation/creating_movies.html . Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('REAL CURRENT EDITOR', 'Open the supplied scene, then run it', F.editor(),
    notes='74-77 min. Actual official 4.7.2 editor on isolated Xvfb/Mesa, 29 October. Import week12/godot/project.godot in Project Manager, open world.tscn, choose 2D and locate World/world.gd/world.json. The screenshot gives orientation; do not ask the room to read small menu text. Runtime drawing leaves the editor canvas blank by design. F6 or world.py play reveals the actual world. Stop an editor run before launching another. Normal Ctrl+Q/Enter exited 0 with no remaining engine process. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(code_panel('RUN FROM WEEK12', 'Check before capturing', [
    'uv run python world.py check',
    'uv run python world.py replay',
    'uv run python world.py capture',
], lang='', notes='77-82 min. Budget five minutes for visible replay, closing the game, capture and opening the output. Config 275 must pass. Manual play uses arrow keys; replay is automatic. Capture removes old movie/report/sample files, reruns the check, then invokes real graphical Movie Maker and FFmpeg. If graphics fails, preserve the error and explicitly label the reference clip fallback. Never substitute dummy/headless frames. Latest standard Godot, FFmpeg/ffprobe and working graphics are prerequisites; no model account, bridge or dedicated GPU is required. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(code_panel('CAPTURE · ACTUAL ARGUMENTS', 'Request a finite movie', [
    'result = execute(["--write-movie", str(movie),',
    '                  "--fixed-fps", "30",',
    '                  "--quit-after", "120",',
    '                  "--", "--replay"], timeout=90)',
], notes='82-84 min. This is the actual world.py call with equivalent line wrapping. The movie path is absolute; Godot evaluates relative paths from its project folder. The separator -- sends --replay to the scene. --quit-after limits rendered frames, while the checker counts physics ticks. The 90-second timeout limits engine wall time. Encoding is bounded to 60 seconds, full decode to 30 and probes/samples to 15 each. Separate list arguments avoid interpolating a shell command. Source: current Godot 4.7 CLI and Movie Maker docs. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('ACTUAL FILM · 0 SECONDS', 'Before: three lights remain', F.screenshot('frame-start.png'),
    notes='84-85 min. The real film starts with player left, zero of three lights and grey exit. Source hashes identify the exact original final model-selected source. The later film does not silently rewrite the checker or world. Open the actual four-second clip as well as this sampled frame. A valid-looking initial frame alone says little about completion. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('ACTUAL FILM · 1.5 SECONDS', 'During: two lights collected', F.screenshot('frame-middle.png'),
    notes='85-86 min. At 1.5 seconds the player has moved right and collected two lights. Only the third light remains; the exit is still grey. This supports motion and order, unlike a valid container or changing file hash. Compare positions and the counter with the start. Current capture uses the same behavior with stronger checks and completion logging, separately from this original-source reference film. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('ACTUAL FILM · 3.9 SECONDS', 'After: open exit and COMPLETE', F.screenshot('frame-end.png'),
    notes='86-88 min. The final frame shows three lights collected, mint exit, player at exit and COMPLETE. The win guard holds the state. View the continuous clip so ordered collection and movement are visible between stills. Ask what the model chose and what playback did. Later deterministic filming cannot be described as another model decision episode. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(figure_slide('ACCEPTANCE', 'Check three different claims', F.evidence(),
    notes="88-91 min. Three acceptance layers answer different questions. Behavior: real engine, three pickups, time-bound completion, premature-exit rejection and freeze. File: 960x540, four seconds, 120 frames, H.264/yuv420p and full FFmpeg decode. Visible: real world, movement, collection order and COMPLETE. A black or stale clip can pass file checks. The report retains visual_inspection_required true because a person must inspect each new capture, not only the author's reference. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

S.append(content('KEEP A REVIEWABLE ATTEMPT', 'A clip belongs with its config', [
    'Retain world.json, check.json and session.json.',
    'Keep capture.json, world.mp4 and three sampled frames.',
    'Compare the copied config with the capture report.',
    'Open the copied clip before changing the next attempt.',
], notes='91-95 min. Show the actual hidden .output directory. Config and hashes identify which speed was filmed; a filename or timestamp alone can be stale. Each partner copies their own config/check/session/report/clip/frames before the next reset. Open the copied clip to test that evidence actually transferred. Retain last-error.json with unfinished work. These are practice artifacts, not a new Canvas submission. Do not put identifiable student records into public fixtures. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(section('COMPARE AND TRANSFER', 'A claim should point to evidence',
    'The right next check depends on the missing observation.',
    notes='95-96 min. Return to the opening trust question. Students should now name a particular missing observation and the boundary it belongs to. A generic suggestion to test more is less useful than identifying the fresh process, actual tool result, config identity or visible film that would settle the claim. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('CHALLENGE THE SUCCESS CLAIM', 'Which boundary would you inspect?', [
    '“I saved speed 275, but the open game is still slow.”',
    '“The checker passed; my MP4 is from yesterday.”',
    '“I read the model trace, so I ran an agent.”',
    '“The valid MP4 shows a black screen.”',
], notes='96-101 min. Give pairs two minutes to select a claim, name its missing boundary and propose an exact action; discuss for three minutes. Expected: restart the process; compare config/hash and capture afresh; label read-only recorded replay; inspect real rendering and scene content. Model confidence is not process or visual evidence. Ask whether the proposed action would actually distinguish the suspected fault. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('HANDBOOK TOOL · CROSS-WEEK TRANSFER', 'A retrieved source is an observation too', [
    'Week 10 lost-card query → actual cited passage.',
    'PDF p20 / printed p9 · hb2026-p020-replacement.',
    'Same MiniLM revision · 384 dimensions · score 0.815428.',
    'Index / saved history / transient prompt / spoken reply.',
], notes='101-104 min. Maximum three-minute handoff. The author independently ran W10 handbook.py with the exact prepared query: What should I do if I lose my student identity card? The actual top result is hb2026-p020-replacement, PDF position 20 / printed page 9, cosine 0.815428; return chunk 0.763087. This is direct retriever execution, not a new model call. W10 exposes retrieve_handbook as the agent tool. The six short genuine extracts use sentence-transformers/all-MiniLM-L6-v2 revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41, dimension 384, attention-masked mean pooling, L2 normalization and max_tokens 256. Query and document vectors stay in that same space. Source is the official Student Handbook for Taught Programmes 2026/27, PDF SHA 108956feb2ffac665f8ca0f5a8f68d7150a85fda15e219916785ec50331a4e94; PDF pages 20/25/76 are short extracts, not a full index. The matching real observation and hashes are in the W12 handbook-handoff.json fixture. Four lifetimes: indexed knowledge survives calls; owner-scoped conversation rows persist/reopen; the prompt assembles system/current question/history/tool results for a call; spoken output is derived and checked separately. Scene config is none of these. The world remains self-contained and does not search the handbook. Source index: https://github.com/sd5913/pfad/blob/c59fae0df42e316a431c308bfe582a84411d5887/week10/fixtures/handbook.json . Runnable world source: '+SOURCE))

S.append(content('PROJECT JUDGEMENT', 'Where would one bounded check help?', [
    'A game: can a player reach the exit?',
    'An installation: what happens when input disappears?',
    'A design tool: did the exported artifact match the brief?',
    'Choose a small interaction another person can try.',
], notes='104-108 min. Give two minutes for an individual project example, then hear two responses. Connect historical DRY, small steps and user testing with W8 CI without repeating setup. An agent helps when choosing among actions adds value; a known button/function can remain a direct workflow. Ask for one expected result and one useful failure. These are project possibilities, not mandatory AI/Godot features or a new graded artifact. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(statement('Observe. Choose. Act. Check. Stop.',
    notes="108-110 min. Retrieval practice: ask students to name an actual value or file for each verb. Observe two lights/180 ticks; choose 275; act through the JSON write; check the actual engine's 166-tick win; stop with passed status. Then identify what remains separate: visual inspection and classroom/platform setup. Ask one pair to distinguish model choice from deterministic recording. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

S.append(content('SEPARATE 120-MINUTE TUTORIAL', 'Keep time for the work and the support', [
    '0–20 setup; at 20 move to the prepared partner machine.',
    '20–55 brief, trace and bounded change; 55–65 break.',
    '65–85 fail/adapt/check; 85–100 film and retrieve.',
    '100–120 delivery-candidate tutor support.',
    '[Complete tutorial and runnable source]('+SOURCE+')',
], notes='110-113 min. The tutorial has exact blocks 0-20, 20-35, 35-55, 55-65, 65-85, 85-100 and 100-120. Support includes unfinished projects; do not repair setup by consuming the break or delivery-candidate review. Commands use simple uv run inside the self-contained week12 folder. Core Python has no third-party dependencies; Godot and FFmpeg are external prerequisites. Tutorials need no instructor/ClassPoint login. Explain the minute-20 prepared-machine handoff before students need it. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(content('MINUTE 20 · PREPARED HANDOFF', 'Both learners operate and retain a turn', [
    'Import week12/godot/project.godot on a verified machine.',
    'First learner operates 35–55; swap for 65–85.',
    'Each makes a change and runs their own check.',
    '85–100: seven minutes each for film/copy; one to verify.',
], notes="113-116 min. Prepared means latest Godot, this starter, visible play, fail/pass checks, capture and viewed clip have already passed on that machine. Open a terminal in week12 and locate world.json and hidden .output. Observer predicts/checks, then swaps. Each learner operates their own reset/start/fail/set/check/capture and copies config/check/session/report/clip/frames before the next reset. Transfer and open on the learner's own laptop. Author rehearsal measured 9.484s download, 31.215s active route plus 29.312s full orientation, with existing Python/FFmpeg. It was scripted operator feasibility, not novice or Windows/macOS timing. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

S.append(content('EXISTING GROUP PROJECT', 'Bring a delivery candidate to the tutor', [
    'One working interaction, a failure/check and a runnable README.',
    'Public sd5913-owned team repo; teammates have Write access.',
    '40% · idea 25% / code 50% / execution 25%.',
    'Due 6 December 2026, 23:59 HKT · submit through Canvas.',
], notes='116-118 min. Existing project policy only. Show one working interaction, one failure/check and a runnable README during the 26 November delivery-candidate support block. Update the existing progress record with feedback and next action. GitHub Projects is recommended; an equivalent accessible record is valid. The project remains 40%, rubric 25/50/25 and deadline 6 December 2026, 23:59 HKT. No new upload or compulsory defence. Week 13 is final quiz/revision and support including unfinished work, not another technical practical. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12'))

S.append(end('What actually happened?', 'Show the observation, the change, the check and the stopping point.',
    'sd5913.github.io/teaching', notes="118-120 min. Questions and tutorial handoff. Return to the four outcomes using actual values and files. Evidence should distinguish model choice, human action, recorded replay and deterministic film. Instructor preflight refreshes latest Godot/news, tests classroom graphics and the prepared partner, and checks the pinned W10 source-index handoff. Independent review remains separate from this author's successful local checks. Point to the pinned complete PFAD README. Runnable source: https://github.com/sd5913/pfad/tree/4f2864a02ca32a200cbf7da34a02d33ec917e80f/week12"))

attach_reports(S, HERE / 'week12-reports.json')
DECK = {'title': 'SD5913 · Week 12 · Build, check and film',
        'pdf': 'SD5913-week12.pdf', 'slides': S}
