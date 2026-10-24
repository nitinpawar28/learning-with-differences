---
title: "Multi-Version Concurrency Control (MVCC)"
summary: "A concurrency strategy where writers create new row versions instead of overwriting in place, letting readers see a consistent snapshot without blocking writers (and vice versa)."
acronyms: ["MVCC"]
aliases: []
tracks: [architect]
domain: databases
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A concurrency strategy where writers create new row versions instead of
overwriting in place, letting readers see a consistent snapshot without
blocking writers (and vice versa). Postgres implements isolation levels on
top of MVCC; it's why "Read Committed" in Postgres behaves differently than
lock-based isolation in other engines.

## Further reading

- [Relational Databases](../data/relational/relational-databases.md)
