---
title: Master Glossary
description: Central reference for the system design, architectural, and data engineering terms used throughout this repository.
---

# Master Glossary

A single place to look up the vocabulary used across every comparison article
in this repo. Terms are grouped by domain; where a term is the subject of a
deeper trade-off article, the definition links to it.

!!! tip "How to use this page"
    Definitions here are intentionally short — enough to unblock you mid-article
    without leaving the page. For the full trade-off analysis (when to use,
    performance implications, code), follow the **See:** link.

## Messaging & Eventing

### At-Least-Once vs. Exactly-Once

Delivery guarantees a messaging system offers a consumer. **At-most-once**
delivers zero or one time (fire-and-forget — messages can be lost).
**At-least-once** retries until acknowledged, so a message may be delivered
more than once (consumers must be idempotent). **Exactly-once** guarantees
each message is processed a single time, usually via transactional
producer/consumer coordination — it's expensive and rarely free of caveats,
which is why most systems settle for at-least-once plus an
[idempotency key](#idempotency-key).
*See: [Delivery Semantics](messaging/delivery-semantics.md), [Redis Streams vs. Kafka](messaging/redis-streams-vs-kafka.md).*

### Log Compaction

A retention strategy (native to Kafka) that keeps only the *latest* record
per key instead of deleting by age, so a topic can act as a compacted
changelog of current state rather than a pure event history. Redis Streams
has no native equivalent — retention there is time- or size-bounded via
[`MAXLEN` trim](#maxlen-trim).
*See: [Redis Streams vs. Kafka](messaging/redis-streams-vs-kafka.md).*

### MAXLEN Trim

Redis Streams' mechanism for bounding stream size: `XADD ... MAXLEN ~ 100000`
caps the stream at roughly N entries, evicting the oldest as new ones arrive.
It trims by count/approximate count, not by key like
[log compaction](#log-compaction) — two consumers reading the same offset can
diverge if one falls behind the trim horizon.
*See: [Redis Streams vs. Kafka](messaging/redis-streams-vs-kafka.md).*

### Outbox Pattern

A reliability pattern that writes a domain state change and the event
describing it in the *same local database transaction* (an "outbox" table),
then relays that event to the message broker asynchronously (via polling or
CDC). This avoids the dual-write problem, where writing to the database and
publishing to the broker as two separate operations can partially fail and
leave state and events inconsistent.
*See: [Outbox Pattern](messaging/outbox-pattern.md).*

### Consumer Group

A set of consumer instances that share the work of reading a stream/topic,
where each partition or message is delivered to only one member of the
group. Both Kafka and Redis Streams (`XREADGROUP`) implement this, letting
you scale consumption horizontally while preserving per-partition ordering.

### Idempotency Key

A unique identifier attached to an operation (a request or a message) so
that processing it more than once has the same effect as processing it once.
The standard way to convert an [at-least-once](#at-least-once-vs-exactly-once)
system into one that behaves like exactly-once from the consumer's
perspective.
*See: [Outbox Pattern](messaging/outbox-pattern.md), [Delivery Semantics](messaging/delivery-semantics.md).*

### Dead-Letter Queue (DLQ)

A holding queue/stream for messages that repeatedly fail processing, so a
single poison message can't block an entire consumer group. Diverting to a
DLQ after N retries trades silent data loss for an explicit "needs a human"
signal.

### Choreography vs. Orchestration

Two ways to coordinate a multi-step workflow across services.
**Choreography**: each service reacts to events and emits its own — no
central coordinator, but the overall flow is implicit and harder to trace.
**Orchestration**: a central coordinator (e.g. a saga orchestrator) tells
each service what to do next — the flow is explicit, but the coordinator
becomes a single point of design complexity (and sometimes failure).
*See: [Event-Driven vs. Request-Response](messaging/event-driven-vs-request-response.md).*

## Data & Storage Systems

### Row vs. Columnar Storage

Two ways to lay out a table on disk. **Row-oriented** storage keeps all
columns of a record contiguous — fast for point lookups and writing/reading
whole rows (OLTP). **Columnar** storage keeps each column contiguous across
rows — fast for scanning/aggregating a few columns across many rows (OLAP),
and compresses better since values in a column are more similar to each
other than values in a row.
*See: [Row vs. Columnar Storage](data/row-vs-columnar-storage.md).*

### Hypertable

TimescaleDB's abstraction over a Postgres table that automatically
partitions data into **chunks** (by time, and optionally by a space
dimension like a symbol/device ID) while still being queried as a single
logical table. It's what makes time-based partition pruning, retention
policies, and compression manageable at high ingest volume without you
hand-rolling partitioned tables.
*See: [High-Frequency Indexing & Partitioning](data/high-frequency-indexing-partitioning.md).*

### Write-Ahead Log (WAL)

A durability mechanism where every change is appended to a sequential log
*before* it's applied to the actual data files. On crash, the WAL is replayed
to recover uncommitted-to-disk changes. Postgres/TimescaleDB use it for
crash recovery and as the basis for streaming replication and CDC.

### MVCC (Multi-Version Concurrency Control)

A concurrency strategy where writers create new row versions instead of
overwriting in place, letting readers see a consistent snapshot without
blocking writers (and vice versa). Postgres implements isolation levels on
top of MVCC; it's why "Read Committed" in Postgres behaves differently than
lock-based isolation in other engines.
*See: [Relational Databases](data/relational-databases.md).*

### Partition Pruning

A query planner optimization where, given a filter on the partition key
(e.g. `time > now() - interval '1 day'`), the engine skips scanning
partitions/chunks it can prove don't contain matching rows — turning an
O(total data) scan into O(relevant partitions).
*See: [High-Frequency Indexing & Partitioning](data/high-frequency-indexing-partitioning.md).*

### BRIN Index

A Block Range Index: instead of indexing every row (like a B-tree), it
stores the min/max value per block range. Extremely small and cheap to
maintain, and effective specifically when data is naturally correlated with
insertion order — the common case for append-mostly time-series tables.
*See: [High-Frequency Indexing & Partitioning](data/high-frequency-indexing-partitioning.md).*

### Continuous Aggregate

A TimescaleDB materialized view that incrementally refreshes as new data
arrives, instead of recomputing from scratch. Used to pre-aggregate raw
ticks into OHLCV-style bars without re-scanning the full hypertable on every
query.
*See: [Time-Series / Financial Data Schemas](data/time-series-financial-schemas.md).*

### Retention Policy / Data Tiering

Automated rules for what happens to data as it ages: drop it, compress it,
or move it to cheaper storage (hot → warm → cold). TimescaleDB's retention
and compression policies operate per-chunk on a hypertable, which is why the
chunk boundary (time interval) is a real design decision, not an
implementation detail.

## Frontend & Real-Time

### Change Detection (Zone.js vs. Signals)

How Angular decides a component's view is stale and needs re-rendering.
The classic model patches async APIs via Zone.js and checks the whole
component tree on any event. Angular's Signals model tracks fine-grained
reactive dependencies instead, enabling zoneless change detection that only
re-renders what actually changed.
*See: [Angular](frontend/angular-fundamentals.md).*

### Backpressure

What happens when a producer emits data faster than a consumer can process
it. Handling strategies include buffering (bounded, with a drop policy),
sampling/throttling (`auditTime`, `throttleTime`), or blocking the producer
— the wrong choice under a market-data-style tick flood either OOMs the
client or drops the ticks you actually needed.
*See: [Real-Time UI Streaming](frontend/real-time-ui-streaming.md).*

### Optimistic UI Update

Updating the UI immediately on user action, before the server confirms it,
then reconciling (or rolling back) once the real response arrives. Makes an
app feel instant at the cost of having to define what "undo" looks like when
the optimistic guess was wrong.

### Hydration

Attaching client-side interactivity (event listeners, component state) to
HTML that was already rendered — either on the server (SSR) or from a cached
snapshot — instead of building the DOM from scratch on load.

### Virtual Scrolling / Windowing

Rendering only the DOM nodes currently visible in a scrollable list (plus a
small buffer), recycling nodes as the user scrolls, instead of rendering
every row up front. Necessary once a list is both large and fast-updating —
otherwise DOM node count becomes the bottleneck, not the data itself.
*See: [Real-Time UI Streaming](frontend/real-time-ui-streaming.md).*

### Cold vs. Hot Observable

A **cold** RxJS observable starts producing values only when subscribed, and
each subscriber gets its own independent execution (e.g. an HTTP call
per subscription). A **hot** observable produces values regardless of
subscribers, who all share the same execution (e.g. a `WebSocket` message
stream, or a `Subject`) — subscribing late means missing what already fired.
*See: [RxJS & State Management](frontend/rxjs-state-management.md).*

### Server-Sent Events (SSE)

A one-way, server-to-client push channel over a plain HTTP connection (`text/event-stream`),
with automatic reconnect built into the browser's `EventSource` API. Simpler
than WebSockets when the client never needs to push data back, at the cost
of no built-in binary framing and being one-directional by design.
*See: [SignalR & WebSockets](messaging/signalr-websockets.md).*

## Infrastructure & DevOps

### Immutable Infrastructure

Provisioning servers/containers as artifacts that are never patched in
place — a change means building and deploying a new image/instance, then
discarding the old one, rather than SSH-ing in and running `apt upgrade`.
Removes an entire class of "works on my server, drifted from every other
server" bugs.

### Blue-Green Deployment

Running two identical production environments ("blue" = live, "green" =
new version), then flipping traffic to green all at once after it's
verified healthy. Rollback is just flipping traffic back — fast, at the
cost of running two full environments simultaneously.
*See: [CI/CD Pipelines](devops/ci-cd-pipelines.md).*

### Canary Release

Rolling out a new version to a small percentage of traffic/users first,
watching error rates and latency, then gradually increasing the percentage
(or aborting) based on real production signal — trading deployment speed for
a much smaller blast radius on a bad release.
*See: [CI/CD Pipelines](devops/ci-cd-pipelines.md).*

### Sidecar Pattern

Deploying a helper process (proxy, log shipper, mTLS terminator) alongside
the main application container, sharing its network namespace — used
heavily by service meshes to add cross-cutting concerns (retries, mTLS,
metrics) without modifying application code.
*See: [mTLS vs. API Keys](security/mtls-vs-api-keys.md).*

### Health Check (Liveness vs. Readiness)

Two different questions an orchestrator asks a container. **Liveness**: "is
this process stuck/deadlocked and should be restarted?" **Readiness**: "is
this instance currently able to serve traffic?" Conflating the two causes
either needless restarts (failing readiness treated as liveness) or traffic
sent to instances that aren't actually ready.

### Infrastructure as Code (IaC)

Defining infrastructure (networks, VMs, containers, DNS) as versioned
declarative config (Terraform, Compose files, Ansible playbooks) instead of
manual console/CLI changes — giving infrastructure the same review, diff,
and rollback story as application code.
*See: [Docker & Containerization](devops/docker-containerization.md).*

### Horizontal vs. Vertical Scaling

**Horizontal** scaling adds more instances/nodes to share load (requires the
workload to be distributable/stateless-ish). **Vertical** scaling adds more
CPU/RAM/disk to a single instance (simpler, but bounded by the biggest box
you can buy, and a single point of failure).

## Security & Protocols

### mTLS (Mutual TLS)

TLS where *both* sides present and verify a certificate, not just the
server. Proves the identity of the calling service as well as the one being
called — the standard way to authenticate service-to-service traffic inside
a private network without relying on a shared secret.
*See: [mTLS vs. API Keys](security/mtls-vs-api-keys.md).*

### Workload Identity

An identity issued to a *running workload* (a pod, container, or process) by
the platform itself — typically as a short-lived, automatically-rotated
token — rather than a long-lived credential baked into config or an
environment variable. Removes an entire class of leaked-secret incidents by
removing the long-lived secret.
*See: [Workload Identity vs. Static Credentials](security/workload-identity.md).*

### Capability-Based AuthZ

An authorization model where holding an unforgeable reference (a
"capability" — e.g. a scoped, signed token naming exactly the resource and
action it permits) *is* the permission, as opposed to Role-Based Access
Control, where permission is looked up from an identity/role at each call.
Capabilities are attenuable (you can derive a narrower capability from a
broader one) and resist confused-deputy attacks by construction.
*See: [Capability-Based AuthZ vs. RBAC](security/capability-based-authz.md).*

### Wasm Sandboxing

Running untrusted code inside a WebAssembly runtime, which enforces memory
safety and a deny-by-default capability model (via WASI) at the language-VM
level rather than the OS-process level. Offers much faster cold starts and a
narrower escape surface than a container, at the cost of needing code that
targets a Wasm-compatible runtime.
*See: [Wasm Sandboxing vs. Container Isolation](security/wasm-sandboxing.md).*

### Zero Trust Architecture

A security model that assumes no implicit trust from network location alone
(no "inside the firewall = trusted") — every request is authenticated and
authorized regardless of where it originates. [mTLS](#mtls-mutual-tls) and
[workload identity](#workload-identity) are two of the building blocks used
to implement it.

### OAuth 2.0 Client Credentials Flow

The OAuth grant type for service-to-service auth with no end user in the
loop: a service authenticates directly with a client ID/secret (or a
signed JWT assertion) to obtain an access token. The usual choice for a
backend service calling another backend service or a third-party API.

### Least Privilege

The principle that any identity (user, service, or workload) should hold
only the permissions it needs to do its specific job, for only as long as it
needs them — the design target that [capability-based authz](#capability-based-authz)
and scoped [workload identity](#workload-identity) tokens are both aiming at.

### Secrets Rotation

Periodically or automatically replacing credentials (API keys, certificates,
database passwords) so that a leaked secret has a bounded useful lifetime.
[Workload identity](#workload-identity) is effectively rotation taken to its
limit — credentials so short-lived that manual rotation isn't a process
you need at all.
