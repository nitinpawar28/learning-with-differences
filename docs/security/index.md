---
title: "Security"
description: "Security foundations, identity, threat modeling, application and supply-chain security, cloud security, detection, GRC and AI security."
---

# Security, Identity & Protocols

*Security, Identity & Protocols*

## Domain Overview & Architectural Context

This category is newly promoted to a first-class, cross-cutting concern
rather than a footnote on other articles — driven directly by MCP entering
the stack. Once a system starts letting an AI agent invoke tools against
live services, "how do we authenticate and authorize this call, and what
sandbox does it run in" stops being an edge case and becomes a load-bearing
design question for every integration.

The throughline across this category is a shift from *ambient, long-lived
trust* to *scoped, short-lived, provable trust*: certificates instead of
shared secrets ([mTLS](../terms/mtls.md)), platform-issued
tokens instead of static credentials ([workload
identity](../terms/workload-identity.md)), unforgeable scoped grants
instead of role lookups ([capability-based
authz](../terms/capability-based-authorization.md)), and a narrow, memory-safe
execution boundary instead of a shared-kernel container for anything running
code we don't fully trust ([Wasm sandboxing](../terms/wasm-sandboxing.md)).
Every article in this folder is really one argument, applied at a different
layer of the stack.

## Key Terminology & Concepts

Full definitions in the [Master Glossary](../glossary/index.md); the ones specific
to this category:

- [mTLS](../terms/mtls.md) — both sides of a connection prove
  their identity, not just the server
- [Workload Identity](../terms/workload-identity.md) — short-lived,
  platform-issued identity for a running service instead of a baked-in
  secret
- [Capability-Based AuthZ](../terms/capability-based-authorization.md) —
  possession of an unforgeable, scoped reference *is* the permission
- [Wasm Sandboxing](../terms/wasm-sandboxing.md) — running untrusted code
  behind a deny-by-default, memory-safe VM boundary
- [Zero Trust Architecture](../terms/zero-trust.md) — no
  implicit trust from network location alone
- [Least Privilege](../terms/least-privilege.md) — the design target
  every mechanism above is aiming at
- [Secrets Rotation](../terms/secrets-rotation.md) — bounding how long a
  leaked credential stays useful

## Intended Knowledge Summary

By the time the articles in this folder are filled in, the reader should be
able to:

1. Explain why a static API key and a workload-identity token solve the
   "who is calling me" problem differently, and pick correctly between them
   for a given integration (internal service vs. external broker API).
2. Design an MCP tool-invocation path with an explicit trust boundary: what
   identity the call carries, what capability it's scoped to, and what
   sandbox the tool executes in.
3. Compare capability-based authorization against RBAC concretely enough to
   explain why a capability system resists confused-deputy attacks that an
   RBAC check doesn't.
4. Justify, with a specific threat model, when Wasm sandboxing is worth
   adopting for untrusted tool execution vs. when a container is still the
   pragmatic (if less pure) answer.
5. Apply "zero trust" as a set of concrete mechanisms (mTLS, workload
   identity, least privilege) rather than as a marketing term.

## Planned Topic Matrix

| Topic | Current Stack | Candidate / Alternative | Key Trade-off | Article |
|---|---|---|---|---|
| Service-to-service auth | mTLS (internal services) | Static API keys / shared secrets | Certificate rotation & transport-layer identity vs. simplicity of a bearer token | [mTLS vs. API Keys](iam/mtls-vs-api-keys.md) |
| Credential lifecycle | Workload identity (short-lived, platform-issued) | Static credentials (`.env` secrets, connection strings) | Bounded leak blast-radius vs. availability on self-hosted infra | [Workload Identity vs. Static Credentials](iam/workload-identity.md) |
| Authorization model | Capability-based (scoped, unforgeable grants) | RBAC (role lookup per call) | Confused-deputy resistance & attenuation vs. ease of retrofitting | [Capability-Based AuthZ vs. RBAC](iam/capability-based-authz.md) |
| Untrusted code execution | Wasm sandboxing (MCP tool runners) | Container isolation | Narrow, memory-safe boundary & fast cold start vs. familiar tooling & native OS access | [Wasm Sandboxing vs. Container Isolation](appsec/wasm-sandboxing.md) |
