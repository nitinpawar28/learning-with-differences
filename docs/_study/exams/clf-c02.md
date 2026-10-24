---
code: CLF-C02
title: "AWS Certified Cloud Practitioner"
credential: "AWS Certified Cloud Practitioner"
provider: aws
tracks: [cloud]
clouds: [aws]
level: foundational
tier: core
stage: "1"
progress: planned
official_url: https://aws.amazon.com/certification/certified-cloud-practitioner/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html
outline_version: "undated (HTML guide, retrieved 2026-10-24)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS describes the target candidate as having up to 6 months of exposure to AWS Cloud design, implementation or operations, and says even that is not required."
replaces: ""
replaced_by: ""
counterparts: [az-900]
objectives:
  - { id: "1", title: "Cloud Concepts", weight: "24%" }
  - { id: "1.1", title: "Define the benefits of the AWS Cloud" }
  - { id: "1.1.1", title: "Knowledge: Value proposition of the AWS Cloud" }
  - { id: "1.1.2", title: "Skill: Understanding the benefits of global infrastructure (for example, speed of deployment, global reach)" }
  - { id: "1.1.3", title: "Skill: Understanding the advantages of high availability, elasticity, and agility" }
  - { id: "1.2", title: "Identify design principles of the AWS Cloud" }
  - { id: "1.2.1", title: "Knowledge: AWS Well-Architected Framework" }
  - { id: "1.2.2", title: "Skill: Understanding the pillars of the Well-Architected Framework (for example, operational excellence, security, reliability, performance efficiency, cost optimization, sustainability)" }
  - { id: "1.2.3", title: "Skill: Identifying differences between the pillars of the Well-Architected Framework" }
  - { id: "1.3", title: "Understand the benefits of and strategies for migration to the AWS Cloud" }
  - { id: "1.3.1", title: "Knowledge: Cloud adoption strategies" }
  - { id: "1.3.2", title: "Knowledge: Resources to support the cloud migration journey" }
  - { id: "1.3.3", title: "Skill: Understanding the components of the AWS Cloud Adoption Framework (AWS CAF) (for example, reduced business risk; improved environmental, social, and governance [ESG] performance; increased revenue; increased operational efficiency)" }
  - { id: "1.3.4", title: "Skill: Identifying appropriate migration strategies (for example, database replication)" }
  - { id: "1.4", title: "Understand concepts of cloud economics" }
  - { id: "1.4.1", title: "Knowledge: Aspects of cloud economics" }
  - { id: "1.4.2", title: "Knowledge: Cost savings of moving to the cloud" }
  - { id: "1.4.3", title: "Skill: Understanding the role of fixed costs compared with variable costs" }
  - { id: "1.4.4", title: "Skill: Understanding costs that are associated with on-premises environments" }
  - { id: "1.4.5", title: "Skill: Understanding the differences between licensing strategies (for example, Bring Your Own License [BYOL] model compared with included licenses)" }
  - { id: "1.4.6", title: "Skill: Understanding the concept of rightsizing" }
  - { id: "1.4.7", title: "Skill: Identifying benefits of automation" }
  - { id: "1.4.8", title: "Skill: Understanding the economies of scale (for example, cost savings)" }
  - { id: "2", title: "Security and Compliance", weight: "30%" }
  - { id: "2.1", title: "Understand the AWS shared responsibility model" }
  - { id: "2.1.1", title: "Knowledge: AWS shared responsibility model" }
  - { id: "2.1.2", title: "Skill: Recognizing the components of the AWS shared responsibility model" }
  - { id: "2.1.3", title: "Skill: Describing the customer's responsibilities on AWS" }
  - { id: "2.1.4", title: "Skill: Describing AWS responsibilities" }
  - { id: "2.1.5", title: "Skill: Describing responsibilities that the customer and AWS share" }
  - { id: "2.1.6", title: "Skill: Describing how AWS responsibilities and customer responsibilities can shift, depending on the service used (for example, Amazon RDS, AWS Lambda, Amazon EC2)" }
  - { id: "2.2", title: "Understand AWS Cloud security, governance, and compliance concepts" }
  - { id: "2.2.1", title: "Knowledge: AWS compliance and governance concepts" }
  - { id: "2.2.2", title: "Knowledge: Benefits of cloud security (for example, encryption)" }
  - { id: "2.2.3", title: "Knowledge: Where to capture and locate logs that are associated with cloud security" }
  - { id: "2.2.4", title: "Skill: Identifying where to find AWS compliance information (for example, AWS Artifact)" }
  - { id: "2.2.5", title: "Skill: Understanding compliance needs among geographic locations or industries (for example, AWS compliance)" }
  - { id: "2.2.6", title: "Skill: Describing how customers secure resources on AWS (for example, Amazon Inspector, AWS Security Hub, Amazon GuardDuty, AWS Shield)" }
  - { id: "2.2.7", title: "Skill: Identifying encryption options (for example, encryption in transit, encryption at rest)" }
  - { id: "2.2.8", title: "Skill: Recognizing services that aid in governance and compliance (for example, monitoring with Amazon CloudWatch; auditing with AWS CloudTrail and AWS Config; reporting with access reports)" }
  - { id: "2.2.9", title: "Skill: Recognizing compliance requirements that vary among AWS services" }
  - { id: "2.3", title: "Identify AWS access management capabilities" }
  - { id: "2.3.1", title: "Knowledge: Identity and access management (for example, AWS Identity and Access Management [IAM])" }
  - { id: "2.3.2", title: "Knowledge: Importance of protecting the AWS root user account" }
  - { id: "2.3.3", title: "Knowledge: Principle of least privilege" }
  - { id: "2.3.4", title: "Knowledge: AWS IAM Identity Center" }
  - { id: "2.3.5", title: "Skill: Understanding access keys, password policies, and credential storage (for example, AWS Secrets Manager, AWS Systems Manager)" }
  - { id: "2.3.6", title: "Skill: Identifying authentication methods in AWS (for example, multi-factor authentication [MFA], IAM Identity Center, cross-account IAM roles)" }
  - { id: "2.3.7", title: "Skill: Defining groups, users, custom policies, and managed policies in compliance with the principle of least privilege" }
  - { id: "2.3.8", title: "Skill: Identifying tasks that only the account root user can perform" }
  - { id: "2.3.9", title: "Skill: Understanding which methods can achieve root user protection" }
  - { id: "2.3.10", title: "Skill: Understanding the types of identity management (for example, federated)" }
  - { id: "2.4", title: "Identify components and resources for security" }
  - { id: "2.4.1", title: "Knowledge: Security capabilities that AWS provides" }
  - { id: "2.4.2", title: "Knowledge: Security-related documentation that AWS provides" }
  - { id: "2.4.3", title: "Skill: Describing AWS security features and services (for example, AWS WAF, AWS Firewall Manager, AWS Shield, Amazon GuardDuty)" }
  - { id: "2.4.4", title: "Skill: Understanding that third-party security products are available from AWS Marketplace" }
  - { id: "2.4.5", title: "Skill: Identifying where AWS security information is available (for example, AWS Knowledge Center, AWS Security Center, AWS Security Blog)" }
  - { id: "2.4.6", title: "Skill: Understanding the use of AWS services for identifying security issues (for example, AWS Trusted Advisor)" }
  - { id: "3", title: "Cloud Technology and Services", weight: "34%" }
  - { id: "3.1", title: "Define methods of deploying and operating in the AWS Cloud" }
  - { id: "3.1.1", title: "Knowledge: Various ways of provisioning and operating in the AWS Cloud" }
  - { id: "3.1.2", title: "Knowledge: Various ways to access AWS services" }
  - { id: "3.1.3", title: "Knowledge: Types of cloud deployment models" }
  - { id: "3.1.4", title: "Skill: Deciding between options such as programmatic access (for example, APIs, SDKs, CLI), the AWS Management Console, and infrastructure as code (IaC)" }
  - { id: "3.1.5", title: "Skill: Evaluating requirements to determine whether to use one-time operations or repeatable processes" }
  - { id: "3.1.6", title: "Skill: Identifying deployment models (for example, cloud, hybrid, on-premises)" }
  - { id: "3.2", title: "Define the AWS global infrastructure" }
  - { id: "3.2.1", title: "Knowledge: AWS Regions, Availability Zones, and edge locations" }
  - { id: "3.2.2", title: "Knowledge: High availability" }
  - { id: "3.2.3", title: "Knowledge: Use of multiple Regions" }
  - { id: "3.2.4", title: "Knowledge: Benefits of edge locations" }
  - { id: "3.2.5", title: "Skill: Describing relationships among Regions, Availability Zones, and edge locations" }
  - { id: "3.2.6", title: "Skill: Describing how to achieve high availability by using multiple Availability Zones" }
  - { id: "3.2.7", title: "Skill: Recognizing that Availability Zones do not share single points of failure" }
  - { id: "3.2.8", title: "Skill: Describing when to use multiple Regions (for example, disaster recovery, business continuity, low latency for end users, data sovereignty)" }
  - { id: "3.3", title: "Identify AWS compute services" }
  - { id: "3.3.1", title: "Knowledge: AWS compute services" }
  - { id: "3.3.2", title: "Skill: Recognizing the appropriate use of various Amazon EC2 instance types (for example, compute optimized, storage optimized)" }
  - { id: "3.3.3", title: "Skill: Recognizing the appropriate use of various container options (for example, Amazon Elastic Container Service [Amazon ECS], Amazon Elastic Kubernetes Service [Amazon EKS])" }
  - { id: "3.3.4", title: "Skill: Recognizing the appropriate use of various serverless compute options (for example, AWS Fargate, AWS Lambda)" }
  - { id: "3.3.5", title: "Skill: Recognizing that auto scaling provides elasticity" }
  - { id: "3.3.6", title: "Skill: Identifying the purposes of load balancers" }
  - { id: "3.4", title: "Identify AWS database services" }
  - { id: "3.4.1", title: "Knowledge: AWS database services" }
  - { id: "3.4.2", title: "Knowledge: Database migration" }
  - { id: "3.4.3", title: "Skill: Deciding when to use EC2 hosted databases or AWS managed databases" }
  - { id: "3.4.4", title: "Skill: Identifying relational databases (for example, Amazon RDS, Amazon Aurora)" }
  - { id: "3.4.5", title: "Skill: Identifying NoSQL databases (for example, Amazon DynamoDB)" }
  - { id: "3.4.6", title: "Skill: Identifying memory-based databases (for example, Amazon ElastiCache)" }
  - { id: "3.4.7", title: "Skill: Identifying database migration tools (for example, AWS Database Migration Service [AWS DMS], AWS Schema Conversion Tool [AWS SCT])" }
  - { id: "3.5", title: "Identify AWS network services" }
  - { id: "3.5.1", title: "Knowledge: AWS network services" }
  - { id: "3.5.2", title: "Skill: Identifying the components of a VPC (for example, subnets, gateways)" }
  - { id: "3.5.3", title: "Skill: Understanding security in a VPC (for example, network ACLs, security groups, Amazon Inspector)" }
  - { id: "3.5.4", title: "Skill: Understanding the purpose of Amazon Route 53" }
  - { id: "3.5.5", title: "Skill: Identifying network connectivity options to AWS (for example, AWS VPN, AWS Direct Connect)" }
  - { id: "3.6", title: "Identify AWS storage services" }
  - { id: "3.6.1", title: "Knowledge: AWS storage services" }
  - { id: "3.6.2", title: "Skill: Identifying the uses for object storage" }
  - { id: "3.6.3", title: "Skill: Recognizing the differences in Amazon S3 storage classes" }
  - { id: "3.6.4", title: "Skill: Identifying block storage solutions (for example, Amazon Elastic Block Store [Amazon EBS], instance store)" }
  - { id: "3.6.5", title: "Skill: Identifying file services (for example, Amazon Elastic File System [Amazon EFS], Amazon FSx)" }
  - { id: "3.6.6", title: "Skill: Identifying cached file systems (for example, AWS Storage Gateway)" }
  - { id: "3.6.7", title: "Skill: Understanding use cases for lifecycle policies" }
  - { id: "3.6.8", title: "Skill: Understanding use cases for AWS Backup" }
  - { id: "3.7", title: "Identify AWS artificial intelligence and machine learning (AI/ML) services and analytics services" }
  - { id: "3.7.1", title: "Knowledge: AWS AI/ML services" }
  - { id: "3.7.2", title: "Knowledge: AWS analytics services" }
  - { id: "3.7.3", title: "Skill: Understanding AI/ML services and the tasks that they accomplish (for example, Amazon SageMaker AI, Amazon Lex)" }
  - { id: "3.7.4", title: "Skill: Identifying the services for data analytics (for example, Amazon Athena, Amazon Kinesis, AWS Glue, Amazon Quick Sight)" }
  - { id: "3.8", title: "Identify services from other in-scope AWS service categories" }
  - { id: "3.8.1", title: "Knowledge: Application integration services of Amazon EventBridge, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS)" }
  - { id: "3.8.2", title: "Knowledge: Business application services of Amazon Connect and Amazon Simple Email Service (Amazon SES)" }
  - { id: "3.8.3", title: "Knowledge: Customer enablement services (for example, AWS Support)" }
  - { id: "3.8.4", title: "Knowledge: Developer tool services and capabilities (for example, AWS CodeBuild, AWS CodePipeline, and AWS X-Ray)" }
  - { id: "3.8.5", title: "Knowledge: End-user computing services of Amazon AppStream 2.0, Amazon WorkSpaces, and Amazon WorkSpaces Secure Browser" }
  - { id: "3.8.6", title: "Knowledge: Frontend web and mobile services of AWS Amplify" }
  - { id: "3.8.7", title: "Knowledge: IoT services (for example, AWS IoT Core)" }
  - { id: "3.8.8", title: "Skill: Choosing the appropriate service to deliver messages and to send alerts and notifications" }
  - { id: "3.8.9", title: "Skill: Choosing the appropriate service to meet business application needs" }
  - { id: "3.8.10", title: "Skill: Choosing the appropriate option for business support assistance" }
  - { id: "3.8.11", title: "Skill: Identifying the tools to develop, deploy, and troubleshoot applications" }
  - { id: "3.8.12", title: "Skill: Identifying the services that can present the output of virtual machines (VMs) on end-user machines" }
  - { id: "3.8.13", title: "Skill: Identifying the services that can create and deploy frontend and mobile services" }
  - { id: "3.8.14", title: "Skill: Identifying the services that manage IoT devices" }
  - { id: "4", title: "Billing, Pricing, and Support", weight: "12%" }
  - { id: "4.1", title: "Compare AWS pricing models" }
  - { id: "4.1.1", title: "Knowledge: Compute purchasing options (for example, On-Demand Instances, Reserved Instances, Spot Instances, AWS Savings Plans, Dedicated Hosts, Dedicated Instances, Capacity Reservations)" }
  - { id: "4.1.2", title: "Knowledge: Storage options and tiers" }
  - { id: "4.1.3", title: "Skill: Identifying when to use various compute purchasing options" }
  - { id: "4.1.4", title: "Skill: Describing Reserved Instance flexibility" }
  - { id: "4.1.5", title: "Skill: Describing Reserved Instance behavior in AWS Organizations" }
  - { id: "4.1.6", title: "Skill: Understanding incoming data transfer costs and outgoing data transfer costs (for example, from one AWS Region to another Region, within the same Region)" }
  - { id: "4.1.7", title: "Skill: Understanding pricing options for various storage options and tiers" }
  - { id: "4.2", title: "Understand resources for billing, budget, and cost management" }
  - { id: "4.2.1", title: "Knowledge: Billing support and information" }
  - { id: "4.2.2", title: "Knowledge: Pricing information for AWS services" }
  - { id: "4.2.3", title: "Knowledge: AWS Organizations" }
  - { id: "4.2.4", title: "Knowledge: AWS cost allocation tags" }
  - { id: "4.2.5", title: "Skill: Understanding the appropriate uses and capabilities of AWS Budgets and AWS Cost Explorer" }
  - { id: "4.2.6", title: "Skill: Understanding the appropriate uses and capabilities of AWS Pricing Calculator" }
  - { id: "4.2.7", title: "Skill: Understanding AWS Organizations consolidated billing and allocation of costs" }
  - { id: "4.2.8", title: "Skill: Understanding various types of cost allocation tags and their relation to billing reports (for example, AWS Cost and Usage Report)" }
  - { id: "4.3", title: "Identify AWS technical resources and AWS Support options" }
  - { id: "4.3.1", title: "Knowledge: Resources and documentation available on official AWS websites" }
  - { id: "4.3.2", title: "Knowledge: AWS Support plans" }
  - { id: "4.3.3", title: "Knowledge: Role of the AWS Partner Network, including independent software vendors and system integrators" }
  - { id: "4.3.4", title: "Knowledge: AWS Support Center" }
  - { id: "4.3.5", title: "Skill: Locating AWS whitepapers, blogs, and documentation on official AWS websites" }
  - { id: "4.3.6", title: "Skill: Identifying and locating AWS technical resources (for example, AWS Prescriptive Guidance, AWS Knowledge Center, AWS re:Post)" }
  - { id: "4.3.7", title: "Skill: Identifying AWS Support options for AWS customers (for example, customer service and communities, Basic Support, AWS Business Support+, AWS Enterprise Support, AWS Unified Operations)" }
  - { id: "4.3.8", title: "Skill: Identifying the role of AWS Trusted Advisor, AWS Health Dashboard, and the AWS Health API to help manage and monitor environments for cost optimization" }
  - { id: "4.3.9", title: "Skill: Identifying the role of the AWS Trust and Safety team to report abuse of AWS resources" }
  - { id: "4.3.10", title: "Skill: Understanding the role of AWS Partners (for example, AWS Marketplace, independent software vendors, system integrators)" }
  - { id: "4.3.11", title: "Skill: Identifying the benefits of being an AWS Partner (for example, partner training and certification, partner events, partner volume discounts)" }
  - { id: "4.3.12", title: "Skill: Identifying the key services that AWS Marketplace offers (for example, cost management, governance and entitlement)" }
  - { id: "4.3.13", title: "Skill: Identifying technical assistance options available at AWS (for example, AWS Professional Services, AWS solutions architects)" }
---
## Exam format

Every fact below is as of 2026-10-24 and comes from the [certification page](https://aws.amazon.com/certification/certified-cloud-practitioner/) and the [CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html). AWS changes these details from time to time, so confirm them on those pages before you book.

| Item | Detail (as of 2026-10-24) |
| --- | --- |
| Category | Foundational |
| Question types | Multiple choice (one correct answer out of four) and multiple response (two or more correct answers out of five or more options) |
| Number of questions | 65: 50 scored and 15 unscored. The unscored ones are not marked, so treat every question as if it counts |
| Duration | 90 minutes |
| Passing score | 700 on a scaled score of 100–1,000. Scoring is compensatory: you need to pass the exam as a whole, not each domain |
| Price | 100 USD (see [exam pricing](https://aws.amazon.com/certification/policies/before-testing/) for taxes and currency conversion) |
| Languages | Arabic, English, French (France), German, Italian, Japanese, Korean, Portuguese (Brazil), Spanish (Latin America), Spanish (Spain), Simplified Chinese and Traditional Chinese. The Italian and German versions will be retired after December 31, 2026 |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | Valid for 3 years. You can recertify by passing the latest version of this exam or by passing any Associate or Professional exam. The page also names a game-based option, AWS Cloud Quest: Recertify Cloud Practitioner. Check its current status on the [recertification page](https://aws.amazon.com/certification/recertification/) |
| Discount | Once you hold one AWS certification, you get a 50% discount on another AWS exam through your AWS Certification Account |

Unanswered questions are scored as wrong and there is no penalty for guessing, so never leave a question blank. The exam guide does not print a version number or publication date, so this library records it as undated and was last checked on 2026-10-24.

## What the exam really tests

CLF-C02 tests vocabulary and judgement at the level of "which service or concept fits this need?" It does not test how to configure anything. The guide lists coding, cloud architecture design, troubleshooting, implementation and load testing as out of scope. There are four domains:

- **Cloud Concepts (24%)**: the value of the AWS Cloud, the six pillars of the AWS Well-Architected Framework and how they differ, the AWS Cloud Adoption Framework (AWS CAF) and migration strategies, and cloud economics (fixed and variable costs, BYOL compared with included licences, rightsizing, economies of scale).
- **Security and Compliance (30%)**: the shared responsibility model, including how the line moves between Amazon EC2, Amazon RDS and AWS Lambda; where compliance evidence lives (AWS Artifact); which service does what among Amazon Inspector, AWS Security Hub, Amazon GuardDuty, AWS Shield, AWS WAF and AWS Firewall Manager; IAM users, groups, roles and policies; AWS IAM Identity Center; protecting the root user and the tasks only the root user can perform.
- **Cloud Technology and Services (34%)**: the largest domain and the broadest one. It covers Regions, Availability Zones and edge locations; EC2 instance families; containers (Amazon ECS, Amazon EKS, AWS Fargate); databases (RDS, Aurora, DynamoDB, ElastiCache, AWS DMS, AWS SCT); VPC building blocks; storage (S3 storage classes, EBS compared with instance store, EFS, FSx, Storage Gateway, AWS Backup); AI/ML and analytics names (Amazon SageMaker AI, Amazon Lex, Athena, Kinesis, AWS Glue, Amazon Quick Sight); and a long tail of other services (EventBridge, SNS, SQS, Amazon Connect, SES, AWS Support, the Code* tools, AWS X-Ray, WorkSpaces, AppStream 2.0, AWS Amplify, AWS IoT Core).
- **Billing, Pricing, and Support (12%)**: the EC2 purchasing options (On-Demand, Reserved Instances, Spot, Savings Plans, Dedicated Hosts, Dedicated Instances, Capacity Reservations), how Reserved Instances behave inside AWS Organizations, data transfer charges, AWS Budgets compared with Cost Explorer and the Pricing Calculator, cost allocation tags, and the support plans. The guide now lists Basic Support, AWS Business Support+, AWS Enterprise Support and AWS Unified Operations, along with Trusted Advisor, the AWS Health Dashboard and the AWS Partner Network.

Most questions are short scenarios that end with "which service…" or "whose responsibility…". The wrong answers are real AWS services that sound plausible. Candidates lose points in three places:

1. **Near-twin services.** GuardDuty (threat detection) compared with Inspector (vulnerability scanning) compared with Macie (sensitive data in S3); CloudTrail (who made which API call) compared with Config (what a resource's configuration was and whether it complies) compared with CloudWatch (metrics, logs and alarms); Budgets (alerts you before you overspend) compared with Cost Explorer (analyses what you have already spent).
2. **The shared responsibility boundary.** Patching the guest OS on EC2 is the customer's job. On RDS, AWS patches the database engine. On Lambda, the customer is left mainly with code, IAM and data.
3. **Support plans and pricing details.** These are pure facts to memorise. Learn the support plan names exactly as Task 4.3 of the guide lists them (Basic Support, AWS Business Support+, AWS Enterprise Support, AWS Unified Operations), and check the AWS Support pages for what each one includes.

## Study strategy

1. **Start from what AZ-900 already gave you.** You already understand cloud models, CapEx compared with OpEx, high availability compared with elasticity, and the shared responsibility idea. Build a two-column table that maps each Azure term to its AWS counterpart (Region and Availability Zone, Microsoft Entra ID and IAM or IAM Identity Center, Azure Policy and AWS Config or SCPs, Cost Management and Cost Explorer or Budgets, Defender for Cloud and Security Hub or GuardDuty). Then study the places where the analogy breaks (see the next section).
2. **Read the exam guide domain by domain** and turn every "for example" service it names into a flash card that says what the service does and when you would choose it. The guide is the syllabus, and its examples are a strong hint about which distractors you will see.
3. **Do a little hands-on work.** Create a free-tier account, enable MFA on the root user, create an IAM Identity Center user, launch and terminate one EC2 instance, create an S3 bucket with a lifecycle rule, and set up an AWS Budget. That is enough. The exam does not test configuration, but having clicked through the console once makes the terms stick.
4. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (AWS Cloud Practitioner Essentials, the AWS Certification Official Practice Question Set, the Official Pretest, and the Official Practice Exam as a readiness check), plus the [exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) with its in-scope service list. The certification page also points to AWS Builder Labs, AWS Cloud Quest, AWS Jam, AWS SimuLearn and AWS Escape Room for practice.
5. **Your .NET and Angular background** helps with the developer-tool items (CodeBuild, CodePipeline, X-Ray, Amplify) and with SDK and CLI access methods. **Your AZ-204 and CKAD preparation** makes the container questions easy: ECS is AWS's own orchestrator, EKS is managed Kubernetes, and Fargate is serverless capacity that can sit under either one. Be careful not to over-think. Answers that would be right at associate level ("configure a NAT gateway with a route table…") are not what this exam asks for. Pick the plain service name.

Plan for about two to three weeks part-time given your background. Take CLF-C02 first in the AWS path, because it gives you the shared vocabulary for SAA-C03 and AIF-C01.

## Differences from related exams

- **CLF-C02 compared with AZ-900 (its Azure counterpart).** The scope and depth are almost the same: cloud concepts, core services, security and governance, and pricing and support. CLF-C02 puts much more weight on security and compliance (30%), has a whole task on the Well-Architected Framework and CAF, and asks harder pricing questions (Reserved Instance flexibility, Savings Plans, how RIs are shared in Organizations, data-transfer direction). AZ-900 spends more time on governance tools (Azure Policy, resource locks, the resource hierarchy). The analogies that break: AWS has no container that owns resources the way an Azure resource group does (AWS Resource Groups are only tag-based views, so accounts, Organizations and tags do that job); IAM policies attach to identities and resources, while Azure RBAC role assignments are made at a scope; and "Availability Zone" means roughly the same thing on both clouds, but AWS requires you to pick subnets per AZ.
- **CLF-C02 compared with AIF-C01.** The AI Practitioner certification page says the Cloud Practitioner outline has only one task statement about AI (in the guide that is Task 3.7), while AI Practitioner is about AI from start to finish. AIF-C01 assumes you already know the CLF-level cloud vocabulary.
- **CLF-C02 compared with SAA-C03.** SAA-C03 takes the same service list and asks you to design with it: which combination is most resilient, most secure or cheapest under the stated constraints. CLF-C02 asks only what each service is. The question count and format are the same, but SAA has 130 minutes, much longer scenarios and a 720 passing score.
- **CLF-C02 compared with the Google and other vendor foundational exams.** This library does not track them. Within this library, AZ-900 is the comparison that matters.

## Exam-day notes

- You have 65 questions in 90 minutes, which is about 80 seconds each. Most take 30–45 seconds. Answer every question on the first pass, flag the ones you are unsure of, and come back to them.
- For multiple-response questions, the stem tells you how many answers to choose (for example, "Select TWO"). Count before you submit.
- Watch the qualifiers: "MOST cost-effective", "LEAST operational overhead", "customer responsibility". These words decide between two answers that are otherwise both correct.
- Traps: Trusted Advisor gives recommendations but does not enforce anything; AWS Artifact holds compliance reports, not your own audit logs; edge locations serve CloudFront and Route 53, not EC2 workloads; Savings Plans compared with Reserved Instances is a question of how flexible the commitment is.
- Online proctoring requires a clean desk and a stable connection, and you cannot leave the camera view. If you would rather avoid that risk, book a test centre.
