---
code: ISSAP
title: "Information Systems Security Architecture Professional"
credential: "ISSAP - Information Systems Security Architecture Professional"
provider: isc2
tracks: [security, architect]
clouds: [neutral]
level: expert
tier: elective
stage: "6"
progress: planned
official_url: https://www.isc2.org/certifications/issap
study_guide_url: https://www.isc2.org/certifications/issap/issap-certification-exam-outline
outline_version: "2025-08-01"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "A CISSP in good standing plus two years of cumulative, full-time experience in one or more of the four ISSAP domains. ISC2 also accepts seven years of cumulative, full-time experience in two or more ISSAP domains without the CISSP. On that route a relevant degree or an approved credential can waive one of the seven years."
replaces: ""
replaced_by: ""
counterparts: [sc-100, cas-005]
objectives:
  - { id: "1", title: "Governance, Risk, and Compliance (GRC)", weight: "21%" }
  - { id: "1.1", title: "Identify legal, regulatory, organizational and industry requirements" }
  - { id: "1.1.1", title: "Applicable information security standards and guidelines" }
  - { id: "1.1.2", title: "Third-party and contractual obligations (supply chain, outsourcing, partners)" }
  - { id: "1.1.3", title: "Applicable sensitive/personal data standards, guidelines and privacy regulations" }
  - { id: "1.1.4", title: "Resilient solutions" }
  - { id: "1.2", title: "Architecting for governance, risk and compliance (GRC)" }
  - { id: "1.2.1", title: "Identify key assets, business objectives and stakeholders" }
  - { id: "1.2.2", title: "Design monitoring and reporting (vulnerability management, compliance audit)" }
  - { id: "1.2.3", title: "Design for auditability (regulatory, legislative, forensic requirements, segregation, high-assurance systems)" }
  - { id: "1.2.4", title: "Incorporate risk assessment artifacts" }
  - { id: "1.2.5", title: "Advise risk treatment (mitigate, transfer, accept, avoid)" }
  - { id: "2", title: "Security Architecture Modeling", weight: "22%" }
  - { id: "2.1", title: "Identify the security architecture approach" }
  - { id: "2.1.1", title: "Scope (enterprise, cloud) and types (network, service-oriented architecture)" }
  - { id: "2.1.2", title: "Frameworks (TOGAF, SABSA, service-oriented modeling framework)" }
  - { id: "2.1.3", title: "Reference architectures and blueprints" }
  - { id: "2.1.4", title: "Threat modeling frameworks (STRIDE, CVSS, threat intelligence)" }
  - { id: "2.2", title: "Verify and validate the design (functional acceptance testing, regression)" }
  - { id: "2.2.1", title: "Results of threat modeling (threat vectors, impact, probability)" }
  - { id: "2.2.2", title: "Gaps" }
  - { id: "2.2.3", title: "Alternative solutions, mitigations and compensating controls" }
  - { id: "2.2.4", title: "Internal or external third-party validation (tabletop exercises, modeling and simulation, manual review, peer review)" }
  - { id: "2.2.5", title: "Code review methodology (dynamic, manual, static, source composition analysis)" }
  - { id: "3", title: "Infrastructure and System Security Architecture", weight: "32%" }
  - { id: "3.1", title: "Identify infrastructure and system security requirements" }
  - { id: "3.1.1", title: "Deployment model (on-premises, cloud-based, hybrid)" }
  - { id: "3.1.2", title: "Information technology (IT) and operational technology" }
  - { id: "3.1.3", title: "Physical security (perimeter protection and internal zoning, fire suppression)" }
  - { id: "3.1.4", title: "Infrastructure and system monitoring" }
  - { id: "3.1.5", title: "Infrastructure and system cryptography" }
  - { id: "3.1.6", title: "Application security (requirements traceability matrix, architecture documentation, secure coding)" }
  - { id: "3.2", title: "Architect infrastructure and system security" }
  - { id: "3.2.1", title: "Physical security control set (cameras, doors, system controllers)" }
  - { id: "3.2.2", title: "Platform security (physical, virtual, container, firmware, OS)" }
  - { id: "3.2.3", title: "Network security (wired/wireless, public/private, IoT, management, firewalls, air gaps, software-defined perimeters, VPN, IPsec, NAC, DNS, NTP, VoIP, WAF)" }
  - { id: "3.2.4", title: "Storage security (DAS, SAN, NAS, archival and removable media, encryption)" }
  - { id: "3.2.5", title: "Data repository security (access control, encryption, redaction, masking)" }
  - { id: "3.2.6", title: "Cloud security (public/private, IaaS, PaaS, SaaS)" }
  - { id: "3.2.7", title: "Operational technology (ICS, IoT, SCADA)" }
  - { id: "3.2.8", title: "Endpoint security (BYOD, mobile, EDR, HIDS/HIPS)" }
  - { id: "3.2.9", title: "Secure shared services (email, VoIP, unified communications)" }
  - { id: "3.2.10", title: "Third-party integrations (internal/external, federation, API, VPN, SFTP)" }
  - { id: "3.2.11", title: "Infrastructure monitoring" }
  - { id: "3.2.12", title: "Content monitoring (email, web, data, social media, DLP)" }
  - { id: "3.2.13", title: "Out-of-band communications (incident response, IT system management, BC/DR)" }
  - { id: "3.2.14", title: "Evaluate applicability of security controls for system components (web clients, proxy services, application services)" }
  - { id: "3.3", title: "Architect infrastructure and system cryptographic solutions" }
  - { id: "3.3.1", title: "Cryptographic design considerations and constraints (technologies, lifecycle, computational capabilities, algorithms, attacks)" }
  - { id: "3.3.2", title: "Cryptographic implementation (in transit, in use, at rest)" }
  - { id: "3.3.3", title: "Plan the key management lifecycle (generation, storage, distribution)" }
  - { id: "4", title: "Identity and Access Management (IAM) Architecture", weight: "25%" }
  - { id: "4.1", title: "Architect the identity lifecycle" }
  - { id: "4.1.1", title: "Establish and verify identity (physical, logical)" }
  - { id: "4.1.2", title: "Assign identifiers (users, services, processes, devices, components)" }
  - { id: "4.1.3", title: "Identity provisioning and de-provisioning (joiners, movers and leavers)" }
  - { id: "4.1.4", title: "Identity management technologies" }
  - { id: "4.2", title: "Architect identity authentication" }
  - { id: "4.2.1", title: "Define the authentication approach (single-factor, multi-factor, risk-based elevation)" }
  - { id: "4.2.2", title: "Authentication protocols and technologies (SAML, RADIUS, Kerberos, OAuth)" }
  - { id: "4.2.3", title: "Authentication control protocols and technologies (XACML, LDAP)" }
  - { id: "4.2.4", title: "Define trust relationships (federated, stand-alone)" }
  - { id: "4.3", title: "Architect identity authorization" }
  - { id: "4.3.1", title: "Authorization concepts and principles (discretionary/mandatory, SoD, least privilege, interactive, non-interactive)" }
  - { id: "4.3.2", title: "Authorization models (physical, logical, administrative)" }
  - { id: "4.3.3", title: "Authorization process and workflow (governance, issuance, periodic review, revocation, suspension)" }
  - { id: "4.3.4", title: "Roles, rights and responsibilities for system, application and data access (groups, DRM, trust relationships)" }
  - { id: "4.3.5", title: "Management of privileged accounts (PAM)" }
  - { id: "4.3.6", title: "Authorization approach (SSO, rule-based, role-based, attribute-based, token, certificate)" }
  - { id: "4.4", title: "Architect identity accounting" }
  - { id: "4.4.1", title: "Determine accounting, analysis and forensic requirements" }
  - { id: "4.4.2", title: "Define audit events" }
  - { id: "4.4.3", title: "Establish audit log alerts and notifications" }
  - { id: "4.4.4", title: "Log management (retention, integrity)" }
  - { id: "4.4.5", title: "Log analysis and reporting" }
  - { id: "4.4.6", title: "Comply with policies and regulations (PCI DSS, FISMA, HIPAA, GDPR)" }
---
## Exam format

All facts below are as of 2026-10-24, from the [ISSAP exam outline page](https://www.isc2.org/certifications/issap/issap-certification-exam-outline) and its [outline PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/certifications/Certs/ISSAP/ISSAP-Exam-Outline-2025.pdf) (effective August 1, 2025), unless another link is given.

- **Question types.** The outline page and ISC2's [exam preparation page](https://www.isc2.org/exams/before-your-exam) list "multiple choice and advanced item types". The outline PDF lists multiple choice only. ISC2 says its advanced items can include multimedia, calculation, order-response, drag-and-drop or hotspot, and scenario-based questions.
- **Fixed length, not adaptive.** ISC2 uses Computerized Adaptive Testing only for CC, SSCP, CISSP and CCSP ([CAT page](https://www.isc2.org/certifications/computerized-adaptive-testing)). ISSAP is a fixed-length exam, so every candidate gets the full 125 items.
- **Number of items.** 125, with a 3-hour limit.
- **Passing score.** 700 out of 1000 scaled points.
- **Language.** English only.
- **Delivery.** Pearson VUE test centres. Pearson charges USD 50 to reschedule and USD 100 to cancel ([scheduling page](https://www.isc2.org/exams/schedule-exam)).
- **Price.** USD 599 in the Americas on the [ISC2 exam pricing page](https://www.isc2.org/register-for-exam/isc2-exam-pricing). Prices vary by region.
- **Retakes.** The [retake policy](https://www.isc2.org/exams/after-your-exam#retakePolicy) requires 30, 60 and then 90 test-free days between attempts, with at most four attempts in 12 months.
- **Eligibility.** You need a CISSP in good standing plus two years of architecture-domain experience, or seven years of experience across two or more ISSAP domains.
- **Renewal.** The CPE table in the [member policies](https://www.isc2.org/policies-procedures/member-policies) lists, for an ISSAP who also holds the CISSP, 20 Group A credits suggested a year and 60 per three-year cycle. Its footnote says these concentration credits count toward the CISSP's 120. An ISSAP without the CISSP needs 140 Group A credits per cycle (47 suggested a year). The [AMF overview](https://www.isc2.org/policies-procedures/amfs-overview) sets a single USD 135 annual maintenance fee for holders of CISSP, ISSAP and the other professional credentials.

Confirm all of this on the official pages before booking.

## What the exam really tests

ISSAP is the architect's exam in the ISC2 family. The 2025 outline cut the old six domains to four. Infrastructure and system security architecture is the biggest at 32%, followed by IAM architecture at 25%. The exam expects you to take requirements (legal, business, risk) and turn them into a coherent design. You choose between patterns, justify trade-offs, define trust boundaries, and show that the design can be audited and verified.

Expect scenario questions such as these:

- An enterprise merging two identity estates. You choose a federation model, the protocols (SAML, OAuth, Kerberos, LDAP, XACML) and the authorization approach.
- A plant adding remote OT access. You design zoning, out-of-band management and monitoring.
- A data platform needing encryption in use, in transit and at rest. You decide where keys live and who controls their life cycle.
- A design review. You decide what the threat model reveals, what the gaps are and which compensating controls fit.

This is deeper than CISSP on the same topics. CISSP asks what an ABAC policy decision point is. ISSAP asks where to place PDPs and PEPs, and how authorization reviews, revocation and logging fit together for a regulated workload.

Candidates lose points when they pick the most secure option rather than the one that meets the stated requirements. They also skip the GRC framing: who the stakeholders are, which regulation drives the requirement and how the design will be audited. And they treat IAM as a product feature rather than a life cycle running from establishing identity, through authentication and authorization, to accounting.

## Study strategy

1. **Finish CISSP first.** ISSAP builds on CISSP Domains 1, 3, 4 and 5. Without that base the vocabulary will slow you down. The CISSP is also the usual route to eligibility.
2. **Study in the outline's order.** Do GRC first, because requirements drive the architecture. Then architecture modelling (frameworks, reference architectures, threat modelling, design validation). Then infrastructure, which is the largest domain. Finish with IAM.
3. **Learn the frameworks as tools, not trivia.** Know what SABSA's layers and attribute profiling give you, how TOGAF's ADM phases fit security in, and how STRIDE and CVSS feed a design review. The Open Group's [TOGAF certification exams](https://www.opengroup.org/certifications) (OGEA-101 and OGEA-102, also in this library) pair naturally with ISSAP on the architect track.
4. **Official ISC2 resources.** ISC2 offers [ISSAP Online Self-Paced Training](https://www.isc2.org/training/online-self-paced/issap-online-self-paced) and other training linked from the [ISSAP page](https://www.isc2.org/certifications/issap), plus the [supplementary references list](https://www.isc2.org/certifications/references).
5. **Hands-on as design practice.** Draw real reference designs and defend them in writing. A hub-and-spoke network with a WAF and private endpoints. Federated SSO between two tenants. A PAM model with just-in-time elevation. A logging architecture with integrity protection. For each, list the requirement every component satisfies.

**How your background helps or misleads.**

- **AZ-204 prep** taught you OAuth 2.0/OpenID Connect flows, managed identities and Key Vault. These map to 4.2 and 3.3.
- **CKAD prep** maps to platform and container security (3.2.2).
- **Your developer background** helps with the code review methodology (2.2.5) and application security (3.1.6).

The trap is designing at the component level. ISSAP rewards thinking from requirements to architecture to verification, not "which library do I use".

## Differences from related exams

- **ISSAP vs CISSP.** CISSP is broad and managerial: eight domains, adaptive, 100 to 150 items. ISSAP is narrow and deep: four architecture domains, 125 fixed items, English only. CISSP answers what and why. ISSAP answers how to put it together and how to prove it works.
- **ISSAP vs Microsoft SC-100.** SC-100 (Cybersecurity Architect Expert) designs zero-trust architectures with Microsoft's products and references: the Microsoft Cybersecurity Reference Architectures, Microsoft Defender, Microsoft Entra, Microsoft Purview and Microsoft Sentinel. ISSAP covers the same thinking with no vendor at all. It also covers physical security, OT/SCADA and cryptographic design, which SC-100 barely touches.
- **ISSAP vs CompTIA SecurityX (CAS-005).** SecurityX is an expert engineering exam with performance-based questions. It covers architecture, but also operations and engineering tasks. ISSAP is pure architecture and has no simulations.
- **ISSAP vs TOGAF (OGEA-101/102) and iSAQB CPSA.** Those are general enterprise or software architecture certifications. ISSAP applies architecture discipline to security specifically, uses SABSA alongside TOGAF and adds IAM and crypto design.
- **ISSAP vs CCSP.** CCSP is cloud-only and covers operations, legal and contracts. ISSAP covers every deployment model at design depth and treats cloud as one platform among several (3.2.6).

## Exam-day notes

- 125 items in 180 minutes gives you about 86 seconds each. Keep a steady pace and do not let one long scenario eat the time of three short ones.
- Many stems are long and full of requirements. Underline (mentally) every "must", every regulation and every constraint, then pick the design that satisfies all of them. That is usually not the most elaborate one.
- Watch for actor and life-cycle cues: requirements, design, validation, operation. A validation question wants a test or review technique, not a new control.
- For IAM items, place the scenario in the life cycle first (establish, authenticate, authorize, account), then pick the mechanism.
- The exam is under an ISC2 non-disclosure agreement, so do not use or share recalled questions.
