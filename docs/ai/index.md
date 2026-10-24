---
title: "Agentic AI"
description: "AI foundations, applied generative AI, evaluation, agents, agent protocols and the Microsoft Foundry and Amazon Bedrock platforms."
---

# Agentic AI

From how a language model turns tokens into text, to how a fleet of agents is
identified, authorised, evaluated and governed in production. Each topic is
compared with its neighbours: RAG vs. fine-tuning, an agent vs. a workflow,
MCP vs. A2A, Microsoft Foundry Agent Service vs. Amazon Bedrock AgentCore.

| Domain | Focus |
|---|---|
| AI foundations | Machine learning basics, transformers, tokens, embeddings, context windows, model families and selection |
| Applied generative AI | Prompt and context engineering, structured outputs, tool calling, retrieval-augmented generation (RAG) |
| Evaluation and operations | Offline and online evaluation, LLM-as-judge, groundedness, cost, latency, quotas, model routing, OpenTelemetry tracing |
| Agents | The agent loop, ReAct, planning and reflection, memory, human-in-the-loop, durable execution, multi-agent patterns, frameworks |
| Agent protocols | The Model Context Protocol (current revision 2026-07-28) and Agent2Agent (A2A) |
| AI platforms | Microsoft Foundry and Foundry Agent Service; Amazon Bedrock and Bedrock AgentCore |

AI security (prompt injection, the OWASP Top 10 lists for LLM and agentic
applications, MITRE ATLAS, guardrails and AI governance) lives in
[Security](../security/index.md), because it is shared by both roles.

## Exams this area prepares for

AI-901, AI-103, AI-500 and AI-200 (Azure); AIF-C01 and AIP-C01 (AWS); and
MCPA (Model Context Protocol Associate). See [Exams](../study/exams.md).

## Already in the library

- [MCP Tool Orchestration](protocols/mcp-tool-orchestration.md) (stub, to be
  rewritten for the stateless 2026-07-28 revision of the protocol and its
  Streamable HTTP transport)

!!! note "Coming in waves"
    AI foundations arrive with the foundations wave. Everything else arrives
    with the agentic AI wave, which also includes the capstone of building an
    MCP server over this library's own glossary. Track progress in the
    [content roadmap](../study/reports/roadmap.md).
