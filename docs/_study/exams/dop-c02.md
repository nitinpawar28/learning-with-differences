---
code: DOP-C02
title: "AWS Certified DevOps Engineer – Professional"
credential: "AWS Certified DevOps Engineer – Professional"
provider: aws
tracks: [cloud, architect]
clouds: [aws]
level: professional
tier: elective
stage: "6"
progress: planned
official_url: https://aws.amazon.com/certification/certified-devops-engineer-professional/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html
outline_version: "DOP-C02 guide (no version printed), retrieved 2026-10-24"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends 2 or more years of experience provisioning, operating and managing AWS environments, plus SDLC and programming or scripting experience."
replaces: ""
replaced_by: ""
counterparts: [az-400]
objectives:
  - { id: "1", title: "SDLC Automation", weight: "22%" }
  - { id: "1.1", title: "Implement CI/CD pipelines" }
  - { id: "1.1.1", title: "Knowledge: Software development lifecycle (SDLC) concepts, phases, and models" }
  - { id: "1.1.2", title: "Knowledge: Pipeline deployment patterns for single- and multi-account environments" }
  - { id: "1.1.3", title: "Skill: Configuring code, image, and artifact repositories" }
  - { id: "1.1.4", title: "Skill: Using version control to integrate pipelines with application environments" }
  - { id: "1.1.5", title: "Skill: Setting up build processes (e.g. AWS CodeBuild)" }
  - { id: "1.1.6", title: "Skill: Managing build and deployment secrets (e.g. AWS Secrets Manager, AWS Systems Manager Parameter Store)" }
  - { id: "1.1.7", title: "Skill: Determining appropriate deployment strategies (e.g. AWS CodeDeploy)" }
  - { id: "1.2", title: "Integrate automated testing into CI/CD pipelines" }
  - { id: "1.2.1", title: "Knowledge: Different types of tests (e.g. unit tests, integration tests, acceptance tests, user interface tests, security scans)" }
  - { id: "1.2.2", title: "Knowledge: Reasonable use of different types of tests at different stages of the CI/CD pipeline" }
  - { id: "1.2.3", title: "Skill: Running builds or tests when generating pull requests or code merges (e.g. CodeBuild)" }
  - { id: "1.2.4", title: "Skill: Running load/stress tests, performance benchmarking, and application testing at scale" }
  - { id: "1.2.5", title: "Skill: Measuring application health based on application exit codes" }
  - { id: "1.2.6", title: "Skill: Automating unit tests and code coverage" }
  - { id: "1.2.7", title: "Skill: Invoking AWS services in a pipeline for testing" }
  - { id: "1.3", title: "Build and manage artifacts" }
  - { id: "1.3.1", title: "Knowledge: Artifact use cases and secure management" }
  - { id: "1.3.2", title: "Knowledge: Methods to create and generate artifacts" }
  - { id: "1.3.3", title: "Knowledge: Artifact lifecycle considerations" }
  - { id: "1.3.4", title: "Skill: Creating and configuring artifact repositories (e.g. AWS CodeArtifact, Amazon S3, Amazon ECR)" }
  - { id: "1.3.5", title: "Skill: Configuring build tools for generating artifacts (e.g. CodeBuild, AWS Lambda)" }
  - { id: "1.3.6", title: "Skill: Automating Amazon EC2 instance and container image build processes (e.g. EC2 Image Builder)" }
  - { id: "1.4", title: "Implement deployment strategies for instance, container, and serverless environments" }
  - { id: "1.4.1", title: "Knowledge: Deployment methodologies for various platforms (e.g. Amazon EC2, Amazon ECS, Amazon EKS, Lambda)" }
  - { id: "1.4.2", title: "Knowledge: Application storage patterns (e.g. Amazon EFS, Amazon S3, Amazon EBS)" }
  - { id: "1.4.3", title: "Knowledge: Mutable deployment patterns in contrast to immutable deployment patterns" }
  - { id: "1.4.4", title: "Knowledge: Tools and services available for distributing code (e.g. CodeDeploy, Image Builder)" }
  - { id: "1.4.5", title: "Skill: Configuring security permissions to allow access to artifact repositories (e.g. IAM, CodeArtifact)" }
  - { id: "1.4.6", title: "Skill: Configuring deployment agents (e.g. CodeDeploy agent)" }
  - { id: "1.4.7", title: "Skill: Troubleshooting deployment issues" }
  - { id: "1.4.8", title: "Skill: Using different deployment methods (e.g. blue/green, canary)" }
  - { id: "2", title: "Configuration Management and IaC", weight: "17%" }
  - { id: "2.1", title: "Define cloud infrastructure and reusable components to provision and manage systems throughout their lifecycle" }
  - { id: "2.1.1", title: "Knowledge: Infrastructure as code (IaC) options and tools for AWS" }
  - { id: "2.1.2", title: "Knowledge: Change management processes for IaC-based platforms" }
  - { id: "2.1.3", title: "Knowledge: Configuration management services and strategies" }
  - { id: "2.1.4", title: "Skill: Composing and deploying IaC templates (e.g. AWS SAM, AWS CloudFormation, AWS CDK)" }
  - { id: "2.1.5", title: "Skill: Applying CloudFormation stack sets across multiple accounts and AWS Regions" }
  - { id: "2.1.6", title: "Skill: Determining optimal configuration management services (e.g. AWS OpsWorks, AWS Systems Manager, AWS Config, AWS AppConfig)" }
  - { id: "2.1.7", title: "Skill: Implementing infrastructure patterns, governance controls, and security standards into reusable IaC templates (e.g. AWS Service Catalog, CloudFormation modules, AWS CDK)" }
  - { id: "2.2", title: "Deploy automation to create, onboard, and secure AWS accounts in a multi-account or multi-Region environment" }
  - { id: "2.2.1", title: "Knowledge: AWS account structures, best practices, and related AWS services" }
  - { id: "2.2.2", title: "Skill: Standardizing and automating account provisioning and configuration" }
  - { id: "2.2.3", title: "Skill: Creating, consolidating, and centrally managing accounts (e.g. AWS Organizations, AWS Control Tower)" }
  - { id: "2.2.4", title: "Skill: Applying IAM solutions for multi-account and complex organization structures (e.g. SCPs, assuming roles)" }
  - { id: "2.2.5", title: "Skill: Implementing and developing governance and security controls at scale (AWS Config, AWS Control Tower, AWS Security Hub, Amazon Detective, Amazon GuardDuty, Service Catalog, SCPs)" }
  - { id: "2.3", title: "Design and build automated solutions for complex tasks and large-scale environments" }
  - { id: "2.3.1", title: "Knowledge: AWS services and solutions to automate tasks and processes" }
  - { id: "2.3.2", title: "Knowledge: Methods and strategies to interact with the AWS software-defined infrastructure" }
  - { id: "2.3.3", title: "Skill: Automating system inventory, configuration, and patch management (e.g. Systems Manager, AWS Config)" }
  - { id: "2.3.4", title: "Skill: Developing AWS Lambda function automations for complex scenarios (e.g. AWS SDKs, Lambda, AWS Step Functions)" }
  - { id: "2.3.5", title: "Skill: Automating the configuration of software applications to the desired state (e.g. OpsWorks, Systems Manager State Manager)" }
  - { id: "2.3.6", title: "Skill: Maintaining software compliance (e.g. Systems Manager)" }
  - { id: "3", title: "Resilient Cloud Solutions", weight: "15%" }
  - { id: "3.1", title: "Implement highly available solutions to meet resilience and business requirements" }
  - { id: "3.1.1", title: "Knowledge: Multi-AZ and multi-Region deployments (e.g. compute layer, data layer)" }
  - { id: "3.1.2", title: "Knowledge: SLAs" }
  - { id: "3.1.3", title: "Knowledge: Replication and failover methods for stateful services" }
  - { id: "3.1.4", title: "Knowledge: Techniques to achieve high availability (e.g. Multi-AZ, multi-Region)" }
  - { id: "3.1.5", title: "Skill: Translating business requirements into technical resiliency needs" }
  - { id: "3.1.6", title: "Skill: Identifying and remediating single points of failure in existing workloads" }
  - { id: "3.1.7", title: "Skill: Enabling cross-Region solutions where available (e.g. Amazon DynamoDB, Amazon RDS, Amazon Route 53, Amazon S3, Amazon CloudFront)" }
  - { id: "3.1.8", title: "Skill: Configuring load balancing to support cross-AZ services" }
  - { id: "3.1.9", title: "Skill: Configuring applications and related services to support multiple Availability Zones and AWS Regions while minimizing downtime" }
  - { id: "3.2", title: "Implement solutions that are scalable to meet business requirements" }
  - { id: "3.2.1", title: "Knowledge: Appropriate metrics for scaling services" }
  - { id: "3.2.2", title: "Knowledge: Loosely coupled and distributed architectures" }
  - { id: "3.2.3", title: "Knowledge: Serverless architectures" }
  - { id: "3.2.4", title: "Knowledge: Container platforms" }
  - { id: "3.2.5", title: "Skill: Identifying and remediating scaling issues" }
  - { id: "3.2.6", title: "Skill: Identifying and implementing appropriate auto scaling, load balancing, and caching solutions" }
  - { id: "3.2.7", title: "Skill: Deploying container-based applications (e.g. Amazon ECS, Amazon EKS)" }
  - { id: "3.2.8", title: "Skill: Deploying workloads in multiple Regions for global scalability" }
  - { id: "3.2.9", title: "Skill: Configuring serverless applications (e.g. Amazon API Gateway, AWS Lambda, AWS Fargate)" }
  - { id: "3.3", title: "Implement automated recovery processes to meet RTO and RPO requirements" }
  - { id: "3.3.1", title: "Knowledge: Disaster recovery concepts (e.g. RTO, RPO)" }
  - { id: "3.3.2", title: "Knowledge: AWS Backup and recovery strategies (e.g. pilot light, warm standby)" }
  - { id: "3.3.3", title: "Knowledge: Recovery procedures" }
  - { id: "3.3.4", title: "Skill: Testing failover of Multi-AZ and multi-Region workloads (e.g. Amazon RDS, Amazon Aurora, Route 53, CloudFront)" }
  - { id: "3.3.5", title: "Skill: Identifying and implementing appropriate cross-Region AWS Backup and recovery strategies (e.g. AWS Backup, Amazon S3, AWS Systems Manager)" }
  - { id: "3.3.6", title: "Skill: Configuring a load balancer to recover from backend failure" }
  - { id: "4", title: "Monitoring and Logging", weight: "15%" }
  - { id: "4.1", title: "Configure the collection, aggregation, and storage of logs and metrics" }
  - { id: "4.1.1", title: "Knowledge: How to monitor applications and infrastructure" }
  - { id: "4.1.2", title: "Knowledge: Amazon CloudWatch metrics (e.g. namespaces, metrics, dimensions, and resolution)" }
  - { id: "4.1.3", title: "Knowledge: Real-time log ingestion" }
  - { id: "4.1.4", title: "Knowledge: Encryption options for at-rest and in-transit logs and metrics (e.g. client-side and server-side, AWS KMS)" }
  - { id: "4.1.5", title: "Knowledge: Security configurations (e.g. IAM roles and permissions to allow for log collection)" }
  - { id: "4.1.6", title: "Skill: Securely storing and managing logs" }
  - { id: "4.1.7", title: "Skill: Creating CloudWatch metrics from log events by using metric filters" }
  - { id: "4.1.8", title: "Skill: Creating CloudWatch metric streams (e.g. Amazon S3 or Amazon Kinesis Data Firehose options)" }
  - { id: "4.1.9", title: "Skill: Collecting custom metrics (e.g. using the CloudWatch agent)" }
  - { id: "4.1.10", title: "Skill: Managing log storage lifecycles (e.g. Amazon S3 lifecycles, CloudWatch log group retention)" }
  - { id: "4.1.11", title: "Skill: Processing log data by using CloudWatch log subscriptions (e.g. Amazon Kinesis, AWS Lambda, Amazon OpenSearch Service)" }
  - { id: "4.1.12", title: "Skill: Searching log data by using filter and pattern syntax or Amazon CloudWatch Logs Insights" }
  - { id: "4.1.13", title: "Skill: Configuring encryption of log data (e.g. AWS KMS)" }
  - { id: "4.2", title: "Audit, monitor, and analyze logs and metrics to detect issues" }
  - { id: "4.2.1", title: "Knowledge: Anomaly detection alarms (e.g. CloudWatch anomaly detection)" }
  - { id: "4.2.2", title: "Knowledge: Common CloudWatch metrics and logs (e.g. CPU utilization with Amazon EC2, queue length with Amazon RDS, 5xx errors with an Application Load Balancer (ALB))" }
  - { id: "4.2.3", title: "Knowledge: Amazon Inspector and common assessment templates" }
  - { id: "4.2.4", title: "Knowledge: AWS Config rules" }
  - { id: "4.2.5", title: "Knowledge: AWS CloudTrail log events" }
  - { id: "4.2.6", title: "Skill: Building CloudWatch dashboards and Amazon Quick Sight visualizations" }
  - { id: "4.2.7", title: "Skill: Associating CloudWatch alarms with CloudWatch metrics (standard and custom)" }
  - { id: "4.2.8", title: "Skill: Configuring AWS X-Ray for different services (e.g. containers, Amazon API Gateway, Lambda)" }
  - { id: "4.2.9", title: "Skill: Analyzing real-time log streams (e.g. using Amazon Kinesis Data Streams)" }
  - { id: "4.2.10", title: "Skill: Analyzing logs with AWS services (e.g. Amazon Athena, CloudWatch Logs Insights)" }
  - { id: "4.3", title: "Automate monitoring and event management of complex environments" }
  - { id: "4.3.1", title: "Knowledge: Event-driven, asynchronous design patterns (e.g. S3 Event Notifications or Amazon EventBridge events to Amazon SNS or Lambda)" }
  - { id: "4.3.2", title: "Knowledge: Capabilities of auto scaling for a variety of AWS services (e.g. EC2 Auto Scaling groups, RDS storage auto scaling, Amazon DynamoDB, Amazon ECS capacity provider, Amazon EKS autoscalers)" }
  - { id: "4.3.3", title: "Knowledge: Alert notification and action capabilities (e.g. CloudWatch alarms to Amazon SNS, Lambda, EC2 automatic recovery)" }
  - { id: "4.3.4", title: "Knowledge: Health check capabilities in AWS services (e.g. ALB target groups, Amazon Route 53)" }
  - { id: "4.3.5", title: "Skill: Configuring solutions for auto scaling (e.g. DynamoDB, EC2 Auto Scaling groups, RDS storage auto scaling, ECS capacity provider)" }
  - { id: "4.3.6", title: "Skill: Creating CloudWatch custom metrics and metric filters, alarms, and notifications (e.g. Amazon SNS, Lambda)" }
  - { id: "4.3.7", title: "Skill: Configuring S3 events to process log files (e.g. by using Lambda) and deliver log files to another destination (e.g. OpenSearch Service, CloudWatch Logs)" }
  - { id: "4.3.8", title: "Skill: Configuring EventBridge to send notifications based on a particular event pattern" }
  - { id: "4.3.9", title: "Skill: Installing and configuring agents on EC2 instances (e.g. AWS Systems Manager Agent (SSM Agent), CloudWatch agent)" }
  - { id: "4.3.10", title: "Skill: Configuring AWS Config rules to remediate issues" }
  - { id: "4.3.11", title: "Skill: Configuring health checks (e.g. Route 53, ALB)" }
  - { id: "5", title: "Incident and Event Response", weight: "14%" }
  - { id: "5.1", title: "Manage event sources to process, notify, and take action in response to events" }
  - { id: "5.1.1", title: "Knowledge: AWS services that generate, capture, and process events (e.g. AWS Health, Amazon EventBridge, AWS CloudTrail)" }
  - { id: "5.1.2", title: "Knowledge: Event-driven architectures (e.g. fan out, event streaming, queuing)" }
  - { id: "5.1.3", title: "Skill: Integrating AWS event sources (e.g. AWS Health, EventBridge, CloudTrail)" }
  - { id: "5.1.4", title: "Skill: Building event processing workflows (e.g. Amazon SQS, Amazon Kinesis, Amazon SNS, AWS Lambda, AWS Step Functions)" }
  - { id: "5.2", title: "Implement configuration changes in response to events" }
  - { id: "5.2.1", title: "Knowledge: Fleet management services (e.g. AWS Systems Manager, AWS Auto Scaling)" }
  - { id: "5.2.2", title: "Knowledge: Configuration management services (e.g. AWS Config)" }
  - { id: "5.2.3", title: "Skill: Applying configuration changes to systems" }
  - { id: "5.2.4", title: "Skill: Modifying infrastructure configurations in response to events" }
  - { id: "5.2.5", title: "Skill: Remediating a non-desired system state" }
  - { id: "5.3", title: "Troubleshoot system and application failures" }
  - { id: "5.3.1", title: "Knowledge: AWS metrics and logging services (e.g. Amazon CloudWatch, AWS X-Ray)" }
  - { id: "5.3.2", title: "Knowledge: AWS service health services (e.g. AWS Health, CloudWatch, Systems Manager OpsCenter)" }
  - { id: "5.3.3", title: "Knowledge: Root cause analysis" }
  - { id: "5.3.4", title: "Skill: Analyzing failed deployments (e.g. AWS CodePipeline, AWS CodeBuild, AWS CodeDeploy, AWS CloudFormation, CloudWatch synthetic monitoring)" }
  - { id: "5.3.5", title: "Skill: Analyzing incidents regarding failed processes (e.g. auto scaling, Amazon ECS, Amazon EKS)" }
  - { id: "6", title: "Security and Compliance", weight: "17%" }
  - { id: "6.1", title: "Implement techniques for identity and access management at scale" }
  - { id: "6.1.1", title: "Knowledge: Appropriate usage of different IAM entities for human and machine access (e.g. users, groups, roles, identity providers, identity-based policies, resource-based policies, session policies)" }
  - { id: "6.1.2", title: "Knowledge: Identity federation techniques (e.g. using IAM identity providers and AWS IAM Identity Center)" }
  - { id: "6.1.3", title: "Knowledge: Permission management delegation by using IAM permissions boundaries" }
  - { id: "6.1.4", title: "Knowledge: Organizational SCPs" }
  - { id: "6.1.5", title: "Skill: Designing policies to enforce least privilege access" }
  - { id: "6.1.6", title: "Skill: Implementing role-based and attribute-based access control patterns" }
  - { id: "6.1.7", title: "Skill: Automating credential rotation for machine identities (e.g. AWS Secrets Manager)" }
  - { id: "6.1.8", title: "Skill: Managing permissions to control access to human and machine identities (e.g. enabling multi-factor authentication (MFA), AWS STS, IAM profiles)" }
  - { id: "6.2", title: "Apply automation for security controls and data protection" }
  - { id: "6.2.1", title: "Knowledge: Network security components (e.g. security groups, network ACLs, routing, AWS Network Firewall, AWS WAF, AWS Shield)" }
  - { id: "6.2.2", title: "Knowledge: Certificates and public key infrastructure (PKI)" }
  - { id: "6.2.3", title: "Knowledge: Data management (e.g. data classification, encryption, key management, access controls)" }
  - { id: "6.2.4", title: "Skill: Automating the application of security controls in multi-account and multi-Region environments (e.g. AWS Security Hub, AWS Organizations, AWS Control Tower, AWS Systems Manager)" }
  - { id: "6.2.5", title: "Skill: Combining security controls to apply defense in depth (e.g. AWS Certificate Manager (ACM), AWS WAF, AWS Config, AWS Config rules, Security Hub, Amazon GuardDuty, security groups, network ACLs, Amazon Detective, Network Firewall)" }
  - { id: "6.2.6", title: "Skill: Automating the discovery of sensitive data at scale (e.g. Amazon Macie)" }
  - { id: "6.2.7", title: "Skill: Encrypting data in transit and data at rest (e.g. AWS KMS, AWS CloudHSM, ACM)" }
  - { id: "6.3", title: "Implement security monitoring and auditing solutions" }
  - { id: "6.3.1", title: "Knowledge: Security auditing services and features (e.g. AWS CloudTrail, AWS Config, VPC Flow Logs, AWS CloudFormation drift detection)" }
  - { id: "6.3.2", title: "Knowledge: AWS services for identifying security vulnerabilities and events (e.g. GuardDuty, Amazon Inspector, IAM Access Analyzer, AWS Config)" }
  - { id: "6.3.3", title: "Knowledge: Common cloud security threats (e.g. insecure web traffic, exposed AWS access keys, S3 buckets with public access enabled or encryption disabled)" }
  - { id: "6.3.4", title: "Skill: Implementing robust security auditing" }
  - { id: "6.3.5", title: "Skill: Configuring alerting based on unexpected or anomalous security events" }
  - { id: "6.3.6", title: "Skill: Configuring service and application logging (e.g. CloudTrail, Amazon CloudWatch Logs)" }
  - { id: "6.3.7", title: "Skill: Analyzing logs, metrics, and security findings" }
---
## Exam format

All facts are as of 2026-10-24, taken from the [certification page](https://aws.amazon.com/certification/certified-devops-engineer-professional/) and the [DOP-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/devops-engineer-professional-02/devops-engineer-professional-02.html). Confirm them on the official page before you book.

| Item | DOP-C02 (as of 2026-10-24) |
|---|---|
| Question types | Multiple choice (one correct answer out of four) and multiple response (two or more correct answers out of five or more; all must be selected for credit) |
| Number of questions | 75 in total: 65 scored and 10 unscored |
| Duration | 180 minutes |
| Passing score | 750 on a scaled score of 100–1,000, compensatory across domains |
| Price | 300 USD. AWS's exam pricing page has further cost information, including foreign exchange rates. Once you earn one AWS certification, AWS gives you a 50% discount on your next AWS certification exam |
| Languages | English, Japanese, Korean, Simplified Chinese. The page says the Korean version will be retired after December 31, 2026 |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | 3 years. You renew by passing the latest version |
| Prerequisites | None required. AWS recommends 2 or more years provisioning, operating and managing AWS environments, plus software development lifecycle and programming or scripting experience |
| Version news | The page announces no DOP-C03 as of 2026-10-24. Check again before booking, because AWS has been refreshing its professional exams (the SAP certification page says SAP-C03 registration opens October 27, 2026) |

## What the exam really tests

DOP-C02 is the operator's professional exam. It asks how you would automate the delivery, configuration, observation and protection of AWS workloads across many accounts and Regions, and how you would react when something breaks. The guide puts advanced networking, deep security advice to developers, database design and tuning, and full-stack coding **out of scope**.

- **SDLC automation (22%, the largest).** AWS CodePipeline, CodeBuild, CodeDeploy and CodeArtifact, Amazon ECR, EC2 Image Builder, secrets in pipelines (Secrets Manager, Parameter Store), test stages, cross-account pipelines, and deployment strategies for EC2, ECS, EKS and Lambda (in-place, rolling, blue/green, canary, linear).
- **Configuration management and IaC (17%).** CloudFormation (stack sets, modules, change sets, drift, helper scripts), AWS CDK and AWS SAM, Service Catalog, Systems Manager (State Manager, Patch Manager, Automation, Inventory), AWS Config, AppConfig, and account vending with Organizations and Control Tower.
- **Resilient cloud solutions (15%).** Multi-AZ and multi-Region designs, failover for RDS, Aurora, DynamoDB global tables and Route 53, scaling ECS, EKS, Lambda and Auto Scaling groups, and backup and recovery against RTO and RPO.
- **Monitoring and logging (15%).** CloudWatch metrics, metric filters, metric streams, the agent, Logs Insights, subscriptions to Kinesis, Lambda or OpenSearch Service, anomaly detection, dashboards, X-Ray, and log encryption and retention.
- **Incident and event response (14%).** EventBridge rules and patterns, AWS Health events, fan-out with SNS and SQS, Step Functions workflows, auto-remediation with Config and Systems Manager, and troubleshooting failed deployments and scaling events.
- **Security and compliance (17%).** IAM at scale (roles, federation, permissions boundaries, SCPs), credential rotation, defence-in-depth automation (Security Hub, GuardDuty, Config, AWS WAF, Network Firewall), Macie for sensitive-data discovery, and audit trails with CloudTrail and Config.

Where candidates lose points:

- **CodeDeploy details.** The appspec file and lifecycle hooks, the deployment configurations for EC2, ECS and Lambda, and automatic rollback on CloudWatch alarms. Many questions are decided by which hook or configuration fits.
- **CloudFormation behaviour.** Update policies and creation policies, `DeletionPolicy` and `UpdateReplacePolicy`, custom resources, stack set deployment targets and failure tolerance, and why a stack goes into `UPDATE_ROLLBACK_FAILED`.
- **Event wiring.** Knowing that an EventBridge rule can match a CodePipeline state change, a GuardDuty finding or an AWS Health event and target Lambda, SSM Automation or Step Functions, with no custom polling.
- **Managed over custom.** The answer that adds a Lambda function to poll something is usually wrong when a native integration (Config remediation, EventBridge, a CodeDeploy alarm rollback) exists.

## Study strategy

1. **Foundations.** Make sure IAM roles and policies, VPC basics, EC2 Auto Scaling, ELB, ECS and Lambda are comfortable. The SOA-C03 and DVA-C03 objectives in this library cover that ground at associate depth.
2. **Pipelines hands-on.** Build a CodePipeline that pulls from a Git repository, builds a .NET app in CodeBuild, publishes a NuGet package to CodeArtifact and an image to ECR, and deploys with CodeDeploy blue/green to ECS and canary to Lambda. Add a manual approval and a cross-account deploy stage.
3. **IaC depth.** Write the same stack in CloudFormation and in CDK (C# is supported), deploy it with stack sets to two accounts and two Regions, break an update on purpose, and recover it.
4. **Systems Manager.** Patch a fleet with Patch Manager and maintenance windows, enforce a desired state with State Manager, and run an Automation runbook from an EventBridge rule.
5. **Observability.** Ship application logs with the CloudWatch agent, add a metric filter and alarm, stream logs to OpenSearch Service, and trace a request through API Gateway and Lambda with X-Ray.
6. **Governance and security automation.** Config rules with auto-remediation, Security Hub across an organization, and rotating a secret with Secrets Manager.

Official resources named on the certification page (as of 2026-10-24) are the AWS Skill Builder **Exam Prep Plan** (four steps), the **Official Practice Question Set**, digital courses, **AWS Builder Labs**, **AWS Cloud Quest**, **AWS Jam**, **AWS SimuLearn**, flashcards, exam-style questions and instructor walkthroughs of them, the **Official Practice Exam**, and AWS Training Live on Twitch.

How your background helps or misleads:

- **AZ-204 preparation** gives you CI/CD and app-configuration ideas, but Azure DevOps or GitHub Actions pipelines don't map cleanly onto CodePipeline stages and actions, and Azure App Configuration is not quite AppConfig. Learn the AWS deployment primitives, especially CodeDeploy, on their own terms.
- **CKAD preparation** helps with rolling and blue/green thinking, probes and EKS questions. On AWS the "health" that drives a rollback is usually an ELB target health check or a CloudWatch alarm, not a Kubernetes probe.
- **.NET experience** is directly usable in CDK and CodeBuild.

## Differences from related exams

- **DOP-C02 vs AZ-400 (Designing and Implementing Microsoft DevOps Solutions).** They are counterparts. AZ-400 is broader on process and tooling: source control strategy, work tracking, GitHub and Azure DevOps, package management, security and compliance in pipelines, and instrumentation. It is platform-agnostic in places and expects AZ-104 or AZ-204 for the credential. DOP-C02 has no prerequisite but goes deeper into operations: resilience, incident response, auto-remediation and multi-account security automation are a much larger share than in AZ-400. Also check the AZ-401 entry in this library, Microsoft's newer DevOps exam.
- **DOP-C02 vs SOA-C03 (CloudOps Engineer – Associate).** SOA covers the same operational services at associate depth and with shorter scenarios. DOP adds pipelines, multi-account automation and professional-length trade-off questions.
- **DOP-C02 vs DVA-C03 (Developer – Associate).** DVA is about writing and deploying code against AWS services, with some CI/CD. DOP assumes that and moves to fleets, organizations and automated operations.
- **DOP-C02 vs SAP-C03.** SAP chooses the architecture; DOP automates, observes and repairs it. They overlap on governance, DR and deployment strategies.
- **DOP-C02 vs GH-200 (GitHub Actions).** GH-200 tests GitHub Actions in depth (workflows, runners, reusable actions). DOP tests AWS-native pipelines and only touches third-party tooling.

## Exam-day notes

- **Time budget.** 180 minutes for 75 questions is about 2 minutes 24 seconds each. DOP scenarios are shorter than SAP's but denser in configuration detail, so read each answer option fully. Two options often differ by one setting.
- **Find the automation verb.** "Automatically", "with the least manual effort" and "without custom code" point to native integrations: EventBridge plus SSM Automation, Config remediation, CodeDeploy alarm-based rollback, or stack set auto-deployment.
- **Deployment questions.** First work out the compute platform (EC2 or on-premises, ECS, Lambda), because the available CodeDeploy configurations differ for each. Then match the risk profile (all-at-once, rolling, canary, linear, blue/green).
- **Multi-account questions.** Look for the delegated-administrator or organization-wide feature before picking an answer that loops through accounts.
- **Short names.** The certification page says the exam uses short names for some AWS services, and a list of short and full names is available through the Help button during the exam.
- **Flag and move on.** Leave nothing blank. There is no penalty for guessing.
