---
title: "Idempotency Key"
summary: "A unique identifier attached to an operation (a request or a message) so that processing it more than once has the same effect as processing it once."
acronyms: []
aliases: []
tracks: [architect]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A unique identifier attached to an operation (a request or a message) so
that processing it more than once has the same effect as processing it once.
The standard way to convert an [at-least-once](at-least-once-delivery.md)
system into one that behaves like exactly-once from the consumer's
perspective.

## Further reading

- [Outbox Pattern](../messaging/eventing/outbox-pattern.md)
- [Delivery Semantics](../messaging/eventing/delivery-semantics.md)
