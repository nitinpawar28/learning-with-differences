---
title: "Engine notes"
description: "How the site is generated: Zensical, the lwd generator, its commands and its validation rules."
---

# Engine notes

The site is built by [Zensical](https://zensical.org/) 0.0.72, pinned in
`requirements.txt`, from `zensical.toml`. Before every build, a small Python
package in this repository, `lwd`, compiles the glossary, exams and learning
paths into Markdown pages.

## Two kinds of content

| Kind | Where you write it | What becomes of it |
|---|---|---|
| Rendered pages | `docs/<area>/...` (articles, index pages, practice, about) | Rendered as-is by Zensical |
| Compiled entities | `docs/_terms/<slug>.md`, `docs/_study/exams/<code>.md`, `docs/_study/paths/<slug>.md`, `docs/_data/*.yml` | Compiled by `lwd` into `docs/terms/`, `docs/glossary/` and `docs/study/` (gitignored) |

A source and its output sit at the same depth: `docs/_terms/x.md` becomes
`docs/terms/x.md`. That means a relative link written in a term source works
unchanged on the compiled page.

## Commands

Run these from the repository root, inside the virtual environment.

| Command | What it does |
|---|---|
| `python -m lwd validate` | Check every source; write nothing |
| `python -m lwd gen` | Validate, then write the generated pages, writing only files that changed |
| `python -m lwd serve` | Generate, start `zensical serve`, and regenerate whenever a source changes |
| `python -m lwd build` | Generate, run `zensical build --strict`, then check the built site |
| `python -m lwd new term <slug>` | Scaffold a term (also `exam <code>`, `path <slug>`, `article <path>`; add `--from-backlog` to pre-fill from the content backlog) |
| `python -m lwd stale` | List content overdue for re-verification |
| `python -m lwd coverage [EXAM…] --gaps` | Show each exam's objective coverage and its gaps |
| `python -m lwd export anki --exam az-104` | Write an Anki deck |
| `python -m lwd doctor` | Check the Python version, the Zensical pin and the config |

## Validation codes

Errors stop generation. Warnings are reported and listed on the
[integrity report](../study/reports/integrity.md).

| Code | Meaning |
|---|---|
| LWD001–003 | YAML or front-matter parse error, duplicate key, invalid UTF-8 |
| LWD010 | Unknown front-matter key (with a "did you mean") |
| LWD011–014 | Missing required field, wrong type, value not in the taxonomy, bad or future date |
| LWD020–023 | Bad slug or file name; the same name used by several terms |
| LWD030–034 | Unknown reference; equivalent on the same cloud; a one-sided contrast or equivalent |
| LWD040–044 | Acronym that can never match, skipped or ambiguous acronyms |
| LWD050–052 | Objective id problems; unknown exam objective in `covers` |
| LWD060 | Learning-path step without exactly one target |
| LWD070–075 | Complete page missing required parts; quality warnings |
| LWD080–083 | Broken link, missing anchor, link into a source folder, wrong letter case |
| LWD090–095 | Navigation entry missing, page not in the navigation, unreachable generated page, config problems |

## Zensical compatibility notes

Results of the compatibility checks run against Zensical 0.0.72 are recorded
here. Re-run the checks before every Zensical upgrade.
