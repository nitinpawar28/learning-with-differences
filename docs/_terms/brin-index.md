---
title: "Block Range Index (BRIN)"
summary: "A Block Range Index: instead of indexing every row (like a B-tree), it stores the min/max value per block range."
acronyms: ["BRIN"]
aliases: ["BRIN index"]
tracks: [architect]
domain: databases
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A Block Range Index: instead of indexing every row (like a B-tree), it
stores the min/max value per block range. Extremely small and cheap to
maintain, and effective specifically when data is naturally correlated with
insertion order — the common case for append-mostly time-series tables.

## Further reading

- [High-Frequency Indexing & Partitioning](../data/time-series/high-frequency-indexing-partitioning.md)
