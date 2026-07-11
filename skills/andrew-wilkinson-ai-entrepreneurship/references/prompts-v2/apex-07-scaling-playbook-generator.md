---
name: "APEX-07: Scaling Playbook Generator"
source_prompt: "skills/andrew-wilkinson-ai-entrepreneurship/references/prompts/apex-07-scaling-playbook-generator.md"
skill: andrew-wilkinson-ai-entrepreneurship
standard: structure-pure-v2
refactored: 2026-07-11
---

# APEX-07: Scaling Playbook Generator

Transform a working product into a scalable revenue machine.

## Role

You architect the transition from "I built a thing" to a repeatable revenue system.

## Input Required

- **[PRODUCT]**: What you've built
- **[CURRENT_REVENUE]**: If any (even $0)
- **[CURRENT_CUSTOMERS]**: Number and type
- **[TIME_TO_SCALE]**: 30/60/90 day target

## Execution Protocol

### Phase 1: Foundation Lock (Days 1-7)
1. Identify highest-paying use case
2. Document customer acquisition path
3. Establish metrics dashboard

### Phase 2: Traffic Engine (Days 8-21)
1. Pick ONE acquisition channel
2. Build content/outreach machine
3. Optimize conversion

### Phase 3: Revenue Optimization (Days 22-30)
1. Raise prices where underpriced
2. Add upsells/cross-sells
3. Implement retention systems

## Output Contract

Deliver a **Scaling Playbook**:

- **Format**: Markdown with revenue targets, unit economics, channel strategy, pricing, and a phased checklist
- **Length**: 500-700 words
- **Required components** (all must appear):
  1. Revenue Target — current, 30-day goal, 90-day goal
  2. Unit Economics — LTV, CAC, LTV:CAC ratio, payback period (with estimation method noted if inputs are unknown)
  3. The One Channel Rule — exactly one primary channel with a stated reason it beat the alternatives, plus the condition that unlocks a secondary channel
  4. Traffic Machine Blueprint — the content/outreach system, distribution path, conversion mechanism, and what Claude Code can automate vs. what needs a human
  5. Pricing Strategy — current price, recommended price, and a justification tied to delivered value (not just "raise it")
  6. Upsell Architecture — base product plus at least two additional tiers
  7. 30-Day Scaling Checklist broken into four weeks (Foundation / Traffic / Conversion / Optimization)
  8. Danger Signals and Success Indicators — at least two concrete, checkable conditions each

## Output Skeleton

```markdown
# SCALING PLAYBOOK: [Product Name]

## Revenue Target
**Current**: $[X]/month
**30-day goal**: $[X]/month
**90-day goal**: $[X]/month

## Unit Economics
**Customer LTV**: $[X]
**CAC**: $[X]
**LTV:CAC ratio**: [X]:1
**Payback period**: [X] days

## The One Channel Rule
**Primary channel**: [choice]
**Why this one**: [reasoning vs. alternatives]
**Secondary (unlocked after [milestone])**: [choice]

## Traffic Machine Blueprint

### Content/Outreach System
**Daily output**: [what you create]
**Distribution**: [where it goes]
**Conversion mechanism**: [how interest becomes purchase]

### Automation Requirements
- [ ] [what Claude Code can automate]
- [ ] [what needs human touch]

## Pricing Strategy
**Current price**: $[X]
**Recommended price**: $[X]
**Price justification**: [why customers will pay, tied to value delivered]

## Upsell Architecture
1. **Base product**: $[X]
2. **Add-on 1**: $[X] — [what]
3. **Premium tier**: $[X] — [what]

## 30-Day Scaling Checklist

### Week 1: Foundation
- [ ] [task]
- [ ] [task]

### Week 2: Traffic
- [ ] [task]
- [ ] [task]

### Week 3: Conversion
- [ ] [task]
- [ ] [task]

### Week 4: Optimization
- [ ] [task]
- [ ] [task]

## Danger Signals
If you see these, pivot:
- [signal]
- [signal]

## Success Indicators
You're on track when:
- [indicator]
- [indicator]
```

## Quality Gate

- Exactly one primary acquisition channel is named, with a stated reason it was chosen over the alternatives considered
- Unit economics section includes all four figures (LTV, CAC, ratio, payback), with an estimation method noted wherever an input is unknown
- Pricing recommendation is justified by value delivered to the customer, not by a bare instruction to charge more
- Danger Signals and Success Indicators each list at least two concrete, checkable conditions — not vague sentiment
- Secondary channel is explicitly gated behind a stated revenue milestone, not introduced as a parallel effort from day one
- Automation Requirements splits tasks between "Claude Code can do this" and "needs a human," with at least one item in each
