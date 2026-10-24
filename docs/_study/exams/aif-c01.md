---
code: AIF-C01
title: "AWS Certified AI Practitioner"
credential: "AWS Certified AI Practitioner"
provider: aws
tracks: [agentic-ai, cloud]
clouds: [aws]
level: foundational
tier: core
stage: "1"
progress: planned
official_url: https://aws.amazon.com/certification/certified-ai-practitioner/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html
outline_version: "1.1 (2026-04-30)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends up to 6 months of exposure to AI/ML technologies on AWS and familiarity with core AWS services, the shared responsibility model, IAM and AWS pricing models."
replaces: ""
replaced_by: ""
counterparts: [ai-901]
objectives:
  - { id: "1", title: "Fundamentals of AI and ML", weight: "20%" }
  - { id: "1.1", title: "Explain basic AI concepts and terminologies" }
  - { id: "1.1.1", title: "Skill: Define basic AI terms (for example, AI, ML, deep learning, neural networks, computer vision, natural language processing [NLP], model, algorithm, training and inferencing, bias, fairness, fit, large language model [LLM], generative AI [GenAI], agentic AI)" }
  - { id: "1.1.2", title: "Skill: Describe the similarities and differences between AI, ML, GenAI, deep learning, and agentic AI" }
  - { id: "1.1.3", title: "Skill: Describe various types of inferencing (for example, batch, real-time, asynchronous, serverless)" }
  - { id: "1.1.4", title: "Skill: Describe the different types of data in AI models (for example, labeled and unlabeled, tabular, time-series, image, text, structured and unstructured)" }
  - { id: "1.1.5", title: "Skill: Describe different types of AI/ML learning (for example, supervised learning, unsupervised learning, reinforcement learning methods)" }
  - { id: "1.2", title: "Identify practical use cases for AI" }
  - { id: "1.2.1", title: "Skill: Recognize applications where AI/ML can provide value (for example, assist human decision making, solution scalability, automation)" }
  - { id: "1.2.2", title: "Skill: Determine when AI/ML solutions are not appropriate (for example, cost-benefit analyses, situations when a specific outcome is needed instead of a prediction)" }
  - { id: "1.2.3", title: "Skill: Select the appropriate AI/ML techniques for specific use cases (for example, regression, classification, clustering)" }
  - { id: "1.2.4", title: "Skill: Identify examples of real-world AI applications (for example, computer vision, NLP, speech recognition, recommendation systems, fraud detection, forecasting, knowledge bases, agentic AI)" }
  - { id: "1.2.5", title: "Skill: Explain the capabilities of AWS managed AI/ML services (for example, Amazon SageMaker AI, Amazon Transcribe, Amazon Translate, Amazon Comprehend, Amazon Lex, Amazon Polly)" }
  - { id: "1.2.6", title: "Skill: Identify when traditional ML models or foundation models (FMs) are appropriate for a specific use case (for example, based on regulatory concerns, explainability requirements, operational constraints)" }
  - { id: "1.3", title: "Describe the AI/ML development lifecycle" }
  - { id: "1.3.1", title: "Skill: Describe and differentiate components of an AI/ML pipeline" }
  - { id: "1.3.2", title: "Skill: Describe sources of FM models (for example, open source pre-trained models, training custom models)" }
  - { id: "1.3.3", title: "Skill: Describe methods to use a model in production (for example, managed API service, self-hosted API)" }
  - { id: "1.3.4", title: "Skill: Identify relevant AWS services and features for each stage of an AI/ML pipeline (for example, Amazon Bedrock, Amazon Quick, Kiro, SageMaker AI)" }
  - { id: "1.3.5", title: "Skill: Describe fundamental concepts of ML operations (MLOps) (for example, experimentation, repeatable processes, scalable systems, managing technical debt, achieving production readiness, model monitoring, model re-training)" }
  - { id: "1.3.6", title: "Skill: Describe model performance metrics (for example, accuracy, precision, recall, F1 score) and business metrics (for example, cost per user, development costs, customer feedback, return on investment [ROI]) to evaluate ML models" }
  - { id: "2", title: "Fundamentals of GenAI", weight: "24%" }
  - { id: "2.1", title: "Explain the basic concepts of generative AI (GenAI)" }
  - { id: "2.1.1", title: "Skill: Define foundational GenAI concepts (for example, tokens, chunking, embeddings, vectors, prompt engineering, transformer-based large language models [LLMs], foundation models [FMs], multi-modal models, diffusion models)" }
  - { id: "2.1.2", title: "Skill: Identify potential use cases for GenAI models (for example, image, video, and audio generation; summarization; AI assistants; translation; code generation; customer service agents; search; recommendation engines)" }
  - { id: "2.1.3", title: "Skill: Describe the FM lifecycle (for example, data selection, model selection, pre-training, fine-tuning, evaluation, deployment, feedback)" }
  - { id: "2.1.4", title: "Skill: Describe the token-based pricing model and its effect on cost and performance for inference" }
  - { id: "2.1.5", title: "Skill: Describe the role of context engineering in FM applications" }
  - { id: "2.1.6", title: "Skill: Define foundational agentic AI concepts (for example, multi-agent system patterns for complex AI applications, Model Context Protocol [MCP] and its role in connecting agents to external systems, multi-agent communication patterns, memory management, tool usage, and workflow orchestration)" }
  - { id: "2.2", title: "Understand the capabilities and limitations of GenAI for solving business problems" }
  - { id: "2.2.1", title: "Skill: Describe the advantages of GenAI (for example, adaptability, responsiveness, conversational capabilities, ability to generate content)" }
  - { id: "2.2.2", title: "Skill: Identify disadvantages of GenAI solutions (for example, hallucinations, interpretability, inaccuracy, nondeterminism)" }
  - { id: "2.2.3", title: "Skill: Identify factors to consider when selecting GenAI models (for example, model types, performance requirements, capabilities, constraints, compliance, cost, latency, model complexity)" }
  - { id: "2.2.4", title: "Skill: Determine business value and metrics for GenAI applications (for example, cross-domain performance, ROI, efficiency, conversion rate, average revenue per user, accuracy, customer lifetime value)" }
  - { id: "2.3", title: "Describe AWS infrastructure and technologies for building GenAI applications" }
  - { id: "2.3.1", title: "Skill: Identify AWS services and features to develop GenAI applications (for example, Amazon Bedrock, Amazon SageMaker AI, SageMaker JumpStart, Amazon Quick, Kiro, Strands Agents, Amazon Bedrock AgentCore)" }
  - { id: "2.3.2", title: "Skill: Describe the advantages of using AWS GenAI services to build applications (for example, accessibility, lower barrier to entry, efficiency, cost-effectiveness, speed to market, ability to meet business objectives)" }
  - { id: "2.3.3", title: "Skill: Describe the benefits of AWS infrastructure for GenAI applications (for example, security, compliance, responsibility, safety)" }
  - { id: "2.3.4", title: "Skill: Describe cost tradeoffs of AWS GenAI services (for example, responsiveness, availability, redundancy, performance, regional coverage, token-based pricing, provision throughput, custom models)" }
  - { id: "3", title: "Applications of Foundation Models", weight: "28%" }
  - { id: "3.1", title: "Describe design considerations for applications that use foundation models (FMs)" }
  - { id: "3.1.1", title: "Skill: Identify selection criteria to choose FMs (for example, cost, modality, latency, multi-lingual, model size, model complexity, customization, input/output length, prompt caching)" }
  - { id: "3.1.2", title: "Skill: Describe the effect of inference parameters on model responses (for example, temperature, input/output length)" }
  - { id: "3.1.3", title: "Skill: Define Retrieval Augmented Generation (RAG) and describe its business applications (for example, Amazon Bedrock Knowledge Bases)" }
  - { id: "3.1.4", title: "Skill: Identify AWS services that help store embeddings within vector databases (for example, Amazon OpenSearch Service, Amazon Aurora, Amazon Neptune, Amazon RDS for PostgreSQL)" }
  - { id: "3.1.5", title: "Skill: Explain the cost tradeoffs of various approaches to FM customization (for example, pre-training, fine-tuning, in-context learning, RAG, model distillation)" }
  - { id: "3.1.6", title: "Skill: Define the role of AI agents and describe AI agents' business applications" }
  - { id: "3.2", title: "Choose effective prompt engineering techniques" }
  - { id: "3.2.1", title: "Skill: Define the concepts and constructs of prompt engineering (for example, context, instruction, negative prompts)" }
  - { id: "3.2.2", title: "Skill: Define techniques for prompt engineering (for example, chain-of-thought, zero-shot, single-shot, few-shot, prompt templates)" }
  - { id: "3.2.3", title: "Skill: Identify and describe the benefits and best practices for prompt engineering (for example, response quality improvement, experimentation, guardrails, discovery, specificity and concision, using multiple comments)" }
  - { id: "3.2.4", title: "Skill: Define potential risks and limitations of prompt engineering (for example, exposure, poisoning, hijacking, jailbreaking)" }
  - { id: "3.2.5", title: "Skill: Describe prompt versioning and management strategies that use Amazon Bedrock Prompt Management" }
  - { id: "3.3", title: "Describe the training and fine-tuning process for FMs" }
  - { id: "3.3.1", title: "Skill: Describe the key elements of training an FM (for example, pre-training, fine-tuning, continuous pre-training, distillation)" }
  - { id: "3.3.2", title: "Skill: Define methods for fine-tuning an FM (for example, instruction tuning, adapting models for specific domains, transfer learning, continuous pre-training)" }
  - { id: "3.3.3", title: "Skill: Describe how to prepare data to fine-tune an FM (for example, data curation, governance, size, labeling, representativeness, reinforcement learning from human feedback [RLHF])" }
  - { id: "3.4", title: "Describe methods to evaluate FM performance" }
  - { id: "3.4.1", title: "Skill: Determine approaches to evaluate FM performance (for example, human-in-the-loop evaluation, benchmark datasets, Amazon Bedrock Model Evaluation)" }
  - { id: "3.4.2", title: "Skill: Identify relevant metrics to assess FM performance (for example, Recall-Oriented Understudy for Gisting Evaluation [ROUGE], Bilingual Evaluation Understudy [BLEU], BERTScore, LLM-as-a-judge)" }
  - { id: "3.4.3", title: "Skill: Determine whether an FM effectively meets business objectives (for example, productivity, user engagement, task engineering)" }
  - { id: "3.4.4", title: "Skill: Identify approaches to evaluate the performance of applications built with FM (for example, RAG, agents, workflows)" }
  - { id: "3.4.5", title: "Skill: Identify business objective alignment metrics for AI applications (for example, task completion rate, user satisfaction, cost per interaction)" }
  - { id: "4", title: "Guidelines for Responsible AI", weight: "14%" }
  - { id: "4.1", title: "Explain the development of AI systems that are responsible" }
  - { id: "4.1.1", title: "Skill: Identify features of responsible AI (for example, bias, fairness, inclusivity, robustness, safety, veracity)" }
  - { id: "4.1.2", title: "Skill: Explain how to use tools to identify features of responsible AI (for example, Amazon Bedrock Guardrails)" }
  - { id: "4.1.3", title: "Skill: Define responsible practices to select a model (for example, environmental considerations, sustainability)" }
  - { id: "4.1.4", title: "Skill: Identify legal risks of working with generative AI (GenAI) (for example, intellectual property infringement claims, biased model outputs, loss of customer trust, end user risk, hallucinations)" }
  - { id: "4.1.5", title: "Skill: Identify characteristics of datasets (for example, inclusivity, diversity, curated data sources, balanced datasets)" }
  - { id: "4.1.6", title: "Skill: Describe effects of bias and variance (for example, effects on demographic groups, inaccuracy, overfitting, underfitting)" }
  - { id: "4.1.7", title: "Skill: Describe tools to detect and monitor bias, trustworthiness, and truthfulness (for example, analyzing label quality, human audits, subgroup analysis)" }
  - { id: "4.2", title: "Recognize the importance of transparent and explainable models" }
  - { id: "4.2.1", title: "Skill: Describe the differences between models that are transparent and explainable and models that are not transparent and explainable" }
  - { id: "4.2.2", title: "Skill: Describe tools to identify transparent and explainable models (for example, Amazon SageMaker Model Cards, Amazon Bedrock Model Evaluations, open source models, data, licensing)" }
  - { id: "4.2.3", title: "Skill: Identify tradeoffs between model safety and transparency (for example, measure interpretability and performance)" }
  - { id: "4.2.4", title: "Skill: Describe principles of human-centered design for explainable AI (for example, user-feedback mechanisms, AI decision transparency)" }
  - { id: "5", title: "Security, Compliance, and Governance for AI Solutions", weight: "14%" }
  - { id: "5.1", title: "Explain methods to secure AI systems" }
  - { id: "5.1.1", title: "Skill: Identify AWS services and features to secure AI systems (for example, IAM roles, policies, and permissions; encryption; Amazon Macie; AWS PrivateLink; AWS shared responsibility model; Amazon Bedrock AgentCore Identity; Policy in AgentCore; Amazon Bedrock Guardrails)" }
  - { id: "5.1.2", title: "Skill: Describe the concept of source citation and documenting data origins (for example, data lineage, data cataloging, Amazon SageMaker Model Cards)" }
  - { id: "5.1.3", title: "Skill: Describe best practices for secure data engineering (for example, assessing data quality, implementing privacy-enhancing technologies, data access control, data integrity)" }
  - { id: "5.1.4", title: "Skill: Describe security and privacy considerations for AI systems (for example, application security, threat detection, vulnerability management, infrastructure protection, prompt injection, encryption at rest and in transit, data leakage prevention, output filtering and validation, audit trail and logging requirements for AI interactions, toxicity)" }
  - { id: "5.1.5", title: "Skill: Describe hallucination detection methods and grounding techniques to improve output accuracy (for example, Retrieval Augmented Generation [RAG] grounding, output validation, confidence scoring)" }
  - { id: "5.2", title: "Recognize governance and compliance regulations for AI systems" }
  - { id: "5.2.1", title: "Skill: Identify AWS services and features to assist with governance and regulation compliance (for example, AWS Config, Amazon Inspector, AWS Artifact, AWS CloudTrail, AWS Trusted Advisor)" }
  - { id: "5.2.2", title: "Skill: Describe data governance strategies (for example, data lifecycles, logging, residency, monitoring, observation, retention)" }
  - { id: "5.2.3", title: "Skill: Describe processes to follow governance protocols (for example, policies, review cadence, review strategies, governance frameworks such as the Generative AI Security Scoping Matrix, transparency standards, team training requirements)" }
---
## Exam format

Every fact below is as of 2026-10-24 and comes from the [certification page](https://aws.amazon.com/certification/certified-ai-practitioner/) and the [AIF-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html). Confirm both before you book.

| Item | Detail (as of 2026-10-24) |
| --- | --- |
| Category | Foundational |
| Question types | Multiple choice, multiple response, **ordering** (put 3–5 responses in the correct sequence) and **matching** (pair responses with 3–7 prompts). Ordering and matching questions give credit only when the whole answer is correct, with no partial credit |
| Number of questions | 65: 50 scored and 15 unscored (the unscored ones are not marked) |
| Duration | 90 minutes |
| Passing score | 700 on a scaled score of 100–1,000. Scoring is compensatory |
| Price | 100 USD (see [exam pricing](https://aws.amazon.com/certification/policies/before-testing/)) |
| Languages | Arabic, English, French (France), German, Italian, Japanese, Korean, Portuguese (Brazil), Spanish (Latin America), Spanish (Spain), Simplified Chinese and Traditional Chinese. On 2026-10-24 the page still lists Italian and German but also says those versions will be retired after October 15, 2026, a date that has passed. Check before you book in either language |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | Valid for 3 years. You can recertify by passing the latest AIF version, or automatically by earning AWS Certified Machine Learning Engineer – Associate (see [recertification](https://aws.amazon.com/certification/recertification/)) |

The outline transcribed here is **version 1.1 of the guide, published April 30, 2026**. Version 1.0 was published March 26, 2026. The [revisions page](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-revisions.html) lists what changed: agentic AI terms, asynchronous and serverless inference, context engineering, Model Context Protocol, Amazon Bedrock AgentCore, Strands Agents, Kiro and Amazon Quick were added. AWS says it publishes guide updates about a month before the exam reflects them, so study from v1.1.

## What the exam really tests

AIF-C01 is aimed at someone who **uses** AI/ML on AWS but does not necessarily build it. The guide puts coding models, feature engineering, hyperparameter tuning, building pipelines, statistical analysis and writing governance frameworks out of scope. What it tests is whether you can pick the right approach and the right AWS service, and explain the trade-offs:

- **Fundamentals of AI and ML (20%)**: the difference between AI, ML, deep learning, GenAI and agentic AI; types of learning; batch, real-time, asynchronous and serverless inference; when AI is the wrong tool; choosing between a traditional ML model and a foundation model; the managed AI services (SageMaker AI, Transcribe, Translate, Comprehend, Lex, Polly); MLOps ideas; precision, recall and F1 compared with business metrics.
- **Fundamentals of GenAI (24%)**: tokens, chunking, embeddings, vectors, transformers, multimodal and diffusion models, the foundation model lifecycle, token-based pricing, context engineering, and now **agentic AI basics** (multi-agent patterns, MCP, agent memory). It also covers the AWS GenAI stack: Amazon Bedrock, SageMaker JumpStart, Amazon Quick, Kiro, Strands Agents, Amazon Bedrock AgentCore, and the cost trade-offs of on-demand compared with provisioned throughput.
- **Applications of Foundation Models (28%)**: the heaviest domain. It covers criteria for choosing a model, inference parameters (temperature, length), RAG with Amazon Bedrock Knowledge Bases, vector stores (OpenSearch Service, Aurora, Neptune, RDS for PostgreSQL), and the cost order of customisation methods (in-context learning, RAG, fine-tuning, distillation, pre-training). It also covers prompt-engineering techniques and their risks (poisoning, hijacking, jailbreaking), Bedrock Prompt Management, ways to fine-tune, and evaluation (human review, benchmark datasets, Bedrock Model Evaluation, ROUGE, BLEU, BERTScore, LLM-as-a-judge).
- **Guidelines for Responsible AI (14%)**: bias, fairness, robustness and veracity; Amazon Bedrock Guardrails; legal risks; bias compared with variance; transparency and explainability tools such as SageMaker Model Cards.
- **Security, Compliance, and Governance for AI Solutions (14%)**: IAM, encryption, Macie, PrivateLink, AgentCore Identity and Policy; data lineage; prompt injection and data leakage; ways to detect hallucinations and ground answers; AWS Config, Inspector, Artifact, CloudTrail and Trusted Advisor for governance; and the Generative AI Security Scoping Matrix.

Questions describe a business need and ask for a technique, metric or service. The cheapest marks to lose are **customisation cost ordering** (prompt engineering and RAG before fine-tuning, and fine-tuning before pre-training), **choosing the metric** (ROUGE for summarisation, BLEU for translation, F1 when classes are imbalanced), and **service boundaries**: Comprehend analyses text, Textract extracts text from documents, Rekognition analyses images, Kendra is enterprise search, Bedrock gives access to foundation models, and SageMaker AI is for building and training your own models. Ordering and matching questions punish knowledge that is only half there, because a single misplaced item makes the whole answer wrong.

## Study strategy

1. **Do the concepts before the services.** Learn ML vocabulary and evaluation metrics first, then GenAI ideas (tokens, embeddings, RAG, fine-tuning, agents). Only then map them onto AWS services. If you start with the service list, you will be memorising names that have nothing to attach to.
2. **Build one small thing on Amazon Bedrock.** Call a model from the console playground and then through the SDK, change the temperature, create a Knowledge Base over a few documents, and add a Guardrail. With your .NET background, the AWS SDK for .NET can call Bedrock Runtime directly. That single exercise covers a large share of Domain 3.
3. **Learn the agent vocabulary deliberately.** Your agentic-AI track will benefit: know what MCP standardises (how an agent connects to tools and data), what AgentCore offers (runtime, identity, memory, observability and policy for agents), and what Strands Agents is (an open-source SDK for building agents).
4. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (the foundational AI courses, the Official Practice Question Set, the Official Pretest and the Official Practice Exam), the [exam guide](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html) with its in-scope and out-of-scope service lists, and AWS Builder Labs, AWS Cloud Quest and AWS Jam for practice. The certification page says that holders of Cloud Practitioner or an Associate certification can skip the foundational cloud courses.
5. **How your background helps or misleads.** AZ-900 helps with the cloud basics. If you have studied AI-901 or Azure AI services, the concepts carry over one to one, but the service names do not: Microsoft Foundry corresponds roughly to Amazon Bedrock plus SageMaker AI, Azure AI Search to OpenSearch Service or Kendra, and Azure AI Content Safety to Bedrock Guardrails. Your developer instinct will push you to "fine-tune it". On this exam the expected first answer is usually prompt engineering or RAG, because they are cheaper and faster.

Take AIF-C01 at stage 1 together with CLF-C02. It is a good early win for the agentic AI track, and MLA-C02 later recertifies it automatically.

## Differences from related exams

- **AIF-C01 compared with AI-901 (Azure AI Fundamentals, its counterpart).** Both are foundational, concept-first AI exams with a vendor service layer. AI-901 has two skill areas: AI concepts (40–45%) and building AI solutions with Microsoft Foundry (55–60%). It leans more towards "which Foundry capability do I use". AIF-C01 spreads its weight over five domains and gives 28% to security, compliance, governance and responsible AI, and its question formats (ordering, matching) are more varied. AIF-C01 also now asks explicitly about agent protocols (MCP) and AgentCore.
- **AIF-C01 compared with CLF-C02.** The AWS page says CLF has a single AI task (Task 3.7). AIF is AI throughout. Both are 100 USD and 90 minutes.
- **AIF-C01 compared with AIB-C01 (AWS Certified AI Business Strategist).** AWS describes AIB as testing business judgement (which investments to make, the business case, governance and adoption) and as not assessing AWS AI services. AIF does test the services.
- **AIF-C01 compared with MLA-C02.** MLA is the hands-on version: you build data pipelines, train and tune with SageMaker AI, deploy endpoints and agents, and run MLOps. Topics that AIF lists as out of scope (feature engineering, hyperparameter tuning, pipelines) are the core of MLA.
- **AIF-C01 compared with AIP-C01 (AWS Certified Generative AI Developer – Professional).** AIP goes deep on building GenAI and agentic applications in production. AIF is the vocabulary that AIP assumes you already have.

## Exam-day notes

- You have 65 questions in 90 minutes. Ordering and matching items take longer, so budget about 2 minutes for each of those and make it up on the short multiple-choice questions.
- In ordering questions, first find the item that is clearly first and the one that is clearly last, then place the middle ones. For the ML pipeline, the usual order is collect, explore, pre-process, engineer features, train, tune, evaluate, deploy, monitor.
- Traps: "reduce hallucinations using company data" points to RAG, not fine-tuning; "consistent output" points to a lower temperature; "filter harmful content or block denied topics" points to Bedrock Guardrails; "explain model decisions to auditors" points to Model Cards and explainability, not accuracy metrics; and the answer that leaves the customer the least to manage (managed API, serverless inference) usually wins when the stem stresses operational simplicity.
- Flag the questions you are unsure of and come back to them. Never leave a question blank.
