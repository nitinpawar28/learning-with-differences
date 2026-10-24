---
title: "Broker & Exchange API Integrations"
description: Trade-offs when integrating with external trading and market-data APIs.
tags:
  - messaging
  - integrations
  - finance
status: stub
level: practitioner
tracks: [architect]
---

# Broker & Exchange API Integrations

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- REST polling vs. WebSocket/FIX push feeds for market data
- FIX protocol vs. vendor REST/WebSocket APIs
- Rate-limit-aware polling vs. persistent streaming connections
- Normalizing multiple broker/exchange APIs behind an internal contract vs. coding directly to each
- Handling reconnect/replay semantics for dropped market-data connections
