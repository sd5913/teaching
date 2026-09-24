"""Generate the Week 4 illustration; EASEL_KEY must be set in the environment.

Run from the repo root: python scripts/image_api_example.py
Uses only Python's standard library. Makes one image generation request.
"""
import base64
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

PROMPT = (
    'Editorial paper sculpture of a tidal wave becoming a flowing ribbon, '
    'layered warm ivory paper, deep navy and muted teal with one vivid orange accent. '
    'A small orange sphere floats above the crest. Minimal gallery still life, '
    'tactile cut paper edges, soft studio shadows, warm off-white background. '
    'Confident sculptural composition filling a square frame, generous negative space. '
    'No text, no letters, no charts, no logos. Art school exhibition quality.'
)
PAYLOAD = {'model': 'qwen-image-2.1', 'prompt': PROMPT, 'size': '1024x1024',
           'n': 1, 'response_format': 'b64_json'}


def main():
    request = Request(
        'https://easel.ait4x.org/v1/images/generations',
        data=json.dumps(PAYLOAD).encode(),
        headers={'Authorization': 'Bearer ' + os.environ['EASEL_KEY'],
                 'Content-Type': 'application/json'},
        method='POST',
    )
    with urlopen(request, timeout=600) as response:
        result = json.load(response)
    item = result['data'][0]
    if 'b64_json' in item:
        image = base64.b64decode(item['b64_json'])
    else:
        # A provider may return a download URL instead of encoded image bytes.
        with urlopen(item['url'], timeout=60) as response:
            image = response.read()
    target = Path('deck/assets/week04-image-api-wave.png')
    target.write_bytes(image)
    target.with_suffix('.json').write_text(json.dumps({
        'provider': 'https://easel.ait4x.org/v1',
        'request': PAYLOAD,
        'purpose': 'Generated illustration; not a visualisation of measured tide data.',
    }, indent=2) + '\n')
    print(f'Saved {target} ({len(image)} bytes)')


if __name__ == '__main__':
    main()
