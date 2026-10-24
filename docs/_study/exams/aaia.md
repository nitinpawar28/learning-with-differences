---
code: AAIA
title: "ISACA Advanced in AI Audit"
credential: "ISACA Advanced in AI Audit (AAIA)"
provider: isaca
tracks: [security, agentic-ai]
clouds: [neutral]
level: advanced
tier: elective
stage: "6"
progress: planned
official_url: https://www.isaca.org/credentialing/aaia
study_guide_url: https://www.isaca.org/credentialing/aaia/aaia-exam-content-outline
outline_version: "June 2025"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "An active CISA, or one of the designations on ISACA's list (such as CIA, US CPA, ACCA, Canadian CPA or ICAEW ACA), which count only when the holder works in an IT audit or IT advisory role."
replaces: ""
replaced_by: ""
counterparts: [aigp, pecb-42001-li]
objectives:
  - { id: "1", title: "AI Governance and Risk", weight: "33%" }
  - { id: "1.1", title: "AI models, considerations, and requirements" }
  - { id: "1.2", title: "AI governance and program management" }
  - { id: "1.3", title: "AI risk management" }
  - { id: "1.4", title: "Privacy and data governance programs" }
  - { id: "1.5", title: "Leading practices, ethics, regulations, and standards for AI" }
  - { id: "2", title: "AI Operations", weight: "46%" }
  - { id: "2.1", title: "Data management specific to AI" }
  - { id: "2.2", title: "AI solution development methodologies and lifecycle" }
  - { id: "2.3", title: "Change management specific to AI" }
  - { id: "2.4", title: "Supervision of AI solutions (e.g., outputs, impacts, and decisions)" }
  - { id: "2.5", title: "Testing techniques for AI solutions" }
  - { id: "2.6", title: "Threats and vulnerabilities specific to AI" }
  - { id: "2.7", title: "Incident response management specific to AI" }
  - { id: "3", title: "AI Auditing Tools and Techniques", weight: "21%" }
  - { id: "3.1", title: "Audit planning and design" }
  - { id: "3.2", title: "Audit testing and sampling methodologies" }
  - { id: "3.3", title: "Audit evidence collection techniques" }
  - { id: "3.4", title: "Audit data quality and data analytics" }
  - { id: "3.5", title: "AI audit outputs and reports" }
---
## Exam format

ISACA's code for this credential is AAIA, and the exam has no separate number. All facts in this section are as of 2026-10-24. They come from the [AAIA certification page](https://www.isaca.org/credentialing/aaia), the [AAIA exam content outline](https://www.isaca.org/credentialing/aaia/aaia-exam-content-outline) and the [AAIA exam candidate guide](https://www.isaca.org/-/media/files/isacadp/project/isaca/certification/aaia/aaia-exam-candidate-guide.pdf).

| Item | AAIA |
|---|---|
| Question types | Multiple-choice only |
| Number of questions | 90 |
| Duration | 2.5 hours (150 minutes) |
| Scoring | Scaled from 200 to 800. **450 or higher passes.** There is no penalty for wrong answers. |
| Languages | English, Simplified Chinese and Spanish |
| Price | US$459 for ISACA members, US$599 for non-members, plus a US$50 certification application fee after you pass |
| Delivery | PSI test centres worldwide or online with remote proctoring. Candidates in India, Mainland China and Hong Kong must use a test centre. |
| Eligibility window | Six months from registration. You can schedule from 48 hours after payment, up to 90 days ahead. |
| Prerequisite | **An active CISA**, or one of the other designations listed on the certification page (for example CIA, US CPA, ACCA, Canadian CPA, ICAEW ACA). Every designation other than CISA counts only when the holder works in an IT audit or IT advisory role. |

**Renewal.** As of 2026-10-24, ISACA's [CPE policy](https://www.isaca.org/-/media/files/isacadp/project/isaca/certification/general/cpe_policy.pdf) sets out what an ISACA Advanced certification requires each year:

- keep your prerequisite designation current
- earn at least 10 CPE hours a year, and 30 over each three-year period, all aligned to the AAIA content outline
- pay the annual maintenance fee

The content outline in the candidate guide is dated **June 2025**. Confirm the details on the official pages before you book.

## What the exam really tests

AAIA asks whether an IT auditor can **give assurance over AI**, and also whether they can use AI in their own audit work. There are three domains: AI Governance and Risk (33%), AI Operations (46%) and AI Auditing Tools and Techniques (21%). Their subtopics (1A–1E, 2A–2G, 3A–3E) are the objectives above. ISACA also lists 23 "other skills tested", nearly all of which begin with **Evaluate**. They cover evaluating:

- AI solutions, policies and decision-making systems
- the impact on the workforce, and awareness programmes
- alignment with the enterprise architecture
- the AI life cycle, algorithms and models
- vendor and supply-chain programmes
- ownership of AI risk
- AI controls, and change, configuration, data-governance, IAM, privacy, threat-and-vulnerability and incident management for AI
- the appropriateness of input data, including bias and privacy
- AI metrics (KPIs and KRIs)

The last two skills cover using AI within the audit process itself: its impact, opportunities and risks, and AI-enhanced planning, execution and reporting.

**The style.** Questions are written from the auditor's seat. You evaluate, test, sample, collect evidence and report. You do not design or implement. The classic ISACA traps apply:

- The auditor does not fix findings. Management does.
- The auditor's independence matters.
- The "first" step is usually to understand the process or review the documentation before testing.

The AI-specific twist is that the evidence is unusual: model cards, training-data lineage, bias-testing results, drift monitoring, human-oversight logs and prompt and output logs.

**Where candidates lose points:**

- **Choosing a remediation instead of an audit action.** "Retrain the model" is management's job. "Evaluate whether retraining controls exist and operate" is the auditor's.
- **Domain 2 is the heaviest (46%).** It covers data management for AI, development methodologies, change management, supervision of outputs, testing techniques, AI threats and incident response. Candidates from finance-audit backgrounds tend to be weakest here.
- **Sampling and evidence (3B, 3C).** The questions look familiar from CISA, but now apply to non-deterministic outputs. Ask yourself how you would sample a model's decisions.

## Study strategy

**Order of study:**

1. **Audit fundamentals.** If you do not hold CISA, you cannot be certified without another qualifying designation, so the main path is CISA first. CISA's audit-process domain is the foundation for Domain 3 here.
2. **AI fundamentals for Domain 1A and Domain 2.** Learn the model types, the training, validation and testing split, data lineage, drift, explainability and the common AI attacks.
3. **Domain 1, governance, risk and privacy.** Responsible-AI principles, the NIST AI RMF, ISO/IEC 42001 and the EU AI Act, and privacy and data governance.
4. **Domain 2, operations, in order.** Data management, the life cycle, change management, supervision of outputs, testing, threats and incident response.
5. **Domain 3, audit techniques.** Planning, testing and sampling, evidence, analytics and data quality, and reporting, including the use of AI tools in the audit.

**Official learning resources.** The [AAIA page](https://www.isaca.org/credentialing/aaia) lists the AAIA Review Manual (digital and print), an online review course, a Questions, Answers & Explanations database (a six-month subscription with over 200 questions), a virtual workshop, a free 12-question practice quiz and a member study group.

**How your background helps or misleads:**

- **Your developer background (.NET, Angular, AZ-204 prep)** is an advantage in Domain 2. You know what CI/CD, change control, testing and logging look like, so judging whether they exist for a model pipeline comes naturally.
- **CKAD prep** helps you understand where models run (containers, configuration, secrets), which matters for 2B and 2C.
- **The misleading part.** This exam rewards the auditor's restraint. You already know how to build it, but the exam asks how you would *prove* it is controlled.
- **Eligibility is the real hurdle.** Without CISA or a listed equivalent you cannot be certified. In this roadmap AAIA is a later-stage target, after CISA or an equivalent designation.

## Differences from related exams

- **AAIA vs AAISM and AAIR.** All three share the same format: 90 multiple-choice questions in 150 minutes, scored on a 200–800 scale with 450 to pass. AAIA takes the *assurance* view and requires CISA or an equivalent. AAISM takes the *security-management* view and requires CISM or CISSP. AAIR takes the *risk* view. AAIA is the only one with a whole domain on audit tools and techniques (21%).
- **AAIA vs AIGP (IAPP).** AIGP tests designing and running AI governance (law, policy, impact assessments). AAIA tests evaluating whether that governance works. Use AIGP if you build the program and AAIA if you audit it.
- **AAIA vs PECB ISO/IEC 42001 Lead Implementer.** The PECB course and exam teach you to *implement* an AI management system to ISO/IEC 42001. AAIA is broader than one standard and audit-focused.
- **AAIA vs CY0-001 (SecAI+).** SecAI+ is a hands-on practitioner exam with PBQs on securing AI. AAIA has no hands-on element and covers the whole AI operating model, not just security.

## Exam-day notes

- **Pace.** About 1 minute 40 seconds per question. That is enough time to reread every stem.
- **Before you answer, check your role.** "Is this something an auditor does?" If an option implements, designs or fixes, it is probably a distractor.
- **For "first" questions,** prefer understanding the scope, the process and the risk, and reviewing documentation, before testing.
- **Answer every question.** There is no penalty for wrong answers.
- **Remote proctoring rules are strict.** Read the candidate guide's remote-proctoring section in advance.
