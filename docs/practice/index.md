---
title: "Practice"
description: "Paired Azure and AWS labs, design katas, threat models, incident tabletops and capstones."
---

# Practice

Reading builds recognition. Practice builds the ability to do the job and to
answer scenario questions under exam pressure. Every practice item here links
back to the articles and terms it exercises.

## Labs

Labs are **paired**: the same capability is built on Azure and on AWS, so the
differences show up in your own hands. Every lab includes:

- an architecture diagram and the objective;
- infrastructure as code: Bicep for Azure, CloudFormation or CDK for AWS, and a
  Terraform variant where it helps compare;
- application code in both C# and Python;
- a cost estimate, a budget alert and a mandatory teardown step;
- a "break it" exercise and reflection questions.

## Design katas, threat models and tabletops

- **Design katas:** a scenario, its constraints and the deliverables (C4
  diagrams, ADRs, a threat model), with a rubric and a model answer you can
  reveal.
- **Threat models:** STRIDE-based models of real systems: an MCP server, a RAG
  application, the trading platform and a multi-account landing zone.
- **Incident tabletops:** a credential leak, ransomware, a cloud account
  takeover, and data exfiltration through prompt injection.

## Capstones

- **Capstone A: the platform on two clouds.** Design the real stack (.NET 9,
  Angular 20, Redis Streams, TimescaleDB, SignalR, MCP) on Azure *and* on AWS,
  with C4 diagrams, ADRs, a cost model and Well-Architected reviews against
  both frameworks.
- **Capstone B: an agent over this glossary.** Build an MCP server over the
  library's own `glossary.json`, plus an agent that uses it. Threat-model it
  against the OWASP Top 10 for Agentic Applications, then harden it with
  capability-scoped authorization, workload identity and sandboxing.

!!! note "Coming in waves"
    Each wave adds the labs and exercises for its exams. Track progress in the
    [content roadmap](../study/reports/roadmap.md).
