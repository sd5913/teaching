"""SD5913 Week 5: images and video, from pixel values to model outputs."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import week05_figures as F
from week05_examples import (API_EXAMPLE, FRAME_EXAMPLE, NOISE_EXAMPLE,
                             TINY_PIXEL_EXAMPLE)
from deckgen import attach_reports
from deckgen.layouts import (agenda, cards, code_slide, content, end, exercise,
                             figure_slide, live, question, section, statement,
                             timeline, two_col, title)

COURSE = 'SD5913'
SITE = 'sd5913.github.io/teaching'
EYE = 'SD5913 · WEEK 05'
S = []


# 00 · Last week made APIs tangible; today adds an image response.
cover = title(EYE, 'Images & video', 'Pixels, models and interaction.')
cover.notes = ('Move from the Week 4 API example to the data a picture contains, then ask '
               'what changes when time joins the image axes. Keep this as a bridge from '
               'code students can read to models they will inspect, not a product launch.')
S.append(cover)
agenda_slide = agenda(EYE, [
    'Recall values, types, lists and positions',
    'Build a grid, then read it as pixels',
    'Make an image from a rule or random numbers',
    'Add time: video is an ordered sequence of frames',
    'Compare learned image models and trace one generation path',
    'Use an API or local model, then sketch one project interaction',
])
agenda_slide.notes = ('The 2025 Week 5 deck begins with recap, input, APIs and classes before '
                      'its image section (PDF pp. 1-31). This 2026 lesson assumes last week’s '
                      'API work and keeps the agreed image/video sequence. GAN is a brief '
                      'supplemental comparison; LCM and ControlNet are optional code examples, '
                      'not topics in the 2025 slide deck.')
S.append(agenda_slide)
# 00 · Recall the values and structures students already use.
S.append(section('00', 'Start with values', 'Build from Python you already know'))
S.append(content('00 · QUICK RECALL', 'A value has a type', [
    'An **int** counts: 3.',
    'A **float** can measure: 3.5.',
    'A **str** holds text: "blue".',
    'A **bool** is a yes/no value: True or False.',
    '',
    'A **list** keeps several values in order. The type tells Python how to interpret a value.',
    '',
    '[Course Python reference](https://github.com/sd5913/pfad/blob/2026/reference/python.md)',
], notes='Pause before showing the next slide. Ask students to name the type and one operation '
    'that makes sense for each value. Link back to the values and list operations collected in '
    'the course Python reference: '
    'https://github.com/sd5913/pfad/blob/2026/reference/python.md.'))
S.append(two_col('00 · ONE VALUE, THEN A LIST', 'Position gives an ordered value a place', [
    'A number can stand alone. A list gives several numbers an order.',
    '',
    'Python counts list positions from zero.',
    '',
    '**Predict:** what is at position two?',
], [
    'brightness = 160',
    'row = [20, 80, 160, 240]',
    '',
    'print(row[0])  # 20',
    'print(row[2])  # 160',
], notes='Brightness values are integers. The list is a one-dimensional row of sample values; '
    'by itself it has an order but no second spatial axis. This reuses indexing before adding '
    'the second dimension.'))
S.append(two_col('00 · FROM ROW TO GRID', 'A list of rows gives each value a position', [
    'Put rows inside an outer list and a value now has a row and a column.',
    '',
    'The same brightness value can be drawn as a dark or light square.',
    '',
    '**Read it:** gray[1][0] is row 1, column 0.',
], [
    'gray = [',
    '    [20, 80, 160],',
    '    [240, 160, 80],',
    ']',
    '',
    'print(gray[1][0])  # 240',
], notes='Introduce the outer list as rows and each inner list as columns. The values remain '
    'ordinary integers and lists; the image interpretation comes from agreeing what each '
    'position and value mean. This is the bridge from a one-dimensional Python list to a '
    'two-dimensional grid.'))
S.append(figure_slide('00 · FROM GRID TO VISIBLE VALUES',
                      'A display maps each number to a shade.', F.grayscale_grid(),
                      notes='First treat the diagram as a grayscale value grid: each position '
                      'has one brightness value and a display maps lower values to darker marks. '
                      'Then reveal that a colour pixel can hold several channel values. The image '
                      'does not contain painted squares; this is a useful discrete model of '
                      'sampled light.'))
S.append(exercise('00 · BROWSER PYTHON', 'A value becomes a shade', [
    'Open the HTML slides on your laptop. Press Run: the Python prints an SVG image.',
    '',
    'The shades are reversed. Change one expression so 0 is black and 255 is white.',
    '{muted:Predict which square changes before you run it again. No install needed.}',
], code='grid = [[0, 128, 255], [255, 64, 0]]\n'
        'print(\'<svg viewBox="0 0 3 2" width="600">\')\n'
        'for y, row in enumerate(grid):\n'
        '    for x, value in enumerate(row):\n'
        '        shade = 255 - value\n'
        '        fill = f"rgb({shade},{shade},{shade})"\n'
        '        print(f\'<rect x="{x}" y="{y}" \'\n'
        '              f\'width="1" height="1" fill="{fill}"/>\')\n'
        'print("</svg>")',
   check='from xml.etree import ElementTree as ET\n'
         'rects = list(ET.fromstring(_out))\n'
         'ok = len(rects) == 6 and [r.get("fill") for r in rects] == [\n'
         '    "rgb(0,0,0)", "rgb(128,128,128)", "rgb(255,255,255)",\n'
         '    "rgb(255,255,255)", "rgb(64,64,64)", "rgb(0,0,0)"]',
   eid='a-value-becomes-a-shade',
   hint='change 255 - value · ctrl+enter runs it',
   notes='This is the same Pyodide Python exercise layout as Weeks 2 and 3. The console '
         'renders printed SVG; it is not Pillow, a file download, or an external API. '
         'First run downloads Python into the browser. Ask for a prediction before '
         'correcting the inversion. Changing one input value updates one visible square.'))
S.append(two_col('00 · ONE PIXEL, THREE VALUES', 'A colour pixel groups its channels', [
    'One grayscale pixel stores one brightness value.',
    '',
    'An RGB pixel stores three channel values: red, green and blue.',
    '',
    'A grid of RGB pixels has row, column and channel positions.',
], [
    'gray_pixel = 160',
    'rgb_pixel = [30, 90, 240]',
    '',
    '# red, green, blue',
], notes='Name each axis before introducing a library: rows, columns, channels. For this RGB '
    'example, the channel order is explicitly red, green, blue. Some libraries or formats use '
    'another order; read the representation rather than assuming.'))
S.append(statement('Numbers describe the picture. A renderer makes them visible.',
                   eyebrow_text='00 · DATA → DISPLAY', size=72,
                   notes='Separate the stored values from the rendering step. Python holds '
                   'numbers; Pillow, a browser, a notebook or a display interprets them and '
                   'produces visible light. The next slides name the dimensions and conventions '
                   'that make that interpretation unambiguous.'))

# 01 · What a digital image looks like to a program.
S.append(section('01', 'Pixels are values', 'A display turns an ordered set of numbers into a picture'))
S.append(statement('A picture to us. A grid of values to a program.',
                   eyebrow_text='01 · TWO WAYS TO SEE IT', size=78,
                   notes='Ask what a computer can address: a location and a value. The image '
                   'does not contain little painted squares; this grid is a useful discrete '
                   'model of sampled colour. The display turns those values into light.'))
S.append(figure_slide('01 · SPATIAL AXES + COLOUR CHANNELS',
                      'One position. Three channel values.', F.pixel_grid(),
                      notes='The diagram uses row then column: pixel[y][x]. Many array libraries '
                      'describe an RGB image as (height, width, channels). Some APIs and libraries '
                      'use another channel order, so name the convention you are reading. The '
                      'highlighted pixel is [30, 90, 240] in RGB: little red, some green, more blue.'))
S.append(two_col('01 · A TINY IMAGE', 'A small list becomes visible pixels', [
    'Each row holds pixels; each pixel has red, green and blue values.',
    '',
    'Run the complete script to enlarge a 2 x 2 image and save tiny-image.png.',
    '',
    'Run: uv run --with pillow python tiny_image.py',
], TINY_PIXEL_EXAMPLE.splitlines(), notes='No array library is needed to see the structure. '
    'This complete example uses Pillow to render four RGB tuples as a visible image. Python '
    'calls these lists; an image library turns the nested values into a displayed image. Say '
    'row/column before saying x/y: image APIs often put height before width in an array shape.'))
S.append(two_col('01 · READ ONE PIXEL', 'Position first, channels second', [
    'pixels[0][1] is the top row, second column: green.',
    'pixels[1][0] is the bottom row, first column: blue.',
    'The final three values describe one colour at that position.',
    '',
    '**Try:** change one position, not the whole image.',
], [
    'pixels = [',
    '    [(255, 0, 0), (0, 255, 0)],',
    '    [(0, 0, 255), (255, 255, 0)],',
    ']',
    '',
    'print(len(pixels))          # rows: 2',
    'print(len(pixels[0]))       # columns: 2',
    'print(len(pixels[0][0]))    # channels: 3',
    'pixels[0][1] = [255, 255, 255]  # make it white',
], notes='The complete Pillow example above now keeps rows nested and flattens them '
   'only at putdata. This is the same pixels variable: look up a row and column '
   'before flattening. The assignment changes one pixel; ask students '
   'to predict which visible square changes before describing a plotting helper. A row/column '
   'mistake is a common reason a transformation appears rotated or flipped.'))
S.append(content('01 · HOW MUCH DATA?', 'Dimensions and representation matter', [
    'A 512 x 512 RGB image with one 8-bit value per channel contains 512 x 512 x 3 bytes.',
    '',
    'That is **786,432 bytes** (768 KiB) before file headers or compression.',
    '',
    'Grayscale can use one value per pixel. RGBA adds an alpha channel for transparency. '
    'Floating-point models may use different value ranges and more bytes.',
], notes='The byte count assumes uncompressed 8-bit channels. A PNG/JPEG file is encoded and '
    'will usually have a different size. Dimensions, channels, bit depth, and compression are '
    'different properties; do not call them all image resolution.'))
S.append(two_col('01 · NUMPY + PILLOW + OPENCV', 'Each library sees the same pixels differently', [
    'Array shape is (H, W, C); Pillow size is (W, H).',
    'Pillow modes include RGB, L and RGBA. OpenCV transforms images/video; camera frames may be BGR.',
    '[2025 Week 5 notebook](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)',
], [
    'import numpy as np',
    'from PIL import Image',
    'pixels = np.zeros((100, 100, 3), dtype=np.uint8)',
    'pixels[:50, :50] = [255, 0, 0]',
    'image = Image.fromarray(pixels)',
    'gray = image.convert("L")',
    'print(pixels.shape, pixels.dtype)',
    'print(image.size, image.mode, gray.mode)',
], notes='Adapted from cells 2-6 of the SD5913 2025 Week 5 notebook. It constructs a 100 by '
    '100 RGB array in (height, width, channels) order, then uses Pillow to interpret and '
    'convert it. The 2025 Week 5 PDF p. 37 lists NumPy, PIL and OpenCV; this small code '
    'example needs only NumPy and Pillow. OpenCV is included here as a related tool, not a '
    'student installation requirement. The active 2026 pfad branch has no Week 5 examples yet; '
    'the link intentionally points to the frozen 2025 branch.'))

# 02 · Generate values before asking a learned model for them.
S.append(section('02', 'Make an image in code', 'Choose a rule, then inspect the marks it produces'))
S.append(two_col('02 · RANDOM PIXELS', 'Noise is a starting material', [
    'Each pixel gets three chosen values, from 0 through 255.',
    '**Try:** change one dimension and predict what changes.',
    'Run: uv run --with pillow python noise.py',
    '[2025 source: 1_random_image.py](https://github.com/sd5913/pfad/blob/2025/week05/1_random_image.py)',
], NOISE_EXAMPLE.splitlines(), notes='This complete 2026 example uses Python’s seeded random '
   'generator and Pillow; no array library is needed. The output is an RGB image with three '
   '8-bit channels. The 2025 source uses NumPy and a high bound of 256, which is exclusive, '
   'so generated values are 0 through 255. Run a downloaded archive example with uv run '
   '--with numpy --with pillow 1_random_image.py; its larger requirements also include model '
   'and webcam packages.'))
S.append(cards('02 · FROM NOISE TO FORM', 'An image is a field we can transform', [
    ('sample', 'Choose values', 'Random numbers, a formula, or measured data.'),
    ('map', 'Apply a rule', 'Use position, neighbours, or time to change each value.'),
    ('inspect', 'Judge the result', 'Look for a pattern and ask what the rule made visible.'),
], notes='This is the bridge from the week 3 idea that a chart is a transformation to image '
    'generation. The same pixels can be redrawn, recoloured or moved; none of those operations '
    'requires a learned model.'))
S.append(exercise('02 · BROWSER PYTHON', 'Change the rule, change the image', [
    'This program draws 144 RGB pixels. Both colours currently follow the column.',
    '',
    'Make blue depend on the row instead: top-right blue, bottom-left red.',
    '{muted:Then try a diagonal or make the boundary move. The pixels are the output.}',
], code='print(\'<svg viewBox="0 0 12 12" width="430">\')\n'
        'for y in range(12):\n'
        '    for x in range(12):\n'
        '        red = 255 if x < 6 else 0\n'
        '        blue = 255 if x < 6 else 0\n'
        '        fill = f"rgb({red},0,{blue})"\n'
        '        print(f\'<rect x="{x}" y="{y}" \'\n'
        '              f\'width="1" height="1" fill="{fill}"/>\')\n'
        'print("</svg>")',
   check='from xml.etree import ElementTree as ET\n'
         'fills = [r.get("fill") for r in ET.fromstring(_out)]\n'
         'ok = len(fills) == 144 and fills[0] == "rgb(255,0,255)" and '
         'fills[6] == "rgb(0,0,255)" and fills[72] == "rgb(255,0,0)"',
   eid='change-the-rule-change-the-image',
   hint='blue needs y · ctrl+enter runs it',
   notes='Use the same x and y axes as the numeric grid; the colour rule is a '
         'transformation, not a learned image generator. This result can be compared '
         'with the local Pillow random-noise script immediately before it.'))
S.append(content('02 · FROM THE INTRODUCTIONS', 'Two marks, two source images', [
    'These came from the student mark collection: a pixel yarn-ball and a stepped '
    'arrow with a separate underscore.',
    '',
    'What survives when either image has fewer pixels, or becomes characters instead?',
    '',
    '{muted:Source marks, not final A/B branding. The icon choice is still being refined.}',
], images=['week05-mark18-display-crop.png', 'mark-38.jpeg'], body_size=29,
   notes='Left: a display-only crop of Mark 18, yarn-ball and tail; the untouched '
         'source is deck/assets/mark-18.png. Right: Mark 38, diagonal stepped arrow and '
         'separate underscore. Both are already in the public teaching asset collection. '
         'Do not attribute names or say either mark is the chosen course identity. '
         'The later treatments are exploratory; Gio will supply two final images.'))

ASCII_FRAMES = json.loads((Path(__file__).parent / 'week05_ascii_frames.json').read_text())['frames']
ASCII_CODE = '''from ascii_magic import AsciiArt

image = AsciiArt.from_image("out/source-crop.png")
chars = "@%#*+=-:. "
for n in range(12, 67, 6):
    print(image.to_ascii(columns=n, char=chars,
                         width_ratio=1.5))'''
ASCII_JS = '''let columns, playing = true, direction = 1;

function setup() {
  createCanvas(640, 560);
  columns = createSlider(12, 66, 36, 6, 'columns');
  columns.elt.addEventListener('input', e => {
    if (e.isTrusted) playing = false;
  });
  playing = !matchMedia('(prefers-reduced-motion: reduce)').matches;
  frameRate(6);
}

function draw() {
  if (playing && frameCount % 3 === 0) {
    let next = columns.value() + direction * 6;
    if (next > 66 || next < 12) {
      direction *= -1;
      next = columns.value() + direction * 6;
    }
    columns.value(next);
    columns.elt.dispatchEvent(new Event('input'));
  }
  let frame = ASCII_FRAMES.find(f => f.columns === columns.value());
  let rows = frame.text.split('\\n');
  let ink = rows.filter(row => row.trim());
  let left = Math.min(...ink.map(row => row.search(/\\S/)));
  let right = Math.max(...ink.map(row => row.trimEnd().length));
  rows = rows.slice(rows.findIndex(row => row.trim()),
                    rows.findLastIndex(row => row.trim()) + 1)
             .map(row => row.slice(left, right));
  textFont('monospace');
  textSize(100);
  let ratio = textWidth('M') / 100;
  let size = min(54, 590 / ((right - left) * ratio), 435 / (rows.length * 1.25));
  background('#FAF8F4');
  fill('#000B1C');
  textSize(21);
  text(frame.columns + ' columns / ' + rows.length + ' active rows', 24, 36);
  textSize(size);
  let lineHeight = size * 1.25;
  let x = (640 - (right - left) * textWidth('M')) / 2;
  let y0 = 86 + (390 - rows.length * lineHeight) / 2 + size;
  for (let y = 0; y < rows.length; y++) text(rows[y], x, y0 + y * lineHeight);
  textSize(18);
  text('click to pause / play', 24, 542);
}

function mousePressed() { playing = !playing; }
function keyPressed() { if (key === 'p') playing = !playing; }'''
# Frame data is computed by the linked Python tutorial; the sketch only selects frames.
ASCII_EXTRA = 'const ASCII_FRAMES = ' + json.dumps(ASCII_FRAMES, ensure_ascii=True).replace('</', '<\\/') + ';'
S.append(code_slide('02 · ASCII-MAGIC · ONE SOURCE', 'One mark, several text widths',
    ASCII_CODE, sketch=live('logo-ascii-resolution', ASCII_JS, 640, 560,
                            hint='slider chooses text width · click to pause/play',
                            extra=ASCII_EXTRA), edit=False, lang='py',
    caption='[Full Python script](https://github.com/sd5913/pfad/blob/draft/week05-logo-ascii/week05/logo_ascii.py) · uv run logo_ascii.py',
    notes='The Python snippet runs locally, after the full student tutorial script has '
          'written out/source-crop.png. The tutorial uses ascii-magic to make ten '
          'ASCII text frames and a GIF; the browser p5.js sketch selects the precomputed '
          'text frames with a slider or plays them back. It does not execute ascii-magic '
          'inside the browser. Narrow columns discard shape information; more columns '
          'do not recreate detail absent from the source. The animation is a changing '
          'representation, not generated video. Ten sizes use a fixed width ratio. Source: '
          'https://github.com/sd5913/pfad/blob/draft/week05-logo-ascii/week05/logo_ascii.py.'))

# 03 · Video adds a temporal index to the frame.
S.append(section('03', 'Add time', 'A video can be inspected as frames in an order'))
S.append(figure_slide('03 · THREE FRAMES', 'The same object, a different position',
                      F.frame_sequence(),
                      notes='These are three drawn frames, not generated video. At a fixed frame '
                      'rate, the frame index maps to time. Raw uncompressed frames can be described '
                      'with axes (frames, height, width, channels); actual video files use codecs '
                      'and often store changes between frames instead of this literal array.'))
S.append(two_col('03 · IMAGE VS VIDEO', 'Time is another axis of change', [
    '**One RGB image:** height x width x channels.',
    '',
    '**A raw frame sequence:** frames x height x width x channels.',
    '',
    'Playback speed and frame order shape the motion we perceive.',
    '',
    'A simple animation is a list of still images in order.',
], [
    'frame 0 -> time 0',
    'frame 1 -> time 0.2 s',
    'frame 2 -> time 0.4 s',
    '',
    'same frames + new order = different motion',
], notes='Keep the distinction between the raw-frame mental model and a compressed video '
    'file. A saved animation has an explicit frame order and duration; webcam processing is a '
    'separate live-input example and is not used here.'))
S.append(two_col('03 · A RUNNABLE EXAMPLE', 'Make three frames; save a short animation', [
    'Each loop makes one complete still image.',
    '',
    'The dot moves to a new position in each frame.',
    '',
    'Pillow saves the ordered frames as moving-dot.gif.',
    '',
    'Run: uv run --with pillow python make_gif.py',
], FRAME_EXAMPLE.splitlines(), notes='This complete 2026 example uses Pillow to create three '
    'still frames and save them in order as a looping GIF. The GIF plays each frame for the '
    'same duration; no webcam or video-processing library is needed.',
    right_size=20))
FRAME_JS = '''let positions = [80, 280, 480];

function setup() {
  createCanvas(640, 360);
  frameRate(5);
}

function draw() {
  background('#FAF8F4');
  let index = (frameCount - 1) % positions.length;
  let x = positions[index];
  noStroke();
  fill('#ED6D24');
  circle(x, 180, 90);
  fill('#000B1C');
  textSize(26);
  text('frame ' + index, 24, 40);
}'''
S.append(code_slide('03 · EDIT THE FRAMES', 'Change one position; watch the motion',
                    FRAME_JS, figure=F.frame_preview(), code_size=22,
                    sketch=live('moving-pixels', FRAME_JS, 640, 360,
                                hint='edit positions or frameRate · Run to replay'),
                    notes='This editable p5.js sketch is live in HTML as in Week 3; the '
                          'Python/Pillow slide before it exports the three still frames as '
                          'a GIF locally. JavaScript in the browser drives this preview; '
                          'the two programs implement the same frame-index idea, not '
                          'identical files. Change 280 to 400 or frameRate to 2, rerun '
                          'and name what changed. The still diagram is the PDF/PPTX fallback.'))

# 04 · A compact map of learned image-generation ideas.
S.append(section('04', 'Learned image models', 'Different training ideas, different jobs'))
S.append(cards('04 · THREE FAMILIES', 'GAN, VAE, diffusion', [
    ('GAN', 'Generator + discriminator', 'A generator proposes images; a discriminator learns to distinguish generated from training examples.'),
    ('VAE', 'Encoder + decoder', 'An encoder maps an image into a compact latent representation; a decoder reconstructs from it.'),
    ('Diffusion', 'Learn to denoise', 'A model learns to reverse a noise process over many steps, guided by conditioning such as text.'),
], notes='These are conceptual sketches, not a ranking. GANs use an adversarial training '
    'game. VAEs learn an encoder/decoder and a structured latent space. Diffusion models train '
    'a denoising process; implementations and objectives vary. A VAE is a representation and '
    'decoder component in some pipelines, not a synonym for diffusion. The 2025 SD5913 Week 5 '
    'PDF focuses on diffusion, CLIP, U-Net and VAE (pp. 38-44), not GANs. Keep GAN as a short '
    'supplemental comparison rather than the spine of this lesson. Do not transplant SD2112 '
    'project examples or claim every modern model follows one exact recipe. Supplemental '
    'concept source: '
    'https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py.'))
S.append(figure_slide('04 · CLIP · IMAGE/TEXT ALIGNMENT',
                      'Compare representations; do not generate an image.', F.clip_alignment(),
                      notes='The 2025 Week 5 PDF p. 39 says CLIP can generate descriptions and '
                      'visual representations, which is misleading. The p. 40 diagram shows '
                      'separate text/image encoders and a similarity matrix. Teach CLIP as an '
                      'alignment model for comparing or ranking pairs, not as a captioner or '
                      'image generator. Code reference: '
                      'https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb.',
                      caption='Code: [week05_notebook.ipynb](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)'))
S.append(content('04 · TWO USES OF TEXT', 'A similarity score is not a drawing instruction', [
    '**CLIP:** its text and image encoders compare a caption with an existing image.',
    '',
    '**Text-conditioned generation:** a prompt becomes features that guide repeated '
    'changes to a noisy latent. The CLIP image encoder does not draw the image.',
    '',
    'Which words name an object? Which constrain material, composition or what must be absent?',
    '',
    '{muted:The particular text encoder and denoising architecture depend on the model.}',
], notes='Do not equate CLIP’s two-encoder similarity task with the generative pipeline '
    'or imply the prompt determines every pixel. Classic Stable Diffusion pipelines '
    'may use a CLIP-family text encoder for conditioning; newer pipelines differ.'))
S.append(figure_slide('04 · U-NET · TRAINING AND GENERATION',
                      'Learn to remove noise; then use that skill.', F.diffusion_training(),
                      notes='Based on the 2025 Week 5 PDF pp. 41-42. The archived p. 41 slide is '
                      'titled “U-Net Training” but depicts both forward noising and reverse '
                      'sampling. This original diagram shows latent diffusion: encode each '
                      'training image to z0 before adding noise; the U-Net learns to predict '
                      'that known sampled noise, then uses its error to update denoiser '
                      'weights. Generation starts at zT with weights fixed, applies the denoiser '
                      'repeatedly, then decodes the clean latent to pixels. It is a simplified '
                      'noise-prediction example; not every current model uses this exact '
                      'objective. The p. 42 U-Net image '
                      'is an architecture sketch; it omits conditioning details.',
                      caption='Code: [week05_notebook.ipynb](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)'))
S.append(figure_slide('04 · VAE · ENCODER AND DECODER',
                      'Learn a latent distribution; sample and reconstruct.', F.vae_path(),
                      notes='The latent is a compact learned representation; a VAE decoder maps '
                      'it back to image values. The encoder estimates a distribution, '
                      'represented by mean and variance; sampling produces a latent. '
                      'Reconstruction is approximate. A VAE '
                      'can support generation from a sampled latent, but it is not the same process '
                      'as latent diffusion. This diagram follows the image -> encoder -> latent -> '
                      'decoder -> reconstruction sequence in the SD5913 2025 Week 5 PDF p. 43. '
                      'Notebook reference: '
                      'https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb.',
                      caption='Code: [week05_notebook.ipynb](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)'))
S.append(figure_slide('04 · ONE LATENT-DIFFUSION PATH',
                      'From prompt and noise to pixels', F.latent_diffusion(),
                      notes='A common latent diffusion pipeline: an encoder represents the prompt; '
                      'a U-Net denoiser iteratively refines a noisy latent under that conditioning; '
                      'a VAE decoder maps the final latent back to pixels. This diagram follows the '
                      'SD1.5 pipeline in the SD5913 2025 Week 5 PDF p. 44. The source diagram uses '
                      'a 64 x 64 latent and a 50-step loop as an illustration; this deck leaves '
                      'those values generic. Not all diffusion models use the same architecture, '
                      'latent space or objective. Code reference: '
                      'https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb.',
                      caption='Code: [week05_notebook.ipynb](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)'))
S.append(content('04 · MODEL BOUNDARY', 'One diagram, not every image model', [
    'This diagram explains one **classic latent-diffusion** path: text features '
    'condition a denoiser; a VAE decoder turns the final latent into pixels.',
    '',
    'The training objective, denoiser and text encoder vary across model families. '
    'Some current systems use transformer denoisers or flow matching instead.',
    '',
    '**Ask of a service:** which model made the image? Which controls does it expose? '
    'Which parts of our diagram are only assumptions?',
], notes='A hosted API is an interface, not a statement about its model internals. '
    'Check the classroom model selection before describing it as a U-Net or '
    'noise-prediction implementation. Do not treat the Easel client name as '
    'the underlying media model.'))
S.append(content('04 · OPTIONAL CODE EXTRA · LCM', 'A compatible model can generate in fewer steps', [
    'The 2025 examples contrast Stable Diffusion at 20 inference steps with an LCM pipeline at 4 inference steps.',
    '',
    'LCM uses a model and scheduler designed for few-step sampling; changing the step count alone is not the same thing.',
    '',
    'Fewer steps can reduce wait time. Compare the image too: speed is not a quality guarantee.',
    '',
    '[2025 source: 3_gen_image_lcm.py](https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py)',
], notes='Adapted from the SD5913 2025 2_gen_image.py and 3_gen_image_lcm.py examples. '
    'The standard and LCM examples use different model/scheduler combinations, so their outputs '
    'are not a controlled quality comparison. Explain that few-step sampling depends on a '
    'compatible model and scheduler. This code-repository extra is not in the 2025 Week 5 PDF. '
    'The archived 2_gen_image.py selects CPU when CUDA is unavailable but passes float16 '
    'unconditionally; test the exact device/model before any live demo. Sources: '
    'https://github.com/sd5913/pfad/blob/2025/week05/2_gen_image.py ; '
    'https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py.'))
S.append(figure_slide('04 · OPTIONAL CODE EXTRA · CONTROLNET',
                      'Use an edge map as a structural guide.', F.controlnet_canny(),
                      notes='The 2025 archive demonstrates Canny edge detection as an additional '
                      'ControlNet condition. Canny extracts an edge map from an input image; the '
                      'prompt still describes appearance, while the condition can guide broad '
                      'structure. It does not guarantee a pixel-perfect copy. This is a code '
                      'example, not a topic in the 2025 Week 5 PDF. Keep it as an '
                      'instructor explanation unless the selected Easel or ComfyUI workflow has '
                      'the matching control model preflighted. Source: '
                      'https://github.com/sd5913/pfad/blob/2025/week05/4_controlnet_canny.py.',
                      caption='2025 code: [4_controlnet_canny.py](https://github.com/sd5913/pfad/blob/2025/week05/4_controlnet_canny.py)'))
S.append(cards('04 · WHERE DOES IT RUN?', 'A model has a size and a cost', [
    ('download', 'Weights on disk', 'The 2025 notebook estimates 2–5 GB for its model files; check the selected model.'),
    ('inference', 'Memory and compute', 'Its 4–6 GB VRAM estimate is for 512 x 512 Stable Diffusion, not a guarantee.'),
    ('service', 'Remote API', 'A service hides local setup; the request, wait, response and access rules still matter.'),
], notes='Model size is not the only runtime cost. A smaller checkpoint may still need more '
    'memory at a larger resolution; hosted APIs move computation elsewhere but do not make it '
    'free or instantaneous. The 2025 notebook lists approximate 2–5 GB model files and 4–6 GB '
    'VRAM for its 512 x 512 Stable Diffusion example. Treat those as dated, model-specific '
    'estimates, not current hardware requirements. The archive also discusses CPU fallback, '
    'half precision and smaller resolutions. Source: '
    'https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb.'))
S.append(cards('04 · GENERATION SETTINGS', 'Every control changes the experiment', [
    ('steps', 'Denoising updates', 'The archive compares different step counts; more steps can take longer.'),
    ('guidance', 'Prompt influence', 'Guidance scale affects conditioning; its effect depends on the model.'),
    ('seed', 'Starting randomness', 'A fixed seed can help repeat a run when the other settings also match.'),
    ('resolution', 'Pixel dimensions', 'Larger outputs usually cost more memory and compute.'),
], notes='The 2025 notebook explores inference step counts, guidance scale and seeds. These '
    'are not universal quality sliders, and an API may hide or rename them. Keep the Easel '
    'exercise to one control that the installed client actually exposes. Sources: '
    'https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb ; '
    'https://github.com/sd5913/pfad/blob/2025/week05/2_gen_image.py.'))

# 05 · Turn the Week 4 request/response idea into an image exercise.
S.append(section('05', 'Generate and inspect', 'A prompt is an input; the image is a response'))
S.append(question('multiple_choice', 'What crosses an image-generation API?',
                  choices=['A finished chart', 'A request in; image data out',
                           'A mouse click only', 'A video camera feed'],
                  eyebrow_text='05 · RECALL THE API',
                  notes='B. The client sends a request with a prompt and options; the service '
                  'returns image data and metadata. The client decides how to display or save '
                  'the result. This recalls Week 4 immediately before the generation/API segment.'))
S.append(exercise('05 · BROWSER PYTHON', 'A prompt is part of the request', [
    'This prints request data. It does not send anything or need a key.',
    '',
    'Add a material and a composition constraint to the prompt.',
    '{muted:What would the model still have to decide on its own?}',
], code='import json\n'
        'prompt = "An orange circle"\n'
        'request = {"prompt": prompt, "size": "1024x1024", "n": 1}\n'
        'print(json.dumps(request, indent=2))',
   check=('ok = "paper" in request["prompt"].lower() and '
          '"center" in request["prompt"].lower() and '
          'request["size"] == "1024x1024" and request["n"] == 1'),
   eid='a-prompt-is-part-of-the-request',
   hint='add paper and centered · no network request',
   notes='This safe browser drill reuses Week 4’s request-as-data idea: the output '
         'is only JSON. The following slide is an instructor-controlled API call '
         'with a key from the environment, not a browser-side request. After a '
         'prompt passes, discuss remaining unspecified attributes and latency.'))
S.append(two_col('05 · THE API LOOP', 'The client asks; the service returns media', [
    'This complete example sends one request and saves the image response.',
    '',
    'The key must already be set in EASEL_KEY. Never paste it into source code.',
    '',
    'Run only when the teacher has enabled the API account:',
    'uv run python request_image.py',
    '',
    '[Complete Week 4 example](https://github.com/sd5913/teaching/blob/main/scripts/image_api_example.py)',
], API_EXAMPLE.splitlines(), notes='This complete slide example uses the Python standard library '
    'and reads its key from the EASEL_KEY environment variable. It asks for a base64 image '
    'response and saves api-image.png. The linked Week 4 script is also runnable, handles a '
    'download URL fallback, and writes to the Week 4 demo asset path; do not run it from the '
    'shared repo unless intentionally regenerating that asset. Do not require students to '
    'create credentials. Preflight the exact classroom client and model.',
    right_size=19))
S.append(timeline('05 · GUIDED API EXERCISE', 'Make a small comparison, not a masterpiece', [
    ('01', 'State an invariant', 'Name material, composition and one thing the result must not contain.'),
    ('02', 'Generate a first result', 'Use the classroom Easel client and note the model and settings shown.'),
    ('03', 'Change one input', 'Revise one part of the request; keep the rest as stable as the client allows.'),
    ('04', 'Judge the evidence', 'Did it meet your invariant? What did the model decide unprompted?'),
], notes='This is a short study, not a polished deliverable or a controlled scientific experiment. '
    'If the client does not expose a seed, do not describe the comparison as controlled. The '
    'instructor demonstrates the API path and supervises the image exercise; use the static '
    'prepared example if the service is unavailable.'))
S.append(content('05 · IMAGE EDIT · ASCII → CRT', 'Keep the input; change the scene', [
    '**Left:** the 56-column ASCII image from an earlier, denser conversion of '
    'the pixel yarn-ball. This PNG was the image-edit input.',
    '',
    '**Right:** a draft image edit places an approximation of it on a CRT screen.',
    '',
    '{muted:One image input + one editing instruction; not a text-only generation request.}',
], images=['week05-mark18-ascii-edit-input.png', 'week05-mark18-crt-draft.png'],
   body_size=28, notes='The 56-column input is size 6 from the earlier ten-size '
    'ASCII study. It uses a denser character ramp than the classroom slider; '
    'do not imply the 32-column slide still was used as this edit input. '
    'The provisional CRT result invents glyphs and is not the final A/B choice. '
    'Ask what was preserved and what changed in a service-mediated image edit.'))
S.append(content('05 · IMAGE EDIT · DIGITAL → WOOL', 'Keep the shapes; change the material', [
    '**Left:** the original grid mark has a stepped diagonal arrow and a '
    'separate underscore.',
    '',
    '**Right:** a draft wool edit keeps two pieces, but pushes the arrow '
    'toward a vertical shape. Is that still the same mark?',
    '',
    '{muted:Two experiments, not two approved logos. Final images are pending.}',
], images=['mark-38.jpeg', 'week05-mark38-wool-draft.png'], body_size=28,
   notes='The right is a provisional model edit of Mark 38; the original left '
    'has a diagonal stepped arrow with a distinct underscore. The wool result '
    'alters the silhouette, so students can critique its fidelity. These '
    'source/edit comparisons are teaching experiments, not selected logos.'))
S.append(content('05 · DO THE GLYPHS STILL MATCH?', 'Generated text is not guaranteed text', [
    'Compare the actual 56-column ASCII input with the CRT edit. Are the characters '
    'the same, in the same places?',
    '',
    'A prompt can ask for fidelity; it cannot guarantee spelling or exact alignment. '
    'If a wordmark must be exact, composite the real text layer after generation.',
    '',
    '**Record:** input image, editing instruction, model/settings, result, and one '
    'thing you would keep or reject.',
], notes='These two student-mark experiments link the code-first and generative parts of '
    'the lesson. The CRT edit demonstrates an important limitation of model text '
    'rendering; compare it to the deterministic ASCII file before discussing '
    'quality. A teacher may demonstrate a real image edit only after preflighting '
    'the model and input-image controls; no student keys or paid calls required.'))
S.append(content('05 · OPTIONAL INSTRUCTOR DEMO', 'ComfyUI / local model: useful, not required', [
    'If ComfyUI has a local checkpoint ready, compare its setup, latency and output with the API.',
    '',
    'The 2025 Stable Diffusion, LCM and ControlNet scripts are references, not a guarantee that every laptop can run them.',
    '',
    '{muted:If the model is not ready, keep the lesson moving with the API result and a prepared screenshot.}',
], notes='Do not ask students to install PyTorch, download a checkpoint or create API credentials '
    'as a condition of completing the exercise. Rehearse the local pipeline on the actual demo '
    'machine. CPU execution may be slow and half-precision GPU settings do not transfer safely '
    'to every device. This draft should explain fallback, not promise a live run.'))

# 06 · A low-stakes bridge toward the interactive experience project.
S.append(section('06', 'From image to interaction', 'Start with what someone can do'))
S.append(content('06 · TUTORIAL · MAKE AN ICON', 'Your image, your choice', [
    'Run the logo-to-ASCII script with your own image. Move the resolution slider '
    'and play the generated sequence; where does the mark become recognisable?',
    '',
    'Export a square version and inspect it at avatar size. If you like it, '
    'set your GitHub profile picture yourself; this is optional, not a submission.',
    '',
    '[Week 5 tutorial and runnable Python](https://github.com/sd5913/pfad/tree/draft/week05-logo-ascii/week05)',
], notes='GitHub Settings -> Public profile -> Profile picture -> Upload a photo is '
    'a student-controlled choice; do not alter student profiles or require anyone '
    'to publish a class mark as their own avatar. The draft tutorial points to '
    'the pfad PR branch pending lecturer review; update this link to 2026 '
    'only after the student tutorial merges.'))
S.append(content('06 · PROJECT SEED', 'Name one meaningful interaction', [
    'Who is the person using your project, and what are they trying to do?',
    '',
    'What action or input can they make? What does the program do next?',
    '',
    'What feedback lets them understand the response? Which choice should stay in their control?',
    '',
    '{orange:Bring one rough idea into a three-step storyboard: action -> system response -> feedback.}',
], notes='Give pairs a few quiet minutes, then invite one or two examples. Keep it connected to '
    "each student's project rather than prescribing a single interface or adding a new assignment "
    'requirement. AI image generation is one possible system response, not the definition of '
    "interaction. The assignment's detailed deliverables and due date remain to be confirmed."))
S.append(question('multiple_choice', 'Which is the strongest first interaction to prototype?',
                  choices=['A tool list', 'A user action with a visible response',
                           'A model name', 'A larger image file'],
                  eyebrow_text='06 · EXIT CHECK',
                  notes='B. Ask students to say the interaction in one sentence: “When I ___, '
                  'the interface ___.” This is a quick exit check, not an assessed poll.'))
S.append(end('Make the data visible. Make the response legible.',
             'Images are values; video adds time; interaction gives someone a way in.',
             '[' + SITE + '](https://' + SITE + '/)'))

attach_reports(S, Path(__file__).resolve().parent / 'week05-reports.json')

DECK = {'title': f'{COURSE} · Week 5 — Images & video',
        'pdf': f'{COURSE}-week05.pdf', 'slides': S}
