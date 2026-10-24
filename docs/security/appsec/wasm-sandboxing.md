---
title: "Wasm Sandboxing vs. Container Isolation"
description: Running untrusted or third-party code (e.g. MCP tools) safely, at two very different levels of the stack.
tags:
  - security
  - sandboxing
status: stub
level: expert
tracks: [security]
---

# Wasm Sandboxing vs. Container Isolation

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- [Wasm sandboxing](../../terms/wasm-sandboxing.md) (capability-scoped, memory-safe-by-construction, sub-millisecond cold start) vs. container isolation (Docker/OCI, kernel-namespace-based, heavier but more familiar tooling)
- Deny-by-default capability imports (WASI) vs. a container's default network/filesystem access unless explicitly restricted
- Cold-start and density trade-offs when sandboxing many short-lived, untrusted MCP tool invocations
- Escape surface: a Wasm runtime's narrow host interface vs. a container's shared-kernel attack surface
- When a container is still the right call: tools that need native OS dependencies Wasm can't yet reach
