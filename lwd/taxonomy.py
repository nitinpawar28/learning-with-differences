"""Controlled vocabularies (docs/_data/taxonomy.yml, abbreviations.yml)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from lwd import yamlio


@dataclass
class Vocab:
    id: str
    label: str
    extra: dict = field(default_factory=dict)


@dataclass
class Area:
    id: str
    label: str
    root_pages: bool
    domains: dict[str, str]  # domain id -> label
    groups: dict[str, dict[str, str]]  # domain id -> {group id -> label}
    tracks: list[str]


@dataclass
class Taxonomy:
    tracks: list[Vocab]
    clouds: list[Vocab]
    levels: list[Vocab]
    fidelity: list[Vocab]
    volatility: dict[str, int]
    term_domains: list[Vocab]
    areas: dict[str, Area]
    providers: list[Vocab]
    exam_levels: list[str]
    settings: dict
    abbreviations: dict = field(default_factory=dict)

    # -- lookups -----------------------------------------------------------
    def ids(self, kind: str) -> list[str]:
        return [t.id for t in getattr(self, kind)]

    def label(self, kind: str, value: str) -> str:
        for t in getattr(self, kind):
            if t.id == value:
                return t.label
        return value

    def fidelity_rank(self, value: str) -> int:
        for t in self.fidelity:
            if t.id == value:
                return int(t.extra.get("rank", 0))
        return -1

    def domain_volatility(self, domain: str) -> str | None:
        for t in self.term_domains:
            if t.id == domain:
                return t.extra.get("volatility")
        return None

    def provider(self, pid: str) -> Vocab | None:
        return next((p for p in self.providers if p.id == pid), None)


class TaxonomyError(Exception):
    def __init__(self, message: str, path: str, line: int = 0) -> None:
        super().__init__(message)
        self.path = path
        self.line = line


def _terms(data, key: str, path: str) -> list[Vocab]:
    items = data.get(key) or []
    out = []
    for i, item in enumerate(items):
        if not isinstance(item, dict) or "id" not in item:
            raise TaxonomyError(f"{key}[{i}] needs an id", path, items.line_of(i))
        extra = {k: v for k, v in item.items() if k not in ("id", "label")}
        out.append(Vocab(str(item["id"]), str(item.get("label", item["id"])), extra))
    return out


def load_taxonomy(docs: Path) -> Taxonomy:
    rel = "docs/_data/taxonomy.yml"
    path = docs / "_data" / "taxonomy.yml"
    text, _ = yamlio.read_text(path.read_bytes())
    try:
        data = yamlio.load(text)
    except yamlio.YamlError as exc:
        raise TaxonomyError(str(exc), rel, exc.line) from exc
    areas: dict[str, Area] = {}
    for aid, spec in (data.get("areas") or {}).items():
        domains: dict[str, str] = {}
        groups: dict[str, dict[str, str]] = {}
        for did, dspec in (spec.get("domains") or {}).items():
            if isinstance(dspec, dict):
                domains[did] = str(dspec.get("label", did))
                groups[did] = {gid: str(glabel) for gid, glabel in (dspec.get("groups") or {}).items()}
            else:
                domains[did] = str(dspec)
        areas[aid] = Area(
            id=aid,
            label=str(spec.get("label", aid)),
            root_pages=bool(spec.get("root_pages", False)),
            domains=domains,
            groups=groups,
            tracks=list(spec.get("tracks") or []),
        )
    tax = Taxonomy(
        tracks=_terms(data, "tracks", rel),
        clouds=_terms(data, "clouds", rel),
        levels=_terms(data, "levels", rel),
        fidelity=_terms(data, "fidelity", rel),
        volatility={str(v["id"]): int(v["days"]) for v in (data.get("volatility") or [])},
        term_domains=_terms(data, "term_domains", rel),
        areas=areas,
        providers=_terms(data, "providers", rel),
        exam_levels=[str(x) for x in (data.get("exam_levels") or [])],
        settings=dict(data.get("settings") or {}),
    )
    abbr_path = docs / "_data" / "abbreviations.yml"
    if abbr_path.is_file():
        text, _ = yamlio.read_text(abbr_path.read_bytes())
        try:
            tax.abbreviations = dict(yamlio.load(text) or {})
        except yamlio.YamlError as exc:
            raise TaxonomyError(str(exc), "docs/_data/abbreviations.yml", exc.line) from exc
    return tax
