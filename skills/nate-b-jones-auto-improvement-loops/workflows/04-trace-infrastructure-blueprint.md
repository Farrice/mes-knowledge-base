---
description: Reasoning-trajectory logging schema, storage, retrieval, and analysis layer for any agent system. Traces before optimization — the foundation that ceilings everything above it.
---

# Trace Infrastructure Blueprint

> Load `genius.md` first. "The quality of your trace infrastructure as a business determines the quality of your auto improvement."

## Pre-Flight Gate

Build traces BEFORE optimization. Score-only logging produces random mutations (GP-6). This workflow is a prerequisite even for the readiness audit's own trace assessment.

## When to Use

- Agent system logs outcomes but not reasoning (common)
- Planning auto-improvement and need to build foundation
- Auditing existing system and trace layer scored <7 in WF 02
- Upgrading from score-only to trajectory-logging

## Skill Acquisition

Load: `genius.md` (GP-6, HK-6, SM-3, Anti-pattern #4), `references/karpathy-loop-quotes.md` (Traces Over Scores section)

## Input Required

- Agent system architecture (what agents exist, what they do)
- Current logging state (what's captured today)
- Storage constraints (budget, retention policy)

## Execution

### Phase 1 — Reasoning Chain Schema

Define what goes in a trace. Start from the minimum (SM-3):

```yaml
trace:
  # Identity
  trace_id: uuid
  experiment_id: uuid  # links to auto-improvement experiment if applicable
  parent_trace_id: uuid  # for sub-agent calls
  timestamp: iso8601
  agent_name: string
  model: string
  
  # Task context
  task:
    task_id: string
    task_type: string
    input: {serialized}
    spec_reference: path  # link to spec/rubric this task was graded against
  
  # Reasoning trajectory (THE critical field — GP-6)
  reasoning_chain:
    - step: integer
      thought: string
      confidence: float  # 0-1, self-reported
      tool_calls:
        - tool: string
          args: {}
          result_summary: string
          result_full_ref: path  # for progressive disclosure
      decision: string
      decision_rationale: string
      alternatives_considered: []
  
  # Output
  final_output: string
  final_output_format_valid: bool
  
  # Self-reported diagnostics
  failure_signals:
    - step: integer
      signal_type: string  # "uncertain", "context_exhaustion", "tool_failed", etc.
      severity: string  # "minor", "major", "blocker"
  
  # External evaluation (attached after scoring)
  evaluation:
    score: float
    rubric_breakdown: {dimension: score}
    held_out_score: float
    human_review: string  # if reviewed
  
  # Resource telemetry
  telemetry:
    tokens_used: int
    tokens_remaining: int
    wall_time_seconds: float
    compute_cost_usd: float
```

**Key fields for meta-agent interpretability**:
- `reasoning_chain[].decision_rationale` → lets meta-agent ask "why did it pick this path?"
- `failure_signals` → meta-agent's primary input for identifying what to fix
- `alternatives_considered` → shows the decision space, not just the chosen path

### Phase 2 — Decision Point Instrumentation

Where does the task-agent emit a trace step? Minimum instrumentation points:

1. **Task reception** — initial interpretation of the task
2. **Plan formulation** — proposed approach
3. **Each tool call** — before and after
4. **Each branching decision** — where the agent chose path A over B
5. **Self-criticism / verification step** — if implemented per Pattern 2
6. **Handoff to sub-agent** — if implemented per Pattern 5/6
7. **Final output generation** — spec-check step
8. **Failure / escalation** — any point the agent flags uncertainty

Instrumentation approach:
- **Preferred**: structured logging at each point (explicit `log_trace_step()` calls)
- **Acceptable**: system-prompt requirement that agent emits trace markers
- **Insufficient**: post-hoc reconstruction from chat history

### Phase 3 — Failure Capture

Specific instrumentation for failure modes (lets meta-agent diagnose "lost direction at step 14"):

| Failure Type | How to Capture | Meta-Agent Use |
|--------------|---------------|----------------|
| Context exhaustion | Token-utilization at decision point | Spot: "agent truncated here" |
| Tool misuse | Tool call + result mismatch | Spot: "wrong tool or wrong args" |
| Specification miss | Spec-check diff at final output | Spot: "missed required field X" |
| Reasoning loop | Repeated thought patterns (hashable) | Spot: "got stuck in loop" |
| Premature commit | Early termination without spec-satisfaction | Spot: "gave up too early" |
| Over-generation | Output length vs. spec length ratio | Spot: "over-verbose" |

### Phase 4 — Storage + Retrieval

Storage architecture:
- **Format**: JSON Lines (one trace per line) or structured DB
- **Location**: version-controlled if small (git), object storage if large (S3/GCS)
- **Partitioning**: by experiment_id, then by date
- **Retention**: minimum 90 days for recent trace analysis, permanent archive for KEPT-variant traces

Retrieval requirements:
- Index by `experiment_id`, `variant_hash`, `task_id`, `score` (for quality-band filtering)
- Query patterns the meta-agent needs:
  - "Last N traces from this variant"
  - "All failure signals matching type X across recent traces"
  - "Score distribution for variant Y"
  - "Traces where agent lost direction at step <N>"

### Phase 5 — Analysis Layer

How the meta-agent actually consumes traces. Options:

**Option A — Direct File Access (simple)**
- Meta-agent reads trace JSONL files directly
- Uses structured-output prompts to parse and reason
- Good for small scale (<1000 traces)

**Option B — Trace Summarizer (medium)**
- Preprocessing step summarizes trace clusters
- Meta-agent sees summary + drills into specific traces on demand
- Good for medium scale (1000-10K traces)

**Option C — Trace Database + Query DSL (complex)**
- Traces indexed in specialized DB (SQLite for local, Postgres for team)
- Meta-agent uses query tools: "find traces where format_valid=false AND score<6"
- Good for large scale (>10K traces)

Select based on team size + trace volume. Start simple.

### Phase 6 — Implementation Checklist

```markdown
## Trace Infrastructure Build Checklist

### Schema
- [ ] Full schema defined (with all required fields)
- [ ] Optional fields documented
- [ ] Schema versioned (for future migration)

### Instrumentation
- [ ] All 8 instrumentation points covered
- [ ] Failure capture for all 6 failure types
- [ ] Trace emission in system prompt OR explicit logging calls

### Storage
- [ ] Storage location chosen (git / S3 / DB)
- [ ] Partitioning scheme documented
- [ ] Retention policy set

### Retrieval
- [ ] Index on core fields (experiment_id, variant_hash, task_id, score)
- [ ] All 4 meta-agent query patterns supported

### Analysis Layer
- [ ] Option A/B/C selected based on scale
- [ ] Tooling built and tested
- [ ] Meta-agent has example queries

### Validation
- [ ] 10+ traces collected from test runs
- [ ] Meta-agent can answer "what caused failure in trace X" from traces alone
- [ ] "Lost direction at step N" query returns correct results
```

## Content Type Adaptations

| System | Reasoning Chain Focus | Failure Capture Focus |
|--------|----------------------|----------------------|
| Code-gen agent | Implementation decisions, test choices | Compilation errors, test failures, spec misses |
| Content workflow | Draft logic, revision rationale | Voice drift, spec misses, format errors |
| Research agent | Query formulation, source synthesis | Hallucination markers, source attribution gaps |
| Customer service | Intent interpretation, response selection | Escalation signals, policy violations |
| Pricing engine | Rule application, threshold decisions | Policy boundary violations |

## Output Requirements

- Trace schema (YAML, copy-ready)
- Instrumentation point list (8 minimum)
- Storage architecture decision
- Retrieval query pattern list
- Implementation checklist
- Document: `deliverables/trace-infrastructure-[system].md`

## Quality Gate

- **Trace Infrastructure Depth** (0-10): full schema, not minimal?
- **Prerequisite Completeness** (0-10): all 8 instrumentation + 6 failure types covered?
- **Judgment Leverage** (0-10): can a meta-agent actually USE these traces to propose targeted edits?

Minimum: 7 on each.

## Anti-Patterns

- ❌ Logging only `{input, output, score}` — no reasoning chain
- ❌ Ad-hoc string logging instead of structured schema
- ❌ No retention policy ("we'll figure it out later")
- ❌ Building optimization before traces exist
- ❌ Skipping failure capture ("we'll just look at low scores")

## Hand-off

- Infrastructure built → proceed to `/nate-auto-emergent` (WF 05) for affordance pre-load
- Infrastructure incomplete → remediate gaps before architecture deployment
