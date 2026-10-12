"""Offline contract tests: fake transport and clock; no credentials or credits."""
import contextlib
import http.client
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / "site/week06/examples" / "request_song.py"
song = None
if MODULE.exists():
    spec = importlib.util.spec_from_file_location("request_song", MODULE)
    song = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(song)

ATTEMPT = "69d70c38-6802-4281-a0ae-fb6f8473f715"
OTHER = "c20ec236-e950-4f1c-9bb6-e51cb584b34d"
TRACK = "a8627b92-354b-40d9-a50e-ab241e4fb3a1"
PATH = "/v1/audio/tracks/" + TRACK
STATUS = "/v1/audio/generations/status"
SUBMIT = "/v1/audio/generations"


class FakeClock:
    def __init__(self):
        self.now = 0

    def time(self):
        return self.now

    def sleep(self, seconds):
        self.now += seconds


class FakeClient:
    def __init__(self, steps):
        self.steps = list(steps)
        self.calls = []

    def json(self, method, path, payload=None):
        self.calls.append((method, path, payload))
        expected_method, expected_path, result = self.steps.pop(0)
        if (method, path) != (expected_method, expected_path):
            raise AssertionError((method, path, expected_method, expected_path))
        if isinstance(result, Exception):
            raise result
        return result

    def content(self, path):
        return self.json("GET", path)


class RequestSongTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(song, "The offline teaching client has not been implemented yet")
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.output = Path(self.directory.name)
        self.clock = FakeClock()

    def run_flow(self, client, wait_seconds=30):
        with contextlib.redirect_stdout(io.StringIO()):
            return song.generate_and_save(
                client, song.build_payload("Warm piano", instrumental=True), self.output,
                wait_seconds=wait_seconds, clock=self.clock.time, sleep=self.clock.sleep,
            )

    def test_offline_default_never_constructs_client_or_reads_key(self):
        class UnreadableEnvironment(dict):
            def get(self, name, default=None):
                if name.startswith("EASEL_"):
                    raise AssertionError("Offline preview must not read connection credentials")
                return default  # argparse/gettext may inspect locale variables.

        output = io.StringIO()
        with patch.object(song, "Client", side_effect=AssertionError("Network forbidden")), \
             patch.object(song.os, "environ", UnreadableEnvironment()), \
             contextlib.redirect_stdout(output):
            self.assertEqual(song.main(["--prompt", "Warm piano", "--instrumental"]), 0)
        text = output.getvalue()
        self.assertNotIn("DO-NOT-PRINT", text)
        self.assertIn('"model": "suno-music"', text)
        self.assertNotIn('"dry_run"', text)

    def test_supported_custom_payload(self):
        payload = song.build_payload("Warm piano", title="Evening", instrumental=True,
                                     duration_seconds=30, weirdness=25, style_influence=70)
        self.assertEqual(payload, {"model": "suno-music", "prompt": "Warm piano",
                                  "title": "Evening", "make_instrumental": True,
                                  "duration_seconds": 30, "weirdness": 25,
                                  "style_influence": 70})

    def test_validation_rejects_invalid_music_before_network(self):
        cases = [(" ", {}), ("x" * 1001, {}), ("Piano", {"lyrics": "x" * 5001}),
                 ("Piano", {"lyrics": "Hello", "instrumental": True}),
                 ("Piano", {"weirdness": 101}), ("Piano", {"style_influence": -1}),
                 ("Piano", {"duration_seconds": 9}), ("Piano", {"duration_seconds": 361}),
                 ("Piano", {"weirdness": True})]
        for prompt, options in cases:
            with self.subTest(options=options), self.assertRaises(song.SongError):
                song.build_payload(prompt, **options)
        self.assertEqual(song.build_payload("", lyrics="Hello")["lyrics"], "Hello")

    def test_pending_then_track_complete_saves_actual_encoding(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "pending", "attempt_id": ATTEMPT}),
            ("GET", STATUS, {"status": "submitted", "attempt_id": ATTEMPT,
                              "songs": [{"id": TRACK, "status": "queued"}]}),
            ("GET", PATH, {"id": TRACK, "status": "complete"}),
            ("POST", PATH + "/download", {"song_id": TRACK, "filename": "song.m4a",
                                           "format": "m4a", "size": 5}),
            ("GET", PATH + "/content", b"AUDIO"),
        ])
        files = self.run_flow(client)
        self.assertEqual(files, [self.output / "song.m4a"])
        self.assertEqual(files[0].read_bytes(), b"AUDIO")
        self.assertEqual(client.steps, [])
        self.assertEqual(sum(method == "POST" and path == SUBMIT
                             for method, path, _ in client.calls), 1)

    def test_already_complete_submission_downloads_without_status_poll(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "complete", "attempt_id": ATTEMPT,
                               "songs": [{"id": TRACK, "status": "complete"}]}),
            ("POST", PATH + "/download", {"filename": "song.m4a", "size": 5}),
            ("GET", PATH + "/content", b"AUDIO"),
        ])
        self.assertEqual(len(self.run_flow(client)), 1)

    def test_id_only_song_entry_fetches_individual_track_before_deciding(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "submitted", "attempt_id": ATTEMPT,
                               "songs": [{"id": TRACK}]}),
            ("GET", PATH, {"id": TRACK, "status": "complete"}),
            ("POST", PATH + "/download", {"filename": "song.m4a", "size": 5}),
            ("GET", PATH + "/content", b"AUDIO"),
        ])
        files = self.run_flow(client)
        self.assertEqual(files[0].read_bytes(), b"AUDIO")
        self.assertEqual(client.steps, [])

    def test_shared_pending_attempt_blocks_submission(self):
        client = FakeClient([("GET", STATUS, {"status": "pending", "attempt_id": OTHER})])
        with self.assertRaisesRegex(song.SongError, "shared"):
            self.run_flow(client)
        self.assertFalse(any(method == "POST" for method, _, _ in client.calls))

    def test_unknown_shared_status_blocks_submission(self):
        for state in ({}, {"status": "new-unknown-state"}):
            client = FakeClient([("GET", STATUS, state)])
            with self.subTest(state=state), self.assertRaisesRegex(song.SongError, "shared"):
                self.run_flow(client)
            self.assertEqual(len(client.calls), 1)

    def test_replaced_attempt_is_never_accepted(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "pending", "attempt_id": ATTEMPT}),
            ("GET", STATUS, {"status": "submitted", "attempt_id": OTHER,
                              "songs": [{"id": TRACK, "status": "complete"}]}),
        ])
        with self.assertRaisesRegex(song.SongError, "another attempt"):
            self.run_flow(client)
        self.assertEqual(list(self.output.iterdir()), [])

    def test_captcha_stops_without_retry_or_automatic_abandon(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "captcha_required", "attempt_id": ATTEMPT}),
        ])
        with self.assertRaisesRegex(song.SongError, "CAPTCHA"):
            self.run_flow(client)
        self.assertEqual(len(client.calls), 2)

    def test_submission_transport_failure_is_not_retried(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, song.SongError("Ambiguous timeout; inspect status")),
        ])
        with self.assertRaisesRegex(song.SongError, "Ambiguous"):
            self.run_flow(client)
        self.assertEqual(len(client.calls), 2)

    def test_track_error_stops_before_save(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "submitted", "attempt_id": ATTEMPT,
                               "songs": [{"id": TRACK, "status": "queued"}]}),
            ("GET", PATH, {"id": TRACK, "status": "error"}),
        ])
        with self.assertRaisesRegex(song.SongError, "Track failed"):
            self.run_flow(client)

    def test_pending_polling_is_bounded(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "pending", "attempt_id": ATTEMPT}),
        ])
        with self.assertRaisesRegex(song.SongError, "Timed out"):
            self.run_flow(client, wait_seconds=2)
        self.assertEqual(self.clock.now, 2)
        self.assertEqual(len(client.calls), 2)

    def test_unsafe_server_filename_is_rejected(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "complete", "attempt_id": ATTEMPT,
                               "songs": [{"id": TRACK, "status": "complete"}]}),
            ("POST", PATH + "/download", {"filename": "../outside.m4a", "size": 5}),
        ])
        with self.assertRaisesRegex(song.SongError, "filename"):
            self.run_flow(client)

    def test_size_mismatch_does_not_write_audio(self):
        client = FakeClient([
            ("GET", STATUS, {"status": "idle"}),
            ("POST", SUBMIT, {"status": "complete", "attempt_id": ATTEMPT,
                               "songs": [{"id": TRACK, "status": "complete"}]}),
            ("POST", PATH + "/download", {"filename": "song.m4a", "size": 99}),
            ("GET", PATH + "/content", b"AUDIO"),
        ])
        with self.assertRaisesRegex(song.SongError, "size"):
            self.run_flow(client)
        self.assertEqual(list(self.output.iterdir()), [])

    def test_transport_rejects_unsafe_urls_before_opening(self):
        with patch.object(song.urllib.request, "build_opener") as opener:
            client = song.Client("https://example.invalid", "secret")
            for path in ("https://evil.invalid/audio", "//evil.invalid/audio",
                         "/v1/\\evil", "/v1/audio\nInjected: yes"):
                with self.subTest(path=path), self.assertRaises(song.SongError):
                    client.json("GET", path)
            opener.return_value.open.assert_not_called()
        with self.assertRaises(song.SongError):
            song.Client("http://example.invalid", "secret")

    def test_redirect_handler_refuses_to_forward_credentials(self):
        handler = song.NoRedirect()
        self.assertIsNone(handler.redirect_request(None, None, 302, "Found", {},
                                                    "https://evil.invalid"))

    def test_http_error_message_does_not_leak_credentials(self):
        error = song.urllib.error.HTTPError("https://example.invalid", 401, "bad", {},
                                           io.BytesIO(b'{"error":{"message":"secret"}}'))
        with patch.object(song.urllib.request, "build_opener") as opener:
            opener.return_value.open.side_effect = error
            client = song.Client("https://example.invalid", "secret")
            with self.assertRaises(song.SongError) as caught:
                client.json("GET", STATUS)
            self.assertNotIn("secret", str(caught.exception))
            self.assertIn("401", str(caught.exception))

    def test_response_body_failures_keep_recovery_guidance(self):
        class BrokenBody:
            headers = {"Content-Type": "audio/mp4"}

            def __init__(self, error):
                self.error = error

            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self, *_):
                raise self.error

        for method in ("json", "content"):
            for error in (TimeoutError("secret"), http.client.IncompleteRead(b"secret", 50)):
                with self.subTest(method=method, error=type(error).__name__), \
                     patch.object(song.urllib.request, "build_opener") as opener:
                    opener.return_value.open.return_value = BrokenBody(error)
                    client = song.Client("https://example.invalid", "secret")
                    with self.assertRaisesRegex(song.SongError, "[Ii]nspect") as caught:
                        if method == "json":
                            client.json("POST", SUBMIT, {"prompt": "Piano"})
                        else:
                            client.content(PATH + "/content")
                    self.assertNotIn("secret", str(caught.exception))
                    self.assertEqual(opener.return_value.open.call_count, 1)

    def test_transport_encodes_verified_json_and_bearer_header(self):
        response = io.BytesIO(b'{"status":"idle"}')
        with patch.object(song.urllib.request, "build_opener") as opener:
            opener.return_value.open.return_value = response
            client = song.Client("https://example.invalid", "test-only-key")
            payload = song.build_payload("Piano", instrumental=True)
            self.assertEqual(client.json("POST", SUBMIT, payload), {"status": "idle"})
            request = opener.return_value.open.call_args.args[0]
            self.assertEqual(request.full_url, "https://example.invalid" + SUBMIT)
            self.assertEqual(request.get_header("Authorization"), "Bearer test-only-key")
            self.assertEqual(json.loads(request.data), payload)


if __name__ == "__main__":
    unittest.main()
