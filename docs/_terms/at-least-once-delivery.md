---
title: "At-Least-Once Delivery"
summary: "Delivery guarantees a messaging system offers a consumer."
acronyms: []
aliases: []
tracks: [architect]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Delivery guarantees a messaging system offers a consumer. **At-most-once**
delivers zero or one time (fire-and-forget — messages can be lost).
**At-least-once** retries until acknowledged, so a message may be delivered
more than once (consumers must be idempotent). **Exactly-once** guarantees
each message is processed a single time, usually via transactional
producer/consumer coordination — it's expensive and rarely free of caveats,
which is why most systems settle for at-least-once plus an
[idempotency key](idempotency-key.md).

## Further reading

- [Delivery Semantics](../messaging/eventing/delivery-semantics.md)
- [Redis Streams vs. Kafka](../messaging/eventing/redis-streams-vs-kafka.md)
