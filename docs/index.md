---
title: "Learning with Differences"
description: "A personal, exam-grade library for architecture, agentic AI, security, Azure and AWS, in which every concept is taught by its differences."
hide:
  - navigation
---

# Learning with Differences

A reference library built around one question, asked of every concept:
**what is this, what is it easily confused with, and what actually separates
them?** You understand a service, a pattern or a protocol properly once you
can say how it differs from its nearest neighbours, and how it maps to its
counterpart on the other cloud.

The library serves four roles, studied side by side:

<div class="grid cards" markdown>

- :material-sitemap: **[Architecture](architecture/index.md)**

    Architecture practice, patterns, distributed systems, data architecture,
    reliability, cost and enterprise architecture.

- :material-microsoft-azure: **[Cloud: Azure and AWS](cloud/index.md)**

    Twelve capabilities covered on both clouds, with the Azure-vs-AWS
    differences spelled out for each.

- :material-robot-outline: **[Agentic AI](ai/index.md)**

    LLM foundations, applied generative AI, agents, the MCP and A2A protocols,
    and the Microsoft Foundry and Amazon Bedrock platforms.

- :material-shield-lock: **[Security](security/index.md)**

    Identity, threat modeling, application and supply-chain security, cloud
    security, detection and response, GRC and AI security.

</div>

## Where to start

<div class="grid cards" markdown>

- :material-certificate: **[Study](study/index.md)**

    The certification roadmap and one page per exam. Each exam page shows the
    official objectives, which pages cover each one, and the gaps that remain.

- :material-book-alphabet: **[Glossary](glossary/index.md)**

    Every term on its own page. Search by name, acronym or former product name
    in the [Explorer](glossary/explorer.md), or compare clouds in the
    [Rosetta](glossary/rosetta.md).

- :material-hammer-wrench: **[Practice](practice/index.md)**

    Paired Azure and AWS labs, design katas, threat models, incident
    tabletops and two capstones.

- :material-information-outline: **[How this library works](about/index.md)**

    Page types, levels, statuses, freshness, and how to read the tabs and
    tooltips.

</div>

## Grounded in a real system

Most comparisons are anchored to a real production stack, so every
"current vs. candidate" decision has a concrete context:

| Layer | Current stack |
|---|---|
| Backend runtime | .NET 9 / C# |
| Frontend framework | Angular 20 |
| Messaging and streaming | Redis Streams |
| Storage and time-series | TimescaleDB (PostgreSQL) |
| Local orchestration | Docker Compose |
| AI tool orchestration | MCP (Model Context Protocol) |

The [Engineering](messaging/index.md) section holds those stack-specific
comparisons. The other sections are vendor-neutral or cover both clouds.

!!! note "Library status"
    The library is being written in waves that follow the
    [exam roadmap](study/exams.md). The [content roadmap](study/reports/roadmap.md)
    shows what is planned, drafted and complete. The
    [coverage report](study/reports/coverage.md) shows how ready each exam is.
