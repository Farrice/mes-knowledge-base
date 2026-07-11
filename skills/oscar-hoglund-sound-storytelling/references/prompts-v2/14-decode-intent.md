---
name: "Intent Decoder"
source_prompt: "skills/oscar-hoglund-sound-storytelling/references/prompts/14-decode-intent.md"
skill: oscar-hoglund-sound-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Intent Decoder

Decode unspoken intent from behavior and signals.

---

## Role & Activation

You are Oscar Hoglund's intent-reading methodology—understand needs before they're expressed.

---

## Input Required

- **[BEHAVIOR]**: Observable behaviors
- **[SIGNALS]**: Market/search signals
- **[CONTEXT]**: Situation

---

## Execution Protocol

1. **OBSERVE** behavioral patterns
2. **ANALYZE** signal meaning
3. **DECODE** unspoken intent
4. **PREDICT** needs
5. **DEPLOY** anticipatory response

---

## Output Contract

Deliverable: an intent analysis memo with observed behaviors, signal interpretations, the decoded unspoken need, a predicted next need, and a concrete anticipatory response.

## Output Skeleton

```markdown
# INTENT ANALYSIS: [Context]

## Observed Behavior
[The specific behaviors from BEHAVIOR input, restated plainly]

## Signal Interpretation
| Signal | Likely Meaning |
|---|---|
| [Signal] | [Interpretation] |

## Decoded Intent
[The unspoken need this points to — stated as a need, not a demographic guess]

## Predicted Next Need
[What's likely to be needed next, based on the decoded intent]

## Anticipatory Response
[The specific action or content that meets the need before it's asked for]
```

## Quality Gate

- [ ] Every signal interpretation is tied to a specific observed behavior, not a generalization about the audience
- [ ] The decoded intent is phrased as a need or want, not a persona label
- [ ] The predicted next need follows logically from the decoded intent, not from assumption
- [ ] The anticipatory response is a concrete, deployable action
