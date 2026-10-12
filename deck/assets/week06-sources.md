# Source notes for the Week 6 draft

Read-only source refresh: 12 October 2026. All three course repository heads
matched the earlier supplied commits.

## Reused course materials

- [SD5913 Week 5 deck](https://github.com/sd5913/teaching/blob/dd8e30ed640af73008f283fd6cbcca9167fc3735/deck/week05.py)
  provides the course typography, teaching voice and image-to-API progression.
- [SD5913 Week 5 figures](https://github.com/sd5913/teaching/blob/dd8e30ed640af73008f283fd6cbcca9167fc3735/deck/week05_figures.py)
  supplies the unchanged RGB pixel grid on slide 4.
- [PFAD Week 5 examples](https://github.com/sd5913/pfad/tree/11252caa6ee6e34937fc3314b396e944be6bdf7d/week05)
  ground the seeded-noise, array-shape and offline API-preview parallels.
- [SD2112 Week 6 deck](https://github.com/venetanji/sd2112-teaching/blob/558d1d77ce6b0e42c2e9ec955ca191d40cb7976e/deck/week06.py)
  supplies the reused sequencer JavaScript.
- [SD2112 Week 6 figures](https://github.com/venetanji/sd2112-teaching/blob/558d1d77ce6b0e42c2e9ec955ca191d40cb7976e/deck/week06_figures.py)
  supplies the unchanged waveform, spectrum/waterfall still, spectrogram and
  four-voice score illustrations.
- [SD2112 live analysis](https://github.com/venetanji/sd2112-teaching/blob/558d1d77ce6b0e42c2e9ec955ca191d40cb7976e/deck/week06_analysis.js)
  supplies the unchanged p5 / Web Audio instrument.

The sound figures are computed teaching illustrations. They are not recordings,
measured FFT captures or generated song outputs. In the spectrogram explanation,
the adjacent panels illustrate representations rather than one numerical
transformation of a single signal. All source attribution remains in the notes.

## Technical references

- [Python 3.12 wave](https://docs.python.org/3.12/library/wave.html)
- [Python 3.12 struct](https://docs.python.org/3.12/library/struct.html)
- [Web Audio AnalyserNode](https://webaudio.github.io/web-audio-api/#AnalyserNode)
- [Easel audio API at inspected commit](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/AUDIO_API.md)
- [Easel request schema and routes](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/easel/audio_api.py)
- [Inspected Easel CLI](https://github.com/venetanji/easel-cli/blob/ba2400ce22f1a4c9da4d6f5d2855aee309d7ffd9/src/easel_cli/client.py)

`site/week06/examples/TEACHER_NOTES.md` records the full verified API contract and limits.
These references support the source behavior. They do not verify the current
classroom deployment, account access, credits or generated audio quality.

## Format

The draft preserves the course's Python spec and pinned
[`ait4x/deckgen@v0.11.2`](https://github.com/ait4x/deckgen/tree/v0.11.2).
The installed revision used for this build was
`9990546c01865807e6aaac5aaa50977b4b6b916a`.

## Live-coding revision

- [Strudel first sounds](https://strudel.cc/workshop/first-sounds/) and
  [first notes](https://strudel.cc/workshop/first-notes/): cycles, rests, layers,
  native oscillators and editor controls.
- [Easel Strudel workflow](https://github.com/venetanji/easel-client/blob/d8dda0f1b953136ee7fc827eeeb39104471770b4/docs/strudel.md)
  and [compatibility](https://github.com/venetanji/easel-client/blob/d8dda0f1b953136ee7fc827eeeb39104471770b4/docs/strudel-compatibility.md):
  user-started Run, agent buffer/evaluation bridge, durable source saves,
  fresh-project kit pins and bounded WAV export.

The four cumulative scores are original teaching examples. No third-party song
is transcribed or packaged. The website starter is used through its own editor.
No tutorial video is identified yet. Keep that slot pending until the instructor
supplies the exact selection.
