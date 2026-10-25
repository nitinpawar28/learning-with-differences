# Learning with Differences

A personal, exam-grade library for **architecture, agentic AI, security, Azure
and AWS**, in which every concept is taught by its differences: what it is,
what it is easily confused with, and how it maps to its counterpart on the
other cloud.

Published at **https://nitinpawar28.github.io/learning-with-differences/**.
It is built with [Zensical](https://zensical.org/) and `lwd`, a small
generator in this repository that compiles the glossary, the exam hub and the
learning paths.

## Quickstart

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

python -m lwd serve          # generate, then live preview at http://localhost:8000
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m lwd serve
```

## Everyday commands

| Command | What it does |
|---|---|
| `python -m lwd validate` | Check every source; writes nothing |
| `python -m lwd gen` | Validate, then write the generated pages (only files that changed) |
| `python -m lwd serve` | Generate, start the dev server, regenerate on every source change |
| `python -m lwd build` | Generate, `zensical build --strict`, then check the built site |
| `python -m lwd new term <slug>` | Scaffold a glossary term (`exam <code>`, `path <slug>`, `article <path>` too) |
| `python -m lwd coverage az-104 --gaps` | Show an exam's objective coverage and gaps |
| `python -m lwd stale` | List content overdue for re-verification |
| `python -m lwd export anki --exam az-104 --out az-104.csv` | Write an Anki deck |
| `python -m lwd nav` | Regenerate the area tabs of the navigation from the taxonomy (`--check` only reports) |
| `python -m lwd doctor` | Check the Python version, the Zensical pin and the config |
| `python -m unittest discover -s tests` | Run the generator's tests |

## How the repository is organised

```text
zensical.toml            Site configuration and navigation (TOML 1.0)
requirements.txt         zensical==0.0.72 — the only dependency
lwd/                     The generator: load → validate → render → write
tests/                   Generator tests (fixture library, negative cases)
docs/
  index.md, about/       Home page, how the library works, templates, engine notes
  architecture/ cloud/ ai/ security/      The four tracks (rendered as-is)
  messaging/ data/ frontend/ devops/      Engineering pages for the real stack
  practice/              Labs, katas, threat models, tabletops, capstones
  _terms/<slug>.md       Glossary term sources            ┐
  _study/exams/<code>.md Exam sources with objectives     │ compiled by lwd,
  _study/paths/<slug>.md Learning-path sources            │ excluded from the
  _glossary/, _study/    Optional intro frames for hubs   │ Zensical build
  _data/                 taxonomy.yml, abbreviations.yml, backlog/
  terms/ glossary/ study/                Generated output (gitignored)
generated/               Generated tooltips file, manifest (gitignored)
```

Rendered pages live at `docs/<area>/<domain>[/<group>]/<page>.md`. The areas,
domains and groups are listed in `docs/_data/taxonomy.yml`.

## Writing content

1. **Terms:** `python -m lwd new term managed-identity`, then fill in the front
   matter (summary, aliases, former names, tracks, domain, cloud, level,
   equivalents with fidelity, differs_from, covers, sources) and the sections
   (Explanation, How it differs, Examples, Misconceptions, Exam notes,
   Self-check, Further reading).
2. **Articles:** `python -m lwd new article cloud/azure/identity/managed-identities.md`
   (add `--from-backlog` to pre-fill from `docs/_data/backlog/`), then run
   `python -m lwd nav` to add it to the navigation.
3. Mark a page `status: complete` only when every claim about cloud
   behaviour, limits, defaults or availability links a primary source, and set
   `last_verified`.
4. `python -m lwd validate` reports problems with a code and file:line, and a
   suggestion where it can. The codes are explained in `docs/about/engine.md`.

Never edit `docs/terms/`, `docs/glossary/`, `docs/study/` or `generated/`.
They are rebuilt on every run.

## Publishing

Pushing to `main` runs `.github/workflows/publish.yml`. It runs the tests,
`python -m lwd build --ci` (which includes a strict Zensical build), and then
deploys to GitHub Pages. A weekly scheduled run keeps the freshness and
coverage reports current.
