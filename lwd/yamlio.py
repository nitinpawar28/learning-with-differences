"""Strict YAML loading with line numbers, and front-matter splitting.

Only ``true``/``false`` and ``null`` are resolved implicitly; every other
scalar stays a string, so ``level: 200``, ``id: 1.10`` and ``NO`` survive
unchanged. Duplicate keys are errors. Mappings and sequences remember the
1-based source line of each key or item.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import yaml

try:  # libyaml is much faster when available
    from yaml import CSafeLoader as _BaseLoader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as _BaseLoader  # type: ignore[assignment]


class _Loader(_BaseLoader):
    pass


_Loader.yaml_implicit_resolvers = {}
_Loader.add_implicit_resolver(
    "tag:yaml.org,2002:bool", re.compile(r"^(?:true|false|True|False|TRUE|FALSE)$"), list("tTfF")
)
_Loader.add_implicit_resolver("tag:yaml.org,2002:null", re.compile(r"^(?:~|null|Null|NULL|)$"), ["~", "n", "N", ""])


class YamlError(Exception):
    def __init__(self, message: str, line: int) -> None:
        super().__init__(message)
        self.line = line


class LineDict(dict):
    """A dict that records the source line of each key."""

    lines: dict[str, int]
    line: int

    def line_of(self, key: str) -> int:
        return self.lines.get(key, self.line)


class LineList(list):
    """A list that records the source line of each item."""

    lines: list[int]
    line: int

    def line_of(self, index: int) -> int:
        return self.lines[index] if 0 <= index < len(self.lines) else self.line


def _build(node: yaml.Node, offset: int):
    line = node.start_mark.line + 1 + offset
    if isinstance(node, yaml.MappingNode):
        out = LineDict()
        out.lines = {}
        out.line = line
        for key_node, value_node in node.value:
            if not isinstance(key_node, yaml.ScalarNode):
                raise YamlError("mapping keys must be plain scalars", key_node.start_mark.line + 1 + offset)
            key = key_node.value
            if key == "<<":
                raise YamlError("merge keys (<<) are not supported", key_node.start_mark.line + 1 + offset)
            if key in out:
                raise YamlError(f"duplicate key '{key}'", key_node.start_mark.line + 1 + offset)
            out[key] = _build(value_node, offset)
            out.lines[key] = key_node.start_mark.line + 1 + offset
        return out
    if isinstance(node, yaml.SequenceNode):
        items = LineList()
        items.lines = []
        items.line = line
        for item in node.value:
            items.append(_build(item, offset))
            items.lines.append(item.start_mark.line + 1 + offset)
        return items
    tag = node.tag
    if tag == "tag:yaml.org,2002:bool":
        return node.value.lower() == "true"
    if tag == "tag:yaml.org,2002:null":
        return None
    if tag in ("tag:yaml.org,2002:str", "!") or tag.startswith("tag:yaml.org,2002:str"):
        return node.value
    if tag.startswith("tag:yaml.org,2002:"):
        # Explicit tags such as !!int are allowed but kept as their text.
        return node.value
    raise YamlError(f"unsupported YAML tag {tag}", line)


def load(text: str, offset: int = 0):
    """Parse one YAML document. ``offset`` is added to every reported line."""
    try:
        node = yaml.compose(text, Loader=_Loader)
    except yaml.MarkedYAMLError as exc:
        mark = exc.problem_mark or exc.context_mark
        line = (mark.line + 1 + offset) if mark else offset + 1
        raise YamlError(str(exc.problem or exc).strip(), line) from exc
    except yaml.YAMLError as exc:
        raise YamlError(str(exc).strip(), offset + 1) from exc
    if node is None:
        empty = LineDict()
        empty.lines = {}
        empty.line = offset + 1
        return empty
    return _build(node, offset)


@dataclass
class Document:
    """A Markdown file split into front matter and body."""

    meta: LineDict
    body: str
    body_line: int  # 1-based line on which the body starts
    had_bom: bool = False


_FENCE = re.compile(r"^---[ \t]*$")
_END = re.compile(r"^(?:---|\.\.\.)[ \t]*$")


def read_text(raw: bytes) -> tuple[str, bool]:
    """Decode UTF-8 (strict), strip a BOM, normalise newlines."""
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw[3:].decode("utf-8") if bom else raw.decode("utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n"), bom


def split(text: str) -> Document:
    """Split ``---`` front matter from the Markdown body."""
    lines = text.split("\n")
    if not lines or not _FENCE.match(lines[0]):
        meta = LineDict()
        meta.lines = {}
        meta.line = 1
        return Document(meta, text, 1)
    for i in range(1, len(lines)):
        if _END.match(lines[i]):
            fm = "\n".join(lines[1:i])
            meta = load(fm, offset=1)
            if not isinstance(meta, LineDict):
                raise YamlError("front matter must be a mapping", 2)
            body = "\n".join(lines[i + 1 :])
            return Document(meta, body, i + 2)
    raise YamlError("front matter is not closed with ---", 1)
