"""Offline contracts for the optional local, browser-microphone teacher demo."""
from array import array
import importlib.util
from pathlib import Path
import unittest

FILE = Path(__file__).resolve().parents[1] / 'site/week06/examples/speech_webrtc.py'


def app():
    spec = importlib.util.spec_from_file_location('speech_webrtc', FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SpeechWebrtcTests(unittest.TestCase):
    def test_resampled_pcm_makes_bounded_float_chunks(self):
        module = app()

        class Frame:
            def __init__(self, values):
                self.values = values

            def to_ndarray(self):
                return self

            def tobytes(self):
                return array('h', self.values).tobytes()

        class Resampler:
            def resample(self, frame):
                return [frame]

        chunker = module.AudioChunker(Resampler(), seconds=1)
        self.assertEqual(chunker.push(Frame([16384] * 8000)), [])
        chunks = chunker.push(Frame([-16384] * 10000))
        self.assertEqual(len(chunks), 1)
        self.assertEqual(len(chunks[0]), 16000)
        self.assertAlmostEqual(chunks[0][0], 0.5)
        self.assertAlmostEqual(chunks[0][-1], -0.5)
        self.assertEqual(chunker.pending_samples, 2000)

    def test_reply_requires_checked_text_and_fixed_loopback_destination(self):
        module = app()
        calls = []

        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self, size):
                self.size = size
                return b'{"message":{"content":"Please check the saved file."}}'

        def transport(request, timeout):
            calls.append((request, timeout))
            return Response()

        with self.assertRaises(ValueError):
            module.ask_local_model('  ', transport=transport)
        self.assertEqual(calls, [])
        reply = module.ask_local_model('Did the file save?', transport=transport)
        self.assertEqual(reply, 'Please check the saved file.')
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][0].full_url, 'http://127.0.0.1:11434/api/chat')
        self.assertLessEqual(calls[0][1], 12)
        self.assertIn(b'Did the file save?', calls[0][0].data)


if __name__ == '__main__':
    unittest.main()
