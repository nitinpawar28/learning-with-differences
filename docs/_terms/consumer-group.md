---
title: "Consumer Group"
summary: "A set of consumer instances that share the work of reading a stream/topic, where each partition or message is delivered to only one member of the group."
acronyms: []
aliases: []
tracks: [architect]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A set of consumer instances that share the work of reading a stream/topic,
where each partition or message is delivered to only one member of the
group. Both Kafka and Redis Streams (`XREADGROUP`) implement this, letting
you scale consumption horizontally while preserving per-partition ordering.
