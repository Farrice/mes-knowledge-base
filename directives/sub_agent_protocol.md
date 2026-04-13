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

### SkillExecutor Prompt Template

```
## PHASE 1: SKILL ACQUISITION
Read: 1. skills/[name]/SKILL.md  2. genius-patterns.md  3. [specific-prompt].md
Confirm: 3 most important patterns? Output structure? What would expert say is WRONG?

## PHASE 2: EXPERT-DRIVEN EXECUTION
Apply methodology to: [Task]

## PHASE 3: OUTPUT — Embody principles (not templates). Reference patterns by name.

## PHASE 4: RECURSIVE REFLECTION — Would expert be proud? Creative or mechanical?

VERIFICATION: SKILL FILES READ: [list] | PATTERNS APPLIED: [list] | QUALITY CHECK: [pass/fail]
```

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

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |

*Created: 2026-02-17 | Compressed: 2026-04-13*
