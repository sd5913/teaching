"""Optional local speech models, separate from the song-generation service."""
from deckgen.layouts import content, code_panel

WHISPER = 'https://github.com/SYSTRAN/faster-whisper/blob/v1.2.1/README.md'
KOKORO = 'https://huggingface.co/hexgrad/Kokoro-82M'


def speech_slides():
    return [
        content('03 · SPEECH AND REPRESENTATION', 'Words can become sound, and sound can become words', [
            'Text-to-speech: a sentence becomes an audio waveform.',
            'Speech-to-text: recorded sound becomes a proposed transcript.',
            'Try one spoken interface cue, then inspect its transcription.',
            '[Open the Python speech exercise](speech.html)',
        ], notes='Seven-minute instructor comparison. The optional PFAD Python examples use local model inference: '
            'Kokoro for speech synthesis and faster-whisper for transcription. Setup and initial model downloads '
            'happen before class in a separate Python 3.12 environment. No account or classroom API is required. '
            'These models do not perform inverse operations: a transcript discards timbre and timing, and a '
            'synthetic voice chooses pronunciation and prosody. Keep Strudel making time and the existing mock slot.'),
        code_panel('03 · TEXT TO SPEECH', 'Kokoro saves a spoken cue', [
            'cd week06/speech',
            'uv run --no-project synthesise.py \\',
            '  --text "Your file is ready." \\',
            '  --speed 1.0 --out out/cue.wav',
            '',
            '# Keep the first file. Try a new speed:',
            '# --speed 0.85 --out out/cue-slower.wav',
        ], lang=None, caption='Kokoro 0.9.4 · preset synthetic voice · 24,000 samples/s · no autoplay',
            notes='Run after the linked PFAD setup, from that repository root. The script retains all generated '
            'chunks and saves a mono PCM WAV with settings. Prediction: does a slower cue feel clearer or more '
            'interruptive? Keep the text and voice fixed. Model speed is a synthesis control, not a guarantee of '
            'exact duration. First use downloads weights and language resources. CPU execution and espeak-ng '
            'need preflight. Model inference has not been run for this addition; source APIs and offline tests '
            'are the evidence. Sources: https://pypi.org/project/kokoro/0.9.4/ and ' + KOKORO),
        code_panel('03 · SPEECH TO TEXT', 'Whisper prints a proposed transcript', [
            '# No microphone: inspect the saved cue',
            'uv run --no-project transcribe.py \\',
            '  --audio out/cue.wav --out out/cue.txt',
            '',
            '# With consent: three 5-second microphone chunks',
            'uv run --no-project transcribe.py --microphone \\',
            '  --chunks 3 --seconds 5 --out out/mic.txt',
        ], lang=None, caption='Chunked near-live output can lag or cut words. Ctrl+C stops the demo.',
            notes='Continue in PFAD week06/speech. faster-whisper 1.2.1 runs base.en on CPU with int8. '
            'File input is decoded and resampled to mono 16 kHz; do not relabel 24 kHz samples as 16 kHz. '
            'The microphone captures continuously for a finite window, while the model processes queued chunks. '
            'This is near-live chunking, not a native streaming recognizer. Five-second boundaries can cut words '
            'and slow CPUs add delay. Only record yourself or consenting people; no recording starts from these '
            'slides. Compare every transcript with its source. Silence, noise, accents and unfamiliar words can '
            'produce errors or hallucinated text. Microphone and inference runtime remain untested here. ' + WHISPER),
    ]
