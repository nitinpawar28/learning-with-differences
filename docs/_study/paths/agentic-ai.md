---
title: "Agentic AI: from AI-901 to AI-103, MCPA and AIP-C01"
summary: "The agentic-AI route: model and retrieval fundamentals, then agents, the Model Context Protocol and the Microsoft Foundry and Amazon Bedrock platforms."
tracks: [agentic-ai, security]
level: practitioner
exams: [ai-901, aif-c01, ai-103, mcpa, aip-c01]
status: draft
steps:
  - page: ai/index.md
    note: The area map; AI security lives in the security area and is linked from here.
  - objective: ai-901:1
  - objective: aif-c01:1
  - page: ai/protocols/mcp-tool-orchestration.md
    note: Still a stub; it will be rewritten for the stateless 2026-07-28 revision of MCP.
  - term: server-sent-events
  - term: websocket
  - check: An agent streams model tokens to a browser and also needs the browser to interrupt the run. Which transport fits each direction, and why is SSE alone not enough?
  - term: oauth-authorization-code-flow
  - term: oauth-client-credentials-flow
  - term: capability-based-authorization
  - term: wasm-sandboxing
  - term: container-isolation
  - check: A tool server runs third-party tools on behalf of many users. Which authorization model and which sandbox would you pick for it, and what does each protect against?
  - objective: mcpa:1
  - objective: ai-103:1
  - objective: aip-c01:1
  - check: Compare Microsoft Foundry Agent Service with Amazon Bedrock AgentCore for hosting the same agent. Name three differences that would change your design.
---
This path is for the agentic-AI role. It assumes the foundations exams come
first, then builds the protocol and security knowledge an agent platform
needs before the platform-specific exams. The capstone for this path is the
MCP server over this library's own glossary, in [Practice](../../practice/index.md).
