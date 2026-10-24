---
title: "Workload Identity"
summary: "An identity issued to a *running workload* (a pod, container, or process) by the platform itself — typically as a short-lived, automatically-rotated token — rather than a long-lived credential baked into config or an environment variable."
acronyms: []
aliases: []
tracks: [security, cloud]
domain: identity
cloud: neutral
level: practitioner
status: draft
---

## Explanation

An identity issued to a *running workload* (a pod, container, or process) by
the platform itself — typically as a short-lived, automatically-rotated
token — rather than a long-lived credential baked into config or an
environment variable. Removes an entire class of leaked-secret incidents by
removing the long-lived secret.

## Further reading

- [Workload Identity vs. Static Credentials](../security/iam/workload-identity.md)
