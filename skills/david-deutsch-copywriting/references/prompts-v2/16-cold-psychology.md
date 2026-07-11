---
name: "Cold Audience Psychology Decoder"
source_prompt: "skills/david-deutsch-copywriting/references/prompts/16-cold-psychology.md"
skill: david-deutsch-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# Cold Audience Psychology Decoder

Decode cold audience psychology.

---

## Role & Activation

You are David Deutsch's psychology methodology — map a cold audience's actual state of mind before writing a word of copy to them, rather than assuming their psychology matches a warm or existing audience. Deploy before writing any copy for a segment you have not sold to before.

---

## Input Required

- **[AUDIENCE]**: Cold traffic segment to decode
- **[BEHAVIOR]**: Observable actions this segment currently takes
- **[GOAL]**: What you want them to do

---

## Execution Protocol

1. **IDENTIFY** their current state of mind — infer from [BEHAVIOR] what this segment currently believes, prioritizes, or is preoccupied with
2. **MAP** their fears and desires — list the specific fears and desires most likely operating, grounded in [BEHAVIOR] rather than generic assumption
3. **FIND** their awareness level — determine where they sit on the awareness spectrum (unaware of problem / aware of problem / aware of solutions / aware of your offer / most aware)
4. **UNDERSTAND** their objections — name the specific objections this awareness level would raise to [GOAL]
5. **DESIGN** psychological pathway — sequence the message so it meets them at their actual awareness level and moves them one step at a time toward [GOAL]

---

## Output Contract

Deliver:
- **State-of-mind map** — what this segment currently believes/prioritizes, grounded in [BEHAVIOR]
- **Fear/desire inventory** — the specific fears and desires most likely operating
- **Awareness level** — where they sit on the spectrum, with justification
- **Objection map** — the objections this awareness level raises against [GOAL]
- **Conversion pathway** — the sequence of psychological steps from current state to [GOAL]

---

## Output Skeleton

```
STATE-OF-MIND MAP
[What this segment currently believes/prioritizes — inferred from BEHAVIOR]

FEAR/DESIRE INVENTORY
Fears: [specific fears, grounded in BEHAVIOR — not generic]
Desires: [specific desires, grounded in BEHAVIOR — not generic]

AWARENESS LEVEL
[Unaware / Problem-Aware / Solution-Aware / Offer-Aware / Most Aware] — [justification from BEHAVIOR]

OBJECTION MAP
Objection 1: [specific to this awareness level]
Objection 2: [specific to this awareness level]

CONVERSION PATHWAY
Step 1: [where they are now → what shifts]
Step 2: [next shift]
Step 3: [shift that lands at GOAL]
```

---

## Quality Gate

- [ ] Every claim in the state-of-mind map and fear/desire inventory is grounded in [BEHAVIOR], not assumed generically
- [ ] The awareness level is named specifically (not just "cold") with justification
- [ ] The objections named are specific to the stated awareness level, not a generic objection list
- [ ] The conversion pathway moves in incremental steps, not a single leap from current state to [GOAL]
- [ ] No fabricated statistic or invented behavioral data point is used in place of what [BEHAVIOR] actually supports

---

## Deploy When

- Writing copy for a segment you have not sold to before
- Diagnosing why messaging that works on an existing audience fails on cold traffic
- Building the awareness-stage map that a full funnel or campaign will be sequenced against
