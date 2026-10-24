"""Read zensical.toml (TOML 1.0, via tomllib) into a small typed view."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

import pathspec

from lwd.paths import CONFIG_NAME


class ConfigError(Exception):
    pass


@dataclass
class SiteConfig:
    root: Path
    raw: dict
    docs_dir: str = "docs"
    site_dir: str = "site"
    site_url: str | None = None
    use_directory_urls: bool = True
    nav: list = field(default_factory=list)
    nav_pages: list[str] = field(default_factory=list)
    nav_titles: dict[str, str] = field(default_factory=dict)
    not_in_nav: pathspec.PathSpec | None = None
    exclude_docs: pathspec.PathSpec | None = None
    plugins: dict = field(default_factory=dict)
    markdown_extensions: dict = field(default_factory=dict)
    features: list[str] = field(default_factory=list)

    @property
    def docs(self) -> Path:
        return self.root / self.docs_dir

    @property
    def site(self) -> Path:
        return self.root / self.site_dir

    def is_not_in_nav(self, page: str) -> bool:
        return bool(self.not_in_nav and self.not_in_nav.match_file(page))

    def is_excluded(self, page: str) -> bool:
        return bool(self.exclude_docs and self.exclude_docs.match_file(page))


def _spec(text: str | None) -> pathspec.PathSpec | None:
    if not text:
        return None
    lines = [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    return pathspec.PathSpec.from_lines("gitwildmatch", lines) if lines else None


def _flatten_nav(items: list, out: list[str], titles: dict[str, str]) -> None:
    for item in items:
        if isinstance(item, str):
            if item.endswith(".md"):
                out.append(item)
        elif isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    if value.endswith(".md"):
                        out.append(value)
                        titles[value] = title
                elif isinstance(value, list):
                    _flatten_nav(value, out, titles)
                else:
                    raise ConfigError(f"nav entry '{title}' must be a path or a list")
        else:
            raise ConfigError(f"unsupported nav entry: {item!r}")


def load_config(root: Path) -> SiteConfig:
    path = root / CONFIG_NAME
    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"{CONFIG_NAME} is not valid TOML 1.0 (tomllib): {exc}") from exc
    project = raw.get("project")
    if not isinstance(project, dict):
        raise ConfigError(f"{CONFIG_NAME} has no [project] table")
    cfg = SiteConfig(root=root, raw=raw)
    cfg.docs_dir = project.get("docs_dir", "docs")
    cfg.site_dir = project.get("site_dir", "site")
    cfg.site_url = project.get("site_url")
    cfg.use_directory_urls = bool(project.get("use_directory_urls", True))
    cfg.nav = project.get("nav", []) or []
    _flatten_nav(cfg.nav, cfg.nav_pages, cfg.nav_titles)
    cfg.not_in_nav = _spec(project.get("not_in_nav"))
    cfg.exclude_docs = _spec(project.get("exclude_docs"))
    cfg.plugins = project.get("plugins", {}) or {}
    cfg.markdown_extensions = project.get("markdown_extensions", {}) or {}
    cfg.features = (project.get("theme", {}) or {}).get("features", []) or []
    if "offline" in cfg.plugins and cfg.plugins.get("offline", {}).get("enabled", True):
        cfg.use_directory_urls = False
    return cfg
