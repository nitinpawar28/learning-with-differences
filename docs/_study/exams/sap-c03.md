---
code: SAP-C03
title: "AWS Certified Solutions Architect – Professional"
credential: "AWS Certified Solutions Architect – Professional"
provider: aws
tracks: [architect, cloud]
clouds: [aws]
level: professional
tier: core
stage: "5"
progress: planned
official_url: https://aws.amazon.com/certification/certified-solutions-architect-professional/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html
outline_version: "SAP-C02 guide (no version printed), retrieved 2026-10-24"
last_verified: 2026-10-24
retires_on:
provisional: true
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends 2 or more years of experience using AWS services to design and implement cloud solutions."
replaces: "sap-c02"
replaced_by: ""
counterparts: [az-305]
objectives:
  - { id: "1", title: "Design Solutions for Organizational Complexity", weight: "26%" }
  - { id: "1.1", title: "Architect network connectivity strategies" }
  - { id: "1.1.1", title: "Knowledge: AWS Global Infrastructure" }
  - { id: "1.1.2", title: "Knowledge: AWS networking concepts (e.g. Amazon Virtual Private Cloud (Amazon VPC), AWS Direct Connect, AWS VPN, transitive routing, AWS container services)" }
  - { id: "1.1.3", title: "Knowledge: Hybrid DNS concepts (e.g. Amazon Route 53 Resolver, on-premises DNS integration)" }
  - { id: "1.1.4", title: "Knowledge: Network segmentation (e.g. subnetting, IP addressing, connectivity among VPCs)" }
  - { id: "1.1.5", title: "Knowledge: Network traffic monitoring" }
  - { id: "1.1.6", title: "Skill: Evaluating connectivity options for multiple VPCs" }
  - { id: "1.1.7", title: "Skill: Evaluating connectivity options for on-premises, co-location, and cloud integration" }
  - { id: "1.1.8", title: "Skill: Selecting AWS Regions and Availability Zones based on network and latency requirements" }
  - { id: "1.1.9", title: "Skill: Troubleshooting traffic flows by using AWS tools" }
  - { id: "1.1.10", title: "Skill: Using service endpoints for service integrations" }
  - { id: "1.2", title: "Prescribe security controls" }
  - { id: "1.2.1", title: "Knowledge: AWS Identity and Access Management (IAM) and AWS IAM Identity Center" }
  - { id: "1.2.2", title: "Knowledge: Route tables, security groups, and network ACLs" }
  - { id: "1.2.3", title: "Knowledge: Encryption keys and certificate management (e.g. AWS Key Management Service (AWS KMS), AWS Certificate Manager (ACM))" }
  - { id: "1.2.4", title: "Knowledge: AWS security, identity, and compliance tools (e.g. AWS CloudTrail, AWS Identity and Access Management Access Analyzer, AWS Security Hub, Amazon Inspector)" }
  - { id: "1.2.5", title: "Skill: Evaluating cross-account access management" }
  - { id: "1.2.6", title: "Skill: Integrating with third-party identity providers" }
  - { id: "1.2.7", title: "Skill: Deploying encryption strategies for data at rest and data in transit" }
  - { id: "1.2.8", title: "Skill: Developing a strategy for centralized security event notifications and auditing" }
  - { id: "1.3", title: "Design reliable and resilient architectures" }
  - { id: "1.3.1", title: "Knowledge: Recovery time objectives (RTOs) and recovery point objectives (RPOs)" }
  - { id: "1.3.2", title: "Knowledge: Disaster recovery strategies (e.g. using AWS Elastic Disaster Recovery, pilot light, warm standby, and multi-site)" }
  - { id: "1.3.3", title: "Knowledge: Data backup and restoration" }
  - { id: "1.3.4", title: "Skill: Designing disaster recovery solutions based on RTO and RPO requirements" }
  - { id: "1.3.5", title: "Skill: Implementing architectures to automatically recover from failure" }
  - { id: "1.3.6", title: "Skill: Developing the optimal architecture by considering scale-up and scale-out options" }
  - { id: "1.3.7", title: "Skill: Designing an effective backup and restoration strategy" }
  - { id: "1.4", title: "Design a multi-account AWS environment" }
  - { id: "1.4.1", title: "Knowledge: AWS Organizations and AWS Control Tower" }
  - { id: "1.4.2", title: "Knowledge: Multi-account event notifications" }
  - { id: "1.4.3", title: "Knowledge: AWS resource sharing across environments" }
  - { id: "1.4.4", title: "Skill: Evaluating the most appropriate account structure for organizational requirements" }
  - { id: "1.4.5", title: "Skill: Recommending a strategy for central logging and event notifications" }
  - { id: "1.4.6", title: "Skill: Developing a multi-account governance model" }
  - { id: "1.5", title: "Determine cost optimization and visibility strategies" }
  - { id: "1.5.1", title: "Knowledge: AWS cost and usage monitoring tools (e.g. AWS Trusted Advisor, AWS Pricing Calculator, AWS Cost Explorer, AWS Budgets)" }
  - { id: "1.5.2", title: "Knowledge: AWS purchasing options (e.g. Reserved Instances, Savings Plans, Spot Instances)" }
  - { id: "1.5.3", title: "Knowledge: AWS rightsizing visibility tools (e.g. AWS Compute Optimizer, Amazon Simple Storage Service (Amazon S3) Storage Lens)" }
  - { id: "1.5.4", title: "Skill: Monitoring cost and usage with AWS tools" }
  - { id: "1.5.5", title: "Skill: Developing an effective tagging strategy that maps costs to business units" }
  - { id: "1.5.6", title: "Skill: Understanding how purchasing options affect cost and performance" }
  - { id: "2", title: "Design for New Solutions", weight: "29%" }
  - { id: "2.1", title: "Design a deployment strategy to meet business requirements" }
  - { id: "2.1.1", title: "Knowledge: Infrastructure as code (IaC) (e.g. AWS CloudFormation)" }
  - { id: "2.1.2", title: "Knowledge: Continuous integration and continuous delivery (CI/CD)" }
  - { id: "2.1.3", title: "Knowledge: Change management processes" }
  - { id: "2.1.4", title: "Knowledge: Configuration management tools (e.g. AWS Systems Manager)" }
  - { id: "2.1.5", title: "Skill: Determining an application or upgrade path for new services and features" }
  - { id: "2.1.6", title: "Skill: Selecting services to develop deployment strategies and implement appropriate rollback mechanisms" }
  - { id: "2.1.7", title: "Skill: Adopting managed services as needed to reduce infrastructure provisioning and patching overhead" }
  - { id: "2.1.8", title: "Skill: Making advanced technologies accessible by delegating complex development and deployment tasks to AWS" }
  - { id: "2.2", title: "Design a solution to ensure business continuity" }
  - { id: "2.2.1", title: "Knowledge: AWS Global Infrastructure" }
  - { id: "2.2.2", title: "Knowledge: AWS networking concepts (e.g. Amazon Route 53, routing methods)" }
  - { id: "2.2.3", title: "Knowledge: RTOs and RPOs" }
  - { id: "2.2.4", title: "Knowledge: Disaster recovery scenarios (e.g. backup and restore, pilot light, warm standby, multi-site)" }
  - { id: "2.2.5", title: "Knowledge: Disaster recovery solutions on AWS" }
  - { id: "2.2.6", title: "Skill: Configuring disaster recovery solutions" }
  - { id: "2.2.7", title: "Skill: Configuring data and database replication" }
  - { id: "2.2.8", title: "Skill: Performing disaster recovery testing" }
  - { id: "2.2.9", title: "Skill: Architecting a backup solution that is automated, is cost-effective, and supports business continuity across multiple Availability Zones or AWS Regions" }
  - { id: "2.2.10", title: "Skill: Designing an architecture that provides application and infrastructure availability in the event of a disruption" }
  - { id: "2.2.11", title: "Skill: Using processes and components for centralized monitoring to proactively recover from system failures" }
  - { id: "2.3", title: "Determine security controls based on requirements" }
  - { id: "2.3.1", title: "Knowledge: IAM" }
  - { id: "2.3.2", title: "Knowledge: Route tables, security groups, and network ACLs" }
  - { id: "2.3.3", title: "Knowledge: Encryption options for data at rest and data in transit" }
  - { id: "2.3.4", title: "Knowledge: AWS service endpoints" }
  - { id: "2.3.5", title: "Knowledge: Credential management services" }
  - { id: "2.3.6", title: "Knowledge: AWS managed security services (e.g. AWS Shield, AWS WAF, Amazon GuardDuty, AWS Security Hub)" }
  - { id: "2.3.7", title: "Skill: Specifying IAM users and IAM roles that adhere to the principle of least privilege access" }
  - { id: "2.3.8", title: "Skill: Specifying inbound and outbound network flows by using security group rules and network ACL rules" }
  - { id: "2.3.9", title: "Skill: Developing attack mitigation strategies for large-scale web applications" }
  - { id: "2.3.10", title: "Skill: Developing encryption strategies for data at rest and data in transit" }
  - { id: "2.3.11", title: "Skill: Specifying service endpoints for service integrations" }
  - { id: "2.3.12", title: "Skill: Developing strategies for patch management to remain compliant with organizational standards" }
  - { id: "2.4", title: "Design a strategy to meet reliability requirements" }
  - { id: "2.4.1", title: "Knowledge: AWS Global Infrastructure" }
  - { id: "2.4.2", title: "Knowledge: AWS storage services and replication strategies (e.g. Amazon S3, Amazon RDS, Amazon ElastiCache)" }
  - { id: "2.4.3", title: "Knowledge: Multi-AZ and multi-Region architectures" }
  - { id: "2.4.4", title: "Knowledge: Auto scaling policies and events" }
  - { id: "2.4.5", title: "Knowledge: Application integration (e.g. Amazon SNS, Amazon SQS, AWS Step Functions)" }
  - { id: "2.4.6", title: "Knowledge: Service quotas and limits" }
  - { id: "2.4.7", title: "Skill: Designing highly available application environments based on business requirements" }
  - { id: "2.4.8", title: "Skill: Using advanced techniques to design for failure and ensure seamless system recoverability" }
  - { id: "2.4.9", title: "Skill: Implementing loosely coupled dependencies" }
  - { id: "2.4.10", title: "Skill: Operating and maintaining high-availability architectures (e.g. application failovers, database failovers)" }
  - { id: "2.4.11", title: "Skill: Using AWS managed services for high availability" }
  - { id: "2.4.12", title: "Skill: Implementing DNS routing policies (e.g. Route 53 latency-based routing, geolocation routing, simple routing)" }
  - { id: "2.5", title: "Design a solution to meet performance objectives" }
  - { id: "2.5.1", title: "Knowledge: Performance monitoring technologies" }
  - { id: "2.5.2", title: "Knowledge: Storage options on AWS" }
  - { id: "2.5.3", title: "Knowledge: Instance families and use cases" }
  - { id: "2.5.4", title: "Knowledge: Purpose-built databases" }
  - { id: "2.5.5", title: "Skill: Designing large-scale application architectures for a variety of access patterns" }
  - { id: "2.5.6", title: "Skill: Designing an elastic architecture based on business objectives" }
  - { id: "2.5.7", title: "Skill: Applying design patterns to meet performance objectives with caching, buffering, and replicas" }
  - { id: "2.5.8", title: "Skill: Developing a process methodology for selecting purpose-built services for required tasks" }
  - { id: "2.5.9", title: "Skill: Designing a rightsizing strategy" }
  - { id: "2.6", title: "Determine a cost optimization strategy to meet solution goals and objectives" }
  - { id: "2.6.1", title: "Knowledge: AWS cost and usage monitoring tools (e.g. AWS Cost Explorer, AWS Trusted Advisor, AWS Pricing Calculator)" }
  - { id: "2.6.2", title: "Knowledge: Pricing models (e.g. Reserved Instances, AWS Savings Plans)" }
  - { id: "2.6.3", title: "Knowledge: Storage tiering" }
  - { id: "2.6.4", title: "Knowledge: Data transfer costs" }
  - { id: "2.6.5", title: "Knowledge: AWS managed service offerings" }
  - { id: "2.6.6", title: "Skill: Identifying opportunities to select and rightsize infrastructure for cost-effective resources" }
  - { id: "2.6.7", title: "Skill: Identifying appropriate pricing models" }
  - { id: "2.6.8", title: "Skill: Performing data transfer modeling and selecting services to reduce data transfer costs" }
  - { id: "2.6.9", title: "Skill: Developing a strategy and implementing controls for expenditure and usage awareness" }
  - { id: "3", title: "Continuous Improvement for Existing Solutions", weight: "25%" }
  - { id: "3.1", title: "Determine a strategy to improve overall operational excellence" }
  - { id: "3.1.1", title: "Knowledge: Alerting and automatic remediation strategies" }
  - { id: "3.1.2", title: "Knowledge: Disaster recovery planning" }
  - { id: "3.1.3", title: "Knowledge: Monitoring and logging solutions (e.g. Amazon CloudWatch)" }
  - { id: "3.1.4", title: "Knowledge: CI/CD pipelines and deployment strategies (e.g. blue/green, all-at-once, rolling)" }
  - { id: "3.1.5", title: "Knowledge: Configuration management tools (e.g. AWS Systems Manager)" }
  - { id: "3.1.6", title: "Skill: Determining the most appropriate logging and monitoring strategy" }
  - { id: "3.1.7", title: "Skill: Evaluating current deployment processes for improvement opportunities" }
  - { id: "3.1.8", title: "Skill: Prioritizing opportunities for automation within a solution stack" }
  - { id: "3.1.9", title: "Skill: Recommending the appropriate AWS solution to enable configuration management automation" }
  - { id: "3.1.10", title: "Skill: Engineering failure scenario activities to support and exercise an understanding of recovery actions" }
  - { id: "3.2", title: "Determine a strategy to improve security" }
  - { id: "3.2.1", title: "Knowledge: Data retention, data sensitivity, and data regulatory requirements" }
  - { id: "3.2.2", title: "Knowledge: Automated monitoring and remediation strategies (e.g. AWS Config rules)" }
  - { id: "3.2.3", title: "Knowledge: Secrets management (e.g. Systems Manager, AWS Secrets Manager)" }
  - { id: "3.2.4", title: "Knowledge: Principle of least privilege access" }
  - { id: "3.2.5", title: "Knowledge: Security-specific AWS solutions" }
  - { id: "3.2.6", title: "Knowledge: Patching practices" }
  - { id: "3.2.7", title: "Knowledge: Backup practices and methods" }
  - { id: "3.2.8", title: "Skill: Evaluating a strategy for the secure management of secrets and credentials" }
  - { id: "3.2.9", title: "Skill: Auditing an environment for least privilege access" }
  - { id: "3.2.10", title: "Skill: Reviewing implemented solutions to ensure security at every layer" }
  - { id: "3.2.11", title: "Skill: Reviewing comprehensive traceability of users and services" }
  - { id: "3.2.12", title: "Skill: Prioritizing automated responses to the detection of vulnerabilities" }
  - { id: "3.2.13", title: "Skill: Designing and implementing a patch and update process" }
  - { id: "3.2.14", title: "Skill: Designing and implementing a backup process" }
  - { id: "3.2.15", title: "Skill: Employing remediation techniques" }
  - { id: "3.3", title: "Determine a strategy to improve performance" }
  - { id: "3.3.1", title: "Knowledge: High-performing systems architectures (e.g. auto scaling, instance fleets, placement groups)" }
  - { id: "3.3.2", title: "Knowledge: Global service offerings (e.g. AWS Global Accelerator, Amazon CloudFront, edge computing services)" }
  - { id: "3.3.3", title: "Knowledge: Monitoring tool sets and services (e.g. CloudWatch)" }
  - { id: "3.3.4", title: "Knowledge: Service level agreements (SLAs) and key performance indicators (KPIs)" }
  - { id: "3.3.5", title: "Skill: Translating business requirements to measurable metrics" }
  - { id: "3.3.6", title: "Skill: Testing potential remediation solutions and making recommendations" }
  - { id: "3.3.7", title: "Skill: Proposing opportunities for the adoption of new technologies and managed services" }
  - { id: "3.3.8", title: "Skill: Assessing solutions and applying rightsizing based on requirements" }
  - { id: "3.3.9", title: "Skill: Identifying and examining performance bottlenecks" }
  - { id: "3.4", title: "Determine a strategy to improve reliability" }
  - { id: "3.4.1", title: "Knowledge: AWS Global Infrastructure" }
  - { id: "3.4.2", title: "Knowledge: Data replication methods" }
  - { id: "3.4.3", title: "Knowledge: Scaling methodologies (e.g. load balancing, auto scaling)" }
  - { id: "3.4.4", title: "Knowledge: High availability and resiliency" }
  - { id: "3.4.5", title: "Knowledge: Disaster recovery methods and tools" }
  - { id: "3.4.6", title: "Knowledge: Service quotas and limits" }
  - { id: "3.4.7", title: "Skill: Understanding application growth and usage trends" }
  - { id: "3.4.8", title: "Skill: Evaluating existing architecture to determine areas that are not sufficiently reliable" }
  - { id: "3.4.9", title: "Skill: Remediating single points of failure" }
  - { id: "3.4.10", title: "Skill: Enabling data replication, self-healing, and elastic features and services" }
  - { id: "3.5", title: "Identify opportunities for cost optimizations" }
  - { id: "3.5.1", title: "Knowledge: Cost-conscious architecture choices (e.g. using Spot Instances, scaling policies, and rightsizing resources)" }
  - { id: "3.5.2", title: "Knowledge: Price model adoptions (e.g. Reserved Instances, AWS Savings Plans)" }
  - { id: "3.5.3", title: "Knowledge: Networking and data transfer costs" }
  - { id: "3.5.4", title: "Knowledge: Cost management, alerting, and reporting" }
  - { id: "3.5.5", title: "Skill: Analyzing usage reports to identify underutilized and overutilized resources" }
  - { id: "3.5.6", title: "Skill: Using AWS solutions to identify unused resources" }
  - { id: "3.5.7", title: "Skill: Designing billing alarms based on expected usage patterns" }
  - { id: "3.5.8", title: "Skill: Investigating AWS Cost and Usage Reports at a granular level" }
  - { id: "3.5.9", title: "Skill: Using tagging for cost allocation and reporting" }
  - { id: "4", title: "Accelerate Workload Migration and Modernization", weight: "20%" }
  - { id: "4.1", title: "Select existing workloads and processes for potential migration" }
  - { id: "4.1.1", title: "Knowledge: Migration assessment and tracking tools (e.g. AWS Migration Hub)" }
  - { id: "4.1.2", title: "Knowledge: Portfolio assessment" }
  - { id: "4.1.3", title: "Knowledge: Asset planning" }
  - { id: "4.1.4", title: "Knowledge: Prioritization and migration of workloads (e.g. wave planning)" }
  - { id: "4.1.5", title: "Skill: Completing an application migration assessment" }
  - { id: "4.1.6", title: "Skill: Evaluating applications according to the seven common migration strategies (7Rs)" }
  - { id: "4.1.7", title: "Skill: Evaluating total cost of ownership (TCO)" }
  - { id: "4.2", title: "Determine the optimal migration approach for existing workloads" }
  - { id: "4.2.1", title: "Knowledge: Data migration options and tools (e.g. AWS DataSync, AWS Transfer Family, AWS Snow Family, Amazon S3 Transfer Acceleration)" }
  - { id: "4.2.2", title: "Knowledge: Application migration tools (e.g. AWS Application Discovery Service, AWS Application Migration Service)" }
  - { id: "4.2.3", title: "Knowledge: AWS networking services and DNS (e.g. AWS Direct Connect, AWS Site-to-Site VPN, Amazon Route 53)" }
  - { id: "4.2.4", title: "Knowledge: Identity services (e.g. AWS IAM Identity Center, AWS Directory Service)" }
  - { id: "4.2.5", title: "Knowledge: Database migration tools (e.g. AWS DMS, AWS SCT)" }
  - { id: "4.2.6", title: "Knowledge: Governance tools (e.g. AWS Control Tower, AWS Organizations)" }
  - { id: "4.2.7", title: "Skill: Selecting the appropriate database transfer mechanism" }
  - { id: "4.2.8", title: "Skill: Selecting the appropriate application transfer mechanism" }
  - { id: "4.2.9", title: "Skill: Selecting the appropriate data transfer service and migration strategy" }
  - { id: "4.2.10", title: "Skill: Applying the appropriate security methods to migration tools" }
  - { id: "4.2.11", title: "Skill: Selecting the appropriate governance model" }
  - { id: "4.3", title: "Determine a new architecture for existing workloads" }
  - { id: "4.3.1", title: "Knowledge: Compute services (e.g. Amazon EC2, AWS Elastic Beanstalk)" }
  - { id: "4.3.2", title: "Knowledge: Containers (e.g. Amazon ECS, Amazon EKS, AWS Fargate, Amazon ECR)" }
  - { id: "4.3.3", title: "Knowledge: AWS storage services (e.g. Amazon EBS, Amazon EFS, Amazon FSx, Amazon S3, AWS Storage Gateway Volume Gateway)" }
  - { id: "4.3.4", title: "Knowledge: Databases (e.g. Amazon DynamoDB, Amazon OpenSearch Service, Amazon RDS, self-managed databases on Amazon EC2)" }
  - { id: "4.3.5", title: "Skill: Selecting the appropriate compute platform" }
  - { id: "4.3.6", title: "Skill: Selecting the appropriate container hosting platform" }
  - { id: "4.3.7", title: "Skill: Selecting the appropriate storage service" }
  - { id: "4.3.8", title: "Skill: Selecting the appropriate database platform" }
  - { id: "4.4", title: "Determine opportunities for modernization and enhancements" }
  - { id: "4.4.1", title: "Knowledge: Serverless compute offerings (e.g. AWS Lambda)" }
  - { id: "4.4.2", title: "Knowledge: Containers (e.g. Amazon ECS, Amazon EKS, Fargate)" }
  - { id: "4.4.3", title: "Knowledge: AWS storage services (e.g. Amazon S3, Amazon EFS)" }
  - { id: "4.4.4", title: "Knowledge: Purpose-built databases (e.g. DynamoDB, Amazon Aurora Serverless, Amazon ElastiCache)" }
  - { id: "4.4.5", title: "Knowledge: Integration services (e.g. Amazon SQS, Amazon SNS, Amazon EventBridge, AWS Step Functions)" }
  - { id: "4.4.6", title: "Skill: Identifying opportunities to decouple application components" }
  - { id: "4.4.7", title: "Skill: Identifying opportunities for serverless solutions" }
  - { id: "4.4.8", title: "Skill: Selecting the appropriate service for containers" }
  - { id: "4.4.9", title: "Skill: Identifying opportunities for purpose-built databases" }
  - { id: "4.4.10", title: "Skill: Selecting the appropriate application integration service" }
---
## Exam format

**Provisional outline.** AWS is replacing SAP-C02 with SAP-C03. As of 2026-10-24 the [certification page](https://aws.amazon.com/certification/certified-solutions-architect-professional/) says registration for SAP-C03 opens on October 27, 2026, and that the last day to sit SAP-C02 is November 16, 2026. The page does not yet give the date of the first SAP-C03 sitting. AWS has not yet published the SAP-C03 exam guide, so the objectives on this page come from the [SAP-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html). Re-transcribe them when the C03 guide appears. Expect the four-domain shape to survive and the service examples, weightings and emerging topics to move.

All facts are as of 2026-10-24, taken from the [certification page](https://aws.amazon.com/certification/certified-solutions-architect-professional/) and the SAP-C02 exam guide. AWS says it will post SAP-C03 details on October 27, 2026, so any of them can change for C03. Confirm on the official page before you book.

| Item | SAP-C02 (current, as of 2026-10-24) |
|---|---|
| Question types | Multiple choice (one correct answer out of four) and multiple response (two or more correct answers out of five or more; you must pick all of them to get credit) |
| Number of questions | 75 in total: 65 scored and 10 unscored pretest questions, which you cannot tell apart |
| Duration | 180 minutes |
| Passing score | 750 on a scaled score of 100–1,000. Scoring is compensatory, so you only need to pass overall, not every domain |
| Price | 300 USD. AWS's exam pricing page has further cost information, including foreign exchange rates. Once you earn one AWS certification, AWS gives you a 50% discount on your next AWS certification exam |
| Languages | English, Japanese, Korean, Portuguese (Brazil), Simplified Chinese, Spanish (Latin America) |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | 3 years. You renew by passing the latest version of the exam again |
| Prerequisites | None required. AWS recommends 2 or more years of experience designing and implementing cloud solutions on AWS |

Unanswered questions are marked wrong and there is no penalty for guessing, so answer every question. The C02 guide also lists **emerging topics** that may appear only as unscored pretest items: content filtering and compliance controls for generative AI (Amazon Bedrock Guardrails), access control for agentic applications (AgentCore Identity), and human-approval workflows for AI operations (AWS Step Functions). AWS says it uses these pretest questions to evaluate new content, so treat the three topics as a hint of where SAP-C03 may be heading, not as confirmed scored content.

## What the exam really tests

SAP is an exam about judgement under constraints. Almost every question is a long scenario: a company with several AWS accounts, an on-premises data centre, a compliance rule, a budget and a deadline. Then come four answers that would all work technically. The skill being scored is picking the one that meets *every* stated constraint with the least operational overhead, cost or risk. Expect to read three or four paragraphs per question and to compare answers that differ by one service or one setting.

The four domains map onto four situations an architect meets:

- **Organizational complexity (26%).** Multi-account landing zones with AWS Organizations and AWS Control Tower, service control policies, cross-account access, centralised logging and security tooling, hybrid networking with AWS Direct Connect, Site-to-Site VPN, Transit Gateway and Route 53 Resolver, disaster recovery against an RTO and RPO, and cost visibility through tagging and purchasing options.
- **New solutions (29%, the largest).** Deployment strategy, business continuity, security controls, reliability, performance and cost for something being built now. Purpose-built databases, caching and buffering patterns, multi-AZ and multi-Region design, and DNS routing policies show up here.
- **Continuous improvement (25%).** An existing workload is too slow, too expensive, too fragile or not secure enough, and you must pick the change that fixes it. Questions often hinge on "with minimal changes to the application".
- **Migration and modernization (20%).** Portfolio assessment, the 7 Rs, wave planning, picking a transfer mechanism (AWS DataSync, AWS Transfer Family, AWS Snow Family, AWS DMS and AWS SCT, AWS Application Migration Service), then re-platforming onto containers, serverless or purpose-built databases.

Where candidates lose points:

- **Missing one constraint.** A phrase such as "the least operational effort", "without exposing traffic to the internet", "within the existing Direct Connect bandwidth" or "a single team must manage..." usually rules out two of the answers. Underline it in your head before you look at the options.
- **Multi-account mechanics.** Which account owns the trail, the delegated administrator, the Transit Gateway or the RAM share; how SCPs interact with IAM policies; what an organization trail captures.
- **DR tiers.** Telling backup-and-restore, pilot light, warm standby and multi-site apart by cost and recovery time, and knowing which services replicate on their own (Aurora Global Database, DynamoDB global tables, S3 Replication) and which need help.
- **Data transfer economics.** Cross-AZ, cross-Region, NAT gateway and internet egress costs, and when a VPC endpoint or CloudFront lowers the bill.
- **Migration tooling confusion.** DataSync versus Transfer Family versus Snowball, and DMS versus SCT versus Application Migration Service, each have a narrow sweet spot.

## Study strategy

1. **Close the AWS associate gap first.** Your AWS knowledge is basic, and SAP assumes associate-level fluency. Work through the SAA-C03 objectives in this library (VPC design, IAM, S3 storage classes, EC2 purchasing, RDS and Aurora, ELB and Auto Scaling) until you can answer associate scenarios quickly. Sitting SAA-C03 first is optional, but it is the cheapest way to prove the foundation and earns you the 50% discount on your next AWS exam.
2. **Multi-account governance and identity.** Set up a free-tier AWS Organization with a few member accounts, enable IAM Identity Center, write an SCP, create an organization trail, delegate Security Hub and GuardDuty to a security account, and share a subnet with AWS RAM. Domain 1 rewards having done this once.
3. **Networking at scale.** Build two or three VPCs joined through a Transit Gateway, add interface and gateway endpoints, and read the Direct Connect resiliency recommendations. You cannot practise Direct Connect hands-on cheaply, so learn its options (private, public and transit VIFs, Direct Connect gateway, SiteLink, MACsec) from the documentation.
4. **Resilience and DR.** Practise RTO and RPO arithmetic and the four DR patterns. Try AWS Elastic Disaster Recovery and AWS Backup cross-Region copies.
5. **Migration and modernization.** Learn the 7 Rs and the migration service family by use case, then the modernization targets: Lambda, ECS and EKS on Fargate, DynamoDB, Aurora Serverless, EventBridge, SQS, SNS and Step Functions.
6. **Cost.** Savings Plans versus Reserved Instances versus Spot, Compute Optimizer, Cost Explorer, Budgets, and Cost and Usage Reports with cost allocation tags.

Official resources named on the certification page (as of 2026-10-24) are the AWS Skill Builder **Exam Prep Plan**, the **AWS Certification Official Practice Question Set**, the **Official Practice Exam**, digital courses, **AWS Builder Labs**, **AWS Cloud Quest**, **AWS Jam**, **AWS SimuLearn**, flashcards and exam-style question walkthroughs. AWS says new SAP-C03 preparation resources arrive with the October 27 update. Read the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) pillars too, because the exam guide grounds the whole exam in it.

How your background helps or misleads:

- **AZ-900 and AZ-204 preparation** give you the cloud vocabulary and the developer view of managed services. The trap is mapping concepts one to one. An Azure subscription is not an AWS account (AWS accounts are the hard security and billing boundary, and you will use dozens), management groups are not organizational units with SCPs, and Azure VNet peering and Virtual WAN do not behave exactly like VPC peering and Transit Gateway. Learn the AWS model on its own terms.
- **CKAD preparation** helps with the container-modernization questions and with EKS. Remember that SAP almost always prefers the managed option (Fargate, ECS) unless the scenario demands Kubernetes.
- **.NET and Angular experience** helps with application-integration and decoupling scenarios. Watch out for over-engineering: the exam usually rewards the managed service over custom code.

## Differences from related exams

- **SAP-C03 vs SAA-C03 (Solutions Architect – Associate).** SAA tests whether you know which service fits a single workload, in a short scenario. SAP tests whether you can design across many accounts, Regions and an on-premises estate, with migration and continuous improvement added, and with much longer scenarios. SAA questions are a paragraph and SAP questions are a page. SAA has no migration domain and almost no Organizations depth.
- **SAP-C03 vs SAP-C02.** SAP-C02 can be taken until November 16, 2026, and SAP-C03 registration opens on October 27, 2026. Until AWS publishes the C03 guide, the safe assumption is the same role and the same four situations. The C02 emerging-topics list (Bedrock Guardrails, AgentCore Identity, Step Functions human approval) is the strongest hint of what moves into scored content. Compare this page with the SAP-C02 entry in this library when the new guide lands.
- **SAP-C03 vs AZ-305 (Azure Solutions Architect Expert).** They are counterparts in role: both are design exams that rarely ask how to click through a console. AZ-305 requires AZ-104 for the credential, and its domains are identity, governance and monitoring, data storage, business continuity and infrastructure. SAP has no prerequisite and a separate migration and modernization domain, and its scenarios are longer and more about trade-offs. AZ-305 can include case studies with several questions on one company. SAP keeps every question self-contained.
- **SAP-C03 vs DOP-C02 (DevOps Engineer – Professional).** DOP is the operator's professional exam (pipelines, IaC, monitoring and incident automation). SAP is the designer's. They overlap on multi-account governance and resilience, and studying them back to back is efficient.
- **SAP-C03 vs SCS-C03 (Security – Specialty).** SAP treats security as one design dimension, such as encryption strategy, least privilege and centralised findings. SCS goes much deeper into detection, incident response and key management.

## Exam-day notes

- **Time budget.** 180 minutes for 75 questions is about 2 minutes 24 seconds each, and long scenarios eat that fast. Aim to reach question 40 by the 90-minute mark and to leave 15 minutes for flagged items.
- **Read the last sentence first.** It holds the actual requirement ("most cost-effective", "least operational overhead", "fastest recovery"). Then read the scenario for constraints, then the answers.
- **Eliminate by constraint.** Two answers are usually wrong on a single fact, such as needing internet access, a single point of failure or too much custom code. Of the remaining two, pick the one with more managed services and fewer moving parts.
- **Multiple-response questions** tell you how many answers to choose. Each choice must be independently correct; do not pick a pair just because the two answers fit together.
- **Don't fight the scenario.** If it says the company must keep its on-premises database for two more years, do not pick an answer that migrates it now.
- **Short names.** The exam uses short service names. AWS publishes the list, and it is available through the Help button during the exam.
- **Fatigue is the real enemy.** Three hours of dense reading is the hardest part. Check AWS's current break policy for your delivery method before exam day, and don't assume you can leave the desk during an online-proctored session.
