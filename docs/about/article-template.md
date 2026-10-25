---
title: "Templates and conventions"
description: "The authoring standard for every page type in the library: front matter, required sections, tabs, links, sources and depth targets."
---

# Templates and conventions

Every page in this library follows one standard, so that any page can be read
on its own. A reader who lands on it from search should never need to have read
something else first. This page sets out that standard. Glossary terms have
their own schema, described in the [engine notes](engine.md); everything below
applies to the pages under `docs/<area>/`.

## Rules for every page

- **Self-explanatory.** Define every technical term the first time it is used,
  or link it to its glossary page. Say what the reader should already know in
  the *Before you start* box.
- **Taught by difference.** Each concept is explained against its nearest
  neighbours and against its counterpart on the other cloud. A page that only
  describes one thing has missed the point of the library.
- **Grounded.** Every claim about cloud behaviour, limits, defaults, prices or
  availability links a primary source: Microsoft Learn, AWS documentation,
  NIST, OWASP, IETF RFCs, the Kubernetes docs, modelcontextprotocol.io, or the
  original paper or standard. Blogs and vendor marketing are never the only
  source. Put the date of a limit or price next to it ("as of 2026-10").
- **Original.** Write in your own words. Never copy documentation text. Never
  reproduce real exam questions; practice questions are original scenarios.
- **Public.** The site is published. Never include internal hostnames, keys,
  account ids, customer data or anything else about a real production
  environment. Use placeholders such as `contoso`, `example.com`, `10.0.0.0/16`
  and `123456789012`.
- **Current.** Use today's product names; give the old name once, in
  parentheses, when a product was renamed (for example "Microsoft Entra ID
  (formerly Azure Active Directory)").

## Front matter

```yaml
---
title: "Amazon VPC fundamentals: subnets, route tables, gateways and security groups"
description: "One sentence on what the reader will be able to do or decide after reading."
status: complete            # stub | draft | complete | deprecated
level: foundation           # foundation | practitioner | expert
tracks: [cloud, security]   # architect | agentic-ai | security | cloud; the first is the primary track
clouds: [aws]               # [] for vendor-neutral, [azure], [aws] or [azure, aws]
compares: [vpc, vnet]       # optional: glossary term slugs this page contrasts
covers:                     # exam objectives this page teaches (ids from docs/_study/exams/<exam>.md)
  - clf-c02:3.4
  - { ref: "saa-c03:1.1", depth: partial }
last_verified: 2026-10-25   # required for complete cloud and AI pages
tags: [networking]          # optional
---
```

- `covers` is what drives the exam coverage reports. Use the most specific
  objective id that the page genuinely teaches. Mark it `depth: partial` when
  the page covers only part of that objective. Never pad the list.
- `status: complete` means every required section is present and every factual
  claim has been checked against a primary source on `last_verified`.
- Unknown keys are reported by `python -m lwd validate`.

## Markdown conventions

**Linked tabs.** A choice made in one tab group applies to every group with the
same labels on the page, so use exactly these labels:

- code: `=== "C#"` and `=== "Python"` (.NET 10 and Python 3.12 or later);
- providers: `=== "Azure"` and `=== "AWS"`;
- infrastructure as code: `=== "Bicep"`, `=== "CloudFormation"`, `=== "CDK"`
  and `=== "Terraform"`;
- command lines: `=== "Azure CLI"`, `=== "PowerShell"` and `=== "AWS CLI"`.

Tab content is indented by four spaces:

````markdown
=== "C#"

    ```csharp
    await using var client = new ServiceBusClient(fqdn, new DefaultAzureCredential());
    ```

=== "Python"

    ```python
    client = ServiceBusClient(fqdn, credential=DefaultAzureCredential())
    ```
````

**Diagrams.** Use Mermaid in a ` ```mermaid ` fence: `flowchart`,
`sequenceDiagram`, `stateDiagram-v2`, `classDiagram` or `erDiagram`. Every
diagram has a sentence before it saying what it shows.

**Admonitions.** Use `!!! abstract`, `!!! info`, `!!! tip`, `!!! warning` and
`!!! danger`. Self-check questions use `??? question "…"` blocks, which
collapse, with the answer indented by four spaces.

**Links.**

- Link with relative paths to `.md` files, never to site URLs. From
  `cloud/aws/networking/amazon-vpc-fundamentals.md`, the glossary page for VPC
  is `../../../terms/vpc.md`, and a sibling article is
  `amazon-ec2-fundamentals.md`.
- Never link into a folder that starts with an underscore.
- Use explicit heading ids only in lowercase: `## Limits { #limits }`.
- `python -m lwd validate` checks every link and anchor.

**Acronyms.** Acronyms that have a glossary term get a hover tooltip
automatically. Write the full name the first time anyway: "virtual private
cloud (VPC)".

## Concept article

A concept article explains a vendor-neutral idea, or one provider's service, in
depth. Target length: 2,500 to 6,000 words.

````markdown
# Title

!!! abstract "In this article"
    - **You will learn:** three to five concrete outcomes.
    - **Before you start:** the pages or terms to read first, as links.
    - **Exams:** the exams and domains this serves, e.g. CLF-C02 domain 3, SAA-C03 domain 1.

## Overview
The problem this exists to solve, the mental model (a diagram or an analogy), and where it shows up in a real system.

## How it works
The mechanics, step by step, with a diagram. Define every moving part.

## Azure and AWS
Linked "Azure" and "AWS" tabs: the service names, the resource model, how you create and configure it (portal concepts, CLI, IaC), and SDK code in "C#" and "Python" tabs.
(Vendor-neutral articles map the concept onto both providers here. A page about one provider's service shows that provider, then a short "On the other cloud" section naming the counterpart and how closely it matches.)

## Differences that matter
A table and prose: this concept against its nearest neighbours, and Azure against AWS. Say which difference changes a design decision.

## Design guidance
How to choose and configure it well, with the anti-patterns that cost teams later in a `!!! warning` box.

## Security
Identity, network exposure, encryption, logging, and the misconfigurations seen most often.

## Reliability, performance and cost
Failure modes, scaling behaviour, and the cost drivers, with numbers where a source gives them.

## Limits and quotas
The limits that affect design, each dated and linked to the provider's limits page.

## Troubleshooting
Symptom, likely cause and how to confirm it, as a table or a list.

## Exam focus
For each exam in `covers`: what it tests on this topic, the distractors, and the traps.

## Hands-on
A link to the lab that exercises this page, or the shortest safe way to try it yourself, including the clean-up step.

## Self-check
Five to ten `??? question` blocks of scenario questions, with the reasoning in each answer.

## References
Primary sources first, then the related library pages and glossary terms.
````

The sections may be renamed slightly when the topic calls for it; *Overview*,
*How it works*, *Differences that matter*, *Exam focus*, *Self-check* and
*References* are always present.

## Cloud-compare article

A compare article lives under `cloud/compare/` and puts one capability on Azure
and AWS side by side. Target length: 2,500 to 5,000 words. It uses the concept
article's summary box, then:

1. **The short answer:** a fidelity rating (exact, close, partial or none) and
   the mapping in one table: Azure service, AWS service, fidelity, the one
   difference that matters.
2. **Concept model differences:** how each provider models the capability:
   scopes, resource hierarchy, naming, defaults.
3. **Identity and access differences.**
4. **Networking and data residency differences.**
5. **Limits and pricing:** dated and linked.
6. **Porting gotchas:** what breaks when you move a design from one cloud to
   the other.
7. **IaC side by side:** the same resource in Bicep, CloudFormation or CDK,
   and Terraform tabs.
8. **Exam focus**, **Self-check** and **References**, as for a concept article.

## Lab

A lab lives under `practice/labs/` and is runnable from start to finish on both
clouds unless its title says otherwise.

1. **Objective:** what you will build, and the skill it proves.
2. **Architecture:** a diagram of the end state.
3. **Cost and guardrails:** the expected cost, the free-tier notes, the budget
   alert to set first, and how long the resources may stay up.
4. **Prerequisites:** accounts, CLI versions, permissions.
5. **Steps:** in "Azure" and "AWS" tabs. Every command is complete and can be
   pasted as it stands; every step says what you should see.
6. **Verify:** commands that prove the result.
7. **Break it:** one or two deliberate faults to diagnose and fix.
8. **Teardown:** the commands that delete everything, and how to confirm that
   nothing billable is left.
9. **Reflect:** questions that connect the lab to the concept pages.

## Kata, threat model and tabletop

Practice pages under `practice/katas/`, `practice/threat-models/` and
`practice/tabletops/` share one shape:

1. **Scenario:** the system, the organisation and the pressure on it.
2. **Constraints:** budget, compliance, team size, deadlines.
3. **Deliverables:** what to produce (a diagram, an ADR, a threat list, a
   decision log).
4. **Hints:** in a collapsed `??? tip` block.
5. **Rubric:** what a strong answer contains.
6. **Model answer:** in a collapsed `??? success "Model answer"` block.

A threat model uses STRIDE or LINDDUN where they fit and names the
mitigations on both clouds. A tabletop runs as timed injects, each with the
decisions the team must make.

## Capstone

A capstone under `practice/capstones/` combines several waves of work into one
system designed on both clouds. Add these sections to the kata shape:
milestones, C4 diagrams, ADRs, a cost model, and a Well-Architected review for
each cloud.
