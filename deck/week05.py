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
    'An **int** counts: `3`.',
    'A **float** can measure: `3.5`.',
    'A **str** holds text: `"blue"`.',
    'A **bool** is a yes/no value: `True` or `False`.',
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
    'Python counts list positions from `0`.',
    '',
    '**Predict:** what is at position `2`?',
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
    '**Read it:** `gray[1][0]` is row 1, column 0.',
], [
    'gray = [',
    '    [20, 80, 160],',
    '    [240, 160, 80],',
    ']',
    '',
    'gray[1][0]  # 240',
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
    'A 512 x 512 RGB array; each channel is uint8.',
    '`high=256` is exclusive: values run from 0 through 255.',
    '**Try:** change one dimension and predict what changes.',
    '[2025 source: 1_random_image.py](https://github.com/sd5913/pfad/blob/2025/week05/1_random_image.py)',
], [
    'import numpy as np',
    'from PIL import Image',
    'img_dimensions = {',
    '    "low": 0, "high": 256,',
    '    "size": (512, 512, 3),',
    '    "dtype": np.uint8,',
    '}',
    'data = np.random.randint(',
    '    **img_dimensions',
    ')',
    'Image.fromarray(data).show()',
], notes='Adapted from the SD5913 2025 `1_random_image.py` example. `high=256` is exclusive, '
   'so the generated values are 0-255; the array contains (height, width, RGB channels). '
   'Download the linked file and run it with `uv run --with numpy --with pillow 1_random_image.py`; '
   'do not install the full 2025 week05 requirements for this example, as they include Diffusers '
   'and webcam dependencies. `Image.show()` opens the platform image viewer; in a notebook, use '
   '`display(Image.fromarray(data))`.'))
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
                      'and often store changes between frames instead of this literal array. The '
                      '2025 pfad code also has a webcam callback that flips incoming frames; that '
                      'is live input processing, not video generation. If shown, preflight camera '
                      'permissions. Source: '
                      'https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py.'))
S.append(two_col('03 · IMAGE VS VIDEO', 'Time is another axis of change', [
    '**One RGB image:** height x width x channels.',
    '',
    '**A raw frame sequence:** frames x height x width x channels.',
    '',
    'Playback speed and the order of frames shape the motion we perceive.',
    '',
    'A webcam callback transforms incoming frames; it does not synthesize a clip.',
], [
    'frame 0 -> time 0',
    'frame 1 -> time 1 / fps',
    'frame 2 -> time 2 / fps',
    '',
    'same frame data + new order = different motion',
], notes='Keep the distinction between the raw-frame mental model and a compressed video '
    'file. A webcam feed, a sequence of hand-drawn frames and a model-generated clip are '
    'different ways to obtain frames; they are not the same technique.'))
S.append(two_col('03 · LIVE FRAME CALLBACK', 'Transform a frame; return a frame', [
    'This callback runs once for each incoming camera frame.',
    '',
    'The slice reverses the row order. It changes the frame; it does not generate new content.',
    '',
    'Some video APIs use BGR channel order rather than RGB.',
    '',
    '[2025 source: st_video_stream.py](https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py)',
], [
    'import av',
    '',
    'def video_frame_callback(frame):',
    '    img = frame.to_ndarray(',
    '        format="bgr24"',
    '    )',
    '    flipped = img[::-1, :, :]',
    '    return av.VideoFrame.from_ndarray(',
    '        flipped, format="bgr24"',
    '    )',
], notes='This runnable excerpt follows the 2025 source file. To try it from a local copy, '
    'use `uv run --with streamlit --with streamlit-webrtc --with av streamlit run '
    'st_video_stream.py` and preflight camera access. Do not install the complete 2025 week05 '
    'requirements for this small demo. The 2025 course plan lists OpenCV for image/video '
    'processing in Week 6, but the archived Week 6 slide deck is titled “Audio streams” and '
    'does not contain that lesson. This is a 2026 extension grounded in archived code, not a '
    'claim about the Week 6 PDF.'))

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
S.append(figure_slide('04 · U-NET · TRAINING AND GENERATION',
                      'Learn to remove noise; then use that skill.', F.diffusion_training(),
                      notes='Based on the 2025 Week 5 PDF pp. 41-42. The archived p. 41 slide is '
                      'titled “U-Net Training” but depicts both forward noising and reverse '
                      'sampling. This original diagram shows latent diffusion: encode each '
                      'training image to z0 before adding noise; the U-Net learns to predict '
                      'that noise. Generation starts at zT, applies the learned denoiser '
                      'repeatedly, then decodes the clean latent to pixels. It is a simplified '
                      'noise-prediction example; not every current model uses this exact '
                      'objective. The p. 42 U-Net image '
                      'is an architecture sketch; it omits conditioning details.',
                      caption='Code: [week05_notebook.ipynb](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)'))
S.append(figure_slide('04 · VAE · ENCODER AND DECODER',
                      'Compress the image, then reconstruct it.', F.vae_path(),
                      notes='The latent is a compact learned representation; a VAE decoder maps '
                      'it back to image values. A variational encoder models a distribution, but '
                      'this teaching sketch omits its mean, variance and sampling details. A VAE '
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
S.append(content('04 · OPTIONAL CODE EXTRA · LCM', 'A compatible model can generate in fewer steps', [
    'The 2025 examples contrast Stable Diffusion at 20 inference steps with an LCM pipeline at 4 inference steps.',
    '',
    'LCM uses a model and scheduler designed for few-step sampling; changing the step count alone is not the same thing.',
    '',
    'Fewer steps can reduce wait time. Compare the image too: speed is not a quality guarantee.',
    '',
    '[2025 source: 3_gen_image_lcm.py](https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py)',
], notes='Adapted from the SD5913 2025 `2_gen_image.py` and `3_gen_image_lcm.py` examples. '
    'The standard and LCM examples use different model/scheduler combinations, so their outputs '
    'are not a controlled quality comparison. Explain that few-step sampling depends on a '
    'compatible model and scheduler. This code-repository extra is not in the 2025 Week 5 PDF. '
    'The archived `2_gen_image.py` selects CPU when CUDA is unavailable but passes float16 '
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
S.append(two_col('05 · THE API LOOP', 'The client asks; the service returns media', [
    'Send a prompt and model options with a POST request.',
    '',
    'Keep credentials in an environment variable, not in the source or browser.',
    '',
    'The response may contain image bytes or a URL; the client displays the result.',
    '',
    '[Complete, runnable Week 4 example](https://github.com/sd5913/teaching/blob/main/scripts/image_api_example.py)',
], [
    'URL = (',
    '    "https://easel.ait4x.org/v1/images/generations"',
    ')',
    'token = os.environ["EASEL_KEY"]',
    'headers = {',
    '    "Authorization": "Bearer " + token,',
    '    "Content-Type": "application/json",',
    '}',
    'request = Request(',
    '    URL, data=json.dumps(PAYLOAD).encode(),',
    '    headers=headers, method="POST",',
    ')',
], notes='The code is excerpted from the current teaching repo’s complete standard-library '
    'example at `scripts/image_api_example.py`. It reads `EASEL_KEY` from the environment; '
    'never put a key in a slide, browser bundle or public repository. The selected classroom '
    'Easel client may expose a different interface, so preflight that exact workflow and do '
    'not require students to create credentials. The full script writes to the Week 4 demo '
    'asset path; do not run it from the shared repo unless intentionally regenerating that '
    'asset. Its response handler supports base64 image data and a download URL.',
    right_size=28))
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
    'The 2025 Stable Diffusion, LCM and ControlNet scripts are references, not a guarantee that every laptop can run them.',
    '',
    '{muted:If the model is not ready, keep the lesson moving with the API result and a prepared screenshot.}',
], notes='Do not ask students to install PyTorch, download a checkpoint or create API credentials '
    'as a condition of completing the exercise. Rehearse the local pipeline on the actual demo '
    'machine. CPU execution may be slow and half-precision GPU settings do not transfer safely '
    'to every device. This draft should explain fallback, not promise a live run.'))

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
