---
title: "Outbox Pattern vs. Dual-Write"
description: Guaranteeing atomicity between a state change and the event that announces it.
tags:
  - messaging
  - reliability
status: stub
level: practitioner
tracks: [architect]
---

# Outbox Pattern vs. Dual-Write

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- The [Outbox Pattern](../../terms/transactional-outbox.md) (write state + event in one local transaction, relay separately) vs. naive dual-write (write to DB, then publish — two failure points)
- Transactional outbox + polling publisher vs. transactional outbox + CDC (e.g. Debezium-style log tailing)
- Relay-once semantics vs. relayer-induced duplicate delivery (and why consumers still need [idempotency](../../terms/idempotency-key.md))
- Outbox table growth/cleanup strategy vs. an unbounded audit log
- Where this pattern applies: TimescaleDB/Postgres write path publishing to Redis Streams
