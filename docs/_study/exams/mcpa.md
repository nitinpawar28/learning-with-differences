---
code: MCPA
title: "Model Context Protocol Associate"
credential: "Model Context Protocol Associate (MCPA)"
provider: linux-foundation
tracks: [agentic-ai, architect]
clouds: [neutral]
level: beginner
tier: core
stage: "3"
progress: planned
official_url: https://training.linuxfoundation.org/certification/model-context-protocol-associate-mcpa/
study_guide_url: https://training.linuxfoundation.org/certification/model-context-protocol-associate-mcpa/
outline_version: "MCP 2026-07-28"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "None required. The exam page recommends familiarity with JSON-RPC or similar message protocols, LLM APIs, agentic AI concepts (tool use, ReAct), basic security (API keys, OAuth 2.1, tokens) and reading MCP server manifests and capability definitions."
replaces: ""
replaced_by: ""
counterparts: []
objectives:
  - { id: "1", title: "MCP Fundamentals", weight: "16%" }
  - { id: "1.1", title: "MCP purpose and scope" }
  - { id: "1.2", title: "Core MCP concepts" }
  - { id: "1.3", title: "Interoperability and value" }
  - { id: "2", title: "Architecture and Components", weight: "14%" }
  - { id: "2.1", title: "Schemas and structured data" }
  - { id: "2.2", title: "MCP hosts, clients and servers" }
  - { id: "2.3", title: "Model interaction flow" }
  - { id: "3", title: "Interactions and Execution", weight: "26%" }
  - { id: "3.1", title: "Interaction patterns and response handling" }
  - { id: "3.2", title: "Error handling" }
  - { id: "3.3", title: "Tool invocation lifecycle" }
  - { id: "3.4", title: "Protocol primitives" }
  - { id: "4", title: "Security and Governance", weight: "24%" }
  - { id: "4.1", title: "Trust boundaries" }
  - { id: "4.2", title: "Permissions and consent" }
  - { id: "4.3", title: "Risk and safety controls" }
  - { id: "4.4", title: "Auditability and observability" }
  - { id: "5", title: "Use Cases and Ecosystem", weight: "20%" }
  - { id: "5.1", title: "Roles, responsibilities and adoption" }
  - { id: "5.2", title: "Operational use cases" }
  - { id: "5.3", title: "Ecosystem and portability" }
---
## Exam format

MCPA is the first certification from the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation to which Anthropic donated the Model Context Protocol in December 2025 ([Anthropic announcement](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)). It was announced on 2026-09-14 ([press release](https://www.linuxfoundation.org/press/agentic-ai-foundation-launches-mcpa-certification-to-validate-mcp-expertise)) and is delivered through Linux Foundation Training. All facts below are as of 2026-10-24, from the [MCPA exam page](https://training.linuxfoundation.org/certification/model-context-protocol-associate-mcpa/) and the Linux Foundation [multiple-choice exam FAQ](https://docs.linuxfoundation.org/tc-docs/certification/faq-mc).

- **Question type:** multiple choice, online, proctored.
- **Number of questions:** not published.
- **Duration:** 90 minutes on the exam page (the FAQ also gives 90 minutes for all Linux Foundation multiple-choice exams except CNPA). The launch press release said 120 minutes. Trust the exam page and check it again when you book.
- **Passing score:** not stated on the exam page. The FAQ sets 75% for Linux Foundation multiple-choice exams.
- **Specification:** aligned with the MCP specification release **2026-07-28**.
- **Price:** USD 250 for the exam alone, or USD 495 bundled with a THRIVE-ONE annual subscription. One retake is included. The exam page says buying through an AAIF conference saves 20%.
- **Languages:** English only, per the Linux Foundation [language table](https://docs.linuxfoundation.org/tc-docs/certification/lf-handbook2/language).
- **Results:** scored automatically and emailed within 24 hours (FAQ).
- **Eligibility and renewal:** 12 months to schedule and sit after purchase. Valid for 2 years, and you renew by passing the exam again before it expires (FAQ).
- **Outline detail:** the exam page lists five domains with two to four topic headings each. There is no separate curriculum PDF, so the objectives above are those headings. No finer bullets have been published.

The exam is new, and the specification moves quickly. Confirm the duration, the spec version and the price before booking.

## What the exam really tests

MCPA tests whether you understand how MCP works as a protocol and how to use it safely. It is not a coding exam, but the questions assume you can read JSON-RPC messages, tool definitions and capability declarations and say what they mean.

- **Fundamentals (16%).** What MCP is for: a standard way for AI applications to connect to tools, data and prompts, replacing one-off integrations between each model client and each system (the "N times M" problem). Its scope (what the protocol defines and what it leaves to hosts and servers) and why interoperability across vendors matters.
- **Architecture and components (14%).** The host (the AI application the user runs), the clients it creates (one per server connection) and the servers that expose capabilities. JSON-RPC 2.0 messages, JSON Schema 2020-12 `inputSchema` and `outputSchema`, and `structuredContent`. The transports (stdio for local servers, Streamable HTTP for remote ones) and how a model's request flows from host to client to server and back.
- **Interactions and execution (26%, the largest domain).** The server primitives (tools, resources, prompts) and their list, read, get and call methods. The tool-invocation lifecycle: discovery, the model choosing a tool, the host asking for consent, the call, the result. Result handling, including `resultType` and the new Multi Round-Trip Request pattern, error handling (JSON-RPC protocol errors versus tool results flagged as errors, and the spec's error-code ranges), notifications and progress, and caching hints.
- **Security and governance (24%).** Trust boundaries between user, host, model and server; why tool descriptions and tool output are untrusted input (prompt injection, tool poisoning, "rug pull" changes to tool definitions); user consent and human-in-the-loop approval; least privilege and scoped access; authorization for remote servers with OAuth 2.1 (protected resource metadata, resource indicators, issuer validation, Client ID Metadata Documents); token handling (no token passthrough, audience checks); audit logging and observability, including OpenTelemetry trace context in `_meta`.
- **Use cases and ecosystem (20%).** Who does what (protocol maintainers, server authors, host builders, platform and governance teams), how organisations adopt MCP, typical operational uses (coding assistants, internal data access, operations automation) and portability of servers across hosts and model providers.

**The specification changed a lot in 2026-07-28, and this is the biggest risk for anyone who learned MCP earlier.** According to the [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog), compared with 2025-11-25:

- The protocol is now **stateless**. The `initialize` / `notifications/initialized` handshake and the `Mcp-Session-Id` header are gone. Every request carries its protocol version and client capabilities in `_meta`, and servers must implement a new `server/discover` method.
- Server-initiated requests (sampling, elicitation, roots) are replaced by the **Multi Round-Trip Requests** pattern: the server returns an `input_required` result and the client retries the original request with the answers.
- `resources/subscribe` and the HTTP GET stream are replaced by `subscriptions/listen`. `ping` and `logging/setLevel` are removed, and SSE resumability is removed.
- **Tasks** moved out of the core into an official extension.
- **Roots, Sampling and Logging are deprecated.** The old HTTP+SSE transport and OAuth Dynamic Client Registration are formally deprecated in favour of Streamable HTTP and Client ID Metadata Documents.

Tutorials, SDK samples and blog posts from 2025 describe the older handshake-based model. Where they disagree with the 2026-07-28 specification, the specification wins for this exam.

## Study strategy

1. **Foundations first.** JSON-RPC 2.0 (request, response, notification, error object), JSON Schema basics, and the LLM tool-calling loop (the model proposes a call, the application runs it and returns the result). If agent concepts are new, learn ReAct-style tool use before MCP itself.
2. **Read the specification, not summaries.** Start at the [MCP introduction](https://modelcontextprotocol.io/), then read the [2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28) in this order: overview and architecture, base protocol and lifecycle, transports, server features (tools, resources, prompts), the MRTR pattern, authorization, and the security best-practices page. Finish with the changelog and the deprecated-features registry.
3. **Build one server and connect it to one host.** Use an official SDK (the C# SDK suits a .NET developer; TypeScript and Python are the most documented). Expose one tool, one resource and one prompt, then watch the raw messages in the MCP Inspector. Seeing the JSON makes the interactions domain concrete.
4. **Add a remote transport and authorization.** Run the same server over Streamable HTTP behind OAuth, and follow the discovery steps (protected resource metadata, then authorization server metadata).
5. **Study security as its own subject.** It is almost a quarter of the exam. Write down, for each trust boundary, what can go wrong and what control applies.

Official learning resources: the exam page links the MCP introduction, the 2026-07-28 specification, AAIF community blog posts and the THRIVE-ONE subscription. No dedicated Linux Foundation course for MCPA is linked as of 2026-10-24.

How your background helps or misleads:

- **.NET and Angular** experience makes JSON, HTTP, async request handling and schemas familiar. OAuth flows from web apps carry over directly to MCP authorization.
- **AZ-204 preparation** (Microsoft identity platform, managed identities, API Management) helps with the authorization and gateway concepts. Do not assume Azure-specific behaviour. MCP is vendor-neutral, and the exam will not ask about Azure services.
- **Experience with function calling in one model provider's API** helps with the tool lifecycle, but MCP sits between the host and external servers, not between your code and the model. Keep the two layers apart.

## Differences from related exams

- **MCPA vs cloud AI fundamentals (AIF-C01, AI-901).** Those cover AI and generative-AI concepts and their vendor's services broadly. MCPA is about one open protocol, in protocol-level detail, with no vendor services.
- **MCPA vs cloud AI developer and agent exams (AI-103, AIP-C01).** Those test building AI solutions on Microsoft Foundry or Amazon Bedrock, where MCP may appear as one integration option. MCPA tests the protocol itself: message shapes, primitives, lifecycle and security model.
- **MCPA vs KCNA and KCSA.** Same Linux Foundation multiple-choice format, price band and 90-minute length. KCSA's habit of thinking in trust boundaries and threat models transfers well to MCPA's security domain.
- **MCPA vs general security exams (CompTIA Security+, CCSK).** Those are broad. MCPA's security domain is narrow and specific to agents: prompt injection through tool output, consent, token audience and confused-deputy problems.

## Exam-day notes

- **Time:** 90 minutes. Answer everything on a first pass, flag the uncertain ones, then return.
- **Answer for the 2026-07-28 spec.** If an option mentions the `initialize` handshake, sessions, or server-initiated sampling as current behaviour, it is probably describing an older version.
- **Know who does what.** Many questions turn on whether something is the host's, the client's or the server's job. Consent and showing tool calls to the user are host responsibilities. Validating inputs and enforcing access are server responsibilities.
- **Traps:** a tool error reported inside a successful result is not a JSON-RPC error; tool annotations and descriptions are hints, not trusted security guarantees; a server must not pass the client's token through to an upstream API.
