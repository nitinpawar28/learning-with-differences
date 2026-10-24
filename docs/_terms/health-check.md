---
title: "Health Check"
summary: "Two different questions an orchestrator asks a container."
acronyms: []
aliases: ["Health probe"]
tracks: [architect, cloud]
domain: sre
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Two different questions an orchestrator asks a container. **Liveness**: "is
this process stuck/deadlocked and should be restarted?" **Readiness**: "is
this instance currently able to serve traffic?" Conflating the two causes
either needless restarts (failing readiness treated as liveness) or traffic
sent to instances that aren't actually ready.
