# SD5913 · 8 October 2026 lesson plan (`week05`)

**8 October 2026 · Images & video: pixels, models and interaction** · 2 hours.
This is `week05` content taught one Thursday later after the 1 October holiday.
Keep repository names and routes aligned with PFAD; use calendar dates rather than
week numbers for teaching dates from here on. The deck is `deck/week05.py`; it
extends the previous API request/response example. Do not infer a final semester
date from the one-week shift.

## Purpose

Students move from numbers they already know how to inspect to image data they can
manipulate, then use that model to understand video frames and generated images. The
session distinguishes procedural pixels from learned image-generation models. An Easel
API exercise makes the request and response tangible; a short project sketch starts
students thinking about the interactive experience assignment without inventing a due
date or adding an assessed deliverable.

Start more gently than the first draft: recall Python values and types, then use lists,
indexes and nested rows to build a small numeric grid. Only after students can read that
grid do we interpret its values as brightness or colour, and ask a renderer to make the
data visible. The first browser exercise renders a grayscale SVG directly from a
Python grid: students predict a pixel, run the code, correct the shade mapping, and
see the result on the HTML slide without installing an image library.

By the end of class, students can:

- describe a conventional RGB image as rows, columns and channel values, and explain what
  a pixel lookup addresses;
- recall scalar Python types, read list positions from zero, and explain how a list of
  rows gives image values spatial positions;
- make or change a small NumPy image, pass it to Pillow, and explain how its shape,
  dtype and mode describe the values;
- generate random pixels in code and explain the 8-bit value range and exclusive upper bound;
- edit a spatial colour rule in an in-slide Python drill and see its pixels change;
- compare ASCII renderings of an introductory student mark at several text widths,
  distinguishing character-grid resolution from genuine source-image detail;
- describe a frame sequence as still images in an order, make a short animated GIF, and
  edit a browser animation; distinguish these from compressed video or live webcam processing;
- contrast GAN, VAE and diffusion at a high level; trace one Stable Diffusion path and
  distinguish CLIP, text conditioning, U-Net and VAE roles, including weights versus
  latents in training and generation;
- describe the request, wait and response in an image API exercise, using the previous
  week's vocabulary; write a constrained prompt and judge the result against an
  observable requirement rather than assuming text specifies every pixel;
- distinguish a text-only image-generation request from an image edit that uses a
  source file, and detect invented glyphs or altered silhouettes in edit outputs;
- sketch one project-specific interaction as an action, system response and feedback.

Keep LCM and ControlNet as optional code-repository extensions, not core outcomes. The
2025 slide deck does not cover GAN, LCM or ControlNet.

Keep the mathematics visual and incremental. Recall values and types, then one-dimensional
lists, indexes, nested rows, grayscale values, and RGB channel groups. Let students predict
which value occupies a position before introducing array shape or image libraries. Mention
NumPy/Pillow as tools that package and render these same axes, not as prerequisites for
understanding them. Clarify that channel order, value range and compression depend on the
chosen representation.

## Before class

- Preflight the [official DHH keynote](https://www.youtube.com/watch?v=vDjW_dRyKXY&t=1694s),
  sound and YouTube access. Play 28:14–31:14 of the edited video and stop manually;
  the player does not stop automatically. Test both independent ClassPoint votes,
  or use a show of hands if the add-in is unavailable. Keep the first vote hidden
  until the second one is complete.
- Check the Easel client, classroom connection and intended model options on the teaching
  machine. Keep credentials out of the deck and any student-facing files.
- Prepare one saved API result as a fallback. Generation latency or service availability
  should not consume the interaction exercise.
- The active `pfad` `2026` branch has no Week 5 examples yet; linked student code examples
  below intentionally point to its frozen `2025` branch.
- The slides include complete scripts for a tiny RGB image, a random-noise image and a
  three-frame animated GIF. Copy each code panel into its named Python file and run the
  command printed beside it; these examples need only Pillow. The random-noise example
  starts with Python's standard-library random module before introducing array libraries.
- In the HTML deck, three Python drills run via Pyodide: two print SVG images from
  pixel values and one prints a JSON request without calling an API. The first Run
  downloads the runtime; these need a connection initially but no image library,
  account or key. Check the editor and image preview on the classroom device.
- An editable p5.js sketch previews the same frame-index idea in the browser; it is
  JavaScript, not the Python/Pillow code that exports a GIF. A still substitutes for
  the live sketch in the PDF and PPTX.
- Source marks 18 and 38 already live in the teaching assets and were part of the
  introductions. Use the new Week 5 student tutorial to make local ASCII renderings
  with `ascii-magic`, a ten-step resolution slider and a GIF. The in-slide slider
  selects frames prepared from Python; it does not run the package in the browser.
  The CRT edit used an earlier, denser 56-column ASCII image as input, which is
  shown alongside it; it was not made from the slider's 36-column still. Keep the
  draft CRT and wool edits labelled as experiments until Gio supplies final A/B art.
  Inspect the exact input glyphs against the model-edited screen image: a model may
  approximate the silhouette while inventing characters. Do not require a student
  image-edit account or call, and do not set anyone's GitHub avatar for them.
- The current teaching repo's
  [`image_api_example.py`](https://github.com/sd5913/teaching/blob/main/scripts/image_api_example.py)
  is a runnable standard-library Easel request. It reads `EASEL_KEY` from the environment
  and writes to the Week 4 demo asset path; use it as an instructor reference, keep the key
  private, and do not run it from the shared repo unless regenerating that image.
- The archived examples depend on older Diffusers/PyTorch model setups. If showing
  Stable Diffusion, LCM or ControlNet in ComfyUI, rehearse that exact workflow and checkpoint
  on the teaching device. Treat it as an instructor demonstration; do not require student
  installation or promise that the archive's dependencies run on every laptop. In particular,
  the archived `2_gen_image.py` passes float16 even when selecting CPU; test the exact path.
- The in-slide animation example writes `moving-dot.gif` from three generated still
  frames, using Pillow only. The archived
  [`st_video_stream.py`](https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py)
  is a separate optional webcam reference, not the class example.
- Pull the student repository's current `2026` branch. Assignment 3 is listed as
  interactive experience, with its brief/date still TBC in the course README.

## Two-hour run of show

| Time | Segment | Instructor move / student action |
|---|---|---|
| 0:00–0:10 | Before / after | Vote on understanding code, inspect dated AI news, watch the short Rust excerpt, vote again. Ask what evidence would change a mind. |
| 0:10–0:20 | Types and lists | Recall `int`, `float`, `str`, `bool`; read list positions from zero. |
| 0:20–0:30 | Rows become a grid | Nest lists; predict a pixel, then correct the in-slide grayscale SVG. |
| 0:30–0:43 | Values become pixels | Map numbers to grayscale, then group three channel values into RGB. |
| 0:43–0:53 | Tools and rules | Compare NumPy/Pillow representations, read the local noise script and change one rule in the browser RGB grid. |
| 0:53–1:00 | Source marks → text | Recall the pixel yarn-ball and arrow-plus-underscore from introductions. Change text-column resolution on the ASCII slider; compare with the local `ascii-magic` code. |
| 1:00–1:10 | Frames into motion | Run the Pillow GIF locally if prepared; edit positions or rate in the live p5 sketch. Distinguish a GIF from compressed video. |
| 1:10–1:27 | Image-model paths | Contrast CLIP alignment with text conditioning; trace VAE sampling, known noise, training weight updates and fixed-weight generation. GAN/LCM/ControlNet are optional. |
| 1:27–1:31 | Size and settings | Discuss historical model/VRAM estimates and service vs local run. |
| 1:31–1:35 | API recall | Print and revise a JSON prompt request in the browser, without a credential or network call. |
| 1:35–1:50 | Generate and edit | If preflighted, request an image through Easel; compare the actual 56-column ASCII edit input with its draft CRT result, then the arrow-and-underscore source with its wool result. Check glyph fidelity and silhouette. |
| 1:50–1:55 | Tutorial invitation | Point to the local Python script, resolution slider, animated GIF and optional student-chosen GitHub icon. |
| 1:55–2:00 | Interaction seed | In pairs, name one project-specific action, system response and feedback. |

The API study is exploratory rather than a controlled model comparison: only call it
controlled if the client exposes a seed and the relevant settings are held fixed. The
interaction seed is a warm-up, not a new submission requirement.

## Opening discussion

The two independent ClassPoint polls ask the same neutral question: **Should a
developer understand every line of code they ship?** A: Agree; B: Unsure; C:
Disagree. The sequence is a conversation, not a controlled experiment or a
preferred answer. The [13 May 2025 DHH post](https://world.hey.com/dhh/coding-should-be-a-vibe-50908f49)
argues for enjoying code while already using LLMs daily. The
[23 September 2026 keynote](https://www.youtube.com/watch?v=vDjW_dRyKXY&t=1694s)
argues for wider agent-written code; ask students to separate claims and evidence.
The [22 September Anthropic release](https://www.anthropic.com/claude-opus-5-5),
[29 September OpenAI model release](https://openai.com/index/introducing-gpt-6-1-sol/)
and [29 September dots announcement](https://openai.com/index/introducing-dots/)
are vendor sources using different benchmarks or describing a product. The 29
September releases followed the keynote and cannot explain what DHH said on the
23rd. Return to the lesson's practice: inspect representations, predict a change,
run it, and check the result. Do not require any student account for the news.

The marks are not final A/B candidates yet. Mark 18 (yarn-ball) goes from pixels to
ASCII characters and then an edited CRT setting; Mark 38 (separate arrow and
underscore) goes from a digital grid to a wool interpretation. These are opposite
material translations, not two definitive logo designs. Once the two final images
arrive, replace the two draft assets without revising the teaching logic. The
student's own icon is a personal, optional profile choice, never a course requirement.

## Model language to keep precise

- **GAN:** a generator proposes samples while a discriminator learns to distinguish
  generated samples from training examples. Keep this as a brief supplemental comparison;
  GANs do not appear in the 2025 SD5913 Week 5 slide PDF.
- **Diffusion and U-Net:** for latent diffusion, first encode each training image to `z0`,
  then add known sampled noise at timestep `t` and teach a denoiser to predict it.
  Prediction error updates the **weights**. Generation starts at noise `zT`, holds
  weights fixed and updates the **latent**, then decodes it to pixels.
  The 2025 PDF p. 41 is titled “U-Net Training” but combines forward noising and reverse
  sampling; keep those processes distinct. Its p. 42 U-Net drawing is an architecture sketch,
  not a complete Stable Diffusion denoiser.
- **CLIP:** the 2025 PDF p. 39 overstates CLIP as generative. Page 40 shows separate text and
  image encoders and similarity scores: teach it as alignment for matching/ranking, not as
  an image generator or captioner. A generative pipeline can use a text encoder to
  condition the denoiser; CLIP's image encoder does not draw the output.
- **VAE:** an encoder and decoder learn a compact latent representation and reconstruction
  path. The encoder estimates a distribution (mean and variance); a sampled latent
  gives an approximate reconstruction. The 2025 PDF p. 43 sketches this path.
  A VAE component is not synonymous with a diffusion model.
- **Latent diffusion:** the 2025 PDF p. 44 shows one text-conditioned path: text encoder,
  repeated U-Net denoising in latent space, then VAE decoding. Its 64 x 64 latent and 50-step
  loop are one illustration, not universal settings or architecture.
- **LCM and ControlNet:** keep these as optional repository-code extras from
  [`3_gen_image_lcm.py`](https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py)
  and [`4_controlnet_canny.py`](https://github.com/sd5913/pfad/blob/2025/week05/4_controlnet_canny.py),
  not as topics in the 2025 Week 5 slide PDF. Few-step sampling needs a compatible model and
  scheduler; Canny edges can guide broad structure but do not promise a pixel-perfect copy.
- The live Easel/ComfyUI model may use a different objective (for example, flow matching).
  Check the selected model and version; do not label every text-to-image pipeline as the
  classic noise-prediction diagram.
- **Model size:** checkpoint size is one cost. Resolution, precision, batch size, pipeline
  components, memory and inference steps also affect whether and how quickly a model runs.
- The 2025 notebook's approximate 2–5 GB model files and 4–6 GB VRAM for a 512 × 512
  Stable Diffusion example are historical and model-specific estimates, not current hardware
  guarantees. Treat CPU/GPU fallback, half precision and storage as preflight topics.

## Project interaction seed

Ask each student to complete these prompts for their own project:

1. Who is using it, and what are they trying to do?
2. What action or input can they make?
3. What does the program do next, and what feedback makes that response legible?
4. Which choice should the person control, and which part could the system vary?

The quick output is a three-step sketch: **action → system response → feedback**. Keep the
responses tied to each student's idea; do not imply a fixed interface or assignment
deadline until the Assignment 3 brief is confirmed.

## Sources and adaptation notes

- **2025 Week 5 slides:** the verified local reference bundle contains
  `SD5913 - PFAD - Week 5.pdf` and `.pptx`. The image section is PDF pp. 32-37 (pixel grid,
  8-bit values, NumPy/PIL/OpenCV and random noise) and pp. 38-46 (diffusion, CLIP, U-Net,
  VAE, latent diffusion, UI/API options and a Streamlit example). The first 31 pages cover
  input, callbacks, APIs and classes; the final pages are historical environment/tutorial
  setup. This 2026 deck keeps the relevant image/model sequence without replaying Week 4 or
  copying old setup instructions.
- **Runnable `pfad` references:** the active `2026` branch has no Week 5 files yet, so
  these links intentionally target the frozen `2025` branch:
  [`1_random_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/1_random_image.py)
  is a NumPy/Pillow noise example, and
  [`week05_notebook.ipynb`](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)
  contains pixel/mode examples and model notes. The archived
  [`st_video_stream.py`](https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py)
  processes live webcam frames; the in-class example instead builds a small Pillow GIF from
  ordered stills. The local Diffusers examples—[`2_gen_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/2_gen_image.py),
  [`3_gen_image_lcm.py`](https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py)
  and [`4_controlnet_canny.py`](https://github.com/sd5913/pfad/blob/2025/week05/4_controlnet_canny.py)—
  are optional instructor references, not a student install requirement. The full archived
  `requirements.txt` includes model and webcam stacks; install only the packages needed for
  a tested example.
- **Scope mismatch in the 2025 bundle:** `Creative Programming - Lecture Plan.docx` lists
  Week 6 as “Interactive Installations & Images/Video Streams” with OpenCV. The actual
  `SD5913 - PFAD - Week 6.pdf` is titled “Audio streams”; its image/diffusion material is
  pp. 12-21 and its audio sequence starts at p. 23. It has no OpenCV/video-processing lesson.
  The current code-generated frame sequence is therefore a 2026 extension, not a
  reproduction of that Week 6 slide deck. The archived webcam callback remains a separate
  optional code reference.
- **2025 Week 12:** `SD5913 - PFAD - Week 12.pdf` pp. 53 and 59-65 covers ComfyUI/MCP and
  local installation. Keep that historical tutorial optional; do not copy its dated CUDA
  setup or its `0.0.0.0` network-listening instructions into student guidance.
- **API and style:** the linked
  [`scripts/image_api_example.py`](https://github.com/sd5913/teaching/blob/main/scripts/image_api_example.py)
  is the current teaching repo's runnable standard-library Easel example. It reads
  `EASEL_KEY` from the environment and writes to the Week 4 illustration path. Reuse Week 4's
  request/response vocabulary and code-first layout; never expose a key or overwrite the
  shared illustration unintentionally.
- **Historical assignment facts:** the 2025 Week 5 PDF p. 4 lists an Oct. 26 deadline.
  Do not carry it forward. The active 2026 `pfad` README still lists Assignment 3 as TBC;
  this interaction sketch remains a warm-up, not a new deliverable.

This is a first draft of the instructor sequence. Final timing, the selected Easel controls,
any local-model demonstration, and the Assignment 3 deadline are deliberately left open for
the lecturer to confirm.
