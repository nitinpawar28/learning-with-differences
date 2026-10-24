---
title: "Cold Observable"
summary: "A **cold** RxJS observable starts producing values only when subscribed, and each subscriber gets its own independent execution (e.g."
acronyms: []
aliases: []
tracks: [architect]
domain: frontend
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A **cold** RxJS observable starts producing values only when subscribed, and
each subscriber gets its own independent execution (e.g. an HTTP call
per subscription). A **hot** observable produces values regardless of
subscribers, who all share the same execution (e.g. a `WebSocket` message
stream, or a `Subject`) — subscribing late means missing what already fired.

## Further reading

- [RxJS & State Management](../frontend/angular/rxjs-state-management.md)
