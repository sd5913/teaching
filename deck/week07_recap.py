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
            slide.notes = (f'Quick recap from Week {week}. Explain the key relationship; do not rerun '
                           'the original exercise or its timing. Park longer questions for the AMA.\n'
                           'Original teaching context:\n' + slide.notes)
            add_chrome(slide, first_number + len(slides), f'SD5913 / WEEK 07 / RECAP WEEK {week:02d}')
            slide.chrome = False
            slides.append(slide)
    return slides
