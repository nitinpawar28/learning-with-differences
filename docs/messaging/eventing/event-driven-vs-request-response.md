---
title: "Event-Driven vs. Request-Response Architecture"
description: Communication pattern trade-offs for service-to-service interaction.
tags:
  - messaging
  - event-driven
status: stub
level: practitioner
tracks: [architect]
---

# Event-Driven vs. Request-Response

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- Synchronous request-response (REST/gRPC) vs. asynchronous event/message-driven flows
- Choreography vs. orchestration for multi-step workflows
- Coupling and failure isolation: a slow downstream service in each model
- Eventual consistency (event-driven) vs. immediate consistency (request-response)
- Event sourcing vs. CRUD-with-events-on-the-side
