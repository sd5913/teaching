"""19 November 2026: authentication, deployment and agent-assisted 3D work."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from deckgen.layouts import title, agenda, section, statement, content, end
import week09_layouts as L
import week11_auth
import week11_blender

E = 'SD5913 / WEEK 11 / 19 NOVEMBER 2026'
# Refresh only after the paired companion is tested and committed.
PFAD = 'https://github.com/sd5913/pfad/tree/b42f5fde0da478fe3932f997e324efd063299fb5/week11'
SOURCE = PFAD.replace('/tree/', '/blob/')
S = []


def prose(heading, lines, notes, label='CREATIVE APPLICATIONS'):
    S.append(content(label, heading, lines, body_size=40, notes=notes))


S.append(title(E, 'Identity, deployment\nand creative tools.',
    'From authenticated requests to an agent-assisted Blender object in Godot.', size=112,
    notes='0-1 minutes. Thursday19 November 2026. 120-minute lecture with 55-65 break; separate '
    '120-minute tutorial. Build from Week 10 account rows into authentication, password verification, '
    'sessions and OAuth, then show the GitHub deployment path. After the break explain Blender '
    'scene data/Python, ask an agent to change a real object, and use the same saved object in '
    'Godot. Preserve the same handbook embeddings, conversation memory and spoken reply from '
    'Week 10: identity and creative actions extend that work; they do not replace retrieval. '
    'Companion: ' + PFAD))
# Four dated news items fit within the existing ten-minute opening.
prose('GPT-6.2 Astra and Sol', [
    '17 November / OpenAI releases new coding and work models.',
    'OpenAI reports better outputs, but also omitted blockers in two tests.',
    'What should an agent say when the scene file is missing?',
], '1-2 minutes. Available in ChatGPT Work/Codex for Plus, Pro, Enterprise and Edu, and API. '
   'OpenAI reports a Codex instruction mitigation for obstacle omissions. These are vendor '
   'observations, not an independent classroom comparison. Ask for an honest stop and evidence '
   'before changing the scene. No new model run or account is required. Source, checked '
   '18 November 2026: https://openai.com/index/introducing-gpt-6-2-astra-sol/',
   label='AI NEWS / 17 NOVEMBER 2026 / OPENAI')
prose('Gemini 4 Hydrogen', [
    '12 November / Google releases a model for fast agent execution.',
    'An orchestrator can switch between Carbon and Hydrogen.',
    'What must an editing agent hand to a separate verifier?',
], '2-3 minutes. Google article updated 16 November, checked 18 November 2026. '
   'Available across Gemini, AI Studio and API tiers; Antigravity requires Pro or Ultra. '
   'Google reports near-Carbon task success with 24% less quota and 19% faster completion '
   'on Terminal-Bench 4.0. This vendor benchmark does not establish our camera task quality. '
   'Keep the same brief and acceptance criterion; inspect the diff and current render. Source: '
   'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/',
   label='AI NEWS / 12 NOVEMBER 2026 / GOOGLE')
prose('Qwen4-Max', [
    '16 November / Alibaba releases vision and tool use with long context.',
    'Available through QwenCloud, QwenWork and QwenStudio.',
    'Which intermediate result would you review before the next action?',
], '3-4 minutes. Alibaba announces a one-million-token context window. Long context and '
   'vendor demonstrations do not guarantee a correct long-running task. Ask for a small diff, '
   'a current render and a clear stop condition. Smaller open-weight Qwen4 models are promised; '
   'this announcement does not establish Max as open source. Checked 18 November 2026. Source: '
   'https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max?_p_lc=1',
   label='AI NEWS / 16 NOVEMBER 2026 / ALIBABA')
prose('Seedream 5.5 and Layers', [
    '12 November / Runway Dev adds image generation and layer extraction.',
    'Layers returns a base image and transparent PNG layers.',
    'After moving one object, which edges and hidden areas need checking?',
], '4-5 minutes. Runway documents source-image decomposition into raster layers, not native '
   'vector objects. Compare a selective edit with whole-image regeneration in discussion; '
   'do not add another live practical. maxImages caps returned images (2-100, default 30); '
   'billing is per returned image after a credit reservation. Use an instructor-owned synthetic '
   'image only if preparing an optional later example; no upload or paid call is needed today. '
   'Checked 18 November 2026. Source: https://docs.dev.runwayml.com/api-details/api_changelog/',
   label='AI NEWS / 12 NOVEMBER 2026 / RUNWAY DEV')
S.append(agenda(E, ['5-30 / authentication: credentials, hashes and sessions',
    '30-55 / GitHub identity and deployment walkthrough',
    '55-65 / break', '65-85 / Blender: scene data and Python',
    '85-103 / ask an agent, observe and revise',
    '103-115 / the same object in Godot', '115-120 / tutorial handoff and questions'],
    notes='End opening at minute 5. News is four brief items within1-5; show the agenda briefly '
    'as a transition. Theory precedes configuration. The second half follows one object from '
    'Blender to Godot. The separate tutorial offers one route: authentication or Blender/Godot, '
    'with its own 55-65 break and 100-120 tutor/project support.'))
S.extend(week11_auth.build())
S.append(section('55-65 / BREAK', 'Back in ten minutes.',
    'After the break: ask an agent to change a Blender scene.',
    notes='Protect the full ten-minute break. No remote class, deployment or personal Blender '
    'scene is needed for the prepared demonstration. At minute 65 begin with the actual render.'))
S.extend(week11_blender.build(SOURCE))
S.append(L.compare('Choose one route for the separate tutorial.',
    ('Authentication', 'Sign in and save\na private note.', 'Inspect the template, revise its UI and trace deployment.'),
    ('Blender -> Godot', 'Ask an agent to\nchange an object.', 'Render, review, revise and import the same saved mesh.'),
    notes='115-117 minutes. PFAD README is the complete 120-minute student/TA guide, no instructor '
    'login or ClassPoint needed. Each route keeps55-65 break and 100-120 project/tutor support. '
    'Authentication uses a personal template copy/OAuth App/Cloudflare account; Blender uses '
    'a personal PFAD fork and the supplied small 3D preview. A prepared partner supports setup '
    'failures; a recording alone is not hands-on work. No new assessment is added. ' + PFAD))
S.append(L.rows('Keep the project support time.', [
    ('19 November', 'Use tutorial minutes 100-120 with the tutor.'),
    ('Group repository', 'Public, owned by sd5913, teammates have Write access.'),
    ('Final project', '40%; rubric 25 / 50 / 25; due 6 December, 23:59 HKT.')],
    notes='117-118 minutes. Rubric is25% idea,50% code,25% execution. Canvas governs submission. '
    'GitHub Projects is recommended; an equivalent accessible progress record is valid. Personal '
    'exercise/OAuth ownership does not change the group repository rule. No requirement to use '
    'today\'s tools in the project. Week 12 retains the complete bounded Godot agent/check/revise/film '
    'episode; today\'s import prepares the asset concept without replacing it.'))
S.append(statement('AMA.\nAsk me anything.', size=130,
    notes='118-120 minutes. Open the floor for questions about the lecture, the project or using '
    'agents in creative work. Invite questions on password verification versus sessions, state/code '
    'versus app session, GitHub CI versus a deployed Worker, or editable scene versus imported '
    'asset. Ask students which observation would let them accept their next change. Protect the '
    'separate tutorial and tutor support allocation.'))
S.append(end('Make it yours.', 'Trace the identity. Inspect the result. Decide what to accept.',
    'SD5913 / PFAD / WEEK 11', notes='Close at minute 120 after the AMA. Continue with the selected '
    'route in the separate tutorial and keep the scheduled tutor/project support time.'))

DECK = {'title': 'SD5913 / Week 11 / Identity, deployment and creative tools',
        'pdf': 'SD5913-week11.pdf', 'slides': S}
