---
code: CSSLP
title: "Certified Secure Software Lifecycle Professional"
credential: "CSSLP - Certified Secure Software Lifecycle Professional"
provider: isc2
tracks: [security]
clouds: [neutral]
level: professional
tier: elective
stage: "6"
progress: planned
official_url: https://www.isc2.org/certifications/csslp
study_guide_url: https://www.isc2.org/certifications/csslp/csslp-certification-exam-outline
outline_version: "2023-09-15"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "Four years of cumulative, full-time experience in one or more of the eight CSSLP domains. A relevant degree can waive one year. Passing without the experience makes you an Associate of ISC2, with five years to earn it."
replaces: ""
replaced_by: ""
counterparts: [gh-500]
objectives:
  - { id: "1", title: "Secure Software Concepts", weight: "12%" }
  - { id: "1.1", title: "Understand core concepts" }
  - { id: "1.1.1", title: "Confidentiality (encryption)" }
  - { id: "1.1.2", title: "Integrity (hashing, digital signatures, code signing, reliability, authenticity)" }
  - { id: "1.1.3", title: "Availability (redundancy, replication, clustering, scalability, resiliency)" }
  - { id: "1.1.4", title: "Authentication (MFA, IAM, SSO, federated identity, biometrics)" }
  - { id: "1.1.5", title: "Authorization (access controls, permissions, entitlements)" }
  - { id: "1.1.6", title: "Accountability (auditing, logging)" }
  - { id: "1.1.7", title: "Nonrepudiation (digital signatures, blockchain)" }
  - { id: "1.1.8", title: "Governance, risk and compliance (GRC) standards (regulatory, legal, industry)" }
  - { id: "1.2", title: "Understand security design principles" }
  - { id: "1.2.1", title: "Least privilege (access control, need-to-know, run-time privileges, Zero Trust)" }
  - { id: "1.2.2", title: "Segregation of duties (multi-party control, secret sharing, split knowledge)" }
  - { id: "1.2.3", title: "Defense in depth (layered controls, geographical and technical diversity, distributed systems)" }
  - { id: "1.2.4", title: "Resiliency (fail safe, fail secure, no single point of failure, failover)" }
  - { id: "1.2.5", title: "Economy of mechanism (SSO, password vaults, resource efficiency)" }
  - { id: "1.2.6", title: "Complete mediation (cookie management, session management, caching of credentials)" }
  - { id: "1.2.7", title: "Open design (Kerckhoffs's principle, peer review, open source, crowd source)" }
  - { id: "1.2.8", title: "Least common mechanism (compartmentalization/isolation, allow list)" }
  - { id: "1.2.9", title: "Psychological acceptability (password complexity, passwordless, screen layouts, CAPTCHA)" }
  - { id: "1.2.10", title: "Component reuse (common controls, libraries)" }
  - { id: "2", title: "Secure Software Lifecycle Management", weight: "11%" }
  - { id: "2.1", title: "Manage security within a software development methodology (Agile, waterfall)" }
  - { id: "2.2", title: "Identify and adopt security standards (implementing frameworks, promoting awareness)" }
  - { id: "2.3", title: "Outline strategy and roadmap" }
  - { id: "2.3.1", title: "Security milestones and checkpoints (control gate, break/build criteria)" }
  - { id: "2.4", title: "Define and develop security documentation" }
  - { id: "2.5", title: "Define security metrics (criticality level, average remediation time, complexity, KPIs, OKRs)" }
  - { id: "2.6", title: "Decommission applications" }
  - { id: "2.6.1", title: "End-of-life policies (credential and configuration removal, license cancellation, archiving, SLAs)" }
  - { id: "2.6.2", title: "Data disposition (retention, destruction, dependencies)" }
  - { id: "2.7", title: "Create security reporting mechanisms (reports, dashboards, feedback loops)" }
  - { id: "2.8", title: "Incorporate integrated risk management methods" }
  - { id: "2.8.1", title: "Regulations, standards and guidelines (ISO, PCI, NIST, OWASP, SAFECode, SAMM, BSIMM)" }
  - { id: "2.8.2", title: "Legal (intellectual property, breach notification)" }
  - { id: "2.8.3", title: "Risk management (risk assessment, risk analysis)" }
  - { id: "2.8.4", title: "Technical risk vs business risk" }
  - { id: "2.9", title: "Implement secure operation practices" }
  - { id: "2.9.1", title: "Change management process" }
  - { id: "2.9.2", title: "Incident response plan" }
  - { id: "2.9.3", title: "Verification and validation" }
  - { id: "2.9.4", title: "Assessment and authorization (A&A) process" }
  - { id: "3", title: "Secure Software Requirements", weight: "13%" }
  - { id: "3.1", title: "Define software security requirements" }
  - { id: "3.1.1", title: "Functional (business requirements, use cases, stories)" }
  - { id: "3.1.2", title: "Non-functional (security, operational, continuity, deployment)" }
  - { id: "3.2", title: "Identify compliance requirements" }
  - { id: "3.2.1", title: "Regulatory authority" }
  - { id: "3.2.2", title: "Legal" }
  - { id: "3.2.3", title: "Industry-specific (defense, healthcare, commercial, financial, PCI)" }
  - { id: "3.2.4", title: "Company-wide (development tools, standards, frameworks, protocols)" }
  - { id: "3.3", title: "Identify data classification requirements" }
  - { id: "3.3.1", title: "Data ownership (data dictionary, data owner, data custodian)" }
  - { id: "3.3.2", title: "Data labeling (sensitivity, impact)" }
  - { id: "3.3.3", title: "Data types (structured, unstructured)" }
  - { id: "3.3.4", title: "Data lifecycle (generation, storage, retention, disposal)" }
  - { id: "3.3.5", title: "Data handling (PII, publicly available information)" }
  - { id: "3.4", title: "Identify privacy requirements" }
  - { id: "3.4.1", title: "Data collection scope" }
  - { id: "3.4.2", title: "Data anonymization (pseudo-anonymous, fully anonymous)" }
  - { id: "3.4.3", title: "User rights and preferences (data disposal, right to be forgotten, marketing preferences, third parties, terms of service)" }
  - { id: "3.4.4", title: "Data retention (how long, where, what)" }
  - { id: "3.4.5", title: "Cross-border requirements (data residency, jurisdiction, multi-national processing boundaries)" }
  - { id: "3.5", title: "Define data access provisioning" }
  - { id: "3.5.1", title: "User provisioning" }
  - { id: "3.5.2", title: "Service accounts" }
  - { id: "3.5.3", title: "Reapproval process" }
  - { id: "3.6", title: "Develop misuse and abuse cases" }
  - { id: "3.6.1", title: "Mitigating control identification" }
  - { id: "3.7", title: "Develop a security requirement traceability matrix" }
  - { id: "3.8", title: "Define third-party vendor security requirements" }
  - { id: "4", title: "Secure Software Architecture and Design", weight: "15%" }
  - { id: "4.1", title: "Define the security architecture" }
  - { id: "4.1.1", title: "Secure architecture and design patterns (SABSA, security chain of responsibility, federated identity)" }
  - { id: "4.1.2", title: "Security controls identification and prioritization" }
  - { id: "4.1.3", title: "Distributed computing (client-server, P2P, message queuing, N-tier)" }
  - { id: "4.1.4", title: "Service-oriented architecture (enterprise service bus, web services, microservices)" }
  - { id: "4.1.5", title: "Rich internet applications (client-side exploits, remote code execution, constant connectivity)" }
  - { id: "4.1.6", title: "Pervasive/ubiquitous computing (IoT, wireless, location-based, RFID, NFC, sensor networks, mesh)" }
  - { id: "4.1.7", title: "Embedded software (secure boot, secure memory, secure update)" }
  - { id: "4.1.8", title: "Cloud architectures (SaaS, PaaS, IaaS)" }
  - { id: "4.1.9", title: "Mobile applications (implicit data collection privacy)" }
  - { id: "4.1.10", title: "Hardware platform concerns (side-channel and speculative execution mitigation, secure element, firmware, drivers)" }
  - { id: "4.1.11", title: "Cognitive computing (AI, virtual reality, augmented reality)" }
  - { id: "4.1.12", title: "Industrial IoT (facilities, automotive, robotics, medical devices, software-defined production)" }
  - { id: "4.2", title: "Perform secure interface design" }
  - { id: "4.2.1", title: "Security management interfaces, out-of-band management, log interfaces" }
  - { id: "4.2.2", title: "Upstream/downstream dependencies (key and data sharing between apps)" }
  - { id: "4.2.3", title: "Protocol design choices (APIs, weaknesses, state, models)" }
  - { id: "4.3", title: "Evaluate and select reusable technologies" }
  - { id: "4.3.1", title: "Credential management (X.509, SSO)" }
  - { id: "4.3.2", title: "Flow control (proxies, firewalls, protocols, queuing)" }
  - { id: "4.3.3", title: "Data loss prevention (DLP)" }
  - { id: "4.3.4", title: "Virtualization (infrastructure as code, hypervisor, containers)" }
  - { id: "4.3.5", title: "Trusted computing (TPM, trusted computing base)" }
  - { id: "4.3.6", title: "Database security (encryption, triggers, views, privilege management, secure connections)" }
  - { id: "4.3.7", title: "Programming language environment (common language runtime, Java VM, Python, PowerShell)" }
  - { id: "4.3.8", title: "Operating system controls and services" }
  - { id: "4.3.9", title: "Secure backup and restoration planning" }
  - { id: "4.3.10", title: "Secure data retention, retrieval and destruction" }
  - { id: "4.4", title: "Perform threat modeling" }
  - { id: "4.4.1", title: "Threat modeling methodologies (STRIDE, PASTA, Hybrid Threat Modeling Method, CVSS)" }
  - { id: "4.4.2", title: "Common threats (APT, insider threat, common malware, third-party suppliers)" }
  - { id: "4.4.3", title: "Attack surface evaluation" }
  - { id: "4.4.4", title: "Threat analysis" }
  - { id: "4.4.5", title: "Threat intelligence (identify credible relevant threats, predict)" }
  - { id: "4.5", title: "Perform architectural risk assessment and design reviews" }
  - { id: "4.6", title: "Model (non-functional) security properties and constraints" }
  - { id: "4.7", title: "Define secure operational architecture (deployment topology, operational interfaces, CI/CD)" }
  - { id: "5", title: "Secure Software Implementation", weight: "14%" }
  - { id: "5.1", title: "Adhere to relevant secure coding practices (standards, guidelines, regulations)" }
  - { id: "5.1.1", title: "Declarative vs imperative (programmatic) security" }
  - { id: "5.1.2", title: "Concurrency (thread safety, database concurrency controls)" }
  - { id: "5.1.3", title: "Input validation and sanitization" }
  - { id: "5.1.4", title: "Error and exception handling" }
  - { id: "5.1.5", title: "Output sanitization (encoding, obfuscation)" }
  - { id: "5.1.6", title: "Secure logging and auditing (confidentiality, privacy)" }
  - { id: "5.1.7", title: "Session management" }
  - { id: "5.1.8", title: "Trusted/untrusted APIs and libraries" }
  - { id: "5.1.9", title: "Resource management (compute, storage, network, memory)" }
  - { id: "5.1.10", title: "Secure configuration management (baseline configuration, credentials management)" }
  - { id: "5.1.11", title: "Tokenization" }
  - { id: "5.1.12", title: "Isolation (sandboxing, virtualization, containerization, separation kernel protection profiles)" }
  - { id: "5.1.13", title: "Cryptography (payload, field level, transport, storage, agility, algorithm selection)" }
  - { id: "5.1.14", title: "Access control (trust zones, function permissions, RBAC, DAC, MAC)" }
  - { id: "5.1.15", title: "Processor microarchitecture security extensions" }
  - { id: "5.2", title: "Analyze code for security risks" }
  - { id: "5.2.1", title: "Secure code reuse" }
  - { id: "5.2.2", title: "Vulnerability databases/lists (OWASP Top 10, CWE, SANS Top 25)" }
  - { id: "5.2.3", title: "Static application security testing (automated code coverage, linting)" }
  - { id: "5.2.4", title: "Manual code review (peer review)" }
  - { id: "5.2.5", title: "Inspect for malicious code (backdoors, logic bombs, high entropy)" }
  - { id: "5.3", title: "Implement security controls (watchdogs, file integrity monitoring, anti-malware)" }
  - { id: "5.4", title: "Address the identified security risks (risk strategy)" }
  - { id: "5.5", title: "Evaluate and integrate components" }
  - { id: "5.5.1", title: "Systems-of-systems integration (trust contracts, security testing, analysis)" }
  - { id: "5.5.2", title: "Reuse third-party code or open-source libraries securely (software composition analysis)" }
  - { id: "5.6", title: "Apply security during the build process" }
  - { id: "5.6.1", title: "Anti-tampering techniques (code signing, obfuscation)" }
  - { id: "5.6.2", title: "Compiler switches" }
  - { id: "5.6.3", title: "Address compiler warnings" }
  - { id: "6", title: "Secure Software Testing", weight: "14%" }
  - { id: "6.1", title: "Develop a security testing strategy and plan" }
  - { id: "6.1.1", title: "Standards (ISO, OSSTMM, Software Engineering Institute)" }
  - { id: "6.1.2", title: "Functional security testing (logic)" }
  - { id: "6.1.3", title: "Nonfunctional security testing (reliability, performance, scalability)" }
  - { id: "6.1.4", title: "Testing techniques (known/unknown environment, functional, acceptance)" }
  - { id: "6.1.5", title: "Testing environment (interoperability, test harness)" }
  - { id: "6.1.6", title: "Security researcher outreach (bug bounties)" }
  - { id: "6.2", title: "Develop security test cases" }
  - { id: "6.2.1", title: "Attack surface validation" }
  - { id: "6.2.2", title: "Automated vulnerability testing (DAST, IAST)" }
  - { id: "6.2.3", title: "Penetration tests (security controls, known vulnerabilities, known malware)" }
  - { id: "6.2.4", title: "Fuzzing (generated, mutated)" }
  - { id: "6.2.5", title: "Simulation (production environment and data, synthetic transactions)" }
  - { id: "6.2.6", title: "Failure (fault injection, stress testing, break testing)" }
  - { id: "6.2.7", title: "Cryptographic validation (pseudorandom number generators, entropy)" }
  - { id: "6.2.8", title: "Unit testing and code coverage" }
  - { id: "6.2.9", title: "Regression tests" }
  - { id: "6.2.10", title: "Integration tests" }
  - { id: "6.2.11", title: "Continuous testing" }
  - { id: "6.2.12", title: "Misuse and abuse test cases" }
  - { id: "6.3", title: "Verify and validate documentation (installation instructions, error messages, user guides, release notes)" }
  - { id: "6.4", title: "Identify undocumented functionality" }
  - { id: "6.5", title: "Analyze security implications of test results (product management impact, prioritization, break/build criteria)" }
  - { id: "6.6", title: "Classify and track security errors" }
  - { id: "6.6.1", title: "Bug tracking (defects, errors, vulnerabilities)" }
  - { id: "6.6.2", title: "Risk scoring (CVSS)" }
  - { id: "6.7", title: "Secure test data" }
  - { id: "6.7.1", title: "Generate test data (referential integrity, statistical quality, production representative)" }
  - { id: "6.7.2", title: "Reuse of production data (obfuscation, sanitization, anonymization, tokenization, aggregation mitigation)" }
  - { id: "6.8", title: "Perform verification and validation testing (independent/internal V&V, acceptance test)" }
  - { id: "7", title: "Secure Software Deployment, Operations, Maintenance", weight: "11%" }
  - { id: "7.1", title: "Perform operational risk analysis" }
  - { id: "7.1.1", title: "Deployment environment (staging, production, QA)" }
  - { id: "7.1.2", title: "Personnel training (administrators vs users)" }
  - { id: "7.1.3", title: "Legal compliance (guidelines, regulations, privacy laws, copyright)" }
  - { id: "7.1.4", title: "System integration" }
  - { id: "7.2", title: "Secure configuration and version control" }
  - { id: "7.2.1", title: "Hardware" }
  - { id: "7.2.2", title: "Baseline configuration" }
  - { id: "7.2.3", title: "Version control/patching" }
  - { id: "7.2.4", title: "Documentation practices" }
  - { id: "7.3", title: "Release software securely" }
  - { id: "7.3.1", title: "Secure CI/CD pipeline (DevSecOps)" }
  - { id: "7.3.2", title: "Application security toolchain" }
  - { id: "7.3.3", title: "Build artifact verification (code signing, hashes)" }
  - { id: "7.4", title: "Store and manage security data" }
  - { id: "7.4.1", title: "Credentials" }
  - { id: "7.4.2", title: "Secrets" }
  - { id: "7.4.3", title: "Keys/certificates" }
  - { id: "7.4.4", title: "Configurations" }
  - { id: "7.5", title: "Ensure secure installation" }
  - { id: "7.5.1", title: "Secure boot (key generation, access, management)" }
  - { id: "7.5.2", title: "Least privilege" }
  - { id: "7.5.3", title: "Environment hardening (configuration hardening, secure patches/updates, firewall)" }
  - { id: "7.5.4", title: "Secure provisioning (credentials, configuration, licensing, infrastructure as code)" }
  - { id: "7.5.5", title: "Security policy implementation" }
  - { id: "7.6", title: "Obtain security approval to operate (risk acceptance, sign-off at the appropriate level)" }
  - { id: "7.7", title: "Perform information security continuous monitoring" }
  - { id: "7.7.1", title: "Observable data (logs, events, telemetry, trace data, metrics)" }
  - { id: "7.7.2", title: "Threat intelligence" }
  - { id: "7.7.3", title: "Intrusion detection/response" }
  - { id: "7.7.4", title: "Regulation and privacy changes" }
  - { id: "7.7.5", title: "Integration analysis (SIEM)" }
  - { id: "7.8", title: "Execute the incident response plan" }
  - { id: "7.8.1", title: "Incident triage" }
  - { id: "7.8.2", title: "Forensics" }
  - { id: "7.8.3", title: "Remediation" }
  - { id: "7.8.4", title: "Root cause analysis" }
  - { id: "7.9", title: "Perform patch management (secure release, testing)" }
  - { id: "7.10", title: "Perform vulnerability management (tracking, triaging, CVE)" }
  - { id: "7.11", title: "Incorporate runtime protection (RASP, WAF, ASLR, dynamic execution prevention)" }
  - { id: "7.12", title: "Support continuity of operations" }
  - { id: "7.12.1", title: "Backup, archiving, retention" }
  - { id: "7.12.2", title: "Disaster recovery plan (DRP)" }
  - { id: "7.12.3", title: "Resiliency (operational redundancy, erasure code, survivability, DoS)" }
  - { id: "7.12.4", title: "Business continuity plan (BCP)" }
  - { id: "7.13", title: "Integrate service-level objectives and SLAs (maintenance, performance, availability, qualified personnel)" }
  - { id: "8", title: "Secure Software Supply Chain", weight: "10%" }
  - { id: "8.1", title: "Implement software supply chain risk management (ISO, NIST)" }
  - { id: "8.1.1", title: "Identification and selection of components" }
  - { id: "8.1.2", title: "Risk assessment of components (mitigate, accept)" }
  - { id: "8.1.3", title: "Maintaining a third-party components list (software bill of materials)" }
  - { id: "8.1.4", title: "Monitoring for changes and vulnerabilities" }
  - { id: "8.2", title: "Analyze security of third-party software" }
  - { id: "8.2.1", title: "Certifications" }
  - { id: "8.2.2", title: "Assessment reports (e.g. Cloud Controls Matrix)" }
  - { id: "8.2.3", title: "Origin and support" }
  - { id: "8.3", title: "Verify pedigree and provenance" }
  - { id: "8.3.1", title: "Secure transfer (chain of custody, authenticity, integrity)" }
  - { id: "8.3.2", title: "System sharing/interconnections" }
  - { id: "8.3.3", title: "Code repository security" }
  - { id: "8.3.4", title: "Build environment security" }
  - { id: "8.3.5", title: "Cryptographically hashed, digitally signed components" }
  - { id: "8.3.6", title: "Right to audit" }
  - { id: "8.4", title: "Ensure and verify supplier security requirements in the acquisition process" }
  - { id: "8.4.1", title: "Audit of security policy compliance (secure development practices)" }
  - { id: "8.4.2", title: "Vulnerability/incident notification, response, coordination and reporting" }
  - { id: "8.4.3", title: "Maintenance and support structure (community vs commercial, licensing)" }
  - { id: "8.4.4", title: "Security track record" }
  - { id: "8.4.5", title: "Scope of testing (shared responsibility model)" }
  - { id: "8.4.6", title: "Log integration into SIEM" }
  - { id: "8.5", title: "Support contractual requirements (IP ownership, code escrow, liability, warranty, EULA, SLAs)" }
---
## Exam format

All facts below are as of 2026-10-24, from the [CSSLP exam outline page](https://www.isc2.org/certifications/csslp/csslp-certification-exam-outline) and its [outline PDF](https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/CSSLP-Exam-Outline-November-2023-English.pdf) (effective September 15, 2023), unless another link is given.

- **Question types.** Multiple choice and advanced item types. CSSLP is a fixed-length exam. ISC2 uses Computerized Adaptive Testing only for CC, SSCP, CISSP and CCSP ([CAT page](https://www.isc2.org/certifications/computerized-adaptive-testing)).
- **Number of items.** 125, with a 3-hour limit.
- **Passing score.** 700 out of 1000 scaled points.
- **Language.** English only.
- **Delivery.** Pearson VUE test centres. Pearson charges USD 50 to reschedule and USD 100 to cancel ([scheduling page](https://www.isc2.org/exams/schedule-exam)).
- **Price.** USD 599 in the Americas on the [ISC2 exam pricing page](https://www.isc2.org/register-for-exam/isc2-exam-pricing). Prices vary by region.
- **Retakes.** The [retake policy](https://www.isc2.org/exams/after-your-exam#retakePolicy) requires 30, 60 and then 90 test-free days between attempts, with at most four attempts in 12 months.
- **Experience.** Four years of cumulative, full-time experience in one or more of the eight domains. A relevant bachelor's or master's degree can waive one year. Without the experience you become an Associate of ISC2 and have five years to earn it.
- **Renewal.** 90 CPE credits per three-year cycle (60 of them Group A) and the single USD 135 annual maintenance fee ([member policies](https://www.isc2.org/policies-procedures/member-policies), [AMF overview](https://www.isc2.org/policies-procedures/amfs-overview)).

The September 2023 outline is still current as of 2026-10-24. The outline page announces no replacement, and ISC2's [July 2025 outline update](https://www.isc2.org/Insights/2025/07/new-exam-outlines-for-isc2-advanced-certifications) covered only ISSAP, ISSEP and ISSMP. Confirm the outline date, price and format before booking.

## What the exam really tests

CSSLP asks how security is built into every phase of a software product's life. That runs from the concepts and the programme around them, through requirements, design, code, test and release, to operations, decommissioning and the supply chain. It is a process exam, not a coding test. You will not read code. You will judge which practice, artifact or gate belongs where, and who is accountable.

Typical themes:

- **Design principles as Saltzer and Schroeder named them.** Complete mediation, least common mechanism, economy of mechanism and psychological acceptability. You must recognise each from a scenario.
- **Requirements engineering.** Functional vs non-functional requirements, misuse and abuse cases, the requirements traceability matrix, data classification and privacy requirements.
- **Threat modelling and design review.** STRIDE, PASTA and CVSS, attack surface evaluation, and where in the SDLC each happens.
- **Testing.** The many kinds (SAST, DAST, IAST, fuzzing, pen testing, regression, V&V), what each finds, and how to protect test data.
- **Release and operations.** Code signing, build artifact verification, secrets storage, approval to operate, RASP and WAF, and patch and vulnerability management.
- **Supply chain.** SBOM, pedigree and provenance, supplier requirements and contract terms such as code escrow.

Candidates lose points when they answer like a developer ("add input validation") when the question asks for a lifecycle-management action ("update the requirements and traceability matrix, then re-test"). They also confuse similar testing types and principles, and they neglect Domains 2 and 8 (lifecycle management and supply chain), which developers rarely meet day to day.

## Study strategy

1. **Concepts first.** Learn Domain 1 thoroughly. The ten design principles and the core properties reappear in every later domain. Then work through Domains 3 to 7 in SDLC order (requirements, design, implementation, testing, deployment and operations), so each phase's outputs feed the next. Do Domain 2 (programme management) and Domain 8 (supply chain) last, because they wrap around the whole life cycle.
2. **Official ISC2 resources.** ISC2 offers [CSSLP Online Self-Paced Training](https://www.isc2.org/training/online-self-paced/csslp-online-self-paced), instructor-led options and self-study aids linked from the [CSSLP page](https://www.isc2.org/certifications/csslp), plus the [supplementary references list](https://www.isc2.org/certifications/references).
3. **Primary references named in the outline.** The outline names OWASP (including the OWASP Top 10), SAFECode, SAMM and BSIMM, and the CWE and SANS Top 25 lists. Read each at summary level and know what it is for.
4. **Hands-on that pays off.** Run your own .NET/Angular project through a full secure pipeline. Write a STRIDE threat model, enable SAST and dependency scanning (software composition analysis), generate an SBOM, sign the build artifact, store secrets in a vault, add a DAST scan against staging and write the release sign-off. Then map each step to an outline item. This makes the abstract Domains 2, 7 and 8 concrete.

**How your background helps or misleads.**

- **Your .NET/Angular and AZ-204 experience** gives you a head start on Domains 4 to 7: Key Vault, managed identities, App Service deployment slots, CI/CD.
- **CKAD prep** helps with containerisation and isolation (5.1.12) and secure provisioning.

The trap is relying on habit. Your team's process may skip formal requirements traceability, abuse cases, approval to operate or decommissioning, and CSSLP tests exactly those formal steps. Don't trust "how we do it at work". Answer from the outline's life cycle.

## Differences from related exams

- **CSSLP vs CISSP Domain 8.** CISSP gives software development security 10% and treats it at a manager's survey level. CSSLP spends a whole exam on it, with eight domains and 58 objectives. It expects you to place specific practices (fuzzing, traceability matrices, compiler switches, code escrow) in the right phase.
- **CSSLP vs GitHub Advanced Security (GH-500).** GH-500 tests one toolset in depth: CodeQL code scanning, secret scanning, Dependabot and dependency review, and security overview. CSSLP is tool-neutral and covers the process those tools sit in, including requirements, design reviews, release approval, operations and supplier contracts.
- **CSSLP vs CCSP Domain 4.** CCSP's cloud application security domain (16%) covers the secure SDLC from a cloud customer's view: threat modelling, testing types, API security and IAM. CSSLP covers all of that in more depth, plus the programme, operations and supply chain.
- **CSSLP vs CompTIA CySA+ / PenTest+.** Those exams are operational and offensive: finding and responding to vulnerabilities. CSSLP is about preventing them through the life cycle.
- **CSSLP vs ISSAP.** ISSAP designs the security architecture of systems and IAM. CSSLP designs the security process of building software. They overlap only in threat modelling and design review.

## Exam-day notes

- 125 items in 180 minutes gives you about 86 seconds each. Keep a steady pace so the last items get the same attention as the first.
- Identify the SDLC phase in every stem first ("during requirements gathering", "before release", "after deployment"). The right answer is almost always the activity that belongs to that phase.
- When several answers are good practice, pick the one that is earliest in the life cycle and addresses the root cause. Fixing requirements beats fixing code, and fixing code beats adding a WAF.
- Learn the near-twins cold: SAST vs DAST vs IAST vs SCA, fail safe vs fail secure, pseudonymization vs anonymization, verification vs validation.
- The exam is under an ISC2 non-disclosure agreement, so do not use or share recalled questions.
