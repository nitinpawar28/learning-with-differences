"""Compile docs/_terms/<slug>.md into docs/terms/<slug>.md."""

from __future__ import annotations

from lwd import derive
from lwd.load import TERM_SECTION_ORDER, TERM_SECTION_TITLES
from lwd.model import Library, Term
from lwd.render import OutputSet
from lwd.render.common import cell, chip, facet_page, front_matter, inline, link, status_note, term_link

FIDELITY_LABEL = {"exact": "Exact", "close": "Close", "partial": "Partial", "none": "None"}


def render_term(lib: Library, t: Term, ctx: dict) -> str:
    tax = lib.taxonomy
    page = t.page
    out: list[str] = []
    labels = [tax.label("tracks", x) for x in t.tracks] + [tax.label("term_domains", t.domain), tax.label("clouds", t.cloud), tax.label("levels", t.level)]
    meta = {
        "title": t.title,
        "description": t.summary,
        "status": t.status,
        "tags": labels,
        "hide": ["tags"],
    }
    if t.status == "stub":
        meta["search"] = {"exclude": True}  # placeholders should not compete in search
    out.append(front_matter(meta, t.origin.path))
    out.append(f"# {inline(t.title)}\n\n")
    crumbs = [link(page, "glossary/index.md", "Glossary")]
    if t.tracks:
        crumbs.append(link(page, facet_page("track", t.tracks[0]), tax.label("tracks", t.tracks[0])))
    crumbs.append(link(page, facet_page("domain", t.domain), tax.label("term_domains", t.domain)))
    out.append(" › ".join(crumbs) + "\n{ .lwd-crumbs }\n\n")
    if t.status == "deprecated":
        out.append(f'!!! danger "Deprecated"\n    Superseded by {term_link(page, lib, t.superseded_by)}.\n\n')
    else:
        out.append(status_note(t.status))
    fresh = derive.term_freshness(lib, t)
    if fresh.state == "overdue":
        out.append(f'!!! warning "Possibly out of date"\n    Last verified {t.last_verified}; review was due {fresh.due} ({fresh.klass} content is reviewed every {fresh.window} days).\n\n')
    out.append(f'!!! abstract "Definition"\n    {inline(t.summary)}\n\n')

    meta1 = []
    if t.acronyms:
        meta1.append("**Acronym:** " + ", ".join(inline(a) for a in t.acronyms))
    if t.aliases:
        meta1.append("**Also known as:** " + ", ".join(inline(a) for a in t.aliases))
    if t.formerly:
        parts = []
        for f in t.formerly:
            bits = [inline(f.name)]
            if f.acronym:
                bits.append(f"({inline(f.acronym)})")
            if f.until:
                bits.append(f"until {inline(f.until)}")
            parts.append(" ".join(bits))
        meta1.append("**Formerly:** " + "; ".join(parts))
    meta2 = [
        "**Cloud:** " + link(page, facet_page("cloud", t.cloud), tax.label("clouds", t.cloud)),
        "**Level:** " + link(page, facet_page("level", t.level), tax.label("levels", t.level)),
        "**Tracks:** " + ", ".join(link(page, facet_page("track", x), tax.label("tracks", x)) for x in t.tracks),
    ]
    if t.last_verified:
        due = f" (review by {fresh.due})" if fresh.due else ""
        meta2.append(f"**Verified:** {t.last_verified}{due}")
    lines = [" · ".join(meta1)] if meta1 else []
    lines.append(" · ".join(meta2))
    out.append("  \n".join(lines) + "\n{ .lwd-meta }\n\n")

    authored = {s.canonical: s for s in t.sections}

    def section(name: str) -> str:
        s = authored.get(name)
        return s.text.strip() if s and s.text.strip() else ""

    def emit(name: str, extra: str = "") -> None:
        body = section(name)
        if not body and not extra:
            return
        out.append(f"## {TERM_SECTION_TITLES[name]} {{ #{name} }}\n\n")
        if extra:
            out.append(extra + "\n\n")
        if body:
            out.append(body + "\n\n")

    emit("explanation")

    # How it differs: declared contrasts, then reverse edges.
    rows = []
    for c in t.differs_from:
        if c.term in lib.terms:
            rows.append(f"| {term_link(page, lib, c.term)} | {cell(c.note) or '—'} |")
    reverse = [x for x in ctx["contrasts"] if t.slug in (x.a, x.b)]
    declared = {c.term for c in t.differs_from}
    also = []
    for pair in reverse:
        other = pair.b if pair.a == t.slug else pair.a
        if other not in declared:
            note = pair.notes.get(other, "")
            also.append(f"| {term_link(page, lib, other)} | {cell(note) or '—'} |")
    table = ""
    if rows or also:
        table = "| Compared with | Key difference |\n|---|---|\n" + "\n".join(rows + also)
    deep = []
    for pair in reverse:
        for art in pair.articles:
            a = lib.articles.get(art)
            if a:
                deep.append(link(page, art, a.title))
    if deep:
        table += ("\n\n" if table else "") + "**Deep dives:** " + " · ".join(sorted(set(deep)))
    emit("differs", table)

    # Azure <-> AWS.
    if t.cloud in ("azure", "aws"):
        other_cloud = "aws" if t.cloud == "azure" else "azure"
        other_label = tax.label("clouds", other_cloud)
        rows = []
        for pair in ctx["cloud_pairs"]:
            mine = pair.azure if t.cloud == "azure" else pair.aws
            if mine != t.slug:
                continue
            theirs = pair.aws if t.cloud == "azure" else pair.azure
            note = pair.notes.get(t.cloud) or pair.notes.get(other_cloud, "")
            rows.append(f"| {term_link(page, lib, theirs)} | {chip('fidelity', pair.fidelity, FIDELITY_LABEL.get(pair.fidelity, pair.fidelity))} | {cell(note) or '—'} |")
        for note in ctx["none_notes"].get(t.slug, []):
            rows.append(f"| *No direct counterpart* | {chip('fidelity', 'none', 'None')} | {cell(note)} |")
        if rows:
            out.append("## Azure ↔ AWS { #azure-aws }\n\n")
            out.append(f"| {other_label} counterpart | Fidelity | What differs |\n|---|---|---|\n" + "\n".join(rows) + "\n\n")
            extra = []
            if t.concept and t.concept in lib.terms:
                extra.append("**Concept:** " + term_link(page, lib, t.concept))
            extra.append(link(page, "glossary/rosetta.md", "Rosetta: " + tax.label("term_domains", t.domain), t.domain))
            out.append(" · ".join(extra) + "\n\n")
    elif t.cloud == "neutral":
        impls = [x for x in lib.terms.values() if x.concept == t.slug]
        if impls:
            out.append("## Implementations { #implementations }\n\n| Cloud | Service or feature |\n|---|---|\n")
            for x in sorted(impls, key=lambda x: (x.cloud, x.title.lower())):
                out.append(f"| {tax.label('clouds', x.cloud)} | {term_link(page, lib, x.slug)} |\n")
            out.append("\n")

    emit("examples")
    emit("misconceptions")

    exam_lines = []
    for c in t.covers:
        exam = lib.exams.get(c.exam)
        obj = exam.objective(c.objective) if exam else None
        if exam and obj:
            exam_lines.append("- " + link(page, exam.page, f"{exam.code} · {obj.id} {obj.title}", obj.anchor) + (" *(partial)*" if c.depth == "partial" else ""))
    emit("exam-notes", "\n".join(exam_lines))
    emit("self-check")
    emit("further-reading")

    for s in t.sections:
        if s.canonical not in TERM_SECTION_ORDER and s.text.strip():
            out.append(f"## {s.title}\n\n{s.text.strip()}\n\n")

    related = []
    rel_terms = [term_link(page, lib, s) for s in t.related if s in lib.terms]
    if rel_terms:
        related.append("**Related terms:** " + " · ".join(rel_terms))
    used_in = ctx["backlinks"].get(t.slug, [])
    if used_in:
        related.append("**Discussed in:** " + " · ".join(
            link(page, p, lib.articles[p].title if p in lib.articles else lib.terms[p[6:-3]].title)
            for p in used_in if p in lib.articles or (p.startswith("terms/") and p[6:-3] in lib.terms)
        ))
    on_paths = [lp for lp in lib.paths.values() if any(st.kind == "term" and st.target == t.slug for st in lp.steps)]
    if on_paths:
        related.append("**On learning paths:** " + " · ".join(link(page, lp.page, lp.title) for lp in on_paths))
    if related:
        out.append("## Related { #related data-search-exclude }\n\n" + "  \n".join(related) + "\n\n")
    if t.sources:
        out.append("## Sources { #sources data-search-exclude }\n\n")
        for i, s in enumerate(t.sources, 1):
            pub = f" — {inline(s.publisher)}" if s.publisher else ""
            out.append(f"{i}. [{inline(s.title)}]({s.url}){pub}\n")
        out.append("\n")
    return "".join(out).rstrip() + "\n"


def render_terms(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    for t in sorted(lib.terms.values(), key=lambda t: t.slug):
        outputs.add(t.page, render_term(lib, t, ctx))
