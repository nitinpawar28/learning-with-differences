---
code: OSAI
title: "OffSec AI Red Teamer (AI-300 Advanced AI Red Teaming)"
credential: "OffSec AI Red Teamer (OSAI / OSAI+)"
provider: offsec
tracks: [security, agentic-ai]
clouds: [neutral]
level: advanced
tier: elective
stage: "6"
progress: planned
official_url: https://www.offsec.com/courses/ai-300/
study_guide_url: https://cdn.sanity.io/files/t7y0tkf4/production/024258d4bfacd78f94e3565a3657894842f68061.pdf
outline_version: "AI-300 syllabus (2026)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. OffSec recommends penetration-testing, networking, Linux/Windows and scripting experience, OSCP or equivalent."
replaces: ""
replaced_by: ""
counterparts: []
objectives:
  - { id: "1", title: "Introduction to Red Teaming AI Systems" }
  - { id: "1.1", title: "How artificial intelligence systems change the traditional attack surface" }
  - { id: "1.2", title: "Core concepts of AI cybersecurity and how adversaries target AI-enabled environments" }
  - { id: "1.3", title: "Mapping AI attacks to the red team lifecycle" }
  - { id: "2", title: "Reconnaissance for AI Targets" }
  - { id: "2.1", title: "Identifying and mapping AI applications, machine learning components and model infrastructure within a target environment" }
  - { id: "2.2", title: "Reconnaissance techniques to discover AI assets, dependencies and exposed services without alerting defenders" }
  - { id: "3", title: "Attacking AI Agents" }
  - { id: "3.1", title: "Manipulating AI agents by abusing prompt instructions, memory systems and tool integrations" }
  - { id: "3.2", title: "Influencing autonomous AI applications while maintaining stealth" }
  - { id: "4", title: "Attacking Multi-Agent Systems and A2A Protocols" }
  - { id: "4.1", title: "Architecture of multi-agent AI systems and exploiting trust relationships between agents" }
  - { id: "4.2", title: "Message manipulation, agent impersonation and workflow corruption" }
  - { id: "5", title: "Exploiting RAG Pipelines" }
  - { id: "5.1", title: "Poisoning knowledge sources and manipulating retrieval layers to control model outputs" }
  - { id: "6", title: "Attacking Embeddings" }
  - { id: "6.1", title: "The role of embeddings in machine learning systems" }
  - { id: "6.2", title: "Embedding inversion and information extraction to recover sensitive data from AI models" }
  - { id: "7", title: "Attacking Model Context Protocol and Tool Surfaces" }
  - { id: "7.1", title: "Abusing orchestration layers and AI tool-integration frameworks to escalate privileges or execute unintended actions" }
  - { id: "8", title: "Supply Chain Attacks on AI/ML Systems" }
  - { id: "8.1", title: "Targeting the AI supply chain: datasets, model weights, adapters and dependencies" }
  - { id: "8.2", title: "Introducing malicious artifacts into AI environments before deployment" }
  - { id: "9", title: "AI Infrastructure and Deployment Exploits" }
  - { id: "9.1", title: "Vulnerabilities in cloud AI platforms, model servers and containerized machine learning workloads" }
  - { id: "10", title: "Threat Modeling for AI-Enabled Targets" }
  - { id: "10.1", title: "Identifying high-value AI assets, trust boundaries and potential attack paths in complex AI environments" }
  - { id: "11", title: "Assembling The Pieces - Capstone Red Team Engagement" }
  - { id: "11.1", title: "Full-spectrum red team engagement against a realistic enterprise AI environment, simulating how adversaries compromise production AI systems" }
---
## About this entry

OffSec does not give its exams codes. The certification is the **OffSec AI Red Teamer (OSAI)**, earned by passing the practical exam that comes with the **AI-300: Advanced AI Red Teaming** course. This library uses **OSAI** as the code. Because the exam is a practical engagement with no published blueprint, **the objectives above are the eleven modules of the official [AI-300 syllabus](https://cdn.sanity.io/files/t7y0tkf4/production/024258d4bfacd78f94e3565a3657894842f68061.pdf)**, in syllabus order, with no weights. Each module's second-level entries name only the activities the syllabus itself names.

## Exam format

All facts in this section are as of 2026-10-24. They come from the [AI-300 course page](https://www.offsec.com/courses/ai-300/), the [OSAI Exam Guide](https://help.offsec.com/hc/en-us/articles/46593096734612-OSAI-Exam-Guide) (last updated October 22, 2026) and the [OSAI exam FAQ](https://help.offsec.com/hc/en-us/articles/46669767163156-OSAI-Advanced-AI-Red-Teaming-Exam-FAQ).

| Item | OSAI |
|---|---|
| Exam type | A practical, proctored red-team engagement against an AI-enabled enterprise lab |
| Duration | 24 hours in the lab, then another **24 hours to submit the report**. A late report fails automatically. |
| Environment | Ten machines: two attack chains of three machines each, a standalone AI-focused host, a domain controller, and two machines that are deliberately not vulnerable |
| Scoring | 100 points across eight scored targets: AI-vector machines 15 each, traditional-vector machines 10 each, the standalone AI host 15, the domain-controller flag 5 (it counts once). **75 points to pass.** Points depend on the proof *and* on how complete the report is. |
| Resources | Open book with no tool restrictions. Using AI and LLM assistants is explicitly encouraged. Getting help from other people is forbidden. |
| Results | Pass or fail, within ten business days of submission |
| Price | Course + Cert Bundle at US$1,749 once (90 days of course and labs, one exam attempt), or Learn One at US$2,749 a year, auto-renewing (one year of access and two exam attempts) |
| First exam date | The FAQ says the earliest exam slot opened was July 15, 2026 |
| Validity | OSAI does not expire. The **OSAI+** designation lasts three years and is renewed by a recertification exam, another qualifying OffSec exam (OSEP, OSWA, OSED or OSEE) or OffSec's CPE program. |
| Recommended experience | Penetration testing, networking, Linux and Windows, and basic scripting. OSCP or equivalent hands-on experience is recommended. Prior AI or ML knowledge helps but is not required. |

The course page lists 65 hours of content and estimates 50–100 hours of study before the exam. Check the exam guide again just before you book, because OffSec revises it often.

## What the exam really tests

OSAI tests whether you can carry out and document a complete offensive assessment of an organization that runs AI systems alongside ordinary infrastructure. The environment combines **AI-focused and traditional attack vectors**, so you need both your existing penetration-testing skills and the AI-specific material from the course. The eleven syllabus modules are:

1. introduction to red teaming AI systems
2. reconnaissance for AI targets
3. AI agents
4. multi-agent systems and agent-to-agent (A2A) protocols
5. RAG pipelines
6. embeddings
7. Model Context Protocol (MCP) and tool surfaces
8. the AI/ML supply chain
9. AI infrastructure and deployment
10. threat modeling for AI-enabled targets
11. a capstone engagement

The **report** carries as much weight as the exploitation. The exam guide requires every step, command, script and screenshot, documented so that a competent reader could reproduce your work. Missing proof or documentation costs points or zeroes a target. OSAI is also unusual among OffSec exams in **encouraging AI assistance** during the exam. Being able to direct an assistant well is part of what is assessed.

**Where candidates lose points:**

- **Weak documentation.** Proof is captured but the report is incomplete, or the proof does not appear both in the control panel and in a screenshot.
- **Running out of energy or time** in a 24-hour window, followed by a rushed report.
- **Neglecting the traditional vectors.** They are worth fewer points each, but the chains depend on them.
- **Breaking the rules.** Copying files out of the exam environment or seeking help is forbidden.

## Study strategy

**Order of study:**

1. **Penetration-testing foundations first.** OffSec recommends OSCP-level experience. If you do not have it, the traditional half of this exam will be the obstacle, not the AI half.
2. **AI system architecture.** Understand how LLM applications, agents, RAG, embeddings, vector databases, MCP servers and model hosting fit together. Your developer background helps most here.
3. **The AI-300 modules in syllabus order,** finishing each module's labs before you move on.
4. **The capstone engagement,** run as a rehearsal under a 24-hour clock, including writing the full report.
5. **A report template.** Prepare and practise it before the exam. The exam guide suggests Word or LibreOffice templates, and the file must be a PDF inside a .7z archive with exact naming.

**Official learning resources.** The [AI-300 course](https://www.offsec.com/courses/ai-300/) itself, with its on-demand labs, challenge-based modules and AI-powered learning assistant, is the official route. The [OSAI Exam Guide](https://help.offsec.com/hc/en-us/articles/46593096734612-OSAI-Exam-Guide) and the [exam FAQ](https://help.offsec.com/hc/en-us/articles/46669767163156-OSAI-Advanced-AI-Red-Teaming-Exam-FAQ) are required reading.

**How your background helps or misleads:**

- **.NET, Angular and AZ-204 prep** give you a builder's understanding of APIs, identity, managed services and application integration. That helps you understand how AI applications are wired together and where trust boundaries sit.
- **CKAD prep** helps with the infrastructure and deployment module: containers, orchestration and secrets.
- **AZ-900 and basic AWS knowledge** help you recognize cloud AI platform components.
- **The gap.** Your preparation so far is defensive and developer-focused. OSAI assumes offensive experience. Plan time for general penetration-testing practice first (OffSec's PEN-200/OSCP route is the one it recommends), and only work against environments you are authorized to test.

## Differences from related exams

- **OSAI vs CY0-001 (CompTIA SecAI+).** SecAI+ is a 60-minute exam with multiple-choice and PBQ questions about recognizing AI attacks and choosing defences. OSAI is a 24-hour hands-on engagement with a professional report. SecAI+ gives you the vocabulary, and OSAI tests whether you can carry out the work.
- **OSAI vs AAISM, AAIA and AAIR (ISACA).** The ISACA exams are about managing, auditing and governing AI risk, with no hands-on component. OSAI is purely practical and offensive.
- **OSAI vs OSCP (PEN-200).** OSCP is OffSec's general penetration-testing certification and the recommended foundation. OSAI adds AI-specific targets and allows, even encourages, AI assistance.
- **OSAI vs CAS-005 (SecurityX).** SecurityX touches on AI threats as one objective inside an architect-level, multiple-choice and PBQ exam. OSAI is narrow, deep and practical.

## Exam-day notes

- **Plan the 24 hours.** Schedule rest and meals. The exam guide explicitly expects breaks, and you will also need energy for the 24-hour report window that follows.
- **Document as you go.** Take screenshots and save commands immediately. You cannot add anything after you submit.
- **Have a contingency plan for power and the internet.** OffSec extends time only when the problem is on its side.
- **Check the submission format twice:** a PDF inside a .7z with the required file names, no password, under 100 MB, and an MD5 hash that matches after upload.
- **Remember the threshold:** 75 points is the pass mark. Track your total as you go and keep the report time in mind.
