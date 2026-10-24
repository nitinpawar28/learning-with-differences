---
title: "Dead-Letter Queue (DLQ)"
summary: "A holding queue/stream for messages that repeatedly fail processing, so a single poison message can't block an entire consumer group."
acronyms: ["DLQ"]
aliases: []
tracks: [architect, cloud]
domain: messaging
cloud: neutral
level: practitioner
status: draft
---

## Explanation

A holding queue/stream for messages that repeatedly fail processing, so a
single poison message can't block an entire consumer group. Diverting to a
DLQ after N retries trades silent data loss for an explicit "needs a human"
signal.
