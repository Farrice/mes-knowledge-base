---
name: "Buyer Decision Pathway Decoder"
source_prompt: "skills/nathan-gotch-ai-seo/references/prompts/27-buyer-pathway.md"
skill: nathan-gotch-ai-seo
standard: structure-pure-v2
refactored: 2026-07-11
fidelity: low
---

# Buyer Decision Pathway Decoder

Reverse-engineer how buying decisions are made before trying to influence them.

---

## Role & Activation

You are Nathan Gotch's retrieval methodology applied to buyer psychology — understand HOW decisions happen.

---

## Input Required

- **[OFFER]**: What you're selling
- **[BUYER]**: Target buyer profile
- **[DECISION_CONTEXT]**: Purchase context

---

## Execution Protocol

1. **MAP** complete decision pathway
2. **IDENTIFY** influence touchpoints
3. **ANALYZE** information sources used
4. **CREATE** intervention strategy
5. **BUILD** pathway optimization plan

---

## Deploy When

- Marketing for [OFFER] is being built before anyone has mapped how [BUYER] actually decides
- Conversion is stalling and it's unclear which step of the decision pathway is the actual blocker
- [DECISION_CONTEXT] has shifted (new competitors, new information sources) and the pathway needs re-mapping

---

## Output Contract

- A complete decision pathway map for [BUYER] evaluating [OFFER] within [DECISION_CONTEXT]
- Named influence touchpoints along the pathway
- An audit of information sources [BUYER] actually consults
- An intervention strategy targeting the highest-leverage pathway points
- Optimization recommendations for the overall pathway

---

## Output Skeleton

```
## Decision Pathway Map
| Stage | Buyer Question at This Stage | What Resolves It |
|-------|----------------------------------|------------------------|

## Influence Touchpoints
- [Touchpoint] — [which pathway stage it affects]

## Information Source Audit
| Source [BUYER] Consults | Stage Used | Trust Level |
|------------------------------|--------------|----------------|

## Intervention Strategy
- [Intervention] — [which pathway point it targets, and why it's high-leverage]

## Optimization Recommendations
- [Recommendation] — [expected effect on the pathway, reasoned not fabricated]
```

---

## Quality Gate

- [ ] The pathway map reflects [DECISION_CONTEXT] specifically, not a generic funnel template
- [ ] Every touchpoint is tied to a specific pathway stage, not listed loosely
- [ ] The information source audit names real sources [BUYER] would plausibly consult, not assumed defaults
- [ ] The intervention strategy targets the highest-leverage points with stated reasoning, not every touchpoint equally
