---
code: SAA-C03
title: "AWS Certified Solutions Architect – Associate"
credential: "AWS Certified Solutions Architect – Associate"
provider: aws
tracks: [cloud, architect]
clouds: [aws]
level: associate
tier: core
stage: "2"
progress: planned
official_url: https://aws.amazon.com/certification/certified-solutions-architect-associate/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html
outline_version: "undated (HTML guide, retrieved 2026-10-24)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends at least 1 year of hands-on experience designing cloud solutions that use AWS services."
replaces: ""
replaced_by: ""
counterparts: [az-104]
objectives:
  - { id: "1", title: "Design Secure Architectures", weight: "30%" }
  - { id: "1.1", title: "Design secure access to AWS resources" }
  - { id: "1.1.1", title: "Knowledge: Access controls and management across multiple accounts" }
  - { id: "1.1.2", title: "Knowledge: AWS federated access and identity services (for example, IAM, AWS IAM Identity Center)" }
  - { id: "1.1.3", title: "Knowledge: AWS global infrastructure (for example, Availability Zones, AWS Regions)" }
  - { id: "1.1.4", title: "Knowledge: AWS security best practices (for example, the principle of least privilege)" }
  - { id: "1.1.5", title: "Knowledge: The AWS shared responsibility model" }
  - { id: "1.1.6", title: "Skill: Applying AWS security best practices to IAM users and root users (for example, multi-factor authentication [MFA])" }
  - { id: "1.1.7", title: "Skill: Designing a flexible authorization model that includes IAM users, groups, roles, and policies" }
  - { id: "1.1.8", title: "Skill: Designing a role-based access control strategy (for example, AWS STS, role switching, cross-account access)" }
  - { id: "1.1.9", title: "Skill: Designing a security strategy for multiple AWS accounts (for example, AWS Control Tower, service control policies [SCPs])" }
  - { id: "1.1.10", title: "Skill: Determining the appropriate use of resource policies for AWS services" }
  - { id: "1.1.11", title: "Skill: Determining when to federate a directory service with IAM roles" }
  - { id: "1.2", title: "Design secure workloads and applications" }
  - { id: "1.2.1", title: "Knowledge: Application configuration and credentials security" }
  - { id: "1.2.2", title: "Knowledge: AWS service endpoints" }
  - { id: "1.2.3", title: "Knowledge: Control ports, protocols, and network traffic on AWS" }
  - { id: "1.2.4", title: "Knowledge: Secure application access" }
  - { id: "1.2.5", title: "Knowledge: Security services with appropriate use cases (for example, Amazon Cognito, Amazon GuardDuty, Amazon Macie)" }
  - { id: "1.2.6", title: "Knowledge: Threat vectors external to AWS (for example, DDoS, SQL injection)" }
  - { id: "1.2.7", title: "Skill: Designing VPC architectures with security components (for example, security groups, route tables, network ACLs, NAT gateways)" }
  - { id: "1.2.8", title: "Skill: Determining network segmentation strategies (for example, using public subnets and private subnets)" }
  - { id: "1.2.9", title: "Skill: Integrating AWS services to secure applications (for example, AWS Shield, AWS WAF, IAM Identity Center, AWS Secrets Manager)" }
  - { id: "1.2.10", title: "Skill: Securing external network connections to and from the AWS Cloud (for example, VPN, AWS Direct Connect)" }
  - { id: "1.3", title: "Determine appropriate data security controls" }
  - { id: "1.3.1", title: "Knowledge: Data access and governance" }
  - { id: "1.3.2", title: "Knowledge: Data recovery" }
  - { id: "1.3.3", title: "Knowledge: Data retention and classification" }
  - { id: "1.3.4", title: "Knowledge: Encryption and appropriate key management" }
  - { id: "1.3.5", title: "Skill: Aligning AWS technologies to meet compliance requirements" }
  - { id: "1.3.6", title: "Skill: Encrypting data at rest (for example, AWS KMS)" }
  - { id: "1.3.7", title: "Skill: Encrypting data in transit (for example, AWS Certificate Manager [ACM] using TLS)" }
  - { id: "1.3.8", title: "Skill: Implementing access policies for encryption keys" }
  - { id: "1.3.9", title: "Skill: Implementing data backups and replications" }
  - { id: "1.3.10", title: "Skill: Implementing policies for data access, lifecycle, and protection" }
  - { id: "1.3.11", title: "Skill: Rotating encryption keys and renewing certificates" }
  - { id: "2", title: "Design Resilient Architectures", weight: "26%" }
  - { id: "2.1", title: "Design scalable and loosely coupled architectures" }
  - { id: "2.1.1", title: "Knowledge: API creation and management (for example, Amazon API Gateway, REST API)" }
  - { id: "2.1.2", title: "Knowledge: AWS managed services with appropriate use cases (for example, AWS Transfer Family, Amazon SQS, AWS Secrets Manager)" }
  - { id: "2.1.3", title: "Knowledge: Caching strategies" }
  - { id: "2.1.4", title: "Knowledge: Design principles for microservices (for example, stateless workloads compared with stateful workloads)" }
  - { id: "2.1.5", title: "Knowledge: Event-driven architectures" }
  - { id: "2.1.6", title: "Knowledge: Horizontal scaling and vertical scaling" }
  - { id: "2.1.7", title: "Knowledge: How to appropriately use edge accelerators (for example, content delivery network [CDN])" }
  - { id: "2.1.8", title: "Knowledge: How to migrate applications into containers" }
  - { id: "2.1.9", title: "Knowledge: Load balancing concepts (for example, Application Load Balancer [ALB])" }
  - { id: "2.1.10", title: "Knowledge: Multi-tier architectures" }
  - { id: "2.1.11", title: "Knowledge: Queuing and messaging concepts (for example, publish/subscribe)" }
  - { id: "2.1.12", title: "Knowledge: Serverless technologies and patterns (for example, AWS Fargate, AWS Lambda)" }
  - { id: "2.1.13", title: "Knowledge: Storage types with associated characteristics (for example, object, file, block)" }
  - { id: "2.1.14", title: "Knowledge: The orchestration of containers (for example, Amazon ECS, Amazon EKS)" }
  - { id: "2.1.15", title: "Knowledge: When to use read replicas" }
  - { id: "2.1.16", title: "Knowledge: Workflow orchestration (for example, AWS Step Functions)" }
  - { id: "2.1.17", title: "Skill: Designing event-driven, microservice, and/or multi-tier architectures based on requirements" }
  - { id: "2.1.18", title: "Skill: Determining scaling strategies for components used in an architecture design" }
  - { id: "2.1.19", title: "Skill: Determining the AWS services required to achieve loose coupling based on requirements" }
  - { id: "2.1.20", title: "Skill: Determining when to use containers" }
  - { id: "2.1.21", title: "Skill: Determining when to use serverless technologies and patterns" }
  - { id: "2.1.22", title: "Skill: Recommending appropriate compute, storage, networking, and database technologies based on requirements" }
  - { id: "2.1.23", title: "Skill: Using purpose-built AWS services for workloads" }
  - { id: "2.2", title: "Design highly available and/or fault-tolerant architectures" }
  - { id: "2.2.1", title: "Knowledge: AWS global infrastructure (for example, Availability Zones, AWS Regions, Amazon Route 53)" }
  - { id: "2.2.2", title: "Knowledge: AWS Managed Services (AMS) with appropriate use cases (for example, Amazon Comprehend, Amazon Polly)" }
  - { id: "2.2.3", title: "Knowledge: Basic networking concepts (for example, route tables)" }
  - { id: "2.2.4", title: "Knowledge: Disaster recovery (DR) strategies (for example, backup and restore, pilot light, warm standby, active-active failover, recovery point objective [RPO], recovery time objective [RTO])" }
  - { id: "2.2.5", title: "Knowledge: Distributed design patterns" }
  - { id: "2.2.6", title: "Knowledge: Failover strategies" }
  - { id: "2.2.7", title: "Knowledge: Immutable infrastructure" }
  - { id: "2.2.8", title: "Knowledge: Load balancing concepts (for example, ALB)" }
  - { id: "2.2.9", title: "Knowledge: Proxy concepts (for example, Amazon RDS Proxy)" }
  - { id: "2.2.10", title: "Knowledge: Service quotas and throttling (for example, how to configure the service quotas for a workload in a standby environment)" }
  - { id: "2.2.11", title: "Knowledge: Storage options and characteristics (for example, durability, replication)" }
  - { id: "2.2.12", title: "Knowledge: Workload visibility (for example, AWS X-Ray)" }
  - { id: "2.2.13", title: "Skill: Determining automation strategies to ensure infrastructure integrity" }
  - { id: "2.2.14", title: "Skill: Determining the AWS services required to provide a highly available and/or fault-tolerant architecture across AWS Regions or Availability Zones" }
  - { id: "2.2.15", title: "Skill: Identifying metrics based on business requirements to deliver a highly available solution" }
  - { id: "2.2.16", title: "Skill: Implementing designs to mitigate single points of failure" }
  - { id: "2.2.17", title: "Skill: Implementing strategies to ensure the durability and availability of data (for example, backups)" }
  - { id: "2.2.18", title: "Skill: Selecting an appropriate DR strategy to meet business requirements" }
  - { id: "2.2.19", title: "Skill: Using AWS services that improve the reliability of legacy applications and applications not built for the cloud (for example, when application changes are not possible)" }
  - { id: "2.2.20", title: "Skill: Using purpose-built AWS services for workloads" }
  - { id: "3", title: "Design High-Performing Architectures", weight: "24%" }
  - { id: "3.1", title: "Determine high-performing and/or scalable storage solutions" }
  - { id: "3.1.1", title: "Knowledge: Hybrid storage solutions to meet business requirements" }
  - { id: "3.1.2", title: "Knowledge: Storage services with appropriate use cases (for example, Amazon S3, Amazon EFS, Amazon EBS)" }
  - { id: "3.1.3", title: "Knowledge: Storage types with associated characteristics (for example, object, file, block)" }
  - { id: "3.1.4", title: "Skill: Determining storage services and configurations that meet performance demands" }
  - { id: "3.1.5", title: "Skill: Determining storage services that can scale to accommodate future needs" }
  - { id: "3.2", title: "Design high-performing and elastic compute solutions" }
  - { id: "3.2.1", title: "Knowledge: AWS compute services with appropriate use cases (for example, AWS Batch, Amazon EMR, AWS Fargate)" }
  - { id: "3.2.2", title: "Knowledge: Distributed computing concepts supported by AWS global infrastructure and edge services" }
  - { id: "3.2.3", title: "Knowledge: Queuing and messaging concepts (for example, publish/subscribe)" }
  - { id: "3.2.4", title: "Knowledge: Scalability capabilities with appropriate use cases (for example, Amazon EC2 Auto Scaling, AWS Auto Scaling)" }
  - { id: "3.2.5", title: "Knowledge: Serverless technologies and patterns (for example, AWS Lambda, Fargate)" }
  - { id: "3.2.6", title: "Knowledge: The orchestration of containers (for example, Amazon ECS, Amazon EKS)" }
  - { id: "3.2.7", title: "Skill: Decoupling workloads so that components can scale independently" }
  - { id: "3.2.8", title: "Skill: Identifying metrics and conditions to perform scaling actions" }
  - { id: "3.2.9", title: "Skill: Selecting the appropriate compute options and features (for example, EC2 instance types) to meet business requirements" }
  - { id: "3.2.10", title: "Skill: Selecting the appropriate resource type and size (for example, the amount of Lambda memory) to meet business requirements" }
  - { id: "3.3", title: "Determine high-performing database solutions" }
  - { id: "3.3.1", title: "Knowledge: AWS global infrastructure (for example, Availability Zones, AWS Regions)" }
  - { id: "3.3.2", title: "Knowledge: Caching strategies and services (for example, Amazon ElastiCache)" }
  - { id: "3.3.3", title: "Knowledge: Data access patterns (for example, read-intensive compared with write-intensive)" }
  - { id: "3.3.4", title: "Knowledge: Database capacity planning (for example, capacity units, instance types, Provisioned IOPS)" }
  - { id: "3.3.5", title: "Knowledge: Database connections and proxies" }
  - { id: "3.3.6", title: "Knowledge: Database engines with appropriate use cases (for example, heterogeneous migrations, homogeneous migrations)" }
  - { id: "3.3.7", title: "Knowledge: Database replication (for example, read replicas)" }
  - { id: "3.3.8", title: "Knowledge: Database types and services (for example, serverless, relational compared with non-relational, in-memory)" }
  - { id: "3.3.9", title: "Skill: Configuring read replicas to meet business requirements" }
  - { id: "3.3.10", title: "Skill: Designing database architectures" }
  - { id: "3.3.11", title: "Skill: Determining an appropriate database engine (for example, MySQL compared with PostgreSQL)" }
  - { id: "3.3.12", title: "Skill: Determining an appropriate database type (for example, Amazon Aurora, Amazon DynamoDB)" }
  - { id: "3.3.13", title: "Skill: Integrating caching to meet business requirements" }
  - { id: "3.4", title: "Determine high-performing and/or scalable network architectures" }
  - { id: "3.4.1", title: "Knowledge: Edge networking services with appropriate use cases (for example, Amazon CloudFront, AWS Global Accelerator)" }
  - { id: "3.4.2", title: "Knowledge: How to design network architecture (for example, subnet tiers, routing, IP addressing)" }
  - { id: "3.4.3", title: "Knowledge: Load balancing concepts (for example, Application Load Balancer [ALB])" }
  - { id: "3.4.4", title: "Knowledge: Network connection options (for example, AWS VPN, AWS Direct Connect, AWS PrivateLink)" }
  - { id: "3.4.5", title: "Skill: Creating a network topology for various architectures (for example, global, hybrid, multi-tier)" }
  - { id: "3.4.6", title: "Skill: Determining network configurations that can scale to accommodate future needs" }
  - { id: "3.4.7", title: "Skill: Determining the appropriate placement of resources to meet business requirements" }
  - { id: "3.4.8", title: "Skill: Selecting the appropriate load balancing strategy" }
  - { id: "3.5", title: "Determine high-performing data ingestion and transformation solutions" }
  - { id: "3.5.1", title: "Knowledge: Data analytics and visualization services with appropriate use cases (for example, Amazon Athena, AWS Lake Formation, Amazon Quick)" }
  - { id: "3.5.2", title: "Knowledge: Data ingestion patterns (for example, frequency)" }
  - { id: "3.5.3", title: "Knowledge: Data transfer services with appropriate use cases (for example, AWS DataSync, AWS Storage Gateway)" }
  - { id: "3.5.4", title: "Knowledge: Data transformation services with appropriate use cases (for example, AWS Glue)" }
  - { id: "3.5.5", title: "Knowledge: Secure access to ingestion access points" }
  - { id: "3.5.6", title: "Knowledge: Sizes and speeds needed to meet business requirements" }
  - { id: "3.5.7", title: "Knowledge: Streaming data services with appropriate use cases (for example, Amazon Kinesis)" }
  - { id: "3.5.8", title: "Skill: Building and securing data lakes" }
  - { id: "3.5.9", title: "Skill: Designing data streaming architectures" }
  - { id: "3.5.10", title: "Skill: Designing data transfer solutions" }
  - { id: "3.5.11", title: "Skill: Implementing visualization strategies" }
  - { id: "3.5.12", title: "Skill: Selecting appropriate compute options for data processing (for example, Amazon EMR)" }
  - { id: "3.5.13", title: "Skill: Selecting appropriate configurations for ingestion" }
  - { id: "3.5.14", title: "Skill: Transforming data between formats (for example, .csv to .parquet)" }
  - { id: "4", title: "Design Cost-Optimized Architectures", weight: "20%" }
  - { id: "4.1", title: "Design cost-optimized storage solutions" }
  - { id: "4.1.1", title: "Knowledge: Access options (for example, an S3 bucket with Requester Pays object storage)" }
  - { id: "4.1.2", title: "Knowledge: AWS cost management service features (for example, cost allocation tags, multi-account billing)" }
  - { id: "4.1.3", title: "Knowledge: AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)" }
  - { id: "4.1.4", title: "Knowledge: AWS storage services with appropriate use cases (for example, Amazon FSx, Amazon EFS, Amazon S3, Amazon EBS)" }
  - { id: "4.1.5", title: "Knowledge: Backup strategies" }
  - { id: "4.1.6", title: "Knowledge: Block storage options (for example, hard disk drive [HDD] volume types, solid state drive [SSD] volume types)" }
  - { id: "4.1.7", title: "Knowledge: Data lifecycles" }
  - { id: "4.1.8", title: "Knowledge: Hybrid storage options (for example, AWS DataSync, AWS Transfer Family, AWS Storage Gateway)" }
  - { id: "4.1.9", title: "Knowledge: Storage access patterns" }
  - { id: "4.1.10", title: "Knowledge: Storage tiering (for example, cold tiering for object storage)" }
  - { id: "4.1.11", title: "Knowledge: Storage types with associated characteristics (for example, object, file, block)" }
  - { id: "4.1.12", title: "Skill: Designing appropriate storage strategies (for example, batch uploads to Amazon S3 compared with individual uploads)" }
  - { id: "4.1.13", title: "Skill: Determining the correct storage size for a workload" }
  - { id: "4.1.14", title: "Skill: Determining the lowest cost method of transferring data for a workload to AWS storage" }
  - { id: "4.1.15", title: "Skill: Determining when storage auto scaling is required" }
  - { id: "4.1.16", title: "Skill: Managing S3 object lifecycles" }
  - { id: "4.1.17", title: "Skill: Selecting the appropriate backup and/or archival solution" }
  - { id: "4.1.18", title: "Skill: Selecting the appropriate service for data migration to storage services" }
  - { id: "4.1.19", title: "Skill: Selecting the appropriate storage tier" }
  - { id: "4.1.20", title: "Skill: Selecting the correct data lifecycle for storage" }
  - { id: "4.1.21", title: "Skill: Selecting the most cost-effective storage service for a workload" }
  - { id: "4.2", title: "Design cost-optimized compute solutions" }
  - { id: "4.2.1", title: "Knowledge: AWS cost management service features (for example, cost allocation tags, multi-account billing)" }
  - { id: "4.2.2", title: "Knowledge: AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)" }
  - { id: "4.2.3", title: "Knowledge: AWS global infrastructure (for example, Availability Zones, AWS Regions)" }
  - { id: "4.2.4", title: "Knowledge: AWS purchasing options (for example, Spot Instances, Reserved Instances, Savings Plans)" }
  - { id: "4.2.5", title: "Knowledge: Distributed compute strategies (for example, edge processing)" }
  - { id: "4.2.6", title: "Knowledge: Hybrid compute options (for example, AWS Outposts)" }
  - { id: "4.2.7", title: "Knowledge: Instance types, families, and sizes (for example, memory optimized, compute optimized, virtualization)" }
  - { id: "4.2.8", title: "Knowledge: Optimization of compute utilization (for example, containers, serverless computing, microservices)" }
  - { id: "4.2.9", title: "Knowledge: Scaling strategies (for example, auto scaling, hibernation)" }
  - { id: "4.2.10", title: "Skill: Determining an appropriate load balancing strategy (for example, Application Load Balancer [Layer 7] compared with Network Load Balancer [Layer 4] compared with Gateway Load Balancer)" }
  - { id: "4.2.11", title: "Skill: Determining appropriate scaling methods and strategies for elastic workloads (for example, horizontal compared with vertical, EC2 hibernation)" }
  - { id: "4.2.12", title: "Skill: Determining cost-effective AWS compute services with appropriate use cases (for example, AWS Lambda, Amazon EC2, AWS Fargate)" }
  - { id: "4.2.13", title: "Skill: Determining the required availability for different classes of workloads (for example, production workloads, non-production workloads)" }
  - { id: "4.2.14", title: "Skill: Selecting the appropriate instance family for a workload" }
  - { id: "4.2.15", title: "Skill: Selecting the appropriate instance size for a workload" }
  - { id: "4.3", title: "Design cost-optimized database solutions" }
  - { id: "4.3.1", title: "Knowledge: AWS cost management service features (for example, cost allocation tags, multi-account billing)" }
  - { id: "4.3.2", title: "Knowledge: AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)" }
  - { id: "4.3.3", title: "Knowledge: Caching strategies" }
  - { id: "4.3.4", title: "Knowledge: Data retention policies" }
  - { id: "4.3.5", title: "Knowledge: Database capacity planning (for example, capacity units)" }
  - { id: "4.3.6", title: "Knowledge: Database connections and proxies" }
  - { id: "4.3.7", title: "Knowledge: Database engines with appropriate use cases (for example, heterogeneous migrations, homogeneous migrations)" }
  - { id: "4.3.8", title: "Knowledge: Database replication (for example, read replicas)" }
  - { id: "4.3.9", title: "Knowledge: Database types and services (for example, relational compared with non-relational, Amazon Aurora, Amazon DynamoDB)" }
  - { id: "4.3.10", title: "Skill: Designing appropriate backup and retention policies (for example, snapshot frequency)" }
  - { id: "4.3.11", title: "Skill: Determining an appropriate database engine (for example, MySQL compared with PostgreSQL)" }
  - { id: "4.3.12", title: "Skill: Determining cost-effective AWS database services with appropriate use cases (for example, DynamoDB compared with Amazon RDS, serverless)" }
  - { id: "4.3.13", title: "Skill: Determining cost-effective AWS database types (for example, time series format, columnar format)" }
  - { id: "4.3.14", title: "Skill: Migrating database schemas and data to different locations and/or different database engines" }
  - { id: "4.4", title: "Design cost-optimized network architectures" }
  - { id: "4.4.1", title: "Knowledge: AWS cost management service features (for example, cost allocation tags, multi-account billing)" }
  - { id: "4.4.2", title: "Knowledge: AWS cost management tools with appropriate use cases (for example, AWS Cost Explorer, AWS Budgets, AWS Cost and Usage Report)" }
  - { id: "4.4.3", title: "Knowledge: Load balancing concepts (for example, Application Load Balancer [ALB])" }
  - { id: "4.4.4", title: "Knowledge: NAT gateways (for example, NAT instance costs compared with NAT gateway costs)" }
  - { id: "4.4.5", title: "Knowledge: Network connectivity (for example, private lines, dedicated lines, VPNs)" }
  - { id: "4.4.6", title: "Knowledge: Network routing, topology, and peering (for example, AWS Transit Gateway, VPC peering)" }
  - { id: "4.4.7", title: "Knowledge: Network services with appropriate use cases (for example, DNS)" }
  - { id: "4.4.8", title: "Skill: Configuring appropriate NAT gateway types for a network (for example, a single shared NAT gateway compared with NAT gateways for each Availability Zone)" }
  - { id: "4.4.9", title: "Skill: Configuring appropriate network connections (for example, AWS Direct Connect compared with VPN compared with internet)" }
  - { id: "4.4.10", title: "Skill: Configuring appropriate network routes to minimize network transfer costs (for example, Region to Region, Availability Zone to Availability Zone, private to public, AWS Global Accelerator, VPC endpoints)" }
  - { id: "4.4.11", title: "Skill: Determining strategic needs for content delivery networks (CDNs) and edge caching" }
  - { id: "4.4.12", title: "Skill: Reviewing existing workloads for network optimizations" }
  - { id: "4.4.13", title: "Skill: Selecting an appropriate throttling strategy" }
  - { id: "4.4.14", title: "Skill: Selecting the appropriate bandwidth allocation for a network device (for example, a single VPN compared with multiple VPNs, Direct Connect speed)" }
---
## Exam format

Every fact below is as of 2026-10-24 and comes from the [certification page](https://aws.amazon.com/certification/certified-solutions-architect-associate/) and the [SAA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html). Confirm both before you book.

| Item | Detail (as of 2026-10-24) |
| --- | --- |
| Category | Associate |
| Question types | Multiple choice (one correct answer out of four) and multiple response (two or more correct answers out of five or more options) |
| Number of questions | 65: 50 scored and 15 unscored (the unscored ones are not marked) |
| Duration | 130 minutes |
| Passing score | 720 on a scaled score of 100–1,000. Scoring is compensatory |
| Price | 150 USD (see [exam pricing](https://aws.amazon.com/certification/policies/before-testing/)) |
| Languages | English, French (France), Italian, Japanese, Korean, Portuguese (Brazil), Spanish (Latin America), Spanish (Spain), Simplified Chinese and Traditional Chinese. The Italian version will be retired after December 31, 2026 |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | Valid for 3 years. You can recertify by passing the latest version, or automatically by earning Solutions Architect – Professional (see [recertification](https://aws.amazon.com/certification/recertification/)) |
| Service names | The page says the exam uses short names for some services, and a list of short names is available from the Help button during the exam |

The exam guide does not print a version number or date. This library records it as undated and last checked it on 2026-10-24. As of 2026-10-24 the certification page carries no exam-update notice for SAA-C03. The [AWS blog of September 2026](https://aws.amazon.com/blogs/training-and-certification/september-2026-new-offerings/) moves the Professional exam to SAP-C03 on November 17, 2026, but announces no change to the Associate exam.

## What the exam really tests

SAA-C03 tests one skill four ways: **given requirements and constraints, pick the AWS design that satisfies them best.** The four domains are the Well-Architected pillars, rephrased as design verbs:

- **Design Secure Architectures (30%)**: IAM users, groups, roles and policies; STS and cross-account roles; IAM Identity Center and federation; multi-account guardrails with AWS Control Tower and SCPs; resource policies. Inside the VPC it covers security groups, network ACLs, public and private subnets and NAT, plus Shield, WAF, Cognito, GuardDuty, Macie and Secrets Manager. For data it covers KMS key policies and rotation, ACM and TLS, backups, replication and lifecycle policies.
- **Design Resilient Architectures (26%)**: loose coupling (SQS, SNS, EventBridge, API Gateway, Step Functions), containers compared with serverless, read replicas, caching, horizontal compared with vertical scaling; then high availability and disaster recovery. That means Multi-AZ, Route 53 failover, the four DR strategies with their RPO and RTO (backup and restore, pilot light, warm standby, active-active), RDS Proxy, service quotas in a standby Region, and immutable infrastructure.
- **Design High-Performing Architectures (24%)**: storage choice (S3, EFS, EBS, FSx, hybrid storage), compute choice and sizing (EC2 families, Lambda memory, Batch, EMR, Fargate, Auto Scaling metrics), database choice (Aurora compared with DynamoDB, engine choice, Provisioned IOPS, ElastiCache), network design (CloudFront compared with Global Accelerator, subnet tiers, VPN, Direct Connect, PrivateLink) and **data ingestion** (Kinesis, Glue, Athena, Lake Formation, DataSync, Amazon Quick, converting CSV to Parquet).
- **Design Cost-Optimized Architectures (20%)**: S3 storage classes and lifecycle, EBS volume types, the cheapest way to move data in, Spot, Reserved Instances and Savings Plans, ALB compared with NLB compared with GWLB, DynamoDB compared with RDS, NAT gateway placement, and routing that keeps transfer charges down (VPC endpoints, staying within an AZ).

The questions are 3–6 sentence scenarios. Usually **two answers work**, and the stem's qualifier picks the winner: "MOST cost-effective", "LEAST operational overhead", "with minimal changes to the application", "highly available". Candidates lose points when they:

1. Pick a technically correct answer that ignores the qualifier. Custom code on EC2 loses to a managed service when the stem says "least operational overhead".
2. Confuse near-equivalents: SQS (a queue you poll) compared with SNS (push and fan-out) compared with EventBridge (event routing with rules); CloudFront (caches HTTP at the edge) compared with Global Accelerator (anycast IPs for TCP and UDP, fast regional failover); Aurora Global Database compared with cross-Region read replicas; EFS (Linux NFS) compared with FSx for Windows File Server (SMB) compared with FSx for Lustre (HPC).
3. Forget which way traffic or encryption flows: a gateway VPC endpoint (S3 and DynamoDB, free) compared with an interface endpoint (PrivateLink, charged hourly); SSE-S3 compared with SSE-KMS compared with client-side encryption.

## Study strategy

1. **Do the foundations first: networking and IAM.** Build a VPC by hand: two AZs, public and private subnets, an internet gateway, a NAT gateway, route tables, security groups and a network ACL. Then write IAM policies, including a cross-account role. Every domain assumes you can do this without thinking.
2. **Then compute and storage, then databases, then integration, then analytics.** Each layer reuses the one beneath it. Keep a "pick-one" sheet for each category (storage, database, messaging, edge, DR) with the deciding question for each pair.
3. **Hands-on work that matters.** An Auto Scaling group behind an ALB across two AZs; an S3 bucket with lifecycle rules, versioning and a bucket policy; RDS Multi-AZ with a read replica; a Lambda function triggered by SQS; a CloudFront distribution in front of S3. Then tear it all down and set an AWS Budget alarm first. Using CloudFormation or the CDK (C# is supported) helps you make these environments repeatable.
4. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (the Official Practice Question Set, the exam-prep course, AWS Builder Labs, AWS SimuLearn, AWS Escape Room and the Official Practice Exam); the [exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html) with its in-scope service list; the AWS Well-Architected Framework whitepaper, which is the source of the exam's way of thinking.
5. **How your background helps or misleads.**
    - *AZ-900 and AZ-104-style thinking*: the concepts transfer, but the boundaries are different. AWS security groups are stateful and attach to network interfaces, much like an Azure NSG on a NIC, but network ACLs are **stateless** subnet filters, and that difference is a favourite exam topic. Azure subnets can span zones, while an AWS subnet sits in exactly one AZ. A "public subnet" in AWS just means its route table has a route to an internet gateway.
    - *AZ-204 preparation*: your knowledge of Functions, Service Bus and Cosmos DB maps to Lambda, SQS and SNS, and DynamoDB, which speeds up Domain 2. Don't carry Cosmos DB consistency levels into DynamoDB answers: DynamoDB offers eventually consistent or strongly consistent reads, plus global tables.
    - *CKAD preparation*: EKS questions here are about choosing it, not running it. "Already on Kubernetes, want managed" points to EKS; "no servers to manage" points to Fargate.
    - *.NET*: FSx for Windows File Server, licence-included compared with BYOL Windows on EC2, and directory federation questions will feel familiar.

Expect 6–10 weeks part-time. This is the core AWS architect exam on your path and the counterpart of AZ-104 for this library. Take CLF-C02 first if you want the vocabulary to feel easy.

## Differences from related exams

- **SAA-C03 compared with AZ-104 (the counterpart this library pairs it with).** The scope overlaps heavily: identity, networking, compute, storage, backup and monitoring. The **style differs completely**. AZ-104 is an administrator exam that asks how to configure something (which blade, setting, PowerShell or CLI parameter, RBAC scope). SAA-C03 is a design exam that asks which architecture to build and why, and almost never asks for console steps or CLI syntax. AZ-104 has more governance mechanics (Azure Policy, locks, management groups, RBAC scopes). SAA-C03 has far more trade-off reasoning about cost, decoupling, DR and data ingestion. The closest AWS exam to AZ-104 in style is SOA-C03.
- **SAA-C03 compared with AZ-305 (Azure Solutions Architect Expert).** These two match on style (design and trade-offs), but AZ-305 is expert level, requires AZ-104 first, and assumes enterprise scenarios (landing zones, identity governance, migrations). SAA-C03 is associate level with no prerequisite, and its scenarios cover a single workload or a few accounts.
- **SAA-C03 compared with SAP-C02 and SAP-C03 (Solutions Architect – Professional).** The Professional exams use the same design style at multi-account, hybrid, migration and organisation scale, with long, dense scenarios. SAP-C03 (from November 17, 2026) adds GenAI and agentic architecture, resilience engineering and post-quantum cryptography. SAA-C03 is the foundation for both.
- **SAA-C03 compared with SOA-C03 and DVA-C03.** These are the same associate tier with different verbs. SOA asks you to operate and troubleshoot (CloudWatch, Systems Manager, CloudFormation), and DVA asks you to build and deploy code (SDKs, Lambda, CI/CD). SAA asks you to choose and combine services. Many service names overlap, so studying one makes the others cheaper.
- **SAA-C03 compared with CLF-C02.** CLF asks what a service is. SAA asks which combination of services best meets five constraints at once.

## Exam-day notes

- You have 65 questions in 130 minutes, which is two minutes each. Read the **last sentence first** (the actual question and its qualifier), then the scenario, underlining the constraints in your head (RPO and RTO, "no code changes", "cost", "least overhead", "serverless").
- Eliminate first. Two of the four options are usually clearly wrong: the service cannot do the job, or the answer adds needless infrastructure. Decide between the remaining two using the qualifier.
- Traps: S3 Glacier retrieval times compared with "immediate access"; S3 One Zone-IA for data that must survive an AZ loss; a single NAT gateway in a "highly available" design; Multi-AZ RDS used to scale reads (Multi-AZ is for failover, read replicas are for read scaling); Spot Instances for work that cannot be interrupted; "encrypt with keys the company controls" (that means KMS customer managed keys or CloudHSM, not SSE-S3).
- Flag long questions on the first pass and leave at least 15 minutes for review. Don't change an answer on review unless you can name the constraint you misread.
