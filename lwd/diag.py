"""Diagnostics: coded, located messages with text and GitHub reporters."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field

ERROR = "error"
WARNING = "warning"
INFO = "info"

_RANK = {INFO: 0, WARNING: 1, ERROR: 2}


@dataclass(frozen=True)
class Diagnostic:
    code: str
    severity: str
    path: str
    line: int
    message: str
    hint: str = ""

    def format(self) -> str:
        loc = f"{self.path}:{self.line}" if self.line else self.path
        text = f"{loc}: {self.severity} {self.code} {self.message}"
        return f"{text}\n    hint: {self.hint}" if self.hint else text


@dataclass
class Diagnostics:
    items: list[Diagnostic] = field(default_factory=list)

    def add(self, code: str, severity: str, path: str, line: int, message: str, hint: str = "") -> None:
        self.items.append(Diagnostic(code, severity, path, line or 0, message, hint))

    def error(self, code: str, path: str, line: int, message: str, hint: str = "") -> None:
        self.add(code, ERROR, path, line, message, hint)

    def warn(self, code: str, path: str, line: int, message: str, hint: str = "") -> None:
        self.add(code, WARNING, path, line, message, hint)

    def info(self, code: str, path: str, line: int, message: str, hint: str = "") -> None:
        self.add(code, INFO, path, line, message, hint)

    def extend(self, other: Diagnostics) -> None:
        self.items.extend(other.items)

    def count(self, severity: str) -> int:
        return sum(1 for d in self.items if d.severity == severity)

    @property
    def has_errors(self) -> bool:
        return self.count(ERROR) > 0

    def at_least(self, severity: str) -> list[Diagnostic]:
        return [d for d in self.items if _RANK[d.severity] >= _RANK[severity]]

    def sorted(self) -> list[Diagnostic]:
        return sorted(self.items, key=lambda d: (-_RANK[d.severity], d.path, d.line, d.code))


def report(diags: Diagnostics, fmt: str = "text", verbose: bool = False) -> str:
    """Render diagnostics as plain text, GitHub annotations or JSON."""
    shown = [d for d in diags.sorted() if verbose or d.severity != INFO]
    if fmt == "json":
        return json.dumps([asdict(d) for d in shown], indent=2, sort_keys=True)
    if fmt == "github":
        lines = []
        for d in shown:
            level = {"error": "error", "warning": "warning"}.get(d.severity, "notice")
            msg = d.message + (f" — {d.hint}" if d.hint else "")
            lines.append(f"::{level} file={d.path},line={d.line or 1},title={d.code}::{msg}")
        return "\n".join(lines)
    lines = [d.format() for d in shown]
    lines.append(
        f"{diags.count(ERROR)} error(s), {diags.count(WARNING)} warning(s), {diags.count(INFO)} info"
    )
    return "\n".join(lines)
