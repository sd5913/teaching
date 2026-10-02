"""SD5913 Week 5: images and video, from pixel values to model outputs."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import week05_figures as F
from deckgen import attach_reports
from deckgen.layouts import (agenda, cards, content, end, figure_slide,
                             question, section, statement, timeline, two_col, title)

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
S.append(agenda(EYE, [
    'Read an image as numbers with named axes',
    'Build a small image and a field of noise in code',
    'Add time: video is ordered frames, not one magic object',
    'Compare GANs, VAEs and diffusion without a progress ladder',
    'Use a generation API, then sketch one project interaction',
]))
S.append(question('multiple_choice', 'What crosses an image-generation API?',
                  choices=['A finished chart', 'A request in; image data out',
                           'A mouse click only', 'A video camera feed'],
                  eyebrow_text='00 · RECALL THE API',
                  notes='B. The client sends a request with a prompt and options; the service '
                  'returns image data and metadata. The client decides how to display or save '
                  'the result. This recalls Week 4 without repeating the API lesson.'))

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
S.append(two_col('01 · A TINY IMAGE', 'Nested lists make the axes visible', [
    'The outer list holds rows. Each row holds pixels. Each pixel holds R, G and B.',
    '',
    'For this 2 x 2 image, the data has 2 rows, 2 columns and 3 channel values per pixel.',
], [
    'pixels = [',
    '    [[255, 0, 0], [0, 255, 0]],',
    '    [[0, 0, 255], [255, 255, 0]],',
    ']',
], notes='No array library is needed to see the structure. Python calls these lists; an '
    'image library can turn the nested values into a displayed image. Say row/column before '
    'saying x/y: image APIs often put height before width in an array shape.'))
S.append(two_col('01 · READ ONE PIXEL', 'Position first, channels second', [
    'pixels[0][1] is the top row, second column: green.',
    'pixels[1][0] is the bottom row, first column: blue.',
    'The final three values describe one colour at that position.',
    '',
    '**Try:** change one position, not the whole image.',
], [
    'print(len(pixels))          # rows: 2',
    'print(len(pixels[0]))       # columns: 2',
    'print(len(pixels[0][0]))    # channels: 3',
    'pixels[0][1] = [255, 255, 255]  # make it white',
], notes='The assignment changes the three channel values at one coordinate. Ask students '
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

# 02 · Generate values before asking a learned model for them.
S.append(section('02', 'Make an image in code', 'Choose a rule, then inspect the marks it produces'))
S.append(two_col('02 · RANDOM PIXELS', 'Noise is a starting material', [
    'Each pixel gets one random grey value.',
    'A loop applies the same rule to every position.',
    'The result is unpredictable in detail, but the range and dimensions are chosen.',
    '',
    '**Task:** display the nested list with the week 3 plotting tools.',
], [
    'import random',
    'import matplotlib.pyplot as plt',
    'pixels = []',
    'for y in range(64):',
    '    row = []',
    '    for x in range(64):',
    '        grey = random.randint(0, 255)',
    '        row.append([grey, grey, grey])',
    '    pixels.append(row)',
    'plt.imshow(pixels, interpolation="nearest")',
    'plt.show()',
], notes='After making the list, pass it to matplotlib.pyplot.imshow to see the image. '
   'Explain that random noise is an algorithmic '
   'image: the person chose the dimensions, range, colour rule and random process. It is not a '
   'learned image model. Seed random only if demonstrating repeatable output.'))
S.append(cards('02 · FROM NOISE TO FORM', 'An image is a field we can transform', [
    ('sample', 'Choose values', 'Random numbers, a formula, or measured data.'),
    ('map', 'Apply a rule', 'Use position, neighbours, or time to change each value.'),
    ('inspect', 'Judge the result', 'Look for a pattern and ask what the rule made visible.'),
], notes='This is the bridge from the week 3 idea that a chart is a transformation to image '
    'generation. The same pixels can be redrawn, recoloured or moved; none of those operations '
    'requires a learned model.'))

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
    'Playback speed and the order of frames shape the motion we perceive.',
], [
    'frame 0 -> time 0',
    'frame 1 -> time 1 / fps',
    'frame 2 -> time 2 / fps',
    '',
    'same frame data + new order = different motion',
], notes='Keep the distinction between the raw-frame mental model and a compressed video '
    'file. A webcam feed, a sequence of hand-drawn frames and a model-generated clip are '
    'different ways to obtain frames; they are not the same technique.'))

# 04 · A compact map of learned image-generation ideas.
S.append(section('04', 'Learned image models', 'Different training ideas, different jobs'))
S.append(cards('04 · THREE FAMILIES', 'GAN, VAE, diffusion', [
    ('GAN', 'Generator + discriminator', 'A generator proposes images; a discriminator learns to distinguish generated from training examples.'),
    ('VAE', 'Encoder + decoder', 'An encoder maps an image into a compact latent representation; a decoder reconstructs from it.'),
    ('Diffusion', 'Learn to denoise', 'A model learns to reverse a noise process over many steps, guided by conditioning such as text.'),
], notes='These are conceptual sketches, not a ranking. GANs use an adversarial training '
    'game. VAEs learn an encoder/decoder and a structured latent space. Diffusion models train '
    'a denoising process; implementations and objectives vary. A VAE is a representation and '
    'decoder component in some pipelines, not a synonym for diffusion. Adapt the accessible '
    'Week 5 model diagrams from the SD2112 teaching materials; do not transplant its examples '
    'or claim every modern model follows one exact recipe. Source: '
    'https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py.'))
S.append(figure_slide('04 · GAN · ADVERSARIAL TRAINING',
                      'One learns to make. One learns to catch.', F.gan_adversaries(),
                      notes='Walk from random latent input to generator to candidate image; the '
                      'discriminator also sees real training examples and supplies a learning '
                      'signal. This is a simplified schematic, not a literal network graph or '
                      'a claim that every GAN is unconditional. Adapted from the 2025 SD2112 Week '
                      '5 generator/discriminator diagram and sample grids, PDF pp. 45-46. Source '
                      'deck notes: https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py.'))
S.append(figure_slide('04 · VAE · ENCODER AND DECODER',
                      'Compress the image, then reconstruct it.', F.vae_path(),
                      notes='The latent is a compact learned representation; a VAE decoder maps '
                      'it back to image values. A variational encoder models a distribution, but '
                      'this teaching sketch omits its mean, variance and sampling details. A VAE '
                      'can support generation from a sampled latent, but it is not the same process '
                      'as latent diffusion. Adapted from the 2025 SD2112 Week 5 VAE diagram, PDF '
                      'p. 53. Source deck notes: '
                      'https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py.'))
S.append(figure_slide('04 · ONE LATENT-DIFFUSION PATH',
                      'From prompt and noise to pixels', F.latent_diffusion(),
                      notes='A common latent diffusion pipeline: an encoder represents the prompt; '
                      'a denoiser iteratively refines a noisy latent under that conditioning; a VAE '
                      'decoder maps the final latent back to pixels. Not all diffusion models use '
                      'the same architecture, latent space or training objective.'))
S.append(statement('CLIP aligns representations. It does not generate the image.',
                   eyebrow_text='04 · DO NOT CONFUSE THE COMPONENTS', size=64,
                   notes='CLIP learns a shared embedding space for text and images, useful for '
                   'matching or ranking them. A text-to-image pipeline may use a text encoder or '
                   'other conditioning component, but CLIP by itself is not the image generator. '
                   'This distinction is a carry-over from the SD2112 theory sequence and its '
                   'caption/image pairing diagrams (2025 PDF pp. 48-50): '
                   'https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py.'))
S.append(cards('04 · WHERE DOES IT RUN?', 'A model has a size and a cost', [
    ('download', 'Weights on disk', 'The model files must fit the device or be available to a service.'),
    ('inference', 'Memory and compute', 'Resolution, precision, batch size and pipeline parts also affect memory and speed.'),
    ('service', 'Remote API', 'A service hides local setup; the request, wait, response and access rules still matter.'),
], notes='Model size is not the only runtime cost. A smaller checkpoint may still need more '
    'memory at a larger resolution; hosted APIs move computation elsewhere but do not make it '
    'free or instantaneous. Avoid promising a particular local speed before preflighting the '
    'classroom hardware.'))

# 05 · Turn the Week 4 request/response idea into an image exercise.
S.append(section('05', 'Generate and inspect', 'A prompt is an input; the image is a response'))
S.append(content('05 · THE API LOOP', 'The service returns media, not meaning', [
    'The client sends a prompt and model options to the image service.',
    '',
    'The service returns image data or a reference to it, depending on the endpoint.',
    '',
    'The client waits, fetches if needed, displays the result and lets a person inspect it.',
    '',
    'Try one intentional change at a time: prompt, size, or model. Save the input beside the output.',
], notes='Reuse the Week 4 image API request/response idea. The exact Easel client steps and '
    'available model controls must be preflighted in the installed classroom client; keep keys '
    'out of slides, student code and public repositories. Do not claim an image API returns '
    'a particular binary format unless the selected endpoint shows it.'))
S.append(timeline('05 · GUIDED API EXERCISE', 'Make a small comparison, not a masterpiece', [
    ('01', 'State an intention', 'Choose a simple image idea you can describe in one sentence.'),
    ('02', 'Generate a first result', 'Use the classroom Easel client and note the model and settings shown.'),
    ('03', 'Change one input', 'Revise one part of the request; keep the rest as stable as the client allows.'),
    ('04', 'Compare and annotate', 'What changed? What did the model decide without being asked?'),
], notes='This is a short study, not a polished deliverable or a controlled scientific experiment. '
    'If the client does not expose a seed, do not describe the comparison as controlled. The '
    'instructor demonstrates the API path and supervises the image exercise; use the static '
    'prepared example if the service is unavailable.'))
S.append(content('05 · OPTIONAL INSTRUCTOR DEMO', 'ComfyUI / local model: useful, not required', [
    'If ComfyUI has a local checkpoint ready, compare its setup, latency and output with the API.',
    '',
    'The 2025 Stable Diffusion and LCM scripts are references, not a guarantee that every laptop can run them.',
    '',
    '{muted:If the model is not ready, keep the lesson moving with the API result and a prepared screenshot.}',
], notes='Do not ask students to install PyTorch, download a checkpoint or create API credentials '
    'as a condition of completing the exercise. Rehearse the local pipeline on the actual demo '
    'machine. CPU execution may be slow and half-precision GPU settings do not transfer safely '
    'to every device. The current notebook should explain fallback, not promise a live run.'))

# 06 · A low-stakes bridge toward the interactive experience project.
S.append(section('06', 'From image to interaction', 'Start with what someone can do'))
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
