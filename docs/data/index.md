---
title: "Data and Storage"
description: "Relational modelling, time-series storage, columnar layouts, indexing and caching trade-offs."
---

# Data & Storage Systems

*Data Engineering, Storage & Analytics*

## Domain Overview & Architectural Context

This layer stores and serves the data every other layer depends on — and in
a system built around high-frequency, time-stamped data (ticks, bars,
telemetry), the storage engine's shape is not an implementation detail, it's
the constraint everything else is designed around. A schema that's correct
but slow at 100x the write volume is, in practice, wrong.

The current stack centers on TimescaleDB: PostgreSQL's relational guarantees
(transactions, joins, MVCC, a mature ecosystem) combined with
[hypertables](../terms/hypertable.md) that give it purpose-built
time-series behavior — automatic chunking, retention policies, and
continuous aggregates — without adopting a separate, narrower time-series
database. This category exists to keep that decision honest: know exactly
what a purpose-built engine (InfluxDB, kdb+) would buy back, and what a
general-purpose relational store costs you at scale.

## Key Terminology & Concepts

Full definitions in the [Master Glossary](../glossary/index.md); the ones specific
to this category:

- [Hypertable](../terms/hypertable.md) — TimescaleDB's auto-partitioned
  table abstraction over Postgres
- [Row vs. Columnar Storage](../terms/columnar-storage.md) — why
  the same query is fast or slow purely based on disk layout
- [MVCC](../terms/mvcc.md) — how
  Postgres gives readers a consistent snapshot without blocking writers
- [Partition Pruning](../terms/partition-pruning.md) / [BRIN
  Index](../terms/brin-index.md) — how the planner and the index both
  exploit time-ordered, append-mostly data
- [Continuous Aggregate](../terms/continuous-aggregate.md) — incrementally
  materialized rollups instead of scan-and-recompute
- [Retention Policy / Data Tiering](../terms/data-retention-policy.md) —
  what happens to a chunk as it ages out of "hot"

## Intended Knowledge Summary

By the time the articles in this folder are filled in, the reader should be
able to:

1. Explain what a hypertable actually does under the hood (chunking,
   per-chunk indexes, per-chunk compression) — not just that it "makes
   TimescaleDB fast."
2. Choose between row-major and columnar layout for a given workload, and
   articulate why compression ratios differ between them.
3. Design a partitioning/indexing strategy (chunk interval, BRIN vs. B-tree,
   space partitioning by symbol/device) that keeps both writes and
   time-range queries fast as volume grows.
4. Know when TimescaleDB's relational-plus-hypertable model stops being
   enough, and a purpose-built time-series or columnar engine is the honest
   answer instead of a workaround.
5. Design retention and continuous-aggregate policies that reduce storage
   cost without silently deleting data a compliance or backtesting use case
   still needs.

## Planned Topic Matrix

| Topic | Current Stack | Candidate / Alternative | Key Trade-off | Article |
|---|---|---|---|---|
| Relational modeling & concurrency | PostgreSQL (MVCC, isolation levels) | SQL Server | Locking/MVCC model & tooling differences | [Relational Databases](relational/relational-databases.md) |
| Time-series schema | TimescaleDB hypertables (OHLCV + raw ticks) | Purpose-built stores (InfluxDB, kdb+) | Relational flexibility vs. purpose-built time-series performance | [Time-Series / Financial Schemas](time-series/time-series-financial-schemas.md) |
| Storage layout | Row-oriented (Postgres heap) | Columnar (columnstore extensions) | OLTP point-lookup speed vs. OLAP scan/compression efficiency | [Row vs. Columnar Storage](time-series/row-vs-columnar-storage.md) |
| Indexing & partitioning | Hypertable chunking + BRIN indexes | Manual range/hash partitioning + B-tree | Write-friendly, prune-friendly design vs. general-purpose flexibility | [High-Frequency Indexing & Partitioning](time-series/high-frequency-indexing-partitioning.md) |
