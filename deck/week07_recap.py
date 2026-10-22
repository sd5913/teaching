"""Twenty taught slides, reused rather than rewritten for the midterm recap."""
from copy import deepcopy
from importlib import import_module
from deckgen.layouts import add_chrome

SELECTION = {
    1: ('Programs are instructions for changing state', 'Git and GitHub'),
    2: ('Three questions, all semester', 'Six types, and that is most of it',
        'A cap never sits under a drawn cell', 'A repo that does not say what it needs\nis not finished.'[:60]),
    3: ('That is a loop, and that is all of it', 'A rule with a name',
        "Four rules for taking somebody else's numbers", 'The same numbers, five ways'),
    4: ('Three parts of the interaction', 'One promise, four steps',
        'Ask for September', 'Return data. Draw in the browser.'),
    5: ('One position. Three channel values.', 'Time is another axis of change',
        'Learn to remove noise; then use that skill.'),
    6: ('A sound gives values positions in time', 'A sample rate gives the sequence a duration',
        'Frequency and sample rate'),
}

RECAP_NOTES = {
    'A cap never sits under a drawn cell':
        'A specification describes what must remain true in the picture. The previous cell in '
        'the same column supplies the boolean needed to decide whether to draw a cap.',
    'A repo that does not say what it needs\nis not finished.':
        'Ask what a classmate would need to run the code from a fresh checkout: instructions, '
        'dependencies, and any permitted data or assets.',
    'That is a loop, and that is all of it':
        'Point out that the indented body runs once per item. In Python the indentation '
        'determines which statements belong to the loop.',
    'A rule with a name':
        'The argument is local to the function. Without an explicit return, Python returns None. '
        'Ask how a caller could use the result of bar(height).',
    "Four rules for taking somebody else's numbers":
        'Caching a permitted raw response makes later runs independent of a changing URL. '
        'Discuss the difference between JSON and HTML and avoid repeated requests to a public server.',
    'The same numbers, five ways':
        'Each view answers a different question about the same tide data: return of the cycle, '
        'hourly height, daily rhythm, differences between days, or the fortnightly pattern.',
    'One promise, four steps':
        'This depicts the test-driven development sequence, not a live exercise today. '
        'A failure only supports the missing-feature hypothesis if the test reaches that feature; '
        'a network error alone does not.',
    'A sound gives values positions in time':
        'This tiny sequence is illustrative, not a playable sound file. Positive and negative '
        'are opposite signal displacements, not louder and quieter.',
}

def recap_slides(first_number=3):
    slides = []
    for week, titles in SELECTION.items():
        source = import_module(f'week{week:02d}').S
        for title in titles:
            matches = [s for s in source if s.title == title]
            if len(matches) != 1:
                raise ValueError(f'Expected one Week {week} slide: {title!r}')
            slide = deepcopy(matches[0])
            slide.els = [e for e in slide.els if not getattr(e, 'name', '').startswith('chrome-')
                         and getattr(e, 'name', '') not in ('week05-slide-number', 'week06-slide-number')]
            slide.cp = None
            slide.report = ''
            if title == 'That is a loop, and that is all of it':
                slide.els[2].paras[4].runs[0].text = (
                    'The same pattern can update a picture instead of printing a value.')
            if title == 'A rule with a name':
                body = slide.els[2].paras
                body[2].runs[3].text = ', Python returns '
                body[2].runs[4].text = ''
                body[2].runs[6].text = '; callers must handle that value.'
                body[4].runs[0].text = 'Check the returned value when you use a generated function.'
            if title == 'Learn to remove noise; then use that skill.':
                source = slide.els[3].paras[0].runs
                source[1].text = 'week05/diffusion/generate.py'
                source[1].url = 'https://github.com/sd5913/pfad/blob/2026/week05/diffusion/generate.py'
            slide.notes = (f'Quick recap from Week {week}. Explain the key relationship; do not rerun '
                           'the original exercise or its timing. Park longer questions for the AMA.\n'
                           + RECAP_NOTES.get(title, 'Original teaching context:\n' + slide.notes))
            if title == 'Learn to remove noise; then use that skill.':
                slide.notes += ('\nThe linked current-year Week 5 script runs pretrained inference; '
                                'it does not train the denoiser shown in the upper row.')
            add_chrome(slide, first_number + len(slides), f'SD5913 / WEEK 07 / RECAP WEEK {week:02d}')
            slide.chrome = False
            slides.append(slide)
    return slides
