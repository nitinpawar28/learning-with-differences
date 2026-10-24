---
title: "Docker & Containerization Trade-offs"
description: Image design, orchestration, and runtime choices for containerized workloads.
tags:
  - devops
  - docker
status: stub
level: practitioner
tracks: [architect, cloud]
---

# Docker & Containerization

!!! note "Status"
    Draft stub — expand using the [article template](../about/article-template.md).

## Scope

Compare choices such as:

- Multi-stage builds vs. single-stage images — size and attack surface
- Alpine vs. Debian-slim base images — musl vs. glibc gotchas
- Docker Compose vs. Kubernetes — when the added complexity is worth it
- Bind mounts vs. named volumes for persistent data
- Bridge networking vs. host networking for latency-sensitive services
