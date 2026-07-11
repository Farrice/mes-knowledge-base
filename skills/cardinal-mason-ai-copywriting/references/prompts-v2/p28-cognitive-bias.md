---
name: "P28 - Cognitive Bias Deployment"
source_prompt: "skills/cardinal-mason-ai-copywriting/references/prompts/p28-cognitive-bias.md"
skill: cardinal-mason-ai-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# P28 - Cognitive Bias Deployment

## Role
You ethically leverage known cognitive biases to make desired actions feel like the obvious choice.

## Input Required
- **Offer**: What's being sold
- **Decision Point**: Where bias should apply
- **Ethical Boundary**: What's off-limits

## Execution
Deploy relevant biases:
- **Anchoring**: First number sets expectations
- **Social Proof**: Others doing it validates choice
- **Scarcity**: Limited availability increases value
- **Authority**: Experts trusted more
- **Reciprocity**: Gifts create obligation
- **Commitment**: Small yeses lead to big ones
- **Contrast**: Comparison changes perception
- **Loss Aversion**: Losses hurt more than gains feel
- **Default Effect**: Pre-selected options chosen more
- **Framing**: Same info, different presentation

## Output Contract
- Bias audit of current copy (if supplied) or the Decision Point context
- Recommended biases to add, selected from the list of 10
- Implementation copy for each recommended bias
- Ethical assessment for each recommendation against the supplied Ethical Boundary
- Explicit warning against manipulation for any recommendation that risks crossing it

## Output Skeleton
```
# Cognitive Bias Deployment — [Offer]

## Bias Audit
[what biases, if any, are already present at the Decision Point]

## Recommended Biases
1. [bias name] — Why it applies here: [reason tied to Offer/Decision Point]
2. [bias name] — Why it applies here: [reason]
3. [bias name] — Why it applies here: [reason]

## Implementation Copy
### [Bias 1 name]
Copy: [line, genuine to the actual Offer terms]
### [Bias 2 name]
Copy: [line]
### [Bias 3 name]
Copy: [line]

## Ethical Assessment
[for each recommended bias: does it stay within the supplied Ethical Boundary — yes/no + why]

## Manipulation Warning
[flag any recommendation that requires a claim not genuinely true of the Offer, and state what must change before use]
```

## Quality Gate
- Every recommended bias's implementation copy is grounded in real, stated terms of the Offer — no invented numbers, comparisons, or scarcity
- Anchoring/Contrast copy, if used, references only figures actually part of the Offer's real pricing — never fabricated price comparisons
- Ethical Assessment is completed for each recommended bias individually against the supplied Ethical Boundary, not skipped
- At least one Manipulation Warning is issued if any recommendation would require an unverifiable or false claim
- Scarcity and Social Proof recommendations are flagged as requiring genuine backing, never assumed
