---
title: "Hypertable (TimescaleDB)"
summary: "TimescaleDB's abstraction over a Postgres table that automatically partitions data into **chunks** (by time, and optionally by a space dimension like a symbol/device ID) while still being queried as a single logical table."
acronyms: []
aliases: []
tracks: [architect]
domain: time-series
cloud: neutral
level: practitioner
status: draft
---

## Explanation

TimescaleDB's abstraction over a Postgres table that automatically
partitions data into **chunks** (by time, and optionally by a space
dimension like a symbol/device ID) while still being queried as a single
logical table. It's what makes time-based partition pruning, retention
policies, and compression manageable at high ingest volume without you
hand-rolling partitioned tables.

## Further reading

- [High-Frequency Indexing & Partitioning](../data/time-series/high-frequency-indexing-partitioning.md)
