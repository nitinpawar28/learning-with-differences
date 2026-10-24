---
title: "Sidecar Pattern"
summary: "Deploying a helper process (proxy, log shipper, mTLS terminator) alongside the main application container, sharing its network namespace — used heavily by service meshes to add cross-cutting concerns (retries, mTLS, metrics) without modifying application code."
acronyms: []
aliases: ["Sidecar"]
tracks: [architect, cloud]
domain: containers
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Deploying a helper process (proxy, log shipper, mTLS terminator) alongside
the main application container, sharing its network namespace — used
heavily by service meshes to add cross-cutting concerns (retries, mTLS,
metrics) without modifying application code.

## Further reading

- [mTLS vs. API Keys](../security/iam/mtls-vs-api-keys.md)
