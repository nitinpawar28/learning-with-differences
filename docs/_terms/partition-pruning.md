---
title: "Partition Pruning"
summary: "A query planner optimization where, given a filter on the partition key (e.g."
acronyms: []
aliases: []
tracks: [architect]
domain: databases
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A query planner optimization where, given a filter on the partition key
(e.g. `time > now() - interval '1 day'`), the engine skips scanning
partitions/chunks it can prove don't contain matching rows — turning an
O(total data) scan into O(relevant partitions).

## Further reading

- [High-Frequency Indexing & Partitioning](../data/time-series/high-frequency-indexing-partitioning.md)
