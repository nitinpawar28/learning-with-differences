---
title: "Time-Series / Financial Data Schemas"
description: Schema design trade-offs for tick data, OHLCV bars, and order-book snapshots.
tags:
  - data
  - time-series
  - finance
status: stub
level: practitioner
tracks: [architect]
---

# Time-Series / Financial Data Schemas

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- Wide (columnar, one row per bar) vs. narrow (EAV-style, one row per tick) schemas
- Purpose-built time-series stores (e.g. TimescaleDB, InfluxDB, kdb+) vs. general-purpose RDBMS
- Storing raw ticks vs. pre-aggregated bars (OHLCV) — and recomputing vs. materializing
- Append-only event log vs. mutable "latest state" tables
- Handling corrections/restatements in immutable time-series data
