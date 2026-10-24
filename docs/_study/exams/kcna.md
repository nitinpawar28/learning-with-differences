---
code: KCNA
title: "Kubernetes and Cloud Native Associate"
credential: "Kubernetes and Cloud Native Associate (KCNA)"
provider: linux-foundation
tracks: [cloud]
clouds: [neutral]
level: associate
tier: skip
stage: ""
progress: planned
official_url: https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/
study_guide_url: https://github.com/cncf/curriculum
outline_version: "n/a"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. It is the entry-level Kubernetes certification from the Linux Foundation and CNCF."
replaces: ""
replaced_by: ""
counterparts: []
objectives: []
---
## Why this is catalogue only

KCNA is active as of 2026-10-24. The [certification page](https://training.linuxfoundation.org/certification/kubernetes-cloud-native-associate/) describes an online, proctored, multiple-choice exam of 90 minutes, priced at 250 USD with one retake, and valid for 2 years. The domains are Kubernetes Fundamentals (44%), Container Orchestration (28%), Cloud Native Application Delivery (16%) and Cloud Native Architecture (12%). The CNCF publishes the curriculum in its [curriculum repository](https://github.com/cncf/curriculum).

It is catalogue-only because the reader's CKAD preparation already goes further than KCNA. CKAD requires you to build and fix Pods, Deployments, Services, ConfigMaps, probes and network policies at a live terminal. KCNA only asks you to recognize those concepts, plus some ecosystem vocabulary (observability, GitOps, CNCF project maturity). If a Kubernetes credential is wanted, sit CKAD, then CKA or CKS.

## Differences from related exams

- **KCNA vs CKAD, CKA and CKS.** KCNA is multiple-choice and tests concepts. The other three are hands-on, performance-based exams in a real cluster under time pressure. They test application delivery (CKAD), cluster administration (CKA) and cluster security (CKS).
- **KCNA vs KCSA.** Both are entry-level multiple-choice exams. KCSA narrows the scope to Kubernetes and cloud-native security: the 4Cs, threat modelling, Pod Security Standards and compliance frameworks.
- **KCNA vs AZ-900 and CLF-C02.** The style and depth are similar. The cloud fundamentals exams test one provider's services and pricing, and KCNA tests the vendor-neutral orchestration layer that AKS and EKS both run.
