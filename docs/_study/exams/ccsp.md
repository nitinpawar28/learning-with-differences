---
code: CCSP
title: "Certified Cloud Security Professional"
credential: "CCSP - Certified Cloud Security Professional"
provider: isc2
tracks: [security, cloud, architect]
clouds: [neutral]
level: professional
tier: core
stage: "6"
progress: planned
official_url: https://www.isc2.org/certifications/ccsp
study_guide_url: https://www.isc2.org/certifications/ccsp/ccsp-certification-exam-outline
outline_version: "2026-08-01"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "Five years of cumulative, full-time IT experience, including three years in cybersecurity and one year in one or more of the six CCSP domains. The CSA CCSK can substitute for one year (only one year can be waived). An active CISSP substitutes for the entire requirement. Without the experience you become an Associate of ISC2."
replaces: ""
replaced_by: ""
counterparts: [ccsk, scs-c03, sc-100]
objectives:
  - { id: "1", title: "Cloud Concepts, Architecture and Design", weight: "17%" }
  - { id: "1.1", title: "Understand cloud computing concepts" }
  - { id: "1.1.1", title: "Cloud computing definitions" }
  - { id: "1.1.2", title: "Cloud computing roles and responsibilities (customer, CSP, partner, broker, regulator)" }
  - { id: "1.1.3", title: "Essential characteristics (on-demand self-service, broad network access, multi-tenancy, elasticity, resource pooling, measured service)" }
  - { id: "1.1.4", title: "Building block technologies (virtualization, storage, networking, databases, orchestration)" }
  - { id: "1.2", title: "Describe cloud reference architecture" }
  - { id: "1.2.1", title: "Cloud computing activities" }
  - { id: "1.2.2", title: "Cloud service capabilities (application, platform, infrastructure capability types)" }
  - { id: "1.2.3", title: "Cloud service categories (SaaS, IaaS, PaaS)" }
  - { id: "1.2.4", title: "Cloud deployment models (public, private, hybrid, community, multi-cloud)" }
  - { id: "1.2.5", title: "Cloud shared considerations (interoperability, portability, reversibility, availability, SLAs, auditability, outsourcing and more)" }
  - { id: "1.2.6", title: "Impact of related technologies (data science, ML, AI, blockchain, IoT, containers, quantum, edge, confidential computing)" }
  - { id: "1.3", title: "Understand security concepts relevant to cloud computing" }
  - { id: "1.3.1", title: "Cryptography and key management" }
  - { id: "1.3.2", title: "Identity and access control (user, privilege, service access)" }
  - { id: "1.3.3", title: "Data and media sanitization (overwriting, cryptographic erase)" }
  - { id: "1.3.4", title: "Network security (network security groups, traffic inspection, geofencing)" }
  - { id: "1.3.5", title: "Virtualization security (hypervisor, container, ephemeral computing, serverless, isolation)" }
  - { id: "1.3.6", title: "Common cloud threats" }
  - { id: "1.3.7", title: "Security hygiene (patching, baselining, immutable architecture, hardening)" }
  - { id: "1.4", title: "Understand design principles of secure cloud computing" }
  - { id: "1.4.1", title: "Cloud secure data lifecycle" }
  - { id: "1.4.2", title: "Cloud-based business continuity (BC) and disaster recovery (DR) planning" }
  - { id: "1.4.3", title: "Business impact analysis (cost-benefit analysis, ROI)" }
  - { id: "1.4.4", title: "Functional security requirements (portability, interoperability, vendor lock-in)" }
  - { id: "1.4.5", title: "Security considerations and responsibilities for SaaS, IaaS and PaaS" }
  - { id: "1.4.6", title: "Cloud design patterns (SANS security principles, Well-Architected Framework, CSA Enterprise Architecture, secure by design)" }
  - { id: "1.4.7", title: "DevOps security" }
  - { id: "1.5", title: "Evaluate cloud service providers (CSP)" }
  - { id: "1.5.1", title: "Verification against criteria" }
  - { id: "1.5.2", title: "System/subsystem product certifications (Common Criteria, FIPS 140-2)" }
  - { id: "1.6", title: "Comprehend artificial intelligence (AI)/machine learning (ML)" }
  - { id: "1.6.1", title: "Cloud threat detection and analysis" }
  - { id: "1.6.2", title: "Data source validation and verification" }
  - { id: "1.6.3", title: "Security orchestration, automation and response (SOAR)" }
  - { id: "1.6.4", title: "Ethical concerns" }
  - { id: "1.6.5", title: "Regulatory requirements" }
  - { id: "2", title: "Cloud Data Security", weight: "20%" }
  - { id: "2.1", title: "Describe cloud data concepts" }
  - { id: "2.1.1", title: "Cloud data lifecycle phases" }
  - { id: "2.1.2", title: "Data dispersion" }
  - { id: "2.1.3", title: "Data flows" }
  - { id: "2.2", title: "Design and implement cloud data storage architectures" }
  - { id: "2.2.1", title: "Storage types (long-term, ephemeral, raw, object, volume)" }
  - { id: "2.2.2", title: "Threats to storage types" }
  - { id: "2.3", title: "Design and apply data security technologies and strategies" }
  - { id: "2.3.1", title: "Encryption and key management" }
  - { id: "2.3.2", title: "Hashing (data integrity, nonrepudiation)" }
  - { id: "2.3.3", title: "Data obfuscation (masking, anonymization)" }
  - { id: "2.3.4", title: "Tokenization" }
  - { id: "2.3.5", title: "Data loss prevention (DLP)" }
  - { id: "2.3.6", title: "Keys, secrets and certificates management" }
  - { id: "2.4", title: "Implement data discovery" }
  - { id: "2.4.1", title: "Structured data" }
  - { id: "2.4.2", title: "Unstructured data" }
  - { id: "2.4.3", title: "Semi-structured data" }
  - { id: "2.4.4", title: "Data location" }
  - { id: "2.5", title: "Plan and implement data classification" }
  - { id: "2.5.1", title: "Data classification policies" }
  - { id: "2.5.2", title: "Data mapping" }
  - { id: "2.5.3", title: "Data labeling and tagging" }
  - { id: "2.6", title: "Design and implement information rights management (IRM)" }
  - { id: "2.6.1", title: "Objectives (data rights, provisioning, access models)" }
  - { id: "2.6.2", title: "Appropriate tools (issuing and revocation of certificates)" }
  - { id: "2.7", title: "Plan and implement data retention, deletion and archiving policies" }
  - { id: "2.7.1", title: "Data retention policies" }
  - { id: "2.7.2", title: "Data deletion procedures and mechanisms" }
  - { id: "2.7.3", title: "Data archiving procedures and mechanisms" }
  - { id: "2.7.4", title: "Legal hold (authorized access, deletion prevention)" }
  - { id: "2.8", title: "Design and implement auditability, traceability and accountability of data events" }
  - { id: "2.8.1", title: "Event sources and required event attributes (identity, IP address, geolocation)" }
  - { id: "2.8.2", title: "Logging, storage and analysis of data events" }
  - { id: "2.8.3", title: "Chain of custody and non-repudiation" }
  - { id: "2.9", title: "Comprehend data protection of AI and ML data" }
  - { id: "2.9.1", title: "Data set and model privacy" }
  - { id: "2.9.2", title: "Data set and model security (validation, verification)" }
  - { id: "3", title: "Cloud Platform and Infrastructure Security", weight: "17%" }
  - { id: "3.1", title: "Comprehend cloud infrastructure components" }
  - { id: "3.1.1", title: "Physical environment" }
  - { id: "3.1.2", title: "Network and communications" }
  - { id: "3.1.3", title: "Compute" }
  - { id: "3.1.4", title: "Virtualization" }
  - { id: "3.1.5", title: "Storage" }
  - { id: "3.1.6", title: "Management plane" }
  - { id: "3.2", title: "Design a secure data center" }
  - { id: "3.2.1", title: "Logical design (tenant partitioning, access control)" }
  - { id: "3.2.2", title: "Physical design (location, buy or build)" }
  - { id: "3.2.3", title: "Environmental design (HVAC, multi-vendor pathway connectivity)" }
  - { id: "3.2.4", title: "Design resilience (power, HVAC, connectivity)" }
  - { id: "3.3", title: "Analyze risks associated with cloud infrastructure and platforms" }
  - { id: "3.3.1", title: "Risk assessment (identification, analysis)" }
  - { id: "3.3.2", title: "Cloud vulnerabilities, threats and attacks" }
  - { id: "3.3.3", title: "Risk treatment strategies" }
  - { id: "3.4", title: "Plan and implementation of security controls" }
  - { id: "3.4.1", title: "Physical and environmental protection (on-premises)" }
  - { id: "3.4.2", title: "System, storage and communication protection" }
  - { id: "3.4.3", title: "Identification, authentication and authorization in cloud environments" }
  - { id: "3.4.4", title: "Audit mechanisms (log collection, correlation, packet capture)" }
  - { id: "3.5", title: "Plan business continuity (BC) and disaster recovery (DR)" }
  - { id: "3.5.1", title: "BC/DR strategy" }
  - { id: "3.5.2", title: "Business requirements (RTO, RPO, recovery service level)" }
  - { id: "3.5.3", title: "Creation, implementation and testing of the plan" }
  - { id: "4", title: "Cloud Application Security", weight: "16%" }
  - { id: "4.1", title: "Advocate training and awareness for application security" }
  - { id: "4.1.1", title: "Cloud development basics" }
  - { id: "4.1.2", title: "Common pitfalls" }
  - { id: "4.1.3", title: "Common cloud vulnerabilities (OWASP Top 10, ASVS, API Top 10, Top 10 for LLM Applications, SANS Top 25)" }
  - { id: "4.2", title: "Describe the secure software development life cycle (SDLC) process" }
  - { id: "4.2.1", title: "Business requirements" }
  - { id: "4.2.2", title: "Phases and methodologies (design, code, test, maintain, waterfall vs agile)" }
  - { id: "4.3", title: "Apply the secure SDLC" }
  - { id: "4.3.1", title: "Cloud-specific risks (shared technology, CSP insider threats, lack of visibility, legal and jurisdiction)" }
  - { id: "4.3.2", title: "Threat modeling (STRIDE, DREAD, ATASM, PASTA)" }
  - { id: "4.3.3", title: "Avoid common vulnerabilities during development" }
  - { id: "4.3.4", title: "Secure coding (OWASP ASVS, SAFECode)" }
  - { id: "4.3.5", title: "Software configuration management and versioning" }
  - { id: "4.4", title: "Apply cloud software assurance and validation" }
  - { id: "4.4.1", title: "Functional and non-functional testing (CI/CD processes)" }
  - { id: "4.4.2", title: "Security testing methodologies (blackbox, whitebox, SCA, IAST, SAST, DAST)" }
  - { id: "4.4.3", title: "Quality assurance (QA)" }
  - { id: "4.4.4", title: "Abuse case testing" }
  - { id: "4.5", title: "Use verified secure software" }
  - { id: "4.5.1", title: "Securing application programming interfaces (APIs)" }
  - { id: "4.5.2", title: "Supply-chain management (vendor assessment, integrity, authenticity, licensing)" }
  - { id: "4.5.3", title: "Third-party software management" }
  - { id: "4.5.4", title: "Validated open-source software" }
  - { id: "4.6", title: "Comprehend and apply the specifics of cloud application architecture" }
  - { id: "4.6.1", title: "Supplemental security components (WAF, DAM, XML firewalls, API gateway, load balancer)" }
  - { id: "4.6.2", title: "Cryptography" }
  - { id: "4.6.3", title: "Sandboxing" }
  - { id: "4.6.4", title: "Application virtualization and orchestration (microservices, containers, Docker, Kubernetes)" }
  - { id: "4.7", title: "Design appropriate identity and access management (IAM) solutions" }
  - { id: "4.7.1", title: "Federated identity" }
  - { id: "4.7.2", title: "Identity providers (IdP)" }
  - { id: "4.7.3", title: "Single sign-on (SSO)" }
  - { id: "4.7.4", title: "Multi-factor authentication (MFA)" }
  - { id: "4.7.5", title: "Cloud access security broker (CASB)" }
  - { id: "4.7.6", title: "Secrets, key and certificate management" }
  - { id: "5", title: "Cloud Security Operations", weight: "17%" }
  - { id: "5.1", title: "Build and implement physical and logical infrastructure for cloud environment" }
  - { id: "5.1.1", title: "Hardware-specific security configuration requirements (HSM, TPM)" }
  - { id: "5.1.2", title: "Secure by default" }
  - { id: "5.1.3", title: "Installation and configuration of management plane tools" }
  - { id: "5.1.4", title: "Virtual hardware security configuration (network, storage, memory, CPU, type 1 and 2 hypervisors)" }
  - { id: "5.1.5", title: "Installation of guest OS virtualization toolsets" }
  - { id: "5.2", title: "Operate and maintain physical and logical infrastructure for cloud environment" }
  - { id: "5.2.1", title: "Access controls for local and remote access (RDP, secure terminal, SSH, console, jumpboxes, virtual client, SSO)" }
  - { id: "5.2.2", title: "Secure network configuration (VLAN, TLS, DHCP, DNSSEC, VPN)" }
  - { id: "5.2.3", title: "Network security controls (firewalls, IDS, IPS, honeypots, vulnerability assessments, NSGs, bastion host, segmentation)" }
  - { id: "5.2.4", title: "OS hardening through baselines, monitoring and remediation (Windows, Linux, VMware)" }
  - { id: "5.2.5", title: "Patch management" }
  - { id: "5.2.6", title: "Availability of clustered hosts (distributed resource scheduling, dynamic optimization, storage clusters, maintenance mode, HA)" }
  - { id: "5.2.7", title: "Availability of guest OS" }
  - { id: "5.2.8", title: "Performance and capacity monitoring (network, compute, storage, response time)" }
  - { id: "5.2.9", title: "Hardware monitoring (disk, CPU, fan speed, temperature)" }
  - { id: "5.2.10", title: "Configuration of host and guest OS backup and restore functions" }
  - { id: "5.2.11", title: "Management plane (scheduling, orchestration, maintenance)" }
  - { id: "5.3", title: "Implement operational controls and standards (NIST, ISO, HIPAA, COBIT, CIS Controls, COSO, ITIL, ISO/IEC 20000-1)" }
  - { id: "5.3.1", title: "Change management" }
  - { id: "5.3.2", title: "Continuity management" }
  - { id: "5.3.3", title: "Information security management" }
  - { id: "5.3.4", title: "Continual service improvement management" }
  - { id: "5.3.5", title: "Incident management" }
  - { id: "5.3.6", title: "Problem management" }
  - { id: "5.3.7", title: "Release management" }
  - { id: "5.3.8", title: "Deployment management" }
  - { id: "5.3.9", title: "Configuration management (CM)" }
  - { id: "5.3.10", title: "Service-level management" }
  - { id: "5.3.11", title: "Availability management" }
  - { id: "5.3.12", title: "Capacity management" }
  - { id: "5.4", title: "Support digital forensics" }
  - { id: "5.4.1", title: "Forensic data collection methodologies" }
  - { id: "5.4.2", title: "Evidence management" }
  - { id: "5.4.3", title: "Collecting, acquiring and preserving digital evidence" }
  - { id: "5.5", title: "Manage communication with relevant parties" }
  - { id: "5.5.1", title: "Vendors" }
  - { id: "5.5.2", title: "Customers" }
  - { id: "5.5.3", title: "Partners" }
  - { id: "5.5.4", title: "Regulators" }
  - { id: "5.5.5", title: "Other stakeholders" }
  - { id: "5.6", title: "Manage security operations" }
  - { id: "5.6.1", title: "Security operations center (SOC)" }
  - { id: "5.6.2", title: "Intelligent monitoring of security controls (firewalls, IDS, IPS, honeypots, NSGs, AI)" }
  - { id: "5.6.3", title: "Log capture and analysis (SIEM, log management, threat intelligence)" }
  - { id: "5.6.4", title: "Incident response (IR)" }
  - { id: "5.6.5", title: "Vulnerability assessments" }
  - { id: "5.6.6", title: "Penetration testing" }
  - { id: "6", title: "Legal, Risk and Compliance", weight: "13%" }
  - { id: "6.1", title: "Articulate legal requirements and unique risks within the cloud environment" }
  - { id: "6.1.1", title: "Conflicting international legislation" }
  - { id: "6.1.2", title: "Evaluation of legal risks specific to cloud computing" }
  - { id: "6.1.3", title: "Legal and regulatory frameworks and guidelines" }
  - { id: "6.1.4", title: "eDiscovery (ISO/IEC 27050, CSA Guidance)" }
  - { id: "6.1.5", title: "Forensics requirements (CSA, ISO/IEC 27037, 27041, 27042, 27043)" }
  - { id: "6.2", title: "Understand privacy requirements" }
  - { id: "6.2.1", title: "Contractual vs regulated private data (PHI, PII)" }
  - { id: "6.2.2", title: "Country-specific privacy legislation (FERPA, PIPEDA, GDPR, HIPAA, Digital Personal Data Protection Act)" }
  - { id: "6.2.3", title: "Jurisdictional differences in data privacy" }
  - { id: "6.2.4", title: "Standard privacy requirements (ISO/IEC 27018, GAPP, GDPR)" }
  - { id: "6.2.5", title: "Privacy impact assessments (PIA)" }
  - { id: "6.3", title: "Understand audit processes, methodologies and required adaptations for a cloud environment" }
  - { id: "6.3.1", title: "Internal and external audit controls" }
  - { id: "6.3.2", title: "Impact of audit requirements" }
  - { id: "6.3.3", title: "Identify assurance challenges of virtualization and cloud" }
  - { id: "6.3.4", title: "Types of audit reports (SSAE, SOC, ISAE)" }
  - { id: "6.3.5", title: "Restrictions of audit scope statements (SSAE, ISAE)" }
  - { id: "6.3.6", title: "Gap analysis (control analysis, baselines, risk and control self-assessment)" }
  - { id: "6.3.7", title: "Audit planning" }
  - { id: "6.3.8", title: "Internal information security management system (ISMS)" }
  - { id: "6.3.9", title: "Internal information security controls system" }
  - { id: "6.3.10", title: "Policies (organizational, functional, cloud computing)" }
  - { id: "6.3.11", title: "Identification and involvement of relevant stakeholders" }
  - { id: "6.3.12", title: "Specialized compliance for highly regulated industries (NERC CIP, HIPAA, HITECH, PCI)" }
  - { id: "6.3.13", title: "Impact of the distributed IT model (geographies, crossing legal jurisdictions)" }
  - { id: "6.4", title: "Understand implications of cloud to enterprise risk management" }
  - { id: "6.4.1", title: "Assess providers' risk management programs (controls, methodologies, policies, risk profile, risk appetite)" }
  - { id: "6.4.2", title: "Difference between data roles (owner, controller, custodian, processor, steward)" }
  - { id: "6.4.3", title: "Regulatory transparency requirements (breach notification, SOX, GDPR)" }
  - { id: "6.4.4", title: "Risk treatment (avoid, mitigate, transfer, share, accept)" }
  - { id: "6.4.5", title: "Different risk frameworks" }
  - { id: "6.4.6", title: "Metrics for risk management" }
  - { id: "6.4.7", title: "Assessment of the risk environment (service, vendor, infrastructure, business)" }
  - { id: "6.5", title: "Understand outsourcing and cloud contract design" }
  - { id: "6.5.1", title: "Business requirements (SLA, MSA, SOW)" }
  - { id: "6.5.2", title: "Vendor management (assessments, lock-in risks, viability, escrow)" }
  - { id: "6.5.3", title: "Contract management (right to audit, metrics, termination, litigation, data ownership, cyber insurance and more)" }
  - { id: "6.5.4", title: "Supply-chain management (ISO/IEC 27036)" }
---
## Exam format

All facts below are as of 2026-10-24, from the [CCSP exam outline page](https://www.isc2.org/certifications/ccsp/ccsp-certification-exam-outline) and the [outline PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/EXAMS-CCSP-Exam-Outline-English-01-2026-V2.pdf) (effective August 1, 2026; file version 01-2026-V2), unless another link is given.

- **Question types.** Multiple choice and advanced item types.
- **Adaptive delivery.** Computerized Adaptive Testing (CAT) in English, Simplified Chinese, German and Japanese. The number of items you get depends on how you perform.
- **Number of items.** 100 to 150, with a 3-hour limit.
- **Passing score.** 700 out of 1000 scaled points.
- **Languages.** English, Chinese, German and Japanese. Chinese is offered only in select windows.
- **Delivery.** Pearson VUE test centres. Pearson charges USD 50 to reschedule and USD 100 to cancel ([scheduling page](https://www.isc2.org/exams/schedule-exam)).
- **Price.** USD 599 in the Americas and Asia-Pacific, EUR 575.04 in EMEA, on the [ISC2 exam pricing page](https://www.isc2.org/register-for-exam/isc2-exam-pricing). Other regions have their own local prices.
- **Retakes.** The [retake policy](https://www.isc2.org/exams/after-your-exam#retakePolicy) requires 30, 60 and then 90 test-free days between attempts, with at most four attempts in 12 months.
- **Experience and endorsement.** You need five years of IT experience, three of them in cybersecurity and one in a CCSP domain, plus an endorsement. CCSK waives one year. An active CISSP waives the whole requirement.
- **Renewal.** 90 CPE credits per three-year cycle (60 of them Group A) and the single USD 135 annual maintenance fee ([member policies](https://www.isc2.org/policies-procedures/member-policies), [AMF overview](https://www.isc2.org/policies-procedures/amfs-overview)).

The August 2026 outline replaces the August 2022 one. Compared with the [2022 outline PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/CCSP-Exam-Outline-August-2022-English.pdf), it adds two AI/ML subdomains (1.6 and 2.9), adds ASVS, the OWASP API Top 10 and the Top 10 for LLM Applications to 4.1, and adds India's Digital Personal Data Protection Act to 6.2. It drops DevSecOps from the related-technologies list in 1.2 and the Infrastructure as Code (IaC) strategy bullet from 5.2. Domain 4 drops from 17% to 16% and Domain 5 rises from 16% to 17%. The other weights are unchanged. The outline page also has a separate note on how AI security runs through every domain. Study material written for the 2022 outline predates these items, so check it against the new outline. Confirm format, price and the outline version before booking.

## What the exam really tests

CCSP asks you to be the security professional who sits between a cloud customer and its providers. Questions are vendor-neutral. You will never see "Azure Policy" or "AWS Config". You will see "the customer needs to verify that the provider meets its requirements". The exam rewards precise knowledge of:

- **Roles.** Who is responsible for what in each service model (SaaS, PaaS, IaaS), and in each data role (owner, controller, custodian, processor).
- **The cloud data life cycle.** Create, store, use, share, archive, destroy, and which control fits each phase: encryption, tokenization, masking, IRM, DLP, crypto-shredding.
- **Legal and contractual mechanics.** Conflicting jurisdictions, eDiscovery, legal hold, SOC 1/SOC 2/SOC 3 and ISAE 3402 reports, right to audit, SLAs vs MSAs vs SOWs, escrow and vendor lock-in.
- **Operations.** ITIL-style management processes, forensics in multi-tenant environments, hypervisor types, management-plane security and BC/DR with RTO and RPO.
- **Application security in the cloud.** Threat modelling methods (STRIDE, DREAD, PASTA, ATASM), testing types and API security.

Scenarios are often written from the customer's side: choosing a provider, writing a contract, responding to an incident when you cannot touch the hardware, or meeting GDPR when data replicates across regions. Many questions have more than one plausible answer. As with CISSP, the best answer is usually the one that respects governance and the shared-responsibility split.

Candidates lose points when they assume they can act like the provider (seize the server, install an agent on the hypervisor). They also mix up near-synonyms: anonymization vs pseudonymization vs masking vs tokenization, or SOC 2 Type I vs Type II. And they underrate Domain 6. Legal, Risk and Compliance is only 13%, but it is the domain engineers find least intuitive.

## Study strategy

1. **Start with Domain 1.** It sets the vocabulary every other domain assumes: NIST-style characteristics, ISO/IEC 17788/17789-style roles and capability types, deployment models and shared considerations. Then do Domain 2 (data, 20%, the heaviest), then Domains 3 and 5 (infrastructure and operations), then Domain 4 (applications), and finish with Domain 6 (legal).
2. **Official ISC2 resources.** ISC2 offers [CCSP Online Self-Paced Training](https://www.isc2.org/training/online-self-paced/ccsp-online-self-paced), online instructor-led and classroom training, and free self-study aids linked from the [CCSP page](https://www.isc2.org/certifications/ccsp). The outline cites CSA material (Security Guidance, CSA Enterprise Architecture), so [CSA Security Guidance v5](https://cloudsecurityalliance.org/artifacts/security-guidance-v5) is a natural companion, and it is also the basis of CCSK.
3. **Hands-on helps understanding, not answers.** Build the controls in Azure and AWS free tiers: customer-managed keys, an object-storage bucket with a lifecycle and legal-hold policy, a WAF in front of an app, and a log pipeline to a SIEM. Then describe each one in neutral words. CCSP will ask about the concept, never the console.
4. **Read primary standards in summary form.** Know what ISO/IEC 27017, 27018, 27036 and 27050, NIST SP 800-145 and the SSAE 18 SOC reports are for. You do not need to memorise them clause by clause.

**How your background helps or misleads.**

- **AZ-900** gives you the service and deployment models and shared responsibility.
- **AZ-204 prep** gives you Key Vault, managed identities, Blob Storage tiers and lifecycle, and API Management, which map to 2.3, 2.7, 4.5 and 4.7.
- **CKAD prep** maps to 1.3.5 and 4.6.4 (containers, Kubernetes, isolation).
- **Your .NET/Angular background** helps with Domain 4.

The trap is vendor reflex. In Azure, "the provider handles physical security" is a given. CCSP asks how you, as a customer, get assurance of it (audit reports, certifications, contract clauses), not whether it happens.

## Differences from related exams

- **CCSP vs CCSK.** [CCSK](https://cloudsecurityalliance.org/education/ccsk) is CSA's online, open-book knowledge test (60 questions, 80% to pass, no experience requirement) built on CSA Security Guidance v5. CCSP is a proctored, closed-book, adaptive exam of up to 150 items. It requires experience and endorsement and adds much more on legal and contracts, data-centre design, operations management (ITIL processes) and forensics. CCSK is good preparation, and it counts as one year of CCSP experience.
- **CCSP vs CISSP.** Same vendor, same format. CISSP spans all of security. CCSP drills into cloud and repeats some CISSP topics (BC/DR, crypto, SDLC, privacy law) from the cloud customer's angle.
- **CCSP vs AWS SCS-C03.** The AWS Security Specialty tests real AWS services and configurations: IAM policy evaluation, KMS key policies, GuardDuty, Security Hub and the logging architecture. CCSP never names a product but goes further into contracts, audit reports and jurisdiction. Together they cover the "what and why" and the "how on AWS".
- **CCSP vs Microsoft SC-100.** SC-100 designs security architecture using Microsoft's stack, including the Microsoft Cybersecurity Reference Architectures and the Defender and Entra product families. CCSP is the neutral equivalent for the cloud layer only and is weaker on identity-platform specifics.
- **CCSP vs Microsoft SC-500.** SC-500 implements security controls in Azure and Microsoft 365. CCSP sits a level above: governance and design, not implementation.

## Exam-day notes

- CAT gives you about 72 seconds per item, with no review and no going back. Answer, commit and move on.
- Mark the perspective in your head for every stem: customer, provider, broker or regulator. Many wrong answers are right for a different actor.
- Look for life-cycle cues ("before migration", "during contract negotiation", "after the breach"). The best answer is the one that fits that stage.
- For data questions, map the stem to the data life-cycle phase and the data role first, then choose the control.
- If two answers both reduce risk, prefer the one that gives verifiable assurance (an audit report, a contract clause, a key you control) over one that relies on trust.
- The exam is under an ISC2 non-disclosure agreement, so do not use or share recalled questions.
