"""Filesystem helpers: repo root, POSIX docs paths, links, atomic writes."""

from __future__ import annotations

import hashlib
import os
import posixpath
import time
from pathlib import Path

CONFIG_NAME = "zensical.toml"
OWNED_MARKER = ".lwd-owned"


def find_root(start: Path | None = None) -> Path:
    """Return the directory that contains zensical.toml, searching upwards."""
    here = (start or Path.cwd()).resolve()
    for candidate in (here, *here.parents):
        if (candidate / CONFIG_NAME).is_file():
            return candidate
    raise FileNotFoundError(f"{CONFIG_NAME} not found in {here} or any parent directory")


def rel_link(from_page: str, to_path: str) -> str:
    """Relative link from one docs-relative page to another docs-relative path."""
    base = posixpath.dirname(from_page)
    return posixpath.relpath(to_path, base or ".")


def resolve(from_page: str, target: str) -> str:
    """Resolve a relative link target (no fragment) against a docs-relative page."""
    base = posixpath.dirname(from_page)
    return posixpath.normpath(posixpath.join(base, target)) if base else posixpath.normpath(target)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write(path: Path, data: bytes, retries: int = 5) -> None:
    """Write via a dot-prefixed temp file and os.replace, retrying on Windows locks."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_bytes(data)
    delay = 0.05
    for attempt in range(retries):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == retries - 1:
                tmp.unlink(missing_ok=True)
                raise
            time.sleep(delay)
            delay *= 2


def to_posix(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()
