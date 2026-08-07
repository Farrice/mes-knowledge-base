# Sub-Agent Protocol

> **Purpose**: When and how to spawn sub-agents for context isolation.
> **Loading Protocol**: `directives/agent-loading-protocol.md` (Tier 3 = sub-agent)

---

## Why Sub-Agents Exist

Sub-agents solve **context pollution**. Fresh context window = honest code review, clean research, accurate documentation.

---

## Auto-Spawn Triggers

| Trigger | Archetype | When |
|---------|-----------|------|
| Major code change (50+ lines) | CodeReviewer | After change, before marking done |
| Directive created/updated | DocSyncer | After change, verify matches code |
| Deep research mid-task | Researcher | When main task needs data without context pollution |
| Multi-file refactor | CodeReviewer | After refactor, fresh-eyes review |
| Pre-deployment | CodeReviewer | Before `modal deploy` or production push |
| Expert skill execution (2+ experts or 10+ files) | SkillExecutor | Tier 3 loading |
| Multi-expert ensemble | SkillExecutor | `/roundtable`, `/swarm`, multi-expert workflows |

Don't spawn for trivial changes (<20 lines).

---

## Archetypes

| Archetype | Permissions | Mission | Output |
|-----------|------------|---------|--------|
| **CodeReviewer** | READ-ONLY on targets | Find bugs, security, perf, logic errors | Markdown with 🔴🟡🟢 severity |
| **DocSyncer** | READ `execution/`, WRITE `directives/` | Ensure docs match code | Diff with rationale |
| **Researcher** | READ context summary + web | External data without file modification | Structured findings with 🟢🟡🔴 confidence |
| **SkillExecutor** | READ skills, WRITE `.tmp/` only | Load expert in fresh context, apply methodology | Deliverable + provenance (~300-500 tokens) |

**SkillExecutor — when to use**: 2+ experts needed, 10+ files loaded, running ensemble workflows, full extraction pipeline.
**When NOT to spawn**: <~1,000 token output, follow-up refinements, rapid-fire mode, conversational Q&A.

### Sub-Agent Prompt Envelope (Anthropic 4-field — Wave 5 / 2026-05-21, scope universalized 2026-05-22)

**Every sub-agent spawn MUST use the Anthropic 4-field envelope, regardless of archetype** (SkillExecutor, CodeReviewer, DocSyncer, Researcher). The fields are EXPECTED — vague delegation ("research the semiconductor shortage") causes 30%+ duplicate work and gaps per Anthropic's multi-agent research-system retro (anthropic.com/engineering/built-multi-agent-research-system). Each spawn must declare all four explicitly:

**Field-name aliasing** (both forms recognized — substance is identical):

| Box-separator (used below) | YAML-style alias | What it carries |
|---|---|---|
| `═══ OBJECTIVE ═══` | `objective:` | One sentence — single specific deliverable |
| `═══ OUTPUT FORMAT ═══` | `output_format:` | Filepath + ≤500 token summary, per the lightweight-references pattern |
| `═══ TOOLS ALLOWED ═══` | `tool_allowlist:` | Explicit list — no implicit "all tools"; always include "no nesting" denial |
| `═══ BOUNDARIES ═══` | `boundaries:` | SCOPE + ANTI-SCOPE + HALT — what NOT to do, scope walls, no further spawns |

```
═══ OBJECTIVE ═══
[single specific deliverable — one sentence. NOT "research X" but "produce a 5-bullet
summary of the top 3 Anthropic-published failure modes from the multi-agent research
post, with one-sentence each".]

═══ OUTPUT FORMAT ═══
- Write deliverable to: .tmp/[workflow]/[agent-or-slug].md
- Return to orchestrator: ≤500 token summary + filepath (NOT full deliverable)
- Summary schema:
    STATUS: completed | partial | blocked
    WHAT_RAN: [one-line description]
    KEY_FINDINGS: [3-5 bullets, ≤20 words each]
    FILE: [path]
    CONFIDENCE: VERIFIED | LIKELY | UNCONFIRMED
    BLOCKERS: [if STATUS != completed]

═══ TOOLS ALLOWED ═══
ALLOW: [explicit subset — e.g., "Read, Grep, mcp__recall__search, WebFetch"]
DENY:  [explicit denials — always include: "do NOT spawn further sub-agents (no nesting)"]

═══ BOUNDARIES ═══
SCOPE:      [exactly what's in-scope, 1-2 lines]
ANTI-SCOPE: [what's explicitly OUT — prevents drift]
HALT:       [when to stop and return]

═══ ANCHORS (read-only) ═══
[1-3 anchor file paths or context snippets injected from anchor_memory.py describe;
keep <2KB combined]

═══ SKILL ACQUISITION (the prior PHASE 1 of this template) ═══
Read: skills/[name]/SKILL.md → genius.md → [specific-prompt].md (only if Tier 2+)
Confirm internally: 3 most important patterns? Output structure? What would the expert say is WRONG?
```

**Wave 5 Read-Only Constraint**: When spawning from a `/autopilot` outcome class, fan-out is restricted to read-heavy phases (research, review, diagnosis-only refinement, verification, extraction). Write-heavy parallel fan-out (atomization, multi-deliverable) defaults sequential per Cognition's "Don't Build Multi-Agents" thesis. See `.agent/workflows/autopilot.md` Phase 2 fan-out posture matrix.

**Tiered budget** (Anthropic field-standard, mirrors autopilot.md):
- Simple fact-finding / single-format → 1 agent / 3-10 tool calls
- Direct comparison / 2-domain synthesis → 2-4 agents / 10-15 tool calls each
- Complex research / 9-lens refinement → 5-10 agents / 10-15 tool calls each
- HARD CAP: 12 parallel workers per phase. Batch into waves above that.

### Return Format

```markdown
## SkillExecutor Result: [Expert]
**Task**: [1-line] | **Patterns Applied**: [list] | **Quality Check**: [pass/fail]
### Output
[Deliverable, compressed to essentials]
### Key Insight
[1-2 sentences of framework's most important revelation]
```

---

## Parallel Execution

### Decision Tree

Independent tasks, no coordination needed? → **Parallel Task Calls** (2-5 agents)
Independent tasks, agents need each other's output? → **Agent Teams** (2-5, coordinated)
6+ agents, cost-sensitive? → **parallel_swarm.py** (Gemini API, ~$0.15/5 agents, no tool access)

### Parallel Rules

1. Verify independence before parallelizing
2. Max 5 parallel Task calls
3. Always synthesize parallel outputs
4. One agent fails → others continue
5. Each agent writes to own file (`.tmp/[workflow]/[agent].md`)

### Common Patterns

| Workflow | Execution | Why |
|----------|-----------|-----|
| `/extract` (single) | Sequential | One source, no parallel benefit |
| `/parallel-extract` | Parallel Tasks | Independent sources |
| `/roundtable` | Sequential | Experts build on each other |
| `/parallel-research` | Parallel Tasks | Independent angles |
| `/swarm` (5+) | Gemini parallel | Too many for Task parallelism |
| Complex builds | Agent Teams | Dependency graph |

---

## Adaptive Re-Routing on Failure

PARL-inspired pattern (Moonshot Kimi K2.6): when a sub-agent fails, do not return the failure silently. Re-route to an ensemble fallback before escalating.

**When it fires** (in `execution/parallel_swarm.py::execute_agent_with_fallback`):
| Trigger | Detection |
|---|---|
| Exception during generation | `status = "failed"` |
| Empty output | `output` is empty or whitespace |
| Thin output | `len(output.strip()) < MIN_VIABLE_OUTPUT` (default 400 chars) — likely truncation, refusal, or token collapse |

**Re-routing logic**:
1. Look up primary expert in `ENSEMBLE_FALLBACKS` (mirrors `directives/expert_auto_routing.md` ensemble table)
2. If no fallback defined → mark result `needs_refine`, return
3. Retry once with first fallback expert
4. If fallback succeeds → status becomes `rerouted`, `original_agent` records primary, `failure_trace` records what failed
5. If fallback also fails → mark `needs_refine`, return with full trace

**After needs_refine**: orchestrator should escalate to `/jcc-refine` (human-in-loop). Never auto-retry a second fallback — that path is Phase D autonomous, which was explicitly rejected (see `feedback_phase2-activation-gap.md`).

**Status values** (expanded):
- `success` — primary expert produced usable output
- `rerouted` — fallback expert succeeded after primary failed
- `needs_refine` — both primary and fallback failed; human intervention required
- `failed` — legacy; only used when fallback isn't attempted (e.g., token budget exhausted pre-retry)
- `skipped` — work order skipped (e.g., budget exceeded before execution)

**Synthesis inclusion**: `_is_usable(result)` returns True for both `success` and `rerouted`. Synthesis consumes both; `needs_refine` is excluded and surfaced to user.

**Logging**: `original_agent` and `failure_trace` are persisted in `metadata.json` of every swarm run. Use these to track ensemble quality over time and feed the evolution engine.

---

## Anti-Patterns

- ❌ Share full conversation with sub-agent (defeats purpose)
- ❌ Spawn for <20 lines (overhead > benefit)
- ❌ Chain 3+ sub-agents deep (coordination cost explodes)
- ❌ Give sub-agents write access to code (main agent only)
- ❌ Spawn without clear return condition
- ❌ Sequential Task calls when independent (force parallel)
- ❌ Agent Teams for purely independent tasks (unnecessary coordination)
- ❌ 6+ parallel Task calls (resource contention)

---

## How to Spawn (Explicit Syntax)

When a workflow phase qualifies for sub-agent spawn (2+ experts, 10+ files in context, complex multi-domain task), invoke the `Agent` tool directly. **Every spawn's `prompt` parameter MUST contain the 4-field envelope above** — the examples below show abbreviated illustrative forms, but production spawns expand all four fields.

**Parallel multi-expert ensemble** (SkillExecutor — writers-room Layer 1+2+3):
```
Agent(
    description="Compress layer review",
    subagent_type="general-purpose",
    prompt="""
═══ OBJECTIVE ═══
Apply Layer 1 (structure & compression) lenses from Albom + Franzen + Cole to the draft below and produce the top 3 compression cuts with citation back to which expert lens identified each.

═══ OUTPUT FORMAT ═══
- Write deliverable to: .tmp/writers-room/layer1-compression-review.md
- Return to orchestrator: STATUS + 3-bullet KEY_FINDINGS + FILE + CONFIDENCE

═══ TOOLS ALLOWED ═══
ALLOW: Read (skills/*), Write (.tmp/writers-room/**)
DENY:  no further sub-agent spawns (no nesting); no edits outside .tmp/

═══ BOUNDARIES ═══
SCOPE:      Structure + compression lens only; ignore voice/tone (Layer 2's job)
ANTI-SCOPE: Do NOT rewrite the draft; identify cuts only
HALT:       After 3 cuts identified with citations

═══ DRAFT ═══
[DRAFT]
"""
)
```

**Researcher with context isolation** (deep-research / verification):
```
Agent(
    description="Source verification",
    subagent_type="deep-research",
    prompt="""
═══ OBJECTIVE ═══
Verify the claims below against primary sources and label each VERIFIED / LIKELY / UNCONFIRMED.

═══ OUTPUT FORMAT ═══
- Write to: .tmp/verification/claim-audit.md (one row per claim: claim, label, source URL, confidence)
- Return: STATUS + count by label + FILE + ≤200 word summary

═══ TOOLS ALLOWED ═══
ALLOW: WebFetch, WebSearch, mcp__recall__search, mcp__perplexity-ask__perplexity_ask
DENY:  no further sub-agent spawns; no inference-only labels (must have source)

═══ BOUNDARIES ═══
SCOPE:      Each claim labeled with one citation
ANTI-SCOPE: Don't rewrite the draft; verification only
HALT:       After all claims labeled OR 400 word cap hit

═══ CLAIMS ═══
[CLAIMS]
"""
)
```

**CodeReviewer on a non-trivial change** (envelope applies to non-SkillExecutor archetypes too):
```
Agent(
    description="Migration safety review",
    subagent_type="feature-dev:code-reviewer",
    prompt="""
═══ OBJECTIVE ═══
Review [FILE] for safety issues with [CHANGE_RATIONALE] in mind. Report under 🔴🟡🟢 severity.

═══ OUTPUT FORMAT ═══
- Write to: .tmp/code-review/[file-slug]-review.md
- Return: STATUS + count by severity + FILE + top issue summary (≤200 words)

═══ TOOLS ALLOWED ═══
ALLOW: Read (only the targets listed), Grep, Glob
DENY:  no Edit / Write / Bash — review only; no further sub-agent spawns

═══ BOUNDARIES ═══
SCOPE:      Safety, security, perf, logic errors in the listed files
ANTI-SCOPE: Style nitpicks unless they create real risk
HALT:       After all targets reviewed

═══ TARGETS ═══
[FILE]
"""
)
```

**Anti-pattern**: Spawning a sub-agent with "share full conversation history" — defeats context isolation. Brief the sub-agent fresh.
**Anti-pattern**: Omitting any of the 4 envelope fields — vague delegation re-introduces the 30% duplicate-work failure mode Anthropic documented.

---

## Deterministic Backstop (Shipped 2026-05-12)

Per `feedback_ai-memory-dependent-observability.md`, this protocol cannot rely on AI memory to fire. `execution/chain_runner.py finalize()` now auto-logs **misses** — when a qualifying workflow ran without sub-agent spawn — to `evolution_store/sub_agent_misses.jsonl`.

**Qualifying workflows** (logged miss if `--sub-agents 0` or omitted):
parallax, extract-forge, writers-room, campaign, jcc-deploy, swarm, parallel-swarm, swarm-research, research-swarm, big-project, content-bundle, proof-pipeline, build-bos, roundtable, council, parallel-extract, parallel-content, jcc-strike, jcc-campaign, jcc-solo, jcc-refine, jcc-upgrade, jcc-aar, brief, generate-brief, mini-brief, deep-research.

**Reporting actual spawns** via the CLI flag:
```bash
python3 execution/chain_runner.py finalize "..." --workflow parallax --sub-agents 3 [...]
```

**After 30 days of misses data** (target: 2026-06-12), audit `evolution_store/sub_agent_misses.jsonl`:
- If consistent misses on the same workflows → strengthen those workflows with explicit Agent-tool spawn instructions (the conservative Phase D Move 2 escalation deferred from 2026-05-12 brief)
- If miss rate drops naturally (AI starts spawning correctly without escalation) → leave gate as soft warning, do not escalate to blocking
- If misses concentrate on workflows that don't actually benefit from sub-agents → remove those from `_SUB_AGENT_QUALIFYING_WORKFLOWS` set in `execution/chain_runner.py`

Source: `_active/_archive/2026-08-07-sweep/system-integration/2026-05-12-agentic-os-elevation-brief.md` Move 2 Phase D.

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-05-12 (deterministic backstop shipped — `chain_runner.py` auto-logs misses) |
| **Activation Count** | 0 explicit + automatic miss-logging for all qualifying chain finalize calls |
| **30-Day Review Date** | 2026-06-12 — audit `evolution_store/sub_agent_misses.jsonl` |

*Created: 2026-02-17 | Compressed: 2026-04-13 | Backstop shipped: 2026-05-12*
