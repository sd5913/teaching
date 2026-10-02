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
- generate random pixels in code and explain how a random rule affects the image;
- describe raw video as ordered frames with a time axis, while distinguishing this model
  from a compressed video file, and distinguish a webcam transform from generated video;
- contrast GAN, VAE and diffusion at a high level, and identify LCM and ControlNet as
  variations on the generation pipeline; identify CLIP as alignment rather than generation;
- describe the request, wait and response in an image API exercise;
- sketch one project-specific interaction as an action, system response and feedback.

Keep the mathematics visual. Use nested lists first so students can read the structure
with Python they already know; mention array libraries as tools that package the same
axes, not as a prerequisite. Clarify that channel order, value range and compression
depend on the chosen representation.

## Before class

- Check the Easel client, classroom connection and intended model options on the teaching
  machine. Keep credentials out of the deck and any student-facing files.
- Prepare one saved API result as a fallback. Generation latency or service availability
  should not consume the interaction exercise.
- The archived examples depend on older Diffusers/PyTorch model setups. If showing
  Stable Diffusion, LCM or ControlNet in ComfyUI, rehearse that exact workflow and checkpoint
  on the teaching device. Treat it as an instructor demonstration; do not require student
  installation or promise that the archive's dependencies run on every laptop.
- If showing `st_video_stream.py`, preflight camera access. It flips a live webcam frame; it
  is a frame-processing example, not generated video. A generated-video demo is optional and
  only if a tested service is available.
- Pull the student repository's current `2026` branch. Assignment 3 is listed as
  interactive experience, with its brief/date still TBC in the course README.

## Two-hour run of show

| Time | Segment | Instructor move / student action |
|---|---|---|
| 0:00–0:10 | API recall | Revisit last week's request/response pattern; ask what the client sends and what comes back. |
| 0:10–0:23 | Image representation | Read row, column and RGB channel axes. Have students locate one pixel before showing its colour. |
| 0:23–0:38 | NumPy and Pillow | Predict a pixel edit, then compare array shape/dtype with Pillow size/mode. |
| 0:38–0:48 | Random pixels | Generate an RGB noise image in code; distinguish an algorithmic image from a learned output. |
| 0:48–0:57 | Video as frames | Compare ordered frames and frame rate. Distinguish compressed files from a live webcam callback. |
| 0:57–1:25 | Image-model paths | Relate GAN/VAE/diffusion; then add Stable Diffusion, few-step LCM and Canny-conditioned ControlNet. Mark GAN/CLIP material as supplemental. |
| 1:25–1:35 | Size and settings | Discuss historical model/VRAM estimates, steps, guidance, seed, resolution and service vs local run. |
| 1:35–1:50 | Easel image study | Generate a first result, make one intentional change the client exposes, then compare and annotate. |
| 1:50–2:00 | Interaction seed | In pairs, storyboard one project-specific action, system response and feedback. Take one rough idea forward. |

The API study is exploratory rather than a controlled model comparison: only call it
controlled if the client exposes a seed and the relevant settings are held fixed. The
interaction seed is a warm-up, not a new submission requirement.

## Model language to keep precise

- **GAN:** a generator proposes samples while a discriminator learns to distinguish
  generated samples from training examples; both parts train in relation to each other.
- **VAE:** an encoder and decoder learn a compact latent representation and reconstruction
  path. A VAE component is not synonymous with a diffusion model.
- **Diffusion:** a model learns a denoising process. Latent-diffusion systems operate on a
  compressed representation and decode the final latent back into pixels; implementations
  and objectives vary. The archived Stable Diffusion 1.5 example uses a text encoder, U-Net
  denoiser and VAE; treat that as one specific pipeline.
- **LCM:** the archive's Latent Consistency Model example pairs a compatible checkpoint and
  scheduler with four inference steps, compared with twenty in its Stable Diffusion example.
  Fewer steps aim to reduce wait time; they do not guarantee the same image quality or make
  the examples a controlled comparison.
- **ControlNet:** the archive converts an image to Canny edges and supplies them as an extra
  structural condition. This can guide broad structure; it does not promise a pixel-perfect
  copy and requires a compatible model/workflow.
- The live Easel/ComfyUI model may use a different objective (for example, flow matching).
  Check the selected model and version; do not label every text-to-image pipeline as the
  classic noise-prediction diagram.
- **CLIP:** aligns text and image representations for comparison/ranking. It is not, by
  itself, an image generator.
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

- The SD5913 2025 archive is a notebook and code examples, not an exported slide deck. No
  Week 5 PDF/PPTX was present in the mounted SD5913 repositories, so this draft adapts the
  archived teaching sequence rather than claiming to reproduce 2025 slides:
  [`week05_notebook.ipynb`](https://github.com/sd5913/pfad/blob/2025/week05/week05_notebook.ipynb),
  [`1_random_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/1_random_image.py),
  [`2_gen_image.py`](https://github.com/sd5913/pfad/blob/2025/week05/2_gen_image.py),
  [`3_gen_image_lcm.py`](https://github.com/sd5913/pfad/blob/2025/week05/3_gen_image_lcm.py),
  [`4_controlnet_canny.py`](https://github.com/sd5913/pfad/blob/2025/week05/4_controlnet_canny.py),
  and [`st_video_stream.py`](https://github.com/sd5913/pfad/blob/2025/week05/st_video_stream.py).
  Retain the pixel-array/noise-to-model progression without inheriting old environment
  assumptions as current student setup.
- SD2112 Week 5 source deck at
  [`deck/week05.py`](https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py):
  use the GAN/VAE/CLIP visuals as supplemental model concepts, not as SD5913 2025 content.
  The cited source file contains notes about an older slide PDF, but no PDF export is stored
  in that repository. Keep SD2112 project examples and assignment claims out of SD5913.
- SD5913 Week 4, `week04/README.md` and `teaching/deck/week04.py`: reuse the API
  request/response vocabulary students have just seen.

This is a first draft of the instructor sequence. Final timing, the selected Easel controls,
any local-model demonstration, and the Assignment 3 deadline are deliberately left open for
the lecturer to confirm.
