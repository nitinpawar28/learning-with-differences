---
title: "mTLS vs. API Keys / Shared Secrets"
description: Certificate-based mutual authentication vs. bearer-token secrets for service-to-service auth.
tags:
  - security
  - protocols
status: stub
level: practitioner
tracks: [security]
---

# mTLS vs. API Keys / Shared Secrets

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- [mTLS](../../terms/mtls.md) (both peers present certificates) vs. a static API key/shared secret in a header
- Certificate issuance/rotation (short-lived certs, an internal CA or service mesh) vs. manual key rotation and the leaked-secret blast radius
- Transport-layer identity (mTLS proves *which service*) vs. application-layer identity (an API key proves *possession of a string*)
- Where a service mesh sidecar (Envoy/Linkerd) can provide mTLS transparently vs. terminating TLS at the app layer
- Practical rollout: internal service-to-service calls (mTLS) vs. external partner/broker API integrations (API keys, often the only option offered)
