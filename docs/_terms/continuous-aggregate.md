---
title: "Continuous Aggregate (TimescaleDB)"
summary: "A TimescaleDB materialized view that incrementally refreshes as new data arrives, instead of recomputing from scratch."
acronyms: []
aliases: []
tracks: [architect]
domain: time-series
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A TimescaleDB materialized view that incrementally refreshes as new data
arrives, instead of recomputing from scratch. Used to pre-aggregate raw
ticks into OHLCV-style bars without re-scanning the full hypertable on every
query.

## Further reading

- [Time-Series / Financial Data Schemas](../data/time-series/time-series-financial-schemas.md)
