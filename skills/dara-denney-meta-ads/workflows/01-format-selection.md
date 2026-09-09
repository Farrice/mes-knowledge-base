---
description: Select 2-3 Meta ad formats using Dara Denney's dated 51-type source prior plus job, evidence, access, funnel, friction, claims, and durability gates
---

# `/dara-format-selection` — Format Archetype Selection

Run as the entry point for any Meta ads campaign. Output: a ranked brief naming 2-3 format archetypes paired with messaging strategy, with reasoning grounded in funnel position, audience age, operational maturity, creative budget, and brand maturity.

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **The 8 archetypes** (David & Goliath, Obvious AI Slop, TikTok Love Letter, TikTok Short, We're Not Cheap, We're Sorry, Listical, Yapper)
- **The latest 48-board-group / 51-type source prior** in `references/creative-format-intelligence.md`
- **Format Selection Decision Tree** (5 questions)
- **Format → Messaging Pairing Logic** table
- **Format-then-Messaging Separation** (Pattern 4): vehicle vs. cargo
- **Annual Arbitrage Hunting** (Pattern 1): tag arbitrage stage early/mass/saturated

## Input Required

- **Brand**: name, category, what they sell, hero product
- **Target audience**: demographic (age range critical), psychographic, where they currently are (renting? researching? past customer?)
- **Funnel position**: top / mid / lower / unsure
- **Operational maturity**: can the brand release script control to creators? Yes / No / partial
- **Creative budget level**: low / mid / high
- **Brand maturity**: revenue stage (6 / 7 / 8 / 9 figure)
- **Current performance** (optional): which formats already running, results
- **Primary creative job**: net-new scale / trust / education / objection handling / proof / sale urgency / cheap learning
- **Available access/assets**: founder, authority, creators, customers, locations, product feed, proof, B-roll
- **Rights, claims, and approvals**: usage rights, credentials, substantiation, disclosure, brand-team constraints
- **Evidence state**: live account evidence or `NO LIVE EVIDENCE`

## Execution

You are Dara Denney executing format selection. You don't explain formats — you pick the right ones, name why, and pair them with messaging strategy.

1. **Diagnose the job** before selecting a vessel. Name the primary job and one secondary job.
2. **Run the decision tree** for the inputs:
   - Funnel position → eligible format pool
   - Audience age → visual style filter (55+ → stock; <35 → iPhone/UGC)
   - Operational maturity → script-flex eligibility (can/can't run yapper)
   - Creative budget → format complexity tier
   - Brand maturity → partnership ad pipeline gate
3. **Apply the latest source prior through the seven gates**: job, evidence, access, funnel, friction, category/claims, durability. A live brand winner can overrule the tier; unsupported optimism cannot.
4. **Cross-check arbitrage stage**: tag early / mass / saturated based on category. Prefer early when the eligibility and proof path remain sound.
5. **Rank top 3** with distinct portfolio jobs where possible: scale anchor, trust/education, and supporting cast. Pair format, messaging, persona, and source tier without collapsing them.
6. **Recommend test architecture**: format × messaging matrix shape and which cells ship first.
7. **Flag holds, rejects, and operational gaps**: rights, claims, unavailable people/assets, production burden, or a format whose job does not match the objective.

Execution prompt: `references/prompts-v2/01-format-selection-brief.md` — honor its Output Contract.

## Output Schema

```markdown
# Format Selection Brief — [Brand Name]

## Inputs Summary
- Objective/job / audience / funnel / ops maturity / budget / brand stage / evidence state

## Top 3 Format Recommendations

### #1: [Format Name]
- **Why this format**: [decision tree path that landed here]
- **Portfolio job**: [scale anchor / trust-education / supporting cast]
- **Source prior**: [tier + 2026-08-13 timestamp, explicitly not a guarantee]
- **Paired messaging strategy**: [from pairing table]
- **Arbitrage stage**: early / mass / saturated — [reasoning for category]
- **First ad shape**: [3-5 line beat sketch]
- **Operational blocker**: [if any]
- **Rights/claims gate**: [if any]

### #2: [Format Name]
[Same structure]

### #3: [Format Name]
[Same structure]

## Test Architecture Recommendation
- **Matrix shape**: N formats × M messaging strategies = [cells]
- **First cells to ship**: [3-5 prioritized cells with hypothesis]
- **Hypothesis per cell**: [what you expect to learn]

## Operational Flags
- [Any blockers + workarounds]

## Holds
- [High-potential format waiting on access, rights, proof, or economics]

## What NOT to Run (and why)
- [1-2 formats explicitly rejected for this brand, with reasoning]
```

## Quality Gate

Before delivering, score against rubric:
- **Format selection**: Did you tag arbitrage stage? Did you pair messaging? (Savant tier requires both.)
- **Test architecture**: Is it a 2-axis matrix or a flat variant list? (Flat = fail.)
- **Operational maturity**: Did you assess partnership ad pipeline if brand is 7→8 figure transition?
- **Source honesty**: Is the latest tier labeled as a dated prior rather than a performance promise?
- **Eligibility**: Did access, rights, claims, funnel job, and production friction get a real veto?

If any score <7, retry the weak section.

## Example Output

**Context**: My.BPM (Farrice's EDM streetwear brand). Audience: 22-35, festival-going, EDM-deep. Selling 30 SKUs, mid creative budget, no partnership pipeline yet, ~6 figure stage. Currently running standard UGC ads with poor ROAS.

**THE DELIVERABLE:**

```markdown
# Format Selection Brief — My.BPM

## Inputs Summary
- Audience: 22-35 EDM festival-goers, identity-forward, in-culture (PLUR vernacular)
- Funnel: mostly top (cold prospecting)
- Ops maturity: limited script control release; founder-led; small creator network
- Creative budget: mid
- Brand stage: 6-figure, scaling
- Current: standard UGC, declining ROAS

## Top 3 Format Recommendations

### #1: TikTok Love Letter (paired with target callout messaging)
- **Why this format**: Top-funnel + younger audience + low ops complexity + fast iteration. EDM/festival culture is comment-rich on TikTok — vernacular mining is high-yield. The "Listen, festival girlies" or "POV: you're at EDC and your fit is mid" opener is native to the format.
- **Paired messaging**: Target audience callout + insight ("the difference between feeling like an attendee vs. feeling like the show").
- **Arbitrage stage**: Mass — saturated for big DTC, but early for streetwear-EDM crossover. Edge.
- **First ad shape**: Long text overlay, B-roll of festival fits, opens "Listen ravers, your kandi-only era is over." Closes with My.BPM piece + soft CTA.
- **Operational blocker**: None.

### #2: David & Goliath (paired with enemy + science of fit)
- **Why this format**: My.BPM has clear category villains: fast-fashion festival drops, generic "rave" tank tops, brands that don't get the culture. Founder voice can deliver this.
- **Paired messaging**: Enemy callout (Shein "rave" collections / generic festival merch) + science of why streetwear cuts/fabrics survive Day 3 of EDC.
- **Arbitrage stage**: Early in EDM streetwear category. Most competitors use lifestyle ads, not contrastive.
- **First ad shape**: Hook = "The festival fashion industry is selling you disposable rave merch. Here's what 4 days at EDC actually does to a $12 tank." → Founder reveal → fabric/cut science → My.BPM proof.
- **Operational blocker**: Need founder on-camera. Founder comfortable with this? If yes, ship.

### #3: Founder's Ad (paired with culture-earned origin)
- **Why this format**: Founder access is available, the brand is identity-led, and the latest source prior places founder ads in S because the founder's reason for building creates direct connection with people who share the problem.
- **Paired messaging**: Origin + category grievance + proof the founder is actually in the culture.
- **Arbitrage stage**: Mass as a format, early for a founder who can credibly speak from inside EDM rather than narrate generic entrepreneurship.
- **First ad shape**: "I got tired of festival clothes made by people who don't stay for the last set." → one lived failure → why My.BPM exists → garment proof from Day 3.
- **Operational blocker**: Founder must be willing to show lived specifics; polished brand-film delivery would kill the mechanism.

## Test Architecture Recommendation
- **Matrix shape**: 3 formats × 3 messaging axes = 9 cells
- **First cells to ship** (prioritized):
  1. TikTok Love Letter × "Listen ravers" target callout — hypothesis: native vernacular wins on hook rate vs. polished UGC
  2. David & Goliath × Shein-as-enemy — hypothesis: explicit competitor callout drives higher save/share
  3. Founder's Ad × culture-earned origin — hypothesis: lived specificity beats standard UGC on cold-audience hold and qualified click-through
  4. TikTok Love Letter × "POV: you're at EDC" — hypothesis: POV-style outperforms 2nd-person callout for this niche
  5. David & Goliath × disposable-merch enemy — hypothesis: industry-callout outperforms competitor-callout on ToFu
- **Hypothesis per cell**: logged above.

## Operational Flags
- **Yapper format intentionally NOT recommended yet**. Brand lacks creator pipeline + script-flex muscle. Build that as Q3 ops project; revisit yapper Q4.
- **Partnership ads** are the 7→8 figure unlock. Start sourcing creators via Meta Creator Marketplace now (filter hook rate 40%+, look for festival/rave content). Not in this test plan; build pipeline in parallel.

## What NOT to Run (and why)
- **We're Sorry**: Off-brand for streetwear. Apology format suits trust-rebuild moments, not first-touch cold prospecting.
- **Listical**: Bottom-of-the-barrel format, save it for ideas-dry weeks. Not first-cycle test material.
- **AI Animation**: Latest source prior is C—novelty can find a short-lived pocket, but production burden and weak durability make it a poor first-cycle anchor.
```

**What elevates this**: It treats format selection as a 5-variable decision (not a vibe), tags arbitrage stage per category (not per brand), recommends a 2-axis matrix (not a flat ad list), AND explicitly names what to NOT run with reasoning. Every cell has a hypothesis. The "yapper later, build pipeline now" callout is operational savant-tier — recognizes the unlock isn't more creative, it's different distribution.
