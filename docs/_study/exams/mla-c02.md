---
code: MLA-C02
title: "AWS Certified Machine Learning Engineer – Associate"
credential: "AWS Certified Machine Learning Engineer – Associate"
provider: aws
tracks: [agentic-ai, cloud]
clouds: [aws]
level: associate
tier: elective
stage: "3"
progress: planned
official_url: https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html
outline_version: "2026-09-01 (beta release)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends at least 1 year using Amazon SageMaker AI, Amazon Bedrock and other AWS ML services, at least 1 year in a related role (backend developer, DevOps, data engineer or data scientist), and experience with both traditional ML and generative AI."
replaces: "mla-c01"
replaced_by: ""
counterparts: [ai-300]
objectives:
  - { id: "1", title: "Data Preparation for ML and AI", weight: "28%" }
  - { id: "1.1", title: "Collect and store data" }
  - { id: "1.1.1", title: "Skill: Extract data from data sources (for example, Amazon S3, Amazon EBS, Amazon EFS, Amazon RDS, Amazon DynamoDB, Amazon OpenSearch Service)" }
  - { id: "1.1.2", title: "Skill: Make storage decisions and configure storage services based on cost, performance, data structure, and data compliance" }
  - { id: "1.1.3", title: "Skill: Troubleshoot and debug data ingestion and storage issues that involve capacity and scalability" }
  - { id: "1.1.4", title: "Skill: Use AWS streaming data sources to ingest data (for example, by using Amazon Kinesis, Apache Flink, Apache Kafka)" }
  - { id: "1.1.5", title: "Skill: Ingest from and write by using appropriate data formats (for example, Apache Parquet, JSON, CSV, ORC) based on data access patterns" }
  - { id: "1.1.6", title: "Skill: Merge data from multiple sources (for example, by using programming techniques, AWS Glue, Apache Spark)" }
  - { id: "1.1.7", title: "Skill: Configure scalable vector databases for AI applications (for example, OpenSearch Service, Amazon RDS with pgvector, Amazon S3) based on specifications" }
  - { id: "1.1.8", title: "Skill: Ingest and store diverse data types (for example, text, images, audio) for AI and ML applications" }
  - { id: "1.1.9", title: "Skill: Ingest data into SageMaker Feature Store" }
  - { id: "1.2", title: "Perform data transformation, feature engineering, and pre-processing" }
  - { id: "1.2.1", title: "Skill: Transform data by using AWS tools (for example, AWS Glue, AWS Glue DataBrew, Spark on Amazon EMR, SageMaker Data Wrangler)" }
  - { id: "1.2.2", title: "Skill: Create and manage features by using AWS tools (for example, SageMaker Feature Store)" }
  - { id: "1.2.3", title: "Skill: Transform streaming data (for example, by using AWS Lambda, Spark)" }
  - { id: "1.2.4", title: "Skill: Perform feature engineering (for example, scaling, standardization, feature splitting, binning, log transformation, normalization)" }
  - { id: "1.2.5", title: "Skill: Configure and use embedding models to transform text and image data into numerical representations" }
  - { id: "1.2.6", title: "Skill: Apply advanced text pre-processing techniques (for example, tokenization, domain-specific augmentation)" }
  - { id: "1.2.7", title: "Skill: Prepare documents for Retrieval Augmented Generation (RAG) applications (for example, chunking strategies, metadata extraction)" }
  - { id: "1.2.8", title: "Skill: Mask, redact, and anonymize data" }
  - { id: "1.2.9", title: "Skill: Prepare data for FM fine-tuning, continuous pre-training, and model distillation" }
  - { id: "1.3", title: "Validate data quality and manage bias" }
  - { id: "1.3.1", title: "Skill: Validate data quality (for example, by using DataBrew, AWS Glue Data Quality)" }
  - { id: "1.3.2", title: "Skill: Label and annotate data" }
  - { id: "1.3.3", title: "Skill: Identify and mitigate sources of bias in data by using AWS tools and techniques (for example, dataset splitting, shuffling, augmentation)" }
  - { id: "1.3.4", title: "Skill: Optimize multimodal data distributions by applying bias metrics across numeric, text, and image assets" }
  - { id: "1.3.5", title: "Skill: Resolve class imbalance in numeric, text, and image datasets" }
  - { id: "1.3.6", title: "Skill: Validate AI training data integrity (for example, prompt-response pair validation, content safety screening)" }
  - { id: "1.3.7", title: "Skill: Clean data (for example, by detecting outliers, imputing missing data, deduplication)" }
  - { id: "2", title: "ML Model and Foundation Model (FM) Development", weight: "24%" }
  - { id: "2.1", title: "Choose appropriate modeling approaches for ML and AI solutions" }
  - { id: "2.1.1", title: "Skill: Evaluate and select appropriate FMs from Amazon Bedrock based on task requirements and performance criteria" }
  - { id: "2.1.2", title: "Skill: Identify fine-tuning strategies for pre-trained FMs to meet business needs" }
  - { id: "2.1.3", title: "Skill: Compare and select appropriate ML models, generative AI (GenAI) models, algorithms, and solution templates to meet business needs (for example, interpretability, domain-specific performance, latency)" }
  - { id: "2.1.4", title: "Skill: Evaluate tradeoffs between custom solutions, managed services, pre-trained models, and FMs to meet business needs" }
  - { id: "2.1.5", title: "Skill: Select Retrieval Augmented Generation (RAG) architecture patterns based on use case requirements" }
  - { id: "2.1.6", title: "Skill: Assess tradeoffs between ML model performance, training time, and cost" }
  - { id: "2.1.7", title: "Skill: Assess tradeoffs between AI model performance, latency, and cost" }
  - { id: "2.1.8", title: "Skill: Apply AWS AI services to solve specific business problems (for example, Amazon Textract, Amazon Rekognition, Amazon Comprehend, Amazon Transcribe)" }
  - { id: "2.2", title: "Train, fine-tune, and customize models for ML and AI solutions" }
  - { id: "2.2.1", title: "Skill: Apply Amazon SageMaker AI built-in algorithms and common ML libraries" }
  - { id: "2.2.2", title: "Skill: Configure SageMaker AI script mode with supported frameworks for simplicity and performance" }
  - { id: "2.2.3", title: "Skill: Implement hyperparameter optimization (for example, SageMaker AI automatic model tuning [AMT])" }
  - { id: "2.2.4", title: "Skill: Implement training time reduction techniques (for example, early stopping, distributed training)" }
  - { id: "2.2.5", title: "Skill: Prevent model overfitting, underfitting, and catastrophic forgetting" }
  - { id: "2.2.6", title: "Skill: Combine multiple ML models to improve performance or reduce cost" }
  - { id: "2.2.7", title: "Skill: Adjust fundamental hyperparameters (for example, epoch, steps, batch size)" }
  - { id: "2.2.8", title: "Skill: Apply customization techniques for AI solutions (for example, task-specific prompt engineering, fine-tuning)" }
  - { id: "2.2.9", title: "Skill: Optimize retrieval components and embedding models" }
  - { id: "2.3", title: "Analyze and evaluate the performance of ML and AI systems" }
  - { id: "2.3.1", title: "Skill: Perform reproducible experiments (for example, by using MLflow on SageMaker AI, Amazon Bedrock evaluations, Amazon Bedrock Prompt Management)" }
  - { id: "2.3.2", title: "Skill: Create model performance baselines and implement drift detection" }
  - { id: "2.3.3", title: "Skill: Compare the performance of shadow variants to production variants" }
  - { id: "2.3.4", title: "Skill: Explain model outputs" }
  - { id: "2.3.5", title: "Skill: Debug model convergence issues" }
  - { id: "2.3.6", title: "Skill: Apply comprehensive model evaluation techniques for traditional ML and GenAI models" }
  - { id: "2.3.7", title: "Skill: Implement integrated human evaluation frameworks (for example, human-in-the-loop workflows, text generation quality assessment)" }
  - { id: "2.3.8", title: "Skill: Apply natural language processing (NLP) evaluation metrics (for example, bilingual evaluation understudy [BLEU], Recall-Oriented Understudy for Gisting Evaluation [ROUGE], BERTScore, semantic similarity)" }
  - { id: "2.3.9", title: "Skill: Perform AI evaluation (for example, model output assessment, content quality validation, bias detection, LLM-as-a-judge frameworks)" }
  - { id: "2.3.10", title: "Skill: Configure RAG system monitoring, including retrieval accuracy assessment" }
  - { id: "3", title: "Deployment and Orchestration of ML and AI Workflows", weight: "24%" }
  - { id: "3.1", title: "Manage deployment infrastructure for ML and AI model types" }
  - { id: "3.1.1", title: "Skill: Select appropriate compute environments and deployment targets" }
  - { id: "3.1.2", title: "Skill: Select deployment orchestrators and multi-model or multi-container deployment strategies" }
  - { id: "3.1.3", title: "Skill: Select model inference strategies (for example, real-time and batch processing)" }
  - { id: "3.1.4", title: "Skill: Evaluate and select appropriate foundation model (FM) deployment options" }
  - { id: "3.1.5", title: "Skill: Deploy models that were built outside of AWS into AWS environments (for example, Amazon SageMaker AI, Amazon Bedrock Custom Model Import)" }
  - { id: "3.1.6", title: "Skill: Deploy and configure agents for specific tasks, integration with other services and tools, and agent communication protocols" }
  - { id: "3.1.7", title: "Skill: Configure FM deployment, model hosting, and resource allocation" }
  - { id: "3.1.8", title: "Skill: Apply Retrieval Augmented Generation (RAG) system configurations (for example, retrieval strategies, reranking)" }
  - { id: "3.2", title: "Provision and configure resources for ML and AI workloads based on existing architecture and requirements" }
  - { id: "3.2.1", title: "Skill: Optimize resource provisioning between on-demand and provisioned resources for performance and cost efficiency" }
  - { id: "3.2.2", title: "Skill: Automate compute resource provisioning with integrated communication between stacks and orchestration services" }
  - { id: "3.2.3", title: "Skill: Build and maintain containers for ML and AI workloads" }
  - { id: "3.2.4", title: "Skill: Configure SageMaker AI endpoints within VPC network environments" }
  - { id: "3.2.5", title: "Skill: Deploy and host models programmatically (for example, by using the SageMaker AI SDK for Python, AWS CLI, Boto3)" }
  - { id: "3.2.6", title: "Skill: Select specific metrics for auto scaling implementations" }
  - { id: "3.2.7", title: "Skill: Create and manage Amazon Bedrock knowledge bases with vector database configurations, document indexing, and retrieval optimization" }
  - { id: "3.2.8", title: "Skill: Implement retrieval pipelines to meet business needs" }
  - { id: "3.2.9", title: "Skill: Implement agent state management systems" }
  - { id: "3.2.10", title: "Skill: Implement AI-specific resource scaling for GPU workloads" }
  - { id: "3.2.11", title: "Skill: Deploy agentic workflow infrastructure" }
  - { id: "3.3", title: "Implement automated orchestration and continuous integration and continuous delivery (CI/CD) pipelines for MLOps and AI workloads" }
  - { id: "3.3.1", title: "Skill: Implement automated deployment strategies and rollback actions" }
  - { id: "3.3.2", title: "Skill: Configure and troubleshoot AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, AWS CodePipeline, and AWS CodeConnections" }
  - { id: "3.3.3", title: "Skill: Configure training and inference jobs" }
  - { id: "3.3.4", title: "Skill: Configure automated testing strategies within CI/CD pipelines for traditional ML and AI workloads" }
  - { id: "3.3.5", title: "Skill: Build and integrate mechanisms to re-train models" }
  - { id: "3.3.6", title: "Skill: Manage model versions for repeatability and audits (for example, SageMaker Model Registry, MLflow on SageMaker AI)" }
  - { id: "3.3.7", title: "Skill: Manage prompts (for example, Amazon Bedrock Prompt Management)" }
  - { id: "3.3.8", title: "Skill: Implement automated agent deployment pipelines and agent version management" }
  - { id: "3.3.9", title: "Skill: Implement AI model testing frameworks, including prompt testing" }
  - { id: "3.3.10", title: "Skill: Configure FM deployment automation with fine-tuned model versioning" }
  - { id: "3.3.11", title: "Skill: Configure AI-specific pipeline orchestration for RAG system updates and knowledge base refresh cycles" }
  - { id: "4", title: "Operating, Monitoring, and Securing ML and AI Solutions", weight: "24%" }
  - { id: "4.1", title: "Monitor ML and AI model inference and performance" }
  - { id: "4.1.1", title: "Skill: Monitor model performance in production by using Amazon CloudWatch generative AI observability, Amazon Bedrock Model Evaluation, and drift detection pipelines" }
  - { id: "4.1.2", title: "Skill: Monitor workflows to detect anomalies or errors in data processing or model inference" }
  - { id: "4.1.3", title: "Skill: Detect changes in data distribution that can affect model performance" }
  - { id: "4.1.4", title: "Skill: Monitor model performance in production by using A/B testing" }
  - { id: "4.1.5", title: "Skill: Monitor and automate the management of agent performance and coordination (for example, coordination failure detection, truncated streaming, tool failures)" }
  - { id: "4.1.6", title: "Skill: Configure AI-specific performance monitoring for foundation models (FMs), such as Amazon Bedrock evaluations" }
  - { id: "4.2", title: "Optimize and manage ML and AI infrastructure costs and performance" }
  - { id: "4.2.1", title: "Skill: Select inference instance families to optimize performance and cost" }
  - { id: "4.2.2", title: "Skill: Configure and use tools to troubleshoot and analyze resources (for example, Amazon CloudWatch, Amazon Bedrock AgentCore Observability, AWS X-Ray)" }
  - { id: "4.2.3", title: "Skill: Set up dashboards to monitor performance metrics" }
  - { id: "4.2.4", title: "Skill: Optimize capacity for cost, performance, and reliability" }
  - { id: "4.2.5", title: "Skill: Optimize costs and set cost quotas by using appropriate cost management tools" }
  - { id: "4.2.6", title: "Skill: Optimize infrastructure costs by selecting purchasing options" }
  - { id: "4.2.7", title: "Skill: Evaluate cost implications of using FMs for inference in production" }
  - { id: "4.2.8", title: "Skill: Monitor agent resource consumption patterns" }
  - { id: "4.2.9", title: "Skill: Manage FM inference costs with usage optimization" }
  - { id: "4.2.10", title: "Skill: Monitor AI-specific cost patterns (for example, token usage optimization, embedding computation costs, vector database storage optimization)" }
  - { id: "4.3", title: "Secure ML and AI workloads and model endpoints" }
  - { id: "4.3.1", title: "Skill: Secure continuous integration and continuous delivery (CI/CD) pipelines by checking for code and image vulnerabilities (for example, by using Amazon CodeGuru, Amazon Inspector)" }
  - { id: "4.3.2", title: "Skill: Configure least privilege access to ML and AI artifacts" }
  - { id: "4.3.3", title: "Skill: Configure IAM policies and roles for users and applications in ML and AI systems" }
  - { id: "4.3.4", title: "Skill: Configure comprehensive monitoring, auditing, compliance, and logging for ML and AI systems (for example, AWS CloudTrail, AWS Config)" }
  - { id: "4.3.5", title: "Skill: Troubleshoot and debug security issues in ML and AI systems" }
  - { id: "4.3.6", title: "Skill: Create VPCs, subnets, and security groups to securely isolate ML and AI systems" }
  - { id: "4.3.7", title: "Skill: Identify and mitigate security risks and vulnerabilities in ML and AI systems" }
  - { id: "4.3.8", title: "Skill: Select the appropriate credential type to access FMs (for example, Amazon Bedrock API keys, IAM credentials)" }
  - { id: "4.3.9", title: "Skill: Implement safeguards and sensitive data protection to meet application requirements and responsible AI policies (for example, by using Amazon Bedrock Guardrails)" }
---
## Exam format

Every fact below is as of 2026-10-24 and comes from the [certification page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/), the [MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html) and the [AWS blog announcement of September 1, 2026](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/). MLA-C02 is **in beta**, so check all three again before you book.

| Item | MLA-C02 beta (now) | MLA-C02 GA (planned) |
| --- | --- | --- |
| Category | Associate | Associate |
| Exam code shown at registration | ME1-C02 (the beta code on the certification page) | MLA-C02 |
| Question types | Multiple choice and multiple response | Same, according to the guide |
| Number of questions | 85. The extra items are for statistical evaluation and do not affect your score | The guide says 65: 50 scored and 15 unscored |
| Duration | 170 minutes | Not yet stated on the certification page. MLA-C01 had 130 minutes |
| Passing score | The guide gives 720 out of 1,000 (scaled, compensatory), but a footnote says its pass/fail statement does not apply to the beta. See AWS's [before-testing policies](https://aws.amazon.com/certification/policies/before-testing/) for how beta exams work. Beta results typically arrive within 5 business days | 720 out of 1,000 |
| Price | 75 USD (beta price) | Not yet stated. MLA-C01 costs 150 USD |
| Languages | English only | English, Japanese, Korean and Simplified Chinese at GA |
| Delivery | Pearson VUE test centre or online proctored | Same |
| Key dates | Beta registration opened September 1, 2026; MLA-C01 in English ended September 28, 2026; beta delivery started September 29, 2026 | The AWS blog gives **January 14, 2027** for GA delivery in all languages, and MLA-C01 retires in all languages on that date. The certification page still shows "TBD" for GA registration and delivery |
| Validity and renewal | Valid for 3 years. You can recertify by passing the latest version (see [recertification](https://aws.amazon.com/certification/recertification/)). Earning MLA also recertifies AWS Certified AI Practitioner automatically | Same |

The guide on AWS's site has no revision table. This library records it as the **beta release of September 1, 2026**, the day the blog says the guide was released. The guide is published, so this page is not provisional. Expect AWS to revise it before GA, and check the [comparison page](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/mla-02-comparison.html) for changes.

## What the exam really tests

MLA-C02 tests the **ML engineer who puts both traditional ML and foundation-model systems into production**. That means preparing data, choosing and training or customising models, deploying and orchestrating them (agents included), then monitoring, optimising cost and securing everything. The guide puts designing complete end-to-end AI solutions, setting ML strategy, broad integration with new tools and deep work in two or more ML domains out of scope. The domain structure is the same as MLA-C01, but every domain now has GenAI and agentic skills:

- **Data Preparation for ML and AI (28%)**: extracting data from S3, EBS, EFS, RDS, DynamoDB and OpenSearch; formats (Parquet, ORC, JSON, CSV); streaming with Kinesis, Flink and Kafka; Glue, DataBrew, EMR Spark and SageMaker Data Wrangler; SageMaker Feature Store; feature engineering; **embedding models, vector databases (OpenSearch Service, RDS with pgvector, S3), RAG document chunking and metadata, masking and redaction, and preparing data for fine-tuning, continued pre-training and distillation**; data quality (Glue Data Quality), labelling, bias metrics, class imbalance and validating prompt-response pairs.
- **ML Model and Foundation Model (FM) Development (24%)**: choosing a Bedrock FM compared with a SageMaker AI built-in algorithm compared with a managed AI service (Textract, Rekognition, Comprehend, Transcribe); fine-tuning strategies; RAG architecture patterns; script mode, automatic model tuning, early stopping and distributed training; overfitting, underfitting and catastrophic forgetting; ensembles; reproducible experiments with MLflow on SageMaker AI and Bedrock evaluations; drift baselines, shadow variants and explainability; NLP metrics (BLEU, ROUGE, BERTScore), human-in-the-loop evaluation, LLM-as-a-judge and monitoring RAG retrieval accuracy.
- **Deployment and Orchestration of ML and AI Workflows (24%)**: real-time, serverless, asynchronous and batch inference; multi-model and multi-container endpoints; Bedrock Custom Model Import; **deploying and configuring agents, agent communication protocols, agent state management and agentic workflow infrastructure**; Bedrock Knowledge Bases and retrieval pipelines with reranking; GPU scaling; endpoints inside a VPC; containers; CI/CD with CodePipeline, CodeBuild, CodeDeploy and CodeConnections; retraining mechanisms; Model Registry; Bedrock Prompt Management; agent deployment pipelines and versioning; prompt testing; and refresh cycles for knowledge bases.
- **Operating, Monitoring, and Securing ML and AI Solutions (24%)**: CloudWatch generative AI observability, Bedrock Model Evaluation and drift pipelines; A/B testing; agent coordination failures and tool failures; choosing instance families and purchasing options; AgentCore Observability and X-Ray; **FM inference cost and token usage**; vector storage cost; CI/CD image scanning (CodeGuru, Inspector); least privilege for ML artifacts; VPC isolation; Bedrock API keys compared with IAM credentials; and Bedrock Guardrails for sensitive data and responsible AI.

Questions are engineering scenarios: "the model degrades after deployment", "inference costs spike", "the agent times out calling a tool", "the RAG answers miss recent documents". Candidates lose points on **SageMaker AI deployment options** (real-time compared with serverless compared with asynchronous compared with batch transform, and when each one fits by payload size, latency and traffic pattern), **customisation choices** (prompt engineering compared with RAG compared with fine-tuning compared with distillation, and their cost order), **evaluation metrics**, and the many new **Bedrock and AgentCore names**. Learn exactly what Knowledge Bases, Guardrails, Prompt Management, Custom Model Import, AgentCore Observability and Bedrock API keys each do.

## Study strategy

1. **Foundations first: ML concepts, then SageMaker AI, then Bedrock.** If ML is new to you, do AIF-C01 first, because MLA assumes its vocabulary. Then learn the SageMaker AI training and hosting lifecycle (jobs, built-in algorithms, script mode, AMT, endpoints, Model Registry, Pipelines, Model Monitor). Then learn Bedrock (models, inference parameters, Knowledge Bases, Guardrails, evaluations, Prompt Management, customisation, Custom Model Import) and AgentCore.
2. **Hands-on work that matters**:
    - Train an XGBoost model with a SageMaker AI built-in algorithm, tune it with AMT, register it, and deploy it once to a real-time endpoint and once as a batch transform. Enable Model Monitor.
    - Build a RAG application: chunk documents, create a Bedrock Knowledge Base on OpenSearch Serverless or S3 Vectors, add a Guardrail, and evaluate it with Bedrock evaluations (including LLM-as-a-judge).
    - Deploy a small agent on AgentCore with one tool, watch its traces in AgentCore Observability and CloudWatch, then put it behind a CodePipeline.
    - Use Python with the SageMaker Python SDK and Boto3. The exam names these SDKs.
3. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (the Official Practice Question Set, the Official Pretest, digital courses, AWS Builder Labs, AWS Cloud Quest, AWS Jam, AWS SimuLearn and the Official Practice Exam; check which ones are updated for C02); the [MLA-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html), its [in-scope services](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/mla-02-in-scope-services.html) and [comparison with MLA-C01](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/mla-02-comparison.html). The certification page lists the related AWS MLOps Demonstrated and AWS Agentic AI Demonstrated credentials.
4. **How your background helps or misleads.** **CKAD** helps with containers for training and inference, and with the idea of autoscaling on custom metrics. **AZ-204 and .NET** help with CI/CD and IAM-style security, but the exam's code world is Python. Practise reading SageMaker SDK and Boto3 snippets. Your **agentic AI track** pays off in Domain 3 (agent deployment, state and protocols) and Domain 4 (agent monitoring and cost). If you know Azure ML or Foundry, the concepts map one to one: Azure ML managed online endpoints to SageMaker AI real-time endpoints, the Azure ML registry to Model Registry, Prompt Flow evaluations to Bedrock evaluations, and Azure AI Content Safety to Guardrails. AWS splits "your own models" (SageMaker AI) from "managed FMs" (Bedrock) more sharply than Foundry does, and many questions turn on that split.

Decide by timing. The beta costs half price and is in English only, and it is long (170 minutes, 85 items), with results within about 5 business days. GA is planned for January 14, 2027. As a stage 3 elective, you can take the beta if you are ready now, or plan for GA in early 2027.

## Differences from related exams

- **MLA-C02 compared with AI-300 (Microsoft's MLOps and GenAIOps associate exam, the counterpart).** Both cover running traditional ML and GenAI in production. AI-300 is organised around **infrastructure and quality assurance**: MLOps infrastructure, model lifecycle, GenAIOps infrastructure in Foundry, GenAI evaluation and observability, and optimisation, with Bicep, Azure CLI and GitHub Actions. MLA-C02 gives 28% to **data preparation** (feature engineering, bias, RAG document preparation), which AI-300 treats lightly, and goes deeper into **agents** (deployment, state, protocols, coordination monitoring) and **cost** (token usage, purchasing options, GPU scaling).
- **MLA-C02 compared with MLA-C01 (its predecessor).** The four domains stay the same, with slightly different weights (C01: 28 / 26 / 22 / 24; C02: 28 / 24 / 24 / 24). C02 adds vector databases, embeddings, RAG preparation and configuration, FM selection and fine-tuning, NLP and LLM evaluation, agent deployment and monitoring, Bedrock Knowledge Bases, Prompt Management and Custom Model Import, and FM cost management. The beta format is longer (170 minutes and 85 items, against 130 minutes and 65 items).
- **MLA-C02 compared with AIF-C01.** AIF asks what the technique is and when to use it, and it excludes building. MLA asks you to build, deploy and operate it. Earning MLA recertifies AIF.
- **MLA-C02 compared with AIP-C01 (Generative AI Developer – Professional).** AIP is a professional-level exam focused on GenAI and agentic application design. MLA covers traditional ML as well as GenAI, at associate level, from the operations side.
- **MLA-C02 compared with DEA-C01.** DEA builds the data platform. MLA prepares data specifically for models, then trains, deploys and monitors them. DEA's Glue, Athena and Lake Formation knowledge carries straight into MLA's Domain 1.

## Exam-day notes

- **Beta**: 85 items in 170 minutes is two minutes each, the same pace as the GA associate exams, but it lasts nearly three hours. Plan a steady pace and take a short pause halfway if the delivery rules allow it.
- Read the **constraint word** first: lowest latency, sporadic traffic, large payloads, least operational overhead, lowest cost. Those words decide the inference option and the customisation method.
- Traps: serverless inference for large models or GPUs (check what is supported); asynchronous inference compared with batch transform (async handles queued requests with large payloads, batch handles whole datasets offline); fine-tuning to add fresh facts, when RAG is the right answer for knowledge that changes; using accuracy on imbalanced classes instead of F1, precision or recall; forgetting to refresh the Knowledge Base when the source documents change; giving agents broad IAM permissions instead of scoped tool permissions.
- Flag long scenario questions and come back to them. Never leave a question blank, because there is no penalty for guessing.
