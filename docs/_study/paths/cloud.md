---
title: "Cloud: Azure and AWS side by side, to AZ-104 and SAA-C03"
summary: "The cloud route: provider-neutral foundations, then the twelve capabilities on both clouds together, so each one is learned through its differences."
tracks: [cloud, architect]
level: practitioner
exams: [clf-c02, az-104, saa-c03, ta-004]
status: draft
steps:
  - page: cloud/index.md
    note: The twelve-capability map that every later step follows.
  - objective: clf-c02:1
  - term: horizontal-scaling
  - term: vertical-scaling
  - term: immutable-infrastructure
  - term: infrastructure-as-code
  - check: Describe the same virtual network with two subnets in Bicep and in CloudFormation. Which concepts have no exact equivalent on the other side?
  - term: data-retention-policy
  - term: liveness-probe
  - term: readiness-probe
  - page: devops/docker-containerization.md
  - page: devops/ci-cd-pipelines.md
  - check: A container passes its liveness probe but fails its readiness probe. What does the platform do, and what is the most likely cause?
  - objective: az-104:1
  - objective: saa-c03:1
  - objective: ta-004:1
  - check: Pick one capability (identity, networking or storage) and write the Azure-to-AWS Rosetta row for every service you used this week, with a fidelity rating and the difference that matters.
---
This path is for the cloud role and feeds the architect path. The two
providers are studied together on purpose: the AZ-104 and SAA-C03 objectives
overlap heavily, and the differences between the two clouds are the fastest
way to make each one stick.
