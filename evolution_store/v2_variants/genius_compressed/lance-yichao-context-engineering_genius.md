# Lance Martin & Yichao "Peak" Ji — Genius Context

> Load before executing any workflow. Full extraction intelligence.

## Core Operating System

Context engineering is the discipline of managing what an AI agent sees, remembers, and forgets. The core tension: agents need tool context to act but performance degrades as context grows. The solution is systematic compaction (reversible information offloading), atomic tool design, and schema-enforced structure — always measured against task-specific degradation curves, never assumed from model specs.

---

## Genius Patterns (Compressed)

### GP1: The Context Paradox Recognition
Agents need tool context but performance drops as context grows. Map expected context accumulation (tool calls x avg output size x session length) against effective context limit before designing any architecture.

### GP2: Pre-Rot Threshold Detection
"128K-200K" is the degradation zone — treat as a tunable parameter discovered through evaluation, not a fixed number. Run controlled experiments incrementally increasing context while measuring output quality. Plot the degradation curve and mark the inflection point.

### GP3: Compaction vs. Summarization Separation
Compaction is reversible (information externalized but recoverable); summarization is irreversible (information lost). Define FULL and COMPACT formats for every tool call. Compaction replaces when external state can reconstruct. Target 40-70% reduction with 100% recoverability.

### GP4: The Reversibility Principle
For each tool, identify the unique identifier (file path, URL, query) that allows reconstruction. Compact representations must preserve this identifier. "Almost every action is reversible if you can offload it to the file system or external state."

### GP5: Compaction Sequencing Intelligence
Compact oldest context first while preserving recent tool calls in full — maintaining "fresh few-shot examples" of proper tool usage. Apply to oldest 50% while keeping newest 50% in full format.

### GP6: Schema-Structured Summarization
Never use free-form summarization. Always define structured schema with fields: `files_modified`, `user_goal`, `current_progress`, `where_left_off`, `key_findings`, `pending_actions`.

### GP7: The Three-Layer Action Space
Layer 1 (Function Calling): 10-20 atomic operations only. Layer 2 (Sandbox Utilities): CLI tools via shell, extensible. Layer 3 (Packages/APIs): Computation-heavy in code. Divide capabilities across these abstraction levels.

### GP8: Atomic Function Philosophy
Ruthlessly minimize function calling space to truly atomic operations. Ask of every tool: "Can this be composed from more atomic operations?" Shell + text editor = Turing complete.

### GP9: Agent-as-Tool Pattern
Complex operations become sub-agent calls with structured output schemas. Wrap multi-step tasks as "agent as tool" with constrained output schema defined by main agent.

### GP10: Schema-as-Contract for Sub-Agents
Main agent defines output schema upfront. Sub-agents use `submit_result` with constrained decoding. Think of multi-agent operations as generating structured spreadsheets.

### GP11: Share Context vs. Share Messages
Choose pattern by task: By Communication = sub-agent gets only instruction, works independently. By Sharing Context = sub-agent sees full prior context with own system prompt.

### GP12: File System as Coordination Layer
Sandbox file system as coordination mechanism — agents read/write to shared paths instead of passing context through messages. For context >10K tokens, write to file and pass only the path.

### GP13: Future-Proof Architecture Testing
Test by swapping between weaker and stronger models. If stronger model shows >30% improvement, architecture will benefit from future upgrades and is future-proof.

### GP14: Anti-Anthropomorphic Agent Design
Reject human org-chart metaphor. Design agents by function: Executor (does work), Planner (maintains direction), Knowledge Manager (handles memory). Max 3-5 core agents.

### GP15: Explicit Memory with User Confirmation
Long-term memory requires explicit user confirmation. Surface proposed memory with accept/reject options before storing.

### GP16: Collective Feedback Mining
Look for patterns where many users give the same correction. Log corrections systematically, cluster by type, use common corrections for parameter-free improvement.

### GP17: Line-Based Format Preference
Prefer line-based formats over markdown/JSON — enables grep, line-range reading, Unix tools. Plain text with line structure allows standard tool retrieval.

### GP18: Evaluation Triad
Three evaluation types in combination: (1) User ratings (gold standard), (2) Automated tests with verifiable results (fast iteration), (3) Human evaluation for subjective quality (taste).

### GP19: Context Confusion Prevention
Too many tools cause "context confusion" — wrong tool calls or hallucinations. Keep under 20-30 tools. Check if capability can be achieved via sandbox/code first.

### GP20: KV Cache Awareness
Tool definitions at front of context, stable across turns, enabling cache reuse. Keep schemas stable. Don't dynamically load/unload. Track cache hit rate.

### GP21: Guardrail Layering
Multiple guardrail layers: network (block sensitive data exfiltration), action (require confirmation for destructive ops), progressive (start with more confirmations, reduce over time).

### GP22: The Simplification Principle
"Build less, understand more." Biggest gains from removing features, not adding. Before adding, ask: "Can we achieve this by removing something?" Refactor 4-6 times/year.

### GP23: Model Capability Boundary Awareness
Context engineering is application layer; model training is model layer. Don't duplicate model company efforts. Focus on your specific use case, tools, users.

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Pre-rot threshold is model AND task specific — "128K-200K" requires evaluation for YOUR model and YOUR task | Model selection, capacity planning — always measure, never assume |
| HK2 | Keeping NEW context full preserves behavioral examples — model needs to see correct tool usage in recent context | Compaction sequencing — compact old, keep recent full |
| HK3 | Dynamic tool loading breaks more than it fixes — causes KV cache invalidation and orphaned tool references | Use fixed atomic tools + sandbox extensibility instead of RAG-based tool loading |
| HK4 | Open source models are often more expensive at scale — frontier models with distributed KV cache infra can be cheaper | Cost analysis for model selection — account for infrastructure gap |
| HK5 | MCP creates infinitely extensible action space — fine-tuning on fixed action space becomes obsolete | Architecture decisions — favor MCP extensibility over fine-tuning |
| HK6 | Models scoring high on GAIA benchmark weren't preferred by users — public benchmarks measure wrong things for production | Use user ratings as gold standard, not academic benchmarks |
| HK7 | ToDo.md files wasted one-third of agent actions just updating the list — structured planning via separate planner agent eliminated waste | Agent planning — use dedicated planner agent, not inline todo files |

---

## Signature Moves

1. **The Pre-Rot Threshold Probe** — Runs controlled experiments incrementally feeding larger contexts while measuring task-specific quality metrics, plotting the degradation curve. Deploy when evaluating models or debugging performance drops.
2. **The Reversibility Audit** — Challenges every proposed context reduction: "What identifier allows full reconstruction?" If none exists, redesign. Deploy when designing context management strategies.
3. **The Atomic Tool Scrutiny** — Ruthlessly questions every new tool: "Can this be composed from existing atomic operations?" Default bias toward fewer, simpler tools. Deploy when expanding capabilities.
4. **The Schema-First Contract** — Defines strict machine-readable output schema before any complex data exchange between agents. Deploy when designing multi-agent systems or summarization.
5. **The File System Bypass** — For information exceeding ~10K tokens, writes to sandbox file system and passes only the path. Deploy when handling large files, logs, or intermediate results.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| **Context Efficiency Ratio** | <30% reduction, no info loss metrics | 40-60% reduction with documented recoverability | 60%+ reduction across complex tasks, 100% recoverability for compacted, minimal loss for summaries |
| **Information Reversibility** | Compacted elements often lost or require guesswork | Key elements have identifiers, some manual intervention needed | Every compacted element has unique verifiable identifier for automated lossless reconstruction |
| **Tool Space Atomicity** | 20-30+ tools with overlap | 10-20 distinct tools, some composition | <10 atomic tools, all complex ops composed from primitives, zero context confusion |
| **Schema Enforcement Rigor** | Free-form or loosely defined schemas | Schemas defined for key outputs, occasionally violated | All outputs governed by strict machine-readable schemas with error handling |
| **Degradation Curve Awareness** | Relies on stated context limit | Basic pre-rot threshold identified | Rigorous task-specific evaluation with plotted degradation curve and precise threshold |
| **Inter-Agent Coordination** | Large raw text passed through messages | Smaller chunks via messages, occasional bloat | All data >5K tokens via file system, only paths in messages |
| **Future-Proofing Score** | Brittle; stronger model yields minimal gains | Some improvement with stronger model | >30% consistent improvement on model upgrade — architecture is not the bottleneck |
