---
title: "Capability-Based Authorization"
summary: "An authorization model where holding an unforgeable reference (a 'capability' — e.g."
acronyms: []
aliases: ["Capability-based authz", "Object-capability security"]
tracks: [security, agentic-ai]
domain: identity
cloud: neutral
level: expert
status: draft
---

## Explanation

An authorization model where holding an unforgeable reference (a
"capability" — e.g. a scoped, signed token naming exactly the resource and
action it permits) *is* the permission, as opposed to Role-Based Access
Control, where permission is looked up from an identity/role at each call.
Capabilities are attenuable (you can derive a narrower capability from a
broader one) and resist confused-deputy attacks by construction.

## Further reading

- [Capability-Based AuthZ vs. RBAC](../security/iam/capability-based-authz.md)
