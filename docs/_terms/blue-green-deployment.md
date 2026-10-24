---
title: "Blue-Green Deployment"
summary: "Running two identical production environments ('blue' = live, 'green' = new version), then flipping traffic to green all at once after it's verified healthy."
acronyms: []
aliases: ["Blue/green deployment"]
tracks: [architect, cloud]
domain: devops
cloud: neutral
level: practitioner
status: draft
---

## Explanation

Running two identical production environments ("blue" = live, "green" =
new version), then flipping traffic to green all at once after it's
verified healthy. Rollback is just flipping traffic back — fast, at the
cost of running two full environments simultaneously.

## Further reading

- [CI/CD Pipelines](../devops/ci-cd-pipelines.md)
