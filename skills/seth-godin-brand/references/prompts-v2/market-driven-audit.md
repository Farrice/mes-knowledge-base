---
name: "Seth Godin — Market-Driven Audit"
source_prompt: born-v2
skill: seth-godin-brand
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working from Seth Godin's marketing-operations methodology as extracted from "How to Build a Brand in the Era of AI" (Entrepreneur Studio podcast), specifically the distinction he attributes to his 1981-82 professor ("the George Distinction"): **marketing-driven** means the company is run BY the marketing department; **market-driven** means the company exists TO SERVE the market. These sound similar. They are opposites. Activate this frame: your job is to find every decision that touches the market and check whether marketing judgment — not the marketing department, marketing judgment — was in the room when it was made.

## Input Required

- **[ORGANIZATION]** — company or business being audited
- **[MARKETING TEAM SCOPE]** — what the marketing team currently owns
- **[RECENT DECISION EXAMPLES]** — 3-5 recent business decisions that affected customers, ideally spanning pricing, product, operations, and support

## Execution Protocol

### Step 1 — The George Distinction, Applied
Diagnose who made the last 5 decisions that affected how customers experience the business. Mostly marketing → possibly marketing-driven (department-centric, worth checking whether it's actually customer-centric or just department-territorial). Cross-functional → possibly market-driven. Engineering/finance alone, with marketing absent → neither — this is operations-driven, meaning marketing judgment is absent from decisions that ARE marketing decisions whether anyone calls them that or not.

### Step 2 — The VW Diesel Test
Anchor: five engineers and accountants decided to defeat emissions tests. It cost roughly $1B in fines. Was that a marketing move? Absolutely — it touched the market. Was marketing in the room? No. Apply this exact test to each input decision:
1. Did this decision touch the market (customers, community, perception)?
2. Was anyone with marketing judgment in the room?
3. If not — what was the actual cost, realized or latent?

Build the decision table for all input decisions, not a subset.

### Step 3 — The "Touches the Market" Map
Godin: *"Everything your company does that touches the market — how you design things, how you answer the phone, how much you charge, what you dump in the river — those are ALL marketing decisions."* Map every touchpoint across four zones, checking off what applies and noting who owns it and whether it's consistent with the brand promise:

**Pre-Purchase**: discovery channel, website/profile messaging, inquiry response, pricing signal.
**During Purchase**: buying experience, onboarding/first interaction, expectation-setting.
**Post-Purchase**: support/service quality, follow-up communication, mistake handling, how referrals are earned.
**Invisible Marketing**: employee behavior customers see, environmental/community impact, partner/vendor relationships visible to market, internal decisions that leak externally.

This map should run to at least 15 touchpoints — a shallow map (fewer than the visible/invisible zones combined) under-diagnoses the org.

### Step 4 — Market-Driven Realignment
For every touchpoint where marketing judgment is absent: name the gap, assess the VW-Diesel-equivalent risk (what could go wrong, concretely), design the intervention (how marketing perspective gets inserted — not "marketing owns everything" but "marketing has input on everything that touches the market"), and define ownership.

## Output Contract

Deliver exactly these components:
1. Current-state verdict — Marketing-Driven / Market-Driven / Operations-Driven, with the evidence from the last-5-decisions diagnostic
2. VW Diesel decision table for all input decisions (touched market? / marketing present? / outcome)
3. Touchpoint map — minimum 15 touchpoints across all 4 zones, each with owner and promise-consistency note
4. Critical Gaps — at least 3, each with gap + risk + specific intervention
5. Realignment Priority — Immediate / 30-day / 90-day, each tied to a specific gap from #4

Length: the touchpoint map should be exhaustive within the four zones listed, not trimmed for brevity — this audit's value is in the coverage.

## Output Skeleton

```
MARKET-DRIVEN AUDIT
=====================

Organization: [name]
Current State: [Marketing-Driven / Market-Driven / Operations-Driven]
Evidence: [who made the last 5 customer-affecting decisions]

VW DIESEL DECISION TABLE:
| Decision | Touched Market? | Marketing Present? | Outcome |
|---|---|---|---|
[one row per input decision]

TOUCHPOINT MAP:
Pre-Purchase: [list, owner, promise-consistent Y/N]
During Purchase: [list, owner, promise-consistent Y/N]
Post-Purchase: [list, owner, promise-consistent Y/N]
Invisible Marketing: [list, owner, promise-consistent Y/N]
Coverage: [X] touchpoints mapped, [Y] with marketing input

CRITICAL GAPS:
1. [Gap] — Risk: [VW-Diesel-equivalent] — Intervention: [specific fix]
2. [Gap] — Risk: [...] — Intervention: [...]
3. [Gap] — Risk: [...] — Intervention: [...]

REALIGNMENT PRIORITY:
- Immediate: [highest-risk gap]
- 30-day: [systematic input mechanism]
- 90-day: [culture shift to market-driven]
```

## Quality Gate

- Is the touchpoint map at 15+ items across all four zones, not concentrated in just Pre-Purchase?
- Does at least one VW Diesel Test row surface a real hidden risk — a decision that touched the market with no marketing judgment present — rather than every row coming back clean?
- Is each Critical Gap's intervention specific and assignable (a named mechanism, not "improve communication")?
- Does the current-state verdict cite the actual last-5-decisions evidence rather than asserting a verdict first and rationalizing it after?
- Is the Realignment Priority time-bound (Immediate/30-day/90-day) with each tier tied to a specific named gap?

## Deploy When

Use this prompt when a user asks "is my company serving the market or serving itself?", suspects marketing is siloed as a department rather than a company-wide judgment layer, or needs to explain to leadership why a non-marketing decision (pricing, ops, product) caused a customer-trust problem.
