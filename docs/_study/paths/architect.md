---
title: "Architect: from design fundamentals to AZ-305 and SAP-C03"
summary: "The architect route: quality attributes and trade-offs first, then the patterns, reliability and cloud design knowledge the expert and professional exams test."
tracks: [architect, cloud]
level: practitioner
exams: [az-305, sap-c03, sc-100]
status: draft
steps:
  - page: architecture/index.md
    note: Read the domain map first so you know where each later step fits.
  - term: horizontal-scaling
  - term: vertical-scaling
  - term: health-check
  - term: blue-green-deployment
  - term: canary-release
  - term: rolling-deployment
  - check: For a stateful trading service with a strict latency target, which deployment strategy would you choose, and what makes the other two worse?
  - page: messaging/integration/microservices-vs-modular-monoliths.md
  - page: messaging/eventing/event-driven-vs-request-response.md
  - term: transactional-outbox
  - term: at-least-once-delivery
  - term: exactly-once-delivery
  - term: idempotency-key
  - check: Explain why "at-least-once delivery plus idempotent consumers" is the usual design instead of exactly-once delivery, and name one case where it is not enough.
  - objective: az-305:1
  - objective: az-305:2
  - objective: sap-c03:1
  - check: Design the same three-tier workload on Azure and on AWS. List every service pair you chose and the fidelity of each match.
---
This path is for the architect role. It starts with the vocabulary of trade-offs
(scaling, resilience, delivery semantics), moves through the engineering
comparisons already in the library, and ends on the design domains of AZ-305
and SAP-C03. Steps are added as the architecture area is written; the
[content roadmap](../reports/roadmap.md) shows what is still planned.
