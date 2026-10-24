---
code: CLAUDE-ARCH-F
title: "Claude Certified Architect – Foundations"
credential: "Claude Certified Architect – Foundations"
provider: anthropic
tracks: [agentic-ai, architect]
clouds: [neutral]
level: foundation
tier: elective
stage: "3"
progress: planned
official_url: https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification
study_guide_url: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf
outline_version: "Exam Guide version 1.0, effective July 2026 (exam code CCAR-F)"
last_verified: 2026-10-24
retires_on:
provisional: false
prerequisites: []
prerequisites_any: []
prerequisite_note: "Only people at organizations in the Claude Partner Network can register (membership is free for firms; register with a company email on a domain in the partner record). No mandatory prerequisite; Anthropic recommends 6+ months of hands-on work with the Claude API, Agent SDK, Claude Code and MCP."
replaces: ""
replaced_by: ""
counterparts: [ai-103, aip-c01, gh-600, ncp-aai, paa]
objectives:
  - { id: "1", title: "Agentic Architecture & Orchestration", weight: "27%" }
  - { id: "1.1", title: "Design and implement agentic loops for autonomous task execution" }
  - { id: "1.1.1", title: "Knowledge: The agentic loop lifecycle: sending requests to Claude, inspecting stop_reason (\"tool_use\" vs \"end_turn\"), executing requested tools, and returning results for the next iteration" }
  - { id: "1.1.2", title: "Knowledge: How tool results are appended to conversation history so the model can reason about the next action" }
  - { id: "1.1.3", title: "Knowledge: The distinction between model-driven decision-making (Claude reasons about which tool to call next based on context) and pre-configured decision trees or tool sequences" }
  - { id: "1.1.4", title: "Skill: Implementing agentic loop control flow that continues when stop_reason is \"tool_use\" and terminates when stop_reason is \"end_turn\"" }
  - { id: "1.1.5", title: "Skill: Adding tool results to conversation context between iterations so the model can incorporate new information into its reasoning" }
  - { id: "1.1.6", title: "Skill: Avoiding anti-patterns such as parsing natural language signals to determine loop termination, setting arbitrary iteration caps as the primary stopping mechanism, or checking for assistant text content as a completion indicator" }
  - { id: "1.2", title: "Orchestrate multi-agent systems with coordinator-subagent patterns" }
  - { id: "1.2.1", title: "Knowledge: Hub-and-spoke architecture where a coordinator agent manages all inter-subagent communication, error handling, and information routing" }
  - { id: "1.2.2", title: "Knowledge: How subagents operate with isolated context—they do not inherit the coordinator's conversation history automatically" }
  - { id: "1.2.3", title: "Knowledge: The role of the coordinator in task decomposition, delegation, result aggregation, and deciding which subagents to invoke based on query complexity" }
  - { id: "1.2.4", title: "Knowledge: Risks of overly narrow task decomposition by the coordinator, leading to incomplete coverage of broad research topics" }
  - { id: "1.2.5", title: "Skill: Designing coordinator agents that analyze query requirements and dynamically select which subagents to invoke rather than always routing through the full pipeline" }
  - { id: "1.2.6", title: "Skill: Partitioning research scope across subagents to minimize duplication (e.g., assigning distinct subtopics or source types to each agent)" }
  - { id: "1.2.7", title: "Skill: Implementing iterative refinement loops where the coordinator evaluates synthesis output for gaps, re-delegates to search and analysis subagents with targeted queries, and re-invokes synthesis until coverage is sufficient" }
  - { id: "1.2.8", title: "Skill: Routing all subagent communication through the coordinator for observability, consistent error handling, and controlled information flow" }
  - { id: "1.3", title: "Configure subagent invocation, context passing, and spawning" }
  - { id: "1.3.1", title: "Knowledge: The Task tool as the mechanism for spawning subagents, and the requirement that allowedTools must include \"Task\" for a coordinator to invoke subagents" }
  - { id: "1.3.2", title: "Knowledge: That subagent context must be explicitly provided in the prompt—subagents do not automatically inherit parent context or share memory between invocations" }
  - { id: "1.3.3", title: "Knowledge: The AgentDefinition configuration including descriptions, system prompts, and tool restrictions for each subagent type" }
  - { id: "1.3.4", title: "Knowledge: Fork-based session management for exploring divergent approaches from a shared analysis baseline" }
  - { id: "1.3.5", title: "Skill: Including complete findings from prior agents directly in the subagent's prompt (e.g., passing web search results and document analysis outputs to the synthesis subagent)" }
  - { id: "1.3.6", title: "Skill: Using structured data formats to separate content from metadata (source URLs, document names, page numbers) when passing context between agents to preserve attribution" }
  - { id: "1.3.7", title: "Skill: Spawning parallel subagents by emitting multiple Task tool calls in a single coordinator response rather than across separate turns" }
  - { id: "1.3.8", title: "Skill: Designing coordinator prompts that specify research goals and quality criteria rather than step-by-step procedural instructions, to enable subagent adaptability" }
  - { id: "1.4", title: "Implement multi-step workflows with enforcement and handoff patterns" }
  - { id: "1.4.1", title: "Knowledge: The difference between programmatic enforcement (hooks, prerequisite gates) and prompt-based guidance for workflow ordering" }
  - { id: "1.4.2", title: "Knowledge: When deterministic compliance is required (e.g., identity verification before financial operations), prompt instructions alone have a non-zero failure rate" }
  - { id: "1.4.3", title: "Knowledge: Structured handoff protocols for mid-process escalation that include customer details, root cause analysis, and recommended actions" }
  - { id: "1.4.4", title: "Skill: Implementing programmatic prerequisites that block downstream tool calls until prerequisite steps have completed (e.g., blocking process_refund until get_customer has returned a verified customer ID)" }
  - { id: "1.4.5", title: "Skill: Decomposing multi-concern customer requests into distinct items, then investigating each in parallel using shared context before synthesizing a unified resolution" }
  - { id: "1.4.6", title: "Skill: Compiling structured handoff summaries (customer ID, root cause, refund amount, recommended action) when escalating to human agents who lack access to the conversation transcript" }
  - { id: "1.5", title: "Apply Agent SDK hooks for tool call interception and data normalization" }
  - { id: "1.5.1", title: "Knowledge: Hook patterns (e.g., PostToolUse) that intercept tool results for transformation before the model processes them" }
  - { id: "1.5.2", title: "Knowledge: Hook patterns that intercept outgoing tool calls to enforce compliance rules (e.g., blocking refunds above a threshold)" }
  - { id: "1.5.3", title: "Knowledge: The distinction between using hooks for deterministic guarantees versus relying on prompt instructions for probabilistic compliance" }
  - { id: "1.5.4", title: "Skill: Implementing PostToolUse hooks to normalize heterogeneous data formats (Unix timestamps, ISO 8601, numeric status codes) from different MCP tools before the agent processes them" }
  - { id: "1.5.5", title: "Skill: Implementing tool call interception hooks that block policy-violating actions (e.g., refunds exceeding $500) and redirect to alternative workflows (e.g., human escalation)" }
  - { id: "1.5.6", title: "Skill: Choosing hooks over prompt-based enforcement when business rules require guaranteed compliance" }
  - { id: "1.6", title: "Design task decomposition strategies for complex workflows" }
  - { id: "1.6.1", title: "Knowledge: When to use fixed sequential pipelines (prompt chaining) versus dynamic adaptive decomposition based on intermediate findings" }
  - { id: "1.6.2", title: "Knowledge: Prompt chaining patterns that break reviews into sequential steps (e.g., analyze each file individually, then run a cross-file integration pass)" }
  - { id: "1.6.3", title: "Knowledge: The value of adaptive investigation plans that generate subtasks based on what is discovered at each step" }
  - { id: "1.6.4", title: "Skill: Selecting task decomposition patterns appropriate to the workflow: prompt chaining for predictable multi-aspect reviews, dynamic decomposition for open-ended investigation tasks" }
  - { id: "1.6.5", title: "Skill: Splitting large code reviews into per-file local analysis passes plus a separate cross-file integration pass to avoid attention dilution" }
  - { id: "1.6.6", title: "Skill: Decomposing open-ended tasks (e.g., \"add comprehensive tests to a legacy codebase\") by first mapping structure, identifying high-impact areas, then creating a prioritized plan that adapts as dependencies are discovered" }
  - { id: "1.7", title: "Manage session state, resumption, and forking" }
  - { id: "1.7.1", title: "Knowledge: Named session resumption using –resume <session-name> to continue a specific prior conversation" }
  - { id: "1.7.2", title: "Knowledge: fork_session for creating independent branches from a shared analysis baseline to explore divergent approaches" }
  - { id: "1.7.3", title: "Knowledge: The importance of informing the agent about changes to previously analyzed files when resuming sessions after code modifications" }
  - { id: "1.7.4", title: "Knowledge: Why starting a new session with a structured summary is more reliable than resuming with stale tool results" }
  - { id: "1.7.5", title: "Skill: Using –resume with session names to continue named investigation sessions across work sessions" }
  - { id: "1.7.6", title: "Skill: Using fork_session to create parallel exploration branches (e.g., comparing two testing strategies or refactoring approaches from a shared codebase analysis)" }
  - { id: "1.7.7", title: "Skill: Choosing between session resumption (when prior context is mostly valid) and starting fresh with injected summaries (when prior tool results are stale)" }
  - { id: "1.7.8", title: "Skill: Informing a resumed session about specific file changes for targeted re-analysis rather than requiring full re-exploration" }
  - { id: "2", title: "Tool Design & MCP Integration", weight: "18%" }
  - { id: "2.1", title: "Design effective tool interfaces with clear descriptions and boundaries" }
  - { id: "2.1.1", title: "Knowledge: Tool descriptions as the primary mechanism LLMs use for tool selection; minimal descriptions lead to unreliable selection among similar tools" }
  - { id: "2.1.2", title: "Knowledge: The importance of including input formats, example queries, edge cases, and boundary explanations in tool descriptions" }
  - { id: "2.1.3", title: "Knowledge: How ambiguous or overlapping tool descriptions cause misrouting (e.g., analyze_content vs analyze_document with near-identical descriptions)" }
  - { id: "2.1.4", title: "Knowledge: The impact of system prompt wording on tool selection: keyword-sensitive instructions can create unintended tool associations" }
  - { id: "2.1.5", title: "Skill: Writing tool descriptions that clearly differentiate each tool's purpose, expected inputs, outputs, and when to use it versus similar alternatives" }
  - { id: "2.1.6", title: "Skill: Renaming tools and updating descriptions to eliminate functional overlap (e.g., renaming analyze_content to extract_web_results with a web-specific description)" }
  - { id: "2.1.7", title: "Skill: Splitting generic tools into purpose-specific tools with defined input/output contracts (e.g., splitting a generic analyze_document into extract_data_points, summarize_content, and verify_claim_against_source)" }
  - { id: "2.1.8", title: "Skill: Reviewing system prompts for keyword-sensitive instructions that might override well-written tool descriptions" }
  - { id: "2.2", title: "Implement structured error responses for MCP tools" }
  - { id: "2.2.1", title: "Knowledge: The MCP isError flag pattern for communicating tool failures back to the agent" }
  - { id: "2.2.2", title: "Knowledge: The distinction between transient errors (timeouts, service unavailability), validation errors (invalid input), business errors (policy violations), and permission errors" }
  - { id: "2.2.3", title: "Knowledge: Why uniform error responses (generic \"Operation failed\") prevent the agent from making appropriate recovery decisions" }
  - { id: "2.2.4", title: "Knowledge: The difference between retryable and non-retryable errors, and how returning structured metadata prevents wasted retry attempts" }
  - { id: "2.2.5", title: "Skill: Returning structured error metadata including errorCategory (transient/validation/permission), isRetryable boolean, and human-readable descriptions" }
  - { id: "2.2.6", title: "Skill: Including retriable: false flags and customer-friendly explanations for business rule violations so the agent can communicate appropriately" }
  - { id: "2.2.7", title: "Skill: Implementing local error recovery within subagents for transient failures, propagating to the coordinator only errors that cannot be resolved locally along with partial results and what was attempted" }
  - { id: "2.2.8", title: "Skill: Distinguishing between access failures (needing retry decisions) and valid empty results (representing successful queries with no matches)" }
  - { id: "2.3", title: "Distribute tools appropriately across agents and configure tool choice" }
  - { id: "2.3.1", title: "Knowledge: The principle that giving an agent access to too many tools (e.g., 18 instead of 4-5) degrades tool selection reliability by increasing decision complexity" }
  - { id: "2.3.2", title: "Knowledge: Why agents with tools outside their specialization tend to misuse them (e.g., a synthesis agent attempting web searches)" }
  - { id: "2.3.3", title: "Knowledge: Scoped tool access: giving agents only the tools needed for their role, with limited cross-role tools for specific high-frequency needs" }
  - { id: "2.3.4", title: "Knowledge: tool_choice configuration options: \"auto\", \"any\", and forced tool selection ({\"type\": \"tool\", \"name\": \"...\"})" }
  - { id: "2.3.5", title: "Skill: Restricting each subagent's tool set to those relevant to its role, preventing cross-specialization misuse" }
  - { id: "2.3.6", title: "Skill: Replacing generic tools with constrained alternatives (e.g., replacing fetch_url with load_document that validates document URLs)" }
  - { id: "2.3.7", title: "Skill: Providing scoped cross-role tools for high-frequency needs (e.g., a verify_fact tool for the synthesis agent) while routing complex cases through the coordinator" }
  - { id: "2.3.8", title: "Skill: Using tool_choice forced selection to ensure a specific tool is called first (e.g., forcing extract_metadata before enrichment tools), then processing subsequent steps in follow-up turns" }
  - { id: "2.3.9", title: "Skill: Setting tool_choice: \"any\" to guarantee the model calls a tool rather than returning conversational text" }
  - { id: "2.4", title: "Integrate MCP servers into Claude Code and agent workflows" }
  - { id: "2.4.1", title: "Knowledge: MCP server scoping: project-level (.mcp.json) for shared team tooling vs user-level (~/.claude.json) for personal/experimental servers" }
  - { id: "2.4.2", title: "Knowledge: Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) for credential management without committing secrets" }
  - { id: "2.4.3", title: "Knowledge: That tools from all configured MCP servers are discovered at connection time and available simultaneously to the agent" }
  - { id: "2.4.4", title: "Knowledge: MCP resources as a mechanism for exposing content catalogs (e.g., issue summaries, documentation hierarchies, database schemas) to reduce exploratory tool calls" }
  - { id: "2.4.5", title: "Skill: Configuring shared MCP servers in project-scoped .mcp.json with environment variable expansion for authentication tokens" }
  - { id: "2.4.6", title: "Skill: Configuring personal/experimental MCP servers in user-scoped ~/.claude.json" }
  - { id: "2.4.7", title: "Skill: Enhancing MCP tool descriptions to explain capabilities and outputs in detail, preventing the agent from preferring built-in tools (like Grep) over more capable MCP tools" }
  - { id: "2.4.8", title: "Skill: Choosing existing community MCP servers over custom implementations for standard integrations (e.g., Jira), reserving custom servers for team-specific workflows" }
  - { id: "2.4.9", title: "Skill: Exposing content catalogs as MCP resources to give agents visibility into available data without requiring exploratory tool calls" }
  - { id: "2.5", title: "Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob) effectively" }
  - { id: "2.5.1", title: "Knowledge: Grep for content search (searching file contents for patterns like function names, error messages, or import statements)" }
  - { id: "2.5.2", title: "Knowledge: Glob for file path pattern matching (finding files by name or extension patterns)" }
  - { id: "2.5.3", title: "Knowledge: Read/Write for full file operations; Edit for targeted modifications using unique text matching" }
  - { id: "2.5.4", title: "Knowledge: When Edit fails due to non-unique text matches, using Read + Write as a fallback for reliable file modifications" }
  - { id: "2.5.5", title: "Skill: Selecting Grep for searching code content across a codebase (e.g., finding all callers of a function, locating error messages)" }
  - { id: "2.5.6", title: "Skill: Selecting Glob for finding files matching naming patterns (e.g., **/*.test.tsx)" }
  - { id: "2.5.7", title: "Skill: Using Read to load full file contents followed by Write when Edit cannot find unique anchor text" }
  - { id: "2.5.8", title: "Skill: Building codebase understanding incrementally: starting with Grep to find entry points, then using Read to follow imports and trace flows, rather than reading all files upfront" }
  - { id: "2.5.9", title: "Skill: Tracing function usage across wrapper modules by first identifying all exported names, then searching for each name across the codebase" }
  - { id: "3", title: "Claude Code Configuration & Workflows", weight: "20%" }
  - { id: "3.1", title: "Configure CLAUDE.md files with appropriate hierarchy, scoping, and modular organization" }
  - { id: "3.1.1", title: "Knowledge: The CLAUDE.md configuration hierarchy: user-level (~/.claude/CLAUDE.md), project-level (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files)" }
  - { id: "3.1.2", title: "Knowledge: That user-level settings apply only to that user—instructions in ~/.claude/CLAUDE.md are not shared with teammates via version control" }
  - { id: "3.1.3", title: "Knowledge: The @import syntax for referencing external files to keep CLAUDE.md modular (e.g., importing specific standards files relevant to each package)" }
  - { id: "3.1.4", title: "Knowledge: .claude/rules/ directory for organizing topic-specific rule files as an alternative to a monolithic CLAUDE.md" }
  - { id: "3.1.5", title: "Skill: Diagnosing configuration hierarchy issues (e.g., a new team member not receiving instructions because they're in user-level rather than project-level configuration)" }
  - { id: "3.1.6", title: "Skill: Using @import to selectively include relevant standards files in each package's CLAUDE.md based on maintainer domain knowledge" }
  - { id: "3.1.7", title: "Skill: Splitting large CLAUDE.md files into focused topic-specific files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md)" }
  - { id: "3.1.8", title: "Skill: Using the /memory command to verify which memory files are loaded and diagnose inconsistent behavior across sessions" }
  - { id: "3.2", title: "Create and configure custom slash commands and skills" }
  - { id: "3.2.1", title: "Knowledge: Project-scoped commands in .claude/commands/ (shared via version control) vs user-scoped commands in ~/.claude/commands/ (personal)" }
  - { id: "3.2.2", title: "Knowledge: Skills in .claude/skills/ with SKILL.md files that support frontmatter configuration including context: fork, allowed-tools, and argument-hint" }
  - { id: "3.2.3", title: "Knowledge: The context: fork frontmatter option for running skills in an isolated sub-agent context, preventing skill outputs from polluting the main conversation" }
  - { id: "3.2.4", title: "Knowledge: Personal skill customization: creating personal variants in ~/.claude/skills/ with different names to avoid affecting teammates" }
  - { id: "3.2.5", title: "Skill: Creating project-scoped slash commands in .claude/commands/ for team-wide availability via version control" }
  - { id: "3.2.6", title: "Skill: Using context: fork to isolate skills that produce verbose output (e.g., codebase analysis) or exploratory context (e.g., brainstorming alternatives) from the main session" }
  - { id: "3.2.7", title: "Skill: Configuring allowed-tools in skill frontmatter to restrict tool access during skill execution (e.g., limiting to file write operations to prevent destructive actions)" }
  - { id: "3.2.8", title: "Skill: Using argument-hint frontmatter to prompt developers for required parameters when they invoke the skill without arguments" }
  - { id: "3.2.9", title: "Skill: Choosing between skills (on-demand invocation for task-specific workflows) and CLAUDE.md (always-loaded universal standards)" }
  - { id: "3.3", title: "Apply path-specific rules for conditional convention loading" }
  - { id: "3.3.1", title: "Knowledge: .claude/rules/ files with YAML frontmatter paths fields containing glob patterns for conditional rule activation" }
  - { id: "3.3.2", title: "Knowledge: How path-scoped rules load only when editing matching files, reducing irrelevant context and token usage" }
  - { id: "3.3.3", title: "Knowledge: The advantage of glob-pattern rules over directory-level CLAUDE.md files for conventions that span multiple directories (e.g., test files spread throughout a codebase)" }
  - { id: "3.3.4", title: "Skill: Creating .claude/rules/ files with YAML frontmatter path scoping (e.g., paths: [\"terraform/**/*\"]) so rules load only when editing matching files" }
  - { id: "3.3.5", title: "Skill: Using glob patterns in path-specific rules to apply conventions to files by type regardless of directory location (e.g., **/*.test.tsx for all test files)" }
  - { id: "3.3.6", title: "Skill: Choosing path-specific rules over subdirectory CLAUDE.md files when conventions must apply to files spread across the codebase" }
  - { id: "3.4", title: "Determine when to use plan mode vs direct execution" }
  - { id: "3.4.1", title: "Knowledge: Plan mode is designed for complex tasks involving large-scale changes, multiple valid approaches, architectural decisions, and multi-file modifications" }
  - { id: "3.4.2", title: "Knowledge: Direct execution is appropriate for simple, well-scoped changes (e.g., adding a single validation check to one function)" }
  - { id: "3.4.3", title: "Knowledge: Plan mode enables safe codebase exploration and design before committing to changes, preventing costly rework" }
  - { id: "3.4.4", title: "Knowledge: The Explore subagent for isolating verbose discovery output and returning summaries to preserve main conversation context" }
  - { id: "3.4.5", title: "Skill: Selecting plan mode for tasks with architectural implications (e.g., microservice restructuring, library migrations affecting 45+ files, choosing between integration approaches with different infrastructure requirements)" }
  - { id: "3.4.6", title: "Skill: Selecting direct execution for well-understood changes with clear scope (e.g., a single-file bug fix with a clear stack trace, adding a date validation conditional)" }
  - { id: "3.4.7", title: "Skill: Using the Explore subagent for verbose discovery phases to prevent context window exhaustion during multi-phase tasks" }
  - { id: "3.4.8", title: "Skill: Combining plan mode for investigation with direct execution for implementation (e.g., planning a library migration, then executing the planned approach)" }
  - { id: "3.5", title: "Apply iterative refinement techniques for progressive improvement" }
  - { id: "3.5.1", title: "Knowledge: Concrete input/output examples as the most effective way to communicate expected transformations when prose descriptions are interpreted inconsistently" }
  - { id: "3.5.2", title: "Knowledge: Test-driven iteration: writing test suites first, then iterating by sharing test failures to guide progressive improvement" }
  - { id: "3.5.3", title: "Knowledge: The interview pattern: having Claude ask questions to surface considerations the developer may not have anticipated before implementing" }
  - { id: "3.5.4", title: "Knowledge: When to provide all issues in a single message (interacting problems) versus fixing them sequentially (independent problems)" }
  - { id: "3.5.5", title: "Skill: Providing 2-3 concrete input/output examples to clarify transformation requirements when natural language descriptions produce inconsistent results" }
  - { id: "3.5.6", title: "Skill: Writing test suites covering expected behavior, edge cases, and performance requirements before implementation, then iterating by sharing test failures" }
  - { id: "3.5.7", title: "Skill: Using the interview pattern to surface design considerations (e.g., cache invalidation strategies, failure modes) before implementing solutions in unfamiliar domains" }
  - { id: "3.5.8", title: "Skill: Providing specific test cases with example input and expected output to fix edge case handling (e.g., null values in migration scripts)" }
  - { id: "3.5.9", title: "Skill: Addressing multiple interacting issues in a single detailed message when fixes interact, versus sequential iteration for independent issues" }
  - { id: "3.6", title: "Integrate Claude Code into CI/CD pipelines" }
  - { id: "3.6.1", title: "Knowledge: The -p (or –print) flag for running Claude Code in non-interactive mode in automated pipelines" }
  - { id: "3.6.2", title: "Knowledge: –output-format json and –json-schema CLI flags for enforcing structured output in CI contexts" }
  - { id: "3.6.3", title: "Knowledge: CLAUDE.md as the mechanism for providing project context (testing standards, fixture conventions, review criteria) to CI-invoked Claude Code" }
  - { id: "3.6.4", title: "Knowledge: Session context isolation: why the same Claude session that generated code is less effective at reviewing its own changes compared to an independent review instance" }
  - { id: "3.6.5", title: "Skill: Running Claude Code in CI with the -p flag to prevent interactive input hangs" }
  - { id: "3.6.6", title: "Skill: Using –output-format json with –json-schema to produce machine-parseable structured findings for automated posting as inline PR comments" }
  - { id: "3.6.7", title: "Skill: Including prior review findings in context when re-running reviews after new commits, instructing Claude to report only new or still-unaddressed issues to avoid duplicate comments" }
  - { id: "3.6.8", title: "Skill: Providing existing test files in context so test generation avoids suggesting duplicate scenarios already covered by the test suite" }
  - { id: "3.6.9", title: "Skill: Documenting testing standards, valuable test criteria, and available fixtures in CLAUDE.md to improve test generation quality and reduce low-value test output" }
  - { id: "4", title: "Prompt Engineering & Structured Output", weight: "20%" }
  - { id: "4.1", title: "Design prompts with explicit criteria to improve precision and reduce false positives" }
  - { id: "4.1.1", title: "Knowledge: The importance of explicit criteria over vague instructions (e.g., \"flag comments only when claimed behavior contradicts actual code behavior\" vs \"check that comments are accurate\")" }
  - { id: "4.1.2", title: "Knowledge: How general instructions like \"be conservative\" or \"only report high-confidence findings\" fail to improve precision compared to specific categorical criteria" }
  - { id: "4.1.3", title: "Knowledge: The impact of false positive rates on developer trust: high false positive categories undermine confidence in accurate categories" }
  - { id: "4.1.4", title: "Skill: Writing specific review criteria that define which issues to report (bugs, security) versus skip (minor style, local patterns) rather than relying on confidence-based filtering" }
  - { id: "4.1.5", title: "Skill: Temporarily disabling high false-positive categories to restore developer trust while improving prompts for those categories" }
  - { id: "4.1.6", title: "Skill: Defining explicit severity criteria with concrete code examples for each severity level to achieve consistent classification" }
  - { id: "4.2", title: "Apply few-shot prompting to improve output consistency and quality" }
  - { id: "4.2.1", title: "Knowledge: Few-shot examples as the most effective technique for achieving consistently formatted, actionable output when detailed instructions alone produce inconsistent results" }
  - { id: "4.2.2", title: "Knowledge: The role of few-shot examples in demonstrating ambiguous-case handling (e.g., tool selection for ambiguous requests, branch-level test coverage gaps)" }
  - { id: "4.2.3", title: "Knowledge: How few-shot examples enable the model to generalize judgment to novel patterns rather than matching only pre-specified cases" }
  - { id: "4.2.4", title: "Knowledge: The effectiveness of few-shot examples for reducing hallucination in extraction tasks (e.g., handling informal measurements, varied document structures)" }
  - { id: "4.2.5", title: "Skill: Creating 2-4 targeted few-shot examples for ambiguous scenarios that show reasoning for why one action was chosen over plausible alternatives" }
  - { id: "4.2.6", title: "Skill: Including few-shot examples that demonstrate specific desired output format (location, issue, severity, suggested fix) to achieve consistency" }
  - { id: "4.2.7", title: "Skill: Providing few-shot examples distinguishing acceptable code patterns from genuine issues to reduce false positives while enabling generalization" }
  - { id: "4.2.8", title: "Skill: Using few-shot examples to demonstrate correct handling of varied document structures (inline citations vs bibliographies, methodology sections vs embedded details)" }
  - { id: "4.2.9", title: "Skill: Adding few-shot examples showing correct extraction from documents with varied formats to address empty/null extraction of required fields" }
  - { id: "4.3", title: "Enforce structured output using tool use and JSON schemas" }
  - { id: "4.3.1", title: "Knowledge: Tool use (tool_use) with JSON schemas as the most reliable approach for guaranteed schema-compliant structured output, eliminating JSON syntax errors" }
  - { id: "4.3.2", title: "Knowledge: The distinction between tool_choice: \"auto\" (model may return text instead of calling a tool), \"any\" (model must call a tool but can choose which), and forced tool selection (model must call a specific named tool)" }
  - { id: "4.3.3", title: "Knowledge: That strict JSON schemas via tool use eliminate syntax errors but do not prevent semantic errors (e.g., line items that don't sum to total, values in wrong fields)" }
  - { id: "4.3.4", title: "Knowledge: Schema design considerations: required vs optional fields, enum fields with \"other\" + detail string patterns for extensible categories" }
  - { id: "4.3.5", title: "Skill: Defining extraction tools with JSON schemas as input parameters and extracting structured data from the tool_use response" }
  - { id: "4.3.6", title: "Skill: Setting tool_choice: \"any\" to guarantee structured output when multiple extraction schemas exist and the document type is unknown" }
  - { id: "4.3.7", title: "Skill: Forcing a specific tool with tool_choice: {\"type\": \"tool\", \"name\": \"extract_metadata\"} to ensure a particular extraction runs before enrichment steps" }
  - { id: "4.3.8", title: "Skill: Designing schema fields as optional (nullable) when source documents may not contain the information, preventing the model from fabricating values to satisfy required fields" }
  - { id: "4.3.9", title: "Skill: Adding enum values like \"unclear\" for ambiguous cases and \"other\" + detail fields for extensible categorization" }
  - { id: "4.3.10", title: "Skill: Including format normalization rules in prompts alongside strict output schemas to handle inconsistent source formatting" }
  - { id: "4.4", title: "Implement validation, retry, and feedback loops for extraction quality" }
  - { id: "4.4.1", title: "Knowledge: Retry-with-error-feedback: appending specific validation errors to the prompt on retry to guide the model toward correction" }
  - { id: "4.4.2", title: "Knowledge: The limits of retry: retries are ineffective when the required information is simply absent from the source document (vs format or structural errors)" }
  - { id: "4.4.3", title: "Knowledge: Feedback loop design: tracking which code constructs trigger findings (detected_pattern field) to enable systematic analysis of dismissal patterns" }
  - { id: "4.4.4", title: "Knowledge: The difference between semantic validation errors (values don't sum, wrong field placement) and schema syntax errors (eliminated by tool use)" }
  - { id: "4.4.5", title: "Skill: Implementing follow-up requests that include the original document, the failed extraction, and specific validation errors for model self-correction" }
  - { id: "4.4.6", title: "Skill: Identifying when retries will be ineffective (e.g., information exists only in an external document not provided) versus when they will succeed (format mismatches, structural output errors)" }
  - { id: "4.4.7", title: "Skill: Adding detected_pattern fields to structured findings to enable analysis of false positive patterns when developers dismiss findings" }
  - { id: "4.4.8", title: "Skill: Designing self-correction validation flows: extracting \"calculated_total\" alongside \"stated_total\" to flag discrepancies, adding \"conflict_detected\" booleans for inconsistent source data" }
  - { id: "4.5", title: "Design efficient batch processing strategies" }
  - { id: "4.5.1", title: "Knowledge: The Message Batches API: 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA" }
  - { id: "4.5.2", title: "Knowledge: Batch processing is appropriate for non-blocking, latency-tolerant workloads (overnight reports, weekly audits, nightly test generation) and inappropriate for blocking workflows (pre-merge checks)" }
  - { id: "4.5.3", title: "Knowledge: The batch API does not support multi-turn tool calling within a single request (cannot execute tools mid-request and return results)" }
  - { id: "4.5.4", title: "Knowledge: custom_id fields for correlating batch request/response pairs" }
  - { id: "4.5.5", title: "Skill: Matching API approach to workflow latency requirements: synchronous API for blocking pre-merge checks, batch API for overnight/weekly analysis" }
  - { id: "4.5.6", title: "Skill: Calculating batch submission frequency based on SLA constraints (e.g., 4-hour windows to guarantee 30-hour SLA with 24-hour batch processing)" }
  - { id: "4.5.7", title: "Skill: Handling batch failures: resubmitting only failed documents (identified by custom_id) with appropriate modifications (e.g., chunking documents that exceeded context limits)" }
  - { id: "4.5.8", title: "Skill: Using prompt refinement on a sample set before batch-processing large volumes to maximize first-pass success rates and reduce iterative resubmission costs" }
  - { id: "4.6", title: "Design multi-instance and multi-pass review architectures" }
  - { id: "4.6.1", title: "Knowledge: Self-review limitations: a model retains reasoning context from generation, making it less likely to question its own decisions in the same session" }
  - { id: "4.6.2", title: "Knowledge: Independent review instances (without prior reasoning context) are more effective at catching subtle issues than self-review instructions or extended thinking" }
  - { id: "4.6.3", title: "Knowledge: Multi-pass review: splitting large reviews into per-file local analysis passes plus cross-file integration passes to avoid attention dilution and contradictory findings" }
  - { id: "4.6.4", title: "Skill: Using a second independent Claude instance to review generated code without the generator's reasoning context" }
  - { id: "4.6.5", title: "Skill: Splitting large multi-file reviews into focused per-file passes for local issues plus separate integration passes for cross-file data flow analysis" }
  - { id: "4.6.6", title: "Skill: Running verification passes where the model self-reports confidence alongside each finding to enable calibrated review routing" }
  - { id: "5", title: "Context Management & Reliability", weight: "15%" }
  - { id: "5.1", title: "Manage conversation context to preserve critical information across long interactions" }
  - { id: "5.1.1", title: "Knowledge: Progressive summarization risks: condensing numerical values, percentages, dates, and customer-stated expectations into vague summaries" }
  - { id: "5.1.2", title: "Knowledge: The \"lost in the middle\" effect: models reliably process information at the beginning and end of long inputs but may omit findings from middle sections" }
  - { id: "5.1.3", title: "Knowledge: How tool results accumulate in context and consume tokens disproportionately to their relevance (e.g., 40+ fields per order lookup when only 5 are relevant)" }
  - { id: "5.1.4", title: "Knowledge: The importance of passing complete conversation history in subsequent API requests to maintain conversational coherence" }
  - { id: "5.1.5", title: "Skill: Extracting transactional facts (amounts, dates, order numbers, statuses) into a persistent \"case facts\" block included in each prompt, outside summarized history" }
  - { id: "5.1.6", title: "Skill: Extracting and persisting structured issue data (order IDs, amounts, statuses) into a separate context layer for multi-issue sessions" }
  - { id: "5.1.7", title: "Skill: Trimming verbose tool outputs to only relevant fields before they accumulate in context (e.g., keeping only return-relevant fields from order lookups)" }
  - { id: "5.1.8", title: "Skill: Placing key findings summaries at the beginning of aggregated inputs and organizing detailed results with explicit section headers to mitigate position effects" }
  - { id: "5.1.9", title: "Skill: Requiring subagents to include metadata (dates, source locations, methodological context) in structured outputs to support accurate downstream synthesis" }
  - { id: "5.1.10", title: "Skill: Modifying upstream agents to return structured data (key facts, citations, relevance scores) instead of verbose content and reasoning chains when downstream agents have limited context budgets" }
  - { id: "5.2", title: "Design effective escalation and ambiguity resolution patterns" }
  - { id: "5.2.1", title: "Knowledge: Appropriate escalation triggers: customer requests for a human, policy exceptions/gaps (not just complex cases), and inability to make meaningful progress" }
  - { id: "5.2.2", title: "Knowledge: The distinction between escalating immediately when a customer explicitly demands it versus offering to resolve when the issue is straightforward" }
  - { id: "5.2.3", title: "Knowledge: Why sentiment-based escalation and self-reported confidence scores are unreliable proxies for actual case complexity" }
  - { id: "5.2.4", title: "Knowledge: How multiple customer matches require clarification (requesting additional identifiers) rather than heuristic selection" }
  - { id: "5.2.5", title: "Skill: Adding explicit escalation criteria with few-shot examples to the system prompt demonstrating when to escalate versus resolve autonomously" }
  - { id: "5.2.6", title: "Skill: Honoring explicit customer requests for human agents immediately without first attempting investigation" }
  - { id: "5.2.7", title: "Skill: Acknowledging frustration while offering resolution when the issue is within the agent's capability, escalating only if the customer reiterates their preference" }
  - { id: "5.2.8", title: "Skill: Escalating when policy is ambiguous or silent on the customer's specific request (e.g., competitor price matching when policy only addresses own-site adjustments)" }
  - { id: "5.2.9", title: "Skill: Instructing the agent to ask for additional identifiers when tool results return multiple matches, rather than selecting based on heuristics" }
  - { id: "5.3", title: "Implement error propagation strategies across multi-agent systems" }
  - { id: "5.3.1", title: "Knowledge: Structured error context (failure type, attempted query, partial results, alternative approaches) as enabling intelligent coordinator recovery decisions" }
  - { id: "5.3.2", title: "Knowledge: The distinction between access failures (timeouts needing retry decisions) and valid empty results (successful queries with no matches)" }
  - { id: "5.3.3", title: "Knowledge: Why generic error statuses (\"search unavailable\") hide valuable context from the coordinator" }
  - { id: "5.3.4", title: "Knowledge: Why silently suppressing errors (returning empty results as success) or terminating entire workflows on single failures are both anti-patterns" }
  - { id: "5.3.5", title: "Skill: Returning structured error context including failure type, what was attempted, partial results, and potential alternatives to enable coordinator recovery" }
  - { id: "5.3.6", title: "Skill: Distinguishing access failures from valid empty results in error reporting so the coordinator can make appropriate decisions" }
  - { id: "5.3.7", title: "Skill: Having subagents implement local recovery for transient failures and only propagate errors they cannot resolve, including what was attempted and partial results" }
  - { id: "5.3.8", title: "Skill: Structuring synthesis output with coverage annotations indicating which findings are well-supported versus which topic areas have gaps due to unavailable sources" }
  - { id: "5.4", title: "Manage context effectively in large codebase exploration" }
  - { id: "5.4.1", title: "Knowledge: Context degradation in extended sessions: models start giving inconsistent answers and referencing \"typical patterns\" rather than specific classes discovered earlier" }
  - { id: "5.4.2", title: "Knowledge: The role of scratchpad files for persisting key findings across context boundaries" }
  - { id: "5.4.3", title: "Knowledge: Subagent delegation for isolating verbose exploration output while the main agent coordinates high-level understanding" }
  - { id: "5.4.4", title: "Knowledge: Structured state persistence for crash recovery: each agent exports state to a known location, and the coordinator loads a manifest on resume" }
  - { id: "5.4.5", title: "Skill: Spawning subagents to investigate specific questions (e.g., \"find all test files,\" \"trace refund flow dependencies\") while the main agent preserves high-level coordination" }
  - { id: "5.4.6", title: "Skill: Having agents maintain scratchpad files recording key findings, referencing them for subsequent questions to counteract context degradation" }
  - { id: "5.4.7", title: "Skill: Summarizing key findings from one exploration phase before spawning sub-agents for the next phase, injecting summaries into initial context" }
  - { id: "5.4.8", title: "Skill: Designing crash recovery using structured agent state exports (manifests) that the coordinator loads on resume and injects into agent prompts" }
  - { id: "5.4.9", title: "Skill: Using /compact to reduce context usage during extended exploration sessions when context fills with verbose discovery output" }
  - { id: "5.5", title: "Design human review workflows and confidence calibration" }
  - { id: "5.5.1", title: "Knowledge: The risk that aggregate accuracy metrics (e.g., 97% overall) may mask poor performance on specific document types or fields" }
  - { id: "5.5.2", title: "Knowledge: Stratified random sampling for measuring error rates in high-confidence extractions and detecting novel error patterns" }
  - { id: "5.5.3", title: "Knowledge: Field-level confidence scores calibrated using labeled validation sets for routing review attention" }
  - { id: "5.5.4", title: "Knowledge: The importance of validating accuracy by document type and field segment before automating high-confidence extractions" }
  - { id: "5.5.5", title: "Skill: Implementing stratified random sampling of high-confidence extractions for ongoing error rate measurement and novel pattern detection" }
  - { id: "5.5.6", title: "Skill: Analyzing accuracy by document type and field to verify consistent performance across all segments before reducing human review" }
  - { id: "5.5.7", title: "Skill: Having models output field-level confidence scores, then calibrating review thresholds using labeled validation sets" }
  - { id: "5.5.8", title: "Skill: Routing extractions with low model confidence or ambiguous/contradictory source documents to human review, prioritizing limited reviewer capacity" }
  - { id: "5.6", title: "Preserve information provenance and handle uncertainty in multi-source synthesis" }
  - { id: "5.6.1", title: "Knowledge: How source attribution is lost during summarization steps when findings are compressed without preserving claim-source mappings" }
  - { id: "5.6.2", title: "Knowledge: The importance of structured claim-source mappings that the synthesis agent must preserve and merge when combining findings" }
  - { id: "5.6.3", title: "Knowledge: How to handle conflicting statistics from credible sources: annotating conflicts with source attribution rather than arbitrarily selecting one value" }
  - { id: "5.6.4", title: "Knowledge: Temporal data: requiring publication/collection dates in structured outputs to prevent temporal differences from being misinterpreted as contradictions" }
  - { id: "5.6.5", title: "Skill: Requiring subagents to output structured claim-source mappings (source URLs, document names, relevant excerpts) that downstream agents preserve through synthesis" }
  - { id: "5.6.6", title: "Skill: Structuring reports with explicit sections distinguishing well-established findings from contested ones, preserving original source characterizations and methodological context" }
  - { id: "5.6.7", title: "Skill: Completing document analysis with conflicting values included and explicitly annotated, letting the coordinator decide how to reconcile before passing to synthesis" }
  - { id: "5.6.8", title: "Skill: Requiring subagents to include publication or data collection dates in structured outputs to enable correct temporal interpretation" }
  - { id: "5.6.9", title: "Skill: Rendering different content types appropriately in synthesis outputs—financial data as tables, news as prose, technical findings as structured lists—rather than converting everything to a uniform format" }
---
## About this code

**CLAUDE-ARCH-F is this library's own code.** Anthropic's exam guide gives the exam code **CCAR-F**, but this library uses CLAUDE-ARCH-F (and CLAUDE-ARCH-P for the Professional level) so the provider is obvious in lists. Claude Certified Architect – Foundations was Anthropic's first technical certification, launched with the Claude Partner Network on [March 12, 2026](https://www.anthropic.com/news/claude-partner-network). In July 2026 it became part of a family of four role-based credentials: Associate – Foundations, Developer – Foundations, Architect – Foundations and Architect – Professional ([announcement](https://www.claude.com/blog/four-role-based-claude-certifications)).

**Who can take it:** only people who work at organisations in the **Claude Partner Network**. Membership is free for firms that deliver Claude for clients ([apply at claude.com/partners](https://claude.com/partners)). You register with a company email on a domain listed in your organisation's partner record, and a personal address will not work ([eligibility page](https://anthropic-partners.skilljar.com/page/certification-eligibility)). If your employer is not a partner, the public Claude Academy courses give a certificate of completion, which is not a proctored certification.

### How the objectives above were built

Anthropic publishes a detailed public blueprint. The objectives transcribe the **Claude Certified Architect – Foundations Exam Guide, version 1.0, effective July 2026** ([PDF](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)) in full: 5 domains with weights, 30 task statements, and every "Knowledge of" and "Skills in" bullet, marked *Knowledge:* or *Skill:* in the same style as the AWS guides. Bullet text is kept close to Anthropic's wording because the exact API terms (`stop_reason`, `tool_choice`, `fork_session`, `.claude/rules/`) are what the exam tests.

## Exam format

Facts are as of 2026-10-24, from the exam guide and the [certification page](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification). Confirm them on the Anthropic Partner Academy before you register.

- **Question types:** multiple choice and multiple response. Each item says how many answers to select.
- **Structure:** scenario-based. The exam presents **4 scenarios chosen at random from a published set of 6**: customer support resolution agent, code generation with Claude Code, multi-agent research system, developer productivity with Claude, Claude Code for CI/CD, and structured data extraction.
- **Number of items:** 60.
- **Duration:** 120 minutes.
- **Passing score:** a scaled score of 720 on a 100–1,000 scale (criterion-referenced). The score report shows percent correct by domain.
- **Price:** USD 125. The checkout price reflects any partner-tier discount.
- **Language:** the guide and pages are in English, and no other languages are listed.
- **Delivery:** Pearson VUE, either online proctored or at a test centre. Identity is verified. You may cancel or reschedule up to 24 hours before, and later changes forfeit the fee.
- **Retakes:** waiting periods of 14, then 30, then 90 days after successive failures, with at most four attempts in a rolling 12 months. Every attempt costs the full fee.
- **Validity and renewal:** **12 months**. On-time renewal is a **free, non-proctored assessment** on the Anthropic Partner Academy covering what has changed. If the credential lapses, you must retake the full exam at full price.
- **Badge:** Credly by Pearson.

## What the exam really tests

The guide says it plainly: "practical judgment about architecture, configuration, and tradeoffs in production deployments". The questions are about building with Claude, not marketing or concepts:

- **Agentic loops and orchestration (27%).** Correct loop control on `stop_reason` (`tool_use` vs `end_turn`); coordinator–subagent (hub-and-spoke) design; subagents having *isolated* context, so you must pass findings explicitly; spawning parallel subagents through multiple Task calls in one response; hooks (PostToolUse, tool-call interception) for *deterministic* enforcement when prompts are not enough; and session resumption and forking.
- **Tool design and MCP (18%).** Tool descriptions that remove ambiguity, splitting vs. consolidating tools, structured MCP error responses (`isError`, error categories, retryable flags), giving each agent only the tools it needs, `tool_choice`, `.mcp.json` project vs. user scope with environment-variable expansion, and choosing the right built-in tool (Grep vs. Glob vs. Read).
- **Claude Code configuration (20%).** The CLAUDE.md hierarchy (user / project / directory) and `@import`, `.claude/rules/` with path globs, custom slash commands and skills (`context: fork`, `allowed-tools`, `argument-hint`), plan mode vs. direct execution, iterative refinement, and non-interactive CI use (`-p`, `--output-format json`, `--json-schema`).
- **Prompt engineering and structured output (20%).** Explicit criteria to reduce false positives, targeted few-shot examples, structured output via `tool_use` and JSON Schema (nullable fields to avoid made-up values), validation and retry loops, the Message Batches API (when its latency fits, `custom_id`, no multi-turn tool use), and multi-pass review.
- **Context management and reliability (15%).** Keeping critical facts through summarisation, lost-in-the-middle effects, trimming verbose tool output, scratchpad files, escalation criteria, error propagation across agents, human review with calibrated confidence, and information provenance.

The guide also lists **out-of-scope** topics: fine-tuning, authentication and billing, hosting MCP servers, embeddings and vector databases, computer use, vision, streaming, rate limits and pricing, cloud-provider configuration, and prompt-caching details.

**Where candidates lose points:** choosing *prompt-based* fixes where the scenario needs *programmatic* enforcement (hooks, prerequisite gates); assuming subagents share the parent's memory; using iteration caps or text parsing as the loop-termination signal; giving every agent every tool; and choosing the Batches API for latency-sensitive or multi-turn tool workflows.

## Study strategy

1. **Read the exam guide end to end,** including the six scenarios, the preparation exercises, the sample questions and the appendix's in-scope and out-of-scope lists.
2. **Take the official prep courses** in the Anthropic Partner Academy ([Architect – Foundations prep courses](https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses), part of the [Claude Architect path](https://anthropic-partners.skilljar.com/path/claude-architect)): Claude Platform 101, Claude Code 101, Introduction to Model Context Protocol, Introduction to Subagents, Deployment Architecture, and others. Use the public Claude Academy (academy.claude.com) and the Claude API, Agent SDK, Claude Code and MCP documentation as references.
3. **Do the guide's hands-on exercises.** Build a multi-tool agent with escalation; configure Claude Code for a real repository (CLAUDE.md, rules, a skill, an MCP server); build an extraction pipeline with `tool_use` and JSON Schema plus a validation-retry loop; run a batch job; build a coordinator with two subagents and explicit context passing.
4. **Write the anti-patterns down.** For every task statement, note the wrong approach the Skills bullets warn against. Those are the distractors.
5. **Stay current.** The credential lasts 12 months because the platform changes quickly. Check the guide's version before you book.

**How your background helps or misleads**

- *.NET/Angular development* makes the API and SDK mechanics (tool schemas, JSON validation, retries) feel familiar. The SDK examples in Anthropic's docs are mostly Python and TypeScript, and the exam tests concepts and configuration, not a language.
- *AZ-204 and CKAD preparation* help with CI/CD integration and thinking about distributed failures, but deploying MCP servers and container orchestration are explicitly **out of scope**.
- *Experience with other agent frameworks* (Microsoft Agent Framework or Semantic Kernel, AWS Bedrock Agents, LangChain) transfers conceptually. The exam rewards Claude-specific behaviour: `stop_reason` values, the Task tool, `allowedTools`, Claude Code file locations. Do not answer with another framework's terms.

## Differences from related exams

- **CLAUDE-ARCH-F vs CLAUDE-ARCH-P (Professional).** Foundations is hands-on and SDK-level: 60 items, 4 scenarios from a known bank of 6, very specific Knowledge and Skills bullets, USD 125. Professional (63 items, USD 175) moves up to enterprise solution architecture: model selection, RAG design, integration and auth, evaluation, governance and compliance, stakeholder communication. It publishes only task-level bullets. Foundations asks "configure it correctly". Professional asks "design it and defend it".
- **vs AI-103 (Azure AI Apps and Agents Developer) and AIP-C01 (AWS Certified Generative AI Developer – Professional).** These test the cloud vendor's managed AI platform (Microsoft Foundry and Azure services, or Amazon Bedrock and AWS services), including identity, networking and deployment. CLAUDE-ARCH-F is model-vendor-specific and excludes cloud-provider configuration entirely. Its depth is in agent loop design, tool and MCP design and Claude Code. They complement each other: the Azure/AWS exam shows where you run it, the Claude exam shows how the agent behaves.
- **vs GH-600 (GitHub Agentic AI Developer).** Both cover coding agents in the development workflow. GH-600 centres on GitHub Copilot and GitHub's platform. CLAUDE-ARCH-F centres on Claude Code configuration and the Claude Agent SDK.
- **vs NCP-AAI (NVIDIA Agentic AI) and PAA (Google Cloud Professional Agentic Architect).** NCP-AAI is broader across the agent life cycle and includes NVIDIA NIM, NeMo and Triton for inference and deployment. PAA is tied to Google's Gemini Enterprise, ADK, Agent Runtime and governance tools, and adds hands-on labs. CLAUDE-ARCH-F is the most detailed on loop control flow and tool-interface design.
- **vs AGENTA (iSAQB CPSA-A module).** AGENTA teaches vendor-neutral architecture *for* agentic engineering (harnesses, controls, agent-facing documentation). CLAUDE-ARCH-F tests one concrete implementation of those ideas (CLAUDE.md, rules, hooks, skills).

## Exam-day notes

- **Pace:** 60 items in 120 minutes is 2 minutes each. Scenarios share context, so read each scenario carefully once, then answer its items in a run.
- **Know the six scenarios in advance.** The bank is published. Before exam day, think through the architecture of each one so the scenario text holds no surprises.
- **Multi-response items:** select exactly the number requested.
- **Choose deterministic over hopeful.** When compliance or ordering *must* hold (for example, identity verification before a refund), the answer is a hook or programmatic gate, not a stronger prompt.
- **Choose explicit over implicit context.** If an answer assumes a subagent "knows" something from the coordinator, it is probably wrong.
- **Watch for out-of-scope distractors.** Options about fine-tuning, embeddings infrastructure or cloud IAM are usually there to mislead.
- **Online proctoring:** clear desk, no second monitor, stay in camera view. Have government photo ID that matches your registration name exactly.
