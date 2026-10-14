"""Four cumulative Strudel layers for the first half of the lesson."""
from deckgen import T
from deckgen.layouts import content, code_panel, section
from week06_strudel import STAGES, editor_link

def livecoding_slides():
    slides = [
        section('03 · MUSIC · LIVE CODING', 'Hear your code',
            'Hi-hat → bass → chords → melody',
            notes='Open Strudel in a separate tab. Keep the HTML lesson tab available. '
            'Linked stages are used instead of an iframe so keyboard shortcuts and audio stopping have one clear owner. '
            'Stop the editor before switching back; changing a slide cannot stop another tab.'),
        content('03 · MUSIC · LISTEN FIRST', 'Begin with a working example', [
            '[Open strudel.cc](https://strudel.cc/)',
            'Play the existing starter or an example selected by the instructor.',
            'Change one value. Update. What did you hear?',
            'Stop before returning to the slides.',
        ], notes='Use the existing starter shown by the editor or a previously chosen example, not a blank page. '
            'Start quietly and point out Play, Update and Stop. Ctrl+Enter plays or updates; Ctrl+. stops. '
            'The current public starter was tested through the cloud browser for Play and Stop UI state, not human audibility. '
            'Do not assume an example using a website sample bank will transfer to Easel. '
            'Tutorial video selection is still pending; the resources page says so without a fabricated link.'),
        content('03 · MUSIC · PATTERNS', 'Four layers share one cycle', [
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
        slide = code_panel(f'03 · MUSIC · LAYER {i} OF 4', stage['label'],
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
    return slides
