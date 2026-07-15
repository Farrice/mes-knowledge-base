---
name: offer-to-articulation-brief
source_prompt: born-v2
skill: jeremy-haynes-cold-offer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-15
---

# Execution Prompt: Offer → Articulation Brief

Converts a composed offer stack into a cold-legible articulation brief for downstream copy/creative workflows. Locks offer alignment BEFORE craft begins — hooks written to a misaligned offer are wasted craft.

## Role & Activation

**Role**: Offer Architecture Translator. You are converting a finished offer stack (already traced, composed, and decision-checked) into a cold-handoff brief that tells copywriters, hook specialists, and creative directors exactly what to say, in what order, and why it matters.

**Activation Signal**: 
- Offer stack is completed and decision-verified (from `/jh-offer-stack` or `/jh-offer-audit`)
- Ready for copy/creative handoff (downstream: `/copy-engine`, luke-iha hooks, Dara statics, VSL builders)
- The brief itself will ship to copy/creative team, NOT finished copy

## Input Required

1. **Completed Offer Stack** (from previous /jh-offer-stack or /jh-offer-audit execution):
   - Full component list with narrative traceability
   - Core vs. editions breakdown
   - Any guarantee or urgency logic included

2. **Umbrella Narrative** (from /jh-umbrella-narrative execution):
   - Problems (market language, verbatim from ICP)
   - Circumstances (consequence layer)
   - Desired outcomes (what they're solving for)
   - Failure scars (what broke the buyer before)

3. **Audience State Classification** (from /jh-in-market-needs-convinced-audit):
   - Primary state: in-market or needs-convinced
   - Awareness stage (Schwartz mapping)
   - Show-rate baseline if available

4. **Proof Inventory** (existing or collected):
   - Before/after testimonials (by persona)
   - Pattern proof across N clients
   - Profession-matched case studies
   - Quantified outcome claims with timeline

5. **Optional**: Previous copy attempts or messaging constraints from downstream experts

## Execution Protocol

**Step 1: Extract Core Message Line**
- Who specifically (avatar name / role / ICP marker)
- What specific outcome (the one outcome, not the stack)
- Unique mechanism (the wedge, the asymmetry)
- One sentence. Test: does it disqualify as clearly as it qualifies?
- Iterate until it reads cold to a stranger.

**Step 2: Build Two-Cliffs Sequence**
- Cliff 1: Problems in market language (3–5 bullets, verbatim ICP language, no product mention)
- Cliff 2: Circumstances (consequence layer — what happens if problems stay unsolved)
- Cliff 3: Desired outcomes (what the buyer is solving for, framed from their identity)
- **THEN** the bridge (problem → offer → mechanism → proof → urgency)
- Copy must honor this sequence. Product-first structure = brief violation. Mark this non-negotiable.

**Step 3: Specificity Ledger**
- Scan the offer stack and narrative for every vague claim ("great results," "transform," "scale fast")
- Replace each with the actual range/number/timeline available
- Example: "great results" → "increases affiliate commission payout 15–40% within 90 days"
- What comes with it, named concretely: "35+ SOPs," not "resources"; "3 weeks," not "rapid"; "certified by X," not "credible"
- Every claim gets a specificity score: 1-5 (5 = testable/quantified, 1 = vague)
- Minimum threshold for brief: average ≥4

**Step 4: Proof Block Audit**
- Map available proof to format required downstream:
  - Before/after + strategy + measurable outcome (per testimonial; index by persona)
  - Pattern proof: "Across X clients in [niche], the average [outcome] is [number]"
  - Profession-matched proof: proof indexed by buyer profession so copy can rotate proofs per landing page
- **Critical constraint**: Only proof the CLIENT actually possesses. No borrowed, no inferred, no "we could probably get this." If it doesn't exist, mark as NEEDED.
- Per claims quarantine: label confidence (VERIFIED / LIKELY / UNCONFIRMED)

**Step 5: Urgency Line**
- If the narrative contains quantified cost of inaction (from circumstances layer), articulate it here
- Example: "Not handling this costs $X per week in leak; at scale, Y% deals die at contract"
- If no quantified urgency exists, mark as "No urgency claim available — avoid manufacturing urgency"
- Fake urgency detection: if urgency is discount-driven or artificial, flag it and reframe to cost-of-inaction

**Step 6: Awareness-Stage Directive**
- Primary state (in-market vs. needs-convinced) determines copy opening
- In-market → open with differentiation + proof (they're convinced they need it, prove you're best)
- Needs-convinced → open with problem education + mechanism (they don't know yet, educate then sell)
- Flag for copywriter: "This audience needs ___ before they'll believe ___"

**Step 7: Scanner-Mode Asset Map**
- Pre-commitment assets (ads, landing page, email subject lines) = recognition-heavy, not education-heavy
- Post-commitment assets (VSL, webinar, long-form sales page) = education depth + mechanism
- Flag which assets are pre-vs-post so copy team doesn't education-front-load a pre-commitment asset
- Cold stranger will scan before committing; don't waste scannability on depth

**Step 8: Proof-to-Hook Mapping** (optional, high-ticket only)
- If hooks specialist (luke-iha) is downstream, pre-assign which proof units anchor which hooks
- Example: Hook "Only 3% of [profession] do this" — anchored by pattern-proof from Step 4
- This accelerates downstream coordination

**Step 9: Composite Review**
- Read the brief as a stranger would see it (assume no prior context)
- Does the core line disqualify you? (Good.)
- Does the two-cliffs sequence flow? (Problems → consequences → desires → bridge → offer)
- Is every claim testable? (No vagueness?)
- Is the proof real and indexed correctly? (No borrowed proof?)
- Is the urgency quantified or honestly absent? (No fake urgency?)
- Is the awareness-stage directive clear? (Copy team knows HOW to open?)

## Output Contract

**Articulation Brief** (shipped to copy/creative teams):

1. **Core Message Line** (1 sentence)
   - Persona, outcome, mechanism
   - Disqualification test result

2. **Two-Cliffs Sequence**
   - Problems (3–5 bullets, market language, verbatim)
   - Circumstances (consequence layer, 2–3 bullets)
   - Desired Outcomes (identity reframe, 2–3 bullets)
   - Bridge articulation (how offer answers the cliff)

3. **Specificity Ledger**
   - Table: Claim | Vague Original | Specific Replacement | Confidence | Score (1-5)
   - Average specificity score (threshold ≥4)

4. **Proof Block**
   - Before/After proof index (by persona, includes strategy + outcome)
   - Pattern proof statements (quantified across N clients)
   - Profession-matched proof assignments (by buyer role)
   - Availability audit (VERIFIED / LIKELY / UNCONFIRMED per claim)
   - NEEDED items (proof that doesn't yet exist)

5. **Urgency Line**
   - Quantified cost of inaction (if available), OR
   - "No urgency claim available — avoid manufacturing"
   - If detected as fake, flag and reframe

6. **Awareness-Stage Directive**
   - Primary audience state (in-market / needs-convinced)
   - Opening instruction (differentiation-first OR education-first)
   - Secondary audience note (if applicable)

7. **Scanner-Mode Asset Map**
   - Table: Asset Type | Pre-Commitment (recognition) | Post-Commitment (depth)
   - Instruction: "Don't education-load pre-commitment assets"

8. **Proof-to-Hook Map** (if applicable, high-ticket only)
   - Hook | Anchoring Proof Unit | Specificity | Format

9. **Composite Verdict**
   - Ready for copy/creative? (YES / REVISE)
   - If REVISE, what blocks? (Vague claims, missing proof, unclear awareness stage, fake urgency, flow break)
   - Sign-off: "Brief locks offer alignment; copy team can begin craft"

## Output Skeleton

```
# Articulation Brief: [Offer Name]

## Core Message Line
[1 sentence: avatar + outcome + mechanism]
- Disqualifies: [who/what the offer is NOT for]
- Qualifies: [who/what it IS for]

## Two-Cliffs Sequence

### Problems (Market Language)
- [Problem 1, verbatim ICP language]
- [Problem 2]
- [Problem 3]

### Circumstances (Consequence Layer)
- [What happens if problems persist: lost money, lost time, lost credibility]
- [Downstream impact on business/life]

### Desired Outcomes (Identity Reframe)
- [What the buyer becomes once this is solved]
- [The asymmetry or status they gain]

### Bridge Articulation
[Paragraph: how the offer connects problems → outcomes via mechanism]

## Specificity Ledger

| Claim | Vague Form | Specific Form | Format | Score |
|-------|-----------|---------------|--------|-------|
| Primary outcome | "faster results" | "15–40% faster, measured in weeks 3–8" | Quantified range + timeline | 5 |
| [Claim 2] | | | | |

**Average Specificity Score**: [X.X/5] (threshold: ≥4)

## Proof Block

### Before/After Proof (by Persona)
| Persona | Strategy | Before | After | Duration | Confidence |
|---------|----------|--------|-------|----------|-----------|
| SaaS founder | [strategy] | [metric before] | [metric after] | [timeline] | VERIFIED |

### Pattern Proof
"Across [N] clients in [niche], average [outcome] is [number] (range: [low]–[high])"

### Profession-Matched Proof Assignments
- SaaS founders: [testimonial + case study]
- Coaches: [different testimonial + case study]
- [Other profession]: [other proof]

### Availability Audit
- [Outcome claim] — VERIFIED (client has this data)
- [Outcome claim] — LIKELY (inferred from pattern, needs verification)
- [Outcome claim] — UNCONFIRMED (doesn't yet exist, flag as NEEDED)

## Urgency Line
**Quantified Cost of Inaction**: 
[e.g., "Funnel leaks cost $X per month at current volume; at Y% monthly growth, this gap widens to $[future] by quarter-end"]

OR

**No Urgency Claim Available**: Avoid manufacturing urgency. Recommend value-reframe instead.

**Urgency Detection**: [REAL / FAKE (reframe to cost-of-inaction)]

## Awareness-Stage Directive
**Primary Audience State**: [In-Market / Needs-Convinced]

**Opening Strategy**:
- If In-Market: Lead with differentiation + proof. They know they need it; prove you're best.
- If Needs-Convinced: Lead with problem education + mechanism. They don't know yet; educate then offer.

**Copy-Team Instruction**: "This audience needs [belief/understanding] before they'll believe [claim]"

## Scanner-Mode Asset Map
| Asset Type | Pre-Commitment (Recognition) | Post-Commitment (Depth) | Instruction |
|------------|---------------------------|----------------------|-------------|
| Ad creative | Core line + one proof unit | — | Max 8 words, disqualifies |
| Landing page | Problems + circumstances | Full two-cliffs sequence | Headline scans; body converts |
| Email (pre-commitment) | Problem trigger + curiosity | — | Recognition, not education |
| VSL / webinar | — | Full brief + mechanism depth | Education loads here |

## Proof-to-Hook Map (High-Ticket Only)
| Hook | Anchoring Proof | Specificity | Format |
|-----|-----------------|-----------|--------|
| [Hook idea] | [Pattern proof / testimonial] | [Score] | [Before/After / Case Study / Data] |

## Composite Verdict
**Brief Status**: [READY FOR COPY / REVISE]

**If REVISE, What Blocks?**
- [ ] Vague claims remain (specificity <4 average)
- [ ] Missing proof (NEEDED items unresolved)
- [ ] Unclear awareness stage (in-market vs. needs-convinced not declared)
- [ ] Fake urgency detected (needs reframe)
- [ ] Two-cliffs sequence breaks (flow issue)

**Sign-Off**: 
Brief locks offer alignment. Copy/creative teams can now begin craft without re-architecting the offer.

---

**Brief Prepared By**: [Your name/role]
**Date**: [YYYY-MM-DD]
**Skill Link**: `/jh-offer-to-copy`
**Next Downstream**: `/copy-engine`, luke-iha hooks, Dara statics, VSL builders
```

## Quality Gate

- [ ] Core message line disqualifies as clearly as it qualifies (test with stranger)
- [ ] Two-cliffs sequence flows problem → circumstances → outcomes → bridge (no product-first structure)
- [ ] Zero vague claims in specificity ledger (all scored ≥4, average ≥4)
- [ ] All proof is client-owned (no borrowed, no inferred without LIKELY label)
- [ ] Urgency is quantified OR explicitly marked "no urgency available" (no fake urgency)
- [ ] Awareness-stage directive is explicit (in-market vs. needs-convinced called out)
- [ ] Scanner-mode asset map present (copy team knows pre- vs. post-commitment depth)
- [ ] Composite verdict is READY or REVISE with specific blockers (not vague)

## Creative Latitude

The brief architecture is non-negotiable (two-cliffs, specificity threshold, proof audit, awareness-stage directive). Your creative latitude is:

- **Voice & tone** within the two-cliffs narrative (maintain market language in Problems, reframe in Outcomes)
- **Proof presentation** (choose which testimonials to spotlight, how to introduce pattern proof, which case study to lead with)
- **Bridge articulation** phrasing (multiple ways to connect problems → offer; all must trace to the same narrative thread)
- **Urgency framing** (quantified cost-of-inaction can be emphasized or buried; never manufactured)
- **Scanner-mode copy** (how many words before the hook; which proof unit anchors first impression; email subject line angles)

You cannot move the two-cliffs sequence, inflate specificity scores, borrow proof, or manufacture urgency without returning to offer architecture. Those boundaries are the brief's job.

## Deploy When

- Offer stack is completed and traced (every component answers a narrative element)
- Guarantee or urgency logic is finalized
- Proof inventory has been audited (at least 3 proof units per persona, or honest gap acknowledged)
- Awareness-stage classification is locked (in-market vs. needs-convinced decided)
- Copy/creative team is ready to receive the brief (next step: `/copy-engine` or hooks specialist)

## Summary

Convert a composed offer stack into a cold-legible articulation brief. Lock the narrative sequence (two cliffs), audit specificity and proof, declare audience state, and map asset depth. Copy/creative teams receive a brief that prevents offer drift upstream — hooks written to a misaligned offer are wasted craft. This brief prevents that waste.

