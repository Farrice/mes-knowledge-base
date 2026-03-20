# Lance Martin & Yichao "Peak" Ji - Context Engineering — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work.

## Genius Patterns

## Pattern 1: The Context Paradox Recognition
**Core Insight**: Agents need tool context but performance drops as context grows.
**Implementation**: Map expected context accumulation (tool calls × average output size × session length) against the model's effective context limit before designing.
**Deployment**: Initial architecture design, debugging degraded agent performance, evaluating new model capabilities.

## Pattern 2: Pre-Rot Threshold Detection
**Core Insight**: "128K to 200K" is the degradation zone—treat as tunable parameter discovered through evaluation, not a fixed number.
**Implementation**: Run controlled experiments incrementally increasing context size while measuring output quality. Plot degradation curve. Mark inflection point.
**Deployment**: Model selection, context management trigger configuration, capacity planning.

## Pattern 3: Compaction vs. Summarization Separation
**Core Insight**: Compaction is reversible (information externalized but recoverable); summarization is irreversible (information lost).
**Implementation**: For every tool call, define FULL and COMPACT formats. Compaction replaces when external state can reconstruct. Summarization only triggers when compaction insufficient.
**Success Metric**: 40-70% context reduction with 100% information recoverability.

## Pattern 4: The Reversibility Principle
**Core Insight**: "Almost every action in Manus is reversible if you can offload it to the file system or external state."
**Implementation**: For each tool, identify the unique identifier (file path, URL, query) that allows reconstruction. Compact representations must preserve this identifier.

## Pattern 5: Compaction Sequencing Intelligence
**Core Insight**: Compact oldest context first while preserving recent tool calls in full—maintaining "fresh few-shot examples" of proper tool usage.
**Implementation**: When compacting, apply to oldest 50% of tool calls while keeping newest 50% in full format.

## Pattern 6: Schema-Structured Summarization
**Core Insight**: Never use free-form summarization. Always define structured schema with specific fields.
**Implementation**: Create schema with fields: `files_modified`, `user_goal`, `current_progress`, `where_left_off`, `key_findings`, `pending_actions`.

## Pattern 7: The Three-Layer Action Space
**Core Insight**: Divide capabilities into three abstraction levels.
**Implementation**:
- **Layer 1 (Function Calling)**: 10-20 atomic operations only
- **Layer 2 (Sandbox Utilities)**: CLI tools via shell, extensible
- **Layer 3 (Packages/APIs)**: Computation-heavy in code

## Pattern 8: Atomic Function Philosophy
**Core Insight**: Ruthlessly minimize function calling space to truly atomic operations.
**Implementation**: Ask of every tool: "Can this be composed from more atomic operations?" Shell + text editor = Turing complete.

## Pattern 9: Agent-as-Tool Pattern
**Core Insight**: Complex operations become sub-agent calls with structured output schemas.
**Implementation**: Wrap multi-step tasks as "agent as tool" with constrained output schema defined by main agent.

## Pattern 10: Schema-as-Contract for Sub-Agents
**Core Insight**: Main agent defines output schema upfront. Sub-agents use `submit_result` with constrained decoding.
**Implementation**: Multi-agent operations as generating structured spreadsheets.

## Pattern 11: Share Context vs. Share Messages Pattern Selection
**Core Insight**: Choose pattern based on task characteristics.
- **By Communication**: Sub-agent gets only instruction, works independently
- **By Sharing Context**: Sub-agent sees full prior context with own system prompt

## Pattern 12: File System as Coordination Layer
**Core Insight**: Sandbox file system as coordination mechanism—agents read/write to shared paths instead of passing context through messages.
**Implementation**: For context >10K tokens, write to file and pass only path.

## Pattern 13: Future-Proof Architecture Testing
**Core Insight**: Test by swapping between weaker and stronger models. Significant gains = future-proof architecture.
**Implementation**: If stronger model shows >30% improvement, architecture will benefit from future upgrades.

## Pattern 14: Anti-Anthropomorphic Agent Design
**Core Insight**: Reject human org-chart metaphor. Design agents by function, not role.
**Implementation**: Executor (does work), Planner (maintains direction), Knowledge Manager (handles memory). Max 3-5 core agents.

## Pattern 15: Explicit Memory with User Confirmation
**Core Insight**: Long-term memory requires explicit user confirmation.
**Implementation**: Surface proposed memory with accept/reject options before storing.

## Pattern 16: Collective Feedback Mining
**Core Insight**: Look for patterns where many users give the same correction.
**Implementation**: Log corrections systematically, cluster by type, use common corrections for parameter-free improvement.

## Pattern 17: Line-Based Format Preference
**Core Insight**: Prefer line-based formats over markdown/JSON—enables grep, line-range reading, Unix tools.
**Implementation**: Plain text with line structure allows `grep`, `head`, `tail`, `sed` for retrieval.

## Pattern 18: Evaluation Triad
**Core Insight**: Three evaluation types in combination.
**Implementation**:
1. User ratings (gold standard)
2. Automated tests with verifiable results (fast iteration)
3. Human evaluation for subjective quality (taste)

## Pattern 19: Context Confusion Prevention
**Core Insight**: Too many tools cause "context confusion"—wrong tool calls or hallucinations.
**Implementation**: Keep under 20-30 tools. Check if capability can be achieved via sandbox/code first.

## Pattern 20: KV Cache Awareness
**Core Insight**: Tool definitions at front of context, stable across turns, enabling cache reuse.
**Implementation**: Keep schemas stable. Don't dynamically load/unload. Track cache hit rate.

## Pattern 21: Guardrail Layering
**Core Insight**: Multiple guardrail layers—network, action, progressive.
**Implementation**: Block sensitive data exfiltration, require confirmation for destructive ops, start with more confirmations and reduce over time.

## Pattern 22: The Simplification Principle
**Core Insight**: "Build less, understand more." Biggest gains from removing features, not adding.
**Implementation**: Before adding, ask: "Can we achieve this by removing something?" Refactor 4-6 times/year.

## Pattern 23: Model Capability Boundary Awareness
**Core Insight**: Context engineering is application layer; model training is model layer.
**Implementation**: Don't duplicate model company efforts. Focus on your specific use case, tools, users.

## Hidden Knowledge

## Tacit Knowledge 1: Pre-Rot Threshold Is Model AND Task Specific
Peak says "128K-200K" but emphasizes this requires evaluation for YOUR model and YOUR task. The number isn't universal—it's discovered through measurement. Most teams use the stated context limit and wonder why agents degrade; experts find the actual working limit.

## Tacit Knowledge 2: Compaction Preserves Behavioral Examples
The reason to compact OLD context while keeping NEW context full isn't just about relevance—it's about maintaining behavioral examples. The model needs to see correct tool usage format in recent context or it will output compacted formats inappropriately.

## Tacit Knowledge 3: Dynamic Tool Loading Breaks More Than It Fixes
RAG-based tool loading seems elegant but causes two critical problems: KV cache invalidation and orphaned tool references in history. The "dumb" solution (fixed atomic tools + sandbox extensibility) works better in practice.

## Tacit Knowledge 4: Open Source Models Are Often More Expensive
Counterintuitive truth: at scale, frontier models with distributed KV cache infrastructure can be cheaper than self-hosted open models without that infrastructure. The "cost savings" of open source don't account for the infrastructure gap.

## Tacit Knowledge 5: MCP Changes Everything About Fine-Tuning
Model Context Protocol creates an infinitely extensible action space. Fine-tuning on a fixed action space becomes obsolete when your action space is dynamic. This is why Manus doesn't fine-tune.

## Tacit Knowledge 6: Benchmark-Product Misalignment Is Real
Manus found that models scoring high on GAIA benchmark weren't preferred by users. The evaluation that matters is user ratings, not academic benchmarks. Public benchmarks measure the wrong things for production agents.

## Tacit Knowledge 7: The ToDo.md Pattern Was Wasteful
Manus initially used todo.md files for planning—and found one-third of agent actions were just updating the todo list. Structured planning via a separate planner agent eliminated this waste.

---

## Hall of Fame Exemplars

### Exemplar 1: The "Manus Codebase Navigator" Agent Architecture
**Context**: A developer agent designed to navigate and modify large codebases (tens of thousands of files, millions of lines). Initial attempts suffered from context window overflow and frequent hallucinations regarding file contents and project structure.
**Lance & Peak's Solution**:
An architecture employing:
1.  **Compaction Sequencing Intelligence (Pattern 5)**: Oldest 70% of file read/write operations were compacted to `file_path: [hash]` references, while the most recent 30% (last 10 interactions) remained in full.
2.  **The Reversibility Principle (Pattern 4)**: A `git` hash or file system timestamp was attached to every compacted file reference, allowing full retrieval via a `read_file_at_version` tool.
3.  **File System as Coordination Layer (Pattern 12)**: Instead of passing full file contents or diffs in messages, agents wrote changes to temporary files (`temp/agent_diffs_XYZ.patch`) and passed only the file path to the next sub-agent or for user review.
4.  **Schema-Structured Summarization (Pattern 6)**: A dedicated `ProjectOverview` sub-agent summarized overall project status into a fixed schema: `{ "modified_files": [], "pending_tasks": [], "key_blockers": [] }`
**What makes this excellent**: This design achieved a 65% reduction in context window usage during complex refactoring tasks, zero information loss, and a 40% reduction in "context confusion" errors compared to prior iterations. The reversibility and file-system-centric approach ensured robust, scalable operation without hitting pre-rot thresholds.

### Exemplar 2: The "Manus Data Analyst" Agent Toolset
**Context**: An agent designed to perform complex data analysis and generate reports. Initial versions had a massive tool list (over 50 functions) leading to frequent incorrect tool calls and "tool confusion."
**Lance & Peak's Solution**:
Refactoring the toolset based on:
1.  **Atomic Function Philosophy (Pattern 8)**: Reduced the core toolset to 7 atomic functions: `read_csv`, `write_csv`, `run_python_script`, `read_text_file`, `write_text_file`, `list_directory`, `shell_command`. All complex operations (e.g., "plot histogram," "calculate correlation") were composed from `run_python_script` with dynamically generated Python code.
2.  **Agent-as-Tool Pattern (Pattern 9) & Schema-as-Contract (Pattern 10)**: A "ReportGenerator" sub-agent was created. The main agent would call it with a `generate_report` tool, passing a strict JSON schema for the report content (`{ "title": str, "sections": [{ "heading": str, "content": str, "data_source": str }] }`). The sub-agent was constrained to output *only* data conforming to this schema.
**What makes this excellent**: This approach drastically reduced the tool calling space, virtually eliminating tool confusion. The agent became more robust and predictable. The "ReportGenerator" sub-agent, operating under a strict schema, ensured consistent, high-quality report outputs, making the complex task of report generation a composable, reliable step.

### Anti-Exemplar: The "Generalist Chatbot" Context Strategy
**Context**: A startup built a "generalist chatbot" that could do everything from scheduling to coding, by giving it access to every possible API and a huge context window.
**Problematic Design**:
1.  **Ignoring Pre-Rot Threshold (Anti-Pattern)**: The agent was given a 500K context window and expected to perform optimally throughout, without any measurement of degradation.
2.  **Free-Form Summarization (Anti-Pattern)**: For long conversations, the agent would perform ad-hoc, free-form summarization, often losing critical details or misinterpreting user intent.
3.  **Dynamic Tool Loading (Anti-Pattern)**: Tools were loaded based on keyword matching in user prompts, leading to KV cache invalidation and unpredictable tool availability.
4.  **Anthropomorphic Design (Anti-Pattern)**: The agent was designed with "roles" like "calendar assistant," "coding expert," etc., leading to internal conflicts and difficulty in handoffs.
**Why it's mediocre**: Despite a large context window, the agent frequently "forgot" earlier parts of the conversation, made incorrect tool calls, and produced generic, unhelpful responses. User satisfaction was low due to perceived "memory loss" and inconsistent behavior. The architecture was fragile and expensive to run, with no clear path for improvement beyond "use a bigger model."

## Signature Moves

*   **The Pre-Rot Threshold Probe**: Before deploying any agent, Lance & Peak will run controlled experiments, incrementally feeding the model larger contexts (e.g., from 1K to 200K tokens) and meticulously measuring a task-specific output quality metric, plotting the degradation curve to identify the *actual* performance cliff for that model and task. → **Deploy when**: Evaluating new models, designing a new agent architecture, or debugging unexplained agent performance drops.
*   **The Reversibility Audit**: For any proposed context reduction (compaction or summarization), they will immediately challenge: "What is the unique identifier or external state needed to fully reconstruct the original information?" If no such identifier or state exists, the proposed reduction is rejected or redesigned. → **Deploy when**: Designing context management strategies, defining tool outputs, or reviewing existing agent memory mechanisms.
*   **The Atomic Tool Scrutiny**: When presented with a potential new tool or function call, they will ruthlessly question its necessity: "Can this capability be achieved by composing existing, more atomic operations? Can the sandbox + a text editor already do this?" The default bias is always towards fewer, simpler tools. → **Deploy when**: Expanding an agent's capabilities, designing new tool sets, or refactoring existing ones.
*   **The Schema-First Contract**: Before any complex operation involving data exchange (e.g., sub-agent output, summarization, tool return values), they will first define a strict, machine-readable output schema. This schema acts as the explicit contract for data structure and content. → **Deploy when**: Designing multi-agent systems, implementing summarization, or defining API/tool return types.
*   **The File System Bypass**: When any agent needs to process or generate information exceeding a small, predefined token limit (e.g., >10K tokens), they will immediately design the system to write that information to the sandbox file system and pass only the file path, rather than attempting to pass the full content in a message. → **Deploy when**: Handling large files, long logs, extensive data sets, or complex intermediate processing results within agent workflows.

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
| :------------------------------ | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Context Efficiency Ratio** | Achieves <30% context reduction without clear metrics on information loss. | Achieves 40-60% context reduction with documented information recoverability for compacted elements. | Achieves 60%+ context reduction across complex tasks (e.g., 10+ turns, large files) while maintaining 100% information recoverability for compacted context and minimal loss for schema-structured summaries. Demonstrates quantifiable pre-rot threshold extension. |
| **Information Reversibility** | Compacted context elements are often lost or require significant guesswork to reconstruct. | Key compacted context elements have associated identifiers, allowing reconstruction with some manual intervention or specific tool calls. | Every compacted context element explicitly includes a unique, verifiable identifier (e.g., file path, version hash, query string) that allows automated, lossless reconstruction via a single atomic tool call. |
| **Tool Space Atomicity** | Agent uses 20-30+ tools; some tools overlap or could be composed from simpler primitives. | Agent uses 10-20 tools, most are distinct; some composition is evident. | Agent uses <10 truly atomic tools; all complex operations are demonstrably composed from these primitives, with a clear rationale for why each tool cannot be further decomposed. No "context confusion" due to tool overload. |
| **Schema Enforcement Rigor** | Summarization is free-form or schemas are loosely defined, leading to inconsistent outputs. | Schemas are defined for key outputs but might be flexible or occasionally violated by sub-agents. | All summarization and sub-agent outputs are strictly governed by explicit, machine-readable schemas, with robust error handling for non-conformance. The main agent can reliably parse and utilize these structured outputs. |
| **Degradation Curve Awareness** | Relies on model's stated context limit; performance degradation is observed but not quantified. | Has run basic tests to identify a rough "pre-rot" threshold, but without comprehensive task-specific evaluation. | Has performed rigorous, task-specific evaluation to plot the model's performance degradation curve against context size, identifying the precise pre-rot threshold and designing context management strategies to operate well within optimal bounds. |
| **Inter-Agent Coordination Protocol** | Agents primarily pass large amounts of raw text or data directly through message history. | Agents pass smaller data chunks via messages, but larger items occasionally cause context bloat. | All data exceeding a low token threshold (e.g., 5K tokens) is consistently written to and read from the sandbox file system, with only file paths passed in messages, ensuring efficient, scalable inter-agent communication. |
| **Future-Proofing Score** | Architecture is brittle; swapping to a stronger model yields minimal or inconsistent gains. | Swapping to a stronger model shows some improvement, but the architecture still presents bottlenecks. | Architecture demonstrates significant (>30%) and consistent performance improvements when migrating to stronger underlying models, indicating that the context engineering is not the limiting factor. |
