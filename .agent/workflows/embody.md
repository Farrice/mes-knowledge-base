---
description: "Explicit-only /embody practice for absorbing one judgment from an extraction, artifact, or current session through retrieval, discrimination, transfer, recovery, and teach-back. Never auto-invoke."
tier: system
---

# /embody — Practice One Judgment Until It Becomes Yours

Use only when Farrice explicitly invokes `/embody`. This is a thin, run-scoped
mode of `/operator-school`, not a second teaching system and not a deliverable
engine.

## Invocation

```text
/embody this extraction
/embody this session
/embody <local-source-or-artifact-path>
/embody replay <saved-learning-record>
/embody --save <source-or-session>
```

If the pointer is ambiguous, use the current extraction, artifact, or decision
already active in the conversation. Ask one small question only when choosing
the wrong source would change the lesson.

## Pre-Flight

1. Load `.agent/workflows/operator-school.md` and the installed `teach` skill.
2. Read the exact extraction, source package, artifact, or accessible session
   evidence. Do not invent inaccessible conversation details.
3. When the material claims transfer or surpassing, preserve the proof boundary
   from `mastery-transfer-proof-spine.md`.
4. Select one decision unit: a cue-to-judgment relationship with a meaningful
   countercondition. Do not attempt to embody an entire expert or corpus in one
   run.

## Run-Scoped Default

Default to an interactive conversation with no file writes. Create or extend
`_active/operator-school/<topic>/` only when Farrice uses `--save` or explicitly
asks to preserve the practice over time. Do not schedule reminders, create an
automation, or change the current task without separate approval.

## Embody Loop

Run one prompt at a time so Farrice performs the judgment rather than reading a
finished lesson.

### 1. Cold Retrieval

Before revealing the source rule, ask:

- What decision does this intelligence change?
- What cues matter?
- What would make the method wrong here?
- Confidence: 0–100, with one reason.

Record the answer as the baseline. Confidence is calibration evidence, not a
score to maximize.

### 2. Judgment Card

Reveal a compact source-grounded card:

```markdown
## Judgment Card
- Decision:
- Trigger cues:
- Counterconditions:
- Failure tell:
- Source anchor:
- Proof boundary:
```

Separate what the source demonstrates, what the system infers, and what remains
unknown.

### 3. Blind Discrimination

Present two anonymized cases or outputs: one that embodies the judgment and one
that looks competent but misses it. Farrice chooses the stronger one and states
the decisive cue before seeing the tell. Do not reveal formatting, length, or
labels that leak the answer.

### 4. Near And Far Transfer

Give one unfamiliar same-domain case, then one cross-domain case when the
mechanic plausibly transfers. Farrice decides whether to apply, adapt, abstain,
or hand off. The countercondition is as important as the positive application.

### 5. Recovery Rep

Introduce one plausible failure or misleading cue. Farrice diagnoses what went
wrong and makes the smallest correction. Confidence is earned partly by knowing
how to recover, not by avoiding every error.

### 6. Performance And Teach-Back

Ask Farrice to make the decision, critique, or 5–10 line artifact without the
scaffold, then explain the rule in his own words. Preserve his native judgment
and voice; do not reward imitation of the source's terminology.

### 7. Calibration Verdict

Return:

```markdown
## Embody Receipt
- Judgment practiced:
- Baseline confidence:
- Discrimination:
- Near transfer:
- Far transfer or abstention:
- Recovery:
- Teach-back:
- Calibrated confidence:
- Current learning state: EXPOSED / PRACTICED / DISCRIMINATED / TRANSFERRED / RETAINED
- Weakest remaining cue:
- Replay condition:
- Source and proof boundary:
```

Use `RETAINED` only after a delayed replay on an unfamiliar case. A fluent same-
session answer cannot establish retention.

## Boundaries

- Never auto-invoke or insert this loop into ordinary extraction or production.
- Never substitute practice for the user's requested deliverable.
- Never increase a capability's Mastery Transfer proof state because Farrice
  completed a lesson; operator learning and system evidence are separate.
- Never present confidence as competence without decision evidence.
- Never persist a learning workspace unless Farrice asks.
- Never turn imitation into shipped voice or style.

## Quality Gate

- One judgment unit, not a whole expert.
- Source anchor and countercondition both present.
- Farrice acts before the tell is revealed.
- At least one abstain/adapt/handoff decision is possible.
- Feedback names the cue and smallest correction, not praise.
- Same-session fluency is not called retention.
- Explicit-only and no persistence by default.
