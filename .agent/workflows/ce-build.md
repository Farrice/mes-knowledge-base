---
description: Full end-to-end context-engineering build (supercomputer-grade)
---

## Workflow: Full Context-Engineering Build (`/ce-build`)

**Expert**: Chase Hughes (Context Engineering)
**Skill**: `skills/chase-hughes-context-engineering/`

The supercomputer-grade composite — end-to-end context-engineering build for a complete offer / campaign / content-system in one run: upstream → force-map → PCP → conditions → followability → Defense/Ethics Gate → production handoff. Stacks with `/supercomputer` for multi-deliverable missions (anchor memory + cost gate).

### Steps

1. Read the skill files:
   - `skills/chase-hughes-context-engineering/SKILL.md`
   - `skills/chase-hughes-context-engineering/genius.md`
   - `skills/chase-hughes-context-engineering/references/context-design-spec.md`
   - `skills/chase-hughes-context-engineering/references/pcp-and-upstream.md`
   - `skills/chase-hughes-context-engineering/references/fear-fractionation-pressure.md`
   - `skills/chase-hughes-context-engineering/references/followability-confidence-rapport.md`

2. Read and execute the workflow:
   - `skills/chase-hughes-context-engineering/workflows/ce-build.md`

3. **Deterministic Defense/Ethics Gate (BLOCKING)** — run on the full spec before any production handoff:
   ```bash
   // turbo
   python3 execution/context_ethics_gate.py check --file <spec-path> --kind spec --workflow ce-build --technique "<named techniques>"
   # exit 2 = BLOCK (rewrite); REVIEW = clear flags; PASS = proceed to handoff
   ```

4. For multi-deliverable missions, run under `/supercomputer` (anchor memory + cost gate). Hand each piece to its production expert (Luke Iha copy, Lara Acosta LinkedIn, Caleb 4C, etc.).

5. Quality gate: every offensive mechanic deployed with its defense; destabilization check passed (reducing chaos + supplying clarity, not manufacturing chaos to sell the cure).
