"""Cross-entity checks, plus link / nav / reachability checks on the output."""

from __future__ import annotations

import posixpath
import re
from collections import deque
from urllib.parse import urlparse

from lwd import derive, mdscan, paths
from lwd.diag import Diagnostics
from lwd.load import TERM_SECTION_TITLES, suggest
from lwd.model import Cover, Library

PRIMARY_DEFAULT = ("learn.microsoft.com", "docs.aws.amazon.com", "aws.amazon.com")


def _cover_problems(lib: Library, covers: list[Cover], rel: str, diags: Diagnostics) -> None:
    for c in covers:
        exam = lib.exams.get(c.exam)
        if exam is None:
            diags.error("LWD052", rel, c.line, f"covers '{c.ref}': unknown exam '{c.exam}'", suggest(c.exam, lib.exams))
        elif c.objective and exam.objective(c.objective) is None:
            diags.error("LWD052", rel, c.line, f"covers '{c.ref}': exam {exam.code} has no objective '{c.objective}'", suggest(c.objective, [o.id for o in exam.objectives]))


def check_library(lib: Library, diags: Diagnostics) -> None:
    terms = lib.terms
    tax = lib.taxonomy

    # Names must identify one term.
    owners: dict[str, list[tuple[str, str]]] = {}
    for t in terms.values():
        names = [("title", t.title)] + [("alias", a) for a in t.aliases] + [("formerly", f.name) for f in t.formerly]
        seen_local: set[str] = set()
        for kind, name in names:
            key = name.casefold().strip()
            if not key:
                continue
            if key in seen_local:
                diags.warn("LWD023", t.origin.path, t.origin.line("aliases"), f"'{name}' is listed more than once")
                continue
            seen_local.add(key)
            owners.setdefault(key, []).append((t.slug, kind))
    for key, who in owners.items():
        slugs = sorted({s for s, _ in who})
        if len(slugs) > 1:
            for slug in slugs:
                t = terms[slug]
                diags.error("LWD022", t.origin.path, t.origin.meta.line, f"name '{key}' is used by several terms: {', '.join(slugs)}", "make titles, aliases and former names unique")

    primary = tuple(tax.settings.get("primary_source_hosts") or PRIMARY_DEFAULT)
    for t in terms.values():
        rel = t.origin.path
        # References.
        for eq in t.equivalents:
            if eq.fidelity == "none":
                if eq.term:
                    diags.error("LWD031", rel, eq.line, "an equivalent with fidelity 'none' must not name a term")
                if not eq.note:
                    diags.error("LWD031", rel, eq.line, "fidelity 'none' needs a note explaining the gap")
                continue
            other = terms.get(eq.term)
            if other is None:
                diags.error("LWD030", rel, eq.line, f"equivalent '{eq.term}' is not a term", suggest(eq.term, terms))
            elif t.cloud not in ("azure", "aws"):
                diags.error("LWD031", rel, eq.line, "only azure or aws terms declare equivalents; neutral terms use 'concept' links from the cloud terms")
            elif other.cloud == t.cloud or other.cloud not in ("azure", "aws"):
                diags.error("LWD031", rel, eq.line, f"equivalent '{eq.term}' is {other.cloud}; it must be on the other cloud")
        if t.concept:
            c = terms.get(t.concept)
            if c is None:
                diags.error("LWD030", rel, t.origin.line("concept"), f"concept '{t.concept}' is not a term", suggest(t.concept, terms))
            elif c.cloud != "neutral":
                diags.error("LWD032", rel, t.origin.line("concept"), f"concept '{t.concept}' must be a vendor-neutral term")
        for c in t.differs_from:
            if c.term == t.slug:
                diags.error("LWD030", rel, c.line, "a term cannot differ from itself")
            elif c.term not in terms:
                diags.error("LWD030", rel, c.line, f"differs_from '{c.term}' is not a term", suggest(c.term, terms))
        for i, slug in enumerate(t.related):
            if slug not in terms:
                diags.error("LWD030", rel, t.origin.line("related"), f"related '{slug}' is not a term", suggest(slug, terms))
        if t.status == "deprecated":
            if not t.superseded_by:
                diags.error("LWD070", rel, t.origin.line("status"), "deprecated terms need superseded_by")
            elif t.superseded_by not in terms:
                diags.error("LWD030", rel, t.origin.line("superseded_by"), f"superseded_by '{t.superseded_by}' is not a term")
        _cover_problems(lib, t.covers, rel, diags)

        # Completeness and quality.
        if t.status == "complete":
            need = ["explanation", "examples", "misconceptions", "self-check"] + (["exam-notes"] if t.covers else [])
            for name in need:
                s = t.section(name)
                if s is None or not s.text.strip():
                    diags.error("LWD070", rel, t.origin.body_line, f"complete term is missing the '{TERM_SECTION_TITLES[name]}' section")
            if not t.sources:
                diags.error("LWD070", rel, t.origin.meta.line, "complete term needs at least one source")
            if t.last_verified is None:
                diags.error("LWD070", rel, t.origin.meta.line, "complete term needs last_verified")
            if t.cloud in ("azure", "aws") and not t.equivalents:
                diags.warn("LWD071", rel, t.origin.meta.line, "cloud term has no equivalents on the other cloud", "add one, or a {fidelity: none, note: ...} entry")
            if not t.differs_from:
                diags.warn("LWD072", rel, t.origin.meta.line, "term has no differs_from contrasts")
            if not t.questions:
                diags.warn("LWD070", rel, t.origin.body_line, "Self-check has no '??? question' blocks")
            hosts = {urlparse(s.url).hostname or "" for s in t.sources}
            if t.cloud != "neutral" and not any(h == p or h.endswith("." + p) for h in hosts for p in primary):
                diags.warn("LWD074", rel, t.origin.line("sources"), "no source from a primary-source host", "cite official documentation")
        if t.summary and not 40 <= len(t.summary) <= 300:
            diags.warn("LWD073", rel, t.origin.line("summary"), f"summary is {len(t.summary)} characters; aim for 40–300")
        if re.search(r"\]\(|<a\s|https?://", t.summary or ""):
            diags.warn("LWD073", rel, t.origin.line("summary"), "summary should be plain text without links")

    # Symmetry warnings.
    for t in terms.values():
        for c in t.differs_from:
            other = terms.get(c.term)
            if other and not any(x.term == t.slug for x in other.differs_from):
                diags.warn("LWD033", other.origin.path, other.origin.line("differs_from"), f"'{t.slug}' says it differs from '{other.slug}', but not vice versa",
                           f"add to {other.origin.path}:  - {{ term: {t.slug}, note: \"...\" }}")
        for eq in t.equivalents:
            other = terms.get(eq.term)
            if not other or eq.fidelity == "none":
                continue
            back = [x for x in other.equivalents if x.term == t.slug]
            if not back:
                diags.warn("LWD034", other.origin.path, other.origin.line("equivalents"), f"'{t.slug}' lists '{other.slug}' as an equivalent, but not vice versa",
                           f"add to {other.origin.path}:  - {{ term: {t.slug}, fidelity: {eq.fidelity}, note: \"...\" }}")
            elif back[0].fidelity != eq.fidelity and t.slug < other.slug:
                diags.warn("LWD034", t.origin.path, eq.line, f"fidelity disagrees with '{other.slug}' ({eq.fidelity} vs {back[0].fidelity}); the lower one is shown")

    # Acronyms.
    senses, skipped = derive.senses(lib)
    for code, acr, reason in skipped:
        owner = next((t for t in terms.values() if acr in t.acronyms), None)
        where = owner.origin.path if owner else "docs/_data/abbreviations.yml"
        if code == "LWD040":
            diags.error(code, where, owner.origin.line("acronyms") if owner else 0, f"acronym '{acr}' can never match: {reason}")
        elif code == "LWD042":
            diags.warn(code, where, owner.origin.line("acronyms") if owner else 0, f"acronym '{acr}' skipped: {reason}", "add it to allow_short in abbreviations.yml")
        else:
            diags.info(code, where, 0, f"acronym '{acr}' skipped: {reason}")
    folded: dict[str, set[str]] = {}
    for acr in senses:
        folded.setdefault(acr.casefold(), set()).add(acr)
    for variants in folded.values():
        if len(variants) > 1:
            diags.warn("LWD044", "docs/_data/abbreviations.yml", 0, f"acronyms differ only by case: {', '.join(sorted(variants))}")
    for acr, items in senses.items():
        if len(items) > 1:
            diags.info("LWD043", "docs/_data/abbreviations.yml", 0, f"'{acr}' has {len(items)} senses; tooltip shows all")
    limit = int(tax.settings.get("abbr_soft_limit", 800))
    if len(senses) > limit:
        diags.warn("LWD041", "docs/_data/abbreviations.yml", 0, f"{len(senses)} acronyms exceed the soft limit of {limit}; tooltips slow every page")

    # Articles.
    for a in lib.articles.values():
        rel = a.origin.path
        for slug in a.compares:
            if slug not in terms:
                diags.error("LWD030", rel, a.origin.line("compares"), f"compares '{slug}' is not a term", suggest(slug, terms))
        _cover_problems(lib, a.covers, rel, diags)
        if a.status == "complete" and a.kind == "article" and a.last_verified is None and (a.clouds or "agentic-ai" in a.tracks):
            diags.error("LWD070", rel, a.origin.meta.line, "complete cloud/AI article needs last_verified")

    # Exams.
    for e in lib.exams.values():
        rel = e.origin.path
        for slug in e.prerequisites + e.prerequisites_any:
            if slug not in lib.exams:
                diags.error("LWD030", rel, e.origin.line("prerequisites"), f"prerequisite exam '{slug}' has no exam file", suggest(slug, lib.exams))
        for slug in e.counterparts:
            if slug not in lib.exams:
                diags.warn("LWD030", rel, e.origin.line("counterparts"), f"counterpart exam '{slug}' has no exam file", suggest(slug, lib.exams))
        if e.tier != "skip" and not e.objectives:
            diags.warn("LWD050", rel, e.origin.meta.line, f"{e.code} has no objectives yet; coverage cannot be tracked")

    # Learning paths.
    for lp in lib.paths.values():
        rel = lp.origin.path
        for slug in lp.exams:
            if slug not in lib.exams:
                diags.error("LWD030", rel, lp.origin.line("exams"), f"exam '{slug}' has no exam file", suggest(slug, lib.exams))
        for st in lp.steps:
            if st.kind == "term" and st.target not in terms:
                diags.error("LWD030", rel, st.line, f"step term '{st.target}' is not a term", suggest(st.target, terms))
            elif st.kind == "page" and st.target not in lib.articles:
                diags.error("LWD030", rel, st.line, f"step page '{st.target}' does not exist (docs-relative path)", suggest(st.target, lib.articles))
            elif st.kind == "objective":
                _cover_problems(lib, [Cover(st.target.lower(), line=st.line)], rel, diags)


# --- output-level checks -----------------------------------------------------

def _strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def _page_headings(text: str) -> set[str]:
    return {h[2] for h in mdscan.headings(text)} | set(re.findall(r'\{[^}]*#([A-Za-z0-9_\-:.]+)', text)) | set(re.findall(r'id="([^"]+)"', text))


def check_output(lib: Library, outputs: dict[str, str], diags: Diagnostics) -> None:
    """Links, nav and reachability over authored pages plus generated output."""
    cfg = lib.config
    pages: dict[str, str] = {}  # docs-relative md page -> markdown text (for anchors)
    for p, a in lib.articles.items():
        pages[p] = a.origin.body
    for p, text in outputs.items():
        if p.endswith(".md") and not p.startswith("../"):
            pages[p] = _strip_front_matter(text)
    statics = set(lib.static_files) | {p for p in outputs if not p.endswith(".md") and not p.startswith("../")}
    lower_index = {p.lower(): p for p in list(pages) + list(statics)}
    heading_cache: dict[str, set[str]] = {}

    def anchors(page: str) -> set[str]:
        if page not in heading_cache:
            heading_cache[page] = _page_headings(pages.get(page, ""))
        return heading_cache[page]

    def check_links(src_page: str, rel: str, links) -> None:
        for link in links:
            if link.is_external:
                continue
            if not link.path:
                if link.fragment and link.fragment not in anchors(src_page):
                    diags.warn("LWD081", rel, link.line, f"anchor '#{link.fragment}' not found on this page")
                continue
            target = paths.resolve(src_page, link.path)
            if target.startswith("../"):
                diags.error("LWD080", rel, link.line, f"link '{link.target}' leaves the docs directory")
                continue
            top = target.split("/", 1)[0]
            if top.startswith("_"):
                diags.error("LWD082", rel, link.line, f"link '{link.target}' points into the source directory {top}/",
                            "link to the compiled page instead, e.g. terms/<slug>.md or study/exams/<code>.md")
                continue
            if target in pages or target in statics:
                if link.fragment and target in pages and link.fragment not in anchors(target):
                    diags.warn("LWD081", rel, link.line, f"anchor '#{link.fragment}' not found in {target}")
                continue
            if target.lower() in lower_index:
                diags.error("LWD083", rel, link.line, f"link '{link.target}' has the wrong case; the file is {lower_index[target.lower()]}")
                continue
            hint = suggest(target, list(pages) + list(statics))
            if target.endswith("/") or "." not in posixpath.basename(target):
                hint = "link to the .md file (e.g. folder/index.md), not a folder"
            diags.error("LWD080", rel, link.line, f"broken link '{link.target}' (resolves to {target})", hint)

    for a in lib.articles.values():
        check_links(a.page, a.origin.path, a.links)
    for t in lib.terms.values():
        check_links(t.page, t.origin.path, t.links)
    for lp in lib.paths.values():
        check_links(lp.page, lp.origin.path, mdscan.links(lp.body, lp.origin.body_line))
    for e in lib.exams.values():
        check_links(e.page, e.origin.path, mdscan.links(e.origin.body, e.origin.body_line))
    for page, body in lib.frames.items():
        check_links(page, f"{cfg.docs_dir}/_{page}", mdscan.links(body))

    # Nav entries exist; authored pages are in nav or not_in_nav.
    nav_set = set(cfg.nav_pages)
    for p in cfg.nav_pages:
        if p not in pages:
            diags.error("LWD090", "zensical.toml", 0, f"nav entry '{p}' does not exist", suggest(p, pages))
    for p, a in lib.articles.items():
        if p not in nav_set and not cfg.is_not_in_nav(p):
            folder = posixpath.dirname(p)
            sibling = next((n for n in cfg.nav_pages if posixpath.dirname(n) == folder), None)
            where = f"next to '{sibling}'" if sibling else f"in the '{p.split('/')[0]}' section"
            diags.error("LWD091", a.origin.path, 0, "page is neither in the nav nor matched by not_in_nav", f"add \"{p}\" to the nav {where}")

    # Every generated page must be reachable from the nav.
    graph: dict[str, set[str]] = {}
    for page, text in pages.items():
        targets = set()
        for link in mdscan.links(text):
            if link.is_external or not link.path:
                continue
            t = paths.resolve(page, link.path)
            if t in pages:
                targets.add(t)
        graph[page] = targets
    seen = set(p for p in cfg.nav_pages if p in pages)
    queue = deque(seen)
    while queue:
        cur = queue.popleft()
        for nxt in graph.get(cur, ()):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    for p in outputs:
        if p.endswith(".md") and not p.startswith("../") and p not in seen:
            diags.error("LWD093", f"{cfg.docs_dir}/{p}", 0, "generated page is not reachable from the nav", "link it from a hub page")