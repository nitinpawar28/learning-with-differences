---
title: "Cloud: Azure and AWS"
description: "Cloud foundations, then Azure and AWS across twelve matched capabilities, with the differences spelled out for each."
---

# Cloud: Azure and AWS

The fastest way to learn a second cloud is through its differences from the
first. This area covers both providers along the **same twelve capabilities**,
so every Azure page has an AWS counterpart and a comparison page between them.

| # | Capability | Azure examples | AWS examples |
|---|---|---|---|
| 1 | Identity | Microsoft Entra ID, managed identities, Azure RBAC | IAM, IAM Identity Center, STS |
| 2 | Governance and landing zones | Management groups, Azure Policy, Azure landing zones | Organizations, SCPs/RCPs, Control Tower |
| 3 | Networking | VNets, NSGs, Private Endpoint, Front Door | VPCs, security groups, PrivateLink, CloudFront |
| 4 | Compute | Virtual Machines, scale sets | EC2, Auto Scaling |
| 5 | Containers | AKS, Container Apps | EKS, ECS, Fargate |
| 6 | Serverless and integration | Functions, Logic Apps, Service Bus, Event Grid | Lambda, Step Functions, SQS, EventBridge |
| 7 | Storage and data | Blob Storage, Azure SQL, Cosmos DB | S3, RDS/Aurora, DynamoDB |
| 8 | Observability | Azure Monitor, Log Analytics, Application Insights | CloudWatch, X-Ray, CloudTrail |
| 9 | Security services | Defender for Cloud, Sentinel, Key Vault | Security Hub, GuardDuty, KMS |
| 10 | IaC and DevOps | ARM, Bicep, Azure DevOps | CloudFormation, CDK, SAM |
| 11 | Cost management | Cost Management, reservations, savings plans | Cost Explorer, Budgets, Savings Plans |
| 12 | AI services | Microsoft Foundry (see [AI](../ai/index.md)) | Amazon Bedrock (see [AI](../ai/index.md)) |

The matches in that table are rarely exact. The [Rosetta](../glossary/rosetta.md)
rates every pair, and the comparison pages explain where the models differ.
For example, an AWS account is an identity, security and billing boundary,
whereas Azure identities live in a Microsoft Entra tenant that spans
subscriptions.

## Exams this area prepares for

AZ-900 (held), AZ-104, AZ-305 and AI-200 on Azure; CLF-C02, SAA-C03 and
SAP-C03 on AWS. Start with the [exam roadmap](../study/exams.md).

!!! note "Coming in waves"
    Cloud foundations arrive with the foundations wave. Both providers' core
    capabilities and the comparison pages arrive together in the cloud
    associate wave, one capability at a time. Track progress in the
    [content roadmap](../study/reports/roadmap.md).
