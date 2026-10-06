# SD5913 · Week 5 lesson plan

**Images & video: pixels, models and interaction** · 2 hours. Date and any room-specific
arrangements remain to be confirmed after the 1 October holiday. The deck is
`deck/week05.py`; it extends the Week 4 API request/response example.

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
data visible. The first exercise is therefore about code becoming numbers and numbers
becoming a picture—not about installing an image library.

By the end of class, students can:

- describe a conventional RGB image as rows, columns and channel values, and explain what
  a pixel lookup addresses;
- recall scalar Python types, read list positions from zero, and explain how a list of
  rows gives image values spatial positions;
- make or change a small NumPy image, pass it to Pillow, and explain how its shape,
  dtype and mode describe the values;
- generate random pixels in code and explain the 8-bit value range and exclusive upper bound;
- describe a frame sequence as still images in an order, make a short animated GIF, and
  distinguish this simple example from a compressed video file or live webcam processing;
- contrast GAN, VAE and diffusion at a high level; trace one Stable Diffusion path and
  distinguish CLIP, U-Net and VAE roles;
- describe the request, wait and response in an image API exercise, using the previous
  week's request/response vocabulary;
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
| 0:00–0:05 | Set the path | Today: Python values → a grid → visible pixels → generated images. |
| 0:05–0:18 | Types and lists | Recall `int`, `float`, `str`, `bool`; read list positions from zero. |
| 0:18–0:30 | Rows become a grid | Nest lists; locate a value by row and column. Let students predict before revealing. |
| 0:30–0:43 | Values become pixels | Map numbers to grayscale, then group three channel values into RGB. |
| 0:43–0:53 | Dimensions and tools | Compare nested lists with NumPy shape/dtype and Pillow size/mode. |
| 0:53–1:00 | Random pixels | Generate an RGB noise image in code; distinguish a rule-based result from a learned output. |
| 1:00–1:10 | Frames into motion | Run the three-frame Pillow example; change the dot's positions and frame duration, then distinguish an animated GIF from a compressed video file. |
| 1:10–1:30 | Image-model paths | Compare GAN/VAE/diffusion briefly; trace CLIP, U-Net and VAE through one latent-diffusion path. LCM/ControlNet are optional extras. |
| 1:30–1:35 | Size and settings | Discuss historical model/VRAM estimates, steps, guidance, seed, resolution and service vs local run. |
| 1:35–1:38 | API recall | Revisit last week's request/response pattern; ask what the client sends and what comes back. |
| 1:38–1:55 | Generate and compare | Begin with random pixels, request one image through the Easel client, then optionally compare with a preflighted local model. Change one input and annotate. |
| 1:55–2:00 | Interaction seed | In pairs, name one project-specific action, system response and feedback. |

The API study is exploratory rather than a controlled model comparison: only call it
controlled if the client exposes a seed and the relevant settings are held fixed. The
interaction seed is a warm-up, not a new submission requirement.

## Model language to keep precise

- **GAN:** a generator proposes samples while a discriminator learns to distinguish
  generated samples from training examples. Keep this as a brief supplemental comparison;
  GANs do not appear in the 2025 SD5913 Week 5 slide PDF.
- **Diffusion and U-Net:** for latent diffusion, first encode each training image to `z0`,
  then add noise at a timestep and teach a denoiser to predict it. Generation starts at latent
  noise `zT`, applies the learned denoiser repeatedly, then decodes the clean latent to pixels.
  The 2025 PDF p. 41 is titled “U-Net Training” but combines forward noising and reverse
  sampling; keep those processes distinct. Its p. 42 U-Net drawing is an architecture sketch,
  not a complete Stable Diffusion denoiser.
- **CLIP:** the 2025 PDF p. 39 overstates CLIP as generative. Page 40 shows separate text and
  image encoders and similarity scores: teach it as alignment for matching/ranking, not as
  an image generator or captioner.
- **VAE:** an encoder and decoder learn a compact latent representation and reconstruction
  path. The 2025 PDF p. 43 shows image -> encoder -> latent -> decoder -> reconstruction.
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
