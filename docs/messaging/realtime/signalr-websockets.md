---
title: "SignalR vs. Raw WebSockets"
description: Real-time transport choices, fallback behavior, and scaling trade-offs.
tags:
  - messaging
  - real-time
  - websockets
status: stub
level: practitioner
tracks: [architect]
---

# SignalR & WebSockets

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- SignalR (with automatic transport fallback) vs. raw `WebSocket`
- SignalR Hubs vs. plain WebSocket message routing
- Scaling out: SignalR backplane (Redis/Azure SignalR Service) vs. sticky sessions
- Server-Sent Events (SSE) vs. WebSockets vs. long polling
- Message framing and protocol choice: JSON vs. MessagePack
