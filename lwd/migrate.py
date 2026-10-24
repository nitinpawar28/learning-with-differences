"""One-off migrations: move pages to the new layout, split the glossary."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from markdown.extensions.toc import slugify

from lwd import mdscan, paths

# Old docs-relative path -> new docs-relative path.
MOVES = {
    "messaging/dotnet-core-csharp.md": "messaging/runtime/dotnet-core-csharp.md",
    "messaging/async-threading.md": "messaging/runtime/async-threading.md",
    "messaging/rest-vs-grpc-apis.md": "messaging/apis/rest-vs-grpc-apis.md",
    "messaging/signalr-websockets.md": "messaging/realtime/signalr-websockets.md",
    "messaging/event-driven-vs-request-response.md": "messaging/eventing/event-driven-vs-request-response.md",
    "messaging/redis-streams-vs-kafka.md": "messaging/eventing/redis-streams-vs-kafka.md",
    "messaging/outbox-pattern.md": "messaging/eventing/outbox-pattern.md",
    "messaging/delivery-semantics.md": "messaging/eventing/delivery-semantics.md",
    "messaging/broker-exchange-api-integrations.md": "messaging/integration/broker-exchange-api-integrations.md",
    "messaging/microservices-vs-modular-monoliths.md": "messaging/integration/microservices-vs-modular-monoliths.md",
    "messaging/mcp-tool-orchestration.md": "ai/protocols/mcp-tool-orchestration.md",
    "data/relational-databases.md": "data/relational/relational-databases.md",
    "data/time-series-financial-schemas.md": "data/time-series/time-series-financial-schemas.md",
    "data/row-vs-columnar-storage.md": "data/time-series/row-vs-columnar-storage.md",
    "data/high-frequency-indexing-partitioning.md": "data/time-series/high-frequency-indexing-partitioning.md",
    "frontend/angular-fundamentals.md": "frontend/angular/angular-fundamentals.md",
    "frontend/rxjs-state-management.md": "frontend/angular/rxjs-state-management.md",
    "frontend/typescript.md": "frontend/typescript/typescript.md",
    "frontend/real-time-ui-streaming.md": "frontend/realtime/real-time-ui-streaming.md",
    "security/mtls-vs-api-keys.md": "security/iam/mtls-vs-api-keys.md",
    "security/workload-identity.md": "security/iam/workload-identity.md",
    "security/capability-based-authz.md": "security/iam/capability-based-authz.md",
    "security/wasm-sandboxing.md": "security/appsec/wasm-sandboxing.md",
    "_templates/tech-guide-template.md": "about/article-template.md",
}

# Glossary H3 title -> (slug, title, acronyms, aliases, domain, tracks, level)
GLOSSARY_PLAN = {
    "At-Least-Once vs. Exactly-Once": ("at-least-once-delivery", "At-Least-Once Delivery", [], [], "messaging", ["architect"], "practitioner"),
    "Log Compaction": ("log-compaction", "Log Compaction", [], [], "messaging", ["architect"], "practitioner"),
    "MAXLEN Trim": ("maxlen-trim", "MAXLEN Trim (Redis Streams)", [], ["Stream trimming"], "messaging", ["architect"], "practitioner"),
    "Outbox Pattern": ("transactional-outbox", "Transactional Outbox", [], ["Outbox pattern"], "messaging", ["architect"], "practitioner"),
    "Consumer Group": ("consumer-group", "Consumer Group", [], [], "messaging", ["architect"], "practitioner"),
    "Idempotency Key": ("idempotency-key", "Idempotency Key", [], [], "messaging", ["architect"], "practitioner"),
    "Dead-Letter Queue (DLQ)": ("dead-letter-queue", "Dead-Letter Queue (DLQ)", ["DLQ"], [], "messaging", ["architect", "cloud"], "practitioner"),
    "Choreography vs. Orchestration": ("choreography", "Choreography", [], ["Event choreography"], "patterns", ["architect"], "practitioner"),
    "Row vs. Columnar Storage": ("columnar-storage", "Columnar Storage", [], ["Column-oriented storage", "Columnstore"], "databases", ["architect"], "practitioner"),
    "Hypertable": ("hypertable", "Hypertable (TimescaleDB)", [], [], "time-series", ["architect"], "practitioner"),
    "Write-Ahead Log (WAL)": ("write-ahead-log", "Write-Ahead Log (WAL)", ["WAL"], [], "databases", ["architect"], "practitioner"),
    "MVCC (Multi-Version Concurrency Control)": ("mvcc", "Multi-Version Concurrency Control (MVCC)", ["MVCC"], [], "databases", ["architect"], "practitioner"),
    "Partition Pruning": ("partition-pruning", "Partition Pruning", [], [], "databases", ["architect"], "practitioner"),
    "BRIN Index": ("brin-index", "Block Range Index (BRIN)", ["BRIN"], ["BRIN index"], "databases", ["architect"], "practitioner"),
    "Continuous Aggregate": ("continuous-aggregate", "Continuous Aggregate (TimescaleDB)", [], [], "time-series", ["architect"], "practitioner"),
    "Retention Policy / Data Tiering": ("data-retention-policy", "Data Retention Policy", [], ["Retention policy", "Data tiering"], "databases", ["architect", "cloud"], "practitioner"),
    "Change Detection (Zone.js vs. Signals)": ("angular-change-detection", "Angular Change Detection", [], ["Change detection"], "frontend", ["architect"], "practitioner"),
    "Backpressure": ("backpressure", "Backpressure", [], [], "realtime", ["architect"], "practitioner"),
    "Optimistic UI Update": ("optimistic-ui-update", "Optimistic UI Update", [], ["Optimistic update"], "frontend", ["architect"], "practitioner"),
    "Hydration": ("hydration", "Hydration", [], [], "frontend", ["architect"], "practitioner"),
    "Virtual Scrolling / Windowing": ("virtual-scrolling", "Virtual Scrolling", [], ["Windowing", "List virtualization"], "frontend", ["architect"], "practitioner"),
    "Cold vs. Hot Observable": ("cold-observable", "Cold Observable", [], [], "frontend", ["architect"], "practitioner"),
    "Server-Sent Events (SSE)": ("server-sent-events", "Server-Sent Events (SSE)", ["SSE"], [], "realtime", ["architect"], "practitioner"),
    "Immutable Infrastructure": ("immutable-infrastructure", "Immutable Infrastructure", [], [], "devops", ["architect", "cloud"], "practitioner"),
    "Blue-Green Deployment": ("blue-green-deployment", "Blue-Green Deployment", [], ["Blue/green deployment"], "devops", ["architect", "cloud"], "practitioner"),
    "Canary Release": ("canary-release", "Canary Release", [], ["Canary deployment"], "devops", ["architect", "cloud"], "practitioner"),
    "Sidecar Pattern": ("sidecar-pattern", "Sidecar Pattern", [], ["Sidecar"], "containers", ["architect", "cloud"], "practitioner"),
    "Health Check (Liveness vs. Readiness)": ("health-check", "Health Check", [], ["Health probe"], "sre", ["architect", "cloud"], "practitioner"),
    "Infrastructure as Code (IaC)": ("infrastructure-as-code", "Infrastructure as Code (IaC)", ["IaC"], [], "iac", ["architect", "cloud"], "foundation"),
    "Horizontal vs. Vertical Scaling": ("horizontal-scaling", "Horizontal Scaling", [], ["Scaling out", "Scale-out"], "cloud-foundations", ["architect", "cloud"], "foundation"),
    "mTLS (Mutual TLS)": ("mtls", "Mutual TLS (mTLS)", ["mTLS"], ["Mutual TLS authentication"], "cryptography", ["security"], "practitioner"),
    "Workload Identity": ("workload-identity", "Workload Identity", [], [], "identity", ["security", "cloud"], "practitioner"),
    "Capability-Based AuthZ": ("capability-based-authorization", "Capability-Based Authorization", [], ["Capability-based authz", "Object-capability security"], "identity", ["security", "agentic-ai"], "expert"),
    "Wasm Sandboxing": ("wasm-sandboxing", "WebAssembly Sandboxing", [], ["Wasm sandboxing"], "appsec", ["security", "agentic-ai"], "expert"),
    "Zero Trust Architecture": ("zero-trust", "Zero Trust Architecture", ["ZTA"], ["Zero trust"], "security-foundations", ["security", "architect"], "foundation"),
    "OAuth 2.0 Client Credentials Flow": ("oauth-client-credentials-flow", "OAuth 2.0 Client Credentials Flow", [], ["Client credentials grant"], "identity", ["security"], "practitioner"),
    "Least Privilege": ("least-privilege", "Principle of Least Privilege", ["PoLP"], ["Least privilege"], "security-foundations", ["security"], "foundation"),
    "Secrets Rotation": ("secrets-rotation", "Secrets Rotation", [], ["Credential rotation"], "identity", ["security", "cloud"], "practitioner"),
}

# Match the "](target)" tail so link text that wraps across lines is handled too.
_INLINE = re.compile(r"(\]\(\s*<?)([^)\s>]+)(>?(?:\s+\"[^\"]*\"|\s+'[^']*')?\s*\))")
_REFDEF = re.compile(r"^(\s{0,3}\[[^\]]+\]:\s*<?)(\S+?)(>?(?:\s+[\"'(].*)?)$")


def rewrite_links(text: str, fn) -> str:
    """Apply fn(target) -> new target | None to every link outside code."""
    lines = text.split("\n")
    mask = mdscan.code_mask(lines)
    out = []
    for i, line in enumerate(lines):
        if mask[i]:
            out.append(line)
            continue
        spans = [(m.start(), m.end()) for m in re.finditer(r"(`+)(?:.+?)\1", line)]

        def in_code(pos: int) -> bool:
            return any(a <= pos < b for a, b in spans)

        def sub(m: re.Match) -> str:
            if in_code(m.start()):
                return m.group(0)
            new = fn(m.group(2))
            return m.group(0) if new is None else f"{m.group(1)}{new}{m.group(3)}"

        line = _INLINE.sub(sub, line)
        rd = _REFDEF.match(line)
        if rd and not in_code(0):
            new = fn(rd.group(2))
            if new is not None:
                line = f"{rd.group(1)}{new}{rd.group(3)}"
        out.append(line)
    return "\n".join(out)


def _is_external(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", target)) or target.startswith("//")


def _authored_pages(docs: Path) -> list[str]:
    pages = []
    for p in sorted(docs.rglob("*.md")):
        rel = p.relative_to(docs).as_posix()
        top = rel.split("/", 1)[0]
        if top in ("terms", "glossary", "study") or rel.startswith(("_terms/", "_study/", "_glossary/", "_data/")):
            continue
        pages.append(rel)
    return pages


def _git_tracked(root: Path, rel: str) -> bool:
    r = subprocess.run(["git", "ls-files", "--error-unmatch", rel], cwd=root, capture_output=True)
    return r.returncode == 0


def move_pages(root: Path, apply: bool) -> int:
    docs = root / "docs"
    pages = _authored_pages(docs)
    moves = {old: new for old, new in MOVES.items() if (docs / old).is_file()}
    print(f"{len(moves)} page moves:")
    for old, new in moves.items():
        print(f"  {old} -> {new}")
    changed = 0
    texts: dict[str, str] = {}
    for page in pages:
        new_page = moves.get(page, page)
        original = (docs / page).read_text(encoding="utf-8")

        def fix(target: str, page=page, new_page=new_page) -> str | None:
            if _is_external(target) or target.startswith("#"):
                return None
            path, _, frag = target.partition("#")
            if not path:
                return None
            resolved = paths.resolve(page, path)
            mapped = moves.get(resolved, resolved)
            rel = paths.rel_link(new_page, mapped)
            new = rel + (f"#{frag}" if frag else "")
            return None if new == target else new

        updated = rewrite_links(original, fix)
        if updated != original:
            changed += 1
            print(f"  relink {page}")
        texts[page] = updated
    if not apply:
        print(f"plan only: {len(moves)} moves, {changed} files relinked (run with --apply)")
        return 0
    for page, text in texts.items():
        (docs / page).write_text(text, encoding="utf-8", newline="\n")
    for old, new in moves.items():
        (docs / new).parent.mkdir(parents=True, exist_ok=True)
        rel_old, rel_new = f"docs/{old}", f"docs/{new}"
        if _git_tracked(root, rel_old):
            subprocess.run(["git", "mv", rel_old, rel_new], cwd=root, check=True)
        else:
            (docs / old).rename(docs / new)
    for folder in sorted({(docs / o).parent for o in moves}, reverse=True):
        if folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()
    print(f"applied: {len(moves)} moves, {changed} files relinked")
    return 0


def _parse_glossary(text: str) -> tuple[str, list[dict]]:
    """Return (intro markdown, entries) from the single-page glossary."""
    body = text
    if body.startswith("---\n"):
        end = body.find("\n---\n", 4)
        body = body[end + 5 :]
    lines = body.split("\n")
    intro: list[str] = []
    entries: list[dict] = []
    current: dict | None = None
    group = ""
    for line in lines:
        if line.startswith("## "):
            group = line[3:].strip()
            current = None
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            current = {"heading": title, "group": group, "anchor": slugify(title, "-"), "lines": []}
            entries.append(current)
            continue
        if current is None:
            if not group and not line.startswith("# "):
                intro.append(line)
        else:
            current["lines"].append(line)
    return "\n".join(intro).strip(), entries


def _anchor_map() -> dict[str, str]:
    return {slugify(heading, "-"): plan[0] for heading, plan in GLOSSARY_PLAN.items()}


def _glossary_link_fixer(page: str, anchor_to_slug: dict[str, str]):
    def fix(target: str) -> str | None:
        if _is_external(target) or target.startswith("#"):
            return None
        path, _, frag = target.partition("#")
        if paths.resolve(page, path) != "glossary.md":
            return None
        if frag and frag in anchor_to_slug:
            return paths.rel_link(page, f"terms/{anchor_to_slug[frag]}.md")
        return paths.rel_link(page, "glossary/index.md")
    return fix


def relink_glossary(root: Path) -> int:
    """Rewrite any remaining glossary.md#anchor links (safe to re-run)."""
    docs = root / "docs"
    amap = _anchor_map()
    changed = 0
    for page in _authored_pages(docs):
        original = (docs / page).read_text(encoding="utf-8")
        updated = rewrite_links(original, _glossary_link_fixer(page, amap))
        if updated != original:
            (docs / page).write_text(updated, encoding="utf-8", newline="\n")
            changed += 1
            print(f"  relink {page}")
    print(f"{changed} pages relinked")
    return 0


def split_glossary(root: Path, apply: bool, plan_file: str | None = None) -> int:
    docs = root / "docs"
    gpath = docs / "glossary.md"
    if not gpath.is_file():
        print("docs/glossary.md not found (already split); relinking any leftover glossary.md links")
        return relink_glossary(root) if apply else 0
    intro, entries = _parse_glossary(gpath.read_text(encoding="utf-8"))
    anchor_to_slug: dict[str, str] = {}
    problems = 0
    for e in entries:
        plan = GLOSSARY_PLAN.get(e["heading"])
        if not plan:
            print(f"  no plan for '{e['heading']}'")
            problems += 1
            continue
        e["plan"] = plan
        anchor_to_slug[e["anchor"]] = plan[0]
    print(f"{len(entries)} glossary entries, {len(anchor_to_slug)} planned")
    for e in entries:
        if "plan" in e:
            print(f"  #{e['anchor']} -> terms/{e['plan'][0]}.md  ({e['plan'][1]})")
    if problems:
        return 1

    def term_source(e: dict) -> str:
        slug, title, acronyms, aliases, domain, tracks, level = e["plan"]
        text = "\n".join(e["lines"]).strip()
        see = ""
        m = re.search(r"^\*See:\s*(.+?)\*\s*$", text, re.M)
        if m:
            see = m.group(1).strip().rstrip(".")
            text = (text[: m.start()] + text[m.end():]).strip()

        def fix(target: str) -> str | None:
            if _is_external(target):
                return None
            path, _, frag = target.partition("#")
            if not path:  # in-glossary anchor
                return f"{anchor_to_slug[frag]}.md" if frag in anchor_to_slug else None
            resolved = paths.resolve("glossary.md", path)
            if resolved == "glossary.md" and frag in anchor_to_slug:
                return f"{anchor_to_slug[frag]}.md"
            return paths.rel_link(f"terms/{slug}.md", resolved) + (f"#{frag}" if frag else "")

        text = rewrite_links(text, fix)
        see = rewrite_links(see, fix)
        flat = re.sub(r"\s+", " ", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)).strip()
        first = re.match(r"(.+?[.!?])(\s|$)", flat)
        summary = (first.group(1) if first else flat)[:300]

        def yl(items: list[str]) -> str:
            return "[" + ", ".join(f'"{x}"' for x in items) + "]"

        fm = [
            "---",
            f'title: "{title}"',
            f'summary: "{summary.replace(chr(34), chr(39))}"',
            f"acronyms: {yl(acronyms)}",
            f"aliases: {yl(aliases)}",
            f"tracks: [{', '.join(tracks)}]",
            f"domain: {domain}",
            "cloud: neutral",
            f"level: {level}",
            "status: draft",
            "---",
            "",
            "## Explanation",
            "",
            text,
            "",
        ]
        if see:
            fm += ["## Further reading", "", "- " + see.replace(", ", "\n- "), ""]
        return "\n".join(fm)

    sources = {e["plan"][0]: term_source(e) for e in entries}

    def fix_page(page: str):
        def fix(target: str) -> str | None:
            if _is_external(target) or target.startswith("#"):
                return None
            path, _, frag = target.partition("#")
            resolved = paths.resolve(page, path)
            if resolved != "glossary.md":
                return None
            if frag and frag in anchor_to_slug:
                return paths.rel_link(page, f"terms/{anchor_to_slug[frag]}.md")
            return paths.rel_link(page, "glossary/index.md") + (f"#{frag}" if frag and frag not in anchor_to_slug else "")
        return fix

    rewritten = {}
    for page in _authored_pages(docs):
        if page == "glossary.md":
            continue
        original = (docs / page).read_text(encoding="utf-8")
        updated = rewrite_links(original, fix_page(page))
        if updated != original:
            rewritten[page] = updated
            print(f"  relink {page}")
    if not apply:
        print(f"plan only: {len(sources)} term sources, {len(rewritten)} pages relinked (run with --apply)")
        return 0
    (docs / "_terms").mkdir(parents=True, exist_ok=True)
    for slug, text in sources.items():
        (docs / "_terms" / f"{slug}.md").write_text(text, encoding="utf-8", newline="\n")
    for page, text in rewritten.items():
        (docs / page).write_text(text, encoding="utf-8", newline="\n")
    (docs / "_glossary").mkdir(parents=True, exist_ok=True)
    frame = re.sub(r'!!! tip "How to use this page"\n(    .*\n?)+', "", intro).strip()
    (docs / "_glossary" / "index.md").write_text(frame + "\n", encoding="utf-8", newline="\n")
    if _git_tracked(root, "docs/glossary.md"):
        # -f: the only local edits are this migration's own relinks.
        subprocess.run(["git", "rm", "-q", "-f", "docs/glossary.md"], cwd=root, check=True)
    else:
        gpath.unlink()
    print(f"applied: {len(sources)} term sources written to docs/_terms/, {len(rewritten)} pages relinked, docs/glossary.md removed")
    return 0
