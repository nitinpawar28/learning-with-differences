"""Anki-importable CSV decks with stable GUIDs."""

from __future__ import annotations

import csv
import io

import markdown

from lwd.model import Library, Term
from lwd.render import OutputSet
from lwd.render.common import html, plain

STATUS_RANK = {"stub": 0, "draft": 1, "complete": 2, "deprecated": 2}


def _md(text: str) -> str:
    return markdown.markdown(text or "", extensions=["tables", "fenced_code"])


def _tags(lib: Library, t: Term, kind: str) -> str:
    tags = ["lwd", f"lwd::kind::{kind}", f"lwd::cloud::{t.cloud}", f"lwd::level::{t.level}", f"lwd::domain::{t.domain}"]
    tags += [f"lwd::track::{x}" for x in t.tracks]
    tags += sorted({f"lwd::exam::{c.exam}" for c in t.covers})
    return " ".join(tags)


def cards(lib: Library, ctx: dict, min_status: str = "draft", exam: str | None = None) -> list[tuple[str, str, str, str]]:
    floor = STATUS_RANK.get(min_status, 1)
    out: list[tuple[str, str, str, str]] = []
    pairs = ctx["cloud_pairs"]
    for t in sorted(lib.terms.values(), key=lambda t: t.slug):
        if STATUS_RANK.get(t.status, 0) < floor:
            continue
        if exam and exam not in {c.exam for c in t.covers}:
            continue
        uid = t.uid or t.slug
        back = [html(plain(t.summary))]
        for c in t.differs_from[:3]:
            other = lib.terms.get(c.term)
            if other and c.note:
                back.append(f"<i>vs {html(other.title)}:</i> {html(c.note)}")
        eqs = [p for p in pairs if t.slug in (p.azure, p.aws)]
        if eqs:
            parts = []
            for p in eqs:
                other = lib.terms[p.aws if p.azure == t.slug else p.azure]
                parts.append(f"{html(other.title)} ({p.fidelity})")
            back.append("<i>Other cloud:</i> " + ", ".join(parts))
        out.append((f"lwd-def-{uid}", f"<b>{html(t.title)}</b>", "<hr>".join(back), _tags(lib, t, "def")))
        for f in t.formerly:
            out.append((f"lwd-former-{uid}-{f.name.lower().replace(' ', '-')}", f"What is <b>{html(f.name)}</b> called now?", html(t.title), _tags(lib, t, "former")))
        for i, q in enumerate(t.questions):
            out.append((f"lwd-check-{uid}-{i + 1}", _md(q.question), _md(q.answer), _tags(lib, t, "check")))
        for p in eqs:
            if p.azure != t.slug:
                continue
            other = lib.terms[p.aws]
            if STATUS_RANK.get(other.status, 0) < floor:
                continue
            note = p.notes.get("azure") or p.notes.get("aws", "")
            extra = f"<hr>{html(note)}" if note else ""
            out.append((f"lwd-eq-{uid}-{other.uid or other.slug}", f"AWS counterpart of <b>{html(t.title)}</b>?", f"{html(other.title)} ({p.fidelity}){extra}", _tags(lib, t, "eq")))
            out.append((f"lwd-eq-{other.uid or other.slug}-{uid}", f"Azure counterpart of <b>{html(other.title)}</b>?", f"{html(t.title)} ({p.fidelity}){extra}", _tags(lib, other, "eq")))
    for pair in ctx["contrasts"]:
        a, b = lib.terms[pair.a], lib.terms[pair.b]
        if min(STATUS_RANK.get(a.status, 0), STATUS_RANK.get(b.status, 0)) < floor:
            continue
        if exam and exam not in {c.exam for c in a.covers} | {c.exam for c in b.covers}:
            continue
        notes = "<br>".join(html(n) for n in pair.notes.values()) or "—"
        out.append((f"lwd-diff-{a.uid or a.slug}-{b.uid or b.slug}", f"How does <b>{html(a.title)}</b> differ from <b>{html(b.title)}</b>?", notes, _tags(lib, a, "diff")))
    return out


def to_csv(rows: list[tuple[str, str, str, str]], deck: str) -> str:
    buf = io.StringIO()
    buf.write("#separator:Comma\n#html:true\n#notetype:Basic\n")
    buf.write(f"#deck:{deck}\n#columns:GUID,Front,Back,Tags\n#guid column:1\n#tags column:4\n")
    writer = csv.writer(buf, quoting=csv.QUOTE_ALL, lineterminator="\n")
    for row in rows:
        writer.writerow(row)
    return buf.getvalue()


def render_anki(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    settings = lib.taxonomy.settings.get("anki") or {}
    deck = str(settings.get("deck", "LearnWithDifferences"))
    min_status = str(settings.get("min_status", "draft"))
    outputs.add("glossary/exports/anki-all.csv", to_csv(cards(lib, ctx, min_status), deck))
    for e in sorted(lib.exams.values(), key=lambda e: e.slug):
        rows = cards(lib, ctx, min_status, exam=e.slug)
        if rows:
            outputs.add(f"glossary/exports/anki-{e.slug}.csv", to_csv(rows, f"{deck}::{e.code}"))
