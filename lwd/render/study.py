"""Study hub: exam catalogue and pages, learning paths, renewals, reports."""

from __future__ import annotations

import calendar
from datetime import date

from lwd import derive
from lwd.diag import ERROR, INFO, WARNING, Diagnostics
from lwd.model import Exam, Library
from lwd.render import OutputSet
from lwd.render.common import cell, chip, front_matter, inline, link, status_note, term_link, truncate

GENERATED = "lwd (study hub)"
STATE_LABEL = {"covered": "Covered", "partial": "Partial", "planned": "Planned", "gap": "Gap", "overview": "Overview"}
PROGRESS_LABEL = {"planned": "Planned", "studying": "Studying", "scheduled": "Scheduled", "passed": "Passed", "expired": "Expired", "retired": "Retired"}


def _pct(x: float | None) -> str:
    return "—" if x is None else f"{round(x * 100)}%"


def _add_months(d: date, months: int) -> date:
    y, m = divmod(d.month - 1 + months, 12)
    year, month = d.year + y, m + 1
    return date(year, month, min(d.day, calendar.monthrange(year, month)[1]))


def _stage_key(e: Exam) -> tuple:
    tier_rank = {"core": 0, "elective": 1, "skip": 2}
    try:
        stage = int(e.stage)
    except ValueError:
        stage = 99
    return (tier_rank.get(e.tier, 3), stage, e.code)


def render_index(lib: Library, cov: dict, outputs: OutputSet) -> None:
    page = "study/index.md"
    exams = list(lib.exams.values())
    passed = [e for e in exams if e.progress == "passed"]
    core = [e for e in exams if e.tier == "core"]
    default = ("Everything for certification study in one place: the exam roadmap, one page per exam with its official "
               "objectives and how well the library covers them, learning paths, renewals and the health reports.")
    body = [front_matter({"title": "Study", "description": "Exams, learning paths, renewals and library health."}, GENERATED)]
    body.append("# Study\n\n" + lib.frames.get(page, default).strip() + "\n\n")
    body.append(f"**{len(exams)} exams tracked** · {len(core)} on the core path · {len(passed)} passed · {len(lib.paths)} learning paths\n\n")
    body.append('<div class="grid cards" markdown>\n\n')
    body.append("- :material-certificate: **" + link(page, "study/exams.md", "Exams") + "**\n\n    The recommended sequence, every exam's objectives and coverage.\n\n")
    body.append("- :material-map-marker-path: **" + link(page, "study/paths.md", "Learning paths") + "**\n\n    Ordered routes through the library for each role.\n\n")
    body.append("- :material-calendar-refresh: **" + link(page, "study/renewals.md", "Renewals") + "**\n\n    Expiry dates and renewal windows for passed exams.\n\n")
    body.append("- :material-chart-box: **" + link(page, "study/reports/coverage.md", "Reports") + "**\n\n    Coverage, freshness, integrity and the content roadmap.\n\n")
    body.append("</div>\n")
    outputs.add(page, "".join(body))


def render_catalog(lib: Library, cov: dict, outputs: OutputSet) -> None:
    page = "study/exams.md"
    tax = lib.taxonomy
    body = [front_matter({"title": "Exams", "description": "The certification roadmap and every tracked exam."}, GENERATED)]
    body.append("# Exams\n\n" + lib.frames.get(page, "").strip() + "\n\n")
    tiers = [("core", "Core sequence"), ("elective", "Electives"), ("skip", "Catalogue only")]
    for tier, title in tiers:
        exams = sorted((e for e in lib.exams.values() if e.tier == tier), key=_stage_key)
        if not exams:
            continue
        body.append(f"## {title} {{ #{tier} }}\n\n| Stage | Exam | Provider | Level | Progress | Readiness | Gaps | Outline | Retires |\n|---|---|---|---|---|---|---|---|---|\n")
        for e in exams:
            c = cov.get(e.slug)
            ready = _pct(c.weighted if c and c.weighted is not None else (c.readiness if c else None)) if e.objectives else "—"
            gaps = str(len(c.gaps)) if c and e.objectives else "—"
            prov = " *(provisional)*" if e.provisional else ""
            progress = chip("progress", e.progress, PROGRESS_LABEL.get(e.progress, e.progress))
            body.append(
                f"| {inline(e.stage) or '—'} | {link(page, e.page, e.code)} {cell(e.title)}{prov} | {cell(tax.label('providers', e.provider))} | "
                f"{cell(e.level)} | {progress} | {ready} | {gaps} | {cell(e.outline_version) or '—'} | {e.retires_on or '—'} |\n"
            )
        body.append("\n")
    outputs.add(page, "".join(body))


def render_exam(lib: Library, e: Exam, c: derive.ExamCoverage, ctx: dict, outputs: OutputSet) -> None:
    tax = lib.taxonomy
    page = e.page
    body = [front_matter({"title": f"{e.code}: {e.title}", "description": f"{e.credential or e.title} — objectives, coverage and study plan.", "tags": [e.code]}, e.origin.path)]
    body.append(f"# {inline(e.code)}: {inline(e.title)}\n\n")
    if e.provisional:
        body.append('!!! warning "Provisional outline"\n    The vendor has not published this version\'s skills outline yet; objectives come from the previous version and will be re-transcribed.\n\n')
    if e.retires_on:
        body.append(f'!!! info "Retirement"\n    This exam retires on {e.retires_on}.' + (f" Successor: {link(page, lib.exams[e.replaced_by].page, lib.exams[e.replaced_by].code)}." if e.replaced_by in lib.exams else "") + "\n\n")
    facts = [
        ("Credential", inline(e.credential) or "—"),
        ("Provider", inline(tax.label("providers", e.provider))),
        ("Level", inline(e.level)),
        ("Roadmap", f"{e.tier.title()}" + (f", stage {inline(e.stage)}" if e.stage else "")),
        ("Progress", chip("progress", e.progress, PROGRESS_LABEL.get(e.progress, e.progress)) + (f" · target {e.target_date}" if e.target_date else "") + (f" · passed {e.passed_on}" if e.passed_on else "")),
    ]
    prereq = []
    if e.prerequisites:
        prereq.append("all of: " + ", ".join(link(page, lib.exams[p].page, lib.exams[p].code) if p in lib.exams else inline(p.upper()) for p in e.prerequisites))
    if e.prerequisites_any:
        prereq.append("one of: " + ", ".join(link(page, lib.exams[p].page, lib.exams[p].code) if p in lib.exams else inline(p.upper()) for p in e.prerequisites_any))
    if e.prerequisite_note:
        prereq.append(inline(e.prerequisite_note))
    facts.append(("Prerequisites", "; ".join(prereq) or "none"))
    if e.counterparts:
        facts.append(("Counterparts", ", ".join(link(page, lib.exams[x].page, lib.exams[x].code) for x in e.counterparts if x in lib.exams) or "—"))
    links_ = [f"[Official page]({e.official_url})"]
    if e.study_guide_url:
        links_.append(f"[Skills outline]({e.study_guide_url})")
    facts.append(("Links", " · ".join(links_)))
    facts.append(("Outline", (inline(e.outline_version) or "—") + (f" · verified {e.last_verified}" if e.last_verified else "")))
    body.append("| | |\n|---|---|\n" + "".join(f"| **{k}** | {v} |\n" for k, v in facts) + "\n")

    if e.objectives:
        weighted = f" · weighted {_pct(c.weighted)}" if c.weighted is not None else ""
        body.append(f"## Readiness {{ #readiness }}\n\n**{_pct(c.readiness)} of objectives covered**{weighted}\n\n")
        body.append("| Domain | Weight | Covered | Partial | Planned | Gap | Readiness |\n|---|---|---|---|---|---|---|\n")
        for d in c.domains:
            o = d["objective"]
            k = d["counts"]
            body.append(f"| {link(page, page, o.id + ' ' + o.title, o.anchor)} | {inline(o.weight) or '—'} | {k['covered']} | {k['partial']} | {k['planned']} | {k['gap']} | {_pct(d['readiness'])} |\n")
        body.append("\n")
        if c.gaps:
            items = "\n".join(f"    - {link(page, page, g.id + ' ' + g.title, g.anchor)}" for g in c.gaps[:40])
            more = f"\n    - … and {len(c.gaps) - 40} more" if len(c.gaps) > 40 else ""
            body.append(f'??? warning "Gaps: {len(c.gaps)} objectives with no coverage yet"\n\n{items}{more}\n\n')
        body.append("## Objectives { #objectives }\n\n")
        for o in e.objectives:
            oc = c.objectives[o.id]
            if not o.parent:
                w = f" ({inline(o.weight)})" if o.weight else ""
                body.append(f"### {inline(o.id)} {inline(o.title)}{w} {{ #{o.anchor} }}\n\n")
                continue
            depth_marker = "#### " if o.depth == 2 else ""
            label = chip("coverage", oc.state, STATE_LABEL[oc.state])
            pages = " · ".join(link(page, x.page, x.title, x.anchor) + ("" if x.status == "complete" else f" *({x.status})*") for x in oc.coverers) or "—"
            if depth_marker:
                body.append(f"{depth_marker}{inline(o.id)} {inline(o.title)} {{ #{o.anchor} }}\n\n{label} {pages}\n\n")
            else:
                body.append(f"- **{inline(o.id)}** {inline(o.title)} — {label} {pages} {{ #{o.anchor} }}\n")
        body.append("\n")
    else:
        body.append("## Objectives { #objectives }\n\n*Objectives have not been transcribed yet.*\n\n")

    terms = sorted({t.slug for t in lib.terms.values() if any(cv.exam == e.slug for cv in t.covers)}, key=lambda s: lib.terms[s].title.lower())
    if terms:
        body.append("## Terms to know { #terms }\n\n" + " · ".join(term_link(page, lib, s) for s in terms) + "\n\n")
        body.append(f"Flashcards: [Anki deck for {inline(e.code)}](../../glossary/exports/anki-{e.slug}.csv)\n\n")
    for s in e.sections:
        if s.text.strip():
            body.append(f"## {s.title}\n\n{s.text.strip()}\n\n")
    outputs.add(page, "".join(body).rstrip() + "\n")


def render_paths(lib: Library, outputs: OutputSet) -> None:
    hub = "study/paths.md"
    tax = lib.taxonomy
    body = [front_matter({"title": "Learning paths", "description": "Ordered routes through the library for each role."}, GENERATED)]
    body.append("# Learning paths\n\n" + lib.frames.get(hub, "").strip() + "\n\n")
    if not lib.paths:
        body.append("*No learning paths yet.*\n")
    else:
        body.append("| Path | Tracks | Level | Steps | Complete |\n|---|---|---|---|---|\n")
    for lp in sorted(lib.paths.values(), key=lambda p: p.title.lower()):
        done = _path_completeness(lib, lp)
        body.append(f"| {link(hub, lp.page, lp.title)} | {', '.join(tax.label('tracks', x) for x in lp.tracks)} | {tax.label('levels', lp.level) if lp.level else '—'} | {len(lp.steps)} | {_pct(done)} |\n")
        render_path(lib, lp, outputs)
    outputs.add(hub, "".join(body))


def _target_status(lib: Library, st) -> str:
    if st.kind == "term":
        t = lib.terms.get(st.target)
        return t.status if t else "missing"
    if st.kind == "page":
        a = lib.articles.get(st.target)
        return (a.status or "draft") if a else "missing"
    return "complete"


def _path_completeness(lib: Library, lp) -> float:
    steps = [s for s in lp.steps if s.kind in ("term", "page")]
    if not steps:
        return 1.0
    return sum(1 for s in steps if _target_status(lib, s) == "complete") / len(steps)


def _minutes(lib: Library, st) -> int:
    if st.minutes:
        return st.minutes
    if st.kind == "page" and st.target in lib.articles:
        return max(5, round(lib.articles[st.target].word_count / 220))
    if st.kind == "term" and st.target in lib.terms:
        t = lib.terms[st.target]
        words = sum(len(s.text.split()) for s in t.sections)
        return max(5, round(words / 200))
    return 10 if st.kind == "objective" else 5


def render_path(lib: Library, lp, outputs: OutputSet) -> None:
    page = lp.page
    tax = lib.taxonomy
    body = [front_matter({"title": lp.title, "description": lp.summary}, lp.origin.path)]
    body.append(f"# {inline(lp.title)}\n\n")
    body.append(status_note(lp.status))
    meta = [f"**Tracks:** {', '.join(tax.label('tracks', x) for x in lp.tracks) or '—'}"]
    if lp.level:
        meta.append(f"**Level:** {tax.label('levels', lp.level)}")
    if lp.exams:
        meta.append("**Exams:** " + ", ".join(link(page, lib.exams[x].page, lib.exams[x].code) for x in lp.exams if x in lib.exams))
    total = sum(_minutes(lib, s) for s in lp.steps)
    meta.append(f"**Time:** about {total // 60} h {total % 60} min · **Complete:** {_pct(_path_completeness(lib, lp))}")
    body.append(" · ".join(meta) + "\n\n")
    if lp.body.strip():
        body.append(lp.body.strip() + "\n\n")
    body.append("## Steps { #steps }\n\n")
    for i, st in enumerate(lp.steps, 1):
        note = f" — {inline(st.note)}" if st.note else ""
        if st.kind == "check":
            body.append(f'{i}. **Checkpoint**\n\n    !!! question "Check yourself"\n        {inline(st.target)}\n\n')
            continue
        if st.kind == "term":
            target = term_link(page, lib, st.target)
        elif st.kind == "page":
            a = lib.articles.get(st.target)
            target = link(page, st.target, a.title) if a else inline(st.target)
        else:
            exam_slug, _, oid = st.target.lower().partition(":")
            exam = lib.exams.get(exam_slug)
            obj = exam.objective(oid) if exam else None
            target = link(page, exam.page, f"{exam.code} · {oid} {obj.title}", obj.anchor) if exam and obj else inline(st.target)
        status = _target_status(lib, st)
        badge = "" if status in ("complete",) or st.kind == "objective" else " " + chip("status", status, status.title())
        body.append(f"{i}. {target}{badge} · ~{_minutes(lib, st)} min{note}\n")
    outputs.add(page, "".join(body).rstrip() + "\n")


def render_renewals(lib: Library, outputs: OutputSet) -> None:
    page = "study/renewals.md"
    body = [front_matter({"title": "Renewals", "description": "Expiry dates and renewal windows for passed certifications."}, GENERATED)]
    body.append("# Renewals\n\n")
    rows = []
    for e in lib.exams.values():
        if e.progress != "passed" or not e.passed_on:
            continue
        prov = lib.taxonomy.provider(e.provider)
        months = int(prov.extra.get("validity_months", 0)) if prov else 0
        if e.level == "fundamentals" and e.provider == "microsoft":
            months = 0
        expires = _add_months(e.passed_on, months) if months else None
        days = (expires - lib.today).days if expires else None
        rows.append((expires or date.max, e, months, expires, days, str(prov.extra.get("renewal", "")) if prov else ""))
    if not rows:
        body.append("*No passed exams recorded yet. Set `progress: passed` and `passed_on` in an exam file to track it here.*\n\n")
    else:
        body.append("| Exam | Passed | Valid for | Expires | Days left | How to renew |\n|---|---|---|---|---|---|\n")
        for _, e, months, expires, days, renewal in sorted(rows, key=lambda r: r[0]):
            valid = f"{months} months" if months else "does not expire"
            body.append(f"| {link(page, e.page, e.code)} | {e.passed_on} | {valid} | {expires or '—'} | {days if days is not None else '—'} | {cell(renewal) or '—'} |\n")
        body.append("\n")
    body.append("## Renewal rules { #rules }\n\n| Provider | Validity | Renewal |\n|---|---|---|\n")
    for p in lib.taxonomy.providers:
        months = p.extra.get("validity_months")
        body.append(f"| {inline(p.label)} | {f'{months} months' if months else 'lifetime'} | {cell(str(p.extra.get('renewal', '')))} |\n")
    outputs.add(page, "".join(body))


def render_reports(lib: Library, cov: dict, outputs: OutputSet) -> None:
    # Freshness.
    page = "study/reports/freshness.md"
    rows = []
    for t in lib.terms.values():
        f = derive.term_freshness(lib, t)
        rows.append((f, "term", t.page, t.title, t.status))
    for a in lib.articles.values():
        if a.kind != "article":
            continue
        f = derive.article_freshness(lib, a)
        rows.append((f, "article", a.page, a.title, a.status))
    for e in lib.exams.values():
        f = derive.exam_freshness(lib, e)
        rows.append((f, "exam outline", e.page, e.code, "complete"))
    order = {"overdue": 0, "due-soon": 1, "unverified": 2, "unverified-stub": 3, "fresh": 4}
    rows.sort(key=lambda r: (order[r[0].state], -r[0].days_over, r[3].lower()))
    counts = {s: sum(1 for r in rows if r[0].state == s) for s in order}
    body = [front_matter({"title": "Freshness report", "description": "What is overdue for re-verification.", "search": {"exclude": True}}, GENERATED)]
    body.append(f"# Freshness report\n\nAs of {lib.today}. " + " · ".join(f"**{k.replace('-', ' ')}:** {v}" for k, v in counts.items()) + "\n\n")
    for state in ("overdue", "due-soon", "unverified"):
        sel = [r for r in rows if r[0].state == state]
        if not sel:
            continue
        body.append(f"## {state.replace('-', ' ').title()} {{ #{state} }}\n\n| Item | Kind | Class | Due | Days over |\n|---|---|---|---|---|\n")
        for f, kind, p, title, _status in sel:
            body.append(f"| {link(page, p, title)} | {kind} | {f.klass} ({f.window} d) | {f.due or '—'} | {f.days_over or '—'} |\n")
        body.append("\n")
    stubs = [r for r in rows if r[0].state == "unverified-stub"]
    if stubs:
        body.append(f"## Stubs {{ #stubs }}\n\n{len(stubs)} stub pages are not yet verifiable.\n")
    outputs.add(page, "".join(body))

    # Coverage.
    page = "study/reports/coverage.md"
    body = [front_matter({"title": "Coverage report", "description": "How well the library covers each exam's objectives.", "search": {"exclude": True}}, GENERATED)]
    body.append("# Coverage report\n\n| Exam | Tier | Leaves | Covered | Partial | Planned | Gap | Readiness |\n|---|---|---|---|---|---|---|---|\n")
    for e in sorted(lib.exams.values(), key=_stage_key):
        c = cov[e.slug]
        leaves = [x for x in c.objectives.values() if x.state != "overview"]
        k = {s: sum(1 for x in leaves if x.state == s) for s in ("covered", "partial", "planned", "gap")}
        ready = _pct(c.weighted if c.weighted is not None else c.readiness) if leaves else "—"
        body.append(f"| {link(page, e.page, e.code)} | {e.tier} | {len(leaves)} | {k['covered']} | {k['partial']} | {k['planned']} | {k['gap']} | {ready} |\n")
    outputs.add(page, "".join(body))


def render_integrity(lib: Library, diags: Diagnostics, outputs: OutputSet) -> None:
    page = "study/reports/integrity.md"
    body = [front_matter({"title": "Integrity report", "description": "Validation warnings and notes from the last build.", "search": {"exclude": True}}, GENERATED)]
    body.append(f"# Integrity report\n\nAs of {lib.today}: {diags.count(ERROR)} errors, {diags.count(WARNING)} warnings, {diags.count(INFO)} notes.\n\n")
    items = [d for d in diags.sorted() if d.severity in (WARNING, INFO)]
    if not items:
        body.append("*Nothing to report.*\n")
    else:
        body.append("| Code | Severity | Where | Message |\n|---|---|---|---|\n")
        for d in items[:2000]:
            where = f"`{d.path}:{d.line}`" if d.line else f"`{d.path}`"
            body.append(f"| {d.code} | {d.severity} | {where} | {cell(d.message)}{(' — ' + cell(d.hint)) if d.hint else ''} |\n")
    outputs.add(page, "".join(body))


def render_roadmap(lib: Library, outputs: OutputSet) -> None:
    page = "study/reports/roadmap.md"
    body = [front_matter({"title": "Content roadmap", "description": "Planned, stubbed, drafted and complete pages by section and wave.", "search": {"exclude": True}}, GENERATED)]
    body.append("# Content roadmap\n\n")
    if not lib.backlog:
        body.append("*No backlog imported yet (docs/_data/backlog/).*\n")
        outputs.add(page, "".join(body))
        return
    existing = {a.page: a for a in lib.articles.values()}
    by_wave: dict[str, dict[str, int]] = {}
    section_rows = []
    for section, data in sorted(lib.backlog.items()):
        arts = data.get("articles") or []
        counts = {"backlog": 0, "stub": 0, "draft": 0, "complete": 0}
        for a in arts:
            p = f"{a.get('folder', '').strip('/')}/{a.get('slug', '')}.md"
            state = (existing[p].status or "draft") if p in existing else "backlog"
            if state == "deprecated":
                state = "complete"
            counts[state] = counts.get(state, 0) + 1
            w = str(a.get("wave", "?"))
            by_wave.setdefault(w, {"backlog": 0, "stub": 0, "draft": 0, "complete": 0})[state] += 1
        terms = data.get("terms") or []
        written = sum(1 for t in terms if str(t.get("slug", "")) in lib.terms)
        section_rows.append((section, len(arts), counts, len(terms), written))
    body.append("## By wave { #waves }\n\n| Wave | Backlog | Stub | Draft | Complete |\n|---|---|---|---|---|\n")
    for w in sorted(by_wave, key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x)):
        k = by_wave[w]
        body.append(f"| {inline(w)} | {k['backlog']} | {k['stub']} | {k['draft']} | {k['complete']} |\n")
    body.append("\n## By section { #sections }\n\n| Section | Articles | Backlog | Stub | Draft | Complete | Terms written |\n|---|---|---|---|---|---|---|\n")
    for section, n, k, nterms, written in section_rows:
        body.append(f"| {inline(section)} | {n} | {k['backlog']} | {k['stub']} | {k['draft']} | {k['complete']} | {written}/{nterms} |\n")
    outputs.add(page, "".join(body))


def render_study(lib: Library, ctx: dict, outputs: OutputSet) -> None:
    cov = ctx["coverage"]
    render_index(lib, cov, outputs)
    render_catalog(lib, cov, outputs)
    for e in sorted(lib.exams.values(), key=lambda e: e.slug):
        render_exam(lib, e, cov[e.slug], ctx, outputs)
    render_paths(lib, outputs)
    render_renewals(lib, outputs)
    render_reports(lib, cov, outputs)
    render_roadmap(lib, outputs)
