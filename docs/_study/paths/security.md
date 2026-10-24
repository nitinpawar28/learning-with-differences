---
title: "Security: from SC-900 to SC-500, SCS-C03 and SC-100"
summary: "The security route: principles and identity first, then workload and cloud security on both clouds, then the security-architect exams."
tracks: [security, cloud]
level: practitioner
exams: [sc-900, sc-500, scs-c03, sc-100, cks]
status: draft
steps:
  - page: security/index.md
  - term: least-privilege
  - term: zero-trust
  - term: rbac
  - term: capability-based-authorization
  - check: Explain the confused-deputy problem and why capability-based authorization resists it where RBAC alone does not.
  - term: api-key
  - term: mtls
  - page: security/iam/mtls-vs-api-keys.md
  - term: workload-identity
  - page: security/iam/workload-identity.md
  - term: secrets-rotation
  - check: A service in AKS calls a service in EKS. Describe how each side proves its identity without a stored secret, naming the mechanism on each cloud.
  - term: container-isolation
  - term: service-mesh
  - term: wasm-sandboxing
  - page: security/appsec/wasm-sandboxing.md
  - objective: sc-900:1
  - objective: sc-500:1
  - objective: scs-c03:1
  - objective: cks:1
  - objective: sc-100:1
  - check: Write a one-page threat model for the trading platform's market-data ingestion path using STRIDE, and list the top three controls you would add.
---
This path is for the security role. It follows the order the exams expect:
principles, identity and access, then workload isolation and cloud security,
then architecture. Each step's self-check questions are the exam-style
scenarios to practise.
