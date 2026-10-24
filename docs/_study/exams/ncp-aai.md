---
code: NCP-AAI
title: "NVIDIA-Certified Professional: Agentic AI"
credential: "NVIDIA-Certified Professional: Agentic AI"
provider: nvidia
tracks: [agentic-ai]
clouds: [neutral]
level: professional
tier: elective
stage: "3"
progress: planned
official_url: https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/
study_guide_url: https://dam-cdn.nvd.orangelogic.com/AssetLink/64tei188l3tt132l265u1ipjoexdl1p5.pdf
outline_version: "Certification page blueprint as of 2026-10-24; study guide Sep25"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "No formal prerequisite. NVIDIA recommends 1–2 years in AI/ML roles (the study guide says 2–3) and hands-on work on production-level agentic AI projects, covering agent development, orchestration, multi-agent frameworks, evaluation, observability, deployment and guardrails."
replaces: ""
replaced_by: ""
counterparts: [claude-arch-f, claude-arch-p, paa, ai-103, ai-500, aip-c01]
objectives:
  - { id: "1", title: "Agent Architecture and Design", weight: "15%" }
  - { id: "1.1", title: "Design user interfaces for intuitive human-agent interaction" }
  - { id: "1.2", title: "Implement reasoning and action frameworks (e.g., ReAct)" }
  - { id: "1.3", title: "Configure agent-to-agent communication protocols for collaboration" }
  - { id: "1.4", title: "Manage short-term and long-term memory for context retention" }
  - { id: "1.5", title: "Orchestrate multi-agent workflows and coordination" }
  - { id: "1.6", title: "Apply logic trees, prompt chains and stateful orchestration for multi-step reasoning" }
  - { id: "1.7", title: "Integrate knowledge graphs to enable relational reasoning" }
  - { id: "1.8", title: "Ensure adaptability and scalability of the agent's architecture" }
  - { id: "2", title: "Agent Development", weight: "15%" }
  - { id: "2.1", title: "Engineer prompts and dynamic prompt chains for reliable performance" }
  - { id: "2.2", title: "Integrate generative and multimodal models (text, vision, audio)" }
  - { id: "2.3", title: "Build and connect custom tools, APIs and functions for external system interaction" }
  - { id: "2.4", title: "Implement error handling (retry logic, graceful failure recovery)" }
  - { id: "2.5", title: "Develop dynamic conversation flows with real-time streaming and feedback" }
  - { id: "2.6", title: "Evaluate and refine agent decision-making strategies" }
  - { id: "3", title: "Evaluation and Tuning", weight: "13%" }
  - { id: "3.1", title: "Implement evaluation pipelines and task benchmarks to measure performance" }
  - { id: "3.2", title: "Compare agent performance across tasks and datasets" }
  - { id: "3.3", title: "Collect and integrate structured user feedback for iterative improvements" }
  - { id: "3.4", title: "Tune model parameters (e.g., accuracy vs. latency-efficiency trade-offs)" }
  - { id: "3.5", title: "Analyze evaluation results to guide targeted optimization" }
  - { id: "4", title: "Deployment and Scaling", weight: "13%" }
  - { id: "4.1", title: "Deploy and orchestrate multi-agent systems at production scale" }
  - { id: "4.2", title: "Apply MLOps practices for CI/CD workflows, monitoring and governance" }
  - { id: "4.3", title: "Profile performance and reliability under distributed system loads" }
  - { id: "4.4", title: "Scale deployments using containerization (Docker, Kubernetes) with load balancing" }
  - { id: "4.5", title: "Optimize deployment costs while ensuring high availability" }
  - { id: "5", title: "Cognition, Planning, and Memory", weight: "10%" }
  - { id: "5.1", title: "Implement memory mechanisms for short- and long-term context retention" }
  - { id: "5.2", title: "Apply reasoning frameworks (chain-of-thought, task decomposition)" }
  - { id: "5.3", title: "Engineer planning strategies for sequential and multi-step decision-making" }
  - { id: "5.4", title: "Manage stateful orchestration to coordinate complex tasks and knowledge retention" }
  - { id: "5.5", title: "Adapt reasoning strategies based on prior experiences and feedback" }
  - { id: "6", title: "Knowledge Integration and Data Handling", weight: "10%" }
  - { id: "6.1", title: "Implement retrieval pipelines (RAG, embedded search, hybrid approaches)" }
  - { id: "6.2", title: "Configure and optimize vector databases for fast retrieval" }
  - { id: "6.3", title: "Build ETL pipelines to integrate enterprise or client data sources" }
  - { id: "6.4", title: "Conduct data quality checks, augmentation and preprocessing" }
  - { id: "6.5", title: "Enable real-time access and reasoning over structured and unstructured knowledge" }
  - { id: "7", title: "NVIDIA Platform Implementation", weight: "7%" }
  - { id: "7.1", title: "Integrate NVIDIA NeMo Guardrails for compliance and safety enforcement" }
  - { id: "7.2", title: "Deploy NVIDIA NIM microservices for high-performance inference" }
  - { id: "7.3", title: "Optimize workflows with the NVIDIA NeMo Agent Toolkit" }
  - { id: "7.4", title: "Use NVIDIA TensorRT-LLM and Triton Inference Server for latency reduction" }
  - { id: "7.5", title: "Manage and optimize multimodal input pipelines on NVIDIA hardware" }
  - { id: "8", title: "Run, Monitor, and Maintain", weight: "5%" }
  - { id: "8.1", title: "Define monitoring dashboards and reliability metrics" }
  - { id: "8.2", title: "Track logs, errors and anomalies for root cause diagnosis" }
  - { id: "8.3", title: "Continuously benchmark deployed agents against prior versions" }
  - { id: "8.4", title: "Implement automated tuning, retraining and versioning in production" }
  - { id: "8.5", title: "Ensure continuous uptime, transparency and trust in live deployments" }
  - { id: "9", title: "Safety, Ethics, and Compliance", weight: "5%" }
  - { id: "9.1", title: "Design and enforce system security and audit trails" }
  - { id: "9.2", title: "Integrate compliance guardrails (privacy, enterprise policy)" }
  - { id: "9.3", title: "Mitigate bias and toxicity in outputs" }
  - { id: "9.4", title: "Deploy layered safety frameworks (filters, escalation protocols)" }
  - { id: "9.5", title: "Ensure compliance with licensing and regulatory standards" }
  - { id: "10", title: "Human-AI Interaction and Oversight", weight: "5%" }
  - { id: "10.1", title: "Build intuitive UIs with user-in-the-loop interaction" }
  - { id: "10.2", title: "Design structured feedback loops that guide iterative agent improvements" }
  - { id: "10.3", title: "Implement transparency mechanisms (explainable reasoning, decision traceability)" }
  - { id: "10.4", title: "Enable human oversight and intervention for accountability and trust" }
---
## About this certification

**NCP-AAI** is NVIDIA's own exam code for **NVIDIA-Certified Professional: Agentic AI**, an intermediate, professional-level credential for people who design, evaluate and deploy autonomous AI systems. As of 2026-10-24 the [certification page](https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/) shows **"Coming soon"** next to the registration button. The blueprint, study guide and training are published, but booking is not yet open on that page. Check again before you plan a date.

### How the objectives above were built

- **Domains and weights** come from the "Exam Blueprint" table on the certification page as of 2026-10-24. That table's weights add up to **98%**, and NVIDIA does not explain the missing 2%.
- **Task statements (x.1, x.2 …)** come from the official **[exam study guide](https://dam-cdn.nvd.orangelogic.com/AssetLink/64tei188l3tt132l265u1ipjoexdl1p5.pdf)** (dated Sep25), which numbers them 1.1–10.4 in the same domain order used here.
- **Known discrepancy:** the study guide gives *Deployment and Scaling 5%* and *Run, Monitor, and Maintain 7%*, while the current certification page gives *13%* and *5%*. This library follows the page because it is the newer source. Recheck both when registration opens.

## Exam format

Facts are as of 2026-10-24, from the [certification page](https://www.nvidia.com/en-us/learn/certification/agentic-ai-professional/) and the [NVIDIA certification FAQ](https://www.nvidia.com/en-us/learn/certification/#faq). Confirm them before booking, especially since the exam is listed as coming soon.

- **Question type:** multiple choice (the page gives an item count and no other formats).
- **Number of questions:** 60–70.
- **Duration:** 120 minutes.
- **Passing score:** not published on the page.
- **Price:** USD 200.
- **Language:** English.
- **Delivery:** online, remotely proctored, through **Certiverse**. You need a Certiverse account. [Registration link](https://www.certiverse.com/#/checkout/nvidia/store-exam/NCP-AAI).
- **Validity and renewal:** **two years** from issue. Recertify by retaking the exam.
- **Credential:** a digital badge and an optional certificate.

## What the exam really tests

The study guide describes the role as an intermediate practitioner who builds "resilient, secure, and trustworthy agentic solutions" (assistants, meeting companions, productivity tools) and who knows reactive, deliberative and hybrid agent architectures, goal-oriented reasoning, chain-of-thought prompting, tool orchestration with robust error handling, memory management, evaluation, containerised deployment, monitoring, guardrails, and troubleshooting hallucinations and failures. In practice:

- **Architecture and cognition (about 25%):** ReAct-style reason-and-act loops, planning and task decomposition, short- and long-term memory, stateful orchestration, multi-agent coordination, agent-to-agent protocols and knowledge graphs.
- **Development (15%):** prompt chains, multimodal models, custom tools and APIs, retry and graceful-failure logic, streaming conversation flows.
- **Evaluation and operations (about 31% with the page weights):** evaluation pipelines and benchmarks, user feedback, parameter tuning for accuracy vs. latency, production MLOps, Kubernetes scaling, cost and high availability, dashboards, root-cause analysis and version benchmarking.
- **Knowledge (10%):** RAG, hybrid search, vector database tuning, ETL and data quality.
- **NVIDIA stack (7%):** NeMo Guardrails, NIM microservices, the NeMo Agent Toolkit (formerly Agent Intelligence Toolkit / AIQ), TensorRT-LLM and Triton Inference Server.
- **Responsible AI and oversight (10%):** audit trails, compliance guardrails, bias and toxicity, layered safety, human-in-the-loop and traceability.

The exam is **mostly vendor-neutral agent engineering** with a smaller NVIDIA-specific part. The study guide's suggested readings even include Microsoft's Azure Architecture Center pages on the Retry, Circuit Breaker and Transient Fault Handling patterns, and LangChain and LangSmith material.

**Where candidates lose points:** the NVIDIA-specific 7% (knowing which product does what: NIM for packaged inference, Triton for serving, TensorRT-LLM for optimisation, NeMo Guardrails for rails); confusing memory types and when to persist them; and treating evaluation as a one-off instead of a continuous pipeline.

## Study strategy

1. **Follow the study guide domain by domain.** Each domain lists a recommended NVIDIA course and suggested readings. Use them as your reading list.
2. **Take the NVIDIA Deep Learning Institute courses** recommended on the certification page:
   - *Building Agentic AI Applications With LLMs* (self-paced, 8 h): the most important one, cited in most domains.
   - *Building RAG Agents With LLMs* (self-paced, 8 h).
   - *Evaluating RAG and Semantic Search Systems* (self-paced, 3 h).
   - *Introduction to Deploying RAG Pipelines for Production at Scale* (self-paced, 8 h).
   - *Adding New Knowledge to LLMs* (instructor-led, 8 h).
3. **Get hands-on with the NVIDIA stack.** Deploy a NIM endpoint (NVIDIA's API catalogue offers hosted trials), add NeMo Guardrails to a simple agent, and try the NeMo Agent Toolkit's profiling and evaluation. Read the Triton and TensorRT-LLM overviews well enough to place them.
4. **Build one complete agent:** ReAct-style tool use, memory, RAG over your own documents, an evaluation set, and deployment to Kubernetes with monitoring. This one project covers more than half the blueprint.

**How your background helps or misleads**

- *CKAD preparation* is directly useful for Domain 4 (containers, Kubernetes scaling, load balancing). Here the workloads are GPU inference services. Learn the basics of GPU telemetry and scaling.
- *AZ-204 and Azure AI work* help with retries, circuit breakers and RAG patterns, and NVIDIA's own reading list cites Microsoft pages. Do not assume Azure AI Search or Azure OpenAI answers. Answers are framework-neutral or NVIDIA-specific.
- *.NET/Angular* helps with UI items (Domains 1 and 10, human-agent interfaces). Most NVIDIA tooling and examples are in Python, so read Python fluently.

## Differences from related exams

- **NCP-AAI vs CLAUDE-ARCH-F and CLAUDE-ARCH-P.** The Claude exams tie you to one model provider's agent stack (Agent SDK, Claude Code, MCP) and leave out self-hosting and inference optimisation. NCP-AAI is model-agnostic but includes **running models yourself** (NIM, Triton, TensorRT-LLM, GPU pipelines). The Claude Foundations exam goes much deeper on tool interface and loop design. CLAUDE-ARCH-P adds stakeholder and lifecycle management, which NCP-AAI does not cover.
- **NCP-AAI vs PAA (Google Cloud Professional Agentic Architect).** PAA is tied to Google Cloud services (Gemini Enterprise, ADK, Agent Runtime, Agent Gateway, Model Armor) and requires hands-on labs as well as the multiple-choice exam. NCP-AAI is multiple choice only and mostly platform-neutral.
- **NCP-AAI vs AI-103 and AI-500 (Microsoft) and AIP-C01 (AWS).** The cloud exams test managed agent services, identity and networking on their platforms. NCP-AAI tests the agent engineering underneath them, plus NVIDIA inference. The difference is "use a managed agent service" versus "build and serve the agent system".
- **NCP-AAI vs the NVIDIA associate generative AI exams.** NVIDIA's associate-level generative AI credentials cover LLM fundamentals. NCP-AAI is the professional step focused on agents in production.

## Exam-day notes

- **Pace:** 60–70 questions in 120 minutes is about 1 min 45 s to 2 min each.
- **Remote proctoring on Certiverse:** set up and test your Certiverse account, webcam and connection well before the day. Use a clean desk and a single monitor.
- **Product-mapping questions:** when an option names an NVIDIA product, check it does that job (serving, optimisation, guardrails, agent profiling). Wrong-product distractors are likely.
- **Prefer resilient designs:** retries with backoff, circuit breakers, graceful degradation, human escalation and continuous evaluation reflect the study guide's emphasis.
- **Recheck the blueprint** the week you book. The page and study guide disagree on two weights, and the exam was not yet open for registration on 2026-10-24.
