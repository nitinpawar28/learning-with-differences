---
title: "Mutual TLS (mTLS)"
summary: "TLS where *both* sides present and verify a certificate, not just the server."
acronyms: ["mTLS"]
aliases: ["Mutual TLS authentication"]
tracks: [security]
domain: cryptography
cloud: neutral
level: practitioner
status: draft
---

## Explanation

TLS where *both* sides present and verify a certificate, not just the
server. Proves the identity of the calling service as well as the one being
called — the standard way to authenticate service-to-service traffic inside
a private network without relying on a shared secret.

## Further reading

- [mTLS vs. API Keys](../security/iam/mtls-vs-api-keys.md)
