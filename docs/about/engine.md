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

These checks were run against Zensical 0.0.72 on 2026-10-24 (Python-Markdown
3.11.2, pymdown-extensions 12.3, Windows 11). Re-run them before every
Zensical upgrade.

| Check | Result | What it means for this site |
|---|---|---|
| Config precedence | `zensical.toml` always wins; a leftover `mkdocs.yml` is silently ignored | `mkdocs.yml` is deleted. `lwd` runs `zensical build -f zensical.toml` from the repository root. |
| `exclude_docs` | Works with gitignore-style patterns; must be a multi-line string | Folders starting with `_` are published unless they are excluded, so every source folder is listed. A link from a published page into an excluded folder fails `--strict`; LWD082 catches it earlier. |
| Navigation | No "page not in nav" check. A nav entry pointing at a missing file renders a broken link **without any warning**. | `lwd` checks both itself: LWD090 for missing nav targets, and LWD091/LWD093 for pages not in the nav or unreachable. |
| Status badges | Badges appear in the navigation only. Unknown values show a generic icon, and stub and draft look the same unless styled. | Statuses are validated. `lwd.css` gives stub, draft and deprecated their own icons and hides the badge for complete pages. Pages outside the navigation get a status admonition in the page body instead. |
| Cache and `--clean` | The cache is content-hashed. A failed build still deletes pages from `site/`. | CI runs `build --clean`. Deploy happens only on exit code 0. Never write into `site/`. |
| Tooltips via `auto_append` | A missing file silently drops every tooltip unless `check_paths = true`. Snippet paths resolve against the working directory. | `check_paths = true`. The build runs from the repository root. The abbreviations file is always written, even when empty. |
| Tooltip performance | A contiguous block of definitions costs about 0.25 s per page at 300 definitions and grows quadratically. | One definition per paragraph (linear). The suppress and allow-short lists keep the list lean. |
| Acronyms with symbols | `C#`, `F#`, `C++` and `.NET` never match as abbreviations | LWD040 rejects them. To suppress a tooltip for a single occurrence, use inline code or an HTML entity. |
| Tooltip text in search | Expansions inside `<abbr>` titles are not indexed | Term titles carry the expansion in visible text, e.g. "Mutual TLS (mTLS)". |
| Asset links | `.js`, `.json` and image links are rewritten correctly but never checked for existence | `lwd` checks every link target, including generated exports. `doctor` checks the `extra_css` and `extra_javascript` files. |
| Anchors | `--strict` checks every fragment, including links inside tabs and tables | Explicit `{ #id }` ids are lowercase. Never link to the positional `__tabbed_N_M` ids. |
| Search controls | `search: {exclude: true}` and `{ data-search-exclude }` work; the latter covers only up to the next heading of any level | Hubs, reports and stub terms are excluded from search. |
| Icons | Without the emoji extension, `:material-…:` shortcodes appear as raw text, and the build still passes | The emoji extension is configured. The post-build check fails on any unrendered shortcode. |
| JavaScript | `document$` is defined before `extra_javascript` runs. Top-level code runs once per full page load. | All Explorer set-up happens in `document$.subscribe`. |
| Dev server | Docs pages rebuild in about 0.4 s. Included files are tracked by whole-second modification time. | Generated files are written only when their content changes. On Windows, `lwd serve` stops the whole server process tree. |
| Offline build | Works through a separate config with the offline plugin | Planned as a separate `zensical.offline.toml`, not a toggle in the main config. |
| `betterem` | Renders correctly | Keep code identifiers such as `__init__` in backticks. |
| Large-site build time | Synthetic site of 1,502 pages (1,200 terms of about 300 words, 300 articles of about 3,000 words, 800 tooltip definitions): cold `--clean --strict` build 48 s, unchanged rebuild 54 s, site 94 MB, `search.json` 10.5 MB, term page 43 KB, article page 105 KB (Windows 11, 16 cores) | Build time fits the 5-minute CI budget with room to spare; the unchanged rebuild is no faster, so the cache is not worth protecting. The search index is the number to watch: real articles are longer than the synthetic ones, so hub, report and stub pages stay excluded from search, and index size is re-measured when the library passes about 500 real pages. |
