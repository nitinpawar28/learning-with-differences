---
title: "Server-Sent Events (SSE)"
summary: "A one-way, server-to-client push channel over a plain HTTP connection (`text/event-stream`), with automatic reconnect built into the browser's `EventSource` API."
acronyms: ["SSE"]
aliases: []
tracks: [architect]
domain: realtime
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A one-way, server-to-client push channel over a plain HTTP connection (`text/event-stream`),
with automatic reconnect built into the browser's `EventSource` API. Simpler
than WebSockets when the client never needs to push data back, at the cost
of no built-in binary framing and being one-directional by design.

## Further reading

- [SignalR & WebSockets](../messaging/realtime/signalr-websockets.md)
