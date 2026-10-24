---
code: CLAUDE-ARCH-P
title: "Claude Certified Architect – Professional"
credential: "Claude Certified Architect – Professional"
provider: anthropic
tracks: [agentic-ai, architect]
clouds: [neutral]
level: professional
tier: elective
stage: "3"
progress: planned
official_url: https://anthropic-partners.skilljar.com/claude-certified-architect-professional-certification
study_guide_url: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf
outline_version: "Exam Guide version 1.0, effective July 2026 (exam code CCAR-P)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "Only people at organizations in the Claude Partner Network can register (membership is free for firms). No mandatory prerequisite or course; Anthropic recommends 3+ years in systems architecture or platform engineering and 6+ months of hands-on Claude or comparable LLM systems in production. The Foundations level is the natural first step."
replaces: ""
replaced_by: ""
counterparts: [ai-500, ab-100, aip-c01, paa, ncp-aai]
objectives:
  - { id: "1", title: "Solution Design & Architecture", weight: "17%" }
  - { id: "1.1", title: "Translate business problems into Claude-based AI solutions" }
  - { id: "1.2", title: "Design end-to-end architectures (input → processing → output → feedback loops)" }
  - { id: "1.3", title: "Select appropriate architectural patterns (workflow, agentic, augmented LLM)" }
  - { id: "1.4", title: "Design multi-agent systems and orchestration strategies" }
  - { id: "1.5", title: "Apply decomposition techniques for complex problem solving" }
  - { id: "1.6", title: "Align solutions to business value pillars (efficiency, transformation, productivity, cost, performance SLAs)" }
  - { id: "2", title: "Claude Models, Prompting & Context Engineering", weight: "13%" }
  - { id: "2.1", title: "Select appropriate Claude models based on trade-offs" }
  - { id: "2.2", title: "Design system prompts, templates and guardrails" }
  - { id: "2.3", title: "Apply prompt engineering techniques (zero-shot, few-shot, chain-of-thought)" }
  - { id: "2.4", title: "Optimize context windows and manage token usage" }
  - { id: "2.5", title: "Implement prompt reuse strategies (caching, modular prompts, Skills)" }
  - { id: "3", title: "Integration", weight: "19%" }
  - { id: "3.1", title: "Evaluate tool/agent configuration for capability bloat" }
  - { id: "3.2", title: "Analyze authentication and authorization requirements to identify security gaps" }
  - { id: "3.3", title: "Evaluate accuracy-latency trade-offs and justify configuration decisions" }
  - { id: "3.4", title: "Analyze observability challenges and select monitoring strategies at scale" }
  - { id: "3.5", title: "Design a RAG pipeline with appropriate chunking and indexing strategies" }
  - { id: "3.6", title: "Apply retrieval strategies matched to data shape and query pattern" }
  - { id: "3.7", title: "Evaluate connection protocols and select the integration mechanism (MCP, API/CLI, agent-to-agent)" }
  - { id: "3.8", title: "Evaluate progressive discovery vs. monolithic context strategy" }
  - { id: "4", title: "Evaluation, Testing & Optimization", weight: "16%" }
  - { id: "4.1", title: "Define evaluation metrics (accuracy, latency, cost, safety, security)" }
  - { id: "4.2", title: "Design evaluation datasets and test frameworks using mixed methodologies" }
  - { id: "4.3", title: "Conduct A/B testing and iterative improvements" }
  - { id: "4.4", title: "Diagnose system issues (prompt failure, hallucinations, model mismatch)" }
  - { id: "4.5", title: "Optimize token usage, latency and cost-performance trade-offs" }
  - { id: "4.6", title: "Monitor system performance using logging and observability tools" }
  - { id: "5", title: "Governance, Safety & Risk Management", weight: "14%" }
  - { id: "5.1", title: "Implement guardrails and safety controls" }
  - { id: "5.2", title: "Identify risks, limitations and failure modes of LLM systems" }
  - { id: "5.3", title: "Apply human-in-the-loop validation strategies" }
  - { id: "5.4", title: "Ensure compliance with regulations (e.g., GDPR, HIPAA, FedRAMP)" }
  - { id: "5.5", title: "Address ethical AI considerations (bias, fairness, transparency)" }
  - { id: "6", title: "Stakeholder Communication & Lifecycle Management", weight: "14%" }
  - { id: "6.1", title: "Conduct structured discovery and requirement gathering" }
  - { id: "6.2", title: "Communicate architectural decisions and trade-offs" }
  - { id: "6.3", title: "Manage stakeholder feedback loops and expectation alignment (including SLAs)" }
  - { id: "6.4", title: "Document architectures and provide implementation guidance" }
  - { id: "6.5", title: "Support lifecycle phases (discovery, design, handoff, monitoring, iteration)" }
  - { id: "7", title: "Developer Productivity & Operational Enablement", weight: "7%" }
  - { id: "7.1", title: "Configure Claude tools and environments for teams (e.g., Claude Code)" }
  - { id: "7.2", title: "Improve developer workflows using AI-assisted tooling" }
  - { id: "7.3", title: "Support debugging and operational issue resolution" }
---
## About this code

**CLAUDE-ARCH-P is this library's own code.** Anthropic's exam guide gives the exam code **CCAR-P**. Claude Certified Architect – Professional was announced in July 2026 as the advanced credential in Anthropic's four role-based certifications, covering "integration architecture, governance, and evaluation, built for large enterprises" ([announcement](https://www.claude.com/blog/four-role-based-claude-certifications)). The other three are Associate – Foundations, Developer – Foundations and Architect – Foundations.

**Who can take it:** only people at organisations in the **Claude Partner Network**. Membership is free and open to firms that deliver Claude for clients ([claude.com/partners](https://claude.com/partners), [eligibility](https://anthropic-partners.skilljar.com/page/certification-eligibility)). You register with a company email on a domain in your organisation's partner record.

### How the objectives above were built

Anthropic publishes the blueprint publicly. The objectives transcribe Section 6 of the **Claude Certified Architect – Professional Exam Guide, version 1.0, effective July 2026** ([PDF](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf)): seven domains with weights, and every task bullet beneath each one. Unlike the Foundations guide, the Professional guide has no "Knowledge of / Skills in" breakdown and no published scenario bank, so the task bullets are the most detailed level available.

## Exam format

Facts are as of 2026-10-24, from the exam guide and the [partner certifications page](https://anthropic-partners.skilljar.com/page/partner-certifications). Confirm them before you register.

- **Question types:** multiple choice and multiple response. Each item says how many to select.
- **Number of items:** 63.
- **Duration:** 120 minutes.
- **Passing score:** a scaled score of 720 on a 100–1,000 scale (criterion-referenced, set by a standard-setting study against a "minimally qualified candidate"). The report shows percent correct by domain.
- **Price:** USD 175. The checkout price reflects any partner-tier discount.
- **Language:** English (no other languages are listed).
- **Delivery:** Pearson VUE, online proctored or at a test centre, with identity verification. Cancel or reschedule at least 24 hours before, or you forfeit the fee.
- **Retakes:** waits of 14, 30 and then 90 days after successive failures, with at most four attempts in a rolling 12 months. The full fee applies each time.
- **Validity and renewal:** **12 months**. On time, renewal is a free, non-proctored assessment on the Anthropic Partner Academy. After a lapse, you retake the full exam at full price. If content changes significantly, Anthropic may require the full exam instead of the renewal assessment.

## What the exam really tests

The guide's "minimally qualified candidate" is an experienced practitioner who turns business requirements into scalable, secure and reliable Claude architectures and understands trade-offs in **cost, latency, performance, safety and maintainability**. The blueprint shows what that means in practice:

- **Pattern selection.** When a fixed workflow beats an autonomous agent, when an augmented LLM (retrieval plus tools) is enough, and how to decompose work across agents.
- **Model and context economics.** Choosing a Claude model tier for the task, prompt caching and modular prompts or Skills for reuse, and keeping context lean with progressive discovery rather than loading everything up front.
- **Integration (the heaviest domain, 19%).** Spotting *capability bloat* (too many tools or agents), auth gaps when agents act for users, accuracy vs. latency settings, observability at scale, RAG chunking and indexing, retrieval strategy matched to data shape, and choosing **MCP vs. direct API/CLI vs. agent-to-agent** integration.
- **Evaluation discipline.** Defining metrics for accuracy, latency, cost, safety and security, building evaluation datasets, A/B testing, and diagnosing whether a failure comes from the prompt, retrieval, the model choice or hallucination.
- **Governance.** Guardrails, human-in-the-loop, regulatory fit (GDPR, HIPAA and FedRAMP are named), and bias, fairness and transparency.
- **Consulting skills.** Discovery, communicating trade-offs, SLAs and expectations, documentation and handoff. This domain is unusual for a technical exam.

**Where candidates lose points:** over-engineering (an autonomous multi-agent system where a workflow fits); choosing the biggest model by default instead of justifying the trade-off; treating RAG as a single default answer; missing the security gap in delegated authentication; and skipping the stakeholder or SLA aspect of a scenario.

## Study strategy

1. **Do Foundations first** (CLAUDE-ARCH-F) or at least work through its guide. Its detailed knowledge bullets on agent loops, MCP, Claude Code and structured output are the base the Professional exam builds on.
2. **Take the official prep course** in the Anthropic Partner Academy ([Architect – Professional path](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional)). Its courses include Claude Platform Solution Design, Developer Productivity Enablement, and Stakeholder Engagement, Lifecycle & GTM. Use the official Claude documentation (models, prompt engineering, context and prompt caching, Skills, MCP) as reference, as the guide recommends.
3. **Build and run one solution end to end,** as the guide also recommends: a RAG-backed agent with tools, an evaluation set, A/B testing of a prompt or model change, and logging and tracing. Write an architecture decision record for model choice, integration protocol and the main security trade-off.
4. **Practise explaining trade-offs.** For each blueprint bullet, prepare a two-sentence argument a client executive would accept. The Domain 6 items reward this.
5. **Map regulation to controls.** For GDPR, HIPAA and FedRAMP, list what changes in data flow, hosting choice, logging and human review.

**How your background helps or misleads**

- *Azure and AWS architect preparation* (AZ-305, SAA-C03) helps with integration, auth, observability and compliance thinking. Answer from Claude's platform features (models, caching, Skills, MCP) rather than cloud-native services. The guide does not test cloud-provider configuration.
- *The AI governance track* (AIGP, ISO/IEC 42001) helps with Domain 5 and the governance mindset. This exam wants the *technical* control (guardrail, HITL step, evaluation gate), not the policy document.
- *Development background* helps with Domains 4 and 7. Do not let implementation detail push out the business-value framing that Domains 1 and 6 require.

## Differences from related exams

- **CLAUDE-ARCH-P vs CLAUDE-ARCH-F.** Foundations is configuration-level and very specific (stop_reason handling, `.claude/rules/`, `tool_choice`, the Message Batches API), with a published bank of 6 scenarios. Professional is design-level and broader: model selection, RAG, auth, evaluation, compliance and stakeholder management. It has 63 items, costs USD 175 instead of 125, and publishes only task bullets. Professional adds two domains Foundations lacks: evaluation and testing, and stakeholder and lifecycle management.
- **vs AI-500 (Microsoft Multi-Agent AI Solutions Expert) and AB-100 (Agentic AI Business Solutions Architect).** The Microsoft expert-level exams design agent solutions *on Microsoft's platform* and its services, identity and governance. CLAUDE-ARCH-P is model-platform-specific but cloud-neutral. Its integration choices are MCP, API/CLI and agent-to-agent, not Azure resources.
- **vs AIP-C01 (AWS Certified Generative AI Developer – Professional).** AIP-C01 is about building generative AI on AWS (Amazon Bedrock and its agents, knowledge bases, guardrails and AWS security). CLAUDE-ARCH-P covers similar architecture concerns from the Claude platform side. A partner architect delivering Claude on Bedrock would benefit from both.
- **vs PAA (Google Cloud Professional Agentic Architect).** PAA has a similar professional scope (low-code agents, coding agents, custom agents, evaluation and deployment, security and governance), but it is tied to Google Cloud's agent stack and adds **hands-on labs** after the multiple-choice part. CLAUDE-ARCH-P is multiple-choice only.
- **vs NCP-AAI (NVIDIA Agentic AI).** NCP-AAI includes inference optimisation and self-hosted deployment on NVIDIA hardware and software (NIM, Triton, TensorRT-LLM), which CLAUDE-ARCH-P does not cover. CLAUDE-ARCH-P has stakeholder and lifecycle content that NCP-AAI lacks.
- **vs OGEA-102 and CPSA-A.** The vendor-neutral architect credentials test *method* (TOGAF) or *design craft shown in a written assignment* (iSAQB). CLAUDE-ARCH-P tests applied judgement on one AI platform. Domain 6 (stakeholder communication and lifecycle) is where it comes closest to TOGAF.

## Exam-day notes

- **Pace:** 63 items in 120 minutes is just under 2 minutes each. Flag long scenario items and come back.
- **Name the trade-off.** Most items have several workable answers. Pick the one that best satisfies the *stated* constraint (cost, latency, compliance or SLA) and is no more complex than it needs to be.
- **Simplicity wins.** Prefer workflow over agent, fewer tools over more, and progressive discovery over loading everything up front, unless the scenario clearly needs the opposite.
- **Security reading.** In integration items, check *whose* identity the agent acts under and what it can reach. Many correct answers close an authorisation gap.
- **Evaluation first.** When a scenario reports quality problems, the best first step is often to measure (an evaluation set, diagnostics) before changing the model or prompt.
- **Multi-response:** select exactly the number stated.
- **Check-in:** government photo ID matching your registration name; clear desk; no phones or smartwatches.
