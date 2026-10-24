---
code: PAA
title: "Professional Agentic Architect"
credential: "Google Cloud Certified Professional Agentic Architect"
provider: google
tracks: [agentic-ai, architect]
clouds: [neutral]
level: professional
tier: elective
stage: "3"
progress: planned
official_url: https://cloud.google.com/learn/certification/agentic-architect
study_guide_url: https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf
outline_version: "Exam guide (PDF dated 2026-08-31), beta/GA"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "No prerequisites. Google recommends 3+ years of hands-on experience building, testing, deploying and managing cloud solutions, including 1+ year building agentic solutions on Google Cloud."
replaces: ""
replaced_by: ""
counterparts: [ai-500, ab-100, aip-c01, claude-arch-p, ncp-aai]
objectives:
  - { id: "1", title: "Building agents using low-code tools", weight: "~13%" }
  - { id: "1.1", title: "Configuring agentic workflows and behavior using low-code tools" }
  - { id: "1.1.1", title: "Configure state-based workflows (pages, transition routes, event handlers) in Gemini Enterprise tools (Agent Designer, CX Agent Studio)" }
  - { id: "1.1.2", title: "Create system instructions and in-console prompt templates (few-shot, chain-of-thought) to guide agent behavior" }
  - { id: "1.2", title: "Connecting enterprise data to Gemini Enterprise" }
  - { id: "1.2.1", title: "Configure agents to securely connect to and query proprietary enterprise data sources (Gemini Enterprise, Agent Search)" }
  - { id: "1.2.2", title: "Ingest and process unstructured multimodal data (video, audio, images) into the agentic workflow" }
  - { id: "2", title: "Using coding agents for application development", weight: "~17%" }
  - { id: "2.1", title: "Using coding agents effectively" }
  - { id: "2.1.1", title: "Configure coding agents with MCP servers, custom skills and tool access (Antigravity, Claude Code on Google Cloud)" }
  - { id: "2.1.2", title: "Use coding agents in secure sandboxes (GKE, Cloud Workstations, Antigravity)" }
  - { id: "2.1.3", title: "Use coding agents to refactor code, optimize runtimes and patch application-layer vulnerabilities" }
  - { id: "2.2", title: "Customizing coding agents for enterprise workflows" }
  - { id: "2.2.1", title: "Create skills, plugins, extension hooks, rules and subagents using Antigravity" }
  - { id: "2.2.2", title: "Augment Antigravity with Agents CLI to build, scale, govern and optimize deployed agents" }
  - { id: "3", title: "Developing custom agents", weight: "~33%" }
  - { id: "3.1", title: "Designing and building agentic workflows in code" }
  - { id: "3.1.1", title: "Select and configure the language model (LLM vs. SLM, self-hosted vs. SaaS, OSS vs. proprietary) for cost, security and agent architecture" }
  - { id: "3.1.2", title: "Build custom agents with open-source libraries (e.g., Agent Development Kit)" }
  - { id: "3.1.3", title: "Configure sessions and memory (Agent Platform Memory Bank, managed sessions)" }
  - { id: "3.1.4", title: "Configure skills using Agents CLI (plugins; agent vs. human mode)" }
  - { id: "3.2", title: "Integrating enterprise domain knowledge" }
  - { id: "3.2.1", title: "Design, configure and manage RAG pipelines and vector retrieval (embeddings, similarity scoring, reranking) with Vector Search and Agent Retrieval" }
  - { id: "3.2.2", title: "Configure agent permissions (Agent Identity)" }
  - { id: "3.2.3", title: "Use Agent Registry and Google Cloud MCP servers to configure prebuilt and custom capabilities (database integrations, APIs, MCP to third-party SaaS)" }
  - { id: "3.3", title: "Orchestrating and coordinating agentic workflows" }
  - { id: "3.3.1", title: "Orchestrate agents using agentic protocols (MCP, Agent2Agent)" }
  - { id: "3.3.2", title: "Select and coordinate multi-agent handoffs and workflows (parallel, sequential, graph) with Agent Identity, Agent Registry, Agent Runtime and agent policies" }
  - { id: "4", title: "Evaluating and deploying agentic workflows", weight: "~22%" }
  - { id: "4.1", title: "Evaluating agents in development and in production" }
  - { id: "4.1.1", title: "Create test sets for agent evaluation (golden data, prompts, edge cases)" }
  - { id: "4.1.2", title: "Create continuous evaluation pipelines to assess tool execution against success criteria" }
  - { id: "4.1.3", title: "Choose the evaluation framework and tooling (ADK evalset, Agent Platform GenAI evaluation service, custom autoraters)" }
  - { id: "4.1.4", title: "Evaluate an agentic system against a golden dataset for response and retrieval quality (e.g., using ADK)" }
  - { id: "4.2", title: "Deploying and scaling production workloads" }
  - { id: "4.2.1", title: "Select the deployment runtime by use case, requirements and cost (Agent Runtime, Cloud Run, GKE)" }
  - { id: "4.2.2", title: "Troubleshoot agent issues (drift, tool invocation latency, reasoning loops, system failures)" }
  - { id: "4.2.3", title: "Monitor and optimize agents for performance, reliability and cost (logic errors, latency bottlenecks, hallucinations)" }
  - { id: "5", title: "Securing and governing agentic workflows", weight: "~15%" }
  - { id: "5.1", title: "Configuring agent security and governance" }
  - { id: "5.1.1", title: "Implement authentication and secure tool execution (agent-to-tool API calls using OAuth 2.0)" }
  - { id: "5.1.2", title: "Configure principal access boundary (PAB) policies using Agent Identity" }
  - { id: "5.1.3", title: "Configure Agent Gateway to monitor traffic and track agents" }
  - { id: "5.1.4", title: "Design and configure agentic governance and policy enforcement (Agent Registry, Model Armor)" }
  - { id: "5.2", title: "Implementing secure agent behavior and execution" }
  - { id: "5.2.1", title: "Design safety frameworks and guardrails (Agent Gateway, Model Armor, human-in-the-loop)" }
  - { id: "5.2.2", title: "Configure secure access to data and identity propagation (Agent Gateway, Agent Registry)" }
---
## About this certification

**PAA** is this library's short code for **Google Cloud Certified Professional Agentic Architect**. Google uses that abbreviation in its FAQ but gives no separate exam number. The certification is for an experienced developer or architect who "designs and manages autonomous, AI-driven agentic workflows in Google Cloud", building agentic solutions with reliability, performance, cost, security and scalability in mind.

**Why it is in this library even though it is outside the Azure/AWS focus:** it is one of the few professional-level certifications aimed squarely at *agentic architecture*. Its blueprint is a useful map of the problems every agent platform has to solve: low-code vs. code-first agents, coding agents, memory, RAG, protocols (MCP and A2A), evaluation, runtimes, identity, gateways and guardrails. Read it to compare with Microsoft's and AWS's agent offerings. Taking it is optional.

### How the objectives above were built

The objectives transcribe the official **[exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf)** (PDF dated 31 August 2026) in full: five sections with Google's approximate weights, each subsection (1.1, 1.2 …), and each "consideration" bullet beneath. Product names are kept exactly as Google gives them. The guide also lists the **tools in scope**: Agent Development Kit (ADK), Agent evaluation, Agent Gateway, Agent Identity, Agent Registry, Agent Retrieval and Vector Search 1.0, Agent Runtime (formerly Agent Engine), Agent Search (formerly Vertex AI Search), agentic protocols (A2A, MCP), Agents CLI in Agent Platform, Antigravity (CLI, SDK, App), Auth Manager (OAuth 2.0), BigQuery, Cloud Run, Cloud SQL, Cloud Storage, Firestore, Gemini Enterprise, Gemini LLMs, Google Cloud Observability (Cloud Logging, Cloud Trace), GKE, Memorystore for Redis, Model Armor, MCP servers, Model Garden, RAG Engine, Sensitive Data Protection and Skill Registry.

## Exam format

Facts are as of 2026-10-24, from the [certification page](https://cloud.google.com/learn/certification/agentic-architect) and the [PAA beta FAQ](https://support.google.com/cloud-certification/answer/18080541?hl=en). The exam is moving from beta to general availability (GA), so confirm everything before booking.

- **Status:** **beta**. Beta registration ran 3–30 September 2026 and the multiple-choice window ran 8–30 September 2026. **GA is planned for mid-November 2026**, with GA registration opening then (no exact date yet).
- **Two parts, both required:**
  1. **Part 1:** a proctored **multiple-choice** exam (Pearson) on concepts, design choices and architectural standards.
  2. **Part 2:** hands-on **PAA labs** on Google Skills, open only to candidates who pass Part 1. They check execution and coding ability. Passing the multiple-choice exam alone does **not** certify you.
- **Number of questions:** about 80 multiple-choice questions in the beta.
- **Duration:** beta 3 hours. GA is a standard 2-hour professional exam session. The labs are estimated at under 5 hours.
- **Passing score:** not published. Beta cut scores are set after the beta closes.
- **Price:** USD 200 retail (GA). The beta was USD 120 (40% off), plus tax where applicable.
- **Language:** English.
- **Delivery:** online proctored or onsite proctored at a test centre.
- **Results:** beta multiple-choice results arrive in CM Connect at the end of October 2026. Beta passers must finish the labs by **31 December 2026**. At GA, multiple-choice results come within 7–10 business days, then you have 2 months to complete the labs.
- **Retakes:** beta candidates who fail can retake at GA. Beta attempts do not count towards the attempt limit.
- **Validity:** **1 year**, shorter than the 2 years of other Google Cloud professional certifications. Google mentions a continuing-education path.

## What the exam really tests

The weights show the emphasis: **custom code-first agents (~33%)** and **evaluation and deployment (~22%)** together are more than half the exam. Expect scenario questions such as:

- choosing low-code (Gemini Enterprise Agent Designer, CX Agent Studio) vs. code-first (ADK) for a business requirement;
- choosing a model (LLM vs. SLM, self-hosted vs. SaaS, open-source vs. proprietary) by cost, security and architecture;
- memory and sessions (Memory Bank, managed sessions) and RAG design (embeddings, similarity scoring, reranking, Vector Search and Agent Retrieval);
- protocols and orchestration: MCP for tools, **Agent2Agent (A2A)** between agents, and parallel, sequential and graph multi-agent patterns;
- coding agents (Antigravity, Claude Code on Google Cloud) configured with MCP servers, skills, hooks, rules and subagents, run in **secure sandboxes**;
- evaluation: golden datasets, continuous evaluation of tool execution, ADK evalsets vs. the GenAI evaluation service vs. custom autoraters;
- runtime choice (Agent Runtime vs. Cloud Run vs. GKE) and troubleshooting drift, tool latency and reasoning loops;
- security: OAuth 2.0 for agent-to-tool calls, **Agent Identity** with principal access boundary policies, **Agent Gateway** for traffic and tracking, **Model Armor** and human-in-the-loop guardrails, and identity propagation to data.

The labs then check that you can actually build and run these, not only choose them.

**Where candidates lose points:** product-name confusion in a fast-changing portfolio (several services were renamed: Agent Runtime was Agent Engine, Agent Search was Vertex AI Search); choosing the heaviest runtime by default; and ignoring the identity and governance layer.

## Study strategy

1. **Read the exam guide and in-scope tool list,** and make a one-line note per tool: what it does and its nearest Azure or AWS equivalent.
2. **Follow the official learning path** on Google Skills: [Train for the exam (path 4525)](https://www.skills.google/paths/4525). There is a separate [partner path (4531)](https://partner.skills.google/paths/4531). Earn an agentic-development skill badge on Google Skills, and try the official [sample questions](https://docs.google.com/forms/d/1fi1gqbWsNCFxm1CT9V-JNGff1lyqfU9kNWAaaQMvRi4/preview).
3. **Build with ADK.** Create an agent with tools via MCP, Memory Bank sessions and Vector Search RAG. Deploy it once to Agent Runtime and once to Cloud Run, and evaluate it with an ADK evalset. Then add Agent Identity, Agent Gateway and Model Armor.
4. **Use a coding agent in a sandbox** (Antigravity or Claude Code on Google Cloud) with an MCP server, a custom skill and a rule file.
5. **Practise for the labs:** they are timed and hands-on, so practise in Google Skills lab environments, not only in reading.

**How your background helps or misleads**

- *Azure and AWS knowledge* helps you map concepts: Agent Runtime ≈ Microsoft Foundry Agent Service or Amazon Bedrock AgentCore Runtime, Agent Search/Vector Search ≈ Azure AI Search or Bedrock Knowledge Bases, Model Armor ≈ Azure AI Content Safety or Bedrock Guardrails, and principal access boundaries ≈ scoped IAM boundaries. Use these mappings to learn faster, but answer with Google's names and Google's IAM model.
- *CKAD preparation* helps directly with GKE sandboxes and GKE as a runtime choice.
- *Claude Code experience* is unusually relevant: the guide names **Claude Code on Google Cloud** as an example coding agent.
- *.NET background:* ADK examples are mostly Python (with other language SDKs). Read Python fluently.

## Differences from related exams

- **PAA vs AI-500 and AB-100 (Microsoft agentic expert exams) and AIP-C01 (AWS Generative AI Developer – Professional).** These are the Azure and AWS counterparts in this library's main focus. They cover the same problem space (agent design, RAG, multi-agent orchestration, evaluation, security) on their own platforms. PAA is the only one that also needs **hands-on labs** to certify, and the only one valid for just **one year**.
- **PAA vs CLAUDE-ARCH-P.** Both are professional-level agent architecture exams. CLAUDE-ARCH-P is cloud-neutral, model-platform-specific (Claude) and multiple choice only, and includes stakeholder communication. PAA is cloud-specific (Google Cloud services and IAM) and adds labs. The two meet on coding agents and MCP.
- **PAA vs NCP-AAI.** NCP-AAI is mostly platform-neutral agent engineering plus NVIDIA inference (NIM, Triton, TensorRT-LLM). PAA is about Google's managed agent platform and its governance services.
- **PAA vs Google Professional Cloud Architect.** The Cloud Architect exam covers general Google Cloud infrastructure design. PAA assumes that background and focuses entirely on agents.

## Exam-day notes

- **Watch the GA dates.** If you book in November 2026 or later, you are on the GA format: a 2-hour multiple-choice exam, then labs within 2 months. The beta's 3-hour and ~80-question format no longer applies.
- **Pace (GA):** Google has not published a GA item count. Plan for under 2 minutes per question and confirm the count in the GA exam guide.
- **Name-to-function mapping:** before the exam, test yourself on what each in-scope tool does. Renamed products and look-alike options are the main traps.
- **Prefer managed and governed:** when two designs both work, Google's answer usually uses the managed service (Agent Runtime, Agent Gateway, Agent Identity) with least-privilege policies and Model Armor, unless the scenario explicitly needs GKE-level control.
- **Labs:** read the whole task before you start, check each step's output, and keep within the lab timer. Partial work may not pass.
