"""Fence-aware Markdown scanning: H2 sections, headings, links, questions."""

from __future__ import annotations

import re
from dataclasses import dataclass

from markdown.extensions.toc import slugify

_FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
_HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$")
_ATTR = re.compile(r"\{([^{}]*)\}\s*$")
_ID = re.compile(r"(?:^|\s)#([A-Za-z0-9_\-:.]+)")
# Match the "](target)" tail, so link text that wraps across lines is found too.
_INLINE_LINK = re.compile(r"(!?)(\])\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\"|\s+'[^']*')?\s*\)")
_REF_DEF = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*<?(\S+?)>?(?:\s+[\"'(].*)?$")
_CODE_SPAN = re.compile(r"(`+)(?:.+?)\1")
_QUESTION = re.compile(r'^(\s*)\?\?\?\+?\s+question\s+"(.*)"\s*$')
_HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)


@dataclass
class Section:
    title: str
    canonical: str  # canonical H2 name, or the slug of an unknown heading
    anchor: str
    line: int  # 1-based, relative to file
    text: str  # body of the section without its heading line


@dataclass
class Link:
    target: str  # raw target, may include #fragment
    line: int
    is_image: bool = False

    @property
    def path(self) -> str:
        return self.target.split("#", 1)[0]

    @property
    def fragment(self) -> str:
        return self.target.split("#", 1)[1] if "#" in self.target else ""

    @property
    def is_external(self) -> bool:
        t = self.target.lower()
        return bool(re.match(r"^[a-z][a-z0-9+.\-]*:", t)) or t.startswith("//")


@dataclass
class Question:
    question: str
    answer: str
    line: int


def code_mask(lines: list[str]) -> list[bool]:
    """True for lines that are inside (or delimit) a fenced code block."""
    mask = [False] * len(lines)
    fence: str | None = None
    for i, line in enumerate(lines):
        m = _FENCE_OPEN.match(line)
        if fence is None:
            if m:
                fence = m.group(2)[0] * len(m.group(2))
                mask[i] = True
        else:
            mask[i] = True
            stripped = line.strip()
            if stripped.startswith(fence) and stripped.strip(fence[0]) == "":
                fence = None
    return mask


def heading_id(text: str) -> tuple[str, str]:
    """Return (plain heading text, id) honouring an attr_list { #id }."""
    m = _ATTR.search(text)
    explicit = ""
    if m:
        idm = _ID.search(m.group(1))
        if idm:
            explicit = idm.group(1)
        text = text[: m.start()].rstrip()
    text = text.rstrip("#").rstrip()
    plain = re.sub(r"<[^>]+>", "", text)
    plain = re.sub(r"[*_`]", "", plain)
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", plain)
    return plain, explicit or slugify(plain, "-")


def headings(body: str, line0: int = 1) -> list[tuple[int, str, str, int]]:
    """List (level, text, id, line) for every ATX heading outside code."""
    lines = body.split("\n")
    mask = code_mask(lines)
    out = []
    seen: dict[str, int] = {}
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        m = _HEADING.match(line)
        if not m:
            continue
        text, hid = heading_id(m.group(2))
        # Python-Markdown de-duplicates ids with _1, _2 suffixes.
        if hid in seen:
            seen[hid] += 1
            hid = f"{hid}_{seen[hid]}"
        else:
            seen[hid] = 0
        out.append((len(m.group(1)), text, hid, line0 + i))
    return out


def sections(body: str, line0: int, synonyms: dict[str, str]) -> list[Section]:
    """Split a body into H2 sections. Text before the first H2 is dropped."""
    lines = body.split("\n")
    mask = code_mask(lines)
    result: list[Section] = []
    current: Section | None = None
    buf: list[str] = []
    for i, line in enumerate(lines):
        m = None if mask[i] else _HEADING.match(line)
        if m and len(m.group(1)) == 2:
            if current:
                current.text = "\n".join(buf).strip("\n")
                result.append(current)
            text, hid = heading_id(m.group(2))
            canonical = synonyms.get(text.strip().lower(), hid)
            current = Section(text.strip(), canonical, hid, line0 + i, "")
            buf = []
        elif current is not None:
            buf.append(line)
    if current:
        current.text = "\n".join(buf).strip("\n")
        result.append(current)
    return result


def links(body: str, line0: int = 1) -> list[Link]:
    """Find inline links, images and reference definitions outside code."""
    lines = _HTML_COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), body).split("\n")
    mask = code_mask(lines)
    out: list[Link] = []
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        scrubbed = _CODE_SPAN.sub(lambda m: " " * len(m.group(0)), line)
        for m in _INLINE_LINK.finditer(scrubbed):
            out.append(Link(m.group(3), line0 + i, is_image=bool(m.group(1))))
        rd = _REF_DEF.match(scrubbed)
        if rd and not rd.group(1).startswith("^"):
            out.append(Link(rd.group(2), line0 + i))
    return out


def questions(text: str, line0: int) -> list[Question]:
    """Extract ``??? question "Q"`` blocks and their indented answers."""
    lines = text.split("\n")
    out: list[Question] = []
    i = 0
    while i < len(lines):
        m = _QUESTION.match(lines[i])
        if not m:
            i += 1
            continue
        indent = len(m.group(1))
        start = i
        answer: list[str] = []
        i += 1
        while i < len(lines):
            line = lines[i]
            if line.strip() == "":
                answer.append("")
                i += 1
                continue
            lead = len(line) - len(line.lstrip(" "))
            if lead <= indent:
                break
            answer.append(line[indent + 4 :] if lead >= indent + 4 else line.lstrip())
            i += 1
        out.append(Question(m.group(2).strip(), "\n".join(answer).strip(), line0 + start))
    return out


def word_count(body: str) -> int:
    lines = body.split("\n")
    mask = code_mask(lines)
    text = " ".join(line for i, line in enumerate(lines) if not mask[i])
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", text))
