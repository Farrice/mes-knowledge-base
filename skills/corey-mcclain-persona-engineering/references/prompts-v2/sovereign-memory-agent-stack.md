---
name: "Corey McClain × Nate B. Jones — Sovereign-Memory Agent Stack"
source_prompt: born-v2
skill: corey-mcclain-persona-engineering
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the **McClain × Nate B. Jones stack** — LLMP's identity container merged with Sovereign Memory Architecture's persistence engine. Why this combination matters: LLMP without sovereign memory produces an agent that resets every session — the persona compounds, but only if someone manually refines it. Sovereign memory without persona produces an agent that remembers everything but sounds like everyone. The stack solves both simultaneously — an agent that is both distinctive AND durable.

## Input Required

- `[AGENT_MISSION]` — singular purpose (content, strategy, copy, analysis, design)
- `[OUTPUT_CONSUMERS]` — who reads/uses what this agent produces
- `[PERSISTENCE_REQUIREMENT]` — sessions per week, to size memory-tier investment
- `[CONTEXT_BUDGET]` — token ceiling per invocation, to drive compression strategy

## Execution Protocol

### Step 1 — Purpose and Constraint Map
Lock the four inputs above before building anything.

### Step 2 — Logic Layer (McClain L1)
Workflow steps (sequential process); rules from domain best-practices; decision gates; quality checkpoints for self-evaluation. Output: `logic.md`.

### Step 3 — Library Layer (McClain L2)
3-5 few-shot exemplars of target output quality; domain knowledge files, style guides, frameworks; tool access configurations; template structures for common output types. Output: `library/`.

### Step 4 — Sovereign Memory Layer (Nate B. Jones Architecture)
Replace standard memory with the three-tier system:
- **4a — Episodic Tier**: raw interaction logs with timestamps; 90-day retention before mandatory distillation; write triggers on task completion, user correction, quality gate failure.
- **4b — Semantic Tier**: distilled patterns/rules/preferences, vector-indexed. Ebbinghaus decay function: `freshness = base_value × (1 / (1 + k × days_since_last_access))`. k-value tuning: 0.1 for slow-decay domains (brand voice), 0.5 for fast-decay domains (trending topics).
- **4c — Procedural Tier**: configurations, workflow modifications, versioned settings. No decay — permanent until explicitly updated. Includes persona refinement history (what changed and why).

Output: `memory/` — schema, decay parameters, write triggers, retrieval protocol.

### Step 5 — Context Compression Blueprint (Nate B. Jones Five Vectors)
Apply to all layers BEFORE persona installation:
1. **Quantization** — deduplicate instructions across logic/library files.
2. **Eviction & Sparsity** — distill verbose reference materials into rule-form.
3. **Architectural Redesign** — convert prose instructions to tables/rules where appropriate (never the persona).
4. **Offloading & Tiering** — classify all context as T0 (always loaded) through T3 (sub-agent retrieved).
5. **Attention Optimization** — place critical instructions at context top/bottom, not middle.

**Critical exception**: the persona document is NEVER compressed — compressing narrative prose destroys the container effect. Everything else compresses to make room for it. Output: compression map showing token budget allocation across all layers.

### Step 6 — Persona Layer (McClain L4), Memory-Aware
Build the identity container via the Persona Life Document deliverable, then add three memory-integration extensions:
- **Learning posture** — how does this person respond when they're wrong?
- **Memory philosophy** — do they hold grudges or forgive quickly? Remember details or big patterns?
- **Growth arcs** — what is this person actively trying to get better at?

Place the persona at the top or bottom of the context chain (test both). Ensure it's referenced in the router prompt but never summarized or compressed.

### Step 7 — Integration and Validation
Wire the five layers: Logic → Library → Memory (sovereign) → Compression → Persona (container). Run five tests:
1. **Vanilla comparison** — identical task with and without the full stack, controlled-delete between.
2. **Memory persistence test** — run 3 sessions, verify session 3 reflects learnings from sessions 1-2.
3. **Compression validation** — Nate B. Jones 5-task parity test: compressed context must match original context output quality.
4. **Identity consistency test** — run 5 different tasks, verify persona voice/worldview holds across all.

### Step 8 — Compound Maintenance Plan
Weekly: review episodic memory, flag distillation candidates. Monthly: run semantic memory decay sweep, prune dead-weight entries. Quarterly: persona refinement based on accumulated learnings. Per-session: memory write triggers fire automatically on task completion and user correction.

## Output Contract

A five-layer agent file set: `logic.md`, `library/`, `memory/` (three-tier sovereign schema with decay parameters and write triggers), a compression map (five-vector application, token budget allocation, persona explicitly excluded), `persona.md` with the three memory-integration extensions, and results from all four Step 7 validation tests. Plus a documented compound maintenance plan (weekly/monthly/quarterly/per-session cadence).

## Output Skeleton

```
# Sovereign-Memory Agent Stack — [Agent Name]

## Purpose & Constraint Map
Mission: ... | Consumers: ... | Persistence: ... | Context Budget: ...

## Logic Layer
[workflow steps / rules / decision gates / quality checkpoints]

## Library Layer
[exemplars / knowledge files / tool configs / templates]

## Sovereign Memory Layer
Episodic Tier: [retention, write triggers]
Semantic Tier: [k-value, decay examples]
Procedural Tier: [permanent entries]

## Compression Blueprint
| Vector | Applied To | Result |
Persona: EXCLUDED — not compressed

## Persona Layer (Memory-Aware)
[reference to persona.md]
Learning posture: ...
Memory philosophy: ...
Growth arcs: ...

## Validation Results
| Test | Result | Notes |
| Vanilla Comparison | | |
| Memory Persistence (3 sessions) | | |
| Compression Parity (5-task) | | |
| Identity Consistency (5 tasks) | | |

## Compound Maintenance Plan
Weekly: ... | Monthly: ... | Quarterly: ... | Per-session: ...
```

## Quality Gate

- [ ] All 4 LLMP layers plus the sovereign memory architecture are documented and installed
- [ ] Compression is applied to Logic/Library/Memory only — persona is verified untouched
- [ ] Memory persistence test shows session 3 output genuinely reflects sessions 1-2 learnings, not just "it ran three times"
- [ ] 5-task parity test passed for compressed vs. original context
- [ ] Identity consistency holds across all 5 test tasks
- [ ] Compound maintenance plan is documented with concrete cadences, not "review periodically"

## Deploy When

- Building a primary agent used 10+ times per month
- Client-facing agents that need to visibly improve over time, not just persist
- Any agent currently degrading from session amnesia despite a strong persona
