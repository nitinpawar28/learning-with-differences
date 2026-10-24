---
title: "Data Retention Policy"
summary: "Automated rules for what happens to data as it ages: drop it, compress it, or move it to cheaper storage (hot → warm → cold)."
acronyms: []
aliases: ["Retention policy", "Data tiering"]
tracks: [architect, cloud]
domain: databases
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Automated rules for what happens to data as it ages: drop it, compress it,
or move it to cheaper storage (hot → warm → cold). TimescaleDB's retention
and compression policies operate per-chunk on a hypertable, which is why the
chunk boundary (time interval) is a real design decision, not an
implementation detail.
