"""Command-line interface: python -m lwd <command>."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

from lwd import __version__, derive, output, paths, pipeline
from lwd.diag import ERROR, WARNING, Diagnostics, report


def _today(value: str | None) -> date:
    if value:
        return date.fromisoformat(value)
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        return datetime.fromtimestamp(int(epoch), tz=timezone.utc).date()
    return date.today()


def _root() -> Path:
    try:
        return paths.find_root()
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


def _print_diags(run: pipeline.Run, fmt: str, verbose: bool) -> None:
    text = report(run.diags, fmt, verbose)
    if text:
        print(text)


def _failed(run: pipeline.Run, fail_on: str) -> bool:
    if run.diags.has_errors:
        return True
    return fail_on == "warning" and run.diags.count(WARNING) > 0


def cmd_validate(args) -> int:
    run = pipeline.run(_root(), _today(args.today))
    _print_diags(run, args.format, args.verbose)
    return 1 if _failed(run, args.fail_on) else 0


def generate(root: Path, today: date, fmt: str = "text", verbose: bool = False, quiet: bool = False) -> pipeline.Run:
    run = pipeline.run(root, today)
    if run.outputs is None or run.lib is None:
        _print_diags(run, fmt, verbose)
        return run
    result = output.write_outputs(run.lib.config, run.outputs)
    if not quiet or run.diags.count(WARNING) or run.diags.has_errors:
        _print_diags(run, fmt, verbose)
    for rel in result.hand_edited:
        print(f"warning LWD094 {rel} was edited by hand; backed up to generated/overwritten/ and regenerated")
    print(f"lwd: {len(run.lib.terms)} terms, {len(run.lib.articles)} pages, {len(run.lib.exams)} exams, {len(run.lib.paths)} paths · "
          f"{len(result.written)} written, {result.unchanged} unchanged, {len(result.pruned)} pruned")
    return run


def cmd_gen(args) -> int:
    run = generate(_root(), _today(args.today), args.format, args.verbose)
    return 1 if run.outputs is None or _failed(run, args.fail_on) else 0


def cmd_build(args) -> int:
    from lwd import zensical

    root = _root()
    fmt = "github" if args.ci else "text"
    if args.ci:
        problems = doctor(root, ci=True)
        if problems:
            for p in problems:
                print(f"::error title=lwd doctor::{p}")
            return 1
    run = generate(root, _today(args.today), fmt, args.verbose)
    if run.outputs is None or run.lib is None:
        return 1
    # CI always clears the cache: Zensical fingerprints auto-appended includes by
    # whole-second mtime, so a fast rewrite could otherwise be missed.
    code = zensical.build(run.lib.config, strict=not args.no_strict, clean_cache=args.clean or args.ci)
    if code != 0:
        print(f"zensical build failed with exit code {code}")
        return code
    problems = zensical.assert_site(run.lib)
    for p in problems:
        print(("::error title=post-build::" if args.ci else "post-build: ") + p)
    return 1 if problems else 0


def _snapshot(root: Path, docs_dir: str) -> dict[str, tuple[int, int]]:
    snap: dict[str, tuple[int, int]] = {}
    docs = root / docs_dir
    skip = {"terms", "glossary", "study"}
    for dirpath, dirnames, filenames in os.walk(docs):
        rel = Path(dirpath).relative_to(docs).as_posix()
        top = rel.split("/", 1)[0]
        if rel != "." and top in skip:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and not (rel == "." and d in skip)]
        for f in filenames:
            if f.startswith("."):
                continue
            p = Path(dirpath, f)
            try:
                st = p.stat()
            except OSError:
                continue
            snap[p.as_posix()] = (st.st_mtime_ns, st.st_size)
    cfg_file = root / "zensical.toml"
    if cfg_file.is_file():
        st = cfg_file.stat()
        snap[cfg_file.as_posix()] = (st.st_mtime_ns, st.st_size)
    return snap


def cmd_serve(args) -> int:
    from lwd import zensical

    root = _root()
    today = _today(args.today)
    run = generate(root, today)
    if run.outputs is None or run.lib is None:
        print("lwd: fix the errors above, then run serve again")
        return 1
    proc = zensical.serve(run.lib.config, args.addr)
    docs_dir = run.lib.config.docs_dir
    snap = _snapshot(root, docs_dir)
    print("lwd: watching docs/ sources; Ctrl+C to stop")
    try:
        while proc.poll() is None:
            time.sleep(0.5)
            current = _snapshot(root, docs_dir)
            if current != snap:
                time.sleep(0.25)
                snap = _snapshot(root, docs_dir)
                generate(root, today, quiet=True)
    except KeyboardInterrupt:
        pass
    finally:
        if proc.poll() is None:
            if os.name == "nt":
                # The listener is a grandchild process; kill the whole tree.
                import subprocess

                subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
            else:
                proc.terminate()
            try:
                proc.wait(timeout=5)
            except Exception:
                proc.kill()
    return 0


def cmd_stale(args) -> int:
    run = pipeline.run(_root(), _today(args.today))
    if run.lib is None:
        _print_diags(run, "text", False)
        return 1
    lib = run.lib
    rows = []
    for t in lib.terms.values():
        rows.append(("term", t.origin.path, t.title, derive.term_freshness(lib, t)))
    for a in lib.articles.values():
        if a.kind == "article":
            rows.append(("article", a.origin.path, a.title, derive.article_freshness(lib, a)))
    for e in lib.exams.values():
        rows.append(("exam", e.origin.path, e.code, derive.exam_freshness(lib, e)))
    sel = []
    for kind, path, title, f in rows:
        if args.klass and f.klass != args.klass:
            continue
        due_soon = f.due is not None and (f.due - lib.today).days <= args.within
        if f.state in ("overdue", "unverified") or (f.state == "due-soon" and due_soon):
            sel.append((kind, path, title, f))
    sel.sort(key=lambda r: (r[3].state != "overdue", -r[3].days_over, r[2].lower()))
    if args.format == "json":
        print(json.dumps([{"kind": k, "path": p, "title": t, "state": f.state, "class": f.klass, "due": f.due.isoformat() if f.due else None, "days_over": f.days_over} for k, p, t, f in sel], indent=2))
    else:
        for k, p, t, f in sel:
            print(f"{f.state:<11} {f.klass:<12} due {f.due or '—'!s:<10} {k:<8} {t}  ({p})")
        print(f"{len(sel)} item(s)")
    overdue = any(f.state == "overdue" for *_, f in sel)
    return 1 if args.fail_on_overdue and overdue else 0


def cmd_coverage(args) -> int:
    run = pipeline.run(_root(), _today(args.today))
    if run.lib is None or run.ctx is None:
        _print_diags(run, "text", False)
        return 1
    cov = run.ctx["coverage"]
    wanted = [e.lower() for e in args.exams] or sorted(cov)
    for slug in wanted:
        c = cov.get(slug)
        if c is None:
            print(f"unknown exam {slug}")
            continue
        leaves = [x for x in c.objectives.values() if x.state != "overview"]
        ready = c.weighted if c.weighted is not None else c.readiness
        print(f"{c.exam.code:<10} {round(ready * 100):>3}% ready · {len(leaves)} objectives · {len(c.gaps)} gaps")
        if args.gaps:
            for g in c.gaps:
                print(f"    gap {g.id} {g.title}")
    return 0


def cmd_suggest_covers(args) -> int:
    from lwd import covers

    run = pipeline.run(_root(), _today(args.today))
    if run.lib is None:
        _print_diags(run, "text", False)
        return 1
    sugg = covers.suggest(run.lib)
    if args.terms:
        sugg = {k: v for k, v in sugg.items() if k in set(args.terms)}
    text = covers.format_report(run.lib, sugg)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {args.out}: {len(sugg)} terms, {sum(len(v.items) for v in sugg.values())} suggestions")
    else:
        sys.stdout.write(text)
    return 0


def cmd_export(args) -> int:
    from lwd.render.anki import cards, to_csv
    from lwd.render.glossary import explorer_data

    run = pipeline.run(_root(), _today(args.today))
    if run.lib is None or run.ctx is None:
        _print_diags(run, "text", False)
        return 1
    if args.what == "anki":
        settings = run.lib.taxonomy.settings.get("anki") or {}
        text = to_csv(cards(run.lib, run.ctx, args.min_status, args.exam), str(settings.get("deck", "LearnWithDifferences")))
    else:
        text = json.dumps(explorer_data(run.lib, run.ctx), ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    else:
        sys.stdout.write(text)
    return 0


def cmd_new(args) -> int:
    from lwd import scaffold

    root = _root()
    try:
        path = scaffold.create(root, args.kind, args.name, args.title, args.force, args.from_backlog)
    except scaffold.ScaffoldError as exc:
        print(f"error: {exc}")
        return 1
    print(f"created {path.relative_to(root).as_posix()}")
    return 0


def cmd_migrate(args) -> int:
    from lwd import migrate

    root = _root()
    if args.what == "move-pages":
        return migrate.move_pages(root, apply=args.apply)
    return migrate.split_glossary(root, apply=args.apply, plan_file=args.plan_file)


def doctor(root: Path, ci: bool = False) -> list[str]:
    import tomllib

    problems = []
    if sys.version_info < (3, 11):
        problems.append("Python 3.11 or newer is required")
    try:
        import zensical as _z  # noqa: F401
        from importlib.metadata import version

        installed = version("zensical")
        req = (root / "requirements.txt").read_text(encoding="utf-8") if (root / "requirements.txt").is_file() else ""
        pin = next((ln.split("==", 1)[1].strip() for ln in req.splitlines() if ln.strip().lower().startswith("zensical==")), None)
        if pin and pin != installed:
            problems.append(f"zensical {installed} is installed but requirements.txt pins {pin}")
    except ImportError:
        problems.append("zensical is not installed (pip install -r requirements.txt)")
    try:
        raw = tomllib.loads((root / "zensical.toml").read_text(encoding="utf-8"))
        project = raw.get("project", {})
        if not project.get("site_name"):
            problems.append("zensical.toml: site_name is required")
        site_url = project.get("site_url") or ""
        if ci and (not site_url or "YOUR-" in site_url or "example.com" in site_url):
            problems.append("zensical.toml: site_url must be the real published URL")
        known = {"search", "tags", "offline", "privacy", "social", "blog", "meta", "redirects", "minify", "rss", "glightbox"}
        for name in (project.get("plugins") or {}):
            if name not in known:
                problems.append(f"zensical.toml: plugin '{name}' is not one lwd knows Zensical supports; unsupported plugins are silently ignored")
    except (OSError, tomllib.TOMLDecodeError) as exc:
        problems.append(f"zensical.toml cannot be read with tomllib: {exc}")
    if (root / "mkdocs.yml").exists():
        problems.append("mkdocs.yml still exists; delete it so only zensical.toml configures the site")
    # Zensical does not flag missing extra_css/extra_javascript files, even with --strict.
    try:
        project = tomllib.loads((root / "zensical.toml").read_text(encoding="utf-8")).get("project", {})
        docs_dir = root / project.get("docs_dir", "docs")
        for item in list(project.get("extra_css") or []) + list(project.get("extra_javascript") or []):
            rel = item.get("path") if isinstance(item, dict) else item
            if rel and not (docs_dir / rel).is_file():
                problems.append(f"zensical.toml references {rel}, which does not exist under {docs_dir.name}/")
    except (OSError, tomllib.TOMLDecodeError):
        pass
    return problems


def cmd_nav(args) -> int:
    from lwd import navsync

    diags = Diagnostics()
    lib = pipeline.build_library(_root(), _today(args.today), diags)
    if lib is None:
        print(report(diags, "text", False))
        return 1
    try:
        changed = navsync.sync(lib, check=args.check)
    except navsync.NavError as exc:
        print(f"error: {exc}")
        return 1
    if args.check:
        print("nav is out of date: run python -m lwd nav" if changed else "nav is up to date")
        return 1 if changed else 0
    print("nav updated" if changed else "nav already up to date")
    return 0


def cmd_doctor(args) -> int:
    problems = doctor(_root(), ci=args.ci)
    for p in problems:
        print(f"problem: {p}")
    if not problems:
        print("lwd doctor: all good")
    return 1 if problems else 0


def cmd_clean(args) -> int:
    root = _root()
    from lwd.config import load_config

    removed = output.clean(load_config(root))
    print("removed: " + (", ".join(removed) if removed else "nothing"))
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(prog="python -m lwd", description="Learning with Differences site generator")
    p.add_argument("--version", action="version", version=f"lwd {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    def common(sp, fmt=True):
        sp.add_argument("--today", help="override today's date (YYYY-MM-DD)")
        sp.add_argument("-v", "--verbose", action="store_true", help="also show info diagnostics")
        if fmt:
            sp.add_argument("--format", choices=["text", "github", "json"], default="text")
            sp.add_argument("--fail-on", choices=["error", "warning"], default="error")

    sp = sub.add_parser("validate", help="check every source; write nothing")
    common(sp)
    sp.set_defaults(func=cmd_validate)
    sp = sub.add_parser("gen", help="validate and write generated pages")
    common(sp)
    sp.set_defaults(func=cmd_gen)
    sp = sub.add_parser("build", help="gen, then zensical build --strict, then post-build checks")
    common(sp, fmt=False)
    sp.add_argument("--ci", action="store_true", help="GitHub annotations and stricter doctor checks")
    sp.add_argument("--no-strict", action="store_true")
    sp.add_argument("--clean", action="store_true", help="clear Zensical's cache first")
    sp.set_defaults(func=cmd_build)
    sp = sub.add_parser("serve", help="gen, then zensical serve, regenerating on change")
    common(sp, fmt=False)
    sp.add_argument("--addr", help="IP:PORT for the dev server")
    sp.set_defaults(func=cmd_serve)
    sp = sub.add_parser("stale", help="list content overdue for re-verification")
    common(sp, fmt=False)
    sp.add_argument("--within", type=int, default=30)
    sp.add_argument("--class", dest="klass", choices=["ai", "cloud", "fundamentals"])
    sp.add_argument("--format", choices=["table", "json"], default="table")
    sp.add_argument("--fail-on-overdue", action="store_true")
    sp.set_defaults(func=cmd_stale)
    sp = sub.add_parser("coverage", help="exam objective coverage and gaps")
    common(sp, fmt=False)
    sp.add_argument("exams", nargs="*")
    sp.add_argument("--gaps", action="store_true")
    sp.set_defaults(func=cmd_coverage)
    sp = sub.add_parser("suggest-covers", help="propose exam objectives each term could cover (review before adding)")
    common(sp, fmt=False)
    sp.add_argument("terms", nargs="*", help="limit to these term slugs")
    sp.add_argument("--out")
    sp.set_defaults(func=cmd_suggest_covers)
    sp = sub.add_parser("export", help="write the Anki CSV or glossary JSON")
    common(sp, fmt=False)
    sp.add_argument("what", choices=["anki", "json"])
    sp.add_argument("--exam")
    sp.add_argument("--min-status", default="draft", choices=["stub", "draft", "complete"])
    sp.add_argument("--out")
    sp.set_defaults(func=cmd_export)
    sp = sub.add_parser("new", help="scaffold a term, exam, path or article")
    sp.add_argument("kind", choices=["term", "exam", "path", "article"])
    sp.add_argument("name", help="slug (term/path), exam code, or docs-relative article path")
    sp.add_argument("--title")
    sp.add_argument("--force", action="store_true")
    sp.add_argument("--from-backlog", action="store_true", help="fill title, scope and covers from docs/_data/backlog")
    sp.set_defaults(func=cmd_new)
    sp = sub.add_parser("migrate", help="one-off migrations")
    sp.add_argument("what", choices=["move-pages", "split-glossary"])
    sp.add_argument("--apply", action="store_true", help="perform the changes (default: print the plan)")
    sp.add_argument("--plan-file")
    sp.set_defaults(func=cmd_migrate)
    sp = sub.add_parser("nav", help="regenerate the area tabs of the nav from the taxonomy and backlog order")
    common(sp, fmt=False)
    sp.add_argument("--check", action="store_true", help="exit 1 if the nav is out of date; write nothing")
    sp.set_defaults(func=cmd_nav)
    sp = sub.add_parser("doctor", help="check the environment and config")
    sp.add_argument("--ci", action="store_true")
    sp.set_defaults(func=cmd_doctor)
    sp = sub.add_parser("clean", help="delete generated directories")
    sp.set_defaults(func=cmd_clean)

    args = p.parse_args(argv)
    return int(args.func(args) or 0)
