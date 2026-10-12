# Easel song-request example: teacher notes

Verified 12 October 2026 against source, not a live deployment. No credentials were read and no generation requests were sent. The example is a local teaching artifact, not an easel-cli feature.

## Sources pinned to the inspected commits

- [Audio API documentation](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/AUDIO_API.md)
- [Request schemas, routes and URL rewriting](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/easel/audio_api.py)
- [Transport and error handling](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/easel/suno_client.py)
- [Easel authentication](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/easel/app.py#L69-L76)
- [Mocked API tests](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/tests/test_audio_api.py)
- [Opt-in integration example](https://github.com/venetanji/easel/blob/7c2a419e1eb2143a071d31ae45f2f105fcbf6b81/tests/test_audio_integration.py)
- [Current image-only CLI](https://github.com/venetanji/easel-cli/blob/ba2400ce22f1a4c9da4d6f5d2855aee309d7ffd9/src/easel_cli/client.py)

## Classroom flow

Teach: submit once → wait for confirmed song IDs → poll each track → save remotely → fetch the bytes.

The default example mode is an offline JSON preview. It neither reads credentials nor opens a connection. `--send` explicitly opts into a real generation that can consume credits. In contrast, the API's `dry_run: true` is online: it contacts the backend and fills the native browser form without clicking Create. It is deliberately not the example's default behavior.

From the teaching repository root, run this safe preview and the offline tests:

```sh
python site/week06/examples/request_song.py --prompt "Gentle ambient piano, warm strings, slow pulse" --title Evening --instrumental --duration-seconds 30 --weirdness 25 --style-influence 70
python -m unittest discover -s tests -p 'test_week06*.py' -v
```

If you downloaded only the examples, open that download folder and use
`python request_song.py` with the same options; the repository tests are not
part of that individual download.

A later, separately authorized real demonstration requires the operator-provided HTTPS server root in `EASEL_BASE_URL`, its key in `EASEL_API_KEY`, and the additional `--send` flag. No `.env` file is loaded by this example. Output defaults to `out/songs`; existing files are never overwritten. `--wait-seconds` bounds polling waits (default 300 seconds); each HTTP request separately times out after 180 seconds. Failed or unfinished generation can remain active after the script stops.

Easel uses a shared Suno browser, not a per-student queue. The status endpoint observes its latest attempt and loses state if the upstream service restarts. Serialize demonstrations; simultaneous class-wide generation is unsuitable. Capture `attempt_id`, refuse a mismatched latest attempt, and use track IDs once available. CAPTCHA can appear after submission; handle it manually, then resume polling, never resubmit to bypass it. This example stops with recovery guidance rather than solving or abandoning a CAPTCHA automatically.

Before a later authorized live demo, the teacher must verify service configuration, model discovery, account access, credits and manual CAPTCHA access. This research did not verify those deployment conditions. Keep API keys in environment variables, never slides, screenshots, source, output logs or committed files.

## Verified endpoints and responses

Every route uses `Authorization: Bearer EASEL_API_KEY` when the server has a key configured. `SUNO_REST_API_TOKEN` is a separate operator-side credential, not a student credential.

- `GET /v1/models`: adds `suno-music`, `suno-speech`, `suno-sound` when Suno is configured. These are routing IDs, not pinned model versions.
- `POST /v1/audio/generations`: Easel-specific JSON extension, not OpenAI's speech/TTS API. Music routes to Suno MCP/REST `/api/v1/generate/music`, not ComfyUI.
- Submission normally returns HTTP 202 for `pending`, `submitted`, or `captcha_required`, with `Location`, `Retry-After: 5`, `attempt_id`, `status_url`, and any known `songs`. Wrapper adds `object: audio.generation` and the routing `model`. Online dry runs return HTTP 200, `status: prepared`.
- `GET /v1/audio/generations/status`: latest shared attempt. Known statuses: `idle`, `pending`, `captcha_required`, `submitted`, `complete`, `error`, `abandoned`. The wrapper passes upstream diagnostics through; there is no rigid response schema guaranteeing every optional field. No `/status/{attempt_id}` route exists.
- `GET /v1/audio/tracks/{song_id}`: individual UUID track; wait for `status: complete`; `error` indicates failure. Mock tests also demonstrate `queued`.
- `POST /v1/audio/tracks/{song_id}/download`: saves playable audio in Suno's download volume. Response retains `song_id`, actual `filename`, `format`, `size`, and Easel-hosted `audio_url`/`download_url`, while removing backend paths and direct stream URLs.
- `GET /v1/audio/tracks/{song_id}/content`: authenticated bytes; 404 until remotely saved. Optional `?download=true` sets attachment disposition. Preserve actual encoding, e.g. `.m4a`, rather than forcing `.mp3`. This is authenticated-player audio, not native paid WAV/stem export.
- `POST /v1/audio/generations/abandon` with the exact `attempt_id`: explicit manual recovery for an unconfirmed attempt. It neither cancels accepted tracks nor refunds credits. The example does not call this automatically.

One generation may return multiple tracks; no exact count is promised. The example saves every returned track. Returned file URLs are not arbitrary download authority: use only authenticated same-origin paths, validate IDs, and reject redirects.

## Supported music request fields

`model` defaults to `suno-music`. `prompt` means style/description (up to 1,000 characters; mapped to upstream `tags`); `lyrics` up to 5,000; `title` string; `make_instrumental` boolean (default false); `negative_prompt` up to 1,000; `suno_model` exact native picker label (omit to leave current selection); `weirdness` and `style_influence` optional integers 0–100; `variety` optional integer 0–4; `vocal_gender` empty, `male`, or `female`; `duration_seconds` optional integer 10–360; `dry_run` boolean.

Reference controls: `reference_audio_id` UUID, `audio_mode` (`cover`/`extend`, default `cover`), `audio_influence` optional integer 0–100; or up to four unique UUID `inspiration_ids`, or `inspiration_playlist` string. Reference and inspiration cannot coexist; IDs and playlist cannot coexist. `audio_influence` requires reference audio. The API does not expose file uploads or automate rights confirmation.

Music requires nonblank prompt or lyrics. Instrumental plus nonblank lyrics is invalid. Unknown fields are rejected, including `seed`, `n`, `temperature`, and music `bpm`. Express tempo in the music prompt. Duration is a requested control, not a guaranteed exact length; native model/account capabilities still apply.

Other models have distinct fields: speech accepts prompt/script (1–5,000), tone (up to 1,000), background_music, vocal_gender, variety (0–4), dry_run. Sound accepts prompt (1–500), sound_type (`one_shot`/`loop`), optional bpm (1–300), dry_run. Do not copy music-only fields into these requests.

## Errors and recovery

Error envelope: `error.message`, `error.type`, `error.code`, `error.param`, plus optional recovery details.

- 400: invalid fields, ranges, UUIDs, combinations or unsupported model
- 401 `invalid_api_key`: missing/wrong Easel key
- 409 `generation_pending`: another unconfirmed submission; `error.generation` can identify it
- 429 `browser_queue_full` / 503 `browser_queue_timeout`: backpressure; `Retry-After` and `operation_started: false` may be returned
- 503 `audio_server_unavailable`: backend unconfigured/unavailable
- 504 `upstream_timeout` / `browser_operation_timeout`: possibly ambiguous submission
- 502 `upstream_error`, `upstream_auth_error`, `upstream_invalid_response`: connectivity, operator credential or response problem
- 404 `audio_not_downloaded`: remote save has not happened

Never automatically retry a generation POST after timeout, disconnect or error: it may already have spent credits. Inspect the latest attempt and the Suno library before deliberately submitting again. Preserve `attempt_id` and track IDs for recovery. The example has bounded polling and stops on ambiguity; a timeout is not proof the job failed.
