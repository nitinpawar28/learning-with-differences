---
title: "Angular Change Detection"
summary: "How Angular decides a component's view is stale and needs re-rendering."
acronyms: []
aliases: ["Change detection"]
tracks: [architect]
domain: frontend
cloud: neutral
level: practitioner
status: draft
---

## Explanation

How Angular decides a component's view is stale and needs re-rendering.
The classic model patches async APIs via Zone.js and checks the whole
component tree on any event. Angular's Signals model tracks fine-grained
reactive dependencies instead, enabling zoneless change detection that only
re-renders what actually changed.

## Further reading

- [Angular](../frontend/angular/angular-fundamentals.md)
