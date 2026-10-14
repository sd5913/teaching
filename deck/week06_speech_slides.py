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
            'Text-to-speech turns a reply into a spoken cue.',
            '[Open the local speech exercise](speech.html)',
        ], notes='Speech is separate from the Strudel/music API block. The same small faster-whisper '
            'recognizer powers a PFAD Python console exercise and an optional teacher-run local '
            'Streamlit WebRTC app. They do not infer intent from a voice alone. The transcript is '
            'an uncertain model prediction; a person checks it before an optional response. '
            'The portable bot combines LM Studio and Kokoro ONNX for spoken replies. '
            'Pre-download models; the browser WebRTC app itself is not hosted by this static deck.'),
        code_panel('05 · SPEECH · CONSOLE', 'Speak into Python. Check each chunk.', [
            '# From PFAD week06/speech, after console setup:',
            'uv run --no-project --python .venv/Scripts/python.exe transcribe.py',
            '  --microphone --chunks 3 --seconds 5 --out ../out/mic.txt',
            '',
            '# No device? Read a consented local WAV:',
            '# --audio ../out/onnx-hello.wav --offline',
            '# macOS/Linux: use .venv/bin/python instead.',
        ], lang=None, caption='Join the command into one line. Three 5-second chunks; Ctrl+C stops early.',
            notes='This is the PFAD PR #8 Python 3.12 exercise, after installing and preflighting '
            'its pinned local faster-whisper model and sounddevice/PortAudio dependencies. It records from the instructor laptop, '
            'not from a web browser. `sounddevice` supplies 16 kHz mono frames into a bounded '
            'queue and base.en (CPU/int8) produces a proposed line for each chunk. Capture '
            'ends after 15 seconds but inference may lag. Only record yourself or consenting '
            'people. A supplied WAV is the no-microphone fallback. Select the speech interpreter explicitly '
            'to avoid the root Week 4 project. Source: ' + WHISPER),
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
            '# From PFAD week06/speech, after portable setup:',
            'uv run --no-project --python .venv/Scripts/python.exe',
            '  python -m streamlit run speech_webrtc.py',
            '  --server.address 127.0.0.1 --browser.gatherUsageStats false',
            '',
            '# macOS/Linux: use .venv/bin/python instead.',
            '# Open localhost:8501; Start mic / Stop mic.',
        ], lang=None, caption='Join the command into one line. Full portable setup: speech.html.',
            notes='The local example is downloadable from speech.html; run it only on the '
            'instructor machine with pre-cached base.en and Kokoro ONNX models. Use '
            'conversation_requirements.txt and prepare_models.py in a Python 3.12 .venv. '
            'CPU is the default on Windows, Macs and AMD; NVIDIA CUDA is optional. '
            'LM Studio independently supports Metal on compatible Macs. The browser asks permission '
            'after Start mic and sends a WebRTC audio track to a local Streamlit process. '
            'The process converts audio frames to mono 16 kHz and applies the same '
            'transcribe() settings as the console example in short finite chunks. '
            'This is chunked near-live output, not word-level streaming. A localhost '
            'page has a secure browser context; a remote URL needs HTTPS and network '
            'configuration (possibly TURN). A static Pages preview cannot execute '
            'Python inference. If the device or model fails, show the file transcript '
            'instead. Do not point the class at an untested public server.'),
        content('05 · SPEECH · RESPONSE', 'A response begins with a checked transcript', [
            'Listen or inspect the proposed words. Correct errors first.',
            'Start mic: recognized words fill the editable chat box.',
            'Stop mic to correct the text, then press Enter to send.',
            'LM Studio replies; Kokoro ONNX speaks the reply.',
        ], notes='Capture continues in three-second chunks until Stop mic or Send. Sending '
            'also works during capture and stops the microphone before the reply. The '
            'instructor uses MiniCPM5-2B Q4_K_M in LM Studio on localhost:1234. Select '
            'the loaded model with Find loaded models in the sidebar. Text is sent '
            'only to the configured loopback server after Send. Microphone audio stays '
            'in memory; transcripts and reply audio remain in the session. Browser '
            'autoplay may need a Play click. Keep a typed-message route; if the model '
            'is unavailable, compare written responses. Follow PFAD CONVERSATION.md.'),
        code_panel('05 · SPEECH · OPTIONAL VOICE', 'Kokoro saves a spoken cue', [
            '# From PFAD week06/speech, after portable setup:',
            'uv run --no-project --python .venv/Scripts/python.exe',
            '  synthesise_onnx.py --text "Your file is ready."',
            '  --speed 1.0 --out ../out/cue.wav',
            '',
            '# Keep the first file. Try a new speed:',
            '# --speed 0.85 --out ../out/cue-slower.wav',
            '# macOS/Linux: use .venv/bin/python instead.',
        ], lang=None, caption='Join the command into one line. Kokoro ONNX: CPU default, 24 kHz output.',
            notes='Run after the linked PFAD setup, from its speech directory. The script '
            'retains all generated chunks and saves a mono 24 kHz PCM WAV with settings. '
            'Use a preset synthetic voice and review before playing. Prepare models '
            'once; existing files are reused. Kokoro ONNX needs no PyTorch or separate '
            'system espeak-ng install; espeakng-loader supplies the phonemizer. '
            'The older synthesise.py PyTorch route has separate dependencies. '
            'Recognition resamples 24 kHz output to 16 kHz. Source: '
            'https://github.com/sd5913/pfad/blob/2026/week06/speech/CONVERSATION.md'),
    ]
