---
title: "Workload Identity vs. Static Credentials"
description: Letting the platform vouch for a service's identity instead of handing it a long-lived secret.
tags:
  - security
  - identity
status: stub
level: practitioner
tracks: [security]
---

# Workload Identity vs. Static Credentials

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- [Workload identity](../../terms/workload-identity.md) (short-lived, platform-issued tokens tied to a service's runtime identity) vs. static credentials (API keys, connection strings, `.env` secrets)
- SPIFFE/SPIRE-style cryptographic workload identity vs. cloud-native equivalents (Azure Managed Identity, AWS IAM roles for service accounts)
- Home-lab/bare-metal reality: where workload identity is easy to get (cloud) vs. hard to get (self-hosted Docker Compose) — and what the fallback should be
- Blast radius when a credential leaks: a rotated/short-lived token vs. a long-lived secret sitting in a compromised container
- Secrets management as a stopgap (Vault, sealed secrets) when full workload identity isn't available yet
