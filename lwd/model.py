"""The in-memory library: terms, rendered pages, exams and learning paths."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from lwd.config import SiteConfig
from lwd.mdscan import Link, Question, Section
from lwd.taxonomy import Taxonomy
from lwd.yamlio import LineDict


@dataclass
class Origin:
    """Where an entity came from, for diagnostics."""

    path: str  # repo-relative, e.g. docs/_terms/entra-id.md
    meta: LineDict
    body: str
    body_line: int

    def line(self, key: str) -> int:
        return self.meta.line_of(key) if key in self.meta else self.meta.line


@dataclass
class Formerly:
    name: str
    acronym: str = ""
    until: str = ""


@dataclass
class Equivalent:
    term: str  # slug on the other cloud, or "" when fidelity is none
    fidelity: str
    note: str = ""
    line: int = 0


@dataclass
class Contrast:
    term: str
    note: str = ""
    line: int = 0


@dataclass
class Cover:
    ref: str  # exam-slug:objective-id
    anchor: str = ""
    depth: str = "full"
    line: int = 0

    @property
    def exam(self) -> str:
        return self.ref.split(":", 1)[0]

    @property
    def objective(self) -> str:
        return self.ref.split(":", 1)[1] if ":" in self.ref else ""


@dataclass
class SourceRef:
    title: str
    url: str
    publisher: str = ""


@dataclass
class Term:
    slug: str
    title: str
    summary: str
    acronyms: list[str]
    aliases: list[str]
    formerly: list[Formerly]
    tracks: list[str]
    domain: str
    cloud: str
    level: str
    status: str
    superseded_by: str
    last_verified: date | None
    volatility: str
    concept: str
    equivalents: list[Equivalent]
    differs_from: list[Contrast]
    related: list[str]
    covers: list[Cover]
    sources: list[SourceRef]
    uid: str
    tooltip: str
    sections: list[Section]
    questions: list[Question]
    links: list[Link]
    origin: Origin

    @property
    def page(self) -> str:
        """Docs-relative path of the compiled page."""
        return f"terms/{self.slug}.md"

    def section(self, name: str) -> Section | None:
        return next((s for s in self.sections if s.canonical == name), None)


@dataclass
class Article:
    """A rendered-as-is page under docs/ (articles, indexes, practice, about)."""

    page: str  # docs-relative
    title: str
    description: str
    status: str
    level: str
    tracks: list[str]
    clouds: list[str]
    compares: list[str]
    covers: list[Cover]
    last_verified: date | None
    volatility: str
    tags: list[str]
    area: str
    domain: str
    group: str
    kind: str  # article | index | meta
    headings: dict[str, int]  # heading id -> line
    links: list[Link]
    word_count: int
    origin: Origin


@dataclass
class Objective:
    id: str
    title: str
    weight: str = ""
    line: int = 0

    @property
    def parent(self) -> str:
        return self.id.rsplit(".", 1)[0] if "." in self.id else ""

    @property
    def depth(self) -> int:
        return self.id.count(".") + 1

    @property
    def anchor(self) -> str:
        return "obj-" + self.id.replace(".", "-")

    @property
    def link_anchor(self) -> str:
        """Anchor to link to: only depth 1-2 objectives render as headings
        (Zensical registers heading ids as anchors, not list-item ids)."""
        if self.depth <= 2:
            return self.anchor
        return "obj-" + "-".join(self.id.split(".")[:2])


@dataclass
class Exam:
    slug: str
    code: str
    title: str
    credential: str
    provider: str
    tracks: list[str]
    clouds: list[str]
    level: str
    tier: str
    stage: str
    progress: str
    target_date: date | None
    passed_on: date | None
    official_url: str
    study_guide_url: str
    outline_version: str
    last_verified: date | None
    retires_on: date | None
    provisional: bool
    prerequisites: list[str]
    replaces: str
    replaced_by: str
    counterparts: list[str]
    objectives: list[Objective]
    sections: list[Section]
    origin: Origin
    prerequisites_any: list[str] = field(default_factory=list)
    prerequisite_note: str = ""

    @property
    def page(self) -> str:
        return f"study/exams/{self.slug}.md"

    def objective(self, oid: str) -> Objective | None:
        return next((o for o in self.objectives if o.id == oid), None)

    def leaves(self) -> list[Objective]:
        parents = {o.parent for o in self.objectives if o.parent}
        return [o for o in self.objectives if o.id not in parents]


@dataclass
class Step:
    kind: str  # term | page | objective | check
    target: str
    minutes: int | None = None
    note: str = ""
    line: int = 0


@dataclass
class LearningPath:
    slug: str
    title: str
    summary: str
    tracks: list[str]
    level: str
    exams: list[str]
    status: str
    steps: list[Step]
    body: str
    origin: Origin

    @property
    def page(self) -> str:
        return f"study/paths/{self.slug}.md"


@dataclass
class Library:
    config: SiteConfig
    taxonomy: Taxonomy
    today: date
    terms: dict[str, Term] = field(default_factory=dict)
    articles: dict[str, Article] = field(default_factory=dict)
    exams: dict[str, Exam] = field(default_factory=dict)
    paths: dict[str, LearningPath] = field(default_factory=dict)
    frames: dict[str, str] = field(default_factory=dict)  # output page -> frame body
    static_files: set[str] = field(default_factory=set)  # docs-relative non-md files
    backlog: dict[str, dict] = field(default_factory=dict)  # section -> raw backlog data
