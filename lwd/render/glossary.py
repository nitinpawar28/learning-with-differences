"""Glossary hub pages, facet pages, the Rosetta and Explorer data."""

from __future__ import annotations

import json
import re
import unicodedata

from lwd import derive
from lwd.model import Library, Term
from lwd.render import OutputSet
from lwd.render.common import cell, chip, facet_page, front_matter, inline, link, term_link, truncate

FACETS = ("track", "domain", "cloud", "level")
FIDELITY_LABEL = {"exact": "Exact", "close": "Close", "partial": "Partial", "none": "None"}
GENERATED = "lwd (glossary hub)"


def _frame(lib: Library, page: str, default: str) -> str:
    return lib.frames.get(page, default).strip() + "\n\n"


def _sort_key(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text)
    norm = "".join(ch for ch in norm if not unicodedata.combining(ch)).casefold()
    norm = re.sub(r"^[^0-9a-z]+", "", norm)
    return re.sub(r"\s+", " ", norm)


def _facet_values(lib: Library, facet: str) -> list[tuple[str, str]]:
    tax = lib.taxonomy
    kind = {"track": "tracks", "domain": "term_domains", "cloud": "clouds", "level": "levels"}[facet]
    return [(v.id, v.label) for v in getattr(tax, kind)]


def _members(lib: Library, facet: str, value: str) -> list[Term]:
    def has(t: Term) -> bool:
        if facet == "track":
            return value in t.tracks
        return getattr(t, facet) == value
    return sorted((t for t in lib.terms.values() if has(t)), key=lambda t: _sort_key(t.title))


def _term_row(page: str, lib: Library, t: Term) -> str:
    tax = lib.taxonomy
    acr = f" ({', '.join(inline(a) for a in t.acronyms)})" if t.acronyms else ""
    status = "" if t.status == "complete" else " " + chip("status", t.status, t.status.title())
    return (f"- {term_link(page, lib, t.slug)}{acr} {chip('cloud', t.cloud, tax.label('clouds', t.cloud))}"
            f"{status} — {inline(truncate(t.summary, 140))}")


def render_index(lib: Library, outputs: OutputSet) -> None:
    page = "glossary/index.md"
    n = len(lib.terms)
    complete = sum(1 for t in lib.terms.values() if t.status == "complete")
    by_cloud = {c: sum(1 for t in lib.terms.values() if t.cloud == c) for c in lib.taxonomy.ids("clouds")}
    default = (
        "Every recurring term in the library, defined once and taught by contrast: each entry says what the term "
        "is, what it is commonly confused with, and how it maps between Azure and AWS."
    )
    body = [front_matter({"title": "Glossary", "description": "Search, browse and compare every term in the library."}, GENERATED)]
    body.append("# Glossary\n\n")
    body.append(_frame(lib, page, default))
    body.append(f"**{n} terms** ({complete} complete) · "
                + " · ".join(f"{lib.taxonomy.label('clouds', c)}: {k}" for c, k in by_cloud.items()) + "\n\n")
    body.append('<div class="grid cards" markdown>\n\n')
    body.append("- :material-magnify: **" + link(page, "glossary/explorer.md", "Explorer") + "**\n\n    Search by name, acronym or former name; filter by track, cloud, domain, level, status and exam.\n\n")
    body.append("- :material-sort-alphabetical-ascending: **" + link(page, "glossary/a-z.md", "A–Z index") + "**\n\n    Every term and every alias, acronym and former name, alphabetically.\n\n")
    body.append("- :material-swap-horizontal: **" + link(page, "glossary/rosetta.md", "Azure ↔ AWS Rosetta") + "**\n\n    Each Azure term with its AWS counterpart and how faithful the match is.\n\n")
    body.append("- :material-compare: **" + link(page, "glossary/contrasts.md", "Contrasts") + "**\n\n    Pairs that are easy to confuse, and the difference that matters.\n\n")
    body.append("- :material-tag-multiple: **" + link(page, "glossary/browse.md", "Browse by facet") + "**\n\n    Terms grouped by track, domain, cloud and level.\n\n")
    body.append("- :material-information-outline: **" + link(page, "glossary/legend.md", "Legend") + "**\n\n    What fidelity, levels, statuses and freshness mean.\n\n")
    body.append("</div>\n\n")
    body.append("**Downloads:** [glossary.json](exports/glossary.json) · [Anki deck (all terms)](exports/anki-all.csv)\n")
    outputs.add(page, "".join(body))


def render_explorer(lib: Library, outputs: OutputSet) -> None:
    page = "glossary/explorer.md"
    body = [front_matter({"title": "Glossary Explorer", "description": "Faceted, alias-aware search over every glossary term.", "hide": ["toc"]}, GENERATED)]
    body.append("# Glossary Explorer\n\n")
    body.append(_frame(lib, page, "Type a name, acronym or a former product name. Combine filters to narrow the list; the address bar keeps your filters so you can bookmark a view."))
    body.append('<div class="lwd-explorer" data-lwd-explorer markdown>\n\n')
    body.append("The Explorer needs JavaScript. Use the [A–Z index](a-z.md) or [Browse by facet](browse.md) instead.\n{ .lwd-explorer__fallback }\n\n")
    body.append("[Explorer data](exports/glossary.js){ .lwd-explorer__data hidden }\n\n")
    body.append("</div>\n")
    outputs.add(page, "".join(body))


def render_az(lib: Library, outputs: OutputSet) -> None:
    page = "glossary/a-z.md"
    prefixes = [str(p) for p in lib.taxonomy.settings.get("vendor_prefixes", [])]
    entries: dict[str, dict] = {}

    def add(text: str, slug: str, see: bool) -> None:
        key = text.casefold().strip()
        if not key:
            return
        e = entries.setdefault(key, {"text": text, "slugs": [], "see": True})
        if not see:
            e["see"] = False
            e["text"] = text
        if slug not in e["slugs"]:
            e["slugs"].append(slug)

    for t in lib.terms.values():
        add(t.title, t.slug, see=False)
    for t in lib.terms.values():
        for name in t.aliases + [f.name for f in t.formerly] + t.acronyms + [f.acronym for f in t.formerly if f.acronym]:
            add(name, t.slug, see=True)
        for p in prefixes:
            if t.title.startswith(p + " ") and len(t.title) > len(p) + 1:
                add(f"{t.title[len(p) + 1:]} ({p})", t.slug, see=True)
    buckets: dict[str, list[dict]] = {}
    for e in entries.values():
        k = _sort_key(e["text"])
        letter = k[:1].upper() if k[:1].isalpha() else "#"
        e["sort"] = k
        buckets.setdefault(letter, []).append(e)
    letters = sorted(buckets, key=lambda x: (x == "#", x))
    body = [front_matter({"title": "Glossary A–Z", "description": "Every term, alias, acronym and former name, alphabetically.", "search": {"exclude": True}}, GENERATED)]
    body.append("# Glossary A–Z\n\n")
    body.append(" · ".join(f"[{x}](#{'num' if x == '#' else x.lower()})" for x in letters) + "\n{ .lwd-jumpbar }\n\n")
    for letter in letters:
        anchor = "num" if letter == "#" else letter.lower()
        body.append(f"## {letter} {{ #{anchor} }}\n\n")
        for e in sorted(buckets[letter], key=lambda e: e["sort"]):
            if e["see"]:
                targets = "; ".join(term_link(page, lib, s) for s in e["slugs"])
                body.append(f"- {inline(e['text'])} — *see* {targets}\n")
            else:
                for slug in e["slugs"]:
                    t = lib.terms[slug]
                    acr = f" ({', '.join(inline(a) for a in t.acronyms)})" if t.acronyms else ""
                    body.append(f"- **{term_link(page, lib, slug)}**{acr} {chip('cloud', t.cloud, lib.taxonomy.label('clouds', t.cloud))} — {inline(truncate(t.summary, 120))}\n")
        body.append("\n")
    outputs.add(page, "".join(body))


def render_contrasts(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    page = "glossary/contrasts.md"
    tax = lib.taxonomy
    body = [front_matter({"title": "Contrasts", "description": "Pairs of terms that are easy to confuse, and the difference that matters.", "search": {"exclude": True}}, GENERATED)]
    body.append("# Contrasts\n\n")
    body.append(_frame(lib, page, "Learning by differences: each row pairs two terms people mix up and states what actually separates them."))
    groups: dict[str, list] = {}
    for pair in ctx["contrasts"]:
        groups.setdefault(lib.terms[pair.a].domain, []).append(pair)
    if not groups:
        body.append("*No contrasts declared yet.*\n")
    for domain in [d.id for d in tax.term_domains if d.id in groups]:
        body.append(f"## {inline(tax.label('term_domains', domain))} {{ #{domain} }}\n\n| A | B | How they differ | Deep dive |\n|---|---|---|---|\n")
        for pair in groups[domain]:
            notes = " / ".join(cell(n) for n in pair.notes.values()) or "—"
            deep = " · ".join(link(page, a, lib.articles[a].title) for a in pair.articles if a in lib.articles) or "—"
            body.append(f"| {term_link(page, lib, pair.a)} | {term_link(page, lib, pair.b)} | {notes} | {deep} |\n")
        body.append("\n")
    outputs.add(page, "".join(body))


def render_rosetta(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    page = "glossary/rosetta.md"
    tax = lib.taxonomy
    pairs = ctx["cloud_pairs"]
    body = [front_matter({"title": "Azure ↔ AWS Rosetta", "description": "Every Azure term with its AWS counterpart, the fidelity of the match and what differs.", "search": {"exclude": True}}, GENERATED)]
    body.append("# Azure ↔ AWS Rosetta\n\n")
    body.append(_frame(lib, page, "Matches are rarely one-to-one. Fidelity says how far you can carry your knowledge across: "
                       "**exact** (functionally equivalent), **close** (same job, notable differences), **partial** (covers part of the scope) or **none**."))
    by_domain: dict[str, list] = {}
    for p in pairs:
        by_domain.setdefault(lib.terms[p.azure].domain, []).append(p)
        if lib.terms[p.aws].domain != lib.terms[p.azure].domain:
            by_domain.setdefault(lib.terms[p.aws].domain, [])
    if not pairs:
        body.append("*No cross-cloud equivalents declared yet.*\n\n")
    for domain in [d.id for d in tax.term_domains if d.id in by_domain]:
        body.append(f"## {inline(tax.label('term_domains', domain))} {{ #{domain} }}\n\n")
        az = sorted([p for p in pairs if lib.terms[p.azure].domain == domain], key=lambda p: lib.terms[p.azure].title.lower())
        aw = sorted([p for p in pairs if lib.terms[p.aws].domain == domain], key=lambda p: lib.terms[p.aws].title.lower())
        body.append('=== "Azure → AWS"\n\n')
        if az:
            body.append("    | Azure | AWS | Fidelity | What differs |\n    |---|---|---|---|\n")
            for p in az:
                note = p.notes.get("azure") or p.notes.get("aws", "")
                body.append(f"    | {term_link(page, lib, p.azure)} | {term_link(page, lib, p.aws)} | {chip('fidelity', p.fidelity, FIDELITY_LABEL[p.fidelity])} | {cell(note) or '—'} |\n")
        else:
            body.append("    *No Azure terms in this domain map to AWS yet.*\n")
        body.append('\n=== "AWS → Azure"\n\n')
        if aw:
            body.append("    | AWS | Azure | Fidelity | What differs |\n    |---|---|---|---|\n")
            for p in aw:
                note = p.notes.get("aws") or p.notes.get("azure", "")
                body.append(f"    | {term_link(page, lib, p.aws)} | {term_link(page, lib, p.azure)} | {chip('fidelity', p.fidelity, FIDELITY_LABEL[p.fidelity])} | {cell(note) or '—'} |\n")
        else:
            body.append("    *No AWS terms in this domain map to Azure yet.*\n")
        body.append("\n")
    none_notes = ctx["none_notes"]
    if none_notes:
        body.append("## No counterpart { #no-counterpart }\n\n| Term | Cloud | Why there is no match |\n|---|---|---|\n")
        for slug in sorted(none_notes, key=lambda s: lib.terms[s].title.lower()):
            t = lib.terms[slug]
            body.append(f"| {term_link(page, lib, slug)} | {tax.label('clouds', t.cloud)} | {cell(' '.join(none_notes[slug]))} |\n")
        body.append("\n")
    mapped = {p.azure for p in pairs} | {p.aws for p in pairs} | set(none_notes)
    unmapped = sorted((t for t in lib.terms.values() if t.cloud in ("azure", "aws") and t.slug not in mapped), key=lambda t: t.title.lower())
    if unmapped:
        body.append("## Not yet mapped { #unmapped }\n\n")
        body.append(" · ".join(term_link(page, lib, t.slug) for t in unmapped) + "\n\n")
    body.append("## Fidelity legend { #legend }\n\n| Fidelity | Meaning |\n|---|---|\n")
    for f in tax.fidelity:
        body.append(f"| {chip('fidelity', f.id, f.label)} | {cell(str(f.extra.get('meaning', '')))} |\n")
    outputs.add(page, "".join(body))


def render_browse(lib: Library, outputs: OutputSet) -> None:
    tax = lib.taxonomy
    hub = "glossary/browse.md"
    body = [front_matter({"title": "Browse the glossary", "description": "Terms grouped by track, domain, cloud and level.", "search": {"exclude": True}}, GENERATED)]
    body.append("# Browse the glossary\n\n")
    names = {"track": "Track", "domain": "Domain", "cloud": "Cloud", "level": "Level"}
    for facet in FACETS:
        index_page = f"glossary/browse/{facet}.md"
        values = _facet_values(lib, facet)
        body.append(f"## By {names[facet].lower()} {{ #{facet} }}\n\n")
        body.append(" · ".join(f"{link(hub, facet_page(facet, v), label)} ({len(_members(lib, facet, v))})" for v, label in values) + "\n\n")
        # Facet index page.
        fi = [front_matter({"title": f"Glossary by {names[facet].lower()}", "description": f"Glossary terms grouped by {names[facet].lower()}.", "search": {"exclude": True}}, GENERATED)]
        fi.append(f"# Glossary by {names[facet].lower()}\n\n| {names[facet]} | Terms |\n|---|---|\n")
        for v, label in values:
            fi.append(f"| {link(index_page, facet_page(facet, v), label)} | {len(_members(lib, facet, v))} |\n")
        fi.append("\n" + link(index_page, hub, "← All facets") + "\n")
        outputs.add(index_page, "".join(fi))
        # One page per value.
        secondary = {"track": "domain", "domain": "cloud", "cloud": "domain", "level": "track"}[facet]
        for v, label in values:
            vp = facet_page(facet, v)
            members = _members(lib, facet, v)
            fv = [front_matter({"title": f"{label} terms", "description": f"Glossary terms for {names[facet].lower()} {label}.", "search": {"exclude": True}}, GENERATED)]
            fv.append(f"# {inline(label)}\n\n{link(vp, index_page, 'Glossary by ' + names[facet].lower())} · {len(members)} terms\n\n")
            if facet == "track":
                arts = sorted((a for a in lib.articles.values() if v in a.tracks and a.kind == "article"), key=lambda a: (a.area, a.title.lower()))
                if arts:
                    fv.append("## Articles { #articles }\n\n")
                    for a in arts:
                        status = "" if a.status == "complete" else " " + chip("status", a.status or "draft", (a.status or "draft").title())
                        fv.append(f"- {link(vp, a.page, a.title)}{status} — {inline(truncate(a.description, 120))}\n")
                    fv.append("\n")
            if not members:
                fv.append("*No terms yet.*\n")
            groups: dict[str, list[Term]] = {}
            for t in members:
                keys = t.tracks if secondary == "track" else [getattr(t, secondary)]
                for k in keys[:1]:
                    groups.setdefault(k, []).append(t)
            sec_values = _facet_values(lib, secondary)
            for sv, slabel in sec_values:
                if sv not in groups:
                    continue
                fv.append(f"## {inline(slabel)} {{ #{sv} }}\n\n")
                for t in groups[sv]:
                    fv.append(_term_row(vp, lib, t) + "\n")
                fv.append("\n")
            outputs.add(vp, "".join(fv))
    outputs.add(hub, "".join(body))


def render_legend(lib: Library, outputs: OutputSet) -> None:
    tax = lib.taxonomy
    page = "glossary/legend.md"
    body = [front_matter({"title": "Glossary legend", "description": "What the fidelity, level, status and freshness labels mean."}, GENERATED)]
    body.append("# Glossary legend\n\n## Fidelity { #fidelity }\n\n| Label | Meaning |\n|---|---|\n")
    for f in tax.fidelity:
        body.append(f"| {chip('fidelity', f.id, f.label)} | {cell(str(f.extra.get('meaning', '')))} |\n")
    body.append("\n## Levels { #levels }\n\n| Level | Meaning |\n|---|---|\n")
    for lv in tax.levels:
        body.append(f"| {inline(lv.label)} | {cell(str(lv.extra.get('meaning', '')))} |\n")
    body.append("\n## Status { #status }\n\n| Status | Meaning |\n|---|---|\n"
                "| Stub | Scope outline only. |\n| Draft | Written but not fully verified against primary sources. |\n"
                "| Complete | Full explanation, examples, misconceptions and self-check, with primary sources and a verification date. |\n"
                "| Deprecated | Replaced by another term; kept so old links and names still resolve. |\n")
    body.append("\n## Freshness { #freshness }\n\nEvery verified page is re-checked on a schedule set by how fast its subject changes:\n\n| Class | Review every |\n|---|---|\n")
    for k, days in tax.volatility.items():
        body.append(f"| {inline(k)} | {days} days |\n")
    outputs.add(page, "".join(body))


def explorer_data(lib: Library, ctx: dict) -> dict:
    tax = lib.taxonomy
    url_style = "directory" if lib.config.use_directory_urls else "html"

    def url(t: Term) -> str:
        return f"terms/{t.slug}/" if url_style == "directory" else f"terms/{t.slug}.html"

    cloud_pairs = ctx["cloud_pairs"]
    eq_index: dict[str, list[dict]] = {}
    for p in cloud_pairs:
        eq_index.setdefault(p.azure, []).append({"slug": p.aws, "fidelity": p.fidelity})
        eq_index.setdefault(p.aws, []).append({"slug": p.azure, "fidelity": p.fidelity})
    exams_used = sorted({c.exam for t in lib.terms.values() for c in t.covers if c.exam in lib.exams})
    terms = []
    for t in sorted(lib.terms.values(), key=lambda t: t.slug):
        fresh = derive.term_freshness(lib, t)
        terms.append({
            "slug": t.slug,
            "title": t.title,
            "url": url(t),
            "summary": t.summary,
            "acronyms": t.acronyms,
            "aliases": t.aliases,
            "formerly": [f.name for f in t.formerly] + [f.acronym for f in t.formerly if f.acronym],
            "tracks": t.tracks,
            "domain": t.domain,
            "cloud": t.cloud,
            "level": t.level,
            "status": t.status,
            "last_verified": t.last_verified.isoformat() if t.last_verified else None,
            "freshness": fresh.state,
            "exams": sorted({c.exam for c in t.covers}),
            "equivalents": eq_index.get(t.slug, []),
            "differs_from": [c.term for c in t.differs_from if c.term in lib.terms],
        })
    return {
        "schema": 1,
        "generated": lib.today.isoformat(),
        "base": "../../",
        "url_style": url_style,
        "titles": {t.slug: t.title for t in lib.terms.values()},
        "facets": {
            "tracks": [{"id": v.id, "label": v.label} for v in tax.tracks],
            "domains": [{"id": v.id, "label": v.label} for v in tax.term_domains],
            "clouds": [{"id": v.id, "label": v.label} for v in tax.clouds],
            "levels": [{"id": v.id, "label": v.label} for v in tax.levels],
            "statuses": [{"id": s, "label": s.title()} for s in ("stub", "draft", "complete", "deprecated")],
            "freshness": [{"id": s, "label": s.replace("-", " ").title()} for s in ("fresh", "due-soon", "overdue", "unverified", "unverified-stub")],
            "exams": [{"id": e, "label": lib.exams[e].code} for e in exams_used],
        },
        "terms": terms,
    }


def render_exports(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    data = explorer_data(lib, ctx)
    text = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=1)
    outputs.add("glossary/exports/glossary.json", text + "\n")
    js = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    js = js.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029").replace("</", "<\\/")
    outputs.add("glossary/exports/glossary.js", f"window.__LWD_GLOSSARY__={js};\n")


def render_glossary(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    render_index(lib, outputs)
    render_explorer(lib, outputs)
    render_az(lib, outputs)
    render_contrasts(lib, ctx, outputs)
    render_rosetta(lib, ctx, outputs)
    render_browse(lib, outputs)
    render_legend(lib, outputs)
    render_exports(lib, ctx, outputs)
