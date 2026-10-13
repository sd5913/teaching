"""Exact Easel API extension, separated from the offline signal examples."""
from deckgen.layouts import content, code_panel


def api_slides():
    return [
        code_panel('04 · MUSIC API · REQUEST', 'A request describes the intended sound', [
            '{', '  "model": "suno-music",',
            '  "prompt": "Gentle ambient piano, warm strings, slow pulse",',
            '  "title": "Evening", "make_instrumental": true,',
            '  "duration_seconds": 30,', '  "weirdness": 25, "style_influence": 70', '}',
        ], lang='js', caption='Easel extension: POST /v1/audio/generations',
            notes='JSON example, not Python dictionary syntax. These field names come from the current '
            'Easel implementation. The duration field is a requested target, not a verified exact output length. '
            'weirdness and style_influence use 0–100. Exact output, account access and provider controls require '
            'classroom preflight. Do not add n, seed or BPM fields borrowed from an image API. '
            'The implementation and docs provenance is recorded in site/week06/examples/TEACHER_NOTES.md. '
            'https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/AUDIO_API.md'),
        content('04 · MUSIC API · STATUS', 'Submitted is different from ready', [
            'Prepare the JSON request locally.',
            'Submit once and keep the returned attempt identity.',
            'Poll status with a time limit, then follow the returned track IDs.',
            'Save an available track and download its audio bytes.',
        ], notes='The teaching client guards the latest-attempt status with the expected attempt ID. '
            'Once track IDs arrive, per-track polling is the reliable handle. Generation acceptance, '
            'completion and a saved playable file are separate states. The same-origin content endpoint '
            'avoids following arbitrary URLs or forwarding an API key to another host. No automatic retry '
            'of an ambiguous generation POST. Exact route sequence is in site/week06/examples/TEACHER_NOTES.md.'),
        code_panel('04 · MUSIC API · OFFLINE', 'The default is an offline request preview', [
            'python request_song.py \\',
            '  --prompt "Gentle ambient piano, warm strings, slow pulse" \\',
            '  --title "Evening" --instrumental \\',
            '  --duration-seconds 30 --weirdness 25 --style-influence 70',
        ], lang=None, caption='This command prints JSON. It sends nothing and generates no song.',
            notes='Students can inspect and change the request without a key. This is local preview '
            'behavior in our teaching script. Do not confuse it with Easel’s server dry_run flag, '
            'which still contacts the backend and fills a browser form. The complete script requires '
            'an explicit --send before any API request and uses EASEL_BASE_URL and EASEL_API_KEY. '
            'Never put the key in the deck, source file, screen recording or repository.'),
        content('04 · MUSIC API · INSTRUCTOR', 'One generation at a time', [
            'The current backend uses one shared Suno browser.',
            'Its latest-attempt status can change if another request arrives.',
            'The instructor runs any live generation after checking the account.',
            'If it waits, fails or needs a CAPTCHA, pause and use the offline exercise.',
        ], notes='This is a material current integration limit, not a universal limitation of music APIs. '
            'Do not invite a whole class to submit concurrently to one backend. A captured attempt ID '
            'detects replacement; it does not make the backend multi-user safe. A timed-out POST might '
            'already have reached the provider. Do not repeat it automatically or consume credits to debug '
            'the lesson. Live service availability, credits, provider terms and classroom playback remain '
            'unverified. A human handles login and CAPTCHA. Existing generated audio can be a fallback '
            'only when the instructor has an appropriate saved example.'),
        content('04 · MUSIC API · REFLECT', 'Which parts of the brief are precise?', [
            'Compare “30 seconds” with “a gentle sense of arrival”.',
            'Which part can you measure? Which part needs a listener’s judgment?',
            'Change one field in the offline request and explain your prediction.',
            'After generation, what would count as evidence that it worked?',
        ], notes='Spend three minutes editing or annotating a request, without submitting it. '
            'Use original generic descriptions and any lyrics the student has permission to use. '
            'A prompt can request an exact duration without guaranteeing one. Students can check metadata '
            'and listen to the saved result later. No source claims about Suno’s unpublished model internals '
            'or rights to generated work are needed for this lesson.'),
    ]
