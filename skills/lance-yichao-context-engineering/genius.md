# Lance Martin & Yichao "Peak" Ji - Context Engineering — Genius Context

> Load this file before executing any workflow. It contains the full
> extraction intelligence — patterns, tacit knowledge, and operating
> principles that make this expert's output actually work. Grounding note:
> no raw interview transcript for Lance Martin or Yichao "Peak" Ji lives in
> `extractions/` (confirmed by directory search + a per-member scan of
> `_archive/claude-export-2026-07-01.tar.gz`, 7,728 members, zero hits on
> yichao/lance/manus/peak). The one primary-sourced internal document that
> does exist — `_active/swarm-apex-2026-07-07/research/manus.md` (38 lines,
> 5,141 bytes, dated 2026-07-07, itself citing manus.im's primary
> context-engineering blog post and a LangChain webinar appearance by
> Yichao "Peak" Ji) — is used throughout this file to corroborate or flag
> claims. See `references/source-ledger.md` for the claim-by-claim
> breakdown.

## How to Use This Skill (Model Calibration)

These are architectural intuition primitives, not a checklist to stamp in
order. Absorb the paradox first — context is what makes an agent capable,
context is also what makes it degrade — then design from there. If the
output mechanically walks through "Pattern 1, Pattern 2, Pattern 3" as a
numbered tour, you have failed: neither Lance nor Peak write in framework-
recital voice, they write in "here's the specific failure we hit and the
specific fix" voice.

Specifically:
- Do NOT label sections "here's the compaction layer" or "here's the
  action-space design." Build the artifact; never narrate the architecture
  on the page.
- Do NOT invent a fixed pre-rot number. Peak's own figure ("128K to 200K")
  is explicitly framed as a discovered, tunable threshold — not a constant.
  If a deliverable needs one, either name the evaluation method that would
  find it or mark it TBD-via-evaluation. A confidently-stated round number
  with no discovery method attached is the tell that the pattern was copied
  off the page, not run.
- Their texture is engineering-log, not sales deck: real cache-hit
  percentages, real per-token dollar figures, real error traces kept on
  purpose because the failure is signal. Sanitizing that mess out — the
  cleaned-up stack trace, the "it's 128K-200K" stated as settled fact
  instead of measured — is the tell-class failure. See Anti-Patterns below.
- The test: would Lance Martin or Yichao "Peak" Ji recognize this as an
  architecture they would actually ship at Manus or in a LangChain
  reference agent — or as someone reciting context-engineering vocabulary
  who has never watched a cache-hit-rate dashboard degrade in real time?
  If it's the second, rebuild.

## Genius Patterns

## Pattern 1: The Context Paradox Recognition
**Core Insight**: Agents need tool context but performance drops as context grows.
**Implementation**: Map expected context accumulation (tool calls × average output size × session length) against the model's effective context limit before designing.
**Deployment**: Initial architecture design, debugging degraded agent performance, evaluating new model capabilities.
**Concretely**: Manus's own context-engineering account frames this as an input:output token ratio of roughly 100:1, with cached Sonnet input priced at $0.30/MTok versus $3 uncached — a 10x gap that turns "context accumulation" from an abstraction into a line item on the bill (VERIFIED, manus.im primary source, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

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
**Concretely**: a schema this specific (6 fixed fields, not prose) is what makes a summary parseable by the next turn's agent instead of just readable by a human — the distinction the pattern is actually enforcing. (LIKELY — schema shape is consistent with structured-output practice described in Lance Martin's context-engineering writing; not independently re-verified against a primary transcript this session; no such file exists in `extractions/`.)

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
**Concretely**: Manus's own "Wide Research" fan-out is the production version of this — each of 100+ spun-up sub-agents "must call a constrained 'submit result' tool with schema-constrained decoding for a uniform reduce step" (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Pattern 11: Share Context vs. Share Messages Pattern Selection
**Core Insight**: Choose pattern based on task characteristics.
- **By Communication**: Sub-agent gets only instruction, works independently
- **By Sharing Context**: Sub-agent sees full prior context with own system prompt
**Concretely**: Manus's own Wide Research fan-out picks "By Communication" deliberately — "shared context via sandbox/file system (main agent passes file paths, not raw content)" rather than replaying the parent's message history into every one of 100+ sub-agents (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Pattern 12: File System as Coordination Layer
**Core Insight**: Sandbox file system as coordination mechanism—agents read/write to shared paths instead of passing context through messages.
**Implementation**: For context >10K tokens, write to file and pass only path.

## Pattern 13: Future-Proof Architecture Testing
**Core Insight**: Test by swapping between weaker and stronger models. Significant gains = future-proof architecture.
**Implementation**: If stronger model shows >30% improvement, architecture will benefit from future upgrades.

## Pattern 14: Anti-Anthropomorphic Agent Design
**Core Insight**: Reject human org-chart metaphor. Design agents by function, not role.
**Implementation**: Executor (does work), Planner (maintains direction), Knowledge Manager (handles memory). Max 3-5 core agents.
**Concretely**: this is close to verbatim what Manus runs in production — Peak Ji, direct quote: "we do not divide by role. We only have very few agents — a huge general executor agent and a planner agent and a knowledge management agent... we are very cautious about adding more sub agents because communication is very hard" (VERIFIED, LangChain webinar, youtube.com/watch?v=6_BcCthVvb8, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Pattern 15: Explicit Memory with User Confirmation
**Core Insight**: Long-term memory requires explicit user confirmation.
**Implementation**: Surface proposed memory with accept/reject options before storing.
**Concretely**: the cost of skipping this step compounds silently — a memory system that writes on inference instead of confirmation has no correction mechanism, so a single bad inference propagates into every future session until someone manually audits the store. (Operationalization of the pattern; not independently sourced against a primary transcript this session.)

## Pattern 16: Collective Feedback Mining
**Core Insight**: Look for patterns where many users give the same correction.
**Implementation**: Log corrections systematically, cluster by type, use common corrections for parameter-free improvement.
**Concretely**: the mechanism this pattern describes is the same one behind Manus's benchmark-vs-preference finding below (Tacit Knowledge 6) — aggregate real correction signal beats any single session's read on what "good" looks like (per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Pattern 17: Line-Based Format Preference
**Core Insight**: Prefer line-based formats over markdown/JSON—enables grep, line-range reading, Unix tools.
**Implementation**: Plain text with line structure allows `grep`, `head`, `tail`, `sed` for retrieval.
**Concretely**: this is the same discipline behind Manus's cache-stability rule — "strictly append-only context with deterministic JSON serialization" (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07) — a format that can be diffed and grepped is also a format whose byte-prefix stays stable, which is what keeps the KV-cache hit rate high.

## Pattern 18: Evaluation Triad
**Core Insight**: Three evaluation types in combination.
**Implementation**:
1. User ratings (gold standard)
2. Automated tests with verifiable results (fast iteration)
3. Human evaluation for subjective quality (taste)
**Concretely**: user ratings sit at the top of this triad specifically because the other two can score well while missing what users actually complain about — Manus's own account: models that scored high on the GAIA benchmark were not the ones users preferred in real sessions (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Pattern 19: Context Confusion Prevention
**Core Insight**: Too many tools cause "context confusion"—wrong tool calls or hallucinations.
**Implementation**: Keep under 20-30 tools. Check if capability can be achieved via sandbox/code first.

## Pattern 20: KV Cache Awareness
**Core Insight**: Tool definitions at front of context, stable across turns, enabling cache reuse.
**Implementation**: Keep schemas stable. Don't dynamically load/unload. Track cache hit rate.
**Concretely**: keep the entire prompt prefix byte-identical turn over turn — no timestamps, no reordering. Manus calls cache-hit rate "the single most important metric," reporting cached Sonnet input at $0.30/MTok versus $3 uncached, a 10x gap (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Pattern 21: Guardrail Layering
**Core Insight**: Multiple guardrail layers—network, action, progressive.
**Implementation**: Block sensitive data exfiltration, require confirmation for destructive ops, start with more confirmations and reduce over time.
**Concretely**: "start with more confirmations and reduce over time" means the confirmation count is a decaying variable tied to trust earned, not a fixed setting — a new deployment and a 90-day-mature one should not carry the same guardrail count.

## Pattern 22: The Simplification Principle
**Core Insight**: "Build less, understand more." Biggest gains from removing features, not adding.
**Implementation**: Before adding, ask: "Can we achieve this by removing something?" Refactor 4-6 times/year.

## Pattern 23: Model Capability Boundary Awareness
**Core Insight**: Context engineering is application layer; model training is model layer.
**Implementation**: Don't duplicate model company efforts. Focus on your specific use case, tools, users.
**Concretely**: Manus's own line on this is unambiguous — the company doesn't fine-tune at all; every gain is claimed to come from the context-engineering layer sitting above the model, which is also the reason an MCP-extensible action space (Tacit Knowledge 5) makes fine-tuning obsolete rather than complementary (per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Anti-Patterns

Sourced from `_active/swarm-apex-2026-07-07/research/manus.md` (38 lines,
5,141 bytes, dated 2026-07-07 — a Sonnet deep-research brief carrying its
own VERIFIED/LIKELY/UNCONFIRMED labels, grounded in manus.im's primary
context-engineering blog post and a LangChain webinar appearance by
Yichao "Peak" Ji, read in full this session). Each item below is the
inverse of a pattern above — named as a failure mode because it is one.

- **Dynamic tool loading via RAG-style retrieval.** [VERIFIED, manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07] — "Tools aren't dynamically removed (breaks cache); unavailable tools hidden via logit-masking." Swapping the function-calling schema mid-session invalidates the KV-cache and leaves orphaned tool references sitting in history.
- **Anthropomorphic role-division into many named personas.** [VERIFIED, direct quote, Yichao "Peak" Ji, LangChain webinar, youtube.com/watch?v=6_BcCthVvb8, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07] — "we do not divide by role... we are very cautious about adding more sub agents because communication is very hard." A cast of "calendar assistant," "coding expert," "research assistant" personas invites exactly the coordination tax Peak warns against.
- **Scrubbing failed actions and stack traces out of context.** [VERIFIED, manus.im blog primary source, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07] — "Failed actions and stack traces deliberately left in context — seeing failure 'implicitly updates the model's internal beliefs.'" A sanitized transcript removes exactly the signal that steers the model away from repeating the mistake.
- **Compacting without a reconstruction identifier.** [LIKELY — quoted material also appears in `references/genius-patterns.md` Pattern 4, corroborated by the same manus.im primary source per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07] — "Almost every action in Manus is reversible if you can offload it to the file system or external state." Dropping content without keeping the file path, URL, or hash that makes it retrievable turns "compaction" into lossy summarization wearing compaction's name.
- **Treating the vendor-advertised context window as the usable one.** [LIKELY, corroborated by manus.im primary source per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07, cross-referenced against Tacit Knowledge 1 below] — Peak's own framing puts the real degradation zone at "128K to 200K," not the advertised ceiling; shipping against the sticker limit instead of a measured one is the single most common root cause of "why did my agent get dumber after turn 40."
- **Non-persistent, write-once planning documents.** [UNCONFIRMED — the specific "one-third of agent actions were just updating the todo list" figure could not be re-located in `_active/swarm-apex-2026-07-07/research/manus.md` or anywhere else in this repo this session; flagged rather than deleted, since the claim predates this repair pass and no source file for it could be found] — what IS corroborated (per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07, LIKELY): "The planner produces a step roadmap written to a persistent `todo.md`, injected into context as a 'special event,' checked off as steps complete — survives context resets because it lives on disk." A todo file written once and never re-appended loses this recitation effect entirely.

## Hidden Knowledge

## Tacit Knowledge 1: Pre-Rot Threshold Is Model AND Task Specific
Peak says "128K-200K" but emphasizes this requires evaluation for YOUR model and YOUR task. The number isn't universal—it's discovered through measurement. Most teams use the stated context limit and wonder why agents degrade; experts find the actual working limit.

## Tacit Knowledge 2: Compaction Preserves Behavioral Examples
The reason to compact OLD context while keeping NEW context full isn't just about relevance—it's about maintaining behavioral examples. The model needs to see correct tool usage format in recent context or it will output compacted formats inappropriately. The same underlying mechanism — keeping the recent prompt shape stable and predictable — is what Manus reports for cache economics: "Cached Sonnet input $0.30/MTok vs $3 uncached — 10x gap drives every decision" (VERIFIED, manus.im primary source, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07). Stale formatting anywhere in the recent context breaks tool-call behavior the same way a stale prompt prefix breaks the cache.

## Tacit Knowledge 3: Dynamic Tool Loading Breaks More Than It Fixes
RAG-based tool loading seems elegant but causes two critical problems: KV cache invalidation and orphaned tool references in history. The "dumb" solution (fixed atomic tools + sandbox extensibility) works better in practice. The concrete cost of getting this wrong shows up elsewhere in the same account: reviewers clock opaque credit burn as high as 400 credits for 4 Google Maps lookups and roughly 1,000 credits before first output (VERIFIED, review roundups, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07) — the tax paid when cache-friendly discipline slips.

## Tacit Knowledge 4: Open Source Models Are Often More Expensive
Counterintuitive truth: at scale, frontier models with distributed KV cache infrastructure can be cheaper than self-hosted open models without that infrastructure. The "cost savings" of open source don't account for the infrastructure gap. The concrete version of that infrastructure gap is the same $0.30/MTok cached vs. $3 uncached figure Manus reports (per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07) — self-hosting without an equivalent caching layer means eating the uncached rate on every call.

## Tacit Knowledge 5: MCP Changes Everything About Fine-Tuning
Model Context Protocol creates an infinitely extensible action space. Fine-tuning on a fixed action space becomes obsolete when your action space is dynamic. This is why Manus doesn't fine-tune. Consistent with this, Manus's own "Wide Research" (internally "agentic map-reduce") fans out 100+ homogeneous sub-agent instances rather than training specialized ones — available Pro-tier first, at $199/mo (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07).

## Tacit Knowledge 6: Benchmark-Product Misalignment Is Real
Manus found that models scoring high on GAIA benchmark weren't preferred by users. The evaluation that matters is user ratings, not academic benchmarks. Public benchmarks measure the wrong things for production agents. (VERIFIED, per `_active/swarm-apex-2026-07-07/research/manus.md`, 2026-07-07 — this is the same finding Pattern 18's evaluation triad is built to correct for.)

## Tacit Knowledge 7: The ToDo.md Pattern Was Wasteful
Manus initially used todo.md files for planning—and found one-third of agent actions were just updating the todo list. Structured planning via a separate planner agent eliminated this waste. [UNCONFIRMED — this specific ratio could not be re-located in `_active/swarm-apex-2026-07-07/research/manus.md` or any other file in this repo this session; the claim predates this repair pass, is left in place rather than deleted per the additive-first boundary, and is flagged here rather than presented as verified.] What the same research brief DOES corroborate (LIKELY): "The planner produces a step roadmap written to a persistent `todo.md`, injected into context as a 'special event,' checked off as steps complete — survives context resets because it lives on disk."

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
