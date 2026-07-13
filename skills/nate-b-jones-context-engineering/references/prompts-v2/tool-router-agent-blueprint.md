---
name: "Nate B. Jones — Tool Router Agent Blueprint"
source_prompt: born-v2
skill: nate-b-jones-context-engineering
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are designing Nate B. Jones's Tool Router pattern: a dynamic tool selection architecture that loads only task-relevant tool definitions into an agent's context window, eliminating prompt bloat from unused tool schemas. This is the highest-leverage single vector in the Context Compression Playbook for systems with 50+ tool definitions — the source methodology cites 50-95% reduction of tool-context tokens as the expected range, well above the 10-40% typical of the other four vectors. Applicable directly to any system with numerous MCP servers/tool sets where most invocations use a small fraction of what's loaded.

## Input Required

- **[TOOL INVENTORY SOURCE]** — the full list of available tools/MCP servers with their schemas
- **[USAGE DATA]** — typical task distribution (which tools get used most, at what frequency) — estimate from logs if available, else flag as estimated
- **[EMBEDDING CAPABILITY]** — availability of an embedding model (sentence-transformers, OpenAI embeddings) or fallback to keyword/TF-IDF matching for MVP
- **[DEPLOYMENT TIMELINE PREFERENCE]** — whether an MVP (rule-based, hours) or production (semantic, days) router is wanted first

## Execution Protocol

**Step 1 — Tool Inventory.** Catalog every available tool: name, source (core / which MCP server), one-line description, average monthly use (estimated if no logs), schema size in tokens. Sum the total tool schema tokens if all tools were loaded simultaneously — this is the "before" baseline that every later reduction claim is measured against.

**Step 2 — Tool Clustering.** Group tools by functional domain (example clusters from the source methodology: File Operations, Terminal, Browser, Search, [Platform]-specific tools like Notion, Image, Research, Cloud/Deploy, Design). Clustering is the foundation both the rule-based and semantic router build on.

**Step 3 — Design the Selection Architecture.** Choose one of three options, or justify the hybrid:
- Option A — Rule-Based Router (MVP, hours to deploy): a keyword/intent-to-cluster mapping table (e.g., "write_code" → [file_ops, terminal, search]; "research" → [search, research, browser]). Simple, fast, no embedding infra required.
- Option B — Semantic Router (production, days to deploy): pre-compute embeddings for every tool's description; on a task, embed the task intent and return the top-K most similar tools by cosine similarity.
- Option C — Hybrid (recommended default): core tools (file ops, terminal, search) always loaded regardless of task, plus semantic selection layered on top for specialized/less-common tools.

**Step 4 — Define the Always-On Set.** Name the tools that are ALWAYS included regardless of task intent — foundational capabilities like file read/write, terminal execution, grep/list, web search. Estimate their combined token cost (source example: ~1,500 tokens for ~8 always-on tools). Everything outside this set loads on demand only.

**Step 5 — Design the Fallback Mechanism.** If the agent requests a tool not in its currently-loaded set: detect the miss, query the full tool index for the requested tool, inject its schema on the next turn, and log the cache miss for future routing improvement. Track the cache miss rate over time — a tool that consistently causes misses should be promoted into a broader cluster or the always-on set.

**Step 6 — Token Math & Validation.** Compute before/after: current state (all N tools × avg schema size) versus target state (always-on set + dynamic set). Source example ratio: ~100 definitions × ~200 tokens (20,000 total) down to ~13 tools loaded per invocation (~2,600 total) — an 87% reduction in tool-token overhead. Validate against real usage: run 20 representative tasks with the Tool Router, measure cache miss rate (target <10%), compare task success rate against an all-tools-loaded baseline, measure latency improvement from the reduced context.

**Step 7 — Implementation Plan.** Day 1: catalog tools, measure current overhead. Day 2: implement Option A (rule-based) as MVP. Day 3: test on 10 representative tasks, measure miss rate. Day 4: refine clusters based on observed miss patterns. Day 5: if miss rate exceeds 10%, implement Option B (semantic) for specialized tools. Week 2: monitor in production, track miss rate, adjust the always-on set based on real data.

## Output Contract

Deliver an architecture document with:
1. Complete tool inventory (name, source, description, usage frequency, schema size) with total baseline token count
2. Clustering map (functional domains and their member tools)
3. Selection algorithm specification — the chosen option (A/B/C) with rationale for why it fits this system
4. Always-on set definition with combined token estimate
5. Fallback mechanism design (miss detection, injection, logging, promotion criteria)
6. Token math (before/after, % reduction, worked from real numbers not the generic 87% example)
7. Validation results (cache miss rate, task success rate comparison, latency)
8. Implementation timeline (Day 1 through Week 2, adapted to the target system's actual constraints)

## Output Skeleton

```
# Tool Router Agent Blueprint — [TARGET SYSTEM]

## Tool Inventory
| Tool Name | Source | Description | Avg Monthly Use | Schema Size (tokens) |
|---|---|---|---|---|
Total baseline: [N tools] x [avg tokens] = [total tokens]

## Tool Clustering
| Cluster | Member Tools |
|---|---|

## Selection Architecture
Chosen: [A / B / C]
Rationale: [why this option fits the target system's constraints]
[implementation sketch for chosen option]

## Always-On Set
| Tool | Rationale for always-on |
|---|---|
Combined token cost: [n]

## Fallback Mechanism
Miss detection: [how]
Injection: [when/how the missing schema gets added]
Cache miss logging: [what's tracked]
Promotion rule: [threshold for moving a tool to always-on or a broader cluster]

## Token Math
Before: [N] tools x [avg tokens] = [total]
After: Always-on [n] tools ([tokens]) + Dynamic [n] tools ([tokens]) = [total]
Reduction: [pct]%

## Validation Results
| Metric | Baseline (all tools) | Tool Router | Delta |
|---|---|---|---|
| Task success rate | | | |
| Cache miss rate | — | | |
| Latency | | | |

## Implementation Timeline
Day 1: [ ] | Day 2: [ ] | Day 3: [ ] | Day 4: [ ] | Day 5: [ ] | Week 2: [ ]
```

## Quality Gate

- [ ] Tool inventory covers the full actual tool set of the target system, not a sample or the generic example list from the methodology
- [ ] Token math is computed from the target system's real tool count and schema sizes, not copy-pasted from the source's 100-tool/87%-reduction example
- [ ] The always-on set is justified per tool (why this tool is foundational), not asserted as a block
- [ ] Cache miss rate and task success comparisons are reported as measured (or explicitly marked "not yet run" with a plan) — never presented as achieved without a validation step
- [ ] Fallback mechanism includes both the miss-handling flow AND the promotion criteria for graduating a frequently-missed tool into a broader cluster

## Deploy When

- The target system has 50+ tool definitions (own tools + MCP servers) creating measurable prompt bloat
- A Context Bloat Diagnostic flags tool definitions as the largest or near-largest context component
- Adding new MCP servers is becoming a tax on every invocation regardless of whether that server's tools are used
