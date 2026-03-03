# System Enhancement Design — Foundation Up

**Date**: 2026-03-03
**Status**: Complete (all 4 phases)
**Goal**: Enhance the Antigravity system across 4 dimensions without breaking existing functionality

---

## Context

- **95 agents** + framework, **154 skills** (completion engine v2.0), **38 workflows**, **17 execution scripts**, **32 directives**
- Agent Teams already enabled (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- 33 plugins installed (official + superpowers + gmickel + cc-marketplace)
- Known pain point: parallel execution not working as expected (Feb 6 session)
- Known pain point: routing doesn't always pick the right expert
- Known pain point: "output vs. expertise" mode not distinguished

## Approach: Foundation Up

Fix what exists → Make it findable → Scale it → Expand it

---

## Phase 1: Reliability Pass

**Objective**: Ensure every agent, skill, workflow, and script is structurally sound and functional.

### Automated Audit (`execution/system_audit.py`)

| Check | Pass Criteria |
|-------|--------------|
| Agent structure | AGENT.md exists, non-empty, has meaningful content |
| Skill structure | SKILL.md (with frontmatter) + genius.md + ≥1 workflow |
| Workflow completeness | Non-empty, has deliverable description |
| Cross-references | Invocation cards → actual agents; indexes → actual dirs |
| Index sync | AGENT_INDEX.md and SKILL_INDEX.md match filesystem |
| Execution scripts | Valid Python syntax, imports resolve |

### Quality Sampling

5-8 representative agents/skills across domains:
- Content creation (e.g., nicolas-cole, harry-dry)
- Business strategy (e.g., april-dunford, daniel-priestley)
- Technical (e.g., nick-saraev, nate-b-jones)
- Creative (e.g., sam-goddard, jonathan-franzen)

### Fix Protocol

- Structural issues: fix immediately
- Quality issues: flag and create targeted improvement list
- Index drift: re-sync with `execution/sync_registries.py`

---

## Phase 2: Smart Routing

**Objective**: Make the intent pipeline reliably route requests to the right expert(s).

### Key Changes

1. **Invocation card audit** — ensure all 95 agents have cards with specific trigger keywords
2. **Domain registry update** — verify swim lanes match current agent capabilities
3. **Flexible deliverable mode** — add "output" vs. "expertise" routing to intent pipeline
4. **Routing test suite** — 20 sample requests that should route correctly, run as validation

---

## Phase 3: Parallel Execution

**Objective**: Make Agent Teams work reliably for multi-agent workflows.
**Status**: Complete

### Key Changes

1. **Diagnosed sequential fallback** — root cause: `/swarm` and `/roundtable` embody experts one at a time in single context; Task tool calls made one-per-message force sequential execution
2. **Created 3 parallel workflow templates**:
   - `/parallel-extract` — 2-5 extractions simultaneously
   - `/parallel-research` — 3 research angles simultaneously
   - `/parallel-content` — 3-5 content pieces simultaneously
3. **Validated with real 3-agent research task** — all 3 agents ran truly concurrently (fastest: 24s, slowest: 40s; sequential would be ~100s)
4. **Updated `sub_agent_protocol.md`** — added 3-tier parallelism model (Parallel Task Calls → Agent Teams → Gemini Parallel Swarm), decision tree, rules, and anti-patterns

### 3-Tier Parallelism Model

| Tier | Method | Agents | Coordination | Best For |
|------|--------|--------|-------------|----------|
| 1 | Parallel Task Calls | 2-5 | None | Independent extraction, research, content |
| 2 | Agent Teams (TeamCreate) | 2-5 | Message-based | Dependent tasks, lead-worker patterns |
| 3 | Gemini parallel_swarm.py | 5-10+ | None | Large-scale, cost-sensitive |

---

## Phase 4: Plugin Audit + Expansion

**Objective**: Identify and install high-value plugins; optionally package system as a plugin.
**Status**: Complete

### Key Changes

1. **Marketplace audit** — found all official + superpowers plugins already installed (27/27). Added 2 new marketplaces: `gmickel-claude-marketplace`, `cc-marketplace` (ananddtyagi)
2. **Gap analysis** — identified missing capabilities: social publishing, trend research, growth strategy, automation workflows, analytics
3. **Installed 6 new plugins** (27 → 33 total):
   - `content-creator@cc-marketplace` — content creation slash command
   - `trend-researcher@cc-marketplace` — market opportunity identification
   - `growth-hacker@cc-marketplace` — growth strategy agent
   - `n8n-workflow-builder@cc-marketplace` — automation workflow design
   - `analytics-reporter@cc-marketplace` — data analysis and insights
   - `flow-next@gmickel-claude-marketplace` — planning + execution with Ralph autonomous mode
4. **Custom plugin scoping** — assessed packaging 95 agents + 110 skills as a plugin. Verdict: too large for monolith (556K tokens). Recommended: plugin ecosystem with 5 modular plugins in a custom marketplace. Defer until system stabilizes. Full assessment: `.tmp/custom-plugin-scoping.md`

---

## Success Criteria

- [x] Audit script reports ≥90% pass rate on structural checks (Phase 1 — 95%+)
- [x] 5-8 sampled agents/skills confirmed expert-quality (Phase 1 — 8 sampled)
- [x] Intent pipeline routes 18/20 test requests correctly (Phase 2 — 20/20)
- [x] 3-agent parallel task completes with true concurrency (Phase 3 — confirmed, 24-40s parallel vs ~100s sequential)
- [x] 3+ new plugins installed and integrated (Phase 4 — 6 new plugins from 2 new marketplaces)

---

## Constraints

- **No breaking changes** — existing agents, skills, directives stay functional throughout
- **Additive only** — enhancements build on top, never replace without explicit approval
- **Session boundaries** — each phase can span 1-3 sessions; commit progress at end of each
