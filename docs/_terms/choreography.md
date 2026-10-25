---
title: "Choreography"
summary: "A coordination style for multi-step workflows in which each service reacts to events and emits its own, so the end-to-end flow emerges from independent reactions rather than from a central coordinator that issues commands."
acronyms: []
aliases: ["Event choreography", "Choreography-based saga"]
formerly: []
tracks: [architect]
domain: patterns
cloud: neutral
level: practitioner
status: complete
last_verified: 2026-10-24
differs_from:
  - { term: orchestration, note: "Orchestration puts the workflow in one component that commands participants and holds the state; choreography spreads the workflow across participants that only see events." }
  - { term: transactional-outbox, note: "The outbox is a publishing mechanism that makes a state change and its event atomic; choreography is the coordination style that consumes those events, and it needs the outbox to be reliable." }
  - { term: dead-letter-queue, note: "A dead-letter queue parks an event that could not be processed; it is not a coordination strategy, and a choreographed flow still needs explicit compensating events that a DLQ never produces." }
related: [consumer-group, idempotency-key, at-least-once-delivery]
covers: []
sources:
  - { title: "Choreography pattern (Azure Architecture Center)", url: "https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography", publisher: Microsoft }
  - { title: "Saga design pattern (Azure Architecture Center)", url: "https://learn.microsoft.com/en-us/azure/architecture/patterns/saga", publisher: Microsoft }
  - { title: "Pattern: Saga (microservices.io)", url: "https://microservices.io/patterns/data/saga.html", publisher: Chris Richardson }
  - { title: "What Is Amazon EventBridge?", url: "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html", publisher: AWS }
---

## Explanation

Choreography is the way of running a business transaction across several services without anyone in charge. Each service subscribes to the events it cares about, does its own local work, commits to its own database, and publishes a new event describing what happened. No participant knows the whole flow; the flow is the sum of the subscriptions. The Azure Architecture Center defines it as letting each service decide when and how to process a business operation instead of depending on a central orchestrator, and the saga literature calls the same thing a *choreography-based saga*: a sequence of local transactions where each one triggers the next through an event, with compensating transactions published when a step fails.

Mechanically, choreography needs three things. First, a broker that buffers events until subscribers claim them, usually a publish/subscribe topic (Azure Service Bus topics and subscriptions, Amazon EventBridge rules and targets, SNS fan-out) or a log with [consumer groups](consumer-group.md) (Redis Streams, Kafka). Second, atomic publication: a service that writes to its database and then publishes can crash in between, so the event is written through a [transactional outbox](transactional-outbox.md) or change data capture rather than a second network call. Third, idempotent consumers, because brokers deliver [at least once](at-least-once-delivery.md) and retries produce duplicates; an [idempotency key](idempotency-key.md) such as the order id makes a redelivery harmless. Ordering is a per-flow decision: a Service Bus session id or a stream partition key keeps one order's events in sequence, and events can carry version numbers so consumers reject stale ones.

Failure handling is where choreography earns its reputation. Because nobody holds the transaction state, a failed step is announced as an event (`StockReservationFailed`) and the participants that already acted must subscribe to it and run their own compensation (`PaymentRefunded`). The compensation logic is itself distributed and itself fallible. The Azure guidance lists the resulting issues: complexity of failure handling, awkwardness when steps must run in sequence (a step that waits for two others must correlate two events), observability at scale (no single component has a complete view of an in-flight operation, so distributed tracing and correlation ids are mandatory), event schema evolution breaking downstream consumers, and emergent behaviour such as feedback loops and event storms when many services react to each other.

The benefits are the mirror image. There is no central component to become a bottleneck or a single point of failure, services can be added or replaced by changing subscriptions rather than rewiring a coordinator, and the style fits serverless and fire-and-forget operations where each component completes an atomic task and signals completion. The Azure guidance recommends it for loosely coupled communication across bounded contexts and parallel, independent operations, and recommends considering an orchestrator inside a single bounded context or when a complex flow needs shared logic. The saga guidance adds a sharp drawback: integration testing is hard because every participant must run to simulate one transaction.

In the reader's stack, choreography is the natural shape of a Redis Streams design: the order service appends `OrderPlaced` to a stream, the inventory and payment services each read it through their own consumer group, and each appends its outcome to its own stream, with `XACK` after the local transaction and the outbox write. Docker Compose makes the testing drawback concrete: the whole compose file must be up to exercise one order. The [event-driven vs. request-response](../messaging/eventing/event-driven-vs-request-response.md) article covers the broader choice this style belongs to, and [orchestration](orchestration.md) is the alternative to compare against before committing.

```mermaid
sequenceDiagram
    participant C as Client
    participant O as Order service
    participant B as Broker (stream or topic)
    participant P as Payment service
    participant I as Inventory service
    C->>O: POST /orders
    O->>B: OrderPlaced(orderId)
    B-->>P: OrderPlaced
    B-->>I: OrderPlaced
    P->>B: PaymentCaptured(orderId)
    I->>B: StockReservationFailed(orderId)
    B-->>O: PaymentCaptured, StockReservationFailed
    B-->>P: StockReservationFailed
    P->>B: PaymentRefunded(orderId)
    O->>O: mark order Rejected
    Note over O,I: nobody holds the flow; every participant encodes its own reactions and compensations
```

## How it differs

| Aspect | Choreography | [Orchestration](orchestration.md) | [Transactional outbox](transactional-outbox.md) | [Dead-letter queue](dead-letter-queue.md) |
| --- | --- | --- | --- | --- |
| What it is | coordination style | coordination style | publishing mechanism | failure parking mechanism |
| Who knows the flow | nobody; it is implicit | the orchestrator | n/a | n/a |
| Failure handling | compensating events per participant | compensations driven centrally | none; guarantees the event is sent | isolates the poison message |
| Coupling | to event contracts | to the orchestrator's commands | to the local database | to the broker feature |

**Versus orchestration.** Both coordinate a saga; the question is where the knowledge lives. In orchestration a coordinator sends `ReserveStock` and `CapturePayment` commands, waits for replies, keeps the state and runs compensations in order; participants are simple and the flow is readable in one place. In choreography the same steps are reactions to events, so the flow is only visible by reading every subscriber. The saga guidance summarises the trade: choreography suits simple flows with few participants and no central coordination logic, avoids an extra service and a single point of failure, but gets confusing as steps are added, risks cyclic dependencies and is hard to integration-test; orchestration suits complex flows and growing numbers of services, avoids cycles and keeps participant logic clean, at the cost of implementing and operating the coordinator.

**Versus the transactional outbox.** They are different layers. The outbox makes "update my rows and publish my event" atomic by writing the event into the same database transaction and letting a relay publish it. Choreography is what happens after publication. A choreographed system without an outbox loses or duplicates events at every crash boundary; an orchestrated system needs the outbox just as much for its replies.

**Versus a dead-letter queue.** A DLQ is where the broker or the consumer parks an event that cannot be processed after retries. It stops a poison message from blocking the stream and gives operators something to inspect, but it does not undo the steps that already happened. The Azure example uses dead-lettering for unprocessable messages and a separate remediation service that runs compensation or retry, which is the point: the DLQ is a holding area, the compensation is still your code.

## Examples

Inventory reacts to `OrderPlaced` and announces the outcome; payment reacts to the inventory outcome. No service calls another directly.

=== "C#"

    ```csharp
    // Inventory service: reacts to OrderPlaced, emits StockReserved or StockReservationFailed.
    using System.Text.Json;
    using StackExchange.Redis;

    var db = (await ConnectionMultiplexer.ConnectAsync("redis:6379")).GetDatabase();
    const string inbox = "events:orders", group = "inventory", consumer = "inventory-1";

    try { await db.StreamCreateConsumerGroupAsync(inbox, group, StreamPosition.NewMessages); }
    catch (RedisServerException e) when (e.Message.StartsWith("BUSYGROUP")) { /* group already exists */ }

    while (true)
    {
        // StackExchange.Redis has no blocking reads, so poll with a short delay when idle.
        var entries = await db.StreamReadGroupAsync(inbox, group, consumer, StreamPosition.NewMessages, count: 10);
        foreach (var entry in entries)
        {
            var evt = JsonSerializer.Deserialize<OrderPlaced>(entry["payload"].ToString())!;
            bool reserved = await TryReserveAsync(evt);   // idempotent on evt.OrderId: a redelivery must not reserve twice

            await db.StreamAddAsync("events:inventory", [
                new NameValueEntry("type", reserved ? "StockReserved" : "StockReservationFailed"),
                new NameValueEntry("payload", JsonSerializer.Serialize(new { evt.OrderId })),
            ], maxLength: 1_000_000, useApproximateMaxLength: true);

            await db.StreamAcknowledgeAsync(inbox, group, entry.Id);   // only after the local work and the outgoing event
        }
        if (entries.Length == 0) await Task.Delay(200);
    }

    static Task<bool> TryReserveAsync(OrderPlaced evt) => Task.FromResult(true);   // local transaction goes here

    record OrderPlaced(string OrderId, string Sku, int Quantity);
    ```

=== "Python"

    ```python
    import json
    import redis

    r = redis.Redis(host="redis", port=6379, decode_responses=True)
    INBOX, GROUP, CONSUMER = "events:orders", "inventory", "inventory-1"

    try:
        r.xgroup_create(INBOX, GROUP, id="$", mkstream=True)
    except redis.ResponseError as e:
        if "BUSYGROUP" not in str(e):
            raise

    def try_reserve(order_id: str, sku: str, qty: int) -> bool:
        return True  # local transaction, idempotent on order_id

    while True:
        # Blocking read: returns [] after 5 s with nothing new, so the loop just spins again.
        for _stream, entries in r.xreadgroup(GROUP, CONSUMER, {INBOX: ">"}, count=10, block=5000):
            for entry_id, fields in entries:
                evt = json.loads(fields["payload"])
                ok = try_reserve(evt["orderId"], evt["sku"], evt["quantity"])
                r.xadd("events:inventory", {
                    "type": "StockReserved" if ok else "StockReservationFailed",
                    "payload": json.dumps({"orderId": evt["orderId"]}),
                }, maxlen=1_000_000)  # approximate by default
                r.xack(INBOX, GROUP, entry_id)
    ```

=== "Azure"

    The Architecture Center's reference implementation runs the package, drone-scheduler and delivery services on Azure Container Apps with Azure Service Bus as the bus: an ingestion function publishes to a topic, two services subscribe, and a session-aware queue carries their results so the delivery service can correlate the two messages it needs per transaction by session id. Unprocessable messages are dead-lettered with a reason code and remediated separately, and the final state change is published to Azure Event Grid for consumers outside the workload. Service Bus is chosen for high-value messages that must not be lost or duplicated; Event Grid for fire-and-forget notifications.

=== "AWS"

    Amazon EventBridge is the usual bus: producers put events on a custom event bus, rules match event patterns and deliver to targets such as Lambda functions, SQS queues or Step Functions, and EventBridge Pipes handle point-to-point cases such as a DynamoDB stream feeding the bus. SNS topics fanning out to one SQS queue per subscriber give the same shape with queue-level retries and dead-letter queues. Either way the participants never address each other; the rule or subscription is the only coupling.

## Misconceptions

- **"Choreography means no coordination logic."** The logic is still there; it is sliced across every participant's subscriptions and compensations. What disappears is the single place to read it, which is why distributed tracing and correlation ids are non-negotiable.
- **"There is no single point of failure."** There is no single *application* component, but the broker is shared infrastructure, and emergent behaviour (feedback loops, event storms) can take the whole system down without any one service failing.
- **"Events are delivered exactly once, so handlers can be simple."** Delivery is at least once; retries and concurrent consumers produce duplicates and reordering. Handlers must be idempotent and ordering must be designed with sessions, partition keys or version checks.
- **"It scales better than orchestration in every case."** It removes a bottleneck for independent, parallel operations. Sequential dependencies (D after B and C) need correlation logic in the participants and quickly become harder to follow than an orchestrator.
- **"Each service can be tested on its own, so the system is tested."** Unit tests cover reactions; the saga only exists when every participant runs, which is exactly why the saga guidance flags integration testing as the hard part.

## Exam notes

AWS Certified Developer – Associate (DVA-C03) names choreography and orchestration explicitly among the architectural patterns a developer must describe, alongside event-driven, microservices and fan-out, and asks you to tell synchronous from asynchronous designs and to implement event-driven patterns with EventBridge; the classic trap is a scenario that lists sequential steps with compensation and tempts you to answer "EventBridge" when Step Functions is the intended orchestrator, or the reverse for independent fan-out. AWS Certified Solutions Architect – Associate (SAA-C03) and Professional (SAP-C03) cover event-driven architectures, decoupling with SQS, SNS and EventBridge, and workflow orchestration with Step Functions, so expect to justify the choice by coupling and failure handling. Designing Microsoft Azure Infrastructure Solutions (AZ-305) asks for messaging and event-driven architecture recommendations, where Service Bus topics with sessions versus Event Grid is the usual discriminator; Developing AI Cloud Solutions on Azure (AI-200) tests Service Bus topics, subscriptions and dead-letter handling and Event Grid retries at the implementation level. AWS Certified DevOps Engineer – Professional (DOP-C02) treats the same material as event processing workflows. In every exam, pair choreography with at-least-once delivery, idempotent consumers and compensation; an answer that assumes rollback across services is wrong.

## Self-check

??? question "An order flow has five steps that must run in sequence, each with compensation, and the team expects to add two more steps next quarter. Choreography or orchestration?"
    Orchestration. The saga guidance recommends choreography for simple flows with few participants and no coordination logic, and warns that adding steps makes a choreographed flow confusing and risks cyclic dependencies. A strictly sequential, growing flow with compensation is the orchestrator's case: the flow is readable in one place, compensations run in a known order, and participants stay simple.

??? question "A choreographed system occasionally charges a customer twice when the payment service pod restarts mid-batch. Which design element is missing?"
    Idempotent consumers keyed by the event or order id. The broker delivers at least once, so after a restart the unacknowledged OrderPlaced events are redelivered and the handler captures payment again. Record the processed order ids (or use the payment provider's idempotency key) before acknowledging, and acknowledge only after the local transaction and the outgoing event are durable.

??? question "Operators cannot tell which orders are stuck because no service knows the end-to-end state. What should the architecture add without switching to an orchestrator?"
    A correlation id carried on every event plus distributed tracing, so one trace shows the hops; and a read-only projection service that subscribes to all the flow's events and materialises per-order status for dashboards and alerts. That keeps coordination decentralised while giving operators the view an orchestrator would otherwise provide.

## Further reading

- [Event-driven vs. request-response](../messaging/eventing/event-driven-vs-request-response.md), [the outbox pattern](../messaging/eventing/outbox-pattern.md) and [delivery semantics](../messaging/eventing/delivery-semantics.md).
- [Microservices vs. modular monoliths](../messaging/integration/microservices-vs-modular-monoliths.md) for when a single process makes choreography unnecessary.
- [Orchestration](orchestration.md), [transactional outbox](transactional-outbox.md), [dead-letter queue](dead-letter-queue.md), [consumer group](consumer-group.md) and [idempotency key](idempotency-key.md).
- Azure Architecture Center, Choreography pattern: <https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography>
- Saga pattern: <https://microservices.io/patterns/data/saga.html>
