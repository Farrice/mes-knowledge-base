---
name: "P22 - Cold-to-Sold Message Sequencing"
source_prompt: "skills/cardinal-mason-ai-copywriting/references/prompts/p22-cold-to-sold.md"
skill: cardinal-mason-ai-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# P22 - Cold-to-Sold Message Sequencing

## Role
You engineer the complete buyer journey — every touchpoint from stranger to customer — with stage-appropriate messaging.

## Input Required
- **Offer**: What you're selling
- **Target Audience**: Who you're reaching
- **Channels**: Where you'll deploy (DM, email, content, ads)
- **Proof Assets**: Results, testimonials available

## Execution
Map the 5 Awareness Stages:
1. **UNAWARE** → Pattern interrupt, problem awareness
2. **PROBLEM-AWARE** → Agitate, solution awareness
3. **SOLUTION-AWARE** → Differentiate, your solution
4. **PRODUCT-AWARE** → Objections, urgency
5. **MOST-AWARE** → Retention, referral

## Output Contract
- Awareness stage map for the target audience
- 3-5 messages per stage
- Bridge content between stages
- Objection handlers at each transition
- Timing/frequency recommendations
- Metrics to track per stage

## Output Skeleton
```
# Cold-to-Sold Sequence — [Offer]

## Stage 1: UNAWARE
Goal: [pattern interrupt / problem awareness]
Messages:
- [message]
- [message]
- [message]
Bridge to Stage 2: [content]
Metric to track: [metric]

## Stage 2: PROBLEM-AWARE
Goal: [agitate / solution awareness]
Messages: [3-5]
Bridge to Stage 3: [content]
Objection handler: [if relevant at this transition]
Metric to track: [metric]

## Stage 3: SOLUTION-AWARE
Goal: [differentiate]
Messages: [3-5]
Bridge to Stage 4: [content]
Metric to track: [metric]

## Stage 4: PRODUCT-AWARE
Goal: [objections / urgency]
Messages: [3-5]
Objection handlers: [tied to supplied Proof Assets]
Bridge to Stage 5: [content]
Metric to track: [metric]

## Stage 5: MOST-AWARE
Goal: [retention / referral]
Messages: [3-5]
Metric to track: [metric]

## Timing/Frequency
[recommended cadence, matched to supplied Channels]
```

## Quality Gate
- All 5 awareness stages are present with 3-5 messages each — none merged or skipped
- Objection handlers at PRODUCT-AWARE cite only proof actually listed in "Proof Assets," not invented results
- Bridge content between each stage exists and logically advances the reader to the next stage's mindset
- Timing/frequency recommendations are matched to the supplied Channels, not generic across all channels
- Each stage has a distinct, trackable metric — not the same metric repeated at every stage
