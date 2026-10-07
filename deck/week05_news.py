"""Three dated discussion slides, researched 7 October 2026.

Keep the sources, vendor benchmark settings and the before/after activity distinct.
The existing deckgen Embed accepts a video ID only; the visible timestamped link
opens the excerpt start, while the instructor stops at the printed end time.
"""

from deckgen import Embed, Rect, T, INK, MUTED, ORANGE, PAPER, TEAL
from deckgen.layouts import cards

PROMPT = 'Should a developer understand every line of code they ship?'
CHOICES = 'A  Agree       B  Unsure       C  Disagree'
MAY_SOURCE = 'https://world.hey.com/dhh/coding-should-be-a-vibe-50908f49'
JAN_SOURCE = 'https://world.hey.com/dhh/promoting-ai-agents-3ee04945'
OCT_SOURCE = 'https://world.hey.com/dhh/over-my-dead-pencil-fb0f3647'
OPUS_SOURCE = 'https://www.anthropic.com/claude-opus-5-5'
SOL_SOURCE = 'https://openai.com/index/introducing-gpt-6-1-sol/'
DOTS_SOURCE = 'https://openai.com/index/introducing-dots/'
VIDEO_ID = 'vDjW_dRyKXY'
VIDEO_START = 'https://www.youtube.com/watch?v=vDjW_dRyKXY&t=1694s'


def add_poll(slide):
    """Two separate slide activities, with the same wording and no right answer."""
    slide.els[0].name = 'question-eyebrow'
    slide.els += [
        Rect(120, 794, 1680, 2, '#D7D9D7'),
        T(120, 820, 1680, 95, PROMPT, 'xbold', 44, INK, lh=1.1),
        T(120, 930, 1320, 48, CHOICES, 'body', 30, TEAL, lh=1.2),
    ]
    return slide


def news_slides(before, after):
    # The literal content(..., cp=...) calls live in week05.py so the existing
    # after-class report scanner can find all four polls in presentation order.
    before.els = before.els[:2]
    before.els[1] = T(120, 192, 1680, 140, 'DHH wanted to keep the keyboard',
                      'xbold', 72, INK, lh=0.95, spc=-0.03)
    before.els += [
        T(120, 345, 1680, 220,
          '“AI is a superb pair programmer, but I\'d retire before permanently '
          'handing it the keyboard to drive the code.”',
          'body', 54, INK, lh=1.2),
        T(120, 606, 1680, 96,
          'David Heinemeier Hansson, creator of Ruby on Rails. '
          'He already used AI to look up APIs and discuss ideas.',
          'body', 32, MUTED, lh=1.3),
        T(120, 725, 1680, 40, f'[Coding should be a vibe!]({MAY_SOURCE})',
          'body', 26, TEAL, lh=1.2),
    ]
    before.notes = (
        'Take the BEFORE vote before advancing. There is no correct answer. '
        'Ask one person to explain a reason; do not tell the room how DHH later changed. '
        'This is his own May 13, 2025 statement, not an anti-AI position: he used LLMs '
        'daily but wanted to keep writing the code himself. Source: ' + MAY_SOURCE + '. '
        'Intermediate context for discussion after the reveal: on January 7, 2026 he '
        'endorsed autonomous agents with supervision and review, while saying pure vibe '
        'coding was still aspirational for his professional work. ' + JAN_SOURCE + '. '
        'ClassPoint creates an activity ID when this activity runs. The AFTER poll is '
        'a separate slide activity; never reuse a recorded activity ID. Use a show of '
        'hands if the add-in is unavailable. Keep first results hidden until the second vote.')
    add_poll(before)

    news = cards('CATCH-UP · SEPTEMBER 2026', 'Models improve. Agents get more tools.', [
        ('22 SEP · ANTHROPIC', 'Claude Opus 5.5', [
            'Terminal-Bench 4.0\n**66.4%** vs **52.3%** for Opus 5.',
            'About **40% lower cost**\non typical token-billed work.',
            f'[Release + evaluation]({OPUS_SOURCE})',
        ]),
        ('29 SEP · OPENAI', 'GPT-6.1 Sol', [
            'OSWorld 2.0: **+7 points**\nvs GPT-6 Sol at maximum effort.',
            '**Less than half the cost**\nper task at that setting.',
            f'[Release + evaluation]({SOL_SOURCE})',
        ]),
        ('29 SEP · OPENAI', 'dots', [
            'Always-on agent with a\ncloud computer and apps.',
            'People set permissions and\nreview consequential work.',
            f'[Product introduction]({DOTS_SOURCE})',
        ]),
    ], text_size=28, head_size=39)
    # Leave room for a plainly visible evidence/chronology caveat.
    for el in news.els:
        if el.kind == 'text' and el.y == 588:
            el.h = 296
    news.els.append(T(120, 915, 1680, 88,
        'Different tests and settings; vendor reports, not a head-to-head class test.\n'
        'The two 29 September releases came after the keynote.',
        'body', 25, MUTED, lh=1.3))
    news.notes = (
        'Checked 7 October 2026. These are separate reports, not an apples-to-apples '
        'ranking or proof of a cause for DHH changing his view. Anthropic: ' + OPUS_SOURCE + '. '
        'Terminal-Bench 4.0 uses xhigh effort for Opus 5.5; the reported standard error '
        'is ±2.6 points. Claude benchmarks generally include production safeguards and '
        'specified fallback models. The 40% figure is a typical-workload cost estimate, '
        'not a uniform API token-price reduction. Anthropic describes Opus 5.5 as '
        'performing at the level of Fable 5.1 on most work. OpenAI: ' + SOL_SOURCE + '. '
        'The OSWorld 2.0 claim uses the offline set, partial reward, release v2026.08.08, '
        'maximum effort, compared with GPT-6 Sol. It is not the OSWorld 2.1 number in '
        'Anthropic’s release. OpenAI’s release index dates GPT-6.1 Sol to September 29. '
        'dots: ' + DOTS_SOURCE + '. The launch describes GPT-6 Astra-powered agents, '
        'a cloud computer, plugin access and user permissions. This is a product, not '
        'a separate foundation-model benchmark. Do not require a student subscription. '
        'Return to September 23 on the next slide: the September 29 announcements '
        'followed the keynote, so they cannot be presented as its cause.')

    after.els = after.els[:2]
    after.els[1] = T(120, 192, 1680, 140, 'DHH now argues for agent-written code',
                     'xbold', 62, INK, lh=0.95, spc=-0.03)
    after.els += [
        Rect(120, 335, 810, 430, PAPER),
        T(155, 394, 740, 110, 'DHH · Rails World 2026', 'xbold', 46, INK, lh=1.1),
        T(155, 540, 740, 70, 'Official keynote · Rust excerpt', 'body', 30, MUTED),
        T(155, 640, 740, 70, f'[Play 28:14–31:14 · 3 minutes]({VIDEO_START})',
          'semibold', 32, TEAL, lh=1.2),
        T(1000, 350, 800, 200,
          'He argues that coding agents change which languages and systems '
          'his team can build with.', 'body', 39, INK, lh=1.25),
        T(1000, 580, 800, 155,
          'Watch his Rust example. Which parts are evidence, and which are predictions?',
          'body', 34, INK, lh=1.3),
    ]
    after.html_only.append(Embed(120, 335, 810, 430, VIDEO_ID,
                                 thumb='week05-keynote-poster.png',
                                 name='dhh-rust-excerpt'))
    # Keep the timed fallback visible outside the player on the web as well as in PPTX.
    after.els.append(T(1000, 742, 800, 36,
        f'[Start at 28:14; stop at 31:14]({VIDEO_START})', 'body', 25, TEAL, lh=1.2))
    after.notes = (
        'Play the official Rails Foundation edited keynote, 28:14 to 31:14, then stop. '
        'The iframe is the full official video; use the timestamped link to start at '
        '28:14 if necessary. It does not automatically stop: stop at 31:14. PPTX/PDF '
        'show a labelled playback card and link; no video file is downloaded or redistributed. '
        'Do not use the livestream timestamps: they differ from this edited upload. '
        'Video: https://www.youtube.com/watch?v=' + VIDEO_ID + '. '
        'Event date and location: https://rubyonrails.org/world/2026/ (Austin, September '
        '23–24; opening keynote September 23). His October 6 recap says he called for '
        'putting down the pencils at Rails World: ' + OCT_SOURCE + '. '
        'Treat his economic and productivity claims as his argument, not settled fact '
        'or a measured result from this class. Take the AFTER vote with exactly the '
        'same prompt and choices. Reveal the two distributions after everyone votes; '
        'ask what changed a mind or what evidence would be needed. No preferred answer. '
        'Then bridge to the lesson: read a small representation, predict a change, and '
        'check the result. Understanding, delegation and verification can be discussed '
        'separately. Preflight YouTube access and sound on the teaching machine.')
    add_poll(after)
    return [before, news, after]
