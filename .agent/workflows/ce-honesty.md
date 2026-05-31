---
description: Benevolent SMRP honesty protocol (consent-gated)
---

## Workflow: Benevolent Honesty Protocol (`/ce-honesty`)

**Expert**: Chase Hughes (Context Engineering)
**Skill**: `skills/chase-hughes-context-engineering/`

Dissolve the four resistance walls (Socialize-Minimize-Rationalize-Project) so someone can safely name a hidden truth or the real objection. Sales discovery, coaching breakthroughs, hard conversations. Opens with a hard consent / power-asymmetry pre-flight.

### Steps

1. Read the skill files:
   - `skills/chase-hughes-context-engineering/SKILL.md`
   - `skills/chase-hughes-context-engineering/genius.md`
   - `skills/chase-hughes-context-engineering/references/interrogation-and-honesty.md`

2. **Consent pre-flight (BLOCKING):** Can the other party freely exit the conversation? If they are an employee, subordinate, or intimate partner mid-conflict — anyone in your power who cannot walk away — STOP. Running SMRP here is coercive regardless of intent.

3. Read and execute the workflow:
   - `skills/chase-hughes-context-engineering/workflows/ce-honesty.md`

4. **Deterministic ethics gate:**
   ```bash
   // turbo
   python3 execution/context_ethics_gate.py check --file <design-path> --kind honesty --workflow ce-honesty --technique "SMRP four-wall dissolution"
   # exit 2 = BLOCK; REVIEW = clear power-asymmetry flags; PASS = proceed
   ```

5. Quality gate: Is the aim the person's freedom (naming a truth/objection they want named), or extraction? If extraction — stop.
