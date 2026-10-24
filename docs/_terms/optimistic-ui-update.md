---
title: "Optimistic UI Update"
summary: "Updating the UI immediately on user action, before the server confirms it, then reconciling (or rolling back) once the real response arrives."
acronyms: []
aliases: ["Optimistic update"]
tracks: [architect]
domain: frontend
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Updating the UI immediately on user action, before the server confirms it,
then reconciling (or rolling back) once the real response arrives. Makes an
app feel instant at the cost of having to define what "undo" looks like when
the optimistic guess was wrong.
