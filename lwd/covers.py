"""Suggest `covers` entries: match term names against exam objective titles.

Deterministic first pass; an editor (human or agent) confirms each
suggestion before it goes into the term's front matter.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field

from lwd.model import Library, Term

_STOP = {"the", "and", "or", "of", "for", "to", "in", "on", "with", "a", "an", "vs", "versus", "using", "by", "as", "at", "from"}


def _singular(word: str) -> str:
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def _norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch)).lower()
    text = re.sub(r"\(([^)]*)\)", r" \1 ", text)  # keep parenthesised acronyms as words
    words = re.sub(r"[^a-z0-9+#.]+", " ", text).split()
    return " ".join(_singular(w) for w in words)


_GENERIC_TAIL = {"deployment", "release", "pattern", "index", "policy", "flow", "strategy", "architecture", "model", "storage", "principle"}


def _phrases(t: Term) -> list[tuple[str, str]]:
    """(kind, normalised phrase) for every name a term is known by."""
    title = _norm(re.sub(r"\s*\([^)]*\)\s*$", "", t.title))
    out = [("title", title)]
    # "Blue-Green Deployment" also matches "blue/green traffic splitting".
    words = title.split()
    if len(words) >= 2 and words[-1] in _GENERIC_TAIL:
        stem = " ".join(words[:-1])
        if len(stem) >= 5 and stem not in _STOP:
            out.append(("title-stem", stem))
    out += [("acronym", _norm(a)) for a in t.acronyms]
    out += [("alias", _norm(a)) for a in t.aliases]
    out += [("former", _norm(f.name)) for f in t.formerly]
    seen = set()
    result = []
    for kind, p in out:
        if p and p not in seen and (len(p) > 2 or kind == "acronym"):
            seen.add(p)
            result.append((kind, p))
    return result


@dataclass
class Suggestion:
    ref: str
    exam: str
    objective: str
    title: str
    via: str
    depth: int
    tier: str
    track_match: bool = True  # the exam serves one of the term's tracks


@dataclass
class TermSuggestions:
    slug: str
    items: list[Suggestion] = field(default_factory=list)


def suggest(lib: Library, min_words: int = 1) -> dict[str, TermSuggestions]:
    """Return slug -> suggestions, objective leaves preferred over groups."""
    objective_index = []
    for exam in lib.exams.values():
        if exam.tier == "skip" or not exam.objectives:
            continue
        parents = {o.parent for o in exam.objectives if o.parent}
        for o in exam.objectives:
            if not o.parent:
                continue  # domains are too broad to be "covered" by a term
            is_leaf = o.id not in parents
            objective_index.append((exam, o, is_leaf, " " + _norm(o.title) + " "))
    result: dict[str, TermSuggestions] = {}
    for t in lib.terms.values():
        phrases = _phrases(t)
        found = TermSuggestions(t.slug)
        seen_refs = set()
        for exam, o, is_leaf, otext in objective_index:
            for kind, p in phrases:
                words = [w for w in p.split() if w not in _STOP]
                if len(words) < min_words:
                    continue
                if f" {p} " in otext:
                    ref = f"{exam.slug}:{o.id}"
                    if ref in seen_refs:
                        break
                    # Prefer the leaf; skip a parent group when a child also matches.
                    seen_refs.add(ref)
                    overlap = not t.tracks or not exam.tracks or bool(set(t.tracks) & set(exam.tracks))
                    found.items.append(Suggestion(ref, exam.code, o.id, o.title, f"{kind}: {p}", o.depth, exam.tier, overlap))
                    break
        # Drop parents whose children are also suggested.
        child_parents = {s.ref.rsplit(".", 1)[0] for s in found.items if "." in s.objective}
        found.items = [s for s in found.items if s.ref not in child_parents]
        found.items.sort(key=lambda s: (not s.track_match, {"core": 0, "elective": 1}.get(s.tier, 2), s.exam, [int(x) for x in s.objective.split(".")]))
        if found.items:
            result[t.slug] = found
    return result


def format_report(lib: Library, sugg: dict[str, TermSuggestions], limit_per_term: int = 25) -> str:
    lines = [f"# Suggested covers for {len(sugg)} of {len(lib.terms)} terms", ""]
    for slug in sorted(sugg):
        t = lib.terms[slug]
        items = sugg[slug].items
        lines.append(f"## {t.title} ({slug}) — {len(items)} matches")
        for s in items[:limit_per_term]:
            flag = "" if s.track_match else " **[other track]**"
            lines.append(f"- `{s.ref}` {s.title}  _(via {s.via})_{flag}")
        if len(items) > limit_per_term:
            lines.append(f"- … and {len(items) - limit_per_term} more")
        lines.append("")
    return "\n".join(lines)
