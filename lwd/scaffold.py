"""`lwd new`: create a term, exam, path or article from a scaffold."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from lwd import yamlio
from lwd.load import SLUG

HERE = Path(__file__).parent / "scaffolds"


class ScaffoldError(Exception):
    pass


def _backlog_article(root: Path, page: str) -> dict | None:
    folder = root / "docs" / "_data" / "backlog"
    for path in sorted(folder.glob("*.yml")):
        data = yamlio.load(yamlio.read_text(path.read_bytes())[0]) or {}
        for a in data.get("articles") or []:
            if f"{str(a.get('folder', '')).strip('/')}/{a.get('slug', '')}.md" == page:
                return dict(a)
    return None


def _backlog_term(root: Path, slug: str) -> dict | None:
    folder = root / "docs" / "_data" / "backlog"
    for path in sorted(folder.glob("*.yml")):
        data = yamlio.load(yamlio.read_text(path.read_bytes())[0]) or {}
        for t in data.get("terms") or []:
            if str(t.get("slug", "")) == slug:
                return dict(t)
    return None


def _fill(template: str, values: dict[str, str]) -> str:
    return re.sub(r"\{\{(\w+)\}\}", lambda m: values.get(m.group(1), ""), template)


def _yaml_str(text: str) -> str:
    return '"' + (text or "").replace("\\", "\\\\").replace('"', '\\"') + '"'


def create(root: Path, kind: str, name: str, title: str | None, force: bool, from_backlog: bool) -> Path:
    docs = root / "docs"
    today = date.today().isoformat()
    if kind == "term":
        if not SLUG.match(name):
            raise ScaffoldError("term names are lowercase kebab-case slugs, e.g. managed-identity")
        target = docs / "_terms" / f"{name}.md"
        values = {"title": _yaml_str(title or name.replace("-", " ").title()), "summary": '""', "today": today, "cloud": "neutral", "level": "practitioner", "domain": "", "tracks": "[]", "aliases": "[]", "acronyms": "[]"}
        if from_backlog:
            t = _backlog_term(root, name)
            if not t:
                raise ScaffoldError(f"'{name}' is not in docs/_data/backlog")
            values.update({
                "title": _yaml_str(title or str(t.get("term", name))),
                "summary": _yaml_str(str(t.get("definition", ""))),
                "cloud": str(t.get("cloud", "neutral")),
                "level": str(t.get("level", "practitioner")),
                "domain": str(t.get("domain", "")),
                "tracks": "[" + ", ".join(t.get("tracks") or []) + "]",
                "aliases": "[" + ", ".join(_yaml_str(a) for a in (t.get("aliases") or []) if not str(a).startswith("formerly:")) + "]",
            })
        template = (HERE / "term.md").read_text(encoding="utf-8")
    elif kind == "exam":
        slug = name.lower()
        target = docs / "_study" / "exams" / f"{slug}.md"
        values = {"code": name.upper(), "title": _yaml_str(title or name.upper()), "today": today}
        template = (HERE / "exam.md").read_text(encoding="utf-8")
    elif kind == "path":
        if not SLUG.match(name):
            raise ScaffoldError("path names are lowercase kebab-case slugs")
        target = docs / "_study" / "paths" / f"{name}.md"
        values = {"title": _yaml_str(title or name.replace("-", " ").title())}
        template = (HERE / "path.md").read_text(encoding="utf-8")
    else:
        page = name.strip("/")
        if not page.endswith(".md"):
            page += ".md"
        target = docs / page
        values = {"title": _yaml_str(title or Path(page).stem.replace("-", " ").title()), "description": '""', "level": "practitioner", "covers": "[]", "scope": "Scope to be written."}
        if from_backlog:
            a = _backlog_article(root, page)
            if not a:
                raise ScaffoldError(f"'{page}' is not in docs/_data/backlog")
            values.update({
                "title": _yaml_str(title or str(a.get("title", ""))),
                "description": _yaml_str(str(a.get("scope", "")).split(". ")[0].rstrip(".") + "."),
                "level": str(a.get("level", "practitioner")),
                "scope": str(a.get("scope", "")),
            })
        template = (HERE / "article.md").read_text(encoding="utf-8")
    if target.exists() and not force:
        raise ScaffoldError(f"{target.relative_to(root).as_posix()} already exists (use --force to overwrite)")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(_fill(template, values), encoding="utf-8", newline="\n")
    return target
