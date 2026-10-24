"""load -> check -> derive -> render -> check output -> (write)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from lwd import checks, derive, load
from lwd.config import ConfigError, load_config
from lwd.diag import Diagnostics
from lwd.model import Library
from lwd.render import OutputSet
from lwd.render.abbreviations import render_abbreviations
from lwd.render.anki import render_anki
from lwd.render.glossary import render_glossary
from lwd.render.study import render_integrity, render_study
from lwd.render.terms import render_terms
from lwd.taxonomy import TaxonomyError, load_taxonomy


@dataclass
class Run:
    lib: Library | None
    outputs: OutputSet | None
    diags: Diagnostics
    ctx: dict | None = None


def context(lib: Library) -> dict:
    pairs, none_notes = derive.cloud_pairs(lib)
    senses, _ = derive.senses(lib)
    return {
        "contrasts": derive.contrast_pairs(lib),
        "cloud_pairs": pairs,
        "none_notes": none_notes,
        "backlinks": derive.backlinks(lib),
        "coverage": derive.coverage(lib),
        "senses": senses,
    }


def build_library(root: Path, today: date, diags: Diagnostics) -> Library | None:
    try:
        cfg = load_config(root)
    except ConfigError as exc:
        diags.error("LWD095", "zensical.toml", 0, str(exc))
        return None
    try:
        tax = load_taxonomy(cfg.docs)
    except FileNotFoundError:
        diags.error("LWD095", "docs/_data/taxonomy.yml", 0, "taxonomy.yml is missing")
        return None
    except TaxonomyError as exc:
        diags.error("LWD095", exc.path, exc.line, str(exc))
        return None
    lib = Library(config=cfg, taxonomy=tax, today=today)
    load.discover(lib, diags)
    load.load_backlog(lib, diags)
    return lib


def run(root: Path, today: date) -> Run:
    """Everything except writing. Errors leave outputs as None."""
    diags = Diagnostics()
    lib = build_library(root, today, diags)
    if lib is None:
        return Run(None, None, diags)
    checks.check_library(lib, diags)
    if diags.has_errors:
        return Run(lib, None, diags)
    ctx = context(lib)
    outputs = OutputSet()
    render_terms(lib, ctx, outputs)
    render_glossary(lib, ctx, outputs)
    render_study(lib, ctx, outputs)
    render_anki(lib, ctx, outputs)
    render_abbreviations(ctx["senses"], outputs)
    # Integrity report placeholder so link/nav checks see the page.
    outputs.docs["study/reports/integrity.md"] = "---\ntitle: Integrity report\n---\n"
    checks.check_output(lib, outputs.docs, diags)
    del outputs.docs["study/reports/integrity.md"]
    render_integrity(lib, diags, outputs)
    if diags.has_errors:
        return Run(lib, None, diags, ctx)
    return Run(lib, outputs, diags, ctx)
