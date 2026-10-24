"""Derived knowledge: contrast pairs, Azure↔AWS pairs, backlinks, freshness,
exam coverage and acronym senses. Pure functions over a Library."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, timedelta

from lwd import paths
from lwd.model import Article, Exam, Library, Objective, Term


# --- contrasts -------------------------------------------------------------

@dataclass
class ContrastPair:
    a: str
    b: str
    notes: dict[str, str] = field(default_factory=dict)  # declaring slug -> note
    articles: list[str] = field(default_factory=list)


def contrast_pairs(lib: Library) -> list[ContrastPair]:
    pairs: dict[tuple[str, str], ContrastPair] = {}
    for t in lib.terms.values():
        for c in t.differs_from:
            if c.term not in lib.terms or c.term == t.slug:
                continue
            key = tuple(sorted((t.slug, c.term)))
            pair = pairs.setdefault(key, ContrastPair(*key))
            if c.note:
                pair.notes[t.slug] = c.note
    for art in lib.articles.values():
        known = [s for s in art.compares if s in lib.terms]
        for i, a in enumerate(known):
            for b in known[i + 1 :]:
                key = tuple(sorted((a, b)))
                pair = pairs.setdefault(key, ContrastPair(*key))
                pair.articles.append(art.page)
    return sorted(pairs.values(), key=lambda p: (lib.terms[p.a].title.lower(), lib.terms[p.b].title.lower()))


# --- Azure <-> AWS ---------------------------------------------------------

@dataclass
class CloudPair:
    azure: str
    aws: str
    fidelity: str
    notes: dict[str, str] = field(default_factory=dict)  # side -> note
    declared: dict[str, str] = field(default_factory=dict)  # side -> declared fidelity


def cloud_pairs(lib: Library) -> tuple[list[CloudPair], dict[str, list[str]]]:
    """Return reconciled pairs and the per-term 'no counterpart' notes."""
    tax = lib.taxonomy
    pairs: dict[tuple[str, str], CloudPair] = {}
    none_notes: dict[str, list[str]] = {}
    for t in lib.terms.values():
        if t.cloud not in ("azure", "aws"):
            continue
        for eq in t.equivalents:
            if eq.fidelity == "none":
                if eq.note:
                    none_notes.setdefault(t.slug, []).append(eq.note)
                continue
            other = lib.terms.get(eq.term)
            if other is None or other.cloud == t.cloud or other.cloud not in ("azure", "aws"):
                continue
            key = (t.slug, other.slug) if t.cloud == "azure" else (other.slug, t.slug)
            pair = pairs.setdefault(key, CloudPair(key[0], key[1], eq.fidelity))
            pair.declared[t.cloud] = eq.fidelity
            if eq.note:
                pair.notes[t.cloud] = eq.note
    for pair in pairs.values():
        ranks = [tax.fidelity_rank(f) for f in pair.declared.values()]
        lowest = min(ranks)
        pair.fidelity = next(f for f in pair.declared.values() if tax.fidelity_rank(f) == lowest)
    return list(pairs.values()), none_notes


# --- backlinks ---------------------------------------------------------------

def backlinks(lib: Library) -> dict[str, list[str]]:
    """term slug -> sorted list of authored pages (docs-relative) linking to it."""
    out: dict[str, set[str]] = {}

    def visit(src_page: str, links) -> None:
        for link in links:
            if link.is_external or not link.path:
                continue
            target = paths.resolve(src_page, link.path)
            if target.startswith("terms/") and target.endswith(".md"):
                slug = target[len("terms/") : -3]
                if slug in lib.terms:
                    out.setdefault(slug, set()).add(src_page)

    for art in lib.articles.values():
        visit(art.page, art.links)
        for slug in art.compares:
            if slug in lib.terms:
                out.setdefault(slug, set()).add(art.page)
    for t in lib.terms.values():
        visit(t.page, t.links)
    for slug in out:
        out[slug].discard(lib.terms[slug].page)
    return {k: sorted(v) for k, v in out.items()}


# --- freshness -------------------------------------------------------------

@dataclass
class Freshness:
    state: str  # fresh | due-soon | overdue | unverified | unverified-stub
    klass: str
    window: int
    due: date | None
    days_over: int = 0


def volatility_class(lib: Library, tracks: list[str], domain: str, clouds: list[str], override: str) -> str:
    if override:
        return override
    classes = []
    if "agentic-ai" in tracks or lib.taxonomy.domain_volatility(domain) == "ai":
        classes.append("ai")
    if any(c in ("azure", "aws") for c in clouds):
        classes.append("cloud")
    if not classes:
        classes.append("fundamentals")
    return min(classes, key=lambda c: lib.taxonomy.volatility.get(c, 10_000))


def freshness(lib: Library, status: str, last: date | None, klass: str) -> Freshness:
    window = lib.taxonomy.volatility.get(klass, 730)
    soon = int(lib.taxonomy.settings.get("due_soon_days", 30))
    if status == "stub":
        return Freshness("unverified-stub", klass, window, None)
    if last is None:
        return Freshness("unverified", klass, window, None)
    due = last + timedelta(days=window)
    if lib.today > due:
        return Freshness("overdue", klass, window, due, (lib.today - due).days)
    if (due - lib.today).days <= soon:
        return Freshness("due-soon", klass, window, due)
    return Freshness("fresh", klass, window, due)


def term_freshness(lib: Library, t: Term) -> Freshness:
    klass = volatility_class(lib, t.tracks, t.domain, [t.cloud], t.volatility)
    return freshness(lib, t.status, t.last_verified, klass)


def article_freshness(lib: Library, a: Article) -> Freshness:
    klass = volatility_class(lib, a.tracks, a.domain, a.clouds, a.volatility)
    return freshness(lib, a.status, a.last_verified, klass)


def exam_freshness(lib: Library, e: Exam) -> Freshness:
    klass = "ai" if "agentic-ai" in e.tracks else "cloud"
    return freshness(lib, "complete", e.last_verified, klass)


# --- exam coverage ---------------------------------------------------------

@dataclass
class Coverer:
    page: str  # docs-relative output page
    title: str
    status: str
    depth: str
    anchor: str = ""


@dataclass
class ObjectiveCoverage:
    objective: Objective
    state: str  # covered | partial | planned | gap | overview
    coverers: list[Coverer]


@dataclass
class ExamCoverage:
    exam: Exam
    objectives: dict[str, ObjectiveCoverage]
    domains: list[dict]
    readiness: float
    weighted: float | None
    gaps: list[Objective]


def _midpoint(weight: str) -> float | None:
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", weight or "")]
    return sum(nums) / len(nums) if nums else None


def coverage(lib: Library) -> dict[str, ExamCoverage]:
    by_ref: dict[str, list[Coverer]] = {}
    for t in lib.terms.values():
        for c in t.covers:
            by_ref.setdefault(c.ref, []).append(Coverer(t.page, t.title, t.status, c.depth, c.anchor))
    for a in lib.articles.values():
        for c in a.covers:
            by_ref.setdefault(c.ref, []).append(Coverer(a.page, a.title, a.status or "draft", c.depth, c.anchor))
    result: dict[str, ExamCoverage] = {}
    for exam in lib.exams.values():
        leaves = {o.id for o in exam.leaves()}
        objs: dict[str, ObjectiveCoverage] = {}
        for o in exam.objectives:
            cov = sorted(by_ref.get(f"{exam.slug}:{o.id}", []), key=lambda c: c.title.lower())
            if o.id not in leaves:
                objs[o.id] = ObjectiveCoverage(o, "overview", cov)
                continue
            if any(c.status == "complete" and c.depth == "full" for c in cov):
                state = "covered"
            elif any(c.status in ("draft", "complete") for c in cov):
                state = "partial"
            elif cov:
                state = "planned"
            else:
                state = "gap"
            objs[o.id] = ObjectiveCoverage(o, state, cov)
        domains = []
        weighted_num = 0.0
        weighted_den = 0.0
        for top in [o for o in exam.objectives if not o.parent]:
            members = [x for x in objs.values() if (x.objective.id == top.id or x.objective.id.startswith(top.id + ".")) and x.state != "overview"]
            counts = {s: sum(1 for m in members if m.state == s) for s in ("covered", "partial", "planned", "gap")}
            n = len(members)
            ready = counts["covered"] / n if n else 0.0
            mid = _midpoint(top.weight)
            if mid is not None:
                weighted_num += mid * ready
                weighted_den += mid
            domains.append({"objective": top, "counts": counts, "leaves": n, "readiness": ready})
        all_leaves = [x for x in objs.values() if x.state != "overview"]
        readiness = sum(1 for x in all_leaves if x.state == "covered") / len(all_leaves) if all_leaves else 0.0
        weighted = (weighted_num / weighted_den) if weighted_den else None
        gaps = [x.objective for x in all_leaves if x.state == "gap"]
        result[exam.slug] = ExamCoverage(exam, objs, domains, readiness, weighted, gaps)
    return result


# --- acronym senses ----------------------------------------------------------

@dataclass
class Sense:
    acronym: str
    expansion: str
    gloss: str
    kind: str  # current | exam | extra | former
    slug: str = ""


_STOPLIST = {"IT", "AS", "OR", "ON", "IN", "IS", "ID", "NO", "OK", "US", "IF", "OF", "TO", "AT", "BY", "AN", "BE", "DO", "GO", "UP", "SO", "WE", "ME", "MY", "HE", "IT"}
_WORD_EDGE = re.compile(r"^\w.*\w$|^\w$")


def first_sentence(text: str, limit: int = 160) -> str:
    text = re.sub(r"\s+", " ", re.sub(r"[*_`]|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", text)).strip()
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    if len(s) > limit:
        cut = s[:limit].rsplit(" ", 1)[0]
        s = cut.rstrip(",;:") + "…"
    return s


def strip_acronym_suffix(title: str, acronym: str) -> str:
    return re.sub(rf"\s*\({re.escape(acronym)}\)\s*$", "", title).strip()


def senses(lib: Library) -> tuple[dict[str, list[Sense]], list[tuple[str, str, str]]]:
    """Return acronym -> senses, plus (code, acronym, reason) for skipped ones."""
    abbr = lib.taxonomy.abbreviations or {}
    suppress = {str(s) for s in (abbr.get("suppress") or [])}
    allow_short = {str(s) for s in (abbr.get("allow_short") or [])}
    raw: list[Sense] = []
    for t in lib.terms.values():
        gloss = first_sentence(t.tooltip or t.summary)
        for a in t.acronyms:
            raw.append(Sense(a, strip_acronym_suffix(t.title, a), gloss, "current", t.slug))
        for f in t.formerly:
            if f.acronym:
                when = f" (renamed {f.until[:4]})" if f.until else ""
                raw.append(Sense(f.acronym, f.name, f"former name of {t.title}{when}", "former", t.slug))
    for e in lib.exams.values():
        raw.append(Sense(e.code, e.title, f"{e.credential or e.title} exam", "exam", ""))
    for acr, exp in (abbr.get("extra") or {}).items():
        raw.append(Sense(str(acr), str(exp), "", "extra", ""))
    skipped: list[tuple[str, str, str]] = []
    grouped: dict[str, list[Sense]] = {}
    for s in raw:
        a = s.acronym
        if not _WORD_EDGE.match(a):
            skipped.append(("LWD040", a, "acronyms must start and end with a letter or digit to match"))
            continue
        if a in suppress or a.upper() in _STOPLIST:
            skipped.append(("LWD041", a, "suppressed or on the stoplist"))
            continue
        if len(a) <= 2 and a not in allow_short:
            skipped.append(("LWD042", a, "two-letter acronyms need an allow_short entry"))
            continue
        grouped.setdefault(a, []).append(s)
    order = {str(k): [str(x) for x in v] for k, v in (abbr.get("order") or {}).items()}
    kind_rank = {"current": 0, "exam": 1, "extra": 2, "former": 3}
    result: dict[str, list[Sense]] = {}
    for a, items in grouped.items():
        dedup: dict[str, Sense] = {}
        for s in items:
            key = re.sub(r"[\s\-]+", " ", s.expansion.casefold()).strip()
            dedup.setdefault(key, s)
        pref = order.get(a, [])
        result[a] = sorted(
            dedup.values(),
            key=lambda s: (pref.index(s.slug) if s.slug in pref else len(pref), kind_rank[s.kind], s.expansion.lower()),
        )
    return result, skipped
