---
title: "Async & Threading: Concurrency Models in .NET"
description: async/await, the thread pool, parallelism, and concurrency primitives.
tags:
  - messaging
  - dotnet
  - concurrency
status: stub
level: practitioner
tracks: [architect]
---

# Async & Threading

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- `async`/`await` vs. blocking synchronous calls
- Task Parallel Library (TPL) vs. raw `Thread`/`Thread Pool` usage
- `Task.Run` (CPU-bound) vs. `async I/O` (I/O-bound) — when each is correct
- `lock` / `Monitor` vs. `SemaphoreSlim` vs. lock-free (`Interlocked`, `Channel<T>`)
- Concurrency vs. parallelism as distinct concerns
