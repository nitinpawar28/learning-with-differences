---
title: "Write-Ahead Log (WAL)"
summary: "A durability mechanism where every change is appended to a sequential log *before* it's applied to the actual data files."
acronyms: ["WAL"]
aliases: []
tracks: [architect]
domain: databases
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A durability mechanism where every change is appended to a sequential log
*before* it's applied to the actual data files. On crash, the WAL is replayed
to recover uncommitted-to-disk changes. Postgres/TimescaleDB use it for
crash recovery and as the basis for streaming replication and CDC.
