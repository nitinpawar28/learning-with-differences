---
title: "MCP (Current) vs. Custom REST Tool-Calling (Candidate)"
description: Standardized model-context tool orchestration vs. hand-rolled function-calling endpoints.
tags:
  - messaging
  - mcp
  - ai
status: stub
level: practitioner
tracks: [agentic-ai, security]
---

# MCP Tool Orchestration

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- Model Context Protocol (MCP) servers (current stack) vs. bespoke REST/function-calling endpoints per tool (candidate/legacy)
- Standardized tool/resource discovery (MCP's schema-driven contract) vs. ad hoc OpenAPI specs per integration
- Local (stdio) MCP servers vs. remote (HTTP/SSE) MCP servers — trust boundary and latency implications
- Sandboxing untrusted tool execution: [Wasm sandboxing](../../security/appsec/wasm-sandboxing.md) vs. process/container isolation for MCP tool runners
- Session and auth model: [workload identity](../../security/iam/workload-identity.md) for server-to-server MCP calls vs. static API keys
