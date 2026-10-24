---
title: "Real-Time UI Streaming: Rendering Push-Based Data"
description: Techniques for rendering high-frequency, push-based data without blocking the UI thread.
tags:
  - frontend
  - real-time
---

# Real-Time UI Streaming

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- Direct DOM updates vs. framework-managed rendering under high message rates
- Throttling/debouncing/`auditTime` strategies for high-frequency ticks (e.g. market data)
- Virtual scrolling / windowing for large, fast-changing lists
- `OnPush` + immutable updates vs. mutable state for streamed data
- Backpressure handling: buffering, sampling, and dropping strategies
