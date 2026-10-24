# DevOps & Cloud-Native

*DevOps, Infrastructure & Cloud-Native*

## Domain Overview & Architectural Context

Everything above this layer eventually has to run somewhere, get deployed
without downtime, and survive a host reboot. This category covers how
services are packaged and orchestrated (Docker Compose today, with
Kubernetes as the standing candidate once single-host orchestration stops
being enough), how changes ship (CI/CD pipeline design, deployment
strategy), and the bare-metal reality of running this on self-hosted Linux
hardware rather than a managed cloud.

Docker Compose is the deliberate current choice, not a placeholder for
Kubernetes: for a system at this scale, Compose's single-host simplicity is
usually a better trade than Kubernetes' operational overhead. This category
exists to keep re-testing that assumption as the system grows, rather than
either prematurely adopting Kubernetes or clinging to Compose past the point
it stops fitting.

## Key Terminology & Concepts

Full definitions in the [Master Glossary](../glossary.md); the ones specific
to this category:

- [Immutable Infrastructure](../glossary.md#immutable-infrastructure) —
  replacing instances instead of patching them in place
- [Blue-Green Deployment](../glossary.md#blue-green-deployment) / [Canary
  Release](../glossary.md#canary-release) — two different ways to trade
  deployment speed for blast-radius control
- [Health Check (Liveness vs. Readiness)](../glossary.md#health-check-liveness-vs-readiness) —
  two different questions an orchestrator asks a container
- [Sidecar Pattern](../glossary.md#sidecar-pattern) — attaching cross-cutting
  concerns (mTLS, metrics) without touching application code
- [Infrastructure as Code (IaC)](../glossary.md#infrastructure-as-code-iac) —
  giving infrastructure changes the same review/diff/rollback story as code
- [Horizontal vs. Vertical Scaling](../glossary.md#horizontal-vs-vertical-scaling) —
  more instances vs. a bigger box

## Intended Knowledge Summary

By the time the articles in this folder are filled in, the reader should be
able to:

1. Name the concrete signal that would justify moving from Docker Compose to
   Kubernetes for this system — not "it's more standard," but a specific
   operational pain Compose can't solve.
2. Design a multi-stage Docker build that minimizes both image size and
   attack surface, and explain the musl/glibc gotchas of an Alpine base
   image before hitting them in production.
3. Choose a deployment strategy (blue-green vs. canary vs. rolling) based on
   the actual risk profile of a given service, not a one-size-fits-all
   default.
4. Reason about trunk-based development vs. long-lived branches in terms of
   integration risk, not just team preference.
5. Make informed virtualization choices for the bare-metal home-server
   layer — hypervisor type, storage filesystem, network segmentation — with
   the same rigor applied to the cloud-native layers above it.

## Planned Topic Matrix

| Topic | Current Stack | Candidate / Alternative | Key Trade-off | Article |
|---|---|---|---|---|
| Container orchestration | Docker Compose | Kubernetes | Single-host simplicity vs. multi-node orchestration power | [Docker & Containerization](docker-containerization.md) |
| Delivery pipeline | Trunk-based + GitHub Actions | Long-lived branches / self-hosted runners | Integration velocity vs. isolation and control | [CI/CD Pipelines](ci-cd-pipelines.md) |
| Home-lab virtualization | Docker/LXC on bare-metal Linux | Type-1 hypervisor (Proxmox/ESXi) | Lightweight isolation vs. full VM-level separation | [Bare-Metal Linux & Hypervisors](bare-metal-linux-hypervisors.md) |
