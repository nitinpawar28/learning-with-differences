---
code: CCSK
title: "Certificate of Cloud Security Knowledge v5"
credential: "CCSK - Certificate of Cloud Security Knowledge"
provider: csa
tracks: [security, cloud]
clouds: [neutral]
level: intermediate
tier: core
stage: "6"
progress: planned
official_url: https://cloudsecurityalliance.org/education/ccsk
study_guide_url: https://cloudsecurityalliance.org/artifacts/ccsk-v5-prep-kit
outline_version: "v5 (2024-07-15)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None. CSA sets no experience or training requirement. A pass counts as one year of experience toward ISC2's CCSP."
replaces: ""
replaced_by: ""
counterparts: [ccsp]
objectives:
  - { id: "1", title: "Cloud Computing Concepts and Architectures" }
  - { id: "2", title: "Cloud Governance" }
  - { id: "3", title: "Risk, Audit, and Compliance" }
  - { id: "4", title: "Organization Management" }
  - { id: "5", title: "Identity and Access Management" }
  - { id: "6", title: "Security Monitoring" }
  - { id: "7", title: "Infrastructure and Networking" }
  - { id: "8", title: "Cloud Workload Security" }
  - { id: "9", title: "Data Security" }
  - { id: "10", title: "Application Security" }
  - { id: "11", title: "Incident Response and Resilience" }
  - { id: "12", title: "Related Technologies and Strategies" }
---
## About the objectives

CCSK has no skills outline with numbered sub-objectives or domain weights. The [CCSK page](https://cloudsecurityalliance.org/education/ccsk) and [CSA Security Guidance v5](https://cloudsecurityalliance.org/artifacts/security-guidance-v5) (released 2024-07-15) define the exam scope as the 12 domains of the Security Guidance, listed above in CSA's order. The [exam FAQ](https://exams.cloudsecurityalliance.org/faq) says questions are drawn at random from a pool covering the domains. After each attempt, the Exam Results section shows how many questions came from each domain and how many you answered correctly. CSA publishes no target weighting. The free [CCSK v5 Prep Kit](https://cloudsecurityalliance.org/artifacts/ccsk-v5-prep-kit) (released 2024-07-15, updated 2025-08-26) is the closest thing to an exam guide. It contains a study guide, a knowledge guide, a curriculum covering the 12 domains, sample questions and an FAQ. Use its curriculum outline as your detailed checklist. The outline_version above is the Security Guidance v5 release date.

## Exam format

All facts below are as of 2026-10-24, from the [CCSK page](https://cloudsecurityalliance.org/education/ccsk) and the [CSA exam FAQ](https://exams.cloudsecurityalliance.org/faq).

- **Question types.** 60 multiple-choice questions, drawn at random from a larger pool.
- **Duration.** 120 minutes, uninterrupted. You cannot pause and resume. One place on the CCSK page (its meta description) says 90 minutes, but the exam section and the FAQ both say 120, so check the timer in the exam platform.
- **Passing score.** 80%, which is 48 of 60 correct.
- **Open book.** You may use the Security Guidance and your notes. CSA warns you to rely on them as little as possible because the clock is tight.
- **Price.** USD 445 for a CCSK v5 exam token (FAQ: effective 2024-07-16). The CCSK page describes the USD 445 purchase as "Exam and Chatbot". Instructor-led CCSK Foundation courses and the self-paced exam bundle include a token. The stand-alone self-paced course does not.
- **Attempts.** A token includes two attempts and is valid for two years from purchase. CSA recommends testing within one year. After a second failure you buy a new token. There is no enforced waiting period.
- **Languages.** English, Spanish and Japanese.
- **Delivery.** Online, on demand, through the [CSA exam platform](https://exams.cloudsecurityalliance.org). No test centre or appointment is needed. Results are immediate.
- **Renewal.** The certificate does not expire. CSA advises staying current with the latest CCSK version. v5 has been the current version since 2024-07-16.

Confirm the details on the official pages before buying a token.

## What the exam really tests

CCSK tests whether you understand cloud security the way CSA's Security Guidance describes it. The language is vendor-neutral and centres on governance, the shared responsibility model and the control and management planes. Version 5 was rewritten around current practice, and the 12 domains (down from 14 in v4) reflect that:

- **Concepts and architecture.** Service and deployment models, logical models (infrastructure, metastructure, applistructure, infostructure) and shared responsibility.
- **Governance, risk, audit and compliance.** Cloud governance, risk registers, compliance inheritance, and the CSA Cloud Controls Matrix (CCM) and STAR registry as assurance tools.
- **Organization management.** New in v5. It covers managing many accounts, subscriptions and projects at enterprise scale: organisational hierarchies, landing zones and guardrails.
- **IAM.** Federation, cloud-native identities, permissions and policy, and privileged access.
- **Security monitoring.** Cloud telemetry, logs and security analytics.
- **Infrastructure and networking.** Software-defined networking and zero trust.
- **Workload security.** VMs, containers, serverless and AI workloads.
- **Data security.** Encryption, key management and the data life cycle.
- **Application security.** The secure SDLC and DevSecOps.
- **Incident response and resilience.**
- **Related technologies and strategies.** Zero trust, AI, and other emerging topics.

Questions are short and conceptual. Most test whether you know CSA's specific position, for example who is responsible for what in a given model, or which control best addresses a cloud-specific risk. Because the exam is open book, the hard part is speed and precision. The answers depend on CSA's exact wording and framing, and general security intuition can lead you to a plausible but non-CSA answer.

Candidates lose points in three ways. They spend too long searching the PDF. They answer from their AWS or Azure habits rather than the guidance. They overlook the governance and organisation-management domains in favour of technical ones.

## Study strategy

1. **Get the official material.** Download the free [CCSK v5 Prep Kit](https://cloudsecurityalliance.org/artifacts/ccsk-v5-prep-kit) and [Security Guidance v5](https://cloudsecurityalliance.org/artifacts/security-guidance-v5). The prep kit's study guide is the body of knowledge the exam is written from.
2. **Read in domain order.** Domains 1 to 3 (concepts, governance, risk/audit/compliance) set the vocabulary. Domains 4 to 8 are the technical core. Finish with 9 to 12. Write your own one-page summary per domain, with key terms and CSA's recommendations. Those summaries become your open-book index.
3. **Official training options.** CSA offers [self-paced CCSK v5 training with an exam token](https://training.cloudsecurityalliance.org/certificate-of-cloud-security-knowledge-exam-bundle-v5) and [instructor-led courses](https://cloudsecurityalliance.org/education/schedule) (English, with other languages on demand).
4. **Use the sample questions** in the prep kit to calibrate. Do not rely on unofficial dumps.
5. **Light hands-on.** Map each domain onto Azure and AWS: management groups vs AWS Organizations (Domain 4), Microsoft Entra ID vs IAM Identity Center (Domain 5), Microsoft Defender for Cloud vs Security Hub (Domain 6). This makes the abstractions concrete, but answer the exam in CSA's neutral terms.

**How your background helps or misleads.**

- **AZ-900** covers the service models and shared responsibility, which is most of Domain 1.
- **AZ-204 prep** helps with IAM (OAuth, managed identities), data security (Key Vault, encryption at rest) and application security.
- **CKAD prep** helps with workload security for containers.
- **Your basic AWS knowledge** lets you see the guidance in two clouds.

The mislead is that your mental model is Azure-shaped. CSA's metastructure/applistructure framing and its governance-first language come before any product feature.

## Differences from related exams

- **CCSK vs CCSP.** CCSK is open book, online, 60 questions in 120 minutes, 80% to pass, no experience requirement, no expiry, and costs USD 445 with two attempts. [CCSP](https://www.isc2.org/certifications/ccsp) is closed book and proctored at test centres, 100 to 150 adaptive items in 3 hours, needs five years of experience, renews through CPE credits, and costs USD 599. CCSP covers more legal and contract law, data-centre design, ITIL-style operations and forensics. CCSK goes further into CSA's own frameworks (CCM, STAR) and newer v5 topics such as organisation management. Many people take CCSK first, since it counts as one year of CCSP experience.
- **CCSK vs AWS SCS-C03 and Microsoft SC-500.** Those exams test hands-on platform controls in one cloud. CCSK tests the cloud-agnostic principles behind them. CCSK is a good primer before either.
- **CCSK vs CompTIA Security+ (SY0-701, with [SY0-801](https://www.comptia.org/en-us/certifications/security/v8/) due around 2026-11-17).** Security+ is general security fundamentals with performance-based questions. CCSK assumes those fundamentals and applies them only to cloud.
- **CCSK vs AZ-900 and CLF-C02.** The cloud fundamentals exams teach what a cloud offers. CCSK teaches how to secure and govern it, at a noticeably deeper level.

## Exam-day notes

- 120 minutes for 60 questions is 2 minutes per question. That sounds generous, but it is not when you are searching a long PDF. Answer what you know at once, and look up only what you genuinely need.
- Prepare a searchable copy of the guidance and your domain summaries. Know the key terms you would search for.
- The test cannot be paused. Use a reliable connection and a quiet two-hour block.
- Read every option. CSA questions often hinge on one word, such as "always", "customer", "provider" or "first".
- An 80% pass mark leaves room for only 12 misses. Do not leave anything blank.
- Results are immediate and show per-domain counts for each attempt. If you fail, use them to target the second attempt, which is included in the token.
