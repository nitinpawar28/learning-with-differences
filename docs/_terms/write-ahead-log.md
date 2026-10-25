---
title: "Write-Ahead Log (WAL)"
summary: "The append-only log a database flushes before it touches its data files, so that a commit is durable after one sequential write and crash recovery, replication, point-in-time restore and change data capture can all replay from it."
acronyms: [WAL]
aliases: ["Write-ahead logging", "Transaction log", "Redo log"]
formerly: []
tracks: [architect, cloud]
domain: databases
cloud: neutral
level: practitioner
status: complete
last_verified: 2026-10-24
differs_from:
  - { term: mvcc, note: "The WAL is a physical redo record for durability and recovery; MVCC keeps multiple logical row versions for isolation, and the WAL records the creation of those versions without ever being consulted by a running query." }
  - { term: change-data-capture, note: "CDC is a consumer of the WAL: logical decoding turns physical log records into row-level change events through a replication slot, so CDC depends on the WAL but the WAL exists without CDC." }
  - { term: transactional-outbox, note: "The outbox is an application table written in the same transaction as the business data and polled later; the WAL is the engine's own log, and reading it with logical decoding is the alternative that makes an outbox table unnecessary." }
  - { term: log-compaction, note: "A compacted Kafka topic keeps the latest record per key and is the data itself; a WAL keeps every change in order and is recycled once a checkpoint makes the data files self-sufficient." }
related: [at-least-once-delivery, idempotency-key, row-oriented-storage]
covers: []
sources:
  - { title: "Reliability and the Write-Ahead Log (PostgreSQL 18 documentation)", url: "https://www.postgresql.org/docs/current/wal-intro.html", publisher: PostgreSQL Global Development Group }
  - { title: "WAL Internals (PostgreSQL 18 documentation)", url: "https://www.postgresql.org/docs/current/wal-internals.html", publisher: PostgreSQL Global Development Group }
  - { title: "WAL Configuration (PostgreSQL 18 documentation)", url: "https://www.postgresql.org/docs/current/wal-configuration.html", publisher: PostgreSQL Global Development Group }
  - { title: "Logical Decoding Concepts (PostgreSQL 18 documentation)", url: "https://www.postgresql.org/docs/current/logicaldecoding-explanation.html", publisher: PostgreSQL Global Development Group }
  - { title: "ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging (ACM TODS 17(1), 1992)", url: "https://dl.acm.org/doi/10.1145/128765.128770", publisher: ACM }
---

## Explanation

A write-ahead log is the append-only file a database writes *first*. The rule that defines it: a change to a data file (a table or index page) may reach disk only after the log records describing that change have been flushed to permanent storage.

Mechanically, in PostgreSQL, a backend modifies a page in shared memory and calls `XLogInsertRecord` to put a record describing the change into the WAL buffers; the page is marked dirty and stays in memory. At `COMMIT` the backend calls `XLogFlush`, which writes the WAL buffers up to the commit record and syncs them to disk; only then does the client hear "commit OK". Dirty data pages are written much later. A *checkpoint* flushes every dirty page and writes a checkpoint record; one begins every `checkpoint_timeout` (default five minutes) or when `max_wal_size` (default 1 GB) is about to be exceeded. After a crash the server *redoes* every WAL record since the last checkpoint, reconstructing changes that never reached the data files. Because the first write to a page after a checkpoint could be torn by a power failure, `full_page_writes` (default on) logs the whole page image at that moment, which is why frequent checkpoints inflate WAL volume. The payoff: a commit costs one sequential write plus one `fsync` of the log instead of random writes to every data file touched, and one `fsync` can commit many concurrent transactions (group commit).

Physical facts: WAL lives in `pg_wal` as 16 MB segment files of 8 kB pages; positions are *log sequence numbers* (LSNs), a monotonically increasing byte offset exposed as the `pg_lsn` type, and every data page records the LSN of the last record that changed it. `wal_level` decides how much is logged: `minimal` (crash recovery only), `replica` (the default, enough for archiving and streaming replication) or `logical` (adds what logical decoding needs). `synchronous_commit = off` returns before the flush, so a crash within at most three times `wal_writer_delay` loses the transaction but corrupts nothing.

The theory is ARIES (Mohan and colleagues, 1992): repeat history during redo, keep an LSN on every page so a record is applied at most once, and log compensation records during undo so recovery is itself restartable. SQL Server's transaction log is explicitly a write-ahead log with LSNs, virtual log files and truncation after a checkpoint or log backup. Redis's append-only file is a cousin: it appends commands after executing them and fsyncs every second by default.

Because the WAL is a complete, ordered record of every change, it became the backbone of three more features. *Streaming replication* ships WAL to standbys, which replay it. *Point-in-time recovery* archives WAL so a base backup plus replay reaches any instant. *Logical decoding* reads the WAL through a *replication slot* and an output plugin such as `pgoutput` to emit row-level change events, which is how Debezium-style [change data capture](change-data-capture.md) works. A slot guarantees that the WAL and catalog rows it still needs are retained, but an abandoned slot therefore pins WAL forever, fills the disk and stops `VACUUM` from freezing. A slot emits each change once in normal operation but may resend after a crash, so consumers must be idempotent.

In the reader's stack the WAL is what makes a .NET `SaveChangesAsync` durable, what the [transactional outbox](transactional-outbox.md) relies on, and what a CDC pipeline reads. Amazon Aurora takes the idea to its conclusion: the engine sends only log records to the storage service, which materialises pages from the log.

```mermaid
sequenceDiagram
    participant C as Client
    participant B as Backend
    participant W as WAL (pg_wal)
    participant D as Data files
    C->>B: UPDATE ...; COMMIT
    B->>B: change page in shared buffers, XLogInsertRecord
    B->>W: XLogFlush: write + fsync up to the commit LSN
    W-->>B: durable
    B-->>C: COMMIT OK
    Note over D: dirty page still only in memory
    B->>D: checkpointer writes dirty pages later
    Note over W,D: after a crash: REDO replays WAL from the last checkpoint into the data files
```

## How it differs

**[MVCC](mvcc.md)** and the WAL are both "the database keeps old things around", which invites confusion, but they answer different questions. MVCC keeps multiple *logical* versions of a row in the heap so concurrent transactions see consistent snapshots; the WAL keeps a *physical* record of every page change so the database survives a crash. A running query never reads the WAL, and vacuum never reads it either. They meet only in that every new row version, every `xmax` stamp and every vacuum cleanup is itself WAL-logged.

**[Change data capture](change-data-capture.md)** is the most useful *consumer* of the WAL. Logical decoding converts physical records into "row inserted, row updated (old and new values per the table's replica identity), row deleted" events, in commit order, delivered through a replication slot. CDC therefore inherits the WAL's guarantees (complete, ordered, transactional) and its operational hazards (slots retain WAL; `wal_level = logical` increases volume). Choose log-based CDC over triggers or polling when you need every change with low overhead on the source.

**[Transactional outbox](transactional-outbox.md)** solves "publish an event when the transaction commits" at the application layer: write the event into an outbox table in the same transaction and let a relay publish it. The WAL plus logical decoding solves the same problem at the engine layer and removes the extra table, the polling and the ordering puzzles of sequence gaps. The outbox keeps you independent of database privileges and of a CDC platform; log-based capture keeps the schema and the application untouched. Teams often combine them: an outbox table whose rows are shipped by CDC.

**[Log compaction](log-compaction.md)** in Kafka retains the latest record per key and discards older ones, because the topic *is* the data (a changelog or state store). A WAL must never discard a record that a checkpoint has not yet made redundant, and conversely it has no reason to keep history once the data files are up to date, so segments are recycled rather than compacted. The two are opposite retention policies for logs that serve opposite purposes.

| | WAL | MVCC versions | CDC stream | Outbox table | Compacted topic |
|---|---|---|---|---|---|
| Content | Physical page changes | Row versions in the heap | Logical row events | Application events | Latest value per key |
| Reader | Recovery, replication, decoding | Queries via snapshots | External consumers | Relay process | Consumers |
| Retention | Until checkpoint/archive/slot allows | Until vacuum | Slot position | Until published | Forever, one per key |

## Examples

=== "SQL"

    ```sql
    SHOW wal_level;                                 -- replica by default; logical for CDC
    SELECT pg_current_wal_lsn(), pg_walfile_name(pg_current_wal_lsn());

    -- How much WAL is each replication slot holding back?
    SELECT slot_name, plugin, active, wal_status,
           pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) AS retained
    FROM pg_replication_slots;

    -- Logical decoding through SQL (requires wal_level = logical).
    SELECT pg_create_logical_replication_slot('audit_slot', 'test_decoding');
    INSERT INTO orders (ordered_at, customer, total) VALUES (now(), 'acme', 99.50);
    SELECT lsn, data FROM pg_logical_slot_peek_changes('audit_slot', NULL, NULL);
    SELECT pg_drop_replication_slot('audit_slot');  -- never leave an unused slot behind

    -- How much WAL does a statement generate?
    EXPLAIN (ANALYZE, WAL) UPDATE orders SET total = total * 1.1 WHERE customer = 'acme';
    ```

=== "C#"

    ```csharp
    // .NET 9 + Npgsql (Npgsql.Replication, Npgsql.Replication.PgOutput namespaces).
    // Prerequisites: wal_level = logical, a role with REPLICATION, and
    //   CREATE PUBLICATION orders_pub FOR TABLE orders;
    await using var conn = new LogicalReplicationConnection(connectionString);
    await conn.Open();

    // Create once; afterwards reuse with new PgOutputReplicationSlot("orders_slot").
    var slot = await conn.CreatePgOutputReplicationSlot("orders_slot");

    await foreach (var message in conn.StartReplication(
                       slot, new PgOutputReplicationOptions("orders_pub", 1), ct))
    {
        if (message is InsertMessage insert)
        {
            await foreach (var value in insert.NewRow)
                Console.Write($"{await value.Get<string>()} ");
            Console.WriteLine();
        }

        // Acknowledge, or the slot pins this WAL forever.
        conn.SetReplicationStatus(message.WalEnd);
    }
    ```

=== "Python"

    ```python
    # Python 3.12 + psycopg 3: poll a logical slot through the SQL interface with
    # the wal2json output plugin. get_changes consumes; peek_changes does not.
    import psycopg

    with psycopg.connect(conninfo, autocommit=True) as conn:
        conn.execute(
            "SELECT pg_create_logical_replication_slot('orders_json', 'wal2json')"
        )
        try:
            for lsn, xid, data in conn.execute(
                "SELECT lsn, xid, data FROM pg_logical_slot_get_changes("
                "  'orders_json', NULL, NULL, 'format-version', '2')"
            ):
                print(lsn, xid, data)    # one JSON document per change
        finally:
            conn.execute("SELECT pg_drop_replication_slot('orders_json')")
    ```

=== "Azure"

    - **Azure Database for PostgreSQL flexible server**: set the `wal_level` server parameter to `logical` and restart, grant `ALTER ROLE ... WITH REPLICATION` to the consuming role, then use `pgoutput`, `wal2json`, `test_decoding` or the `pglogical` extension. The service documents the operational trap: unconsumed slots pile up WAL and raise wraparound risk, the server goes read-only at 95 percent storage, and it will drop an unused slot itself when storage runs critically low. On PostgreSQL 17 and later, slot synchronisation (`sync_replication_slots`, `hot_standby_feedback`) preserves logical slots across high-availability failover; earlier versions need the `pg_failover_slots` module.
    - **Azure SQL Database and SQL Server**: the transaction log is the WAL; log records must be on disk before the dirty page is flushed, checkpoints and log backups drive truncation, and automatic backups plus log backups give point-in-time restore.

=== "AWS"

    - **Amazon RDS for PostgreSQL and Aurora PostgreSQL**: `wal_level` is not edited directly; the `rds.logical_replication` parameter in the parameter group turns logical decoding on, and the `rds_replication` role grants slot access. Aurora keeps the WAL records in Aurora storage, decodes with `pgoutput` by default and also supports `wal2json`, and adds a write-through cache for logical replication.
    - **Amazon Aurora storage**: the engine sends only log records to the storage nodes, a write is durable when four of six nodes acknowledge, and the storage tier coalesces log records into data pages; the log-shipping design is why Aurora replicas and crash recovery do not replay WAL at the engine.
    - **AWS DMS** and similar CDC services read PostgreSQL sources through logical replication slots, with the same retention hazard if a task is paused.

## Misconceptions

- **"At commit, my data is on disk."** Only the WAL records are. The data pages may stay dirty in memory until the next checkpoint; durability comes from being able to redo them, not from having written them.
- **"The WAL is a backup."** It is a redo stream. Only a base backup plus an archived WAL sequence gives point-in-time recovery; the WAL alone describes changes to pages it does not contain.
- **"`synchronous_commit = off` can corrupt the database."** It can lose the last few transactions after a crash but leaves the database consistent, because the WAL is still written in order. `fsync = off` is the setting that risks corruption.
- **"A replication slot is free until someone reads it."** A slot retains every WAL segment and catalog row its consumer has not confirmed, whether or not anyone is connected. Abandoned slots are a leading cause of full disks and forced wraparound vacuums.
- **"Logical decoding gives me exactly-once events."** A slot normally emits each change once, but its position is persisted only at checkpoints, so after a server crash recent changes can be resent. Consumers must deduplicate or be idempotent.

## Exam notes

DP-300 tests the SQL Server transaction log directly: recovery models, log backups and truncation, `log_reuse_wait_desc`, checkpoints, VLF sprawl and why a full log stops writes; DP-900 wants the ACID durability concept. AZ-305 and SAA-C03 approach the WAL through recovery objectives: point-in-time restore windows, synchronous versus asynchronous replication and the RPO each implies. DEA-C01 and DP-700 test CDC: that log-based capture (AWS DMS from PostgreSQL, Debezium) reads the database log through logical replication, needs `wal_level = logical` or its managed-service switch, and must keep consumers running so the log does not accumulate. SAP-C03 may describe Aurora's log-only storage path and ask what it implies for replica lag or crash recovery. The classic trap is confusing the WAL with a backup, or `synchronous_commit` with `fsync`.

## Self-check

??? question "A Debezium connector was paused for a week during a migration and the PostgreSQL volume is now 95 percent full although the tables did not grow. What happened and what do you do?"
    The connector's replication slot kept every WAL segment since it last acknowledged, so `pg_wal` grew by a week of changes. Check `pg_replication_slots` for the inactive slot and the retained size, resume the consumer so it acknowledges and the WAL recycles, or drop the slot and re-snapshot. Add monitoring on slot lag and, on managed services, note that the platform may drop the slot itself before the disk fills.

??? question "An order service reports success to the user as soon as `COMMIT` returns, with `synchronous_commit = off` for throughput. The server loses power. Which orders are at risk and is the database consistent afterwards?"
    Transactions committed within the last few hundred milliseconds (up to three times `wal_writer_delay`) may be lost because their WAL records were not yet flushed; everything older is durable. The database is consistent after recovery because the WAL is still applied in order; only `fsync = off` risks corruption. If a lost order is unacceptable, keep `synchronous_commit` on for that transaction, which can be set per session or per transaction.

??? question "Why does the WAL grow sharply right after every checkpoint, and what setting is responsible?"
    `full_page_writes` logs the entire page the first time it is modified after a checkpoint so that a torn page can be rebuilt from the image. Shorter checkpoint intervals mean more first-touches and therefore more full-page images; raising `checkpoint_timeout` and `max_wal_size`, or enabling `wal_compression`, reduces the volume at the cost of longer crash recovery.

## Further reading

- [The Outbox Pattern](../messaging/eventing/outbox-pattern.md) in this library, the application-level alternative to log-based capture
- [Delivery Semantics](../messaging/eventing/delivery-semantics.md) in this library, for why slot consumers must be idempotent
- [Relational Databases](../data/relational/relational-databases.md) in this library
- Term pages: [MVCC](mvcc.md), [Change data capture](change-data-capture.md), [Transactional outbox](transactional-outbox.md), [Log compaction](log-compaction.md), [Row-Oriented Storage](row-oriented-storage.md)
- [Reliability and the Write-Ahead Log](https://www.postgresql.org/docs/current/wal-intro.html), [WAL Internals](https://www.postgresql.org/docs/current/wal-internals.html), [WAL Configuration](https://www.postgresql.org/docs/current/wal-configuration.html) and [Logical Decoding Concepts](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html), PostgreSQL documentation
- [ARIES (ACM TODS, 1992)](https://dl.acm.org/doi/10.1145/128765.128770), the recovery algorithm behind most write-ahead logs
- [SQL Server transaction log architecture and management guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-log-architecture-and-management-guide), Microsoft Learn
- [Npgsql replication](https://www.npgsql.org/doc/replication.html), the API used in the C# example
