---
title: "Redis Streams (Current) vs. Kafka (Candidate)"
description: When our current-stack choice of Redis Streams holds up, and when Kafka's log-compaction and durability guarantees earn the extra operational cost.
tags:
  - messaging
  - streaming
  - redis
  - kafka
status: stub
level: practitioner
tracks: [architect]
---

# Redis Streams vs. Kafka

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- Redis Streams (current stack) vs. Kafka (candidate) as the backbone for event/streaming workloads
- `XADD` + `MAXLEN` trim vs. Kafka's segment-based [log compaction](../../terms/log-compaction.md) and retention
- Consumer groups in Redis Streams vs. Kafka consumer groups + partition rebalancing
- In-memory-first (Redis, AOF/RDB persistence) vs. disk-first (Kafka log segments) durability models
- At-most-once vs. [at-least-once vs. exactly-once](../../terms/at-least-once-delivery.md) delivery guarantees on each platform
- Fan-out to many consumers vs. competing-consumer load distribution
