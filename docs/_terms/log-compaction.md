---
title: "Log Compaction"
summary: "A retention strategy (native to Kafka) that keeps only the *latest* record per key instead of deleting by age, so a topic can act as a compacted changelog of current state rather than a pure event history."
acronyms: []
aliases: []
tracks: [architect]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A retention strategy (native to Kafka) that keeps only the *latest* record
per key instead of deleting by age, so a topic can act as a compacted
changelog of current state rather than a pure event history. Redis Streams
has no native equivalent — retention there is time- or size-bounded via
[`MAXLEN` trim](maxlen-trim.md).

## Further reading

- [Redis Streams vs. Kafka](../messaging/eventing/redis-streams-vs-kafka.md)
