"""Speech path: a finite console transcript becomes a consented WebRTC interaction."""
from deckgen.layouts import content, code_panel, figure_slide
import week06_figures as F

WHISPER = 'https://github.com/SYSTRAN/faster-whisper/blob/v1.2.1/README.md'
KOKORO = 'https://huggingface.co/hexgrad/Kokoro-82M'


def speech_slides():
    return [
        content('05 · SPEECH · TWO DIRECTIONS', 'Words can become sound, and sound can become words', [
            'Speech-to-text: captured sound becomes a proposed transcript.',
            'An interface needs a correction step before it responds.',
            'Text-to-speech can turn an approved reply into a spoken cue.',
            '[Open the local speech exercise](speech.html)',
        ], notes='Speech is separate from the Strudel/music API block. The same small faster-whisper '
            'recognizer powers a PFAD Python console exercise and an optional teacher-run local '
            'Streamlit WebRTC app. They do not infer intent from a voice alone. The transcript is '
            'an uncertain model prediction; a person checks it before an optional response. '
            'Kokoro is a separate text-to-speech extension, not an automatic voice loop. '
            'Pre-download models; the browser WebRTC app itself is not hosted by this static deck.'),
        code_panel('05 · SPEECH · CONSOLE', 'Speak into Python. Check each chunk.', [
            'cd week06/speech',
            'uv run --no-project transcribe.py --microphone \\',
            '  --chunks 3 --seconds 5 --out out/mic.txt',
            '',
            '# No device? Read a consented local WAV:',
            'uv run --no-project transcribe.py \\',
            '  --audio out/cue.wav --out out/cue.txt',
        ], lang=None, caption='Start deliberately. Three 5-second chunks, then stop; Ctrl+C can stop early.',
            notes='This is the PFAD PR #8 Python 3.12 exercise, after installing and preflighting '
            'its pinned local faster-whisper model. It records from the instructor laptop, '
            'not from a web browser. `sounddevice` supplies 16 kHz mono frames into a bounded '
            'queue and base.en (CPU/int8) produces a proposed line for each chunk. Capture '
            'ends after 15 seconds but inference may lag. Only record yourself or consenting '
            'people. A supplied WAV is the no-microphone fallback. No live inference or '
            'microphone was tested while authoring this draft. Source: ' + WHISPER),
        figure_slide('05 · SPEECH · CHANGE THE CAPTURE PATH',
            'One recognizer, two microphone paths', F.w06_speech_pipeline(),
            caption='WebRTC transports browser audio; it is not a different speech recognizer.',
            notes='A local console microphone is read by sounddevice. A browser microphone '
                'instead needs a user START/permission gesture and WebRTC transport to '
                'the local Streamlit process. Both paths convert to mono 16 kHz before '
                'using finite chunks with faster-whisper base.en. The console example '
                'uses five seconds per chunk, this optional browser app uses three; '
                'neither promises word-level real-time text. The CHECK box is human '
                'review before an optional local model reply. This is an original '
                'architecture diagram, not a tested screenshot of the 2025 app.'),
        code_panel('05 · SPEECH · BROWSER TRANSPORT', 'The same transcript moves into the browser', [
            '# optional instructor app, local Python 3.12',
            'uv venv --python 3.12 .venv-webrtc',
            'uv pip install --python .venv-webrtc/bin/python \\',
            '  -r speech_webrtc_requirements.txt',
            '.venv-webrtc/bin/python -m streamlit run \\',
            '  speech_webrtc.py --server.address 127.0.0.1',
            '',
            '# Open localhost:8501, click START, then STOP.',
        ], lang=None, caption='Local Streamlit WebRTC, not an embed in the static slides. Prepare model and mic first.',
            notes='The local example is downloadable from speech.html; run it only on the '
            'instructor machine with a pre-cached base.en model. The browser asks permission '
            'after START and sends a WebRTC audio track to a local Streamlit process. '
            'The process converts audio frames to mono 16 kHz and applies the same '
            'transcribe() settings as the console example in short finite chunks. '
            'This is chunked near-live output, not word-level streaming. A localhost '
            'page has a secure browser context; a remote URL needs HTTPS and network '
            'configuration (possibly TURN). A static Pages preview cannot execute '
            'Python inference. If the device or model fails, show the file transcript '
            'instead. Do not point the class at an untested public server.'),
        content('05 · SPEECH · RESPONSE', 'A response begins with a checked transcript', [
            'Listen or inspect the proposed words. Correct errors first.',
            'Only after review: explicitly ask a local Ollama model for a short text reply.',
            'Show both the transcript and the reply. Which errors would change the intent?',
            'Press STOP to close browser capture; do not forward private speech by default.',
        ], notes='The browser app displays chunked results and lets the instructor edit the '
            'transcript after capture stops. Its Ask local model button is disabled '
            'until a nonempty corrected text exists. It contacts only 127.0.0.1:11434 '
            'on deliberate click; no paid account or external speech upload is configured. '
            'Ollama and the qwen3:4b model are optional local dependencies that were not '
            'inference-tested here. If unavailable, trace the transcript-to-reply '
            'boundary or let students write a response by hand. This is not a verified '
            'autonomous voice agent and does not speak its reply automatically.'),
        code_panel('05 · SPEECH · OPTIONAL VOICE', 'Kokoro saves a spoken cue', [
            'cd week06/speech',
            'uv run --no-project synthesise.py \\',
            '  --text "Your file is ready." \\',
            '  --speed 1.0 --out out/cue.wav',
            '',
            '# Keep the first file. Try a new speed:',
            '# --speed 0.85 --out out/cue-slower.wav',
        ], lang=None, caption='A separate text-to-speech exercise; not automatic agent speech.',
            notes='Run after the linked PFAD setup, from its speech directory. The script '
            'retains all generated chunks and saves a mono 24 kHz PCM WAV with settings. '
            'Use a preset synthetic voice and review before playing. First use downloads '
            'weights and language resources; CPU execution and espeak-ng need preflight. '
            'This is a later extension of the response path, not a working voice agent. '
            'Source: https://pypi.org/project/kokoro/0.9.4/ and ' + KOKORO),
    ]
