---
description: Context-Design Spec — the Context Engineering OS front door
---

## Workflow: Context-Design Spec (`/ce-design`)

**Expert**: Chase Hughes (Context Engineering)
**Skill**: `skills/chase-hughes-context-engineering/`

The operating-layer orchestrator. Input one desired end-state + target + channel; output an 8-section Context-Design Spec a production expert can execute. Runs 5 internal stages: Upstream → Force-Map → PCP → Conditions-Build → Defense/Ethics Gate → Followability.

### Steps

1. Read the skill files:
   - `skills/chase-hughes-context-engineering/SKILL.md`
   - `skills/chase-hughes-context-engineering/genius.md`
   - `skills/chase-hughes-context-engineering/references/pcp-and-upstream.md`
   - `skills/chase-hughes-context-engineering/references/context-design-spec.md`
   - `skills/chase-hughes-context-engineering/references/fear-fractionation-pressure.md` (Stage 1 ambient forces)

2. Read and execute the workflow:
   - `skills/chase-hughes-context-engineering/workflows/ce-design.md`

3. **Deterministic Defense/Ethics Gate (Stage 4, BLOCKING)** — run before the spec ships:
   ```bash
   // turbo
   python3 execution/context_ethics_gate.py check --file <spec-path> --kind spec --workflow ce-design --technique "<named technique>"
   # exit 2 = BLOCK (rewrite); REVIEW = clear the named flags; PASS = proceed
   ```

4. Quality gate: Could you defend the full design if the target saw it? Is the outcome good on its own merits, stripped of the engineered receptivity? If the design only works by hiding what it does, it fails.
