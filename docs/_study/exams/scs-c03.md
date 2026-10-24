---
code: SCS-C03
title: "AWS Certified Security – Specialty"
credential: "AWS Certified Security – Specialty"
provider: aws
tracks: [security, cloud]
clouds: [aws]
level: specialty
tier: core
stage: "4"
progress: planned
official_url: https://aws.amazon.com/certification/certified-security-specialty/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html
outline_version: "1.0 (2026-03-26)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends five years of IT security experience designing and implementing security solutions and two or more years of hands-on experience securing AWS workloads."
replaces: "scs-c02"
replaced_by: ""
counterparts: [sc-500]
objectives:
  - { id: "1", title: "Detection", weight: "16%" }
  - { id: "1.1", title: "Design and implement monitoring and alerting solutions for an AWS account or organization" }
  - { id: "1.1.1", title: "Skill: Analyze workloads to determine monitoring requirements" }
  - { id: "1.1.2", title: "Skill: Design and implement workload monitoring strategies (e.g. by configuring resource health checks)" }
  - { id: "1.1.3", title: "Skill: Aggregate security and monitoring events" }
  - { id: "1.1.4", title: "Skill: Create metrics, alerts and dashboards to detect anomalies (Amazon GuardDuty, Amazon Security Lake, AWS Security Hub, Amazon Macie)" }
  - { id: "1.1.5", title: "Skill: Automate regular assessments and investigations (AWS Config conformance packs, Security Hub, Systems Manager State Manager)" }
  - { id: "1.2", title: "Design and implement logging solutions" }
  - { id: "1.2.1", title: "Skill: Identify sources for log ingestion and storage based on requirements" }
  - { id: "1.2.2", title: "Skill: Configure logging for AWS services and applications (organization CloudTrail trail, dedicated CloudWatch logging account, CloudWatch Logs agent)" }
  - { id: "1.2.3", title: "Skill: Implement log storage and log data lakes (e.g. Security Lake) and integrate with third-party security tools" }
  - { id: "1.2.4", title: "Skill: Use AWS services to analyze logs (e.g. CloudWatch Logs Insights, Amazon Athena, Security Hub findings)" }
  - { id: "1.2.5", title: "Skill: Use AWS services to normalize, parse, and correlate logs (e.g. Amazon OpenSearch Service, AWS Lambda, Amazon Managed Grafana)" }
  - { id: "1.2.6", title: "Skill: Choose log sources based on network design and threats (VPC Flow Logs, transit gateway flow logs, Route 53 Resolver logs)" }
  - { id: "1.3", title: "Troubleshoot security monitoring, logging, and alerting solutions" }
  - { id: "1.3.1", title: "Skill: Analyze functionality, permissions and configuration of logging resources (Lambda, API Gateway, CloudFront logging, health checks)" }
  - { id: "1.3.2", title: "Skill: Remediate misconfiguration of resources (e.g. by troubleshooting CloudWatch Agent configurations, troubleshooting missing logs)" }
  - { id: "2", title: "Incident Response", weight: "14%" }
  - { id: "2.1", title: "Design and test an incident response plan" }
  - { id: "2.1.1", title: "Skill: Design response plans and runbooks for security incidents (Systems Manager OpsCenter, SageMaker AI notebooks)" }
  - { id: "2.1.2", title: "Skill: Prepare services for incidents (provisioned access, pre-deployed security tools, blast-radius reduction, AWS Shield Advanced)" }
  - { id: "2.1.3", title: "Skill: Test and validate the incident response plan (AWS Fault Injection Service, AWS Resilience Hub)" }
  - { id: "2.1.4", title: "Skill: Automatically remediate incidents (Systems Manager, Automated Forensics Orchestrator for Amazon EC2, Step Functions, Amazon Application Recovery Controller, Lambda)" }
  - { id: "2.2", title: "Respond to security events" }
  - { id: "2.2.1", title: "Skill: Capture and store relevant system and application logs as forensic artifacts" }
  - { id: "2.2.2", title: "Skill: Search and correlate logs for security events across applications and AWS services" }
  - { id: "2.2.3", title: "Skill: Validate findings from AWS security services to assess the scope and impact of an event" }
  - { id: "2.2.4", title: "Skill: Contain, eradicate and recover affected resources (network containment controls, restoring backups)" }
  - { id: "2.2.5", title: "Skill: Describe methods to conduct root cause analysis (e.g. Amazon Detective)" }
  - { id: "3", title: "Infrastructure Security", weight: "18%" }
  - { id: "3.1", title: "Design, implement, and troubleshoot security controls for network edge services" }
  - { id: "3.1.1", title: "Skill: Define and select edge security strategies based on anticipated threats and attacks" }
  - { id: "3.1.2", title: "Skill: Implement network edge protection (CloudFront headers, AWS WAF, AWS IoT policies, OWASP Top 10, S3 CORS, Shield Advanced)" }
  - { id: "3.1.3", title: "Skill: Design edge controls and rules (geography, geolocation, rate limiting, client fingerprinting)" }
  - { id: "3.1.4", title: "Skill: Integrate edge services with third parties (OCSF-format ingestion, third-party WAF rules)" }
  - { id: "3.2", title: "Design, implement, and troubleshoot security controls for compute workloads" }
  - { id: "3.2.1", title: "Skill: Build hardened Amazon EC2 AMIs and container images (Systems Manager, EC2 Image Builder)" }
  - { id: "3.2.2", title: "Skill: Apply instance profiles, service roles, and execution roles appropriately to authorize compute workloads" }
  - { id: "3.2.3", title: "Skill: Scan compute for known vulnerabilities (Amazon Inspector for container images and Lambda, GuardDuty runtime monitoring)" }
  - { id: "3.2.4", title: "Skill: Automate patching with continuous validation (Systems Manager Patch Manager, Amazon Inspector)" }
  - { id: "3.2.5", title: "Skill: Configure secure administrative access to compute resources (e.g. Systems Manager Session Manager, EC2 Instance Connect)" }
  - { id: "3.2.6", title: "Skill: Find and fix vulnerabilities in pipelines (Amazon Q Developer, Amazon CodeGuru Security)" }
  - { id: "3.2.7", title: "Skill: Protect generative AI applications (OWASP Top 10 for LLM Applications protections and guardrails)" }
  - { id: "3.3", title: "Design and troubleshoot network security controls" }
  - { id: "3.3.1", title: "Skill: Design and troubleshoot network traffic controls (security groups, network ACLs, AWS Network Firewall)" }
  - { id: "3.3.2", title: "Skill: Design secure hybrid and multi-cloud connectivity (AWS Site-to-Site VPN, AWS Direct Connect, MACsec)" }
  - { id: "3.3.3", title: "Skill: Configure security requirements for hybrid-to-AWS communication (AWS Verified Access)" }
  - { id: "3.3.4", title: "Skill: Design network segmentation based on security requirements (e.g. north/south and east/west traffic protections, isolated subnets)" }
  - { id: "3.3.5", title: "Skill: Identify unnecessary network access (AWS Verified Access, Network Access Analyzer, Amazon Inspector network reachability)" }
  - { id: "4", title: "Identity and Access Management", weight: "20%" }
  - { id: "4.1", title: "Design, implement, and troubleshoot authentication strategies" }
  - { id: "4.1.1", title: "Skill: Design identity solutions for human, application and system authentication (IAM Identity Center, Amazon Cognito, MFA, IdP integration)" }
  - { id: "4.1.2", title: "Skill: Configure mechanisms to issue temporary credentials (e.g. AWS STS, Amazon S3 presigned URLs)" }
  - { id: "4.1.3", title: "Skill: Troubleshooting authentication issues (e.g. CloudTrail, Amazon Cognito, IAM Identity Center permission sets, AWS Directory Service)" }
  - { id: "4.2", title: "Design, implement, and troubleshoot authorization strategies" }
  - { id: "4.2.1", title: "Skill: Design authorization controls for human, application and system access (Amazon Verified Permissions, IAM paths, IAM Roles Anywhere, resource and trust policies)" }
  - { id: "4.2.2", title: "Skill: Design ABAC and RBAC strategies (tag- and attribute-based resource access)" }
  - { id: "4.2.3", title: "Skill: Design, interpret and implement least-privilege IAM policies (permissions boundaries, session policies)" }
  - { id: "4.2.4", title: "Skill: Analyze authorization failures to determine causes or effects (e.g. IAM Policy Simulator, IAM Access Analyzer)" }
  - { id: "4.2.5", title: "Skill: Investigate and correct unintended permissions (IAM Access Analyzer)" }
  - { id: "5", title: "Data Protection", weight: "18%" }
  - { id: "5.1", title: "Design and implement controls for data in transit" }
  - { id: "5.1.1", title: "Skill: Require encryption in transit (ELB security policies, enforced TLS configurations)" }
  - { id: "5.1.2", title: "Skill: Provide secure, private access to resources (AWS PrivateLink, VPC endpoints, AWS Client VPN, AWS Verified Access)" }
  - { id: "5.1.3", title: "Skill: Configure inter-resource encryption in transit (Amazon EMR, Amazon EKS, SageMaker AI inter-node encryption, Nitro encryption)" }
  - { id: "5.2", title: "Design and implement controls for data at rest" }
  - { id: "5.2.1", title: "Skill: Design encryption at rest to requirements (AWS CloudHSM vs AWS KMS, client-side vs server-side encryption)" }
  - { id: "5.2.2", title: "Skill: Protect data integrity (S3 Object Lock, S3 Glacier Vault Lock, versioning, code signing, file validation)" }
  - { id: "5.2.3", title: "Skill: Design lifecycle and retention for data (S3 Lifecycle, S3 Object Lock, Amazon EFS Lifecycle, FSx for Lustre backup policies)" }
  - { id: "5.2.4", title: "Skill: Design secure replication and backup (Amazon Data Lifecycle Manager, AWS Backup, ransomware protection, AWS DataSync)" }
  - { id: "5.3", title: "Design and implement controls to protect confidential data, credentials, secrets, and cryptographic key materials" }
  - { id: "5.3.1", title: "Skill: Design management and rotation of credentials and secrets (e.g. AWS Secrets Manager)" }
  - { id: "5.3.2", title: "Skill: Manage imported key material and external key stores (import, rotation, configuration)" }
  - { id: "5.3.3", title: "Skill: Describe the differences between imported key material and AWS generated key material" }
  - { id: "5.3.4", title: "Skill: Mask sensitive data (e.g. CloudWatch Logs data protection policies, Amazon SNS message data protection)" }
  - { id: "5.3.5", title: "Skill: Manage keys and certificates in one or many Regions (AWS KMS customer managed keys, AWS Private Certificate Authority)" }
  - { id: "6", title: "Security Foundations and Governance", weight: "14%" }
  - { id: "6.1", title: "Develop a strategy to centrally deploy and manage AWS accounts" }
  - { id: "6.1.1", title: "Skill: Deploy and configure organizations by using AWS Organizations" }
  - { id: "6.1.2", title: "Skill: Implement and manage AWS Control Tower in new and existing environments, and deploy optional and custom controls" }
  - { id: "6.1.3", title: "Skill: Implement organization policies to manage permissions (e.g. SCPs, RCPs, AI service opt-out policies, declarative policies)" }
  - { id: "6.1.4", title: "Skill: Centrally manage security services (e.g. delegated administrator accounts)" }
  - { id: "6.1.5", title: "Skill: Manage root user credentials (centralized root access for member accounts, MFA, break-glass procedures)" }
  - { id: "6.2", title: "Implement a secure and consistent deployment strategy for cloud resources" }
  - { id: "6.2.1", title: "Skill: Deploy resources consistently and securely with IaC (CloudFormation StackSets, third-party IaC, CloudFormation Guard, cfn-lint)" }
  - { id: "6.2.2", title: "Skill: Use tags to organize AWS resources into groups for management (e.g. by grouping by department, cost center, environment)" }
  - { id: "6.2.3", title: "Skill: Deploy and enforce policies and configurations from a central source (e.g. AWS Firewall Manager)" }
  - { id: "6.2.4", title: "Skill: Securely share resources across AWS accounts (e.g. AWS Service Catalog, AWS Resource Access Manager (AWS RAM))" }
  - { id: "6.3", title: "Evaluate the compliance of AWS resources" }
  - { id: "6.3.1", title: "Skill: Detect, remediate and notify on noncompliant resources (AWS Config aggregation and remediation, Security Hub)" }
  - { id: "6.3.2", title: "Skill: Use AWS audit services to collect and organize evidence (e.g. AWS Audit Manager, AWS Artifact)" }
  - { id: "6.3.3", title: "Skill: Use AWS services to evaluate architecture for compliance with AWS security best practices (e.g. AWS Well-Architected Framework tool)" }
---
## Exam format

All facts are as of 2026-10-24, taken from the [certification page](https://aws.amazon.com/certification/certified-security-specialty/) and the [SCS-C03 exam guide](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03.html). Confirm them on the official page before you book.

| Item | SCS-C03 (as of 2026-10-24) |
|---|---|
| Version | SCS-C03 replaced SCS-C02 on December 2, 2025. SCS-C02 was last available on December 1, 2025. The guide's change history lists version 1.0, published March 26, 2026 |
| Question types | Multiple choice, multiple response, **ordering** (put 3–5 steps in the right order) and **matching** (pair responses with 3–7 prompts). Ordering and matching give credit only when the whole item is right |
| Number of questions | 65 in total: 50 scored and 15 unscored |
| Duration | 170 minutes |
| Passing score | 750 on a scaled score of 100–1,000, compensatory across domains |
| Price | 300 USD. AWS's exam pricing page has further cost information, including foreign exchange rates. Once you earn one AWS certification, AWS gives you a 50% discount on your next AWS certification exam |
| Languages | English, Japanese, Korean, Portuguese (Brazil), Simplified Chinese, Spanish (Latin America). The page says the Simplified Chinese, Spanish (Latin America) and Portuguese (Brazil) versions will be retired after December 31, 2026 |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | 3 years. You renew by passing the latest version |
| Prerequisites | None required. AWS recommends five years of IT security experience designing and implementing security solutions, plus two or more years securing AWS workloads. The guide frames this as the equivalent of 3–5 years securing cloud solutions |

With only 50 scored questions, each one counts for more than on a 65-scored exam, and the ordering and matching items are all-or-nothing.

## What the exam really tests

SCS-C03 is a practitioner's security exam. It asks how you would detect, contain, prevent and prove compliance with specific AWS services and settings, across one account or a whole organization. The guide says designing cryptographic algorithms, packet-level traffic analysis, architecting entire cloud deployments, managing end-user compute and training ML models are **out of scope**. The depth is in AWS security controls, not in security theory.

- **Detection (16%).** GuardDuty, Security Hub, Security Lake, Macie, AWS Config conformance packs, organization CloudTrail trails, a dedicated log-archive account, CloudWatch Logs Insights and Athena for analysis, network log sources (VPC Flow Logs, transit gateway flow logs, Route 53 Resolver query logs), and troubleshooting missing logs.
- **Incident response (14%).** Runbooks in Systems Manager OpsCenter, preparing accounts before an incident (break-glass access, pre-deployed tooling, Shield Advanced), testing the plan with AWS Fault Injection Service and AWS Resilience Hub, automated remediation, forensic capture, containment, and root cause analysis with Amazon Detective.
- **Infrastructure security (18%).** Edge protection with AWS WAF, CloudFront and Shield Advanced, hardened AMIs and images with EC2 Image Builder, Amazon Inspector scanning, Patch Manager, Session Manager in place of SSH, pipeline security scanning, **guardrails for GenAI applications (OWASP Top 10 for LLM Applications)**, Network Firewall, hybrid connectivity security including MACsec, Verified Access and Network Access Analyzer.
- **Identity and access management (20%, the largest).** IAM Identity Center, Cognito, STS and presigned URLs, policy evaluation logic, permissions boundaries and session policies, ABAC versus RBAC, Verified Permissions, IAM Roles Anywhere, cross-account trust policies, and diagnosing denied requests with the Policy Simulator and IAM Access Analyzer.
- **Data protection (18%).** TLS enforcement, PrivateLink and endpoints, inter-node encryption, KMS versus CloudHSM, client-side versus server-side encryption, imported key material and external key stores, S3 Object Lock and Glacier Vault Lock, AWS Backup and ransomware resilience, Secrets Manager rotation, data masking in CloudWatch Logs and SNS, multi-Region keys and AWS Private CA.
- **Security foundations and governance (14%).** Organizations, Control Tower controls, SCPs, **RCPs** (resource control policies), declarative policies and AI-service opt-out policies, delegated administrators, centralized root access, CloudFormation StackSets and CloudFormation Guard, Firewall Manager, RAM and Service Catalog, Audit Manager and AWS Artifact.

The [appendix comparing SCS-C02 and SCS-C03](https://docs.aws.amazon.com/aws-certification/latest/security-specialty-03/security-specialty-03-appendix-b.html) lists what changed. C03 adds GenAI guardrails, OCSF-format integrations, inter-resource encryption in transit, imported versus AWS-generated key material, data masking and multi-Region keys and certificates. It drops TCP/IP fundamentals, host-based firewalls, S3 static website hosting and ASFF details. Detection and incident response, previously "Threat Detection and Incident Response" and "Security Logging and Monitoring", are now two separate domains.

Where candidates lose points:

- **Policy evaluation.** An explicit deny anywhere wins. SCPs and RCPs limit permissions but never grant them. Permissions boundaries and session policies intersect with identity policies. Cross-account access needs both the resource policy and the caller's identity policy to allow it. Within one account a resource policy can grant access on its own, but a KMS key is only usable when its key policy allows it.
- **KMS details.** Key policy versus IAM policy, grants, the difference between AWS managed and customer managed keys, how imported key material differs from AWS-generated material (you own its durability, expiry and rotation, and you can delete it yourself), and multi-Region keys.
- **"Which log has it?"** CloudTrail management versus data events, VPC Flow Logs not capturing payloads, Route 53 Resolver query logs for DNS exfiltration, and S3 server access logs versus CloudTrail data events.
- **Order of response.** Ordering questions expect the AWS incident-response sequence: preserve evidence (snapshots, memory, logs) and isolate the resource before you terminate or remediate it.

## Study strategy

1. **IAM first.** Learn policy evaluation logic until you can trace a request through SCP, RCP, resource policy, identity policy, boundary and session policy on paper. This is the largest domain and also underpins every other domain.
2. **Multi-account foundations.** In a sandbox organization: enable Control Tower, apply an SCP and an RCP, set delegated administrators for GuardDuty, Security Hub, Macie and Inspector, create an organization trail into a log-archive account, and turn on centralized root access.
3. **Detection pipeline.** Enable GuardDuty and Security Hub, generate sample findings, route them through EventBridge to a Lambda remediation, and query CloudTrail with Athena or CloudTrail Lake.
4. **Data protection.** Create customer managed KMS keys, write key policies for cross-account use, try imported key material, set up Secrets Manager rotation, and use S3 Object Lock in governance and compliance modes.
5. **Infrastructure.** Put AWS WAF on CloudFront with rate-based and geographic rules, try Network Firewall in a hub VPC, replace SSH with Session Manager, and run Inspector on a container image.
6. **Incident response.** Write a runbook for a compromised EC2 instance and a leaked access key, and practise the order of steps.

Official resources named on the certification page (as of 2026-10-24) are the AWS Skill Builder **Exam Prep Plan** (four steps), the **Official Practice Question Set**, the **Official Pretest**, digital courses, **AWS Builder Labs**, **AWS Cloud Quest**, **AWS Jam**, **AWS SimuLearn**, flashcards and instructor-led question walkthroughs. AWS also links the AWS Incident Response Demonstrated and AWS Securing Agent Identities Demonstrated credentials. The [policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) chapter of the IAM User Guide is worth reading in full.

How your background helps or misleads:

- **AZ-900 and AZ-204 preparation** give you RBAC, managed identity and Key Vault concepts. The trap is that Azure RBAC role assignments on scopes are not AWS IAM policies attached to principals and resources. An Azure managed identity is closest to an AWS IAM role assumed by a service, and Key Vault mixes keys, secrets and certificates where AWS splits them into KMS, Secrets Manager and ACM or Private CA.
- **CKAD preparation** helps with container image hardening and with the idea of execution roles, much like Kubernetes service accounts mapped to IAM through EKS Pod Identity.
- **.NET and Angular development** helps with Cognito, OAuth and OIDC flows, presigned URLs and CORS, all of which appear as edge or identity controls here.

## Differences from related exams

- **SCS-C03 vs SC-500 (Microsoft's Azure security engineer exam).** They are counterparts: both are for the engineer who implements cloud security controls. SC-500 covers Azure identity, networking, compute, data and Microsoft Defender for Cloud and Sentinel operations. SCS-C03 is a specialty with fewer, harder questions, includes ordering and matching formats, and weights multi-account governance and incident response more heavily. On the Azure side, much of the SIEM and SOC depth lives in a separate exam (SC-200).
- **SCS-C03 vs AZ-500 (Microsoft Azure Security Technologies).** AZ-500 is the earlier Azure security engineer exam and covers similar engineer-level ground. This library's AZ-500 entry records it as retired on 2026-08-31 and replaced by SC-500, so compare against SC-500 unless you already hold the AZ-500 credential.
- **SCS-C03 vs SAP-C03.** SAP treats security as one design dimension. SCS goes deeper into how each control behaves and how to investigate. SAP will ask you to *choose* encryption at rest, while SCS will ask about the key policy statement that breaks cross-account decryption.
- **SCS-C03 vs CCSK and CCSP.** These are vendor-neutral cloud security credentials: CCSK is knowledge-based and CCSP needs years of experience and an endorsement. They test concepts, governance and the shared responsibility model across all clouds. SCS tests AWS implementation.
- **SCS-C03 vs CISSP.** CISSP is a broad security-management credential with an experience requirement. SCS is narrow and hands-on, and covers almost none of CISSP's governance and risk depth.

## Exam-day notes

- **Time budget.** 170 minutes for 65 questions is about 2 minutes 37 seconds each, more than the 2 minutes 24 seconds of the 75-question, 180-minute professional exams (ANS-C01 uses the same 65-question, 170-minute format as SCS). Use the spare time on policy-reading questions and on the ordering and matching items.
- **Read policies literally.** When a question shows a JSON policy, check `Effect`, `Principal`, `NotAction` and `NotResource`, condition keys (`aws:PrincipalOrgID`, `aws:SourceVpce`, `aws:SecureTransport`, `kms:ViaService`) and whether the statement applies to the bucket or to its objects (`arn:...:bucket` versus `arn:...:bucket/*`).
- **Prefer preventive and automated controls** when the question asks how to stop something happening again: SCPs and RCPs, Config rules with auto-remediation, Firewall Manager. For "investigate", pick detective services and evidence preservation.
- **Ordering items.** Decide the first and last steps first, then fill in the middle.
- **Short names.** The certification page says the exam uses short names for some AWS services, and a list of short and full names is available through the Help button during the exam.
- **Don't over-read "most secure".** If the question also says "least operational overhead", the managed native control usually beats a custom one.
