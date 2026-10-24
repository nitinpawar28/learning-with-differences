# learning-with-differences

Trade-off comparisons, architectural patterns, and deep-dive learning notes
across our production stack — .NET 9, Angular 20, Redis Streams, TimescaleDB,
Docker Compose, and MCP — built with [MkDocs](https://www.mkdocs.org/) +
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Quickstart

### Windows (PowerShell)

```powershell
# 1. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3. Run the local dev server (live-reloads on file save)
mkdocs serve
# -> open http://127.0.0.1:8000
```

### macOS / Linux (bash/zsh)

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3. Run the local dev server (live-reloads on file save)
mkdocs serve
# -> open http://127.0.0.1:8000
```

### Other useful commands

```bash
# Build the static site into ./site
mkdocs build

# Validate config + fail on broken internal links
mkdocs build --strict

# Deactivate the virtual environment when done
deactivate
```

## Adding a new topic page

1. Copy [`docs/_templates/tech-guide-template.md`](docs/_templates/tech-guide-template.md)
   into the relevant domain folder under `docs/` (or start from one of the
   existing stub pages already in place).
2. Fill in each section — the template is structured to force a trade-off
   comparison, not just a description of one option.
3. Add the page to the `nav:` section of [`mkdocs.yml`](mkdocs.yml) so it
   shows up in the sidebar/tabs.

## Project structure

```text
learning-with-differences/
├── mkdocs.yml                  # Site config, theme, nav, extensions
├── requirements.txt             # mkdocs / mkdocs-material / pymdown-extensions
├── docs/
│   ├── index.md                 # Homepage
│   ├── glossary.md              # Master glossary — every recurring term, defined once
│   ├── stylesheets/extra.css    # Small style overrides
│   ├── _templates/
│   │   └── tech-guide-template.md
│   ├── messaging/                # Backend & async messaging: .NET, SignalR, Redis Streams, MCP, outbox
│   ├── data/                     # Relational DBs, TimescaleDB hypertables, indexing, columnar storage
│   ├── frontend/                 # Angular, TypeScript, RxJS, real-time UI
│   ├── devops/                   # Docker Compose, CI/CD, bare-metal/hypervisors
│   └── security/                 # mTLS, workload identity, capability-based authz, Wasm sandboxing
└── .gitignore
```

> **Naming note:** `_templates/`, not `templates/`. MkDocs has a hard-coded
> default that silently excludes any top-level `docs/templates/` folder from
> the build (it's reserved to avoid colliding with theme templates). Keep the
> leading underscore.

## Publishing (optional)

To publish via GitHub Pages once this is pushed to GitHub:

```bash
pip install mkdocs mkdocs-material
mkdocs gh-deploy --force
```

This builds the site and pushes it to a `gh-pages` branch. Set the repo's
GitHub Pages source to that branch afterward.
