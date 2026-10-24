---
title: "RxJS vs. Store-Based State Management"
description: Reactive streams, state containers, and signals for Angular applications.
tags:
  - frontend
  - rxjs
  - state-management
status: stub
level: practitioner
tracks: [architect]
---

# RxJS & State Management

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- Raw RxJS streams vs. a store (NgRx / NGXS / Akita) for shared state
- NgRx (Redux pattern) vs. Signals-based state
- `switchMap` vs. `mergeMap` vs. `concatMap` vs. `exhaustMap` — when each is correct
- Component-local state vs. global store — where the boundary should sit
- Cold vs. hot observables, and subject variants (`Subject`, `BehaviorSubject`, `ReplaySubject`)
