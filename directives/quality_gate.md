# Self-Annealing Quality Gate

> **Trigger**: Run silently after any output produced using an expert skill or agent persona.
> **Mode**: Silent — the user sees nothing unless a retry changes the output.
> **Feeds into**: `directives/feedback-ratchet.md` — quality scores from this gate are logged to the Performance Log database for longitudinal tracking.
> **Fires when**: ANY output was produced using an expert skill, agent persona, or workflow. This includes content, strategy, research, copy, analysis, and creative work.
> **Does NOT fire for**: Pure system operations (file reads, git commands, directory listings) where no expert skill was loaded.
> **"Trivial" and "follow-up" are NOT skip conditions.** If an expert was loaded and output was produced, the gate fires.

---

## The 3-Point Gate (Scored)

After generating output with a skill, run this internal check before delivering. **Score each dimension 1-10** for the feedback ratchet.

### 1. Intent Alignment (Score: 1-10)
> Does this output match what the user actually asked for?

- Re-read the original request
- Check that scope hasn't drifted (answering a question they didn't ask)
- Verify the deliverable format matches expectations (list vs. prose, depth vs. breadth)

| Score | Meaning |
|-------|---------|
| 9-10 | Precisely addresses the request, correct format and scope |
| 7-8 | Addresses the core request, minor scope drift |
| 5-6 | Partially addresses the request, some misalignment |
| 3-4 | Significant drift from what was asked |
| 1-2 | Wrong deliverable entirely |

**Fail signal (score < 6)**: "This is good work, but it's not what they asked for."

### 2. Expert Standard (Score: 1-10)
> Would the skill's expert be proud of this output?

- Does it embody the expert's *thinking style*, not just their terminology?
- Does it demonstrate nuance the expert would insist on?
- Would it pass the skill's named quality test (Kristen Stewart Test, By The Tail Test, Three Rules Test, etc.)?

| Score | Meaning |
|-------|---------|
| 9-10 | Indistinguishable from the expert's own work |
| 7-8 | Captures expert's depth; minor nuance gaps |
| 5-6 | Uses expert's framework but lacks their insight |
| 3-4 | Generic output wearing expert terminology |
| 1-2 | Could have been produced without loading the skill |

**Fail signal (score < 6)**: "A junior could have produced this with a template."

### 3. Adversarial Resilience (Score: 1-10)
> Would this survive a critic from the relevant domain?

- Is there a claim that wouldn't hold up under scrutiny?
- Any unsupported assertions presented as fact?
- Would a knowledgeable reader find something embarrassing?

| Score | Meaning |
|-------|---------|
| 9-10 | Bulletproof — every claim supported, no weak points |
| 7-8 | Solid — minor nitpicks possible but nothing substantive |
| 5-6 | Some claims would need backing under scrutiny |
| 3-4 | Contains unsupported assertions or logical gaps |
| 1-2 | Domain expert would dismiss this immediately |

**Fail signal (score < 6)**: "A domain expert would pick this apart in 30 seconds."

### Composite Quality Score

**Quality Score = average of all three sub-scores**, rounded to nearest integer.

- **7+**: Pass — deliver as-is
- **5-6**: Marginal — retry the weakest dimension
- **< 5**: Fail — retry required

---

## On Failure

If composite score < 7 OR any single dimension < 6:

1. **Diagnose** — Which check failed and why? (1 sentence)
2. **Fix** — Re-generate the failing section only (not the entire output)
3. **Re-check** — Run the 3-point gate on the revised output
4. **Maximum 1 retry** — If it still fails after 1 retry, deliver with a brief confidence note to the user: "I'm at medium confidence on [specific aspect]."

Do NOT loop. One retry maximum.

---

## Performance Logging

After delivery (whether first pass or after retry), log to the feedback ratchet:

```python
from execution.log_performance import log_output

log_output(
    output="[brief description]",
    agent="[agent-name]",
    skill="[skill-name]",
    workflow="[workflow-file]",
    task_type="[type]",
    quality_score=[composite],
    intent_alignment=[score],
    expert_standard=[score],
    adversarial_resilience=[score],
    status="Keep" if composite >= 7 else "Needs Improvement",
    notes="[what worked/didn't]",
)
```

This is how the ratchet accumulates data. Without logging, the system cannot detect regression or identify improvement candidates.

---

## Integration Points

- **Feeds into** `directives/feedback-ratchet.md` — quality scores logged to Performance Log for longitudinal tracking
- **Works with** `quality_assurance.md` (which covers research anti-patterns) — this gate covers *output quality*
- **Works with** `workflow-chains.md` — runs at each handoff point in a chain

---

## Usage Tracking

> **Purpose**: Detect dead infrastructure. If this directive hasn't fired in 30 days, it should be reviewed for relevance or archived.

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-03-11 (retroactive session diagnosis) |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-04-11 |

**Update Rule**: When this protocol fires (3-point check on any output), update the "Last Activated" date and increment the count.

---

*Created: 2026-02-17 | Updated: 2026-03-10 (scored dimensions + feedback ratchet integration)*
