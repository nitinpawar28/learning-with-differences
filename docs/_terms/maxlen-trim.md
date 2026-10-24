---
title: "MAXLEN Trim (Redis Streams)"
summary: "Redis Streams' mechanism for bounding stream size: `XADD ..."
acronyms: []
aliases: ["Stream trimming"]
tracks: [architect]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Redis Streams' mechanism for bounding stream size: `XADD ... MAXLEN ~ 100000`
caps the stream at roughly N entries, evicting the oldest as new ones arrive.
It trims by count/approximate count, not by key like
[log compaction](log-compaction.md) — two consumers reading the same offset can
diverge if one falls behind the trim horizon.

## Further reading

- [Redis Streams vs. Kafka](../messaging/eventing/redis-streams-vs-kafka.md)
