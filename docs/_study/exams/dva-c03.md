---
code: DVA-C03
title: "AWS Certified Developer – Associate"
credential: "AWS Certified Developer – Associate"
provider: aws
tracks: [cloud]
clouds: [aws]
level: associate
tier: elective
stage: "2"
progress: planned
official_url: https://aws.amazon.com/certification/certified-developer-associate/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html
outline_version: "DVA-C02 guide 2.1 (2024-12-12)"
last_verified: 2026-10-24
retires_on:
provisional: true
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends 1 or more years of hands-on experience developing and maintaining applications on AWS, proficiency in at least one high-level programming language and, for DVA-C03, experience with AI-assisted development tools."
replaces: "dva-c02"
replaced_by: ""
counterparts: [ai-200]
objectives:
  - { id: "1", title: "Development with AWS Services", weight: "32%" }
  - { id: "1.1", title: "Develop code for applications hosted on AWS" }
  - { id: "1.1.1", title: "Skill: Describe architectural patterns (for example, event-driven, microservices, monolithic, choreography, orchestration, fanout)" }
  - { id: "1.1.2", title: "Skill: Describe differences between stateful and stateless concepts" }
  - { id: "1.1.3", title: "Skill: Describe differences between tightly coupled and loosely coupled components" }
  - { id: "1.1.4", title: "Skill: Describe differences between synchronous and asynchronous patterns" }
  - { id: "1.1.5", title: "Skill: Create fault-tolerant and resilient applications in a programming language (for example, Java, C#, Python, JavaScript, TypeScript, Go)" }
  - { id: "1.1.6", title: "Skill: Create, extend, and maintain APIs (for example, response/request transformations, enforcing validation rules, overriding status codes)" }
  - { id: "1.1.7", title: "Skill: Write and run unit tests in development environments (for example, using AWS SAM)" }
  - { id: "1.1.8", title: "Skill: Write code to use messaging services" }
  - { id: "1.1.9", title: "Skill: Write code that interacts with AWS services by using APIs and AWS SDKs" }
  - { id: "1.1.10", title: "Skill: Handle streaming data using AWS services" }
  - { id: "1.1.11", title: "Skill: Use Amazon Q Developer to assist with development" }
  - { id: "1.1.12", title: "Skill: Use Amazon EventBridge to implement event-driven patterns" }
  - { id: "1.1.13", title: "Skill: Implement resilient application code for third-party service integrations (for example, retry logic, circuit breakers, error handling patterns)" }
  - { id: "1.2", title: "Develop code for AWS Lambda" }
  - { id: "1.2.1", title: "Skill: Describe the access of private resources in VPCs from Lambda code" }
  - { id: "1.2.2", title: "Skill: Configure Lambda functions by defining environment variables and parameters (for example, memory, concurrency, timeout, runtime, handler, layers, extensions, triggers, destinations)" }
  - { id: "1.2.3", title: "Skill: Handle the event lifecycle and errors by using code (for example, Lambda Destinations, dead-letter queues)" }
  - { id: "1.2.4", title: "Skill: Write and run test code by using AWS services and tools" }
  - { id: "1.2.5", title: "Skill: Integrate Lambda functions with AWS services" }
  - { id: "1.2.6", title: "Skill: Tune Lambda functions for optimal performance" }
  - { id: "1.2.7", title: "Skill: Use Lambda functions to process and transform data in near real time" }
  - { id: "1.3", title: "Use data stores in application development" }
  - { id: "1.3.1", title: "Skill: Describe high-cardinality partition keys for balanced partition access" }
  - { id: "1.3.2", title: "Skill: Describe database consistency models (for example, strongly consistent, eventually consistent)" }
  - { id: "1.3.3", title: "Skill: Describe differences between query and scan operations" }
  - { id: "1.3.4", title: "Skill: Define Amazon DynamoDB keys and indexing" }
  - { id: "1.3.5", title: "Skill: Serialize and deserialize data to provide persistence to a data store" }
  - { id: "1.3.6", title: "Skill: Use, manage, and maintain data stores" }
  - { id: "1.3.7", title: "Skill: Manage data lifecycles" }
  - { id: "1.3.8", title: "Skill: Use data caching services" }
  - { id: "1.3.9", title: "Skill: Use specialized data stores based on access patterns (for example, Amazon OpenSearch Service)" }
  - { id: "2", title: "Security", weight: "26%" }
  - { id: "2.1", title: "Implement authentication and/or authorization for applications and AWS services" }
  - { id: "2.1.1", title: "Skill: Use an identity provider to implement federated access (for example, Amazon Cognito, IAM)" }
  - { id: "2.1.2", title: "Skill: Secure applications by using bearer tokens" }
  - { id: "2.1.3", title: "Skill: Configure programmatic access to AWS" }
  - { id: "2.1.4", title: "Skill: Make authenticated calls to AWS services" }
  - { id: "2.1.5", title: "Skill: Assume an IAM role" }
  - { id: "2.1.6", title: "Skill: Define permissions for IAM principals" }
  - { id: "2.1.7", title: "Skill: Implement application-level authorization for fine-grained access control" }
  - { id: "2.1.8", title: "Skill: Handle cross-service authentication in microservice architectures" }
  - { id: "2.2", title: "Implement encryption by using AWS services" }
  - { id: "2.2.1", title: "Skill: Define encryption at rest and in transit" }
  - { id: "2.2.2", title: "Skill: Describe certificate management (for example, AWS Private CA)" }
  - { id: "2.2.3", title: "Skill: Describe differences between client-side encryption and server-side encryption" }
  - { id: "2.2.4", title: "Skill: Use encryption keys to encrypt or decrypt data" }
  - { id: "2.2.5", title: "Skill: Generate certificates and SSH keys for development purposes" }
  - { id: "2.2.6", title: "Skill: Use encryption across account boundaries" }
  - { id: "2.2.7", title: "Skill: Enable and disable key rotation" }
  - { id: "2.3", title: "Manage sensitive data in application code" }
  - { id: "2.3.1", title: "Skill: Describe data classification (for example, personally identifiable information [PII], protected health information [PHI])" }
  - { id: "2.3.2", title: "Skill: Encrypt environment variables that contain sensitive data" }
  - { id: "2.3.3", title: "Skill: Use secret management services to secure sensitive data" }
  - { id: "2.3.4", title: "Skill: Sanitize sensitive data" }
  - { id: "2.3.5", title: "Skill: Implement application-level data masking and sanitization" }
  - { id: "2.3.6", title: "Skill: Implement data access patterns for multi-tenant applications" }
  - { id: "3", title: "Deployment", weight: "24%" }
  - { id: "3.1", title: "Prepare application artifacts to be deployed to AWS" }
  - { id: "3.1.1", title: "Skill: Manage the dependencies of the code module (for example, environment variables, configuration files, container images) within the package" }
  - { id: "3.1.2", title: "Skill: Organize files and a directory structure for application deployment" }
  - { id: "3.1.3", title: "Skill: Use code repositories in deployment environments" }
  - { id: "3.1.4", title: "Skill: Apply application requirements for resources (for example, memory, cores)" }
  - { id: "3.1.5", title: "Skill: Prepare application configurations for specific environments (for example, by using AWS AppConfig)" }
  - { id: "3.2", title: "Test applications in development environments" }
  - { id: "3.2.1", title: "Skill: Test deployed code by using AWS services and tools" }
  - { id: "3.2.2", title: "Skill: Write integration tests and mock APIs for external dependencies" }
  - { id: "3.2.3", title: "Skill: Test applications by using development endpoints (for example, configuring stages in Amazon API Gateway)" }
  - { id: "3.2.4", title: "Skill: Deploy application stack updates to existing environments (for example, deploying an AWS SAM template to a different staging environment)" }
  - { id: "3.2.5", title: "Skill: Test event-driven applications" }
  - { id: "3.3", title: "Automate deployment testing" }
  - { id: "3.3.1", title: "Skill: Create application test events (for example, JSON payloads for testing AWS Lambda, API Gateway, AWS SAM resources)" }
  - { id: "3.3.2", title: "Skill: Deploy API resources to various environments" }
  - { id: "3.3.3", title: "Skill: Create application environments that use approved versions for integration testing (for example, Lambda aliases, container image tags, AWS Amplify branches, AWS Copilot environments)" }
  - { id: "3.3.4", title: "Skill: Implement and deploy infrastructure as code (IaC) templates (for example, AWS SAM templates, AWS CloudFormation templates)" }
  - { id: "3.3.5", title: "Skill: Manage environments in individual AWS services (for example, differentiating between development, test, and production in API Gateway)" }
  - { id: "3.3.6", title: "Skill: Use Amazon Q Developer to generate automated tests" }
  - { id: "3.4", title: "Deploy code by using AWS Continuous Integration and Continuous Delivery (CI/CD) services" }
  - { id: "3.4.1", title: "Skill: Describe Lambda deployment packaging options" }
  - { id: "3.4.2", title: "Skill: Describe API Gateway stages and custom domains" }
  - { id: "3.4.3", title: "Skill: Update existing IaC templates (for example, AWS SAM templates, CloudFormation templates)" }
  - { id: "3.4.4", title: "Skill: Manage application environments by using AWS services" }
  - { id: "3.4.5", title: "Skill: Deploy an application version by using deployment strategies" }
  - { id: "3.4.6", title: "Skill: Commit code to a repository to invoke build, test, and deployment actions" }
  - { id: "3.4.7", title: "Skill: Use orchestrated workflows to deploy code to different environments" }
  - { id: "3.4.8", title: "Skill: Perform application rollbacks by using existing deployment strategies" }
  - { id: "3.4.9", title: "Skill: Use labels and branches for version and release management" }
  - { id: "3.4.10", title: "Skill: Use existing runtime configurations to create dynamic deployments (for example, using staging variables from API Gateway in Lambda functions)" }
  - { id: "3.4.11", title: "Skill: Configure deployment strategies (for example, blue/green, canary, rolling) for application releases" }
  - { id: "4", title: "Troubleshooting and Optimization", weight: "18%" }
  - { id: "4.1", title: "Assist in a root cause analysis" }
  - { id: "4.1.1", title: "Skill: Debug code to identify defects" }
  - { id: "4.1.2", title: "Skill: Interpret application metrics, logs, and traces" }
  - { id: "4.1.3", title: "Skill: Query logs to find relevant data" }
  - { id: "4.1.4", title: "Skill: Implement custom metrics (for example, Amazon CloudWatch embedded metric format [EMF])" }
  - { id: "4.1.5", title: "Skill: Review application health by using dashboards and insights" }
  - { id: "4.1.6", title: "Skill: Troubleshoot deployment failures by using service output logs" }
  - { id: "4.1.7", title: "Skill: Debug service integration issues in applications" }
  - { id: "4.2", title: "Instrument code for observability" }
  - { id: "4.2.1", title: "Skill: Describe differences between logging, monitoring, and observability" }
  - { id: "4.2.2", title: "Skill: Implement an effective logging strategy to record application behavior and state" }
  - { id: "4.2.3", title: "Skill: Implement code that emits custom metrics" }
  - { id: "4.2.4", title: "Skill: Add annotations for tracing services" }
  - { id: "4.2.5", title: "Skill: Implement notification alerts for specific actions (for example, notifications about quota limits or deployment completions)" }
  - { id: "4.2.6", title: "Skill: Implement tracing by using AWS services and tools" }
  - { id: "4.2.7", title: "Skill: Implement structured logging for application events and user actions" }
  - { id: "4.2.8", title: "Skill: Configure application health checks and readiness probes" }
  - { id: "4.3", title: "Optimize applications by using AWS services and features" }
  - { id: "4.3.1", title: "Skill: Define concurrency" }
  - { id: "4.3.2", title: "Skill: Profile application performance" }
  - { id: "4.3.3", title: "Skill: Determine minimum memory and compute power for an application" }
  - { id: "4.3.4", title: "Skill: Use subscription filter policies to optimize messaging" }
  - { id: "4.3.5", title: "Skill: Cache content based on request headers" }
  - { id: "4.3.6", title: "Skill: Implement application-level caching to improve performance" }
  - { id: "4.3.7", title: "Skill: Optimize application resource usage" }
  - { id: "4.3.8", title: "Skill: Analyze application performance issues" }
  - { id: "4.3.9", title: "Skill: Use application logs to identify performance bottlenecks" }
---
## Exam format

**About this outline.** As of 2026-10-24, AWS has **not yet published the DVA-C03 exam guide**. AWS says the full guide will be available when registration opens on **October 27, 2026**. DVA-C03 delivery starts on **December 1, 2026**, and the last day to sit DVA-C02 is **November 30, 2026** ([certification page](https://aws.amazon.com/certification/certified-developer-associate/); [AWS blog, September 2026](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/)). The objectives on this page are therefore the **DVA-C02 guide, version 2.1 (December 12, 2024)**, transcribed in full, with DVA-C02's domain weights. Re-transcribe this page from the DVA-C03 guide once it is published.

Every fact below is as of 2026-10-24. DVA-C03 facts come from the [AWS blog announcement](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/). Current-exam facts come from the [certification page](https://aws.amazon.com/certification/certified-developer-associate/) and the [DVA-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html). Confirm everything on those pages before you book, especially after October 27, 2026.

| Item | DVA-C03 (from December 1, 2026) | DVA-C02 (until November 30, 2026) |
| --- | --- | --- |
| Category | Associate | Associate |
| Question types | Not yet published (the C03 guide is due October 27, 2026) | Multiple choice and multiple response |
| Number of questions | 65 (50 scored, 15 unscored) | 65 (50 scored, 15 unscored) |
| Duration | 130 minutes | 130 minutes |
| Passing score | 720 out of 1,000 | 720 out of 1,000 (scaled, compensatory) |
| Price | 150 USD | 150 USD (see [exam pricing](https://aws.amazon.com/certification/policies/before-testing/)) |
| Languages | "All languages currently supported" at launch | English, Japanese, Korean, Portuguese (Brazil), Simplified Chinese, Spanish (Latin America) |
| Delivery | Pearson VUE test centre or online proctored | Same |
| Registration | Opens October 27, 2026 | Open until the last sitting on November 30, 2026 |
| Validity and renewal | 3 years. You can recertify by passing the latest version, or automatically by earning DevOps Engineer – Professional (see [recertification](https://aws.amazon.com/certification/recertification/)) | Same |

DVA-C03 domains and weights, as announced: **Development with AWS Services 30%, Security 26%, Testing and Deployment 22%, Troubleshooting and Optimization 22%.** Compared with the DVA-C02 weights transcribed below (32 / 26 / 24 / 18), troubleshooting gains weight, and the blog names Domain 3 "Testing and Deployment" where the DVA-C02 guide says "Deployment". A credential earned on DVA-C02 stays active for its full three years.

## What the exam really tests

The Developer – Associate exam tests whether you can **write, secure, ship and debug application code that calls AWS services**. The guide puts designing architectures, designing CI/CD pipelines, administering IAM users and groups, administering servers and designing networks out of scope. The DVA-C02 outline transcribed here covers:

- **Development with AWS Services**: architectural patterns (event-driven, microservices, fan-out, choreography compared with orchestration), idempotency, retries with exponential backoff and jitter, circuit breakers, SDK and API usage, Amazon Q Developer, EventBridge patterns; Lambda in depth (configuration, event source mappings, concurrency, destinations, layers, VPC access, error handling, real-time stream processing); data stores in depth, especially DynamoDB (partition keys, query compared with scan, consistency models, indexes, TTL, Streams, DAX), plus S3 and caching.
- **Security**: Amazon Cognito user pools compared with identity pools, bearer tokens, IAM roles and STS from code, resource policies, KMS encryption (envelope encryption, client-side compared with server-side), and secrets in Secrets Manager compared with Systems Manager Parameter Store.
- **Deployment**: packaging artifacts (Lambda zips and images, container images in ECR), AWS SAM and CloudFormation templates, environment-specific configuration (Lambda aliases, API Gateway stages), testing with mocks and integration tests, and CodeBuild, CodeDeploy and CodePipeline (CodeArtifact for packages) with blue/green, canary and rolling deployments.
- **Troubleshooting and Optimization**: root-cause analysis from CloudWatch Logs, Logs Insights and X-Ray traces; structured logging, custom metrics and the Embedded Metric Format; optimisation through caching, concurrency tuning, Lambda memory and SQS batching.

The current DVA-C02 guide also lists **"emerging topics"** that may appear as unscored pretest items: AI-assisted code generation and review, security risks of integrating AI services, AI-generated tests, AI support for CI/CD, AI-assisted error analysis, and AI-assisted optimisation. According to the blog, DVA-C03 makes these **scored**. It adds a new **Task 2.3 on AI security** (access management for AI services; data-privacy controls such as VPC endpoints and making sure inputs and outputs are not used for training; content filtering and protection against prompt injection; agent tool-use authorisation, session isolation and human-in-the-loop approval; keeping sensitive content out of logs). It also adds container image building with ECR and deployment to ECS, EKS and Fargate, and brings Amazon Bedrock, Amazon Bedrock AgentCore, Amazon Q, Kiro, Amazon Data Firehose and AWS PrivateLink into scope. Prompt engineering, RAG design, AI model selection, Amazon SageMaker AI and AI governance framework design are announced as **out of scope**. DynamoDB, security, testing, observability and optimisation skills are consolidated into fewer, broader items.

Candidates lose points on the **numbers and the exact behaviour**: DynamoDB capacity-unit arithmetic and when to choose strongly consistent reads; Lambda timeout compared with visibility timeout; which Lambda invocation types retry and where failures go (DLQ compared with destinations); `sam deploy` compared with `cloudformation package`; CodeDeploy lifecycle hooks; and which Cognito pool returns AWS credentials.

## Study strategy

1. **Foundations first.** IAM roles and policies from a developer's point of view (execution roles, STS AssumeRole, resource policies), then the Lambda execution model, then DynamoDB data modelling. Those three areas drive most of the exam.
2. **Build one serverless application end to end in C#.** Use API Gateway, Lambda (.NET), DynamoDB, SQS or EventBridge, Cognito authentication, Secrets Manager, and X-Ray tracing. Deploy it with AWS SAM, then wire it to CodePipeline with a CodeDeploy canary deployment for Lambda. After that, put a small Angular front end on S3 and CloudFront, or on Amplify Hosting. This one project covers most of the outline.
3. **For DVA-C03, also practise:** building a container image, pushing it to ECR and running it on ECS with Fargate; calling Amazon Bedrock from the SDK with a Guardrail applied; looking at how an AgentCore agent authorises tool calls; and using Amazon Q Developer or Kiro for code generation and tests.
4. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (the Official Practice Question Set, the exam-prep course, AWS Builder Labs, AWS Cloud Quest, AWS Jam, AWS SimuLearn and the Official Practice Exam). Watch for refreshed DVA-C03 prep material, which AWS says will appear when registration opens on October 27, 2026. Also use the [DVA-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html) and its in-scope service list until the C03 guide replaces it.
5. **How your background helps or misleads.** Your **AZ-204 preparation** is the single biggest asset. It is the same role on the other cloud. The mappings are Azure Functions to Lambda (triggers and bindings become event sources plus SDK calls, because Lambda has no declarative output bindings), Cosmos DB to DynamoDB (single-table design, no SQL query surface), Service Bus to SQS and SNS, Event Grid to EventBridge, Key Vault to Secrets Manager and KMS, Application Insights to X-Ray and CloudWatch, and Entra ID app registrations to Cognito. The usual mistake is assuming Cosmos DB's tunable consistency levels or Functions' Durable orchestration patterns map one to one. Instead, learn DynamoDB's read consistency options and Step Functions. **CKAD** helps with the new container items. **.NET** helps directly, because the AWS SDK for .NET and Lambda .NET runtimes are first-class, but the exam is language-neutral and shows snippets in pseudo-code or JSON.

Decide by date. If you are ready before November 30, 2026, DVA-C02 is still an option. Otherwise prepare for DVA-C03, which better matches your agentic AI track.

## Differences from related exams

- **DVA-C03 compared with AI-200 (Azure AI Cloud Developer Associate, its counterpart).** Both are associate exams for back-end developers that were rebuilt in 2026 around AI workloads. AI-200 puts AI at the centre: about a third of it is building AI solutions on Azure data services (vector search, RAG on Cosmos DB and PostgreSQL), plus containers on AKS and Container Apps. DVA-C03 keeps the general developer role and adds AI-assisted development and **securing** AI and agent calls, while explicitly leaving RAG design and model selection out. So AI-200 tests more of "build the AI feature" and DVA-C03 tests more of "build the application safely and use AI tools to help".
- **DVA-C03 compared with DVA-C02 (its predecessor).** The four domains are the same, with new weights (30 / 26 / 22 / 22 against 32 / 26 / 24 / 18). DVA-C03 adds Task 2.3 on AI security, AI-assisted development skills across every domain, containers on ECS, EKS and Fargate, and Bedrock, AgentCore, Q, Kiro, Firehose and PrivateLink. Several skill groups are consolidated.
- **DVA-C03 compared with AZ-204 (retired July 31, 2026).** This is the same role and level. AZ-204 gave more weight to API Management, Blob Storage operations and the Microsoft identity platform. DVA gives more weight to CI/CD deployment strategies and DynamoDB.
- **DVA-C03 compared with SAA-C03.** SAA asks which design to choose. DVA asks how to code and deploy a design that someone else chose. DVA goes deeper on Lambda, DynamoDB, Cognito and the Code* tools, and SAA covers networking and DR far more.
- **DVA-C03 compared with SOA-C03.** SOA operates infrastructure (CloudWatch agent, Systems Manager, VPC troubleshooting). DVA instruments and fixes application code.
- **DVA-C03 compared with DOP-C02 (DevOps Engineer – Professional).** DOP designs the pipelines and governance that DVA only uses. Passing DOP recertifies DVA.

## Exam-day notes

- You have 65 questions in 130 minutes, so time is rarely the problem. Precision is. Read code-like details carefully: API names (`PutItem` compared with `UpdateItem`, `Query` compared with `Scan`), header names and IAM actions.
- Do capacity calculations on the whiteboard or scratch sheet. 1 RCU gives one strongly consistent read per second of up to 4 KB, or two eventually consistent reads; 1 WCU gives one write per second of up to 1 KB. Round the item size up before you divide.
- Traps: environment variables are not a secret store; storing credentials in code is never right, so use roles; Lambda in a VPC needs a NAT gateway or a VPC endpoint to reach AWS services; SQS visibility timeout should be longer than the function timeout; API Gateway caching is set per stage; X-Ray needs both the SDK or instrumentation and permissions for the daemon or agent.
- On DVA-C03, expect AI-security scenarios that ask for the most secure option: least-privilege access to Bedrock, PrivateLink endpoints, Guardrails against prompt injection, and human approval before an agent takes a sensitive action.
