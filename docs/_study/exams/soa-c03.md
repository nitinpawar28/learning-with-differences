---
code: SOA-C03
title: "AWS Certified CloudOps Engineer – Associate"
credential: "AWS Certified CloudOps Engineer – Associate"
provider: aws
tracks: [cloud]
clouds: [aws]
level: associate
tier: elective
stage: "2"
progress: planned
official_url: https://aws.amazon.com/certification/certified-cloudops-engineer-associate/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html
outline_version: "1.1 (2026-06-01)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends 1 year of experience with deployment, management, troubleshooting, networking and security on AWS, plus at least 1 year in a related operations role such as system administrator."
replaces: ""
replaced_by: ""
counterparts: [az-104]
objectives:
  - { id: "1", title: "Monitoring, Logging, Analysis, Remediation, and Performance Optimization", weight: "22%" }
  - { id: "1.1", title: "Implement metrics, alarms, and filters by using AWS monitoring and logging services" }
  - { id: "1.1.1", title: "Skill: Use AWS services (for example, Amazon CloudWatch, AWS CloudTrail, Amazon Managed Service for Prometheus) to configure monitoring and logging for workloads (for example, serverless, compute, AI)" }
  - { id: "1.1.2", title: "Skill: Configure and manage the CloudWatch agent to collect metrics and logs from EC2 instances, Amazon ECS clusters, or Amazon EKS clusters" }
  - { id: "1.1.3", title: "Skill: Configure, identify, and troubleshoot CloudWatch alarms that can invoke AWS services directly or through Amazon EventBridge (for example, by creating composite alarms and identifying their invokable actions)" }
  - { id: "1.1.4", title: "Skill: Create, implement, and manage customizable and shareable CloudWatch dashboards that display metrics and alarms for AWS resources across multiple accounts and AWS Regions" }
  - { id: "1.1.5", title: "Skill: Configure AWS services to send notifications to Amazon SNS and to invoke alarms that send notifications to Amazon SNS" }
  - { id: "1.2", title: "Identify and remediate issues by using monitoring and availability metrics" }
  - { id: "1.2.1", title: "Skill: Analyze performance metrics and automate remediation strategies by using AWS services and functionality (for example, CloudWatch, Lambda, AWS Systems Manager, CloudTrail, Kiro, AWS DevOps Agent)" }
  - { id: "1.2.2", title: "Skill: Use EventBridge to route, enrich, and deliver events, and troubleshoot any issues with event bus rules" }
  - { id: "1.2.3", title: "Skill: Create or run custom and predefined Systems Manager Automation runbooks (for example, by using AWS SDKs or custom scripts) to automate tasks and streamline processes on AWS" }
  - { id: "1.3", title: "Implement performance optimization strategies for compute, storage, and database resources" }
  - { id: "1.3.1", title: "Skill: Optimize compute resources and remediate performance problems by using performance metrics, resource tags, and AWS tools" }
  - { id: "1.3.2", title: "Skill: Analyze Amazon EBS performance metrics, troubleshoot issues, and optimize volume types to improve performance and reduce cost" }
  - { id: "1.3.3", title: "Skill: Implement and optimize S3 performance strategies (for example, AWS DataSync, S3 Transfer Acceleration, multipart uploads, S3 Lifecycle policies) to enhance data transfer, storage efficiency, and access patterns" }
  - { id: "1.3.4", title: "Skill: Evaluate and select shared storage solutions (for example, Amazon EFS, Amazon FSx, Amazon S3 Files), and optimize the solutions (for example, EFS lifecycle policies) for specific use cases and requirements" }
  - { id: "1.3.5", title: "Skill: Monitor Amazon RDS metrics (for example, Amazon RDS Performance Insights, CloudWatch alarms) and modify configurations to increase performance efficiency (for example, Performance Insights proactive recommendations, RDS Proxy)" }
  - { id: "1.3.6", title: "Skill: Implement, monitor, and optimize EC2 instances and their associated storage and networking capabilities (for example, EC2 placement groups)" }
  - { id: "2", title: "Reliability and Business Continuity", weight: "22%" }
  - { id: "2.1", title: "Implement scalability and elasticity" }
  - { id: "2.1.1", title: "Skill: Configure and manage scaling mechanisms in compute environments" }
  - { id: "2.1.2", title: "Skill: Implement caching by using AWS services to enhance dynamic scalability (for example, Amazon CloudFront, Amazon ElastiCache)" }
  - { id: "2.1.3", title: "Skill: Configure and manage scaling in AWS managed databases (for example, Amazon RDS, DynamoDB)" }
  - { id: "2.2", title: "Implement highly available and resilient environments" }
  - { id: "2.2.1", title: "Skill: Configure and troubleshoot Elastic Load Balancing (ELB) and Amazon Route 53 health checks" }
  - { id: "2.2.2", title: "Skill: Configure fault-tolerant systems (for example, Multi-AZ deployments)" }
  - { id: "2.3", title: "Implement backup and restore strategies" }
  - { id: "2.3.1", title: "Skill: Automate snapshots and backups for AWS resources (for example, EC2 instances, RDS DB instances, EBS volumes, S3 buckets, DynamoDB tables) by using AWS services (for example, AWS Backup)" }
  - { id: "2.3.2", title: "Skill: Use various methods to restore databases (for example, point-in-time restore) to meet recovery time objective (RTO), recovery point objective (RPO), and cost requirements" }
  - { id: "2.3.3", title: "Skill: Implement versioning for storage services (for example, Amazon S3, Amazon FSx)" }
  - { id: "2.3.4", title: "Skill: Follow disaster recovery procedures and best practices (for example, backup and restore, pilot light, warm standby, active/active)" }
  - { id: "3", title: "Deployment, Provisioning, and Automation", weight: "22%" }
  - { id: "3.1", title: "Provision and maintain cloud resources" }
  - { id: "3.1.1", title: "Skill: Create and manage AMIs and container images (for example, EC2 Image Builder)" }
  - { id: "3.1.2", title: "Skill: Create and manage AWS resources by using CloudFormation and the AWS CDK" }
  - { id: "3.1.3", title: "Skill: Identify and remediate deployment issues (for example, subnet sizing issues, CloudFormation errors, permissions issues)" }
  - { id: "3.1.4", title: "Skill: Provision and share resources across multiple Regions and accounts (for example, AWS Resource Access Manager [AWS RAM], CloudFormation StackSets)" }
  - { id: "3.1.5", title: "Skill: Implement deployment strategies and services" }
  - { id: "3.1.6", title: "Skill: Use and manage third-party tools to automate resource deployment (for example, Terraform, Git)" }
  - { id: "3.2", title: "Automate the management of existing resources" }
  - { id: "3.2.1", title: "Skill: Use AWS services to automate operational processes (for example, Systems Manager)" }
  - { id: "3.2.2", title: "Skill: Implement event-driven automation by using AWS services and features (for example, Lambda, S3 Event Notifications, EventBridge, AWS DevOps Agent)" }
  - { id: "4", title: "Security and Compliance", weight: "16%" }
  - { id: "4.1", title: "Implement and manage security and compliance tools and policies" }
  - { id: "4.1.1", title: "Skill: Implement IAM features (for example, password policies, multi-factor authentication [MFA], roles, federated identity, resource policies, policy conditions)" }
  - { id: "4.1.2", title: "Skill: Troubleshoot and audit access issues by using AWS tools (for example, CloudTrail, IAM Access Analyzer, IAM policy simulator)" }
  - { id: "4.1.3", title: "Skill: Implement multi-account strategies securely (for example, AWS Organizations, service control policies, IAM Identity Center)" }
  - { id: "4.1.4", title: "Skill: Implement remediation based on the results of AWS Trusted Advisor security checks" }
  - { id: "4.1.5", title: "Skill: Enforce compliance requirements and continuous monitoring (for example, Region and service selections, AWS Config conformance packs)" }
  - { id: "4.2", title: "Implement strategies to protect data and infrastructure" }
  - { id: "4.2.1", title: "Skill: Implement and enforce a data classification scheme" }
  - { id: "4.2.2", title: "Skill: Implement, configure, and troubleshoot encryption at rest (for example, AWS KMS)" }
  - { id: "4.2.3", title: "Skill: Implement, configure, and troubleshoot encryption in transit (for example, AWS Certificate Manager [ACM])" }
  - { id: "4.2.4", title: "Skill: Securely store secrets by using AWS services" }
  - { id: "4.2.5", title: "Skill: Configure reports and remediate findings from AWS services (for example, AWS Security Hub, Amazon GuardDuty, AWS Config, Amazon Inspector, AWS Security Agent)" }
  - { id: "5", title: "Networking and Content Delivery", weight: "18%" }
  - { id: "5.1", title: "Implement and optimize networking features and connectivity" }
  - { id: "5.1.1", title: "Skill: Configure a VPC (for example, subnets, route tables, network ACLs, security groups, NAT gateways, internet gateway, egress-only internet gateway)" }
  - { id: "5.1.2", title: "Skill: Configure private networking connectivity (for example, VPC endpoints, AWS PrivateLink, VPC peering)" }
  - { id: "5.1.3", title: "Skill: Audit AWS network protection services (for example, Route 53 Resolver DNS Firewall, AWS WAF, AWS Shield, AWS Network Firewall) in a single account" }
  - { id: "5.1.4", title: "Skill: Optimize the cost of network architectures" }
  - { id: "5.2", title: "Configure domains, DNS services, and content delivery" }
  - { id: "5.2.1", title: "Skill: Configure DNS (for example, Route 53 Resolver)" }
  - { id: "5.2.2", title: "Skill: Implement Route 53 routing policies, configurations, and query logging" }
  - { id: "5.2.3", title: "Skill: Configure content and service distribution (for example, CloudFront, AWS Global Accelerator)" }
  - { id: "5.3", title: "Troubleshoot network connectivity issues" }
  - { id: "5.3.1", title: "Skill: Troubleshoot VPC configurations (for example, subnets, route tables, network ACLs, security groups, transit gateways, NAT gateways)" }
  - { id: "5.3.2", title: "Skill: Collect and interpret networking logs to troubleshoot issues (for example, VPC flow logs, ELB access logs, AWS WAF web ACL logs, CloudFront logs, container logs)" }
  - { id: "5.3.3", title: "Skill: Identify and remediate CloudFront caching issues" }
  - { id: "5.3.4", title: "Skill: Identify and troubleshoot hybrid connectivity issues and private connectivity issues" }
  - { id: "5.3.5", title: "Skill: Configure and analyze CloudWatch network monitoring services" }
---
## Exam format

Every fact below is as of 2026-10-24 and comes from the [certification page](https://aws.amazon.com/certification/certified-cloudops-engineer-associate/) and the [SOA-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html). Confirm both before you book.

| Item | Detail (as of 2026-10-24) |
| --- | --- |
| Category | Associate |
| Question types | Multiple choice and multiple response only. Each scored question counts as one scored opportunity |
| Number of questions | 65: 50 scored and 15 unscored (the unscored ones are not marked) |
| Duration | 130 minutes |
| Passing score | 720 on a scaled score of 100–1,000. Scoring is compensatory |
| Price | 150 USD (see [exam pricing](https://aws.amazon.com/certification/policies/before-testing/)) |
| Languages | English, Japanese, Korean and Simplified Chinese. The Simplified Chinese and Korean versions will be retired after November 19, 2026 |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | Valid for 3 years. You can recertify by passing the latest version, or automatically by earning DevOps Engineer – Professional (see [recertification](https://aws.amazon.com/certification/recertification/)) |

**Name and code history.** The certification used to be called *AWS Certified SysOps Administrator – Associate*. The new name applies only to people who pass SOA-C03. SOA-C02 was in use until September 29, 2025, and SOA-C03 has been in use since September 30, 2025 ([comparison page](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03-comparison.html)). Existing SysOps holders keep their credential for its full three years. SOA-C02 has no page of its own in this library. The outline transcribed here is **guide version 1.1, published June 1, 2026** (v1.0 was published September 30, 2025). The [revisions page](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/soa-03-revisions.html) shows that v1.1 added monitoring for AI workloads, Kiro, AWS DevOps Agent, AWS Security Agent and Amazon S3 Files to the skill examples.

## What the exam really tests

SOA-C03 tests whether you can **run a workload on AWS day to day**: watch it, fix it, scale it, back it up, automate it, lock it down and keep the network working. The guide puts designing distributed architectures, designing CI/CD pipelines, designing hybrid networking, writing software, defining security requirements, capacity planning, TCO analysis and billing out of scope. The five domains:

- **Monitoring, Logging, Analysis, Remediation, and Performance Optimization (22%)**: CloudWatch metrics, alarms (including composite alarms), dashboards across accounts and Regions, and the CloudWatch agent on EC2, ECS and EKS; CloudTrail; Amazon Managed Service for Prometheus; EventBridge rules and troubleshooting them; Systems Manager Automation runbooks; and **performance tuning**, which was its own SOA-C02 domain and is now folded in here: EC2 sizing and placement groups, EBS volume types, S3 performance (multipart upload, Transfer Acceleration, DataSync), EFS, FSx and S3 Files, RDS Performance Insights and RDS Proxy.
- **Reliability and Business Continuity (22%)**: Auto Scaling, caching with CloudFront and ElastiCache, database scaling, ELB and Route 53 health checks, Multi-AZ, AWS Backup, point-in-time restore against RTO and RPO, versioning, and the four DR strategies.
- **Deployment, Provisioning, and Automation (22%)**: AMIs and EC2 Image Builder, CloudFormation and the CDK, fixing failed deployments (subnet sizing, stack errors, permissions), StackSets and AWS RAM across accounts, deployment strategies, Terraform and Git, and event-driven automation (Lambda, S3 Event Notifications, EventBridge, AWS DevOps Agent).
- **Security and Compliance (16%)**: IAM features and troubleshooting access (Access Analyzer, policy simulator, CloudTrail), Organizations, SCPs and IAM Identity Center, Trusted Advisor checks, Config conformance packs, data classification, KMS, ACM, secrets, and remediating findings from Security Hub, GuardDuty, Config, Inspector and AWS Security Agent.
- **Networking and Content Delivery (18%)**: building a VPC (subnets, route tables, network ACLs, security groups, NAT and internet gateways, egress-only internet gateways), VPC endpoints, PrivateLink and peering, auditing Route 53 Resolver DNS Firewall, WAF, Shield and Network Firewall, Route 53 routing policies and query logging, CloudFront and Global Accelerator, and **troubleshooting** with VPC Flow Logs, ELB, WAF and CloudFront logs, transit gateways, hybrid connectivity and CloudWatch network monitoring.

Questions are operational scenarios: "an alarm did not fire", "instances cannot reach S3", "the stack rolled back", "the team needs to be notified when…". The guide lists only multiple-choice and multiple-response questions. Candidates lose points on **exact behaviour**: which CloudWatch metrics need the agent (memory and disk space do, CPU does not); alarm states and how missing data is treated; stateless network ACLs needing ephemeral return ports; route-table precedence; CloudFormation rollback compared with drift detection compared with deletion policies; and Systems Manager feature boundaries (Run Command compared with Automation compared with Patch Manager compared with Session Manager compared with State Manager).

## Study strategy

1. **Foundations first: networking and IAM**, as for SAA-C03. Then CloudWatch and Systems Manager in depth, because they appear in almost every domain.
2. **Hands-on work matters more here than on any other AWS associate exam.** Install the CloudWatch agent with a Systems Manager parameter-store config and push memory metrics; build a composite alarm that triggers an SSM Automation runbook through EventBridge; break a VPC on purpose (remove a route, tighten a network ACL) and diagnose it with Flow Logs and Reachability Analyzer; deploy the same stack to two accounts with StackSets; set up AWS Backup with a cross-Region copy and restore RDS to a point in time; add a CloudFront distribution and invalidate its cache.
3. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (the Official Practice Question Set, the Official Pretest, exam-prep courses, AWS Builder Labs, AWS Cloud Quest, AWS Jam, AWS SimuLearn and the Official Practice Exam); the [exam guide](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html) with its in-scope and out-of-scope service lists; the Systems Manager and CloudWatch user guides for the exact behaviour of each feature.
4. **How your background helps or misleads.** **AZ-104-style knowledge** (even partial, from your Azure work) gives you the operator mindset. The mappings are Azure Monitor to CloudWatch, Activity Log to CloudTrail, Azure Automation and Update Manager to Systems Manager, Recovery Services vaults to AWS Backup, and ARM or Bicep to CloudFormation. The traps are stateless network ACLs (Azure NSGs are stateful), CloudWatch's lack of default memory metrics (the Azure Monitor agent collects guest metrics more transparently), and Route 53 routing policies, which combine what Traffic Manager and Azure DNS do separately. **CKAD** helps with EKS and ECS log and metric collection. **.NET** helps little here, except with Windows instances and SSM documents written in PowerShell.

SOA-C03 is an elective at stage 2. Take it after SAA-C03. Much of the service knowledge carries over, so most of the work is learning operational depth.

## Differences from related exams

- **SOA-C03 compared with AZ-104 (the closest Azure counterpart).** Both are administrator and operator exams at associate level, and this is the best style match across the two clouds. AZ-104 spends more time on identity governance (Entra users and groups, RBAC scopes, Azure Policy, locks) and on configuring individual resources step by step. SOA-C03 spends more time on **observability, automated remediation and troubleshooting**, with CloudWatch, EventBridge and Systems Manager runbooks at its centre and a whole troubleshooting task for networking. Neither exam asks for design work at the depth of AZ-305 or SAA-C03.
- **SOA-C03 compared with SAA-C03.** They cover the same services with a different verb. SAA asks which architecture to choose. SOA asks how to keep it running and how to fix it once it is built. SOA expects you to know specific metrics, log sources and CLI or console behaviour, while SAA rarely does.
- **SOA-C03 compared with SOA-C02 (its predecessor).** SOA-C02 had six domains, and its Cost and Performance Optimization domain (12%) has been folded into Domain 1. SOA-C03 adds the CloudWatch agent for containers, CloudFormation and CDK stack management, enforcing Region and service compliance and CloudWatch network monitoring, and drops S3 static website hosting. Domains 2 and 3 grow from 16% and 18% to 22% each.
- **SOA-C03 compared with DVA-C03.** DVA instruments application code (X-Ray SDK, structured logs, Embedded Metric Format). SOA instruments infrastructure (CloudWatch agent, Flow Logs, Config).
- **SOA-C03 compared with DOP-C02 (DevOps Engineer – Professional).** DOP designs the automation, multi-account pipelines and incident response that SOA carries out. Passing DOP recertifies SOA.

## Exam-day notes

- You have 65 questions in 130 minutes. The troubleshooting questions are long, so read the symptom and the **last sentence** first, then scan the scenario for the configuration detail that explains it.
- Look for the automated, least-effort fix: "use a Systems Manager Automation runbook", "add an EventBridge rule", "enable AWS Backup", rather than "write a script on a cron job".
- Traps: memory-based scaling without the CloudWatch agent; a network ACL that allows inbound traffic but not the ephemeral outbound return range; a VPC endpoint whose policy or route table association is missing; CloudFront serving stale content (invalidate the cache or version the object names); KMS key policies that block cross-account access even when IAM allows it; SCPs, which never grant permissions and only limit them.
- Multi-account items (StackSets, AWS RAM, Organizations) usually have one answer that works in a single account but not across the organisation. Rule it out first.
