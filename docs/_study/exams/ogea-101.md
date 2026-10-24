---
code: OGEA-101
title: "TOGAF Enterprise Architecture Part 1"
credential: "TOGAF Enterprise Architecture Foundation"
provider: open-group
tracks: [architect]
clouds: [neutral]
level: foundation
tier: core
stage: "6"
progress: planned
official_url: https://www.opengroup.org/certifications/togaf-certification-portfolio
study_guide_url: https://www.opengroup.org/certifications/togaf-portfolio-faq
outline_version: "X2202 Conformance Requirements v4.0 (17 Oct 2022); exam plan per TOGAF Portfolio FAQ"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None. The Open Group says certification is open to all applicants and prior knowledge of enterprise architecture is helpful but not required."
replaces: ""
replaced_by: ""
counterparts: [cpsa-f]
objectives:
  - { id: "1", title: "Concepts", weight: "8 questions" }
  - { id: "1.1", title: "The concepts of Enterprise Architecture and the TOGAF Standard" }
  - { id: "1.2", title: "The key terminology of the TOGAF Standard" }
  - { id: "2", title: "Introduction to the ADM", weight: "14 questions" }
  - { id: "2.1", title: "The Architecture Development Method (ADM) cycle and the objectives of each phase, and how to adapt and scope the ADM for use" }
  - { id: "3", title: "Introduction to the ADM Techniques", weight: "6 questions" }
  - { id: "3.1", title: "The techniques available to support application of the ADM" }
  - { id: "4", title: "Introduction to Applying the ADM", weight: "4 questions" }
  - { id: "4.1", title: "Applying the ADM, including use of iteration, partitioning, and application in a Digital enterprise" }
  - { id: "5", title: "Introduction to Architecture Governance", weight: "3 questions" }
  - { id: "5.1", title: "How Architecture Governance contributes to architecture development" }
  - { id: "6", title: "Architecture Content", weight: "5 questions" }
  - { id: "6.1", title: "Architecture content: the outputs produced while executing the ADM" }
---
## About this code

OGEA-101 is The Open Group's own exam number for the English **TOGAF Enterprise Architecture Part 1** exam. Passing it earns **TOGAF Enterprise Architecture Foundation**, which also counts as Part 1 of the Practitioner path. The French and Simplified Chinese versions of the same exam are OGEA-F101 and OGEA-C101. The exam is built on a defined subset of the **TOGAF Standard, 10th Edition**.

### How the objectives above were built

The Open Group defines the body of knowledge in the *TOGAF Conformance Requirements (Multi-Level), Version 4.0* (document [X2202](https://publications.opengroup.org/x2202), published 17 October 2022). That document lists every learning unit and learning outcome, but you need a free Open Group account to download it, so this library cannot transcribe it outcome by outcome. The six top-level objectives are the exam plan published in the [TOGAF Portfolio FAQ](https://www.opengroup.org/certifications/togaf-portfolio-faq), which gives a question count for each syllabus area. The weights above are those counts exactly as The Open Group states them, so they add up to the 40 questions rather than to 100%:

| Syllabus area | Questions (of 40) | Share of the exam |
|---|---|---|
| Concepts | 8 | 20% |
| Introduction to the ADM | 14 | 35% |
| Introduction to the ADM Techniques | 6 | 15% |
| Introduction to Applying the ADM | 4 | 10% |
| Introduction to Architecture Governance | 3 | 7.5% |
| Architecture Content | 5 | 12.5% |

The share column is just the question count divided by 40. The second-level items are the seven "Value of this Certification" statements from the official [Foundation datasheet](https://certification.opengroup.org/docs/datasheets/datasheet_togaf_ea_foundation.pdf), quoted as written and each placed under the syllabus area it belongs to (that placement is this library's, not The Open Group's). The FAQ says the Level 1 body of knowledge has 8 learning units and 63 learning outcomes. When you get X2202 (sign in at publications.opengroup.org), use it as your detailed checklist.

## Exam format

All facts are as of 2026-10-24, taken from The Open Group's [TOGAF exams datasheet](https://certification.opengroup.org/docs/datasheets/togaf-exams.pdf), the [Portfolio FAQ](https://www.opengroup.org/certifications/togaf-portfolio-faq) and the [exam fee schedule](https://certification.opengroup.org/docs/exam-fee-schedule-retail.pdf). Confirm them before you book.

- **Question type:** simple multiple choice, one point per correct answer, no negative marking.
- **Number of questions:** 40.
- **Duration:** 60 minutes. For eligible English-as-a-second-language (ESL) candidates the time extension is added automatically after booking (FAQ).
- **Passing score:** 60%, which is 24 of 40.
- **Book policy:** **closed book**. This is the main difference from Part 2, which is open book.
- **Price:** USD 405 booked directly at Pearson VUE, or USD 435 as a retail voucher from The Open Group shop (retail voucher accounts need approval). The fee schedule has applied since 1 February 2026. Local taxes and currency pricing can change the amount.
- **Languages:** English (OGEA-101), French (OGEA-F101), Simplified Chinese (OGEA-C101).
- **Delivery:** Pearson VUE test centres, or at home or in the office through Pearson VUE OnVUE ([online proctored exams](https://www.opengroup.org/certifications/online-proctored-exams)). Book at [Pearson VUE for The Open Group](https://home.pearsonvue.com/theopengroup).
- **Prerequisites:** none.
- **Validity and renewal:** the datasheet says certification is to a given version of the body of knowledge and **does not expire**, so there are no re-certification or renewal requirements.
- **Combined option:** OGEA-103 combines Part 1 and Part 2 in one 150-minute sitting for USD 610 booked directly. You must pass both sections, and you only retake a failed section. If you know you want Practitioner, OGEA-103 is usually cheaper than taking OGEA-101 and OGEA-102 separately (405 + 405).

## What the exam really tests

At Part 1 the Bloom levels are remembering and understanding: knowledge and comprehension, in The Open Group's own words. Questions check whether you speak TOGAF's language precisely:

- **Vocabulary.** Architecture vs. architecture framework, Enterprise Continuum vs. Architecture Repository, building blocks (Architecture Building Blocks vs. Solution Building Blocks), deliverables vs. artifacts, stakeholders vs. concerns vs. viewpoints vs. views. Many wrong options are real TOGAF words used in the wrong place.
- **The ADM.** About a third of the exam. Know the Preliminary Phase, Phases A–H and Requirements Management at the centre, plus each phase's **objectives** and main outputs. Typical questions ask which phase produces the Statement of Architecture Work, where the Architecture Roadmap is finalised, or what Phase H responds to.
- **Adapting the ADM.** Tailoring, iteration (cycles across the whole ADM and within phase groups), scoping by breadth, depth, time period and architecture domains, and partitioning the landscape (Strategic, Segment and Capability architecture levels).
- **Techniques.** Architecture Principles, stakeholder management, business scenarios, gap analysis, migration planning techniques, interoperability and risk management, and capability-based planning. In the 10th Edition several of these live in the TOGAF Series Guides. The question is usually "which technique fits this purpose?"
- **Governance.** What the Architecture Board does, Architecture Compliance, Architecture Contracts and the governance framework, at definition level.
- **Content.** The Architecture Content Framework and the Enterprise Metamodel at a high level, plus where deliverables live.

**Where candidates lose points:** confusing similar terms, mixing up which phase produces a given output, and choosing a sensible real-world answer instead of the one the Standard states. The exam rewards TOGAF's definitions, not general architecture opinion.

## Study strategy

1. **Read the free Standard.** The TOGAF Standard, 10th Edition is free to download for personal use from The Open Group library. Start with the *Fundamental Content*: Introduction and Core Concepts, the ADM, ADM Techniques, Applying the ADM, Architecture Content and the Enterprise Architecture Capability and Governance documents. Skip the Series Guides at first, except the ones that hold Foundation-level techniques.
2. **Get the learning outcomes.** Register a free account and download [X2202](https://publications.opengroup.org/x2202). Work through it unit by unit, and keep the objective list on this page as a short checklist.
3. **Use the official study guide.** The Open Group sells the *TOGAF Enterprise Architecture Foundation Study Guide* ([B230](https://shop.opengroup.org/study-materials/togaf/b230)), which follows the Part 1 syllabus. Accredited training is optional ([training calendar](https://www.opengroup.org/training-calendar); [accredited course registers](https://www.opengroup.org/certifications/registers)).
4. **Drill the ADM until it is automatic.** Draw the ADM wheel from memory and annotate every phase with its objective and two or three key outputs. Most of the marks are here.
5. **Make flashcards for the terms.** Part 1 is closed book, so you need terms you can recall exactly.

**How your background helps or misleads**

- *AZ-900 and AZ-204/CKAD preparation* give you a feel for cloud building blocks, but TOGAF works one level above any product. In TOGAF a "building block" is a package of functionality, not an Azure resource. Do not read cloud-vendor meanings into TOGAF words.
- *The Azure Well-Architected Framework and Cloud Adoption Framework* are useful analogies. CAF's Strategy → Plan → Ready → Adopt → Govern → Manage resembles a simplified ADM, and both use governance boards and principles. Still answer with TOGAF's terms.
- *A .NET/Angular developer background* pulls you towards solution architecture, the ground CPSA-F covers. TOGAF Phase C (Information Systems Architectures) and Phase D (Technology Architecture) feel familiar, but Phases A, B, E, F and G (vision, business, opportunities, migration and governance) are where developers usually lack experience.

## Differences from related exams

- **OGEA-101 vs OGEA-102 (Practitioner, Part 2).** Part 1 is 40 closed-book questions on terms and concepts. Part 2 is 8 open-book scenario questions with gradient scoring (5/3/1/0 points) that test whether you can *apply* the ADM: which action an architect should take next for a given stakeholder situation. Part 1 is about knowing the Standard. Part 2 is about choosing the best of four plausible actions.
- **OGEA-101 vs CPSA-F (iSAQB Foundation).** The two are complementary, not competing. TOGAF works at *enterprise* level: business, data, application and technology landscapes, roadmaps and governance. CPSA-F works at the level of *one software system*: building blocks, interfaces, quality scenarios, patterns and documentation (arc42-style views). The CPSA-F curriculum (LG 01-05) even lists enterprise IT architecture as a neighbouring domain outside its scope. TOGAF Part 1 tests vocabulary recall in 60 minutes. CPSA-F tests understanding of design trade-offs, with pick-and-tick question types.
- **OGEA-101 vs AZ-305 and SAP-C02/SAP-C03.** The cloud architect exams test which service and configuration meets a requirement on one platform. TOGAF never names a product. It tests the *method* of reaching and governing architecture decisions across an enterprise. Expect cloud exams to ask "which service?" and TOGAF to ask "which phase, which deliverable, which stakeholder?".
- **OGEA-101 vs AIGP and PECB ISO/IEC 42001 Lead Implementer.** These AI governance credentials cover *what* to govern (AI risk, law and management systems). TOGAF's Architecture Governance covers *how* an architecture function governs change. An architect working in AI governance will use TOGAF governance structures (Architecture Board, compliance reviews, contracts) as the vehicle for AI controls.
- **OGEA-101 vs TOGAF 9 Foundation (OG0-091).** The older TOGAF 9 Part 1 also has 40 questions in 60 minutes at 60%, but it is based on TOGAF 9.2 and has a much larger body of knowledge (the FAQ counts 13 learning units and 107 outcomes for TOGAF 9 Level 1). The 10th Edition path is smaller and more practical. Take the 10th Edition exam.

## Exam-day notes

- **Pace:** 40 questions in 60 minutes gives you 90 seconds per question. Answer everything in one pass, flag doubtful items, and come back. There is no penalty for guessing, so never leave a question blank.
- **Read the qualifier.** "Which of the following is *not*…", "which phase *first*…" and "the *primary* purpose…" are where marks slip away.
- **Use the Standard's wording.** If two answers look reasonable, choose the one whose words match the Standard's definition. The answer that sounds like general consulting advice is usually the distractor.
- **Phase traps:** Requirements Management is not a phase with its own position in the sequence. It is continuous and sits at the centre. The Preliminary Phase sets up the architecture *capability*, while Phase A starts a specific architecture *engagement*. Phases E and F both plan migration, but F finalises the Implementation and Migration Plan.
- **Online proctoring:** clear your desk completely, run the OnVUE system test on the same computer and network beforehand, and start check-in early, because Pearson VUE opens check-in up to 30 minutes before the appointment.
