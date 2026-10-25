---
title: "Partition Pruning"
summary: "The planner and executor optimisation that skips partitions or chunks whose bounds cannot satisfy a query's filters on the partition key: at planning time for constants, at executor startup for parameters and stable functions, and during execution for values produced by joins and subqueries."
acronyms: []
aliases: ["Partition elimination", "Chunk exclusion"]
formerly: []
tracks: [architect]
domain: databases
cloud: neutral
level: practitioner
status: complete
last_verified: 2026-10-24
differs_from:
  - { term: table-partitioning, note: "Partitioning is the physical split of a table into children; pruning is the optimisation that decides which children a particular query may ignore, and the first is useless for reads without the second." }
  - { term: hypertable, note: "A hypertable supplies time-bounded chunks; TimescaleDB prunes them with its own chunk exclusion (planner, startup and runtime) rather than with PostgreSQL's partition pruning, which only applies to declarative partitions." }
  - { term: brin-index, note: "A BRIN index skips block ranges inside one table using stored min/max summaries; partition pruning skips whole tables using declared bounds, and needs no index at all." }
  - { term: b-tree-index, note: "A B-tree finds matching rows inside a partition after pruning has chosen the partitions; pruning never consults indexes, and an index never removes a partition from the plan." }
related: [data-retention-policy, columnar-storage, continuous-aggregate]
covers: []
sources:
  - { title: "Table Partitioning: Partition Pruning (PostgreSQL 18 documentation)", url: "https://www.postgresql.org/docs/current/ddl-partitioning.html", publisher: PostgreSQL Global Development Group }
  - { title: "Query Planning configuration: enable_partition_pruning, constraint_exclusion", url: "https://www.postgresql.org/docs/current/runtime-config-query.html", publisher: PostgreSQL Global Development Group }
  - { title: "TimescaleDB GUC reference (chunk exclusion settings)", url: "https://www.tigerdata.com/docs/reference/timescaledb/configuration/gucs", publisher: Tiger Data }
  - { title: "Implementing constraint exclusion for faster query performance", url: "https://www.tigerdata.com/blog/implementing-constraint-exclusion-for-faster-query-performance", publisher: Tiger Data }
---

## Explanation

Partition pruning is the optimisation that makes [table partitioning](table-partitioning.md) pay off for reads. Given a filter on the partition key, the database proves from each partition's declared bounds that it cannot hold matching rows and leaves it out, so cost scales with the partitions that matter rather than with the whole table. PostgreSQL decides purely from the bounds in `PARTITION BY` and `FOR VALUES`; indexes play no part, and `enable_partition_pruning` (default `on`) controls both the planner's and the executor's ability to prune.

The subtlety is *when* the proof can be made, because the planner knows only constants at planning time. PostgreSQL prunes at three moments.

1. **During planning**, for comparisons with constants and immutable expressions through an immutable operator, such as `WHERE ordered_at >= TIMESTAMPTZ '2026-10-01 00:00+00'` on a `timestamptz` key. Pruned partitions never enter the plan; `EXPLAIN` shows only the survivors. A cross-type comparison that depends on the session time zone, such as a `timestamptz` key against a `date` constant, uses a stable operator and is pruned only at executor startup.
2. **At executor initialisation**, for values known only when the plan starts: parameters of a prepared statement running with a generic plan, and stable functions such as `now()` or `current_date`, fixed per statement but not per plan. This step runs even under plain `EXPLAIN` (only `EXPLAIN (GENERIC_PLAN)` skips it), so these partitions are absent from both `EXPLAIN` and `EXPLAIN ANALYZE` output and counted as `Subplans Removed: N` on the `Append` node; they were still locked at the start of execution.
3. **During execution**, for values the running plan produces: subquery results and the parameters of a parameterized nested-loop join, where the inner partitioned scan is pruned afresh for each outer row. `EXPLAIN ANALYZE` shows partitions never needed as `(never executed)`.

Two things defeat pruning. Wrapping the key in a function, `date_trunc('day', ordered_at) = ...` or `ordered_at::date = ...`, hides the column from the bound comparison; rewrite as a half-open range on the bare column. And a predicate that never mentions the key, or a join without an equality the planner can use, leaves every partition in the plan, where each adds planning time and per-session metadata. The older mechanism for inheritance-based partitioning, `constraint_exclusion` (default `partition`), examines `CHECK` constraints at planning time only.

Pruning has relatives: *partitionwise join* and *partitionwise aggregate* process matching partitions separately but default to off because of memory and planning cost, and PostgreSQL 18 reduced the planning cost of queries touching many partitions.

TimescaleDB implements the same idea for [hypertable](hypertable.md) chunks as *chunk exclusion*, at the same three moments. The planner excludes chunks for constant predicates (`timescaledb.enable_constraint_exclusion`); the custom `ChunkAppend` node (`timescaledb.enable_chunk_append`) performs *startup exclusion* for stable expressions and *runtime exclusion* (`timescaledb.enable_runtime_exclusion`) for join parameters, reporting `Chunks excluded during startup: N` or `Chunks excluded during runtime: N` in `EXPLAIN`. Because dashboards filter with `now() - interval`, TimescaleDB 2.7 added `timescaledb.enable_now_constify`, which rewrites such predicates into constants at planning time so chunks disappear before the plan is built; on a 20,000-chunk hypertable Tiger Data measured such queries up to 401 times faster. *Chunk skipping* (`enable_chunk_skipping('ticks', 'trade_id')` for an integer, date or timestamp column, a tech-preview feature whose `timescaledb.enable_chunk_skipping` GUC defaults to off) records min/max ranges for a non-partitioning column per chunk when the chunk is converted to the columnstore so filters on that column can exclude chunks too, as the [columnstore](columnar-storage.md) does per segment with its sparse min/max indexes.

In the reader's stack the rules are short: filter on the partitioning column with a half-open range, pass times as `timestamptz` values rather than `date` values (whose cross-type comparison is only stable and postpones pruning to executor startup), never cast the column, and read `EXPLAIN (ANALYZE)` for `Subplans Removed`, `never executed` or `Chunks excluded` before believing that partitioning helped.

```mermaid
flowchart LR
    Q["SELECT ... FROM orders<br/>WHERE ordered_at >= $1"] --> PL["Planning<br/>constants, immutable expressions"]
    PL -- "pruned partitions<br/>never enter the plan" --> EI["Executor init<br/>prepared-statement params, now()"]
    EI -- "Subplans Removed: N" --> EX["Execution<br/>subquery results, nested-loop params"]
    EX -- "(never executed)" --> S["Scan the surviving partitions"]
```

## How it differs

**[Table partitioning](table-partitioning.md)** is the structure and pruning is the behaviour, and conflating them produces the most common partitioning failure: a table split into hundreds of partitions whose queries filter on a column that is not the key, so every query appends every partition and runs slower than before. Design the key from the predicates queries use; then prove with `EXPLAIN` that the planner prunes, and check prepared-statement and join cases with `EXPLAIN ANALYZE`.

**[Hypertable](hypertable.md)** chunks are not declarative partitions, so PostgreSQL's `enable_partition_pruning` does nothing for them. TimescaleDB brings its own machinery, ChunkAppend with startup and runtime exclusion plus `now()` constification, which in practice covers the dashboard-style predicates better than core PostgreSQL does. The practical difference for a developer is the vocabulary in the plan (`Chunks excluded during startup` versus `Subplans Removed`) and the extra chunk-skipping statistics that let non-time columns prune.

**[BRIN index](brin-index.md)** solves the same skipping problem at a finer grain and with a different input. Pruning uses declared bounds and skips whole tables; BRIN uses stored min/max per block range and skips pages inside one table, which only works when the column correlates with physical order. They compose well: prune to a partition, then BRIN inside it. BRIN is also the fallback when you cannot partition.

**[B-tree index](b-tree-index.md)** is consulted after pruning, inside each surviving partition, to find rows; it never removes a partition. The documentation is explicit that pruning is driven only by the partition constraints, not by the presence of indexes. The confusion is understandable because both reduce rows read; the difference is that pruning is free of I/O (it reads catalog bounds) while an index scan reads index pages.

| | Partition pruning | Chunk exclusion (TimescaleDB) | BRIN | B-tree |
|---|---|---|---|---|
| Input | Declared bounds | Chunk constraints | Stored min/max per block range | Sorted keys |
| Granularity | Whole partition | Whole chunk | Page range | Row |
| When | Plan, executor init, execution | Plan, startup, runtime | Scan time | Scan time |
| Needs | Predicate on partition key | Predicate on time (or chunk-skipping column) | Physical correlation | Selective predicate |

## Examples

=== "SQL"

    ```sql
    -- Plan-time pruning: timestamptz constants on a timestamptz key (immutable
    -- operator) leave one partition in the plan. Session TimeZone is UTC here.
    EXPLAIN (COSTS OFF) SELECT count(*) FROM orders
    WHERE ordered_at >= TIMESTAMPTZ '2026-10-01 00:00+00'
      AND ordered_at <  TIMESTAMPTZ '2026-11-01 00:00+00';
    --  Aggregate
    --    ->  Seq Scan on orders_2026_10 orders
    --          Filter: ((ordered_at >= '2026-10-01 00:00:00+00'::timestamp with time zone) AND ...)
    -- With DATE '2026-10-01' instead, the timestamptz-vs-date operator is only stable:
    -- the plan keeps an Append and prunes at executor startup ("Subplans Removed").

    -- Executor-startup pruning: a generic plan cannot know $1 and $2 until it runs.
    PREPARE recent(timestamptz, timestamptz) AS
        SELECT count(*) FROM orders WHERE ordered_at >= $1 AND ordered_at < $2;
    SET plan_cache_mode = force_generic_plan;
    EXPLAIN (ANALYZE, COSTS OFF) EXECUTE recent(now() - interval '1 day', now());
    --  Aggregate (actual ...)
    --    ->  Append (actual ...)
    --          Subplans Removed: 11
    --          ->  Seq Scan on orders_2026_10 orders_1 (actual ...)

    -- Anti-pattern: a cast on the key hides it from pruning; every partition is scanned.
    EXPLAIN SELECT count(*) FROM orders WHERE ordered_at::date = '2026-10-24';

    -- TimescaleDB: the same parameterised shape is excluded by ChunkAppend at startup.
    PREPARE recent_ticks(timestamptz) AS
        SELECT symbol, last(price, time) FROM ticks WHERE time > $1 GROUP BY symbol;
    EXPLAIN (ANALYZE, COSTS OFF) EXECUTE recent_ticks(now() - interval '1 hour');
    --    ->  Custom Scan (ChunkAppend) on ticks
    --          Chunks excluded during startup: 364
    --          ->  Index Scan ... on _hyper_1_365_chunk
    ```

=== "C#"

    ```csharp
    // .NET 9 + Npgsql. Parameters travel through the extended protocol, so an
    // unprepared query is planned with the bound values and pruned at planning time.
    // After PrepareAsync() (or automatic preparation) the server may switch to a
    // generic plan, and pruning moves to executor startup ("Subplans Removed").
    // In both cases the key column must stay bare in the WHERE clause.
    await using var cmd = dataSource.CreateCommand(
        "SELECT count(*) FROM orders WHERE ordered_at >= $1 AND ordered_at < $2");
    cmd.Parameters.Add(new NpgsqlParameter { Value = fromUtc, NpgsqlDbType = NpgsqlDbType.TimestampTz });
    cmd.Parameters.Add(new NpgsqlParameter { Value = toUtc,   NpgsqlDbType = NpgsqlDbType.TimestampTz });
    await cmd.PrepareAsync();

    var count = (long)(await cmd.ExecuteScalarAsync())!;

    // Anti-pattern that silently scans every partition:
    //   "WHERE ordered_at::date = $1"   or   "WHERE date_trunc('day', ordered_at) = $1"
    ```

=== "Python"

    ```python
    # Python 3.12 + psycopg 3. psycopg prepares a query server-side once it has been
    # executed prepare_threshold times (default 5), or at once with prepare=True.
    # A prepared statement may then run a generic plan, which prunes at executor
    # startup instead of at planning time. Tz-aware datetimes bind as timestamptz.
    import datetime as dt
    import psycopg

    lo = dt.datetime(2026, 10, 1, tzinfo=dt.UTC)
    hi = dt.datetime(2026, 11, 1, tzinfo=dt.UTC)
    query = "SELECT count(*) FROM orders WHERE ordered_at >= %s AND ordered_at < %s"

    with psycopg.connect(conninfo) as conn:
        conn.execute("SET plan_cache_mode = force_generic_plan")   # make it visible at once
        for _ in range(3):
            conn.execute(query, (lo, hi), prepare=True)

        # PostgreSQL 14+: how often each prepared statement used a generic plan.
        for stmt, generic, custom in conn.execute(
            "SELECT statement, generic_plans, custom_plans FROM pg_prepared_statements"
        ):
            print(generic, custom, stmt)
    ```

=== "Azure"

    - **Azure SQL Database, Managed Instance and SQL Server** call the same optimisation *partition elimination*; it applies to partitioned tables and indexes when the predicate constrains the partitioning column, and the plan shows which partitions were accessed.
    - **Azure Database for PostgreSQL flexible server** behaves exactly as PostgreSQL above, including `Subplans Removed` for prepared statements that your connection pool or ORM keeps around.
    - **Microsoft Fabric and Azure Synapse** apply partition and file-level elimination to lake data; the exam-level idea is that filtering on the partition column reads fewer files.

=== "AWS"

    - **Amazon Athena** prunes S3 partitions (`dt=2026-10-24/` style prefixes) when the query filters on the partition column, and *partition projection* computes the partition list from a pattern so that pruning does not depend on catalog lookups; this is the main lever for cutting scanned bytes and cost.
    - **Amazon Redshift** keeps min/max *zone maps* per 1 MB block and sort keys so that range predicates skip blocks, the BRIN-like relative of pruning.
    - **Amazon RDS for PostgreSQL and Aurora PostgreSQL** are stock PostgreSQL for all of the above; the pruning rules and `EXPLAIN` output are identical.

## Misconceptions

- **"Pruning uses the indexes."** It uses only the declared partition bounds. A partitioned table with no indexes at all still prunes; a heavily indexed one with a function on the key does not.
- **"If `EXPLAIN` lists every partition, pruning failed."** Partitions that can only be ruled out during execution (by a subquery result or a nested-loop parameter) stay in the plan and are skipped at run time, which only `EXPLAIN (ANALYZE)` reveals as `(never executed)`; `EXPLAIN (GENERIC_PLAN)` also lists every partition because it has no parameter values. Check with `EXPLAIN (ANALYZE)` for `Subplans Removed` and `(never executed)`, or for `Chunks excluded during startup` and `during runtime` on a hypertable.
- **"`now()` prevents pruning."** `now()` is stable, so core PostgreSQL prunes it at executor startup rather than at planning time, which is still pruning. TimescaleDB goes further and constifies `now()` expressions at planning time.
- **"Pruned partitions cost nothing."** Partitions removed at executor initialisation are still locked, every partition contributes to planning time and session metadata, and a prepared statement's generic plan still contains them all. Fewer, well-chosen partitions beat many small ones.
- **"Partition pruning and constraint exclusion are the same setting."** `constraint_exclusion` serves inheritance-based partitioning and `UNION ALL` at planning time only; `enable_partition_pruning` serves declarative partitioning at planning and execution time.

## Exam notes

DP-300 tests partition elimination as part of SQL Server partitioning: expect a scenario where a query on a partitioned table does not benefit because the predicate does not use the partitioning column, or uses it inside a function. DEA-C01 tests the Athena version heavily: partition the data by the columns queries filter on, use partition projection, and avoid over-partitioning into tiny files; it also tests Redshift sort keys and zone maps as the way to skip blocks. SAA-C03 and SAP-C03 reach pruning only through cost questions ("reduce Athena scan costs": partition and convert to Parquet). DP-600 and DP-700 test file and partition elimination in Fabric lakehouses in the same spirit. The trap in every variant is a predicate that is semantically about the partition column but syntactically not comparable to the bounds, such as a cast, a function call or a join without a usable equality.

## Self-check

??? question "A table is partitioned by day on `event_time`, yet `SELECT count(*) FROM events WHERE event_time::date = current_date` scans every partition. Why, and how do you fix it?"
    The cast turns the predicate into a comparison on an expression, not on the partition key, so the planner cannot compare it with the partition bounds. Rewrite it as a half-open range on the bare column: `event_time >= current_date AND event_time < current_date + 1`. `current_date` is stable, so pruning happens at executor startup, which is fine.

??? question "After enabling prepared statements in Npgsql, `EXPLAIN (GENERIC_PLAN)` of the parameterised date-range query lists all 36 monthly partitions, but the query is still fast. What is going on?"
    With a generic plan the parameter values are unknown at planning time, so the plan contains every partition, and `GENERIC_PLAN` skips executor-startup pruning because it has no values to prune with. At run time PostgreSQL prunes at executor initialisation with the actual values; `EXPLAIN (ANALYZE) EXECUTE` of the prepared statement shows `Subplans Removed: 35` and only one partition is scanned. Nothing is wrong, though the plan still carries every partition's metadata, which is why thousands of partitions become a planning-cost problem.

??? question "A TimescaleDB dashboard query `WHERE time > now() - interval '15 minutes'` on a hypertable with 20,000 chunks took seconds to plan on an old version and milliseconds on a current one, with identical data. What changed?"
    On older versions `now()` was only excluded at executor startup, so the planner built a plan containing all 20,000 chunks before ChunkAppend discarded them. TimescaleDB 2.7 added `timescaledb.enable_now_constify`, which rewrites `now()`-relative predicates into constants at planning time so the chunks are excluded before the plan is built; the engineering post that introduced it measured such queries up to 401 times faster on 20,000 chunks.

## Further reading

- [High-Frequency Indexing & Partitioning](../data/time-series/high-frequency-indexing-partitioning.md) in this library
- [Row-Oriented vs. Columnar Storage](../data/time-series/row-vs-columnar-storage.md) in this library
- Term pages: [Table Partitioning](table-partitioning.md), [Hypertable (TimescaleDB)](hypertable.md), [BRIN index](brin-index.md), [B-Tree Index](b-tree-index.md), [Columnar Storage](columnar-storage.md)
- [Partition Pruning](https://www.postgresql.org/docs/current/ddl-partitioning.html) in the PostgreSQL documentation, including the `EXPLAIN` examples
- [enable_partition_pruning and constraint_exclusion](https://www.postgresql.org/docs/current/runtime-config-query.html), PostgreSQL documentation
- [TimescaleDB GUC reference](https://www.tigerdata.com/docs/reference/timescaledb/configuration/gucs) for the chunk-exclusion settings, and [enable_chunk_skipping()](https://www.tigerdata.com/docs/api/latest/hypertable/enable_chunk_skipping)
- [Implementing constraint exclusion for faster query performance](https://www.tigerdata.com/blog/implementing-constraint-exclusion-for-faster-query-performance) and [How we fixed long-running now() queries](https://www.tigerdata.com/blog/how-we-fixed-long-running-postgresql-now-queries), Tiger Data engineering posts
