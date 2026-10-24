---
title: "Relational Databases: Modeling & Engine Trade-offs"
description: Normalization, isolation levels, and engine-specific behavior differences.
tags:
  - data
  - sql
---

# Relational Databases

!!! note "Status"
    Draft stub — expand using the [article template](../_templates/tech-guide-template.md).

## Scope

Compare choices such as:

- Normalization (3NF) vs. denormalization for read-heavy workloads
- Isolation levels: Read Committed vs. Snapshot vs. Serializable
- Clustered vs. non-clustered indexes
- SQL Server vs. PostgreSQL — locking, MVCC, and tooling differences
- Optimistic vs. pessimistic concurrency control
