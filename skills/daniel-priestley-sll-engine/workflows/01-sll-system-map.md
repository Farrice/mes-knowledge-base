# Workflow: SLL System Map (the OS install)

**Produces**: the complete Short-Form/Long-Form/Lead-Form operating map for one business — topic-lane bank, long-form spine, offer shelf, cadence calendar, LAPS handoff. This is the one-time install every other SLL workflow runs against.

## Load Context

1. Read `../genius.md` (mandatory).
2. Load the ICP/avatar source if one exists (for Farrice: `_active/linkedin/01-research/deep-icp-profile-invisible-expert.md`; for clients: their avatar doc). Lane language must come from the buyer's own words — never invent a customer.

## Steps

1. **Name the buyer connection.** One sentence: who should the recommendation engine hand this content to, and what do they want to buy? (Unit of strategy = the connection, not the platform.)
2. **Build the lane bank** — minimum 5 entries per lane, in the customer's language:
   - PAIN: life right now without the product (Priestley's spin test: one business → 4+ distinct pains).
   - PRIZE: the celebration on the other side.
   - PROBLEM: what has stopped them (obstacle ≠ pain).
   - NEWS hooks: currently trending stories that can multiply any lane (`pain × news`, `prize × news`, `problem × news`).
3. **Draft the long-form spine**: 3 proof stories (real, verifiable — claims quarantine applies), the 3-5 principles behind each, the process the business takes clients through. Mark the ONE awareness gap each future explainer will close.
4. **Stock the offer shelf**: at least one Special Offer, one Product for Prospects (easy first step: workshop / assessment / waitlist / group), one Promotion candidate with an end date. Assign quarters.
5. **Write the cadence contract**: short daily (which lanes on which days), long monthly (next 3 explainer topics), offer quarterly (refresh dates). Name the bridge mechanic per platform (comment-a-word vs pinned long-form).
6. **LAPS handoff**: who/what receives a form fill within 24h (Leads → Appointments → Presentations → Sales).

Output step — Execution prompt: `references/prompts-v2/sll-system-map.md` — honor its Output Contract.

## Output Schema

```
# SLL System Map — [Business]
Buyer connection: [one sentence]
## Lane Bank        (PAIN ×5+ · PRIZE ×5+ · PROBLEM ×5+ · NEWS hooks ×3+)
## Long-Form Spine  (proof stories ×3 · principles per story · process · gap register)
## Offer Shelf      (Special Offer · P4P · Promotion+end date · quarter assignments)
## Cadence Contract (daily lanes · monthly explainer queue · quarterly refresh dates · bridge mechanic)
## LAPS Handoff     (form fill → next action, owner, SLA)
```

## Example Output (abridged)

Scenario: strength & conditioning coach for busy professionals.

> **Buyer connection**: hand this to the 35-50 professional who's watched their strength, energy, and waistline slide for 5 years and wants a system that survives a real calendar.
> **PAIN (excerpt)**: "You're strong at work and weak everywhere else." · "Third January in a row buying the same gym membership." **PROBLEM (excerpt)**: "Every program you've tried assumed you have 90 free minutes a day." (obstacle, not symptom)
> **Proof story #1**: client X, 44, deadlifted 2× bodyweight after 14 months training 3×45min/week → principles: minimum effective dose, progression tracking, protein floor → process: 12-week coaching blocks with weekly check-ins.
> **Offer shelf Q3**: P4P = free "Executive Strength Score" assessment; Promotion = September cohort, doors close 09/05.

**What makes this excellent**: every lane line is in the buyer's own voice (targetable by the engine), the problem lane names obstacles rather than repeating pains, and the proof story is specific enough to be checkable — no "helped hundreds of clients" fog.

## Quality Gate

- [ ] Lane entries pass the stranger test: a cold reader could name who it's for
- [ ] Problem lane ≠ pain lane (obstacles, not symptoms)
- [ ] Proof stories are real and specific (claims quarantine honored)
- [ ] All three cadences have dates, not intentions
- [ ] Form fill has a named owner and SLA
