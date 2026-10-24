---
title: "High-Throughput APIs: REST vs. gRPC"
description: Protocol, serialization, and contract trade-offs for high-throughput services.
tags:
  - messaging
  - api-design
  - grpc
status: stub
level: practitioner
tracks: [architect]
---

# High-Throughput REST/gRPC APIs

!!! note "Status"
    Draft stub — expand using the [article template](../../about/article-template.md).

## Scope

Compare choices such as:

- REST/JSON over HTTP/1.1 vs. gRPC over HTTP/2 (streaming, multiplexing)
- Protobuf vs. JSON serialization — payload size and (de)serialization cost
- Unary calls vs. gRPC streaming (client, server, bidirectional)
- API versioning strategies and contract evolution (REST vs. `.proto`)
- Where an API gateway / BFF changes the calculus
