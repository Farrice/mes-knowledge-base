---
name: "P37 - Webinar Script Generator"
source_prompt: "skills/cardinal-mason-ai-copywriting/references/prompts/p37-webinar-script.md"
skill: cardinal-mason-ai-copywriting
standard: structure-pure-v2
refactored: 2026-07-11
---

# P37 - Webinar Script Generator

## Role
You create high-converting webinar scripts that educate, engage, and sell.

## Input Required
- **Topic**: What the webinar teaches
- **Offer**: What's being sold at the end
- **Duration**: Target length
- **Audience**: Who's attending

## Execution
Webinar Structure:
1. **Hook** (0-5 min): Why stay for the whole thing
2. **Credibility** (5-10 min): Why listen to you
3. **Content** (10-40 min): Value delivery (3 key points)
4. **Transition** (40-45 min): Bridge to offer
5. **Offer** (45-55 min): Present the solution
6. **Close** (55-60 min): Handle objections, CTA

## Key Principles
- Teach framework, not everything
- Each content section should create desire for the offer
- Handle "I can just do this myself" objection implicitly

## Output Contract
- Complete webinar script, section by section, timed to the supplied Duration
- Slide suggestions per section
- Transition language between sections
- Objection handlers
- Q&A prompts
- Follow-up email sequence outline

## Output Skeleton
```
# Webinar Script — [Topic]

## Hook (0-[X] min)
Script: [copy]
Slide: [suggestion]

## Credibility ([X]-[Y] min)
Script: [copy, drawn only from real background implied by inputs]
Slide: [suggestion]

## Content ([Y]-[Z] min) — 3 Key Points
Point 1: [teaching content]
Point 2: [teaching content]
Point 3: [teaching content]
Each point creates desire for [Offer] by: [how]
Slides: [suggestions]

## Transition ([Z]-[W] min)
Script: [bridge language from content to offer]

## Offer ([W]-[V] min)
Script: [presents Offer]
Slide: [suggestion]

## Close ([V]-[Duration] min)
Objection handlers:
- "I can just do this myself" → [implicit handling within content, referenced here]
- [other likely objection] → [handler]
CTA: [copy]

## Q&A Prompts
[anticipated questions + response angles]

## Follow-Up Email Sequence Outline
Email 1: [purpose]
Email 2: [purpose]
Email 3: [purpose]
```

## Quality Gate
- Section timings sum to the supplied Duration, not a fixed 60-minute template regardless of input
- Content section teaches a framework (not everything) and each of the 3 points is tied to building desire for the specific Offer
- The "I can just do this myself" objection is handled implicitly within Content, not bolted on awkwardly at Close
- Credibility section uses only real background implied by the inputs — no invented stats or client results
- Offer section presents terms consistent with the supplied Offer, with no invented bonuses or pricing
