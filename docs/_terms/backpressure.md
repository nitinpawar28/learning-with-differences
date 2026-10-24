---
title: "Backpressure"
summary: "What happens when a producer emits data faster than a consumer can process it."
acronyms: []
aliases: []
tracks: [architect]
domain: realtime
cloud: neutral
level: practitioner
status: draft
---

## Explanation

What happens when a producer emits data faster than a consumer can process
it. Handling strategies include buffering (bounded, with a drop policy),
sampling/throttling (`auditTime`, `throttleTime`), or blocking the producer
— the wrong choice under a market-data-style tick flood either OOMs the
client or drops the ticks you actually needed.

## Further reading

- [Real-Time UI Streaming](../frontend/realtime/real-time-ui-streaming.md)
