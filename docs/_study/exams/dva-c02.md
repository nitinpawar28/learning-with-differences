---
code: DVA-C02
title: "AWS Certified Developer – Associate"
credential: "AWS Certified Developer – Associate"
provider: aws
tracks: [cloud]
clouds: [aws]
level: associate
tier: skip
stage: ""
progress: planned
official_url: https://aws.amazon.com/certification/certified-developer-associate/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/developer-associate-02/developer-associate-02.html
outline_version: "n/a"
last_verified: 2026-10-24
retires_on: 2026-11-30
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends 1 or more years of hands-on experience developing and maintaining applications on AWS."
replaces: ""
replaced_by: "dva-c03"
counterparts: [az-204]
objectives: []
---
## Why this is catalogue only

As of 2026-10-24 the [certification page](https://aws.amazon.com/certification/certified-developer-associate/) says DVA-C02 can be taken until November 30, 2026. Registration for DVA-C03 opens October 27, 2026. The current exam has 65 multiple-choice or multiple-response questions in 130 minutes and costs 150 USD.

With about five weeks left, preparing for the retiring version is a poor investment. Study for DVA-C03 instead (see its page in this library). Its syllabus follows the same development role: Lambda, API Gateway, DynamoDB, SQS, SNS and EventBridge, IAM for applications, the SDKs, deployment with CodePipeline and SAM, and troubleshooting with CloudWatch and X-Ray.

## Differences from related exams

- **DVA-C02 vs DVA-C03.** They test the same role. Use the DVA-C03 exam guide for the current domain weights and service list.
- **DVA-C02 vs AZ-204.** They are the closest match across clouds. Both test serverless compute, NoSQL storage, messaging, identity for applications and monitoring, at the level of SDK calls and configuration. Your AZ-204 preparation maps closely: Functions to Lambda, Cosmos DB to DynamoDB, Service Bus to SQS and SNS, managed identities to IAM roles, and Application Insights to CloudWatch and X-Ray. Watch for the differences, such as DynamoDB key design and capacity modes, and Lambda concurrency limits.
- **DVA-C02 vs SAA-C03.** SAA-C03 asks which services to use. DVA-C02 asks how your code calls them, how errors and retries are handled, and how the code is packaged and deployed.
