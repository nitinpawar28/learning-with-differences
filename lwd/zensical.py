"""Run Zensical and check what it produced."""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from lwd.config import SiteConfig
from lwd.model import Library


def executable() -> str:
    """Prefer the zensical next to the running interpreter (same venv)."""
    scripts = Path(sys.executable).parent
    for name in ("zensical.exe", "zensical"):
        candidate = scripts / name
        if candidate.is_file():
            return str(candidate)
    found = shutil.which("zensical")
    if not found:
        raise FileNotFoundError("zensical is not installed in this environment (pip install -r requirements.txt)")
    return found


def build(cfg: SiteConfig, strict: bool = True, clean_cache: bool = False) -> int:
    cmd = [executable(), "build", "-f", str(cfg.root / "zensical.toml")]
    if strict:
        cmd.append("--strict")
    if clean_cache:
        cmd.append("--clean")
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run(cmd, cwd=cfg.root, env=env).returncode


def serve(cfg: SiteConfig, addr: str | None = None) -> subprocess.Popen:
    cmd = [executable(), "serve", "-f", str(cfg.root / "zensical.toml")]
    if addr:
        cmd += ["-a", addr]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.Popen(cmd, cwd=cfg.root, env=env)


def _page_html(cfg: SiteConfig, page: str) -> Path:
    stem = page[:-3]
    if cfg.use_directory_urls:
        if stem == "index" or stem.endswith("/index"):
            return cfg.site / stem[: -len("index")] / "index.html"
        return cfg.site / stem / "index.html"
    return cfg.site / f"{stem}.html"


def assert_site(lib: Library) -> list[str]:
    """Return problems found in the built site (empty list = all good)."""
    cfg = lib.config
    problems = []
    if not cfg.site.is_dir():
        return [f"{cfg.site} was not created"]
    for t in lib.terms.values():
        if not _page_html(cfg, t.page).is_file():
            problems.append(f"missing HTML for {t.page}")
    for d in cfg.site.iterdir():
        if d.name.startswith("_") and d.is_dir():
            problems.append(f"source directory leaked into the site: {d.name}/")
    js = cfg.site / "glossary" / "exports" / "glossary.js"
    if not js.is_file() or not js.read_text(encoding="utf-8")[:40].startswith("window.__LWD_GLOSSARY__="):
        problems.append("glossary/exports/glossary.js is missing or malformed")
    sample = next((t for t in sorted(lib.terms.values(), key=lambda t: t.slug) if t.acronyms), None)
    if sample:
        html = _page_html(cfg, sample.page)
        if html.is_file() and "<abbr" not in html.read_text(encoding="utf-8"):
            problems.append(f"no <abbr> tooltip rendered on {sample.page}")
    explorer = _page_html(cfg, "glossary/explorer.md")
    if explorer.is_file() and "lwd-explorer__data" not in explorer.read_text(encoding="utf-8"):
        problems.append("Explorer data link was not rendered")
    # Unrendered icon shortcodes (typos, missing emoji config) fail silently in Zensical.
    shortcode = re.compile(r":(?:material|fontawesome|octicons|simple|lucide)-[a-z0-9-]+:")
    for html in cfg.site.rglob("*.html"):
        text = html.read_text(encoding="utf-8", errors="replace")
        # Ignore code samples that show shortcodes literally.
        text = re.sub(r"<code[^>]*>.*?</code>", "", text, flags=re.S)
        m = shortcode.search(text)
        if m:
            problems.append(f"unrendered icon shortcode {m.group(0)} in {html.relative_to(cfg.site).as_posix()}")
    return problems
