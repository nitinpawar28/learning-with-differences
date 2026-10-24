---
title: "Relational Databases: Modeling & Engine Trade-offs"
description: Normalization, isolation levels, and engine-specific behavior differences.
tags:
  - data
  - sql
status: stub
level: practitioner
tracks: [architect]
---

# Relational Databases

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- Normalization (3NF) vs. denormalization for read-heavy workloads
- Isolation levels: Read Committed vs. Snapshot vs. Serializable
- Clustered vs. non-clustered indexes
- SQL Server vs. PostgreSQL — locking, MVCC, and tooling differences
- Optimistic vs. pessimistic concurrency control
