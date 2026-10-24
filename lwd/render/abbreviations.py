"""The auto-appended abbreviations file (one definition per paragraph)."""

from __future__ import annotations

import json

from lwd.derive import Sense
from lwd.render import OutputSet
from lwd.render.common import plain

ABBR_PATH = "generated/includes/abbreviations.md"
INDEX_PATH = "generated/includes/abbr-index.json"
MAX_SENSES = 4
MAX_LEN = 160


def _clip(text: str) -> str:
    text = plain(text).replace("\n", " ")
    if len(text) <= MAX_LEN:
        return text
    return text[:MAX_LEN].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def _gloss(s: Sense) -> str:
    return f"{s.expansion} — {s.gloss}" if s.gloss and s.gloss.lower() != s.expansion.lower() else s.expansion


def render_abbreviations(senses: dict[str, list[Sense]], outputs: OutputSet) -> None:
    lines = []
    for acr in sorted(senses, key=lambda a: (a.casefold(), a)):
        items = senses[acr]
        if len(items) == 1:
            text = _clip(_gloss(items[0]))
        else:
            shown = "; ".join(f"({i}) {_gloss(s)}" for i, s in enumerate(items[:MAX_SENSES], 1))
            more = "; …" if len(items) > MAX_SENSES else ""
            text = _clip(f"Ambiguous: {shown}{more}")
        # A blank line between definitions keeps abbr processing linear.
        lines.append(f"*[{acr}]: {text}")
    outputs.add_root(ABBR_PATH, "\n\n".join(lines) + ("\n" if lines else ""))
    index = {acr: [{"expansion": s.expansion, "gloss": s.gloss, "kind": s.kind, "slug": s.slug} for s in items] for acr, items in senses.items()}
    outputs.add_root(INDEX_PATH, json.dumps(index, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
