---
title: "Choreography"
summary: "Two ways to coordinate a multi-step workflow across services."
acronyms: []
aliases: ["Event choreography"]
tracks: [architect]
domain: patterns
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Two ways to coordinate a multi-step workflow across services.
**Choreography**: each service reacts to events and emits its own — no
central coordinator, but the overall flow is implicit and harder to trace.
**Orchestration**: a central coordinator (e.g. a saga orchestrator) tells
each service what to do next — the flow is explicit, but the coordinator
becomes a single point of design complexity (and sometimes failure).

## Further reading

- [Event-Driven vs. Request-Response](../messaging/eventing/event-driven-vs-request-response.md)
