# Workflow Chain Contracts

> **Purpose**: Define output-to-input contracts for common multi-step workflow sequences.
> Each chain specifies what the upstream workflow must produce and what the downstream workflow expects.

---

## Chain 1: Extract → Convert → Deploy

**Sequence**: `/extract` → `/convert-extraction` → agent auto-registration

| Step | Workflow | Produces | Expected By Next Step |
|------|----------|----------|-----------------------|
| 1 | `/extract` | `extractions/[expert]-extraction.md` with patterns, hidden knowledge, crown jewels | `/convert-extraction` expects extraction file path |
| 2 | `/convert-extraction` | Complete skill folder: `SKILL.md`, `genius-patterns.md`, `hidden-knowledge.md`, prompts | Agent creation expects skill folder path |
| 3 | Agent registration | `agents/[slug]/AGENT.md`, `memory/context.md`, `AGENT_INDEX.md` updated, `SKILL_INDEX.md` updated | System is ready to use the new expert |

**Quality Gate**: Run at step 2→3 boundary. Check that all prompt files exist and SKILL.md references them.

---

## Chain 2: Research → Deploy Skill

**Sequence**: `/research-topic` → `/deploy-skill`

| Step | Workflow | Produces | Expected By Next Step |
|------|----------|----------|-----------------------|
| 1 | `/research-topic` | Research artifact with findings, citations, and actionable insights | `/deploy-skill` expects research context as input |
| 2 | `/deploy-skill` | Expert-driven output grounded in research data | Delivery to user |

**Quality Gate**: Run at step 1→2 boundary. Verify research has `🟢 GROUNDED` provenance tag before feeding to skill.

---

## Chain 3: Brief → Skill → Package

**Sequence**: `/brief` → `/deploy-skill` → `/package-deliverable`

| Step | Workflow | Produces | Expected By Next Step |
|------|----------|----------|-----------------------|
| 1 | `/brief` | Strategic recommendations with matched experts | `/deploy-skill` expects expert names and task |
| 2 | `/deploy-skill` | Raw expert output (strategy, copy, analysis) | `/package-deliverable` expects raw content |
| 3 | `/package-deliverable` | Polished visual deliverable | Delivery to user/client |

**Quality Gate**: Run at each boundary. Step 2 output must pass the 3-point quality gate before packaging.

---

## Chain 4: Roundtable → Action

**Sequence**: `/roundtable` → action items → relevant `/deploy-skill`

| Step | Workflow | Produces | Expected By Next Step |
|------|----------|----------|-----------------------|
| 1 | `/roundtable` | Roundtable artifact with expert positions, consensus, dissents | User selects action items |
| 2 | `/deploy-skill` | Execution of selected recommendations | Delivery to user |

**Quality Gate**: User approval required between steps 1 and 2.

---

## General Rules

1. **Never skip a chain step** — each step depends on the prior step's output
2. **Run quality gate at every boundary** — see `directives/quality_gate.md`
3. **Log chain execution** — note which steps completed in the task artifact
4. **If a step fails** — retry once, then halt the chain and notify user
5. **Use handoff summaries at every boundary** — see below and `directives/token-efficiency-protocol.md`

---

## Handoff Summary Protocol

> **Adapted from Anthropic's PTC philosophy**: Only pass the model what it needs to reason about. Keep intermediate results out of context.

At each chain boundary, the completing step produces a compressed handoff instead of leaving raw output in context:

```markdown
## Chain Handoff: [Completing Step] → [Next Step]

**Expert**: [Name]
**Domain**: [1-line]
**Key Outputs**: [count] patterns, [count] prompts, [count] files
**Core Methodology**: [1-2 sentences — the essential framework]
**Files Created**: [list of paths]
**Next Step Needs**: [what specifically to read — not everything]
```

### Why This Matters

Without handoff summaries, a 3-step chain like `/extract → /convert → /create-agent` accumulates:
- Full transcript (~10K tokens)
- Full extraction report (~5K tokens)  
- Full SKILL.md + genius-patterns (~3K tokens)
- All prompt files (~2K+ tokens each)

With handoff summaries, each step sees only ~200-300 tokens of context from the prior step, plus targeted file reads. **Estimated savings: 40-60% fewer tokens per chain execution.**

---

*Created: 2026-02-17 | Updated: 2026-02-18 (added handoff summary protocol)*
*Component 3 of System Elevation*
