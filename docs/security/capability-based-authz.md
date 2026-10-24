---
title: "Capability-Based AuthZ vs. RBAC"
description: Unforgeable, scoped-by-construction access tokens vs. role checks sprinkled through the code.
tags:
  - security
  - authorization
---

# Capability-Based AuthZ vs. RBAC

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- [Capability-based authorization](../glossary.md#capability-based-authz) (possession of an unforgeable, scoped reference *is* the permission) vs. Role-Based Access Control (identity → role → permission lookup at every call)
- Ambient authority (RBAC's "am I logged in as an admin right now") vs. capability's explicit, per-object grants — and why the latter resists confused-deputy attacks
- Where this matters most: MCP tool servers handing out scoped capabilities per session vs. a single API key with broad role-based access
- Revocation models: expiring/short-lived capability tokens vs. revoking a role and hoping every check re-evaluates it
- Migration cost: RBAC is cheaper to bolt onto an existing system; capabilities usually need to be designed in from the start
