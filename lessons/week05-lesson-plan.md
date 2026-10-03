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

By the end of class, students can:

- describe a conventional RGB image as rows, columns and channel values, and explain what
  a pixel lookup addresses;
- make or change a small NumPy image, pass it to Pillow, and explain how its shape,
  dtype and mode describe the values;
- generate random pixels in code and explain the 8-bit value range and exclusive upper bound;
- describe raw video as ordered frames with a time axis, while distinguishing this model
  from a compressed video file; read a live-frame callback and distinguish it from generated video;
- contrast GAN, VAE and diffusion at a high level; trace one Stable Diffusion path and
  distinguish CLIP, U-Net and VAE roles;
- describe the request, wait and response in an image API exercise, using the previous
  week's request/response vocabulary;
- sketch one project-specific interaction as an action, system response and feedback.

Keep LCM and ControlNet as optional code-repository extensions, not core outcomes. The
2025 slide deck does not cover GAN, LCM or ControlNet.

Keep the mathematics visual. Use nested lists first so students can read the structure
with Python they already know; mention array libraries as tools that package the same
axes, not as a prerequisite. Clarify that channel order, value range and compression
depend on the chosen representation.

## Before class

- Check the Easel client, classroom connection and intended model options on the teaching
  machine. Keep credentials out of the deck and any student-facing files.
- Prepare one saved API result as a fallback. Generation latency or service availability
  should not consume the interaction exercise.
- The active `pfad` `2026` branch has no Week 5 examples yet; linked student code examples
  below intentionally point to its frozen `2025` branch.
- The procedural noise example needs only NumPy and Pillow. After downloading
  [`1_random_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/1_random_image.py),
  run `uv run --with numpy --with pillow 1_random_image.py`; do not install the full 2025
  Week 5 requirements for this small task.
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
- If showing [`st_video_stream.py`](https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py),
  preflight camera access. It flips a live webcam frame; it is a frame-processing example,
  not generated video. A local copy can be run with
  `uv run --with streamlit --with streamlit-webrtc --with av streamlit run st_video_stream.py`.
  Do not install the full archived requirements just for this demo.
- Pull the student repository's current `2026` branch. Assignment 3 is listed as
  interactive experience, with its brief/date still TBC in the course README.

## Two-hour run of show

| Time | Segment | Instructor move / student action |
|---|---|---|
| 0:00–0:10 | API recall | Revisit last week's request/response pattern; ask what the client sends and what comes back. |
| 0:10–0:23 | Image representation | Read row, column and RGB channel axes. Have students locate one pixel before showing its colour. |
| 0:23–0:38 | NumPy and Pillow | Predict a pixel edit, then compare array shape/dtype with Pillow size/mode. |
| 0:38–0:48 | Random pixels | Generate an RGB noise image in code; distinguish an algorithmic image from a learned output. |
| 0:48–1:00 | Video as frames | Compare ordered frames and frame rate; read the archived live-frame callback. Distinguish processing from generation. |
| 1:00–1:25 | Image-model paths | Compare GAN/VAE/diffusion briefly; trace CLIP, U-Net and VAE through one latent-diffusion path. LCM/ControlNet are optional extras. |
| 1:25–1:33 | Size and settings | Discuss historical model/VRAM estimates, steps, guidance, seed, resolution and service vs local run. |
| 1:33–1:50 | Easel image study | Generate a first result, make one intentional change the client exposes, then compare and annotate. |
| 1:50–2:00 | Interaction seed | In pairs, storyboard one project-specific action, system response and feedback. Take one rough idea forward. |

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
- **Runnable `pfad` examples:** the active `2026` branch has no Week 5 files yet, so these
  links intentionally target the frozen `2025` branch:
  [`1_random_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/1_random_image.py)
  is a small NumPy/Pillow script; run a downloaded copy with
  `uv run --with numpy --with pillow 1_random_image.py`.
  [`week05_notebook.ipynb`](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb)
  contains the pixel/mode examples and model notes.
  [`st_video_stream.py`](https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py)
  flips each incoming webcam frame; it is live frame processing, not video generation.
  The local Diffusers examples—[`2_gen_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/2_gen_image.py),
  [`3_gen_image_lcm.py`](https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py)
  and [`4_controlnet_canny.py`](https://github.com/sd5913/pfad/blob/2025/week05/4_controlnet_canny.py)—
  are optional instructor references, not a student install requirement. The full archived
  `requirements.txt` includes model and webcam stacks; install only the packages needed for
  a tested example.
- **Scope mismatch in the 2025 bundle:** `Creative Programming - Lecture Plan.docx` lists
  Week 6 as “Interactive Installations & Images/Video Streams” with OpenCV. The actual
  `SD5913 - PFAD - Week 6.pdf` is titled “Audio streams”; its image/diffusion material is
  pp. 12-21 and its audio sequence starts at p. 23. It has no OpenCV/video-processing lesson.
  The current frames/callback material is therefore a 2026 extension grounded in the
  `pfad` code, not a reproduction of that Week 6 slide deck.
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
