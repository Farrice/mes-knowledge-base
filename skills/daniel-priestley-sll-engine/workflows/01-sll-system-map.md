# Workflow: SLL System Map (the OS install)

**Produces**: the complete Short-Form/Long-Form/Lead-Form operating map for one business — topic-lane bank, long-form spine, offer shelf, cadence calendar, LAPS handoff. This is the one-time install every other SLL workflow runs against.

## Load Context

1. Read `../genius.md` (mandatory).
2. Load the buyer, audience, customer, donor, applicant, or stakeholder source if one exists (for Farrice: `_active/linkedin/01-research/deep-icp-profile-invisible-expert.md`; for clients: interviews, reviews, support logs, sales notes, or an avatar doc). Lane language must come from their own words—never invent a person or demand signal.

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

Scenario: workflow-automation consultancy for operations leaders.

> **Buyer connection**: hand this to the operations leader whose team still copies customer data between five tools and wants one reliable workflow without buying a giant transformation program.
> **PAIN (excerpt)**: "Friday reconciliation starts on Wednesday." · "The spreadsheet only works when Maya is online." **PROBLEM (excerpt)**: "Every automation proposal begins with replacing the stack instead of fixing the handoff." (obstacle, not symptom)
> **Proof story #1**: client X reduced one approved intake workflow from 46 manual steps to 12, with a human review before every external action → principles: diagnose one workflow, preserve review boundaries, instrument exceptions → process: map, prototype, acceptance-test, hand off.
> **Offer shelf Q3**: P4P = free "Workflow Friction Score" assessment; Promotion = September implementation cohort, applications close 09/05.

**What makes this excellent**: every lane line is in the buyer's own voice (targetable by the engine), the problem lane names obstacles rather than repeating pains, and the proof story is specific enough to be checkable — no "helped hundreds of clients" fog.

## Quality Gate

- [ ] Lane entries pass the stranger test: a cold reader could name who it's for
- [ ] Problem lane ≠ pain lane (obstacles, not symptoms)
- [ ] Proof stories are real and specific (claims quarantine honored)
- [ ] All three cadences have dates, not intentions
- [ ] Form fill has a named owner and SLA
