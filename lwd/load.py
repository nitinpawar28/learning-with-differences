"""Discover and parse every source into a Library, collecting diagnostics.

Per-entity schema checks (required fields, types, vocabularies, dates,
unknown keys) happen here; cross-entity checks live in ``lwd.checks``.
"""

from __future__ import annotations

import difflib
import json
import re
from datetime import date
from pathlib import Path

from lwd import mdscan, yamlio
from lwd.config import SiteConfig
from lwd.diag import Diagnostics
from lwd.model import (
    Article,
    Contrast,
    Cover,
    Equivalent,
    Exam,
    Formerly,
    LearningPath,
    Library,
    Objective,
    Origin,
    SourceRef,
    Step,
    Term,
)
from lwd.taxonomy import Taxonomy

GENERATED_DIRS = ("terms", "glossary", "study")
SOURCE_DIRS = ("_terms", "_study", "_glossary", "_data")
STATUSES = ["stub", "draft", "complete", "deprecated"]
PROGRESS = ["planned", "studying", "scheduled", "passed", "expired", "retired"]
TIERS = ["core", "elective", "skip"]
DEPTHS = ["full", "partial"]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
OBJ_ID = re.compile(r"^\d+(?:\.\d+)*$")
RESERVED = {"index", "con", "prn", "aux", "nul"} | {f"com{i}" for i in range(1, 10)} | {f"lpt{i}" for i in range(1, 10)}

# Canonical H2 names for term pages, keyed by lower-cased heading text.
TERM_SECTIONS = {
    "explanation": "explanation",
    "deep explanation": "explanation",
    "in depth": "explanation",
    "how it works": "explanation",
    "how it differs": "differs",
    "differs from": "differs",
    "differences": "differs",
    "examples": "examples",
    "example": "examples",
    "misconceptions": "misconceptions",
    "common misconceptions": "misconceptions",
    "exam traps": "misconceptions",
    "exam notes": "exam-notes",
    "exam focus": "exam-notes",
    "self-check": "self-check",
    "self check": "self-check",
    "check yourself": "self-check",
    "further reading": "further-reading",
    "go deeper": "further-reading",
}
TERM_SECTION_ORDER = ["explanation", "differs", "examples", "misconceptions", "exam-notes", "self-check", "further-reading"]
TERM_SECTION_TITLES = {
    "explanation": "Explanation",
    "differs": "How it differs",
    "examples": "Examples",
    "misconceptions": "Misconceptions",
    "exam-notes": "Exam notes",
    "self-check": "Self-check",
    "further-reading": "Further reading",
}

TERM_KEYS = {
    "title", "summary", "acronyms", "aliases", "formerly", "tracks", "domain", "cloud", "level", "status",
    "superseded_by", "last_verified", "volatility", "concept", "equivalents", "differs_from", "related",
    "covers", "sources", "uid", "tooltip",
}
ARTICLE_KEYS = {
    "title", "description", "status", "level", "tracks", "clouds", "compares", "covers", "last_verified",
    "volatility", "tags",
}
ZENSICAL_KEYS = {"hide", "search", "icon", "template", "subtitle"}
EXAM_KEYS = {
    "code", "title", "credential", "provider", "tracks", "clouds", "level", "tier", "stage", "progress",
    "target_date", "passed_on", "official_url", "study_guide_url", "outline_version", "last_verified",
    "retires_on", "provisional", "prerequisites", "prerequisites_any", "prerequisite_note", "replaces",
    "replaced_by", "counterparts", "objectives",
}
PATH_KEYS = {"title", "summary", "tracks", "level", "exams", "status", "steps"}


def suggest(value: str, options) -> str:
    match = difflib.get_close_matches(value, list(options), n=1, cutoff=0.6)
    return f"did you mean '{match[0]}'?" if match else ""


class Reader:
    """Typed accessors over one front-matter mapping, reporting problems."""

    def __init__(self, origin: Origin, diags: Diagnostics, strict_keys: bool) -> None:
        self.o = origin
        self.d = diags
        self.strict = strict_keys
        self.used: set[str] = set()

    def line(self, key: str) -> int:
        return self.o.line(key)

    def raw(self, key: str):
        self.used.add(key)
        return self.o.meta.get(key)

    def has(self, key: str) -> bool:
        return key in self.o.meta and self.o.meta.get(key) is not None

    def str(self, key: str, required: bool = False, default: str = "") -> str:
        value = self.raw(key)
        if value is None:
            if required:
                self.d.error("LWD011", self.o.path, self.o.meta.line, f"missing required field '{key}'")
            return default
        if isinstance(value, (dict, list)):
            self.d.error("LWD012", self.o.path, self.line(key), f"'{key}' must be text")
            return default
        if isinstance(value, bool):
            self.d.error("LWD012", self.o.path, self.line(key), f"'{key}' must be text, got a boolean", "quote the value")
            return default
        return str(value).strip()

    def boolean(self, key: str, default: bool = False) -> bool:
        value = self.raw(key)
        if value is None:
            return default
        if not isinstance(value, bool):
            self.d.error("LWD012", self.o.path, self.line(key), f"'{key}' must be true or false")
            return default
        return value

    def list(self, key: str, required: bool = False) -> list:
        value = self.raw(key)
        if value is None:
            if required:
                self.d.error("LWD011", self.o.path, self.o.meta.line, f"missing required field '{key}'")
            return []
        if isinstance(value, str):
            return [value]
        if not isinstance(value, list):
            self.d.error("LWD012", self.o.path, self.line(key), f"'{key}' must be a list")
            return []
        return value

    def str_list(self, key: str, required: bool = False) -> list[str]:
        out = []
        items = self.list(key, required)
        for i, item in enumerate(items):
            if isinstance(item, (dict, list, bool)) or item is None:
                ln = items.line_of(i) if hasattr(items, "line_of") else self.line(key)
                self.d.error("LWD012", self.o.path, ln, f"'{key}[{i}]' must be text")
                continue
            out.append(str(item).strip())
        return out

    def enum(self, key: str, allowed, required: bool = False, default: str = "") -> str:
        value = self.str(key, required=required, default=default)
        if value and value not in allowed:
            self.d.error("LWD013", self.o.path, self.line(key), f"'{key}: {value}' is not one of {', '.join(allowed)}", suggest(value, allowed))
            return default
        return value

    def enum_list(self, key: str, allowed, required: bool = False) -> list[str]:
        values = self.str_list(key, required=required)
        good = []
        for v in values:
            if v not in allowed:
                self.d.error("LWD013", self.o.path, self.line(key), f"'{key}' value '{v}' is not one of {', '.join(allowed)}", suggest(v, allowed))
            else:
                good.append(v)
        return good

    def date(self, key: str, today: date, required: bool = False, allow_future: bool = False) -> date | None:
        value = self.str(key, required=required)
        if not value:
            return None
        if not DATE.match(value):
            self.d.error("LWD014", self.o.path, self.line(key), f"'{key}' must be a date YYYY-MM-DD, got '{value}'")
            return None
        try:
            parsed = date.fromisoformat(value)
        except ValueError:
            self.d.error("LWD014", self.o.path, self.line(key), f"'{key}' is not a real date: '{value}'")
            return None
        if not allow_future and parsed > today:
            self.d.error("LWD014", self.o.path, self.line(key), f"'{key}' {value} is in the future")
        return parsed

    def finish(self, allowed: set[str]) -> None:
        for key in self.o.meta:
            if key in allowed or key in self.used:
                continue
            sev_error = self.strict
            msg = f"unknown key '{key}'"
            hint = suggest(key, allowed)
            if sev_error:
                self.d.error("LWD010", self.o.path, self.line(key), msg, hint)
            else:
                self.d.warn("LWD010", self.o.path, self.line(key), msg, hint)


def _read_doc(path: Path, rel: str, diags: Diagnostics) -> yamlio.Document | None:
    try:
        text, bom = yamlio.read_text(path.read_bytes())
    except UnicodeDecodeError as exc:
        diags.error("LWD003", rel, 0, f"file is not valid UTF-8 ({exc.reason} at byte {exc.start})")
        return None
    if bom:
        diags.warn("LWD003", rel, 1, "file starts with a UTF-8 BOM; it is ignored", "save as UTF-8 without BOM")
    try:
        doc = yamlio.split(text)
    except yamlio.YamlError as exc:
        code = "LWD002" if "duplicate key" in str(exc) else "LWD001"
        hint = "quote values that contain ': '" if "mapping values are not allowed" in str(exc) else ""
        diags.error(code, rel, exc.line, f"front matter: {exc}", hint)
        return None
    doc.had_bom = bom
    return doc


def _covers(r: Reader) -> list[Cover]:
    out = []
    items = r.list("covers")
    for i, item in enumerate(items):
        line = items.line_of(i) if hasattr(items, "line_of") else r.line("covers")
        if isinstance(item, str):
            out.append(Cover(item.strip().lower(), line=line))
        elif isinstance(item, dict) and item.get("ref"):
            depth = str(item.get("depth", "full"))
            if depth not in DEPTHS:
                r.d.error("LWD013", r.o.path, line, f"covers depth '{depth}' must be full or partial")
                depth = "full"
            out.append(Cover(str(item["ref"]).strip().lower(), str(item.get("anchor", "") or ""), depth, line))
        else:
            r.d.error("LWD012", r.o.path, line, "covers entries are 'exam:objective' strings or {ref, anchor, depth}")
    for c in out:
        if ":" not in c.ref:
            r.d.error("LWD052", r.o.path, c.line, f"covers ref '{c.ref}' must look like 'az-104:1.2'")
    return out


def _sources(r: Reader) -> list[SourceRef]:
    out = []
    items = r.list("sources")
    for i, item in enumerate(items):
        line = items.line_of(i) if hasattr(items, "line_of") else r.line("sources")
        if isinstance(item, str):
            out.append(SourceRef(item, item))
        elif isinstance(item, dict) and item.get("url"):
            out.append(SourceRef(str(item.get("title") or item["url"]), str(item["url"]), str(item.get("publisher", "") or "")))
        else:
            r.d.error("LWD012", r.o.path, line, "sources entries need at least a url")
    return out


def load_term(path: Path, rel: str, lib: Library, diags: Diagnostics) -> Term | None:
    doc = _read_doc(path, rel, diags)
    if doc is None:
        return None
    tax = lib.taxonomy
    origin = Origin(rel, doc.meta, doc.body, doc.body_line)
    r = Reader(origin, diags, strict_keys=True)
    slug = path.stem
    if not SLUG.match(slug) or len(slug) > 64:
        diags.error("LWD020", rel, 0, f"term slug '{slug}' must be lowercase kebab-case, at most 64 characters")
    if slug in RESERVED:
        diags.error("LWD020", rel, 0, f"'{slug}' is a reserved name on Windows or for index pages")
    formerly = []
    items = r.list("formerly")
    for i, item in enumerate(items):
        if isinstance(item, str):
            formerly.append(Formerly(item.strip()))
        elif isinstance(item, dict) and item.get("name"):
            formerly.append(Formerly(str(item["name"]).strip(), str(item.get("acronym", "") or "").strip(), str(item.get("until", "") or "").strip()))
        else:
            diags.error("LWD012", rel, items.line_of(i), "formerly entries need a name")
    equivalents = []
    items = r.list("equivalents")
    for i, item in enumerate(items):
        line = items.line_of(i)
        if not isinstance(item, dict):
            diags.error("LWD012", rel, line, "equivalents entries are {term, fidelity, note}")
            continue
        fid = str(item.get("fidelity", "")).strip()
        if fid not in tax.ids("fidelity"):
            diags.error("LWD013", rel, line, f"fidelity '{fid}' is not one of {', '.join(tax.ids('fidelity'))}", suggest(fid, tax.ids("fidelity")))
            continue
        equivalents.append(Equivalent(str(item.get("term", "") or "").strip(), fid, str(item.get("note", "") or "").strip(), line))
    contrasts = []
    items = r.list("differs_from")
    for i, item in enumerate(items):
        line = items.line_of(i) if hasattr(items, "line_of") else r.line("differs_from")
        if isinstance(item, str):
            contrasts.append(Contrast(item.strip(), "", line))
        elif isinstance(item, dict) and item.get("term"):
            contrasts.append(Contrast(str(item["term"]).strip(), str(item.get("note", "") or "").strip(), line))
        else:
            diags.error("LWD012", rel, line, "differs_from entries are slugs or {term, note}")
    status = r.enum("status", STATUSES, required=True, default="draft")
    secs = mdscan.sections(doc.body, doc.body_line, TERM_SECTIONS)
    qs: list[mdscan.Question] = []
    for s in secs:
        if s.canonical == "self-check":
            qs.extend(mdscan.questions(s.text, s.line + 1))
    term = Term(
        slug=slug,
        title=r.str("title", required=True),
        summary=r.str("summary", required=True),
        acronyms=r.str_list("acronyms"),
        aliases=r.str_list("aliases"),
        formerly=formerly,
        tracks=r.enum_list("tracks", tax.ids("tracks"), required=True),
        domain=r.enum("domain", tax.ids("term_domains"), required=True),
        cloud=r.enum("cloud", tax.ids("clouds"), required=True, default="neutral"),
        level=r.enum("level", tax.ids("levels"), required=True),
        status=status,
        superseded_by=r.str("superseded_by"),
        last_verified=r.date("last_verified", lib.today),
        volatility=r.enum("volatility", list(tax.volatility)),
        concept=r.str("concept"),
        equivalents=equivalents,
        differs_from=contrasts,
        related=r.str_list("related"),
        covers=_covers(r),
        sources=_sources(r),
        uid=r.str("uid"),
        tooltip=r.str("tooltip"),
        sections=secs,
        questions=qs,
        links=mdscan.links(doc.body, doc.body_line),
        origin=origin,
    )
    r.finish(TERM_KEYS)
    for h in mdscan.headings(doc.body, doc.body_line):
        if h[0] == 1:
            diags.error("LWD075", rel, h[3], "term bodies must not contain an H1; the title comes from front matter")
    seen: set[str] = set()
    for s in secs:
        if s.canonical not in TERM_SECTION_ORDER:
            diags.warn("LWD075", rel, s.line, f"unknown H2 '{s.title}' (kept as-is)", "expected: " + ", ".join(TERM_SECTION_TITLES.values()))
        elif s.canonical in seen:
            diags.error("LWD075", rel, s.line, f"duplicate section '{s.title}'")
        seen.add(s.canonical)
    return term


def classify_page(page: str, tax: Taxonomy) -> tuple[str, str, str, str, str | None]:
    """Return (kind, area, domain, group, problem) for a rendered page path."""
    parts = page.split("/")
    name = parts[-1]
    if len(parts) == 1:
        return ("meta", "", "", "", None if name == "index.md" else "pages at the docs root must be index.md")
    area = parts[0]
    if area == "about":
        return ("meta", "about", "", "", None)
    spec = tax.areas.get(area)
    if spec is None:
        return ("article", area, "", "", f"'{area}/' is not an area in taxonomy.yml")
    kind = "index" if name == "index.md" else "article"
    if len(parts) == 2:
        if kind == "article" and not spec.root_pages:
            return (kind, area, "", "", f"area '{area}' does not allow pages at its root; move it into a domain folder")
        return (kind, area, "", "", None)
    domain = parts[1]
    if domain not in spec.domains:
        return (kind, area, domain, "", f"'{area}/{domain}/' is not a domain in taxonomy.yml")
    if len(parts) == 3:
        return (kind, area, domain, "", None)
    group = parts[2]
    if group not in spec.groups.get(domain, {}):
        return (kind, area, domain, group, f"'{area}/{domain}/{group}/' is not a group in taxonomy.yml")
    if len(parts) == 4:
        return (kind, area, domain, group, None)
    return (kind, area, domain, group, "pages may be at most three folders deep")


def load_article(path: Path, page: str, lib: Library, diags: Diagnostics) -> Article | None:
    rel = f"{lib.config.docs_dir}/{page}"
    doc = _read_doc(path, rel, diags)
    if doc is None:
        return None
    tax = lib.taxonomy
    kind, area, domain, group, problem = classify_page(page, tax)
    if problem:
        diags.error("LWD092", rel, 0, problem)
    origin = Origin(rel, doc.meta, doc.body, doc.body_line)
    r = Reader(origin, diags, strict_keys=False)
    is_article = kind == "article"
    clouds = r.enum_list("clouds", [c for c in tax.ids("clouds") if c != "neutral"])
    heads = {h[2]: h[3] for h in mdscan.headings(doc.body, doc.body_line)}
    art = Article(
        page=page,
        title=r.str("title", required=True),
        description=r.str("description", required=kind != "meta"),
        status=r.enum("status", STATUSES, default="draft" if is_article else ""),
        level=r.enum("level", tax.ids("levels"), required=is_article),
        tracks=r.enum_list("tracks", tax.ids("tracks")),
        clouds=clouds,
        compares=r.str_list("compares"),
        covers=_covers(r),
        last_verified=r.date("last_verified", lib.today),
        volatility=r.enum("volatility", list(tax.volatility)),
        tags=r.str_list("tags"),
        area=area,
        domain=domain,
        group=group,
        kind=kind,
        headings=heads,
        links=mdscan.links(doc.body, doc.body_line),
        word_count=mdscan.word_count(doc.body),
        origin=origin,
    )
    r.finish(ARTICLE_KEYS | ZENSICAL_KEYS)
    if is_article and not art.tracks:
        diags.warn("LWD011", rel, doc.meta.line, "article has no 'tracks'", "add one or more of " + ", ".join(tax.ids("tracks")))
    return art


def load_exam(path: Path, rel: str, lib: Library, diags: Diagnostics) -> Exam | None:
    doc = _read_doc(path, rel, diags)
    if doc is None:
        return None
    tax = lib.taxonomy
    origin = Origin(rel, doc.meta, doc.body, doc.body_line)
    r = Reader(origin, diags, strict_keys=True)
    slug = path.stem
    code = r.str("code", required=True)
    if code and code.lower() != slug:
        diags.error("LWD020", rel, r.line("code"), f"exam file name '{slug}' must equal the lower-cased code '{code.lower()}'")
    objectives: list[Objective] = []
    items = r.list("objectives")
    seen: set[str] = set()
    for i, item in enumerate(items):
        line = items.line_of(i)
        if not isinstance(item, dict) or "id" not in item or "title" not in item:
            diags.error("LWD050", rel, line, "objectives entries need id and title")
            continue
        oid = str(item["id"]).strip()
        if not OBJ_ID.match(oid):
            diags.error("LWD050", rel, line, f"objective id '{oid}' must look like 1, 1.2 or 1.2.3 (quote it)")
            continue
        if oid in seen:
            diags.error("LWD050", rel, line, f"duplicate objective id '{oid}'")
            continue
        obj = Objective(oid, str(item["title"]).strip(), str(item.get("weight", "") or "").strip(), line)
        if obj.parent and obj.parent not in seen:
            diags.error("LWD050", rel, line, f"objective '{oid}' appears before (or without) its parent '{obj.parent}'")
        if obj.weight and obj.parent:
            diags.error("LWD051", rel, line, "weights belong on top-level objectives only")
        seen.add(oid)
        objectives.append(obj)
    exam = Exam(
        slug=slug,
        code=code,
        title=r.str("title", required=True),
        credential=r.str("credential"),
        provider=r.enum("provider", tax.ids("providers"), required=True),
        tracks=r.enum_list("tracks", tax.ids("tracks")),
        clouds=r.enum_list("clouds", tax.ids("clouds")),
        level=r.enum("level", tax.exam_levels, required=True),
        tier=r.enum("tier", TIERS, required=True),
        stage=r.str("stage"),
        progress=r.enum("progress", PROGRESS, default="planned"),
        target_date=r.date("target_date", lib.today, allow_future=True),
        passed_on=r.date("passed_on", lib.today),
        official_url=r.str("official_url", required=True),
        study_guide_url=r.str("study_guide_url"),
        outline_version=r.str("outline_version"),
        last_verified=r.date("last_verified", lib.today),
        retires_on=r.date("retires_on", lib.today, allow_future=True),
        provisional=r.boolean("provisional"),
        prerequisites=[s.lower() for s in r.str_list("prerequisites")],
        replaces=r.str("replaces").lower(),
        replaced_by=r.str("replaced_by").lower(),
        counterparts=[s.lower() for s in r.str_list("counterparts")],
        objectives=objectives,
        sections=mdscan.sections(doc.body, doc.body_line, {}),
        origin=origin,
        prerequisites_any=[s.lower() for s in r.str_list("prerequisites_any")],
        prerequisite_note=r.str("prerequisite_note"),
    )
    r.finish(EXAM_KEYS)
    if exam.progress == "passed" and not exam.passed_on:
        diags.warn("LWD011", rel, r.line("progress"), "progress 'passed' without passed_on: renewal dates cannot be tracked", "add passed_on: YYYY-MM-DD")
    tops = [o for o in objectives if not o.parent and o.weight]
    # Only check weights expressed as percentages; some vendors publish question counts.
    if tops and all("%" in o.weight for o in tops):
        total = 0.0
        for o in tops:
            nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", o.weight)]
            if nums:
                total += sum(nums) / len(nums)
        if not 90 <= total <= 110:
            diags.warn("LWD051", rel, tops[0].line, f"top-level weight midpoints sum to {total:.0f}%, expected about 100%")
    return exam


def load_path(path: Path, rel: str, lib: Library, diags: Diagnostics) -> LearningPath | None:
    doc = _read_doc(path, rel, diags)
    if doc is None:
        return None
    tax = lib.taxonomy
    origin = Origin(rel, doc.meta, doc.body, doc.body_line)
    r = Reader(origin, diags, strict_keys=True)
    steps: list[Step] = []
    items = r.list("steps", required=True)
    for i, item in enumerate(items):
        line = items.line_of(i)
        if not isinstance(item, dict):
            diags.error("LWD060", rel, line, "steps entries are mappings with one of term, page, objective, check")
            continue
        kinds = [k for k in ("term", "page", "objective", "check") if item.get(k)]
        if len(kinds) != 1:
            diags.error("LWD060", rel, line, "each step needs exactly one of term, page, objective, check")
            continue
        minutes = item.get("minutes")
        try:
            mins = int(str(minutes)) if minutes is not None else None
        except ValueError:
            diags.error("LWD012", rel, line, "minutes must be a whole number")
            mins = None
        steps.append(Step(kinds[0], str(item[kinds[0]]).strip(), mins, str(item.get("note", "") or "").strip(), line))
    lp = LearningPath(
        slug=path.stem,
        title=r.str("title", required=True),
        summary=r.str("summary", required=True),
        tracks=r.enum_list("tracks", tax.ids("tracks")),
        level=r.enum("level", tax.ids("levels")),
        exams=[s.lower() for s in r.str_list("exams")],
        status=r.enum("status", STATUSES, default="draft"),
        steps=steps,
        body=doc.body,
        origin=origin,
    )
    r.finish(PATH_KEYS)
    return lp


def discover(lib: Library, diags: Diagnostics) -> None:
    """Populate the library from docs/."""
    cfg: SiteConfig = lib.config
    docs = cfg.docs
    for path in sorted(docs.rglob("*")):
        if not path.is_file():
            continue
        page = path.relative_to(docs).as_posix()
        parts = page.split("/")
        if any(p.startswith(".") for p in parts):
            continue
        top = parts[0]
        if top in GENERATED_DIRS:
            continue
        rel = f"{cfg.docs_dir}/{page}"
        if top.startswith("_"):
            if top not in SOURCE_DIRS:
                diags.warn("LWD092", rel, 0, f"unknown source directory '{top}/' (ignored)")
                continue
            if not page.endswith(".md"):
                continue
            if top == "_terms" and len(parts) == 2 and parts[1] != "index.md":
                term = load_term(path, rel, lib, diags)
                if term:
                    lib.terms[term.slug] = term
            elif top == "_study" and len(parts) == 3 and parts[1] == "exams":
                exam = load_exam(path, rel, lib, diags)
                if exam:
                    lib.exams[exam.slug] = exam
            elif top == "_study" and len(parts) == 3 and parts[1] == "paths":
                lp = load_path(path, rel, lib, diags)
                if lp:
                    lib.paths[lp.slug] = lp
            elif top in ("_glossary", "_study"):
                doc = _read_doc(path, rel, diags)
                if doc is not None:
                    lib.frames[page[1:]] = doc.body
            continue
        if cfg.is_excluded(page):
            continue
        if page.endswith(".md"):
            art = load_article(path, page, lib, diags)
            if art:
                lib.articles[page] = art
        else:
            lib.static_files.add(page)


def load_backlog(lib: Library, diags: Diagnostics) -> None:
    """Planning data in docs/_data/backlog/*.json (or hand-written *.yml)."""
    folder = lib.config.docs / "_data" / "backlog"
    if not folder.is_dir():
        return
    for path in sorted(folder.iterdir()):
        if path.suffix not in (".json", ".yml"):
            continue
        rel = f"{lib.config.docs_dir}/_data/backlog/{path.name}"
        text, _ = yamlio.read_text(path.read_bytes())
        try:
            data = json.loads(text) if path.suffix == ".json" else yamlio.load(text)
        except json.JSONDecodeError as exc:
            diags.error("LWD001", rel, exc.lineno, f"backlog: {exc.msg}")
            continue
        except yamlio.YamlError as exc:
            diags.error("LWD001", rel, exc.line, f"backlog: {exc}")
            continue
        lib.backlog[path.stem] = data
