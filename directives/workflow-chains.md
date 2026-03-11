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

## Chain 5: Ideas → Brief → Flywheel

**Sequence**: `/flywheel-ideas` → `/mini-brief` → `/ip-flywheel` or `/yt-flywheel`

| Step | Workflow | Produces | Expected By Next Step |
|------|----------|----------|-----------------------|
| 1 | `/flywheel-ideas` | 3-5 concept dossier (pain/belief/truth/stakes/engine) | `/mini-brief` expects raw concept or dossier entry |
| 2 | `/mini-brief` | 7-element brief + platform spec + research + expert stack | `/ip-flywheel` expects brief file path |
| 3 | `/ip-flywheel` or `/yt-flywheel` | Complete multi-asset package (essay + prompt kit + visual + Substack) | Publishing |

**Quality Gate**: Run at step 2→3 boundary. Brief must have Oren taste check PASSED and research provenance 🟢 before feeding to flywheel.

**Handoff**: `/mini-brief` output maps directly to `/ip-flywheel` Step 2:
- Elements 1-4 → "Core Hook & Stakes (Kallaway)"
- Element 3 → "Contrarian Angle (Dan Koe)"
- All 7 elements → "Outline/Beat Sheet"
- Platform Spec → format selection in Asset 1
- Element 7 (Expert Stack) → which experts to deploy for asset generation

---

## General Rules

1. **Never skip a chain step** — each step depends on the prior step's output
2. **Run quality gate at every boundary** — see `directives/quality_gate.md`
3. **Log chain execution** — note which steps completed in the task artifact
4. **If a step fails** — retry once, then halt the chain and notify user
5. **Use handoff summaries at every boundary** — see below and `directives/token-efficiency-protocol.md`

---

## Handoff Summary Protocol

**At every chain boundary, use a handoff summary.** Format and rationale: `directives/token-efficiency-protocol.md` Rule 1.

Estimated savings: 40-60% fewer tokens per chain execution.

---

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (chain boundary handoff executed), update the date and increment count.

*Created: 2026-02-17 | Updated: 2026-02-18 (added handoff summary protocol)*
*Component 3 of System Elevation*
