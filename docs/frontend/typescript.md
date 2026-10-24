---
title: "TypeScript: Type-System Trade-offs"
description: Structural typing, strictness settings, and type-level design choices.
tags:
  - frontend
  - typescript
---

# TypeScript

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- `interface` vs. `type` alias
- Structural typing vs. nominal typing (and how to simulate nominal typing)
- `strict` mode on vs. off — what each flag actually buys you
- Generics vs. `any`/`unknown` for flexible APIs
- Discriminated unions vs. class hierarchies for modeling state
