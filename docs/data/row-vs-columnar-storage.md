---
title: "Row-Oriented vs. Columnar Storage"
description: Why the same query can be fast or slow purely based on how bytes are laid out on disk.
tags:
  - data
  - storage-engines
---

# Row vs. Columnar Storage

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- [Row vs. columnar storage](../glossary.md#row-vs-columnar-storage) layout and why it changes which queries are cheap
- OLTP-shaped access (point lookups, single-row writes) vs. OLAP-shaped access (full-column scans, aggregation)
- PostgreSQL/TimescaleDB row-major heap storage vs. columnar extensions (e.g. `timescaledb-columnstore`, Citus columnar) for cold hypertable chunks
- Compression ratios: columnar's per-column encoding vs. row-store's per-row compression
- Hybrid designs: row storage for recent/hot data, columnar for compressed historical chunks (ties into [Hypertables](../glossary.md#hypertable))
