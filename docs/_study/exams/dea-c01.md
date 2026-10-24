---
code: DEA-C01
title: "AWS Certified Data Engineer – Associate"
credential: "AWS Certified Data Engineer – Associate"
provider: aws
tracks: [cloud]
clouds: [aws]
level: associate
tier: elective
stage: "5"
progress: planned
official_url: https://aws.amazon.com/certification/certified-data-engineer-associate/
study_guide_url: https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html
outline_version: "1.1 (2025-12-12)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. AWS recommends the equivalent of 2-3 years of data engineering experience and at least 1-2 years of hands-on experience with AWS services."
replaces: ""
replaced_by: ""
counterparts: [dp-700]
objectives:
  - { id: "1", title: "Data Ingestion and Transformation", weight: "34%" }
  - { id: "1.1", title: "Perform data ingestion" }
  - { id: "1.1.1", title: "Skill: Read data from streaming sources (for example, Amazon Kinesis, Amazon Managed Streaming for Apache Kafka [Amazon MSK], Amazon DynamoDB Streams, AWS DMS, AWS Glue, Amazon Redshift)" }
  - { id: "1.1.2", title: "Skill: Read data from batch sources (for example, Amazon S3, AWS Glue, Amazon EMR, AWS DMS, Amazon Redshift, AWS Lambda, Amazon AppFlow)" }
  - { id: "1.1.3", title: "Skill: Implement appropriate configuration options for batch ingestion" }
  - { id: "1.1.4", title: "Skill: Consume data APIs" }
  - { id: "1.1.5", title: "Skill: Set up schedulers by using Amazon EventBridge, Apache Airflow, or time-based schedules for jobs and crawlers" }
  - { id: "1.1.6", title: "Skill: Set up event triggers (for example, Amazon S3 Event Notifications, EventBridge)" }
  - { id: "1.1.7", title: "Skill: Call a Lambda function from Kinesis" }
  - { id: "1.1.8", title: "Skill: Create allowlists for IP addresses to allow connections to data sources" }
  - { id: "1.1.9", title: "Skill: Implement throttling and overcoming rate limits (for example, DynamoDB, Amazon RDS, Kinesis)" }
  - { id: "1.1.10", title: "Skill: Manage fan-in and fan-out for streaming data distribution" }
  - { id: "1.1.11", title: "Skill: Describe replayability of data ingestion pipelines" }
  - { id: "1.1.12", title: "Skill: Define stateful and stateless data transactions" }
  - { id: "1.2", title: "Transform and process data" }
  - { id: "1.2.1", title: "Skill: Optimize container usage for performance needs (for example, Amazon EKS, Amazon ECS)" }
  - { id: "1.2.2", title: "Skill: Connect to different data sources (for example, Java Database Connectivity [JDBC], Open Database Connectivity [ODBC])" }
  - { id: "1.2.3", title: "Skill: Integrate data from multiple sources" }
  - { id: "1.2.4", title: "Skill: Optimize costs while processing data" }
  - { id: "1.2.5", title: "Skill: Implement data transformation services based on requirements (for example, Amazon EMR, AWS Glue, Lambda, Amazon Redshift)" }
  - { id: "1.2.6", title: "Skill: Transform data between formats (for example, from .csv to Apache Parquet)" }
  - { id: "1.2.7", title: "Skill: Troubleshoot and debug common transformation failures and performance issues" }
  - { id: "1.2.8", title: "Skill: Create data APIs to make data available to other systems by using AWS services" }
  - { id: "1.2.9", title: "Skill: Define volume, velocity, and variety of data (for example, structured data, unstructured data)" }
  - { id: "1.2.10", title: "Skill: Integrate large language models (LLMs) for data processing" }
  - { id: "1.3", title: "Orchestrate data pipelines" }
  - { id: "1.3.1", title: "Skill: Use orchestration services to build workflows for data ETL pipelines (for example, Lambda, EventBridge, Amazon Managed Workflows for Apache Airflow [Amazon MWAA], AWS Step Functions, AWS Glue workflows)" }
  - { id: "1.3.2", title: "Skill: Build data pipelines for performance, availability, scalability, resiliency, and fault tolerance" }
  - { id: "1.3.3", title: "Skill: Implement and maintain serverless workflows" }
  - { id: "1.3.4", title: "Skill: Use notification services to send alerts (for example, Amazon SNS, Amazon SQS)" }
  - { id: "1.4", title: "Apply programming concepts" }
  - { id: "1.4.1", title: "Skill: Optimize code to reduce runtime for data ingestion and transformation" }
  - { id: "1.4.2", title: "Skill: Configure Lambda functions to meet concurrency and performance needs" }
  - { id: "1.4.3", title: "Skill: Use programming languages and frameworks for data engineering (for example, Python, SQL, Scala, R, Java, Bash, PowerShell)" }
  - { id: "1.4.4", title: "Skill: Use software engineering best practices for data engineering (for example, version control, testing, logging, monitoring)" }
  - { id: "1.4.5", title: "Skill: Use Infrastructure as Code (IaC) to deploy data engineering solutions" }
  - { id: "1.4.6", title: "Skill: Use AWS SAM to package and deploy serverless data pipelines (for example, Lambda functions, Step Functions, DynamoDB tables)" }
  - { id: "1.4.7", title: "Skill: Use and mount storage volumes from within Lambda functions" }
  - { id: "1.4.8", title: "Skill: Use infrastructure as code (IaC) for repeatable resource deployment (for example, AWS CloudFormation and AWS CDK)" }
  - { id: "1.4.9", title: "Skill: Describe continuous integration and continuous delivery (CI/CD) (implementation, testing, and deployment of data pipelines)" }
  - { id: "1.4.10", title: "Skill: Define distributed computing" }
  - { id: "1.4.11", title: "Skill: Describe data structures and algorithms (for example, graph data structures and tree data structures)" }
  - { id: "2", title: "Data Store Management", weight: "26%" }
  - { id: "2.1", title: "Choose a data store" }
  - { id: "2.1.1", title: "Skill: Implement the appropriate storage services for specific cost and performance requirements (for example, Amazon Redshift, Amazon EMR, AWS Lake Formation, Amazon RDS, Amazon DynamoDB, Amazon Kinesis Data Streams, Amazon Managed Streaming for Apache Kafka [Amazon MSK])" }
  - { id: "2.1.2", title: "Skill: Configure the appropriate storage services for specific access patterns and requirements (for example, Amazon Redshift, Amazon EMR, Lake Formation, Amazon RDS, DynamoDB)" }
  - { id: "2.1.3", title: "Skill: Apply storage services to appropriate use cases (for example, using indexing algorithms like Hierarchical Navigable Small Worlds [HNSW] with Amazon Aurora PostgreSQL and using Amazon MemoryDB for fast key/value pair access)" }
  - { id: "2.1.4", title: "Skill: Integrate migration tools into data processing systems (for example, AWS Transfer Family)" }
  - { id: "2.1.5", title: "Skill: Implement data migration or remote access methods (for example, Amazon Redshift federated queries, Amazon Redshift materialized views, Amazon Redshift Spectrum)" }
  - { id: "2.1.6", title: "Skill: Manage locks to prevent access to data (for example, Amazon Redshift, Amazon RDS)" }
  - { id: "2.1.7", title: "Skill: Manage open table formats (for example Apache Iceberg)" }
  - { id: "2.1.8", title: "Skill: Describe vector index types (for example, HNSW, IVF)" }
  - { id: "2.2", title: "Understand data cataloging systems" }
  - { id: "2.2.1", title: "Skill: Use data catalogs to consume data from the data's source" }
  - { id: "2.2.2", title: "Skill: Build and reference a technical data catalog (for example, AWS Glue Data Catalog, Apache Hive metastore)" }
  - { id: "2.2.3", title: "Skill: Discover schemas and use AWS Glue crawlers to populate data catalogs" }
  - { id: "2.2.4", title: "Skill: Synchronize partitions with a data catalog" }
  - { id: "2.2.5", title: "Skill: Create new source or target connections for cataloging (for example, AWS Glue)" }
  - { id: "2.2.6", title: "Skill: Create and manage business data catalogs (for example, Amazon SageMaker Catalog)" }
  - { id: "2.3", title: "Manage the lifecycle of data" }
  - { id: "2.3.1", title: "Skill: Perform load and unload operations to move data between Amazon S3 and Amazon Redshift" }
  - { id: "2.3.2", title: "Skill: Manage S3 Lifecycle policies to change the storage tier of S3 data" }
  - { id: "2.3.3", title: "Skill: Expire data when it reaches a specific age by using S3 Lifecycle policies" }
  - { id: "2.3.4", title: "Skill: Manage S3 versioning and DynamoDB TTL" }
  - { id: "2.3.5", title: "Skill: Delete data to meet business and legal requirements" }
  - { id: "2.3.6", title: "Skill: Protect data with appropriate resiliency and availability" }
  - { id: "2.4", title: "Design data models and schema evolution" }
  - { id: "2.4.1", title: "Skill: Design schemas for Amazon Redshift, DynamoDB, and Lake Formation" }
  - { id: "2.4.2", title: "Skill: Address changes to the characteristics of data" }
  - { id: "2.4.3", title: "Skill: Perform schema conversion (for example, by using AWS SCT and AWS DMS Schema Conversion)" }
  - { id: "2.4.4", title: "Skill: Establish data lineage by using AWS tools (for example, Amazon SageMaker ML Lineage Tracking and Amazon SageMaker Catalog)" }
  - { id: "2.4.5", title: "Skill: Describe best practices for indexing, partitioning strategies, compression, and other data optimization techniques" }
  - { id: "2.4.6", title: "Skill: Describe vectorization concepts (for example, Amazon Bedrock knowledge base)" }
  - { id: "3", title: "Data Operations and Support", weight: "22%" }
  - { id: "3.1", title: "Automate data processing by using AWS services" }
  - { id: "3.1.1", title: "Skill: Orchestrate data pipelines (for example, Amazon Managed Workflows for Apache Airflow [Amazon MWAA], AWS Step Functions)" }
  - { id: "3.1.2", title: "Skill: Troubleshoot Amazon managed workflows" }
  - { id: "3.1.3", title: "Skill: Call SDKs to access Amazon features from code" }
  - { id: "3.1.4", title: "Skill: Use the features of AWS services to process data (for example, Amazon EMR, Amazon Redshift, AWS Glue)" }
  - { id: "3.1.5", title: "Skill: Consume and maintain data APIs" }
  - { id: "3.1.6", title: "Skill: Prepare data for transformation (for example, AWS Glue DataBrew and Amazon SageMaker Unified Studio)" }
  - { id: "3.1.7", title: "Skill: Query data (for example, Amazon Athena)" }
  - { id: "3.1.8", title: "Skill: Use AWS Lambda to automate data processing" }
  - { id: "3.1.9", title: "Skill: Manage events and schedulers (for example, Amazon EventBridge)" }
  - { id: "3.2", title: "Analyze data by using AWS services" }
  - { id: "3.2.1", title: "Skill: Visualize data by using AWS services and tools (for example, DataBrew, Amazon QuickSight)" }
  - { id: "3.2.2", title: "Skill: Verify and clean data (for example, Lambda, Athena, QuickSight, Jupyter Notebooks, Amazon SageMaker Data Wrangler)" }
  - { id: "3.2.3", title: "Skill: Use SQL in Amazon Redshift and Athena to query data or to create views" }
  - { id: "3.2.4", title: "Skill: Use Athena notebooks that use Apache Spark to explore data" }
  - { id: "3.2.5", title: "Skill: Describe tradeoffs between provisioned services and serverless services" }
  - { id: "3.2.6", title: "Skill: Define data aggregation, rolling average, grouping, and pivoting" }
  - { id: "3.3", title: "Maintain and monitor data pipelines" }
  - { id: "3.3.1", title: "Skill: Extract logs for audits" }
  - { id: "3.3.2", title: "Skill: Deploy logging and monitoring solutions to facilitate auditing and traceability" }
  - { id: "3.3.3", title: "Skill: Use notifications during monitoring to send alerts" }
  - { id: "3.3.4", title: "Skill: Troubleshoot performance issues" }
  - { id: "3.3.5", title: "Skill: Use AWS CloudTrail to track API calls" }
  - { id: "3.3.6", title: "Skill: Troubleshoot and maintain pipelines (for example, AWS Glue, Amazon EMR)" }
  - { id: "3.3.7", title: "Skill: Use Amazon CloudWatch Logs to log application data (with a focus on configuration and automation)" }
  - { id: "3.3.8", title: "Skill: Analyze logs with AWS services (for example, Athena, Amazon EMR, Amazon OpenSearch Service, CloudWatch Logs Insights, big data application logs)" }
  - { id: "3.4", title: "Ensure data quality" }
  - { id: "3.4.1", title: "Skill: Run data quality checks while processing the data (for example, checking for empty fields)" }
  - { id: "3.4.2", title: "Skill: Define data quality rules (for example, DataBrew)" }
  - { id: "3.4.3", title: "Skill: Investigate data consistency (for example, DataBrew)" }
  - { id: "3.4.4", title: "Skill: Describe data sampling techniques" }
  - { id: "3.4.5", title: "Skill: Implement data skew mechanisms" }
  - { id: "4", title: "Data Security and Governance", weight: "18%" }
  - { id: "4.1", title: "Apply authentication mechanisms" }
  - { id: "4.1.1", title: "Skill: Update VPC security groups" }
  - { id: "4.1.2", title: "Skill: Create and update IAM groups, roles, endpoints, and services" }
  - { id: "4.1.3", title: "Skill: Create and rotate credentials for password management (for example, AWS Secrets Manager)" }
  - { id: "4.1.4", title: "Skill: Set up IAM roles for access (for example, AWS Lambda, Amazon API Gateway, AWS CLI, AWS CloudFormation)" }
  - { id: "4.1.5", title: "Skill: Apply IAM policies to roles, endpoints, and services (for example, S3 Access Points, AWS PrivateLink)" }
  - { id: "4.1.6", title: "Skill: Describe the differences between managed services and unmanaged services" }
  - { id: "4.1.7", title: "Skill: Use domain, domain units, and projects for SageMaker Unified Studio" }
  - { id: "4.2", title: "Apply authorization mechanisms" }
  - { id: "4.2.1", title: "Skill: Create custom IAM policies when a managed policy does not meet the needs" }
  - { id: "4.2.2", title: "Skill: Store application and database credentials (for example, Secrets Manager, AWS Systems Manager Parameter Store)" }
  - { id: "4.2.3", title: "Skill: Provide database users, groups, and roles access and authority in a database (for example, for Amazon Redshift)" }
  - { id: "4.2.4", title: "Skill: Manage permissions through AWS Lake Formation (for Amazon Redshift, Amazon EMR, Amazon Athena, and Amazon S3)" }
  - { id: "4.2.5", title: "Skill: Apply authorization methods that address business needs (role-based, tag-based, and attribute-based)" }
  - { id: "4.2.6", title: "Skill: Construct custom policies that meet the principle of least privilege" }
  - { id: "4.3", title: "Ensure data encryption and masking" }
  - { id: "4.3.1", title: "Skill: Apply data masking and anonymization according to compliance laws or company policies" }
  - { id: "4.3.2", title: "Skill: Use encryption keys to encrypt or decrypt data (for example, AWS KMS)" }
  - { id: "4.3.3", title: "Skill: Configure encryption across AWS account boundaries" }
  - { id: "4.3.4", title: "Skill: Enable encryption in transit or before transit for data" }
  - { id: "4.4", title: "Prepare logs for audit" }
  - { id: "4.4.1", title: "Skill: Use AWS CloudTrail to track API calls" }
  - { id: "4.4.2", title: "Skill: Use Amazon CloudWatch Logs to store application logs" }
  - { id: "4.4.3", title: "Skill: Use AWS CloudTrail Lake for centralized logging queries" }
  - { id: "4.4.4", title: "Skill: Analyze logs by using AWS services (for example, Athena, CloudWatch Logs Insights, Amazon OpenSearch Service)" }
  - { id: "4.4.5", title: "Skill: Integrate various AWS services to perform logging (for example, Amazon EMR in cases of large volumes of log data)" }
  - { id: "4.5", title: "Understand data privacy and governance" }
  - { id: "4.5.1", title: "Skill: Grant permissions for data sharing (for example, data sharing for Amazon Redshift)" }
  - { id: "4.5.2", title: "Skill: Implement PII identification (for example, Amazon Macie with Lake Formation)" }
  - { id: "4.5.3", title: "Skill: Implement data privacy strategies to prevent backups or replications of data to disallowed AWS Regions" }
  - { id: "4.5.4", title: "Skill: Viewing configuration changes that have occurred in an account (for example, AWS Config)" }
  - { id: "4.5.5", title: "Skill: Maintain data sovereignty" }
  - { id: "4.5.6", title: "Skill: Manage data access through Amazon SageMaker Catalog projects" }
  - { id: "4.5.7", title: "Skill: Describe governance data framework and data sharing patterns" }
---
## Exam format

Every fact below is as of 2026-10-24 and comes from the [certification page](https://aws.amazon.com/certification/certified-data-engineer-associate/) and the [DEA-C01 exam guide](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html). Confirm both before you book.

| Item | Detail (as of 2026-10-24) |
| --- | --- |
| Category | Associate |
| Question types | Multiple choice (one correct answer out of four) and multiple response (two or more correct answers out of five or more options) |
| Number of questions | 65: 50 scored and 15 unscored (the unscored ones are not marked) |
| Duration | 130 minutes |
| Passing score | 720 on a scaled score of 100–1,000. Scoring is compensatory |
| Price | 150 USD (see [exam pricing](https://aws.amazon.com/certification/policies/before-testing/)) |
| Languages | English, Japanese, Korean and Simplified Chinese |
| Delivery | Pearson VUE test centre or online proctored |
| Validity and renewal | Valid for 3 years. You can recertify by passing the latest version of this exam. Unlike several other associate exams, no Professional exam is named as recertifying it (see [recertification](https://aws.amazon.com/certification/recertification/)) |
| Service names | The exam uses short names for some services, and a list is available from the Help button during the exam |

The outline transcribed here is **guide version 1.1, published December 12, 2025**. The [revisions page](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/dea-01-revisions.html) explains that v1.1 merged the old separate "knowledge" and "skills" lists into one numbered skill list per task. It added LLMs in data processing, Apache Iceberg open table formats, vector index types (HNSW, IVF), business catalogs with Amazon SageMaker Catalog, vectorisation with Bedrock Knowledge Bases, and SageMaker Unified Studio domains and projects. It also brought Aurora, Amazon Q, Bedrock, Kendra, AWS Data Exchange and Amazon S3 Tables into scope.

## What the exam really tests

DEA-C01 tests whether you can **build and run data pipelines on AWS**: ingest, transform, store, catalogue, orchestrate, monitor, secure and govern. The guide puts ML training and inference, language-specific syntax and drawing business conclusions out of scope. The four domains:

- **Data Ingestion and Transformation (34%)**: streaming sources (Kinesis Data Streams, Amazon MSK, DynamoDB Streams, DMS) compared with batch sources (S3, Glue, EMR, AppFlow); schedulers and event triggers (EventBridge, Amazon MWAA, S3 Event Notifications); Lambda reading from Kinesis; throttling and rate limits; fan-in and fan-out; replayability. Transformation covers EMR compared with Glue compared with Lambda compared with Redshift, CSV to Parquet, JDBC and ODBC connections, containers on ECS and EKS, data APIs, and **LLM-assisted processing**. Orchestration covers Step Functions, MWAA and Glue workflows. Programming concepts include SQL, IaC (CloudFormation, CDK, SAM), CI/CD for pipelines, Lambda concurrency and storage mounts, and distributed computing.
- **Data Store Management (26%)**: choosing between Redshift, EMR, Lake Formation, RDS, Aurora, DynamoDB and MemoryDB by cost, performance and access pattern; Redshift federated queries, materialised views and Spectrum; locks; Iceberg; vector indexes on Aurora PostgreSQL. Cataloguing covers the Glue Data Catalog, crawlers, partition sync and SageMaker Catalog. Lifecycle covers S3 to Redshift `COPY` and `UNLOAD`, S3 Lifecycle, versioning and DynamoDB TTL. Modelling covers schemas for Redshift and DynamoDB, schema evolution, AWS SCT and DMS Schema Conversion, lineage, partitioning, compression and indexing.
- **Data Operations and Support (22%)**: automating with MWAA, Step Functions, Glue, EMR, Lambda and EventBridge; analysis with Athena (including Spark notebooks), Redshift SQL, Amazon Quick Sight (the guide's skills still write QuickSight), DataBrew and Data Wrangler; provisioned compared with serverless trade-offs; monitoring and auditing with CloudTrail, CloudWatch Logs and Logs Insights, and OpenSearch; data quality rules (DataBrew, Glue Data Quality), sampling and handling data skew.
- **Data Security and Governance (18%)**: IAM roles and policies for pipelines, security groups, Secrets Manager and Parameter Store, Redshift database permissions, **Lake Formation permissions** across Redshift, EMR, Athena and S3, RBAC, tag-based and attribute-based access, masking and anonymisation, KMS including cross-account encryption, CloudTrail Lake, Macie for PII, preventing replication to disallowed Regions, Redshift data sharing, SageMaker Unified Studio domains and projects, and SageMaker Catalog projects.

The scenarios read like real pipeline tickets: data arrives in this form at this rate, here are the latency, cost and governance needs, so choose the ingestion, store and transformation. Candidates lose points on **service-choice pairs** (Kinesis Data Streams compared with Amazon Data Firehose; Glue compared with EMR; Athena compared with Redshift Spectrum compared with Redshift; MWAA compared with Step Functions), **file and partition performance** (columnar formats, partition pruning, the small-files problem), and **Lake Formation compared with plain IAM and S3 bucket policies** for fine-grained access.

## Study strategy

1. **Foundations first.** S3 as the data lake (prefixes, partitions, storage classes, lifecycle), IAM roles for services, and SQL. Then the Glue Data Catalog, because Athena, Redshift Spectrum, EMR and Lake Formation all depend on it.
2. **Build one batch lake and one stream.**
    - *Batch*: land CSV files in S3, crawl them with Glue, use a Glue job to convert them to partitioned Parquet (or an Iceberg table), query with Athena, load a subset into Redshift Serverless with `COPY`, apply Lake Formation column-level permissions, orchestrate with Step Functions or MWAA, and add a Glue Data Quality ruleset.
    - *Stream*: Kinesis Data Streams to Lambda, then Firehose to S3, with a CloudWatch alarm on iterator age.
3. **Then the 2025–2026 additions**: SageMaker Unified Studio and SageMaker Catalog, vector indexes (HNSW compared with IVF), Bedrock Knowledge Bases as a consumer of the lake, and calling an LLM in a transformation step.
4. **Official resources**: the Exam Prep Plan on [AWS Skill Builder](https://skillbuilder.aws/) (the Official Practice Question Set, the Official Pretest, exam-prep courses, AWS Builder Labs, AWS Cloud Quest, AWS Jam, AWS SimuLearn and the Official Practice Exam); the [exam guide](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/data-engineer-associate-01.html) and its [in-scope services](https://docs.aws.amazon.com/aws-certification/latest/data-engineer-associate-01/dea-01-in-scope-services.html) list. The certification page also lists the related AWS Data Streaming, Data Lakehouse and Data Visualization *Demonstrated* credentials, which are hands-on.
5. **How your background helps or misleads.** Your **.NET and SQL** experience helps with the SQL and programming-concept items. **AZ-204** helps with event-driven triggers and Cosmos DB, which maps to DynamoDB and its Streams. **AZ-900** has little data-engineering depth. If you later study DP-700, note that Microsoft Fabric bundles lakehouse, warehouse, pipelines, notebooks and governance into one SaaS product with OneLake. On AWS the same job is spread across S3, Glue, Athena, Redshift, EMR, Lake Formation and SageMaker Unified Studio, and the exam is largely about **choosing among them**. Don't assume one tool does everything.

This is a stage 5 elective. Take it after SAA-C03, when your path turns to data for AI. It also gives useful groundwork for MLA-C02's data-preparation domain (28%).

## Differences from related exams

- **DEA-C01 compared with DP-700 (Fabric Data Engineer Associate, the closest Azure counterpart).** Both test ingesting, transforming, storing, securing and monitoring data at associate level. DP-700 is **one platform** (Fabric: lakehouses, warehouses, Data Factory pipelines, notebooks, eventstreams, OneLake security) and asks how to configure that platform. DEA-C01 is **many services**, and most questions ask which one to use and how to connect it to the others, plus AWS-specific governance (Lake Formation, Macie, KMS across accounts). DP-700 expects more hands-on detail with KQL, PySpark and T-SQL in Fabric. DEA-C01 stays language-neutral.
- **DEA-C01 compared with SAA-C03.** SAA's Task 3.5 (data ingestion and transformation) is a thin slice of DEA. DEA goes into partitioning, catalogues, data quality, Redshift internals and Lake Formation permissions, which SAA never touches.
- **DEA-C01 compared with MLA-C02.** MLA picks up where DEA stops. Its data domain covers feature engineering, Feature Store, labelling, bias and preparing data for RAG and fine-tuning, and it goes on to training, deployment and MLOps. DEA explicitly excludes ML training and inference.
- **DEA-C01 compared with DP-600 and DP-900.** DP-900 is a data fundamentals exam, well below DEA's depth. DP-600 (Fabric Analytics Engineer) is about semantic models and analytics, closer to DEA's analysis tasks than its pipeline tasks.

## Exam-day notes

- You have 65 questions in 130 minutes. Many stems are long and list several requirements at once (latency, volume, cost, "serverless", "least operational overhead"). List them before you look at the options.
- Traps: Firehose is near-real-time delivery and is not a store you can replay from (choose Kinesis Data Streams or MSK when you need replay and multiple consumers); Athena query cost depends on bytes scanned, so the fix is Parquet or ORC plus partitions plus compression; Glue crawlers infer schemas but do not enforce data quality; Lake Formation grants sit on top of IAM, and both must allow access; Redshift `COPY` from many compressed files is faster than one large file; DynamoDB TTL deletions are asynchronous and not instant.
- "Least operational overhead" usually points to serverless (Glue, Athena, Redshift Serverless, Step Functions) over EMR on EC2, unless the stem needs custom Spark or Hadoop tuning or long-running clusters.
- Flag the questions you are unsure of and come back to them. Never leave a question blank.
