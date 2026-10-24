---
code: AAISM
title: "ISACA Advanced in AI Security Management"
credential: "ISACA Advanced in AI Security Management (AAISM)"
provider: isaca
tracks: [security, agentic-ai]
clouds: [neutral]
level: advanced
tier: elective
stage: "6"
progress: planned
official_url: https://www.isaca.org/credentialing/aaism
study_guide_url: https://www.isaca.org/credentialing/aaism/aaism-exam-content-outline
outline_version: "June 2025"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "An active CISM or CISSP is required for certification."
replaces: ""
replaced_by: ""
counterparts: [cy0-001, aigp]
objectives:
  - { id: "1", title: "AI Governance and Program Management", weight: "31%" }
  - { id: "1.1", title: "Stakeholder considerations, industry frameworks, and regulatory requirements" }
  - { id: "1.2", title: "AI-related strategies, policies, and procedures" }
  - { id: "1.3", title: "AI asset and data life cycle management" }
  - { id: "1.4", title: "AI security program development and management" }
  - { id: "1.5", title: "Business continuity and incident response" }
  - { id: "2", title: "AI Risk Management", weight: "31%" }
  - { id: "2.1", title: "AI risk assessment, thresholds, and treatment" }
  - { id: "2.2", title: "AI threat and vulnerability management" }
  - { id: "2.3", title: "AI vendor and supply chain management" }
  - { id: "3", title: "AI Technologies and Controls", weight: "38%" }
  - { id: "3.1", title: "AI security architecture and design" }
  - { id: "3.2", title: "AI life cycle (e.g., model selection, training, and validation)" }
  - { id: "3.3", title: "Data management controls" }
  - { id: "3.4", title: "Privacy, ethical, trust and safety controls" }
  - { id: "3.5", title: "Security controls and monitoring" }
---
## Exam format

ISACA's code for this credential is AAISM, and the exam has no separate number. All facts in this section are as of 2026-10-24. They come from the [AAISM certification page](https://www.isaca.org/credentialing/aaism), the [AAISM exam content outline](https://www.isaca.org/credentialing/aaism/aaism-exam-content-outline) and the [AAISM exam candidate guide](https://www.isaca.org/-/media/files/isacadp/project/isaca/certification/aaism/aaism-exam-candidate-guide.pdf).

| Item | AAISM |
|---|---|
| Question types | Multiple-choice only |
| Number of questions | 90 |
| Duration | 2.5 hours (150 minutes) |
| Scoring | Scaled from 200 to 800. **450 or higher passes.** Scored and unscored pretest items are mixed, and there is no penalty for wrong answers. |
| Languages | English, Spanish and Japanese |
| Price | US$459 for ISACA members, US$599 for non-members, plus a US$50 certification application fee after you pass |
| Delivery | PSI test centres worldwide or online with remote proctoring. Candidates in India, Mainland China and Hong Kong must use a test centre. |
| Eligibility window | Six months from registration. You can schedule from 48 hours after payment, up to 90 days ahead. |
| Prerequisite | **An active CISM or CISSP.** Without one you cannot be certified. |

**Renewal.** As of 2026-10-24, ISACA's [CPE policy](https://www.isaca.org/-/media/files/isacadp/project/isaca/certification/general/cpe_policy.pdf) sets out what an ISACA Advanced certification requires each year:

- keep your prerequisite certification current
- earn at least 10 CPE hours a year, and 30 over each three-year period, all aligned to the AAISM content outline
- pay the annual maintenance fee

You have five years after passing to apply for the certification.

The candidate guide's appendix (dated June 2025) calls Domain 2 "AI Risk and Opportunity Management", while the current outline page calls it "AI Risk Management". The subtopics are the same. Confirm the details on the official pages before you book.

## What the exam really tests

AAISM is a **management** exam. The candidate guide describes it as designed for IT security professionals with a CISM or CISSP certification who want recognition for securing enterprise AI. There are three domains: AI Governance and Program Management (31%), AI Risk Management (31%) and AI Technologies and Controls (38%). Each domain has subtopics (1A–1E, 2A–2C, 3A–3E), and these are transcribed as the objectives above. ISACA also publishes 22 **supporting tasks** that apply across the domains. In summary, they ask you to:

- set up the charter and the roles for AI governance
- write AI-specific security policies
- ensure AI is used responsibly
- run the AI risk life cycle and assess the AI threat landscape
- test AI solutions and manage their vulnerabilities
- carry out AI impact assessments
- verify the security requirements of vendor AI products
- design an AI security architecture and fit it into the enterprise architecture
- inventory and classify AI assets and data
- handle AI incidents, from investigation and reporting to containment and recovery
- include AI in business continuity and disaster recovery planning
- define AI security metrics
- choose AI security tools
- provide risk-based human oversight of AI inputs and outputs
- create AI awareness training and acceptable-use rules
- advise on the AI development life cycle

**The style is ISACA's.** Every question is multiple-choice, and the stem usually asks for the BEST, FIRST or MOST important action *from the point of view of the security manager*. The technically strongest option is often wrong when a governance step should come first: approval, a policy, an owner, a risk assessment or a business case. Technical depth is moderate. You need to know what model poisoning, prompt injection, model drift, data lineage and guardrails are, and which control category deals with each, but you will not configure anything.

**Where candidates lose points:**

- **Answering as an engineer.** "Implement a prompt filter" loses to "perform a risk assessment" or "update the AI acceptable-use policy" when the scenario has no baseline in place yet.
- **Ownership.** Questions often test who accepts the risk (the business or risk owner), not who implements the control.
- **The vendor and supply-chain domain (2C).** This domain covers contracts, the right to audit, model provenance and third-party AI components. Readers from a technical background tend to underweight it.
- **Lifecycle placement.** Some questions ask whether a control belongs at data collection, training, validation, deployment or monitoring (3B).

## Study strategy

**Order of study:**

1. **Make sure the CISM-style mindset is in place.** If you hold CISSP rather than CISM, review how ISACA frames governance, risk appetite and program management. The "manager's answer" matters even more here than in CISSP.
2. **Domain 3 basics.** Learn the AI life cycle, the model types and the AI-specific attacks first. You cannot govern what you do not understand.
3. **Domain 1, governance.** Charters, policies, inventories and incident response for AI, plus the main frameworks: the NIST AI RMF, ISO/IEC 42001 and the EU AI Act.
4. **Domain 2, risk.** Risk assessment, thresholds and treatment, threat and vulnerability management, and vendor and supply-chain management.
5. **Go back over Domain 3 controls** (architecture, data controls, privacy, ethics and safety, monitoring) with the governance lens.

**Official learning resources.** The [AAISM page](https://www.isaca.org/credentialing/aaism) lists ISACA's own preparation products: the AAISM Review Manual (digital and print), an online review course, the Questions, Answers & Explanations database (a six-month subscription to a pool of over 200 questions), a virtual workshop, a free 12-question practice exam and a members-only online study group. ISACA's QAE databases are the closest thing to the real question style. Use them to learn how ISACA thinks, not to memorize answers.

**How your background helps or misleads:**

- **AZ-204, CKAD prep and .NET or Angular development** make the technology domain easy. You can picture a RAG pipeline, an API gateway or a container serving a model. The risk is that you over-engineer your answers.
- **AZ-900** gives you the shared responsibility model, which maps well to AI vendor responsibility questions.
- **Your growth into architect and security roles** is exactly the audience of this exam. Treat it as the exam that turns you from "builds secure AI" into "runs an AI security program".
- **You cannot sit this exam for certification yet** unless you hold CISM or CISSP. Plan CISSP first (it is in this library), or treat AAISM as a later-stage target.

## Differences from related exams

- **AAISM vs AAIA vs AAIR (the ISACA AI trio).** All three have the same format: 90 questions in 150 minutes, scored on a 200–800 scale with 450 to pass. AAISM is the *security manager's* view and requires CISM or CISSP. AAIA is the *auditor's* view and requires CISA or an equivalent audit designation. AAIR is the *risk practitioner's* view, with a broad list of prerequisite designations. AAISM puts the most weight on technology and controls (38%), AAIA on operations (46%) and AAIR on risk program management (42%).
- **AAISM vs CY0-001 (CompTIA SecAI+).** SecAI+ is practitioner-level and hands-on. It includes PBQs and spends 40% on implementing AI security controls. AAISM is management-level, multiple-choice only, and asks which control and who owns it.
- **AAISM vs AIGP (IAPP AI Governance Professional).** AIGP centres on AI law, policy and privacy governance. AAISM centres on the security program, with law and frameworks covered in one subtopic (1A).
- **AAISM vs CISSP and CISM.** These are the prerequisites. AAISM assumes their general security-management knowledge and adds only the AI-specific layer.
- **AAISM vs SC-500 and SC-100 (Microsoft).** The Microsoft exams test implementing and architecting security for AI workloads with Microsoft products. AAISM is vendor-neutral and stays at program level.

## Exam-day notes

- **Pace.** 150 minutes for 90 questions is about 1 minute 40 seconds each. That is comfortable, so use the spare time to reread the stem for words like FIRST, BEST and MOST.
- **Ask "what would the security manager do?"** Prefer answers that align with business objectives, involve the right stakeholders, and use policy and risk assessment before technology.
- **Answer every question.** There is no penalty for wrong answers.
- **Remote-proctored rules are strict.** No notes, a room scan, and one short break only with permission. Read the remote proctoring guide linked from the candidate guide before exam day.
