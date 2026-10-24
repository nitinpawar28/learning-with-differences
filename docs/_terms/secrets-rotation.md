---
title: "Secrets Rotation"
summary: "Periodically or automatically replacing credentials (API keys, certificates, database passwords) so that a leaked secret has a bounded useful lifetime."
acronyms: []
aliases: ["Credential rotation"]
tracks: [security, cloud]
domain: identity
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Periodically or automatically replacing credentials (API keys, certificates,
database passwords) so that a leaked secret has a bounded useful lifetime.
[Workload identity](workload-identity.md) is effectively rotation taken to its
limit — credentials so short-lived that manual rotation isn't a process
you need at all.
