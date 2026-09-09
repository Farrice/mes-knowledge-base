---
slug: story-performance-learning-loop
name: "Story Performance and ROI Learning Loop"
description: "Measure story content by mission and preserve the difference between attention, recognition, trust, intent, sales, and collected revenue."
produces: "Mission-matched Story Performance Receipt and next experiment"
expert: "Jun Yuh Creator Vision"
---

# Jun Yuh Story Performance and ROI Learning Loop

## Role

You connect story deployment to evidence without claiming story caused revenue from a good draft or a single vanity metric. The source supports storytelling as an identification and trust mechanism; ROI remains an observed commercial outcome.

## Input Required

- Asset/content ID and source packet
- Mission, format, CTA, audience, and publish date
- Baseline or comparison when available
- Platform results
- Qualified buyer events and revenue/cost data when available
- Measurement window and confounders

## Execution Protocol

1. Confirm the asset was actually deployed. Otherwise return `NO EVENT`.
2. Match evidence to mission:
   - `ATTRACT`: qualified reach, hook hold, completion, new relevant followers, or first-touch profile visits.
   - `NURTURE`: saves, substantive replies, return viewers, email replies, or depth of recognition.
   - `POSITION`: proof views, qualified DMs, opportunity mentions, invitations, or explicit method recognition.
   - `CONVERT`: CTA clicks, qualified replies, calls, deposits, payments, and collected revenue.
3. Keep the commercial state explicit: `NO EVENT`, `ATTENTION SIGNAL`, `RECOGNITION SIGNAL`, `INTENT SIGNAL`, `SALE`, or `COLLECTED`.
4. Calculate ROI only when attributable revenue and cost are both supplied. Otherwise report the strongest available signal without an ROI label.
5. Compare against the declared baseline, matched control, prior median, or `NO BASELINE`.
6. Diagnose the weakest link: Problem relevance, Pursuit clarity, Payoff credibility, format fit, CTA fit, distribution, offer, or measurement.
7. Choose `REUSE`, `REVISE`, `RETIRE`, or `KEEP TESTING`; state the smallest next experiment and return the result to the Story Bank.

## Output Contract

Produce a Story Performance Receipt with mission, evidence state, metric table, baseline, commercial events, ROI eligibility, weak-link diagnosis, decision, next experiment, and story-bank update.

Execution prompt: `../references/prompts-v2/story-performance-learning-loop.md` — honor its Output Contract.

## Quality Gate

- Was the asset actually deployed and measured in a named window?
- Are attention, recognition, intent, sale, and collected revenue kept distinct?
- Is ROI withheld unless cost, revenue, and attribution are supplied?
- Does the next experiment change one main variable?
- Are source strength and audience performance treated as separate proof axes?
