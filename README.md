# SD5913 · Programming for Artists and Designers — teaching repo

Slides and class planning for PolyU School of Design, Semester 1 2026/27.
Lecturer Giovanni Lion (giovanni.lion@polyu.edu.hk).

This repo holds **sources only**. The slide toolchain is not in here — it is
[`ait4x/deckgen`](https://github.com/ait4x/deckgen), pinned by tag in `requirements.txt`
and shared with `venetanji/sd2112-teaching`. A fix to the PowerPoint or ClassPoint
plumbing lands in both courses at once.

Two GitHub Actions workflows run on every push to `main` (and on demand):

| Workflow | What it makes | Where it goes |
|---|---|---|
| **Publish site** (`.github/workflows/site.yml`) | The html decks, a PDF of each without the ClassPoint buttons, the landing page. | GitHub Pages (Week 2: `/week02/`). |
| **Build PowerPoints** (`.github/workflows/pptx.yml`) | `week02.pptx` (plain), `week02-classpoint.pptx` (ait4x master, animations, live ClassPoint buttons), the activity manifest, `.docx` of anything in `syllabus/` and `lessons/`, preview sheets. | The `sd5913-powerpoints` artifact of the run, kept 90 days. Not published. |

## Layout

| Path | What |
|---|---|
| `deckgen.toml` | The course: code, name, year, footer, which decks, what gets published. |
| `deck/week02.py` | **Week 2 as one Python spec**: text, speaker notes, ClassPoint activities, in the order the class runs. Edit here; every output updates. |
| `deck/assets/` | Images. `deck/assets/generated/` is drawn at build time and git-ignored. |
| `lessons/` | Instructor run sheets. Built to `.docx` in the artifact, **not published**. |
| `syllabus/` | Published only if listed under `[[publish]]` in `deckgen.toml`. |
| `site/index.html` | The landing page. The reveal.js vendor bundle is added by the build. |
| `archive/` | The PowerPoint actually shown in class, per week, where it was not generated from `deck/`. Week 1 lives here — it was built by hand. |

Generated and git-ignored: `_site/`, `export/`, `deck/assets/generated/`, `node_modules/`.

## Build locally

```bash
uv venv && uv pip install -r requirements.txt
deckgen build --pptx          # export/: PowerPoints, manifest, docx, previews (no node needed)
deckgen build --site          # _site/: html decks, PDFs — needs node + playwright
deckgen build                 # both
deckgen build --no-pdf        # skip the Chromium step
```

The PDF step needs node 18+ and Playwright's Chromium:
`npm install --no-save playwright@1.56.1 && npx playwright install chromium`.
The html deck: arrow keys, `S` speaker notes, `O` overview, `F` full screen.

`deckgen build` **exits non-zero if any text overflows its box**, so a broken slide fails
the workflow rather than reaching the projector. Previews land in `export/preview/`.

## Classroom checklist

1. Download the PowerPoint from the latest *Build PowerPoints* run (Actions → Artifacts → `sd5913-powerpoints`).
2. Install Inter and JetBrains Mono on the classroom PC — they ship inside the `deckgen` package (`python -c "import deckgen, pathlib; print(pathlib.Path(deckgen.__file__).parent / 'fonts')"`). Restart PowerPoint. Slide 1 should show *Inter Black* in the font box; Arial substitutes automatically if not.
3. Open the deck with the ClassPoint add-in and fire one activity before class — a malformed tag fails silently.
4. Import the roster as the saved class. Students join with the last four digits and the letter of their ID.
5. Keep the html deck or the PDF open on a laptop as backup.

## Keeping the repository public

Nothing in the sources identifies a student. Keep it that way:

- Student IDs, rosters and ClassPoint exports stay local — `roster/`, `ids.csv` and
  `classpoint/*.csv` are git-ignored. The roster lives in `~/dev/sd5913/roster/`, which is
  a different directory on purpose.
- Grades, gradebooks and submissions never enter the repository, not even in a branch:
  the history is public too.
- Workflow artifacts on a public repo are downloadable by anyone with a GitHub account.
  The PowerPoint artifact is fine; a roster would not be.

## Related

- [`sd5913/pfad`](https://github.com/sd5913/pfad) — the course repo students clone. Branch `2026` is this year, `2025` is the archive.
- [`sd5913/github-student-registry`](https://github.com/sd5913/github-student-registry) — the ID ↔ GitHub matcher at <https://pfad.ait4x.org>.
- [`ait4x/deckgen`](https://github.com/ait4x/deckgen) — the slide toolchain this repo uses.
- `~/dev/sd5913/` — the private admin workspace: course plan, deck reviews, roster, org scripts.
