---
title: "Outbox Pattern vs. Dual-Write"
description: Guaranteeing atomicity between a state change and the event that announces it.
tags:
  - messaging
  - reliability
---

# Outbox Pattern vs. Dual-Write

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- The [Outbox Pattern](../glossary.md#outbox-pattern) (write state + event in one local transaction, relay separately) vs. naive dual-write (write to DB, then publish — two failure points)
- Transactional outbox + polling publisher vs. transactional outbox + CDC (e.g. Debezium-style log tailing)
- Relay-once semantics vs. relayer-induced duplicate delivery (and why consumers still need [idempotency](../glossary.md#idempotency-key))
- Outbox table growth/cleanup strategy vs. an unbounded audit log
- Where this pattern applies: TimescaleDB/Postgres write path publishing to Redis Streams
