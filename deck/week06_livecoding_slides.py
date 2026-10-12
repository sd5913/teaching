"""Live coding progression: website first, then the current Easel bridge."""
from deckgen import T
from deckgen.layouts import content, code_panel, section
from week06_strudel import STAGES, editor_link

EASEL_DOCS = 'https://github.com/venetanji/easel-client/blob/d8dda0f1b953136ee7fc827eeeb39104471770b4/docs/strudel.md'


def livecoding_slides():
    slides = [
        section('04 · LIVE CODING', 'Change the score. Hear the change.',
            'Hi-hat → bass → chords → melody → an agent-assisted variation',
            notes='Open Strudel in a separate tab. Keep the HTML lesson tab available. '
            'Linked stages are used instead of an iframe so keyboard shortcuts and audio stopping have one clear owner. '
            'Stop the editor before switching back; changing a slide cannot stop another tab.'),
        content('04 · LISTEN FIRST', 'Begin with a working example', [
            '[Open strudel.cc](https://strudel.cc/)',
            'Play the existing starter or an example selected by the instructor.',
            'Change one value. Update. What did you hear?',
            'Stop before returning to the slides.',
        ], notes='Use the existing starter shown by the editor or a previously chosen example, not a blank page. '
            'Start quietly and point out Play, Update and Stop. Ctrl+Enter plays or updates; Ctrl+. stops. '
            'The current public starter was tested through the cloud browser for Play and Stop UI state, not human audibility. '
            'Do not assume an example using a website sample bank will transfer to Easel. '
            'Tutorial video selection is still pending; the resources page says so without a fabricated link.'),
        content('04 · A SMALL MUSICAL LANGUAGE', 'Four layers share one cycle', [
            '**Hi-hat** marks the pulse. **Bass** gives a low foundation.',
            '**Chords** put notes together. **Melody** moves through notes.',
            '*8 repeats; ~ is a rest; commas put notes together.',
            'setcpm(100/4) means 25 cycles/minute: four beats at 100 BPM.',
        ], notes='Strudel is JavaScript with a small pattern language inside strings. '
            'A cycle is the shared repeating time span; the number of events in a pattern is independent of its duration. '
            's chooses a sound, note supplies pitches, gain scales signal level and stack combines patterns. '
            'Do not equate a gain value with a guaranteed perceived loudness. '
            'Sources: https://strudel.cc/workshop/first-sounds/ and https://strudel.cc/workshop/first-notes/'),
    ]
    prompts = [
        'Change hh*8 to hh*4. Predict the difference before Update.',
        'Keep the hats. Move c2 and g2 up to c3 and g3.',
        'Keep the first two layers. Change e3 to eb3.',
        'Keep the other layers. Replace one melody note with ~.',
    ]
    for i, (stage, prompt) in enumerate(zip(STAGES, prompts), 1):
        slide = code_panel(f'04 · LAYER {i} OF 4', stage['label'],
            stage['code'].rstrip().splitlines(), lang='js',
            caption=prompt,
            notes='This is the complete cumulative score, ready to replace the editor buffer. '
            'The linked editor starts silent; the user presses Play. Keep one tab per score or stop before changing tabs. '
            'Read only the newly added line aloud. ' + prompt + ' '
            'Each next link restores the supplied baseline: undo an experiment before adding the next layer. Hi-hat uses the website’s default hh; Easel uses its own bundled hh, '
            'so identical syntax does not promise identical timbre. No remote bank loading is required. '
            'Source and downloadable score: resources.html#' + stage['id'])
        # Reserve distinct code, experiment and link bands.
        for el in slide.els:
            if el.kind == 'rect' and el.y == 372:
                el.h = 460
            elif el.kind == 'text' and el.name == 'code':
                el.h = 440
            elif el.kind == 'text' and el.y == 916:
                el.y = 856
        slide.els.append(T(120, 928, 1400, 44,
            '[Open this complete stage in Strudel](' + editor_link(stage['code']) + ')',
            'body', 30, '#006B74'))
        slides.append(slide)
    slides.extend([
        content('04 · TAKE THE SCORE TO EASEL', 'Let the agent change one layer', [
            'Create a fresh project, then Templates → Strudel sound.',
            'Paste the four-layer score. You press Run to start sound.',
            '“Make the melody more spacious. Keep the other layers and tempo.”',
            'Inspect the edit, compare it with your prediction, then Stop.',
        ], notes='Current Easel source supports agent editing through window.EaselStrudel. '
            'setCode fills the buffer; evaluate compiles or updates the current clock, but neither starts audio. '
            'The user supplies Run. Keep .play() out of submitted score code. '
            'Start a fresh project as well as a fresh template: older projects can pin older kits without hh. '
            'If the installed build differs, keep the exercise on strudel.cc. '
            'Use bundled drums and native synths rather than assuming website sample banks exist locally. '
            'Source-verified, not an installed-classroom-client test: ' + EASEL_DOCS),
        content('04 · KEEP THE RESULT', 'A live edit needs a saved version', [
            'Keep the starting score and the changed score.',
            'Ask the agent to save the working score, then reopen and check it.',
            'For a short file: Run → choose cycles → Export WAV.',
            'Explain what you changed and what you actually observed.',
        ], notes='Instructor implementation detail: inspect getState().code through execute_canvas_javascript. '
            'For durable live edits, patch instance app.js DEFAULT_LIVE_CODE with reload:false, verify the save, '
            'then evaluate the same complete score. Runtime edits alone do not create source history. '
            'Source-only saves gate WAV export until reload; reload stays silent and the user presses Run again. '
            'Export is a bounded render: 1–16 four-beat cycles, max 30 seconds including a 0.5-second tail, '
            '48 kHz stereo PCM16. Not every live effect or sample manipulation can export. '
            'The starter deliberately uses a small supported subset. Stop/Escape/Ctrl+. silences the Easel template. '
            'Current docs/source verified; instructor is checking their local build separately. ' + EASEL_DOCS),
        content('MAKING · 18 MINUTES', 'Predict → ask → inspect → listen', [
            'Choose one layer and describe a change to its musical role.',
            'Ask the agent for one small edit. Read the changed code.',
            'Run it, compare versions, and test Stop and repeated updates.',
            'Keep both scores and one sentence explaining your decision.',
        ], notes='Pairs use a current Easel project or remain in Strudel if setup is unavailable. '
            'The agent can draft a score that students paste into the website; no agent account or API generation is required. '
            'Reserve the final four minutes for a partner to try it before explanation. '
            'Offer waveform/visual inspection for anyone who prefers not to listen. '
            'This is formative practice, not another assessed task. No external sample bank or Suno call is needed.'),
    ])
    return slides
