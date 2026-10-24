---
title: "Virtual Scrolling"
summary: "Rendering only the DOM nodes currently visible in a scrollable list (plus a small buffer), recycling nodes as the user scrolls, instead of rendering every row up front."
acronyms: []
aliases: ["Windowing", "List virtualization"]
tracks: [architect]
domain: frontend
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Rendering only the DOM nodes currently visible in a scrollable list (plus a
small buffer), recycling nodes as the user scrolls, instead of rendering
every row up front. Necessary once a list is both large and fast-updating —
otherwise DOM node count becomes the bottleneck, not the data itself.

## Further reading

- [Real-Time UI Streaming](../frontend/realtime/real-time-ui-streaming.md)
