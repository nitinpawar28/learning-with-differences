---
title: "Messaging and APIs"
description: "Backend runtime, APIs, real-time transport, eventing and service decomposition, compared option by option."
---

# Messaging & Eventing

*Backend & Asynchronous Messaging*

## Domain Overview & Architectural Context

Every service boundary in a high-throughput system eventually asks the same
question: does the caller wait for an answer, or does it hand off work and
move on? That question — request-response vs. event-driven — is the single
biggest architectural fork in this repository, because it determines
coupling, failure isolation, latency, and how hard it is to reason about
"what happened, in what order."

This category covers the backend runtime that implements services (.NET 9 /
C#, its async and threading model), the transports that connect them
(gRPC, REST, SignalR, WebSockets), and the eventing backbone that lets them
communicate without waiting on each other (Redis Streams, with Kafka as the
standing candidate). It also covers a newer entrant to this layer: MCP, which
brings the same request/response-vs-event, trust-boundary, and
delivery-guarantee questions to AI tool orchestration.

At the throughput and latency targets this stack is built for, the cost of
getting a messaging decision wrong isn't cosmetic — it shows up as duplicate
trades, out-of-order market data, or a service that silently stops
processing under load. This is the layer where [at-least-once vs.
exactly-once](../terms/at-least-once-delivery.md) stops being a
theoretical distinction and starts being a design decision with a dollar
value.

## Key Terminology & Concepts

The full definitions live in the [Master Glossary](../glossary/index.md); the ones
load-bearing for this category:

- [At-Least-Once vs. Exactly-Once](../terms/at-least-once-delivery.md) —
  the delivery guarantee a messaging system actually offers
- [Log Compaction](../terms/log-compaction.md) / [MAXLEN Trim](../terms/maxlen-trim.md) —
  how Kafka and Redis Streams each bound retention, and what falls out of
  each approach
- [Outbox Pattern](../terms/transactional-outbox.md) — atomically pairing a
  state change with the event that announces it
- [Idempotency Key](../terms/idempotency-key.md) — turning at-least-once
  delivery into effectively-once processing
- [Consumer Group](../terms/consumer-group.md) — sharing stream/topic
  consumption across instances without losing per-partition ordering
- [Choreography vs. Orchestration](../terms/choreography.md) —
  implicit event reactions vs. an explicit workflow coordinator

## Intended Knowledge Summary

By the time the articles in this folder are filled in, the reader should be
able to:

1. Decide, for a given service interaction, whether request-response or
   event-driven is the right shape — and defend that call under a failure
   scenario, not just the happy path.
2. Explain precisely what Redis Streams gives up relative to Kafka (log
   compaction, tiered storage, exactly-once transactions) and when that gap
   actually matters at our scale vs. when it's free optionality we're paying
   operational cost for.
3. Implement the outbox pattern correctly — including the part everyone
   skips, which is making the relay idempotent-safe on the consumer side.
4. Reason about MCP the same way as any other integration surface: what's
   the trust boundary, what's the delivery guarantee, what sandboxes the
   tool execution.
5. Know when microservice decomposition earns its coordination tax, and when
   a modular monolith is the more honest choice for the team's actual size.

## Planned Topic Matrix

| Topic | Current Stack | Candidate / Alternative | Key Trade-off | Article |
|---|---|---|---|---|
| Streaming backbone | Redis Streams | Kafka | Log compaction & tiered durability vs. operational simplicity | [Redis Streams vs. Kafka](eventing/redis-streams-vs-kafka.md) |
| Delivery guarantees | At-least-once + idempotent consumers | Transactional exactly-once | Throughput/coordination cost vs. correctness guarantee | [Delivery Semantics](eventing/delivery-semantics.md) |
| State + event consistency | Outbox pattern | Dual-write (DB then publish) | Atomicity vs. implementation simplicity | [Outbox Pattern](eventing/outbox-pattern.md) |
| Real-time push transport | SignalR (auto fallback) | Raw WebSockets | Operational convenience vs. protocol control | [SignalR & WebSockets](realtime/signalr-websockets.md) |
| Synchronous API protocol | REST/JSON | gRPC/Protobuf | Ecosystem ubiquity vs. throughput & streaming support | [REST vs. gRPC APIs](apis/rest-vs-grpc-apis.md) |
| Service coordination | Event-driven (async) | Request-response (sync) | Loose coupling & resilience vs. simplicity & immediate consistency | [Event-Driven vs. Request-Response](eventing/event-driven-vs-request-response.md) |
| AI tool orchestration | MCP servers | Bespoke REST/function-calling per tool | Standardized discovery & sandboxing vs. custom integration effort | [MCP Tool Orchestration](../ai/protocols/mcp-tool-orchestration.md) |
| External integrations | Broker/exchange REST + WebSocket feeds | FIX protocol | Implementation simplicity vs. institutional-grade guarantees | [Broker & Exchange API Integrations](integration/broker-exchange-api-integrations.md) |
| Service decomposition | Modular monolith | Microservices | Operational simplicity vs. independent deployability | [Microservices vs. Modular Monoliths](integration/microservices-vs-modular-monoliths.md) |
| Concurrency model | `async`/`await` + Task Parallel Library | Raw thread/thread-pool management | Developer ergonomics vs. low-level control | [Async & Threading](runtime/async-threading.md) |
| Runtime & language | .NET 9 / C# | — (runtime/language baseline) | Framework and language-version trade-offs underpinning every service | [.NET Core / C#](runtime/dotnet-core-csharp.md) |
