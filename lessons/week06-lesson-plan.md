# SD5913 Week 6: Sound as data

Two-hour interactive HTML instructor draft for designers learning programming with agents.

Keep the lesson number `week06`. The calendar teaching date remains unconfirmed.
15 October 2026 is a proposed date, not a printed commitment.

## Purpose

Continue Week 5's image lesson with another representation students can inspect.
A list of random values becomes two seconds of noise when a sample rate and file
format give it a playback meaning. Replacing the random rule with a sine function
makes frequency and amplitude tangible. The song API then makes a familiar
request/response habit asynchronous. A short local speech-model comparison connects
text, waveforms and imperfect transcripts. A four-layer Strudel score makes live edits
tangible. Students then use an agent to vary one layer and inspect the result.

The outcome is an explanation supported by a working example. Students should
be able to:

- explain how a sample index differs from a pixel position;
- calculate duration from sample count and sample rate for the mono examples;
- predict what changes when they edit seed, frequency, amplitude or duration;
- distinguish a submitted song request from completed, saved audio;
- distinguish speech synthesis from transcription and check an output against its source;
- describe one user action, the data it changes, feedback and a way to stop.

The reflection and making activities are formative. They add no assessed
deliverable or rubric condition. Audio and AI generation are options for
Assignment 3, not requirements.

### From the 2025 slide record to this lesson

The archived 2025 Week 6 PDF (`references/2025/onedrive/PolyU/SD5913/SD5913 - PFAD - Week 6.pdf`,
1-based page numbers) introduces sound as numbers (pp. 24–27), waveform, FFT and
spectrogram (pp. 28–31), then a 44,100-element array (p. 32). Its PyAudio
examples on pp. 33–34 stream through a device; the 2026 finite WAV experiment
is a more reliable first encounter with sample count, rate and a stopping point.
The archived PDF links speech tools (p. 38) and poses a microphone-to-speaker
loopback question (p. 40), but it does not contain this year's runnable speech
exercise, browser score, song API, Strudel layers or agent edit. Those are 2026
additions, not historical carry-overs. The separate historical lecture plan
labels weeks differently; its proposed transcription workshop is not evidence
of what appeared in the Week 6 slide record. The PDF is evidence of archived
slides, not proof that every page was presented aloud.

## Preparation

1. Open the HTML lesson and its linked `resources.html`. Download
   `wav_support.py` beside `noise.py` and `tone.py`. Source files live in
   `site/week06/examples/`. Python 3.10+ is sufficient for these standard-library
   examples. Use `python3` instead of `python` if that is the local command.
2. Run `python noise.py` and `python tone.py`. Each saves a
   two-second mono 16-bit PCM WAV in `out/`. Neither plays automatically.
3. Test the exact classroom device, output route and low volume. The numerical
   amplitude limit cannot guarantee a comfortable listening level on every device.
   Offer waveform/visual review for anyone who does not want to listen.
4. Open the HTML deck. The analysis instrument is slide 19 and the score
   sequencer is slide 32, before the Strudel build. Check Play, Stop, Escape and slide navigation
   on the teaching machine. These instruments need no microphone. Open Strudel
   separately, at low volume; Stop/Ctrl+. before switching back to the slides.
   The deck cannot stop audio in a separate tab.
5. The API preview is offline. Run the slide 26 command without `--send` to show
   the exact JSON. A key and network are unnecessary for the student exercise.
6. For an optional later live generation, read `site/week06/examples/TEACHER_NOTES.md` first.
   Verify the deployed service, model discovery, classroom account, credits,
   provider terms and manual login/CAPTCHA access. The source contract was checked,
   but this draft did not test a live service or create a song. Use original,
   non-sensitive prompts and lyrics the demonstrator has permission to use.
7. The current backend has a shared latest-attempt status. Serialize a teacher
   demo. Do not give the whole class a shared account and invite concurrent calls.
   Do not automatically repeat a timed-out generation submission. Keep an
   appropriate previously saved result if one is available, otherwise use the
   offline request and WAV examples.
8. Open the four staged Strudel links from `resources.html` and keep the starting
   score. For the Easel demonstration, use a current client, a fresh project,
   then Templates → Strudel sound. An old project can retain older pinned kits
   even when adding a fresh template. The instructor is checking the local
   client separately; do not spend class time repairing an old project.
9. Have the already-supplied mock available. No verified course Canvas URL has
   been supplied, so open the existing resource directly. The tutorial video
   is still unidentified: its resource slot is explicitly pending, with no link.

10. For the optional speech demo, follow `speech.html` and the linked PFAD
    `week06/speech/README.md` before class. Use its separate Python 3.12 environment,
    not the Week 4 Worker project. Pre-download the models, test espeak-ng and
    microphone input on the teaching device, and keep a consented short WAV as a
    fallback. No model inference or microphone recording was run while preparing
    this addition. A microphone is unnecessary for the file-input exercise.

## Two-hour run of show

| Elapsed | Slides | Activity and instructor move |
|---|---:|---|
| 00–08 | 1–5 | Discuss a file-save sound; recall image values, then read one audio list. |
| 08–20 | 6–12 | Predict duration in a formative ClassPoint vote, change the rate in browser Python, then inspect noise and WAV. Show hands if ClassPoint is unavailable. |
| 20–26 | 13 | Pairs save a reference, change one constant, predict and compare. |
| 26–38 | 14–18 | Read sine as a recipe; vote on what stays fixed at 440 Hz, then compare tone files. |
| 38–45 | 19–20 | Predict a frequency change, compare the same live oscillator in waveform and spectrum, then Stop. Spectrogram bridge only if useful; its stills are not one measured signal. |
| 45–55 | 21 | Ten-minute break. Stop browser audio. |
| 55–63 | 22–28 | Song request as asynchronous state change; preview JSON offline. Skip live submission and compress API details if time is tight. |
| 63–70 | 29–31 | Contrast text-to-speech and transcription with prepared, consented files. Skip microphone/model setup in class; scripts are optional follow-up. |
| 70–87 | 32–40 | A partner predicts and toggles a browser-score cell, sees the feedback and demonstrates Stop. Then build hi-hat → bass → chords → melody in Strudel. |
| 87–105 | 41–44 | Easel bridge and pair making. Eighteen minutes include the final four-minute partner test. If setup fails, stay in Strudel and paste an agent-drafted edit. |
| 105–115 | 46 | Existing mock practice: six minutes individual work, four minutes explaining reasoning. No new questions. |
| 115–120 | 45, 47–50 | One concrete reflection; resources and assessment reminders are reference slides, not five minutes of new lecture. |

At the end of the pair task, use slide 44 for partner feedback, then slide 45
for one closing observation. If time slips, omit slide 20 and the live API demo.
If speech setup is unavailable, trace input/output without waiting for downloads.
Keep the browser score, Strudel buildup, making time and mock slot.
Do not spend the class installing packages or troubleshooting account access.

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

The reused slide 10 waveform is a separate 220 Hz harmonic teaching illustration
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

### 3. Song API

The script `site/week06/examples/request_song.py` is an instructor reference and local
preview. Teach the compact payload and states in class rather than asking
students to understand the whole defensive client in one sitting.

Default command, with no credential or network request:

```bash
python request_song.py \
  --prompt "Gentle ambient piano, warm strings, slow pulse" \
  --title "Evening" --instrumental \
  --duration-seconds 30 --weirdness 25 --style-influence 70
```

The client implements the verified sequence: one POST submission; bounded
latest-attempt polling with identity checks; per-track polling; remote download
preparation; authenticated same-origin content download. It saves every returned
track and preserves the actual encoding rather than naming any bytes `.wav`.

`--send` deliberately opts into a real generation and can spend credits.
The teacher configures `EASEL_BASE_URL` and `EASEL_API_KEY` in the environment
before using `--send`. The latter is the configured Easel bearer key; the operator's
upstream Suno token is separate. This differs from Week 5's `EASEL_KEY` script
convention. Never print, project or commit credentials.

Easel's server-side `dry_run: true` is **not** offline. It contacts the backend
and fills the native form. The teaching script's default preview is intentionally
different. It does not set that flag or call the server.

No current `easel-cli` song command was found; do not teach an invented CLI
subcommand. See the pinned Easel documentation in `site/week06/examples/TEACHER_NOTES.md` for
all fields and endpoint details. The live service, account controls and exact
generated duration remain unverified. The local tests use fake responses.

### 3a. Local speech models

Slides 29–31 link to `speech.html`. In the separate PFAD speech environment,
run the Kokoro example with a short interface cue, then transcribe its saved WAV.
Keep the script, settings, audio and proposed transcript together. Change only
speech speed and compare the result. Do not assume a familiar sentence will be
pronounced or transcribed perfectly.

The explicit microphone mode captures a bounded amount of local sound and sends
5-second chunks to a local faster-whisper model. Its output can lag and the chunk
boundaries can cut words. It is not a native streaming decoder. Only record
consenting participants, point out Ctrl+C before starting, and use the WAV input
if microphone permission or the device fails. No recording or model loading
occurs just by opening the slides or exercise page.

Kokoro writes at 24 kHz. The transcription file decoder resamples to 16 kHz;
changing a rate label alone would change the perceived speed and pitch. The
transcript is a model prediction. Compare it with the source, including pauses
and silence. Do not treat it as a verbatim record without checking.

KittenTTS is a separately versioned optional comparison in the linked notes.
Keep its legacy lightweight model distinct from the current, larger KittenTTS 2.
These scripts add no assignment requirement. Runtime model quality, installation
and microphone behavior still need a classroom preflight.

### 4. Strudel live coding, then Easel

Begin in strudel.cc with the already-present starter or an existing example
selected by the instructor. Play, change one visible value, Update, and Stop.
No specific third-party song is copied into this repository. Tutorial video:
pending the instructor's exact link; the current lesson does not guess one.

Use slides 37–40 in order. Each opens a complete cumulative score. The next
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

For Easel, create a fresh project and a fresh Strudel sound template in the
current client. Paste the same complete score, then the student presses Run.
Ask the agent to make the melody more spacious while preserving the other
three layers and tempo. Compare the actual code and sound with the prediction.
Use local native synths/drums; remote web sample packs are blocked by this kit.
If the installed client does not support the workflow, keep the website open
and paste the agent's suggested code there instead. No paid generation is needed.

Teacher/agent implementation notes, verified against current source:

- Inspect `window.EaselStrudel.getState().code` with `execute_canvas_javascript`.
- `setCode(source)` fills the buffer without evaluation. `evaluate(source)`
  compiles/updates on the existing clock, but does not start audio. The student
  supplies Run/Ctrl+Enter/Cmd+Enter. Keep `.play()` out of the score.
- A durable live change patches instance `app.js` `DEFAULT_LIVE_CODE` with
  `reload:false`, verifies the save, then evaluates the same full score. Runtime
  edits alone do not create source history. Repair a bad saved default too.
- A source-only save leaves WAV export gated until reload. Reload stays silent;
  press Run again. Stop/Escape/Ctrl+. silences the Easel template including tails.
- Export WAV renders 1–16 cycles, up to 30 seconds including a 0.5-second tail;
  stereo 48 kHz PCM16. It supports a bounded subset, not every live effect or
  sample transformation. The starter stays deliberately simple. At this tempo,
  one cycle plus tail is 2.9 seconds. Save/reopen the result in Media to check it.

The 18-minute making block includes four minutes of pair review. Keep a before
and after score plus one sentence explaining the change. This is formative,
not a new assessed deliverable. Students can inspect the visual code/feedback
without listening. Slides 32–33 use the original grid sequencer to illustrate
one click, one state change and one scheduled note before Strudel.

### Verification and classroom limits

The standard-library noise and tone examples were executed and their WAV
headers/sample values checked. Speech tests use model and device substitutes;
actual synthesis, transcription and microphone capture were not run. Song API tests use mocked responses; no live generation or credentials
were used. Easel's editing and export behavior is verified from the pinned
source and test assertions, not from the instructor's installed client.

The public Strudel editor was checked in the cloud browser: the default starter
loaded and its Play/Stop controls changed state. The four-layer encoded link
loaded the exact score. Its subsequent Play click was not completed because
the cloud browser permission request was dismissed before a decision; it was
not retried. Browser/device audibility and the classroom output route
still require listening. The local deck's Web Audio Play/Stop/Escape/navigation
checks await a reachable HTML preview. The offline mock-Web-Audio test
(`node tests/week06_audio_lifecycle.test.cjs`) checks silent load, Play,
parent slide-stop messages, visibility stop and stopping while startup awaits
a resume. This is control-flow evidence, not a browser audio check.

## Assessment wording to preserve

Dates come from the current course materials; the quiz format and 15-point
assignment value also use the instructor briefing supplied for this draft.

- Quiz: Thursday 22 October 2026; open-book, timed, multiple choice. Question
  count and duration remain unconfirmed. Do not imply AI permission from open-book.
- Assignment 3: an interactive experience, 15 points; Sunday 1 November 2026,
  23:59 Hong Kong time. Detailed rubric weights and submission instructions are
  separate. No audio requirement is added here.
- No assessed quiz bank is included. The existing mock is opened directly for practice; its questions and answers are not published here.

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
