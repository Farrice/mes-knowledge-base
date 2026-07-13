---
name: "Nate B Jones — Trace Infrastructure Blueprint"
source_prompt: born-v2
skill: nate-b-jones-auto-improvement-loops
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building the layer Nate B Jones identifies as the ceiling on everything above it: "The quality of your trace infrastructure as a business determines the quality of your auto improvement." This workflow exists because most agent systems log outcomes, not reasoning — and score-only logging produces random mutations instead of targeted edits, per Nate's account of what happened when Goose's team stripped reasoning trajectories from the meta-agent's input: the improvement rate dropped fast. Traces must be built BEFORE optimization infrastructure, not after. Your job here is not to design a logging system in the abstract — it's to specify the exact schema, instrumentation points, failure-capture taxonomy, storage, retrieval, and analysis layer a meta-agent will actually consume.

## Input Required

- **[AGENT SYSTEM ARCHITECTURE]** — what agents exist in this system, what each does
- **[CURRENT LOGGING STATE]** — what's captured today (outcomes only? partial reasoning? nothing?)
- **[STORAGE CONSTRAINTS]** — budget, retention policy requirements

## Execution Protocol

### Phase 1 — Reasoning Chain Schema
Define the trace schema starting from the minimum viable fields. The critical field is `reasoning_chain` — everything else is scaffolding around it. Structure: identity block (trace_id, experiment_id linking to the auto-improvement experiment if applicable, parent_trace_id for sub-agent calls, timestamp, agent_name, model); task context (task_id, task_type, serialized input, spec_reference path); the reasoning trajectory itself as a step array — for each step: thought, self-reported confidence (0-1), tool_calls (tool, args, result_summary, result_full_ref for progressive disclosure), decision, decision_rationale, alternatives_considered; final_output plus final_output_format_valid; failure_signals (step, signal_type such as "uncertain"/"context_exhaustion"/"tool_failed", severity — minor/major/blocker); evaluation block attached post-scoring (score, rubric_breakdown, held_out_score, human_review); telemetry (tokens_used, tokens_remaining, wall_time_seconds, compute_cost_usd). The three fields that matter most for meta-agent interpretability: `decision_rationale` (lets the meta-agent ask "why did it pick this path?"), `failure_signals` (the meta-agent's primary input for identifying what to fix), and `alternatives_considered` (shows the decision space, not just the chosen path).

### Phase 2 — Decision Point Instrumentation
Specify the minimum 8 instrumentation points where the task-agent must emit a trace step: (1) task reception — initial interpretation; (2) plan formulation — proposed approach; (3) each tool call, before and after; (4) each branching decision — where the agent chose path A over B; (5) self-criticism/verification step, if implemented; (6) handoff to a sub-agent, if implemented; (7) final output generation — spec-check step; (8) failure/escalation — any point the agent flags uncertainty. Rank the instrumentation approach: preferred is structured logging with explicit `log_trace_step()` calls; acceptable is a system-prompt requirement that the agent emits trace markers; insufficient is post-hoc reconstruction from chat history — name this explicitly if that's what's currently happening.

### Phase 3 — Failure Capture
Specify instrumentation for each of 6 failure types the meta-agent needs to diagnose "lost direction at step 14"-style questions: context exhaustion (capture: token-utilization at decision point; use: spot "agent truncated here"); tool misuse (capture: tool call + result mismatch; use: spot "wrong tool or wrong args"); specification miss (capture: spec-check diff at final output; use: spot "missed required field X"); reasoning loop (capture: repeated thought patterns, hashable; use: spot "got stuck in loop"); premature commit (capture: early termination without spec-satisfaction; use: spot "gave up too early"); over-generation (capture: output length vs. spec length ratio; use: spot "over-verbose").

### Phase 4 — Storage + Retrieval
Specify storage architecture: format (JSON Lines or structured DB), location (version-controlled/git if small, object storage if large), partitioning (by experiment_id then date), retention (minimum 90 days for recent analysis, permanent archive for KEPT-variant traces). Specify retrieval: index on experiment_id, variant_hash, task_id, score; and confirm the system supports the four query patterns a meta-agent actually needs — "last N traces from this variant," "all failure signals matching type X across recent traces," "score distribution for variant Y," "traces where agent lost direction at step <N>."

### Phase 5 — Analysis Layer
Select the consumption model by scale: Option A — Direct File Access (meta-agent reads JSONL directly, uses structured-output prompts to parse; good under 1,000 traces); Option B — Trace Summarizer (preprocessing summarizes clusters, meta-agent drills into specifics on demand; good for 1,000-10,000 traces); Option C — Trace Database + Query DSL (indexed in SQLite/Postgres, meta-agent uses query tools like "find traces where format_valid=false AND score<6"; good above 10,000 traces). Select based on team size and trace volume, and default to starting simple.

### Phase 6 — Implementation Checklist
Produce the build checklist covering: Schema (full schema defined, optional fields documented, schema versioned for migration), Instrumentation (all 8 points covered, all 6 failure types captured, emission mechanism specified), Storage (location chosen, partitioning documented, retention set), Retrieval (indexed on core fields, all 4 query patterns supported), Analysis Layer (option selected + tooling built + example queries given to the meta-agent), Validation (10+ traces collected from test runs, meta-agent can answer "what caused failure in trace X" from traces alone, "lost direction at step N" query returns correct results).

## Output Contract

- Copy-ready trace schema in YAML
- Instrumentation point list (all 8, each marked covered/missing)
- Failure capture specification (all 6 types, capture method + meta-agent use)
- Storage architecture decision with rationale
- Retrieval query pattern list (all 4, each marked supported/unsupported)
- Implementation checklist (all 6 sub-sections)
- Document target: `deliverables/trace-infrastructure-[system].md`

## Output Skeleton

```markdown
# Trace Infrastructure Blueprint — [System Name]

## Reasoning Chain Schema
```yaml
[full trace schema, all fields from Phase 1]
```

## Instrumentation Points (8)
| # | Point | Approach | Status |
|---|-------|----------|--------|
| 1 | Task reception | [structured/prompt-marker/insufficient] | [covered/missing] |
[... all 8]

## Failure Capture (6 types)
| Failure Type | Capture Method | Meta-Agent Use |
|--------------|-----------------|-----------------|
[... all 6]

## Storage Architecture
Format: [...]
Location: [...]
Partitioning: [...]
Retention: [...]

## Retrieval
Indexed fields: [...]
Query patterns supported: [4, each marked]

## Analysis Layer
Option selected: [A/B/C]
Rationale: [scale justification]

## Implementation Checklist
[full checklist, all boxes]
```

## Quality Gate

- Does the schema include the full `reasoning_chain` array (thought, tool_calls, decision_rationale, alternatives_considered per step), not just input/output/score?
- Are all 8 instrumentation points addressed, with the instrumentation approach for each ranked (structured logging preferred, post-hoc reconstruction flagged as insufficient if that's the current state)?
- Are all 6 failure types given a specific capture mechanism, not a generic "we'll look at low scores" fallback?
- Is the analysis-layer option chosen justified by actual or projected trace volume, not defaulted without reasoning?
- Does the validation section include a concrete test — "meta-agent can answer what caused failure in trace X from traces alone" — not just a schema-complete checkbox?

## Deploy When

- The agent system logs outcomes but not reasoning (the common starting state)
- Planning auto-improvement and the foundation hasn't been built yet
- An existing system's trace layer scored below 7 in the readiness audit
- Upgrading a system from score-only logging to reasoning-trajectory logging
