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
- make or change a small image in code and explain how a loop or random rule affects it;
- describe raw video as ordered frames with a time axis, while distinguishing this model
  from a compressed video file;
- contrast GAN, VAE and diffusion at a high level, and identify CLIP as an alignment model
  rather than an image generator;
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
- If showing a local Stable Diffusion/LCM checkpoint in ComfyUI, rehearse it on the actual
  device. Treat it as an instructor demonstration only; do not require student installation
  or promise that the 2025 scripts run on every machine.
- Do not use the 2025 webcam-stream example as if it generated video. This lesson explains
  the frame/time representation; a generative-video demo is optional and only if a tested
  service is available.
- Pull the student repository's current `2026` branch. Assignment 3 is listed as
  interactive experience, with its brief/date still TBC in the course README.

## Two-hour run of show

| Time | Segment | Instructor move / student action |
|---|---|---|
| 0:00–0:10 | API recall | Revisit last week's request/response pattern; ask what the client sends and what comes back. |
| 0:10–0:25 | Image representation | Read row, column and RGB channel axes. Have students locate one pixel before showing its colour. |
| 0:25–0:40 | Pixels in code | Predict the effect of changing one list position, then make a tiny RGB image and inspect it. |
| 0:40–0:50 | Noise and rules | Generate random grayscale values with loops; distinguish an algorithmic image from a learned output. |
| 0:50–1:00 | Video as frames | Compare three ordered frames. Add the time/frame-rate idea and note that real files are compressed. |
| 1:00–1:25 | GAN, VAE and diffusion | Use the three-family comparison and one latent-diffusion diagram. Clarify what CLIP does not do. |
| 1:25–1:35 | Model size and location | Discuss storage, memory, resolution and latency. Show a local model only if it is ready. |
| 1:35–1:50 | Easel image study | Generate a first result, make one intentional input change, then compare and annotate the outputs. |
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
  and objectives vary.
- The live Easel/ComfyUI model may use a different objective (for example, flow matching).
  Check the selected model and version; do not label every text-to-image pipeline as the
  classic noise-prediction diagram.
- **CLIP:** aligns text and image representations for comparison/ranking. It is not, by
  itself, an image generator.
- **Model size:** checkpoint size is one cost. Resolution, precision, batch size, pipeline
  components, memory and inference steps also affect whether and how quickly a model runs.

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

- SD5913 2025 archive, `week05/`: `1_random_image.py`, `2_gen_image.py`, `3_gen_image_lcm.py`,
  `week05_notebook.ipynb` — retain the pixel-array/noise-to-model progression, but do not
  inherit the old environment assumptions as current student setup.
- SD2112 Week 5 source deck at
  [`deck/week05.py`](https://github.com/venetanji/sd2112-teaching/blob/main/deck/week05.py):
  adapt the GAN diagram/sample-grid sequence (2025 PDF pp. 45–47), CLIP pairing diagrams
  (pp. 48–50), VAE (p. 53), and latent-diffusion workflow (p. 54) for this course's
  image-data progression. Keep SD2112 project examples and assignment claims out of SD5913
  materials.
- SD5913 Week 4, `week04/README.md` and `teaching/deck/week04.py`: reuse the API
  request/response vocabulary students have just seen.

This is a first draft of the instructor sequence. Final timing, the selected Easel controls,
any local-model demonstration, and the Assignment 3 deadline are deliberately left open for
the lecturer to confirm.
