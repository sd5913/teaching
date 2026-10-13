# Source notes for the Week 6 draft

Read-only source refresh: 12 October 2026. All three course repository heads
matched the earlier supplied commits.

## Reused course materials

- [SD5913 Week 5 deck](https://github.com/sd5913/teaching/blob/dd8e30ed640af73008f283fd6cbcca9167fc3735/deck/week05.py)
  provides the course typography, teaching voice and image-to-API progression.
- [SD5913 Week 5 figures](https://github.com/sd5913/teaching/blob/dd8e30ed640af73008f283fd6cbcca9167fc3735/deck/week05_figures.py)
  supplies the unchanged RGB pixel grid on slide 8.
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

## Original physical-sound opening, 13 October 2026

The 2025 SD5913 Week 6 PDF in the local reference archive, pp. 24–28, introduces
sound as mechanical energy, air-pressure oscillation, a sequence of numbers and
a time-domain waveform. Pages 29–31 show separate FFT, frequency and spectrogram
visuals. The 2026 air-particle and microphone-pressure diagrams are newly drawn
schematics, not scans from that PDF or traces from a real microphone. The new
browser sound lab generates two finite, 2-second sample buffers locally using
Web Audio; its graph shows those buffer values. The existing browser analyser
measures its own oscillator output, not air pressure or a classroom recording.

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

## Speech examples, 13 October 2026

The speech extension uses official source documentation for
[faster-whisper 1.2.1](https://github.com/SYSTRAN/faster-whisper/blob/v1.2.1/README.md),
[Kokoro 0.9.4](https://pypi.org/project/kokoro/0.9.4/),
[Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M), and
[sounddevice 0.5.3](https://python-sounddevice.readthedocs.io/en/0.5.3/usage.html).
The separate Python 3.12 environment avoids the PFAD Week 4 Worker project.

The microphone example uses bounded continuous capture and processes short
chunks with faster-whisper. This is near-live chunking, not a native streaming
decoder. Recording can finish before slow inference does. File decoding
resamples audio; sample-rate relabelling would be incorrect. Models and real
microphone inference were not run while preparing these additions.

The linked comparison uses the official projects for
[Piper](https://github.com/OHF-Voice/piper1-gpl),
[Chatterbox](https://github.com/resemble-ai/chatterbox),
[Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS), and
[KittenTTS](https://github.com/KittenML/KittenTTS).
It distinguishes Kitten's legacy 0.8.1 API/mini-0.8 model from KittenTTS 2.
No shared model benchmark or blanket commercial-use claim is made.

## Console-to-browser speech revision

The 2025 Week 6 PDF pp. 38–43 links speech tools and poses asynchronous
microphone-loopback questions (also tutorial p. 49); it contains no runnable
WebRTC or voice agent. Week 7 PDF pp. 15–17 introduces text agents; Week 9
PDF pp. 33, 39, 46 and 56 discusses WebRTC/WebSockets, Speaches and a PyAudio
transcription exercise separately.
The separate [legacy PFAD Week 9 README](https://github.com/venetanji/pfad/blob/7eb4077d508866ce0d95bbbd489ee64e9badb78b/week09/README.md)
describes a Streamlit WebRTC transcription app and a faster-whisper service, but
the named `speech_to_text_webrtc.py` and Compose file were never committed.
The canonical 2025 branch [ERRATA.md](https://github.com/sd5913/pfad/blob/512edb07927c5d77cacc7279ba6be601b33dc601/ERRATA.md)
documents that false lead and its [revised Week 9 README](https://github.com/sd5913/pfad/blob/512edb07927c5d77cacc7279ba6be601b33dc601/week09/README.md)
lists only tracked files. The [console WebSocket example](https://github.com/sd5913/pfad/blob/512edb07927c5d77cacc7279ba6be601b33dc601/week09/simple_audio_transcription.py)
requires a separate local realtime server; its callback writes to an asyncio
queue from another thread, so it is not the tested class path. The [Week 7 text
agent example](https://github.com/sd5913/pfad/blob/512edb07927c5d77cacc7279ba6be601b33dc601/week07/3_graph_agent.py)
and legacy Docker chatbot are separate, not wired voice-response pipelines.

For 2026 the console stage links the actual PFAD draft's bounded
`transcribe.py`; the teacher-only browser stage is new original code under
`site/week06/examples/speech_webrtc.py`. Its optional UI follows the
[streamlit-webrtc audio receiver example](https://github.com/whitphx/streamlit-stt-app/blob/main/app_deepspeech.py)
and the [Streamlit WebRTC library](https://github.com/whitphx/streamlit-webrtc),
using local faster-whisper inference rather than a hosted service. Model,
microphone, Streamlit/WebRTC installation and local Ollama reply are not
preflighted on the teaching device. A static slide preview is not the live app.
