# Genius Patterns - Lance Martin & Yichao "Peak" Ji

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
