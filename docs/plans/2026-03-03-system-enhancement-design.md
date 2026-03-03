# System Enhancement Design — Foundation Up

**Date**: 2026-03-03
**Status**: In Progress
**Goal**: Enhance the Antigravity system across 4 dimensions without breaking existing functionality

---

## Context

- **95 agents** + framework, **154 skills** (completion engine v2.0), **38 workflows**, **17 execution scripts**, **32 directives**
- Agent Teams already enabled (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
- 27 plugins installed (official + superpowers marketplace)
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

### Key Changes

1. **Debug current Agent Teams behavior** — identify why sequential fallback happens
2. **Create parallel workflow templates** — extraction swarm, research team, content sprint
3. **Test with real tasks** — run a 3-agent research task and validate true parallelism
4. **Update sub_agent_protocol.md** — codify when to parallelize vs. keep sequential

---

## Phase 4: Plugin Audit + Expansion

**Objective**: Identify and install high-value plugins; optionally package system as a plugin.

### Key Changes

1. **Marketplace audit** — scan for content, social, scheduling, research plugins
2. **Gap analysis** — map missing capabilities against business needs
3. **Install + test** — add 3-5 high-value plugins
4. **Custom plugin scoping** — evaluate packaging 95 agents + 154 skills as portable plugin

---

## Success Criteria

- [ ] Audit script reports ≥90% pass rate on structural checks
- [ ] 5-8 sampled agents/skills confirmed expert-quality
- [ ] Intent pipeline routes 18/20 test requests correctly (Phase 2)
- [ ] 3-agent parallel task completes with true concurrency (Phase 3)
- [ ] 3+ new plugins installed and integrated (Phase 4)

---

## Constraints

- **No breaking changes** — existing agents, skills, directives stay functional throughout
- **Additive only** — enhancements build on top, never replace without explicit approval
- **Session boundaries** — each phase can span 1-3 sessions; commit progress at end of each
