---
code: AIP-C01
title: "AWS Certified Generative AI Developer – Professional"
credential: "AWS Certified Generative AI Developer – Professional"
provider: aws
tracks: [agentic-ai, cloud]
clouds: [aws]
level: professional
tier: core
stage: "3"
progress: planned
official_url: https://aws.amazon.com/certification/certified-generative-ai-developer-professional/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html
outline_version: "AIP-C01 guide (no version printed), retrieved 2026-10-24"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends 2 or more years building production applications on AWS or with open-source technologies, general AI/ML or data engineering experience, and 1 year of hands-on generative AI implementation."
replaces: ""
replaced_by: ""
counterparts: [ai-103]
objectives:
  - { id: "1", title: "Foundation Model Integration, Data Management, and Compliance", weight: "31%" }
  - { id: "1.1", title: "Analyze requirements and design GenAI solutions" }
  - { id: "1.1.1", title: "Skill: Create architectural designs aligned to business needs and technical constraints (FM choice, integration patterns, deployment strategies)" }
  - { id: "1.1.2", title: "Skill: Build proofs of concept to validate feasibility, performance and business value (e.g. Amazon Bedrock)" }
  - { id: "1.1.3", title: "Skill: Create standardized components for consistent implementation (AWS Well-Architected Framework, AWS WA Tool Generative AI Lens)" }
  - { id: "1.2", title: "Select and configure FMs" }
  - { id: "1.2.1", title: "Skill: Assess and choose FMs for business use cases (benchmarks, capability and limitation analysis)" }
  - { id: "1.2.2", title: "Skill: Design patterns for dynamic model selection and provider switching without code changes (AWS Lambda, Amazon API Gateway, AWS AppConfig)" }
  - { id: "1.2.3", title: "Skill: Design resilient AI systems for service disruptions (Step Functions circuit breakers, Amazon Bedrock Cross-Region Inference, graceful degradation)" }
  - { id: "1.2.4", title: "Skill: Deploy and manage the lifecycle of customized FMs (Amazon SageMaker AI, LoRA and adapters, SageMaker Model Registry, rollback, retirement)" }
  - { id: "1.3", title: "Implement data validation and processing pipelines for FM consumption" }
  - { id: "1.3.1", title: "Skill: Build data validation workflows for FM input quality (AWS Glue Data Quality, SageMaker Data Wrangler, Lambda, CloudWatch metrics)" }
  - { id: "1.3.2", title: "Skill: Process text, image, audio and tabular data for FMs (Bedrock multimodal models, SageMaker Processing, Amazon Transcribe)" }
  - { id: "1.3.3", title: "Skill: Format input data to model-specific requirements (Bedrock API JSON, SageMaker AI endpoint payloads, conversation formatting)" }
  - { id: "1.3.4", title: "Skill: Enhance input data quality to improve responses (Bedrock reformatting, Amazon Comprehend entity extraction, Lambda normalization)" }
  - { id: "1.4", title: "Design and implement vector store solutions" }
  - { id: "1.4.1", title: "Skill: Design vector database architectures for FM augmentation (Amazon Bedrock Knowledge Bases, OpenSearch Service Neural plugin, Amazon RDS with S3, DynamoDB metadata)" }
  - { id: "1.4.2", title: "Skill: Build metadata frameworks to improve search precision (S3 object metadata, custom attributes, domain tagging)" }
  - { id: "1.4.3", title: "Skill: Optimize vector search performance at scale (OpenSearch sharding, multi-index, hierarchical indexing)" }
  - { id: "1.4.4", title: "Skill: Build integration components for document systems, knowledge bases and internal wikis" }
  - { id: "1.4.5", title: "Skill: Keep vector stores current (incremental updates, change detection, automated sync, scheduled refresh)" }
  - { id: "1.5", title: "Design retrieval mechanisms for FM augmentation" }
  - { id: "1.5.1", title: "Skill: Design document chunking strategies (Bedrock chunking, fixed-size chunking in Lambda, hierarchical chunking)" }
  - { id: "1.5.2", title: "Skill: Select and configure embedding models (Amazon Titan embeddings, dimensionality and domain fit, batch embedding generation)" }
  - { id: "1.5.3", title: "Skill: Deploy vector search (OpenSearch Service, Amazon Aurora with pgvector, Bedrock Knowledge Bases managed vector store)" }
  - { id: "1.5.4", title: "Skill: Build advanced search architectures (semantic search, hybrid keyword and vector search, Bedrock reranker models)" }
  - { id: "1.5.5", title: "Skill: Build query handling (query expansion, decomposition and transformation with Bedrock, Lambda, Step Functions)" }
  - { id: "1.5.6", title: "Skill: Create consistent retrieval access mechanisms (function calling, Model Context Protocol (MCP) clients, standard API patterns)" }
  - { id: "1.6", title: "Implement prompt engineering strategies and governance for FM interactions" }
  - { id: "1.6.1", title: "Skill: Create instruction frameworks to control FM behavior (Amazon Bedrock Prompt Management, Amazon Bedrock Guardrails, response templates)" }
  - { id: "1.6.2", title: "Skill: Build interactive systems that keep context (Step Functions clarification flows, Comprehend intent recognition, DynamoDB conversation history)" }
  - { id: "1.6.3", title: "Skill: Implement prompt management and governance (parameterized templates and approvals, S3 template repositories, CloudTrail, CloudWatch Logs)" }
  - { id: "1.6.4", title: "Skill: Build prompt quality assurance (Lambda output checks, Step Functions edge-case tests, CloudWatch prompt regression)" }
  - { id: "1.6.5", title: "Skill: Refine prompts iteratively (structured inputs, output format specifications, chain-of-thought patterns, feedback loops)" }
  - { id: "1.6.6", title: "Skill: Design complex prompt systems (Amazon Bedrock Prompt Flows chains, conditional branching, reusable components, pre- and post-processing)" }
  - { id: "2", title: "Implementation and Integration", weight: "26%" }
  - { id: "2.1", title: "Implement agentic AI solutions and tool integrations" }
  - { id: "2.1.1", title: "Skill: Build autonomous agents with memory and state management (Strands Agents, AWS Agent Squad, MCP)" }
  - { id: "2.1.2", title: "Skill: Build structured reasoning systems (ReAct and chain-of-thought with Step Functions)" }
  - { id: "2.1.3", title: "Skill: Build safeguarded AI workflows (stopping conditions, Lambda timeouts, IAM resource boundaries, circuit breakers)" }
  - { id: "2.1.4", title: "Skill: Coordinate multiple models (specialized FMs, ensemble aggregation, model selection frameworks)" }
  - { id: "2.1.5", title: "Skill: Build human-in-the-loop systems (Step Functions review and approval, API Gateway feedback collection)" }
  - { id: "2.1.6", title: "Skill: Implement reliable tool integrations (Strands API custom behaviors, standard function definitions, Lambda error handling and parameter validation)" }
  - { id: "2.1.7", title: "Skill: Build model extension frameworks with MCP (stateless MCP servers on Lambda, complex MCP servers on Amazon ECS, MCP client libraries)" }
  - { id: "2.2", title: "Implement model deployment strategies" }
  - { id: "2.2.1", title: "Skill: Deploy FMs to fit application and performance needs (on-demand via Lambda, Bedrock provisioned throughput, SageMaker AI endpoints)" }
  - { id: "2.2.2", title: "Skill: Handle LLM-specific deployment challenges (container patterns for memory, GPU utilization and token capacity, model loading)" }
  - { id: "2.2.3", title: "Skill: Balance performance and resources (right-sized models, smaller task-specific models, API-based model cascading)" }
  - { id: "2.3", title: "Design and implement enterprise integration architectures" }
  - { id: "2.3.1", title: "Skill: Connect FMs to existing enterprise environments (APIs to legacy systems, event-driven loose coupling, data synchronization)" }
  - { id: "2.3.2", title: "Skill: Add GenAI to existing applications (API Gateway microservices, Lambda webhook handlers, Amazon EventBridge)" }
  - { id: "2.3.3", title: "Skill: Create secure access frameworks (identity federation, role-based access to models and data, least-privilege FM API access)" }
  - { id: "2.3.4", title: "Skill: Build cross-environment solutions for data compliance across jurisdictions (AWS Outposts, AWS Wavelength, secure hybrid routing)" }
  - { id: "2.3.5", title: "Skill: Implement CI/CD and GenAI gateway architectures (AWS CodePipeline, AWS CodeBuild, security scans and rollback, centralized abstraction layers)" }
  - { id: "2.4", title: "Implement FM API integrations" }
  - { id: "2.4.1", title: "Skill: Build flexible model interaction (synchronous Bedrock APIs, AWS SDKs with Amazon SQS for async, API Gateway request validation)" }
  - { id: "2.4.2", title: "Skill: Build real-time interaction (Bedrock streaming APIs, WebSockets or server-sent events, chunked transfer encoding)" }
  - { id: "2.4.3", title: "Skill: Build resilient FM systems (SDK exponential backoff, API Gateway rate limiting, fallbacks, AWS X-Ray)" }
  - { id: "2.4.4", title: "Skill: Build model routing (static configuration, Step Functions content-based routing, metric-based routing, API Gateway transformations)" }
  - { id: "2.5", title: "Implement application integration patterns and development tools" }
  - { id: "2.5.1", title: "Skill: Create FM API interfaces for GenAI needs (API Gateway streaming, token limit management, retries for model timeouts)" }
  - { id: "2.5.2", title: "Skill: Build accessible AI interfaces (AWS Amplify UI components, OpenAPI-first design, Bedrock Prompt Flows no-code builder)" }
  - { id: "2.5.3", title: "Skill: Enhance business systems (Lambda CRM enhancements, Step Functions document processing, Amazon Bedrock Data Automation)" }
  - { id: "2.5.4", title: "Skill: Improve developer productivity (Amazon Q Developer code generation and refactoring, AI component testing)" }
  - { id: "2.5.5", title: "Skill: Build advanced GenAI applications (Strands Agents, AWS Agent Squad, Step Functions agent patterns, Bedrock prompt chaining)" }
  - { id: "2.5.6", title: "Skill: Troubleshoot FM applications efficiently (CloudWatch Logs Insights, X-Ray tracing of FM calls, Amazon Q Developer error recognition)" }
  - { id: "3", title: "AI Safety, Security, and Governance", weight: "20%" }
  - { id: "3.1", title: "Implement input and output safety controls" }
  - { id: "3.1.1", title: "Skill: Protect against harmful inputs (Amazon Bedrock Guardrails, custom moderation with Step Functions and Lambda, real-time validation)" }
  - { id: "3.1.2", title: "Skill: Prevent harmful outputs (Guardrails response filtering, FM-based toxicity evaluation, text-to-SQL for deterministic results)" }
  - { id: "3.1.3", title: "Skill: Reduce hallucinations (grounding with Bedrock Knowledge Bases, confidence scoring, semantic similarity checks, JSON Schema outputs)" }
  - { id: "3.1.4", title: "Skill: Build defense-in-depth safety (Comprehend pre-filters, model-based guardrails, Lambda post-validation, API Gateway response filtering)" }
  - { id: "3.1.5", title: "Skill: Detect adversarial inputs (prompt injection and jailbreak detection, input sanitization, safety classifiers, automated adversarial testing)" }
  - { id: "3.2", title: "Implement data security and privacy controls" }
  - { id: "3.2.1", title: "Skill: Secure FM environments (VPC endpoints, IAM data access policies, AWS Lake Formation, CloudWatch access monitoring)" }
  - { id: "3.2.2", title: "Skill: Protect sensitive data in FM interactions (Amazon Comprehend and Amazon Macie PII detection, Bedrock privacy features, Guardrails, S3 Lifecycle retention)" }
  - { id: "3.2.3", title: "Skill: Preserve user privacy while keeping FM utility (masking, anonymization, Comprehend PII detection, Guardrails)" }
  - { id: "3.3", title: "Implement AI governance and compliance mechanisms" }
  - { id: "3.3.1", title: "Skill: Build compliance frameworks (SageMaker AI model cards, AWS Glue data lineage, source metadata tagging, CloudWatch Logs decision logs)" }
  - { id: "3.3.2", title: "Skill: Track data sources for traceability (AWS Glue Data Catalog, source attribution metadata, CloudTrail audit logs)" }
  - { id: "3.3.3", title: "Skill: Create organizational governance aligned to policy, regulation and responsible AI principles" }
  - { id: "3.3.4", title: "Skill: Implement continuous monitoring and governance controls (misuse, drift and policy-violation detection, bias drift, token-level redaction, response logging)" }
  - { id: "3.4", title: "Implement responsible AI principles" }
  - { id: "3.4.1", title: "Skill: Build transparent AI (user-facing reasoning, CloudWatch confidence metrics, source attribution, Bedrock agent tracing)" }
  - { id: "3.4.2", title: "Skill: Apply fairness evaluations (CloudWatch fairness metrics, A/B tests with Prompt Management and Prompt Flows, LLM-as-a-judge)" }
  - { id: "3.4.3", title: "Skill: Build policy-compliant AI (policy-based Guardrails, model cards documenting limitations, Lambda compliance checks)" }
  - { id: "4", title: "Operational Efficiency and Optimization for GenAI Applications", weight: "12%" }
  - { id: "4.1", title: "Implement cost optimization and resource efficiency strategies" }
  - { id: "4.1.1", title: "Skill: Improve token efficiency (token estimation and tracking, context window optimization, prompt compression, response limits)" }
  - { id: "4.1.2", title: "Skill: Build cost-effective model selection (cost-capability trade-offs, tiered models by query complexity, price-performance measurement)" }
  - { id: "4.1.3", title: "Skill: Maximize throughput and utilization (batching, capacity planning, auto scaling, provisioned throughput optimization)" }
  - { id: "4.1.4", title: "Skill: Build caching to avoid unnecessary FM calls (semantic caching, result fingerprinting, edge caching, request hashing, prompt caching)" }
  - { id: "4.2", title: "Optimize application performance" }
  - { id: "4.2.1", title: "Skill: Manage latency-cost trade-offs (pre-computation, latency-optimized Bedrock models, parallel requests, streaming, benchmarking)" }
  - { id: "4.2.2", title: "Skill: Improve retrieval performance (index optimization, query preprocessing, hybrid search with custom scoring)" }
  - { id: "4.2.3", title: "Skill: Optimize FM throughput (token processing, batch inference, concurrent invocation management)" }
  - { id: "4.2.4", title: "Skill: Tune FM parameters for use cases (model-specific parameters, A/B testing, temperature and top-k/top-p)" }
  - { id: "4.2.5", title: "Skill: Allocate resources for FM workloads (token capacity planning, prompt and completion monitoring, GenAI-aware auto scaling)" }
  - { id: "4.2.6", title: "Skill: Optimize system performance (API call profiling, vector query optimization, LLM latency reduction, efficient service communication)" }
  - { id: "4.3", title: "Implement monitoring systems for GenAI applications" }
  - { id: "4.3.1", title: "Skill: Build holistic observability (operational metrics, performance and FM interaction tracing, business impact dashboards)" }
  - { id: "4.3.2", title: "Skill: Monitor GenAI-specific KPIs (CloudWatch token usage, hallucination rate and response quality, anomaly detection, Bedrock Model Invocation Logs, cost anomalies)" }
  - { id: "4.3.3", title: "Skill: Build integrated observability for actionable insight (dashboards, compliance monitoring, forensic traceability, user and model behavior tracking)" }
  - { id: "4.3.4", title: "Skill: Monitor tool performance (call patterns, tool-calling and multi-agent coordination observability, usage baselines)" }
  - { id: "4.3.5", title: "Skill: Operate vector stores reliably (vector database monitoring, automated index optimization, data quality validation)" }
  - { id: "4.3.6", title: "Skill: Build GenAI-specific troubleshooting (golden datasets for hallucinations, output diffing, reasoning path tracing)" }
  - { id: "5", title: "Testing, Validation, and Troubleshooting", weight: "11%" }
  - { id: "5.1", title: "Implement evaluation systems for GenAI" }
  - { id: "5.1.1", title: "Skill: Build assessment frameworks for FM output quality (relevance, factual accuracy, consistency, fluency)" }
  - { id: "5.1.2", title: "Skill: Evaluate models systematically (Amazon Bedrock Model Evaluations, A/B and canary testing, multi-model evaluation, cost-performance analysis)" }
  - { id: "5.1.3", title: "Skill: Build user-centered evaluation (feedback interfaces, output ratings, annotation workflows)" }
  - { id: "5.1.4", title: "Skill: Build quality assurance processes (continuous evaluation, output regression testing, automated quality gates)" }
  - { id: "5.1.5", title: "Skill: Evaluate from multiple perspectives (RAG evaluation, LLM-as-a-Judge, human feedback)" }
  - { id: "5.1.6", title: "Skill: Test retrieval quality (relevance scoring, context matching, retrieval latency)" }
  - { id: "5.1.7", title: "Skill: Evaluate agent performance (task completion rate, tool usage effectiveness, Amazon Bedrock Agent evaluations, multi-step reasoning quality)" }
  - { id: "5.1.8", title: "Skill: Report performance to stakeholders (visualizations, automated reporting, model comparisons)" }
  - { id: "5.1.9", title: "Skill: Validate deployments during FM updates (synthetic user workflows, hallucination and semantic drift checks, consistency checks)" }
  - { id: "5.2", title: "Troubleshoot GenAI applications" }
  - { id: "5.2.1", title: "Skill: Resolve content handling issues (context window overflow, dynamic chunking, truncation errors)" }
  - { id: "5.2.2", title: "Skill: Diagnose FM API integration issues (error logging, request validation, response analysis)" }
  - { id: "5.2.3", title: "Skill: Troubleshoot prompt engineering problems (prompt testing frameworks, version comparison, systematic refinement)" }
  - { id: "5.2.4", title: "Skill: Troubleshoot retrieval issues (relevance analysis, embedding quality, drift, vectorization, chunking, vector search performance)" }
  - { id: "5.2.5", title: "Skill: Troubleshoot prompt maintenance (template testing, CloudWatch Logs, X-Ray prompt observability, schema validation)" }
---
## Exam format

All facts are as of 2026-10-24, taken from the [certification page](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/) and the [AIP-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html). Confirm them on the official page before you book.

| Item | AIP-C01 (as of 2026-10-24) |
|---|---|
| Status | The certification page shows no beta notice and lists the standard format below |
| Question types | Multiple choice (one correct answer out of four) and multiple response (two or more correct answers out of five or more; all must be selected for credit) |
| Number of questions | 75 in total: 65 scored and 10 unscored, which you cannot tell apart |
| Duration | 180 minutes |
| Passing score | 750 on a scaled score of 100–1,000, compensatory across domains |
| Price | 300 USD. AWS's exam pricing page has further cost information, including foreign exchange rates |
| Languages | English, Japanese, Korean, Simplified Chinese |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | AWS certifications are valid for 3 years and renewed by passing the current version. The AIP certification page does not repeat this, so confirm it there |
| Prerequisites | None required. AWS recommends 2 or more years building production applications on AWS or with open-source technologies, general AI/ML or data-engineering experience, and 1 year of hands-on generative AI implementation |

AWS lists AWS Certified AI Practitioner, Solutions Architect – Associate, Machine Learning Engineer – Associate and Data Engineer – Associate as optional earlier certifications, not prerequisites. The guide says model development and training, advanced ML techniques, and data and feature engineering are **out of scope**. This is an exam about building *with* foundation models, not about training them.

## What the exam really tests

AIP-C01 checks whether you can take a foundation model (FM) from proof of concept to a production system that is grounded, safe, observable, affordable and governed, mostly with Amazon Bedrock and the AWS services around it. Most of the exam treats GenAI as distributed-systems engineering, with the model as one unreliable, expensive, rate-limited dependency.

- **Domain 1, FM integration, data management and compliance (31%).** The largest domain. It covers choosing models, switching providers without code changes, cross-Region inference for resilience, data validation and multimodal preprocessing, and above all retrieval-augmented generation (RAG): vector store design (Bedrock Knowledge Bases, OpenSearch Service, Aurora with pgvector), chunking, embedding choice, hybrid search, reranking, query rewriting and keeping the index fresh. Prompt management and governance (Bedrock Prompt Management, Prompt Flows, Guardrails) also sits here.
- **Domain 2, implementation and integration (26%).** Agentic AI (Strands Agents, AWS Agent Squad, Model Context Protocol servers on Lambda or ECS, ReAct-style reasoning with Step Functions, human-in-the-loop approval), deployment choices (on-demand, provisioned throughput, SageMaker AI endpoints), enterprise integration (API Gateway, EventBridge, identity federation, Outposts and Wavelength for data residency), streaming responses and resilient API patterns.
- **Domain 3, AI safety, security and governance (20%).** Input and output guardrails, hallucination reduction through grounding and structured output, prompt-injection and jailbreak defence, PII detection and masking (Comprehend, Macie), network isolation with VPC endpoints, lineage and model cards, and responsible-AI transparency and fairness.
- **Domain 4, operational efficiency (12%).** Token economics, model tiering and cascading, semantic and prompt caching, batching, latency-optimized models, parameter tuning (temperature, top-k and top-p), and GenAI-specific monitoring with CloudWatch and Bedrock model invocation logs.
- **Domain 5, testing, validation and troubleshooting (11%).** Evaluation frameworks (Bedrock model evaluations, LLM-as-a-judge, RAG and agent evaluations, golden datasets), regression and quality gates, and troubleshooting context-window overflow, retrieval drift and prompt regressions.

Where candidates lose points:

- **Treating every problem as a prompt problem.** Many scenarios are really fixed by retrieval (better chunking, metadata filters, reranking), by architecture (a cache, a queue, a cheaper model for easy queries) or by a guardrail, not by rewording the prompt.
- **Confusing similar Bedrock features.** Know what Guardrails, Knowledge Bases, Agents, Prompt Management, Prompt Flows, model evaluations, Data Automation, provisioned throughput and cross-Region inference each do, and where they stop.
- **Ignoring the non-AI constraint.** Many questions are decided by IAM least privilege, private connectivity, data residency, cost or latency rather than by the model.
- **Thinking the choice is fine-tuning or nothing.** The guide lists customization deployment (LoRA and adapters, SageMaker Model Registry) as in scope, but it usually prefers RAG and prompt techniques to retraining.

## Study strategy

1. **Foundations.** If AWS is still new to you, cover IAM, VPC endpoints, Lambda, API Gateway, Step Functions, EventBridge, SQS, DynamoDB, S3 and CloudWatch first. The AI Practitioner (AIF-C01) objectives in this library are a gentle on-ramp for the GenAI vocabulary.
2. **Bedrock hands-on.** Call several models through the Converse API from a small .NET or Python app, add streaming, then put Guardrails in front of it. Build a Knowledge Base over a few hundred documents, try different chunking strategies and compare the retrieval results.
3. **RAG depth.** Replace the managed vector store with OpenSearch Service or Aurora with pgvector, add hybrid search and a reranker, and measure the change with an evaluation set. This is where Domain 1 points are won.
4. **Agents and MCP.** Build one agent with Strands Agents that calls two tools, one of them exposed through an MCP server running on Lambda. Wrap a risky action in a Step Functions approval step.
5. **Operations.** Turn on model invocation logging, build a CloudWatch dashboard for tokens, latency and errors, add a semantic cache, and compare cost before and after.
6. **Evaluation.** Run a Bedrock model evaluation and an LLM-as-a-judge evaluation against a golden dataset.

Official resources named on the certification page (as of 2026-10-24) are the AWS Skill Builder **Exam Prep Plan** (four steps), the **Official Practice Question Set**, the **Official Pretest**, digital courses, **AWS Builder Labs**, **AWS Cloud Quest**, **AWS Jam**, instructor walkthroughs of exam-style questions, **AWS SimuLearn** and the **Official Practice Exam**. AWS also links related Skill Builder credentials: AWS Agentic AI Demonstrated, AWS MLOps Demonstrated, AWS Securing Agent Identities Demonstrated and AWS Databases for Agentic AI Demonstrated. The [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is the primary reference.

How your background helps or misleads:

- **AZ-204 preparation and .NET experience** carry over directly: retries with exponential backoff, async messaging, API design, streaming over WebSockets or server-sent events, and secrets handling are all tested here in an FM context. The trap is reaching for Azure names. Azure AI Foundry, Azure AI Search and Azure AI Content Safety map roughly to Bedrock, Knowledge Bases with OpenSearch, and Guardrails, but the features and limits differ.
- **CKAD preparation** helps with the container-hosting questions (MCP servers on ECS, model containers on SageMaker AI), but the exam rarely wants Kubernetes for this.
- **Angular experience** helps with the streaming and UX items. AWS Amplify appears as the front-end option.
- **Agentic AI is your growth track.** This exam is the most direct AWS validation of it, which is why it sits in stage 3.

## Differences from related exams

- **AIP-C01 vs AI-103 (Microsoft's Azure AI app and agent developer exam).** They are counterparts: both are for developers building GenAI and agent applications on a managed platform. AI-103 is associate-level and built around Microsoft Foundry, Azure AI Search, Azure AI services and Microsoft's agent tooling. AIP-C01 is professional-level, with longer scenarios and much more weight on production concerns such as governance, cost, observability and evaluation. Expect AIP to ask "which of these four valid designs is best", where AI-103 asks more about how to configure a specific service.
- **AIP-C01 vs AIF-C01 (AI Practitioner).** AIF is foundational. It covers concepts (what RAG, fine-tuning and responsible AI are) with no implementation depth. AIP assumes all of that and asks you to build it.
- **AIP-C01 vs MLA-C02 (Machine Learning Engineer – Associate).** MLA covers the classic ML lifecycle on SageMaker AI: data preparation, training, tuning and MLOps. AIP excludes model training and covers FM integration instead. The two overlap only on deployment and monitoring.
- **AIP-C01 vs SAP-C03.** SAP is general architecture across an enterprise. AIP is GenAI-specific but just as scenario-heavy. The SAP-C02 emerging topics (Bedrock Guardrails, AgentCore Identity, human approval with Step Functions) overlap AIP Domain 3 almost exactly.
- **AIP-C01 vs NCP-AAI (NVIDIA agentic AI).** NCP-AAI is vendor-specific to NVIDIA's stack and goes deeper into agent architecture and inference infrastructure. AIP is AWS-managed-service first.

## Exam-day notes

- **Time budget.** 180 minutes for 75 questions is about 2 minutes 24 seconds each. Scenarios are a little shorter than SAP's, so aim to finish the first pass in 140 minutes and use the rest on flagged items.
- **Find the deciding constraint.** "Without changing application code" points to AppConfig or a gateway or routing layer. "Least operational overhead" points to managed Bedrock features. "Data must not leave the VPC" points to VPC endpoints or PrivateLink. "Deterministic" points to structured output, text-to-SQL or rules over model judgement.
- **Hallucination questions** are usually answered by grounding, retrieval quality or structured output, not by a lower temperature alone.
- **Cost questions** are usually answered by a smaller or tiered model, caching, batch inference or prompt compression, before provisioned throughput, which suits steady, predictable high volume.
- **Multiple response.** The question tells you how many answers to select. Check each one on its own merits.
- **Name drift.** GenAI service names change quickly (Amazon SageMaker AI, Amazon Q Developer, the Bedrock AgentCore family). Learn the current names and their recent predecessors, because documentation, courses and practice material still mix them.
