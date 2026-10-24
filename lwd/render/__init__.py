"""Pure renderers: Library -> {docs-relative path: text}."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class OutputSet:
    docs: dict[str, str | bytes] = field(default_factory=dict)  # docs-relative
    root: dict[str, str | bytes] = field(default_factory=dict)  # repo-relative, outside docs/

    def add(self, page: str, content: str | bytes) -> None:
        if page in self.docs:
            raise ValueError(f"two renderers produced {page}")
        self.docs[page] = content

    def add_root(self, path: str, content: str | bytes) -> None:
        self.root[path] = content
