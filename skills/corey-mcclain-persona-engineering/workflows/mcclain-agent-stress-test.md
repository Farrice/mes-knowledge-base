---
name: Agent Stress Test
command: /mcclain-agent-stress-test
expert: Corey McClain
category: Agent Forge
description: Validate agent quality — controlled comparisons, identity consistency, worldview filtering
inputs: Assembled agent (all files deployed), 3+ test tasks
outputs: Validation report — pass/fail on 5 dimensions with improvement prescriptions
---

# Agent Stress Test

Five-dimension validation before an agent goes live. Not "does it work" — "does the persona elevate the output." Controlled conditions. Clear pass/fail.

## Pre-Flight Gate

- [ ] Agent fully assembled (all LLMP layers installed)
- [ ] Persona document loaded into context
- [ ] 3+ test tasks prepared (representative of real usage)

## Tests

### Test 1 — Vanilla Comparison

Run one task WITH persona, controlled-delete, run SAME task vanilla. Compare side by side.

**Pass criteria**: Clear qualitative gap — different structure, voice, and decisions (not just tone).
**Fail prescription**: Persona too thin → add worldview depth, messy details, sharpen voice.

### Test 2 — Identity Consistency

Run 3 different tasks (primary, secondary, edge-case). Review for voice/worldview consistency.

**Pass criteria**: All 3 outputs identifiable as same agent in blind test.
**Fail prescription**: Worldview not deep enough → add decision-shaping beliefs. Voice breaks → expand vocabulary/forbidden lists.

### Test 3 — Worldview Filtering

Create a decision scenario with 2+ valid approaches. Run through persona agent. Verify the agent chose based on worldview, not generic best practice.

**Pass criteria**: Decision traces to a specific worldview belief.
**Fail prescription**: Beliefs too abstract → make them concrete and decisional.

### Test 4 — Output Distinction

Run same task through persona agent, vanilla, and (if available) a different agent. Remove labels. Can you identify which is which?

**Pass criteria**: Correct blind identification.
**Fail prescription**: Add more messy details and worldview contradictions — these create the fingerprint.

### Test 5 — Persona Leakage

Run production task. Check output for ANY explicit mention of persona name, backstory, or details.

**Pass criteria**: Zero leakage. Persona felt but never stated.
**Fail prescription**: Restructure how persona loads — it sets atmosphere, not instructions.

## Report Template

```markdown
# Stress Test Report: [Agent Name] — [Date]

| Test | Result | Notes |
|------|--------|-------|
| 1. Vanilla Comparison | PASS/FAIL | |
| 2. Identity Consistency | PASS/FAIL | |
| 3. Worldview Filtering | PASS/FAIL | |
| 4. Output Distinction | PASS/FAIL | |
| 5. Persona Leakage | PASS/FAIL | |

### Overall: [PASS / CONDITIONAL / FAIL]
### Prescriptions: [If any]
```

## Output Schema

A single **Stress Test Report** (see `## Report Template` above), saved as `agents/[name]/memory/stress-test-[date].md`:

- Title: `# Stress Test Report: [Agent Name] — [Date]`
- 5-row results table (Test 1-5, each PASS/FAIL, notes)
- `### Overall: [PASS / CONDITIONAL / FAIL]`
- `### Prescriptions:` — one specific, actionable fix per failed test (never generic "improve the persona")

## Quality Gate

- [ ] All 5 tests executed with controlled conditions
- [ ] Validation report produced
- [ ] Failures have specific, actionable prescriptions
- [ ] Agent marked production-ready only after all tests pass
