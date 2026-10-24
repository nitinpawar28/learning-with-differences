---
title: "At-Least-Once vs. Exactly-Once Delivery"
description: What each delivery guarantee actually promises, what it costs, and why most systems settle for at-least-once plus idempotency.
tags:
  - messaging
  - reliability
---

# At-Least-Once vs. Exactly-Once Delivery

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- [At-least-once vs. exactly-once](../glossary.md#at-least-once-vs-exactly-once) vs. at-most-once as the three baseline delivery guarantees
- "True" exactly-once (transactional, e.g. Kafka's idempotent producer + transactions) vs. effectively-once (at-least-once delivery + consumer-side [idempotency keys](../glossary.md#idempotency-key))
- The cost of exactly-once: throughput, coordination overhead, and vendor lock-in to a specific broker's transaction model
- Where duplicates actually come from: producer retries, consumer crash-before-ack, rebalances
- Practical default for this stack: Redis Streams at-least-once + idempotent consumers, reserving exactly-once machinery for financially-sensitive writes
