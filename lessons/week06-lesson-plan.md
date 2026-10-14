# SD5913 Week 6: Sound as data

Two-hour interactive HTML instructor draft for designers learning programming with agents.

## Teaching direction

Slides 2–7 offer six optional dated news items; show only a few. Original slide 07
(ArtCraft/PhotoCraft) is removed. The remaining software-analysis prompt asks:
**What is the future of software companies if anyone can create and modify software?**
Before the agenda, ask **What software would you make open source?** Invite
two or three suggestions about what students would inspect, change or share.
Discuss ownership and trust rather than looking for a single answer.
These are vendor/source reports, not classroom-tested product results or assessed questions.

Keep the lesson number `week06`. The calendar teaching date is unconfirmed;
15 October 2026 remains a proposal, not a printed commitment.

## Purpose

Start with a physical vibration, capture it as ordered samples, then change a
sound intentionally. Students save a WAV, play an embedded keyboard piano,
multiply a base frequency to build a harmonic, and see an opt-in microphone
signal flowing across a 3D frequency surface. This is a visualization, not
transcription. Four cumulative Strudel layers turn those observations into
music. Break after the complete four-layer score, then open part two with the
instructor's song API demo. Speech finishes as finite console transcription,
continuous browser capture, editable text, then a local LM Studio reply spoken by
Kokoro ONNX. CPU speech is the portable default; NVIDIA CUDA is optional.

Ask students to name an input, predict its effect, inspect the output, and
show how to stop it. Keep the four-layer Strudel sequence and Canvas mock practice.
No new assessed deliverable or requirement to use audio/AI is added.

### From the 2025 slide record to this lesson

The archived 2025 Week 6 PDF (`references/2025/onedrive/PolyU/SD5913/SD5913 - PFAD - Week 6.pdf`,
1-based page numbers) introduces sound as numbers (pp. 24–27), waveform, FFT and
spectrogram (pp. 28–31), then a 44,100-element array (p. 32). Its PyAudio
examples on pp. 33–34 stream through a device; the 2026 finite WAV experiment
is a more reliable first encounter with sample count, rate and a stopping point.
The archived PDF links speech tools (p. 38), discusses async producers and
consumers (p. 39), and poses a microphone-to-speaker loopback question (p. 40).
It does not include a running WebRTC transcription or responding agent. A
separate legacy PFAD Week 9 README describes a Streamlit WebRTC example, but
its named `speech_to_text_webrtc.py` and Compose service were never committed.
The canonical `sd5913/pfad` `origin/2025` `ERRATA.md` records that omission and
its revised Week 9 README no longer claims the app exists. The tracked console
WebSocket demo there requires a separate local realtime server and writes into
an `asyncio.Queue` from a PyAudio callback thread; neither is a validated
classroom path. The Week 7 examples and legacy `extra/docker-bot` demonstrate
text agents separately, not an integrated voice agent. The 2026 browser example
is original work, not a recovered 2025 runnable file. The separate historical
lecture plan labels weeks differently; its proposed transcription workshop is
not evidence of what appeared in the Week 6 slide record. The PDF is evidence
of archived slides, not proof that every page was presented aloud.

In the new opening, the air-particle diagram depicts compressions carrying
mechanical energy, while the next graph is pressure at one fixed microphone
position over time. Neither is a classroom recording. The browser sound lab
then draws the samples that its own Web Audio buffer plays. It does not claim
to measure air pressure or to run the Python WAV writer in the browser.

## Preparation

1. In the PFAD checkout, run `python noise.py` and `python tone.py` from
   `week06/sound/`. Their shared `wav_support.py` is already beside them.
   Open the saved WAVs at low volume; no Python package or account is needed.
2. Open the HTML deck. Test the finite sound lab (slide 13), keyboard (27),
   harmonics (28) and spectrum surface (29) on the teaching computer. The three
   student JS sources are in PFAD `week06/browser/`. DEMO needs no microphone;
   MIC needs consent and localhost/HTTPS. Verify Stop, Escape and slide navigation.
   PDF/PPTX contain stills only. Offer the visual-only route without playing sound.
3. Open four Strudel stages from `resources.html` at low volume. Stop its separate
   tab before returning to the deck. Open the existing mock test on Canvas and keep a consented WAV
   for the no-device route. Do not spend the lesson installing packages.
4. Optional song API: `week06/sound/request_song.py` previews JSON offline by
   default. For an instructor live send, read `site/week06/examples/TEACHER_NOTES.md`,
   check credit/account/model/service state, and serialize attempts; do not retry
   an uncertain paid submission. A key is never needed for the student route.
5. Optional local speech: follow PFAD `week06/speech/CONVERSATION.md` in a separate
   Python 3.12 environment. Reuse prepared models and load a small LM Studio chat
   model. Rehearse Start mic, editable draft, Enter and reply playback on the
   classroom device. The console microphone route has its own README and
   sounddevice/PortAudio requirements; use a consented file if unavailable.

## Two-hour run of show

| Elapsed | Slides | Activity and instructor move |
|---|---:|---|
| 00–08 | 1–9 | Choose up to three news items, ask what software students would make open source, then show the agenda. |
| 08–20 | 10–14 | Vibration to microphone samples; finite tone/noise lab and Stop; recall image arrays. |
| 20–30 | 15–21 | Ordered values, sample clock, browser-Python prediction and noise WAV. |
| 30–44 | 22–29 | Synthesis; fixed sample clock; vote, piano (27), harmonics (28), then DEMO or consented MIC on the spectrum surface (29). |
| 44–60 | 30–38 | Browser score and four cumulative Strudel layers (35–38). Finish with the complete melody score. |
| 60–70 | 39 | Break; stop the Strudel tab, browser audio and microphone tracks. |
| 70–84 | 40–44 | Start part two with the instructor API demo: compare image/song requests, inspect JSON, follow status and preview. Live generation only if rehearsed. |
| 84–100 | 45–51 | Local speech demo: console, browser capture, edit, send to LM Studio and hear Kokoro ONNX. File and typed-text fallbacks. |
| 100–110 | 54 | Canvas mock: six minutes alone, four minutes discussing reasoning. |
| 110–120 | 52–53, 55–58 | Interaction reflection; resources; 40-question, 30-minute quiz reminder; individual project brief. |

If time slips, omit news and shorten API detail. Preserve the sound lab, complete
Strudel score and Canvas mock practice. The voice surface's synthetic DEMO can replace an untested
classroom microphone; do not imply it is a recording or transcription.

## Demonstration notes

### 1. Noise

Run `python noise.py`. Expected printout includes 44,100 samples,
22,050 samples/s and two seconds. Open the saved WAV at low device volume.

The core list uses `random.Random(7)` and `uniform(-0.08, 0.08)`, echoing
Week 5's seeded RGB noise. A 10 ms fade at both ends reduces abrupt edge jumps.
It does not turn the noise into a periodic tone. Start the explanation with the
numbers and their order before explaining file bytes.

Pair changes: SEED 7 to 8; SECONDS 2 to 1; or AMPLITUDE 0.08 to 0.04.
Change only one initially. Rerunning replaces `noise.wav`; rename the reference
file or use another `--out` folder before comparing. The change in duration
changes sample count and file size; seed and amplitude do not change that count.

The reused slide 20 waveform is a separate 220 Hz harmonic teaching illustration
at 44,100 samples/s. It is labelled explicitly and is not a recording of our
22,050 samples/s noise example.

### 2. A sine rule

Run `python tone.py`. The only important generative difference is the
sample expression. `i / sample_rate` is time in seconds, `frequency` is cycles
per second and `2 * pi` converts cycles to radians. `sin` returns a repeating
value and amplitude scales it. Do not turn this into a trigonometry exercise.

Change FREQUENCY from 220 to 440 while keeping SAMPLE_RATE at 22050. The sound
has twice as many cycles per second and the same duration and sample count.
Halving AMPLITUDE scales the signal values; do not promise half perceived loudness.
The demonstrations reject invalid frequencies at or above half the sample rate.
No live streaming audio driver, PyAudio, GPU or third-party Python package is needed.

### 3. Music: browser score and four Strudel layers

Begin in strudel.cc with the already-present starter or an existing example
selected by the instructor. Play, change one visible value, Update, and Stop.
No specific third-party song is copied into this repository. Tutorial video:
pending the instructor's exact link; the current lesson does not guess one.

Use slides 35–38 in order. Each opens a complete cumulative score. The next
link restores the supplied baseline, so undo an experiment before adding the
next layer, or keep it as a separate saved variation:

1. Hi-hat: `s("hh*8").gain(.12)`; change `*8` to `*4`.
2. Bass: `note("c2 ~ g2 ~").s("triangle").gain(.15)`; try a higher register.
3. Chords: `note("[c3,e3,g3]").s("sine").gain(.08)`; change E to E-flat.
4. Melody: `note("c4 e4 g4 b4").s("sine").gain(.12)`; replace one note with a rest.

`setcpm(100/4)` gives 25 cycles per minute. Here one cycle is four beats at
100 BPM, or 2.4 seconds. `stack` combines parts. Do not teach the full syntax
at once: read only each added line. The website's `hh` and Easel's bundled
`hh` need not sound identical. No remote sample-bank loading is required.

The links use Strudel's encoded-score fragment and open a silent editor.
They replace an iframe: the dedicated tab owns its keyboard controls and audio.
Before leaving it, Stop or Ctrl+.; navigating the slides cannot silence a
separate tab. Browser sound always starts from a user gesture.

Slide 31 uses the original grid sequencer to illustrate one click, one state
change and one scheduled note before Strudel. Students can inspect the visual
code and feedback without listening. Stop the complete four-layer score before
the break on slide 39. Optional Easel agent-edit and export instructions remain
on `resources.html` for follow-up; the separate making and partner-review slides
have been removed from the classroom sequence.

### 4. After the break: instructor API demo

The script `week06/sound/request_song.py` in PFAD is an instructor reference and local
preview. Run it from that folder. Teach the compact payload and states in class rather than asking
students to understand the whole defensive client in one sitting.

Begin part two on slide 40. From PFAD `week06/sound`, preview the default
request without a credential or network request:

```bash
uv run --no-project request_song.py
```

The client implements the verified sequence: one POST submission; bounded
latest-attempt polling with identity checks; per-track polling; remote download
preparation; authenticated same-origin content download. It saves every returned
track and preserves the actual encoding rather than naming any bytes `.wav`.

`--send` deliberately opts into a real generation and can spend credits.
The current PFAD script loads the repository-root `.env` and accepts `EASEL_KEY`,
with `EASEL_API_KEY` as an alias; `EASEL_BASE_URL` overrides the supplied service
default. uv reads the inline `python-dotenv` dependency. The operator's upstream
Suno token is separate. Never print, project or commit credentials.

Easel's server-side `dry_run: true` is **not** offline. It contacts the backend
and fills the native form. The teaching script's default preview is intentionally
different. It does not set that flag or call the server.

No current `easel-cli` song command was found; do not teach an invented CLI
subcommand. See the pinned Easel documentation in `site/week06/examples/TEACHER_NOTES.md` for
all fields and endpoint details. The live service, account controls and exact
generated duration remain unverified. The local tests use fake responses.

### 5. Speech: console to browser to response

Slides 46–51 link to `speech.html`. Start with PFAD `transcribe.py` in its
separate Python 3.12 environment: run the bounded 3-by-5-second local microphone
capture or use a consented WAV if hardware fails. Keep each proposed transcript
with its source and settings. Never equate output text with an authoritative
record of a person’s words.

The explicit console microphone mode captures a bounded amount of local sound and sends
5-second chunks to a local faster-whisper model. Its output can lag and the chunk
boundaries can cut words. It is not a native streaming decoder. Only record
consenting participants, point out Ctrl+C before starting, and use the WAV input
if microphone permission or the device fails. No recording or model loading
occurs just by opening the slides or exercise page.

For the optional teacher WebRTC step, run PFAD `week06/speech/speech_webrtc.py`
locally after the portable `CONVERSATION.md` setup, using
`conversation_requirements.txt` and the explicit speech `.venv` interpreter.
Start mic and browser permission send audio over WebRTC to local Streamlit,
which converts to mono 16 kHz and transcribes three-second chunks continuously
until Stop mic or Send. Proposed text fills the editable chat composer. Stop
for careful editing, then Enter sends to the selected loopback LM Studio model.
Sending also stops capture before Kokoro ONNX speaks the reply. Each reply has
its own player; autoplay can require a Play click. CPU is the default on Windows,
Macs and AMD; CUDA is optional. If localhost transport,
model download or microphone permissions fail, use the PFAD file demo. A remote
network demo would need HTTPS and possibly TURN, not just this lesson link.

Kokoro ONNX also supplies a separate file exercise. It writes at 24 kHz. The transcription file decoder resamples to 16 kHz;
changing a rate label alone would change the perceived speed and pitch. The
transcript is a model prediction. Compare it with the source, including pauses
and silence. Do not treat it as a verbatim record without checking.

KittenTTS is a separately versioned optional comparison in the linked notes.
Keep its legacy lightweight model distinct from the current, larger KittenTTS 2.
These scripts and the app add no speech or AI assignment requirement. See PFAD
`week06/ENVIRONMENT.md` for instructor Windows inference checks and resource
measurements. Physical classroom microphone/speaker behavior and Mac/Linux
installation still need a preflight.

### Verification and classroom limits

The standard-library noise and tone examples were executed and their WAV
headers/sample values checked. Speech console tests use model/device substitutes.
The local Streamlit app rendered silent before START; with Chromium's fake
microphone and a stub recognizer, WebRTC delivered frames, the resampler fed a
16 kHz chunk, a proposed line appeared, and STOP exposed the correction field.
The three p5 sketches loaded silently in Chromium. The keyboard and harmonic
controls started short audio only after a gesture; the spectrum sketch received
fake microphone frames, animated bounded frequency history, and released the
track on Stop/Escape/navigation. A synthetic DEMO and narrow browser viewport
also loaded. The tested source lives in PFAD `week06/browser/` and is copied
unchanged into the slides. PDF and PPTX stills are illustrative, not live audio.
The earlier teaching checks above used the historical bounded app snapshot;
the current app is maintained in PFAD. Its environment report records real
MiniCPM/Whisper/Kokoro inference and repeated browser replies on Windows, plus
one successful live song request. This teaching review does not rerun those
model or paid service checks. Physical microphone capture and classroom
audibility remain unverified. Easel's editing and export behavior is verified from the pinned
source and test assertions, not from the instructor's installed client.

The public Strudel editor was checked in the cloud browser: the default starter
loaded and its Play/Stop controls changed state. The four-layer encoded link
loaded the exact score. Its subsequent Play click was not completed because
the cloud browser permission request was dismissed before a decision; it was
not retried. Browser/device audibility and the classroom output route
still require listening. The local deck's sound lab had Play/natural-end,
mode-change and navigation-stop Chromium checks on the earlier draft head.
The offline mock-Web-Audio test
(`node tests/week06_audio_lifecycle.test.cjs`) checks silent load, Play,
parent slide-stop messages, visibility stop and stopping while startup awaits
a resume. This is control-flow evidence, not a browser audio check.

## Assessment wording to preserve

Dates come from the current course materials; the quiz format and 15-point
assignment value also use the instructor briefing supplied for this draft.

- Quiz: Thursday 22 October 2026; **40 questions in 30 minutes**, open-book,
  multiple choice. Timing and count are instructor-confirmed. Open-book does not
  establish permission to use AI tools.
- Assignment 3: an individual interactive experience, 15% of the course;
  Sunday 1 November 2026, 23:59 Hong Kong time. The Canvas-ready brief is
  `syllabus/03-interactive-experience.md`, with a proposed 15-point rubric,
  repository URL submission, README, PROCESS and a user trial. Audio and AI
  remain optional. The brief is built to Word/HTML but is not published on the site.
- The existing mock test is on Canvas. No direct quiz URL has been supplied;
  open it through the course page. Its questions and answers are not published here.

## Source basis

- SD5913 teaching main at `dd8e30ed640af73008f283fd6cbcca9167fc3735`:
  Week 5 deck, diagrams, example style and lesson plan.
- PFAD `2026` at `11252caa6ee6e34937fc3314b396e944be6bdf7d`:
  `week05/noise.py`, `image_array.py`, `request_image.py`.
- SD2112 teaching main at `558d1d77ce6b0e42c2e9ec955ca191d40cb7976e`:
  Week 6 waveform/spectrogram illustrations, live analysis and sequencer.
- Exact API source commits and routes: `site/week06/examples/TEACHER_NOTES.md`.
- Python [wave](https://docs.python.org/3.12/library/wave.html) and
  [struct](https://docs.python.org/3.12/library/struct.html) documentation.

The source files retain attribution. The reused sound figures are computed
teaching illustrations, not recordings or model outputs.

- Easel client main at `d8dda0f1b953136ee7fc827eeeb39104471770b4`: pinned
  [Strudel workflow](https://github.com/venetanji/easel-client/blob/d8dda0f1b953136ee7fc827eeeb39104471770b4/docs/strudel.md)
  and [compatibility](https://github.com/venetanji/easel-client/blob/d8dda0f1b953136ee7fc827eeeb39104471770b4/docs/strudel-compatibility.md).
- Strudel [first sounds](https://strudel.cc/workshop/first-sounds/) and
  [first notes](https://strudel.cc/workshop/first-notes/).
