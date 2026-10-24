---
title: "CI/CD Pipeline Design Trade-offs"
description: Pipeline structure, deployment strategy, and tooling choices.
tags:
  - devops
  - ci-cd
status: stub
level: practitioner
tracks: [architect, cloud]
---

# CI/CD Pipelines

!!! note "Status"
    Draft stub — expand using the [article template](../about/article-template.md).

## Scope

Compare choices such as:

- GitHub Actions vs. Azure DevOps Pipelines vs. self-hosted (e.g. Jenkins) runners
- Trunk-based development vs. long-lived feature branches
- Blue-green vs. canary vs. rolling deployments
- Build-once-promote-everywhere vs. rebuilding per environment
- Monorepo vs. polyrepo pipeline strategies
