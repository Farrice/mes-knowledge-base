# Self-Annealing Quality Gate

> **Trigger**: Run silently after any output produced using an expert skill or agent persona.
> **Mode**: Silent — the user sees nothing unless a retry changes the output.
> **Inline version**: A compact version of this gate is embedded directly in `CLAUDE.md` under "Post-Output Quality Gate" for enforcement. This file contains the full protocol details.

---

## The 3-Point Gate

After generating output with a skill, run this internal check before delivering:

### 1. Intent Alignment
> Does this output match what the user actually asked for?

- Re-read the original request
- Check that scope hasn't drifted (answering a question they didn't ask)
- Verify the deliverable format matches expectations (list vs. prose, depth vs. breadth)

**Fail signal**: "This is good work, but it's not what they asked for."

### 2. Expert Standard
> Would the skill's expert be proud of this output?

- Does it embody the expert's *thinking style*, not just their terminology?
- Does it demonstrate nuance the expert would insist on?
- Would it pass the skill's named quality test (Kristen Stewart Test, By The Tail Test, Three Rules Test, etc.)?

**Fail signal**: "A junior could have produced this with a template."

### 3. Adversarial Resilience
> Would this survive a critic from the relevant domain?

- Is there a claim that wouldn't hold up under scrutiny?
- Any unsupported assertions presented as fact?
- Would a knowledgeable reader find something embarrassing?

**Fail signal**: "A domain expert would pick this apart in 30 seconds."

---

## On Failure

If **any** check fails:

1. **Diagnose** — Which check failed and why? (1 sentence)
2. **Fix** — Re-generate the failing section only (not the entire output)
3. **Re-check** — Run the 3-point gate on the revised output
4. **Maximum 1 retry** — If it still fails after 1 retry, deliver with a brief confidence note to the user: "I'm at medium confidence on [specific aspect]."

Do NOT loop. One retry maximum.

---

## Integration Points

- **Works with** `quality_assurance.md` (which covers research anti-patterns) — this gate covers *output quality*
- **Works with** `workflow-chains.md` — runs at each handoff point in a chain
- **Referenced by** GEMINI.md Operating Principles → Self-annealing loop

---

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, it should be reviewed for relevance or archived.

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-03-19 |

**Update Rule**: When this protocol fires (3-point check on any output), update the "Last Activated" date and increment the count.

---

*Created: 2026-02-17 | Component 3 of System Elevation*
