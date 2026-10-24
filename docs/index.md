# Learning with Differences

A knowledge base built around one question, asked over and over against our
own production stack: **"what's actually different between these two
options, and when does that difference matter?"**

This is Phase 1 of the repository — the foundational framework. It
establishes the [glossary](glossary.md), the directory structure, and a
per-domain knowledge summary for each category, ahead of the individual
deep-dive comparison articles that will fill in underneath them.

## Platform context

Every comparison in this repo is written against a specific, current stack —
not in the abstract. Where an article says "current" vs. "candidate," it
means:

| Layer | Current stack |
|---|---|
| Backend runtime | .NET 9 / C# |
| Frontend framework | Angular 20 |
| Messaging / streaming | Redis Streams |
| Storage / time-series | TimescaleDB (PostgreSQL) |
| Local orchestration | Docker Compose |
| AI tool orchestration | MCP (Model Context Protocol) |

Articles compare this stack against credible alternatives (Kafka, Kubernetes,
NgRx, InfluxDB, and so on) — the goal isn't to justify the current stack, it's
to know precisely where its edges are.

## How the repository is organized

<div class="grid cards" markdown>

- :material-swap-horizontal: **[Messaging & Eventing](messaging/index.md)**
  Backend & asynchronous messaging — .NET services, SignalR, Redis Streams,
  the outbox pattern, delivery semantics, and MCP tool orchestration

- :material-database: **[Data & Storage Systems](data/index.md)**
  Relational modeling, TimescaleDB hypertables, row vs. columnar storage,
  and high-frequency indexing & partitioning

- :material-angular: **[Frontend & Real-Time UI](frontend/index.md)**
  Angular, TypeScript, RxJS & state management, and rendering high-frequency
  push-based data

- :material-docker: **[DevOps & Cloud-Native](devops/index.md)**
  Docker Compose & containerization, CI/CD pipelines, and bare-metal Linux
  home-server infrastructure

- :material-shield-lock: **[Security, Identity & Protocols](security/index.md)**
  mTLS, workload identity, capability-based authorization, and Wasm
  sandboxing for untrusted tool execution

</div>

## Reference

- **[Master Glossary](glossary.md)** — every recurring term, defined once,
  linked from wherever it's used
- **[Article Template](_templates/tech-guide-template.md)** — the structure
  every deep-dive comparison follows: overview → key differences →
  comparative matrix → when to use / not → code across the stack →
  performance considerations

!!! note "Status: Phase 1"
    The five category pages above are populated with domain overviews,
    terminology, and a **planned topic matrix** — a roadmap of the
    comparisons to come. Individual topic pages exist as scoped stubs
    (see each page's "Status" note) and get expanded to full articles in
    Phase 2, using the [article template](_templates/tech-guide-template.md).
