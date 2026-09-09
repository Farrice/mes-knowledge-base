# Angle Map Brief Repair Plan

## Verdict

Rebuild the recurring deliverable as a creative director's decision brief.
Keep the full research, content assets, evidence, and run logs, but move them
out of the primary reading path.

The brief should take three to five minutes. A reader should leave knowing what
changed in the market, why it matters, which content territory to pursue, and
what to make next.

This is a plan. The live automation has not been changed.

## Why the current brief failed

The 2026-08-28 brief is 5,601 words with 11 numbered sections and 27 subheads.
It combines four products: executive market read, creative direction, content
pack, and operational record.

That design buries the decision. The thesis repeats across several sections.
Research counts and gate results arrive before they help the reader. A fixed
quota of hooks, scripts, slides, prompts, and receipts rewards completion more
than judgment. The handoff to a writer, designer, or AI remains scattered
across the document.

The root problem is the output contract. Sentence-level editing will not fix
an automation that asks one file to be the brief, archive, factory, and audit
log.

## Replacement architecture

One research run should produce four connected artifacts inside the existing
Angle Map system.

1. **Director Brief:** Farrice or a creative lead gets the market decision in
   900 to 1,200 words.
2. **Production Pack:** the writer, designer, editor, or AI gets only the
   selected formats and execution instructions.
3. **Evidence Pack:** a reviewer gets complete sources, quotes, grades, and
   claim boundaries without a word limit.
4. **System Receipt:** the automation preserves gates, ledgers, deltas, and run
   state in a machine-first record.

The Director Brief links to the other artifacts without reproducing them.
Friday's full synthesis stays in `weekly/`; the daily brief carries its
conclusion and link.

## New Director Brief contract

1. **The answer, 150 words:** market move, consequence, chosen territory, and
   next action.
2. **Market read, 250 words:** up to three blocks using Signal → Meaning → Use.
3. **Creative direction, 350 words:** audience, occasion, tension, insight,
   lead angle, proof, counterpoint, visual world, and guardrails.
4. **Production handoff, 350 words:** objective, audience, desired response,
   required material, first deliverable, quality bar, and failure boundaries.
5. **Action board, 100 words:** create now, watch next, ignore for now, and
   companion links.

The opening passes only when Farrice can stop after 150 words and explain the
finding to someone else.

## Decision-density rules

A paragraph stays only when it reveals a market change, explains a consequence,
makes a creative decision, or enables execution.

1. State the lead thesis once. Later sections develop it.
2. Show the winner, why it won, and no more than two real alternatives.
3. Move route notes, context loads, gate results, and mutations to the System
   Receipt.
4. Move complete source tables and claim grading to the Evidence Pack.
5. Store finished copy in the Production Pack. Link to it from the brief.
6. Produce one flagship format by default. Add a second only when it serves a
   distinct job.
7. Keep proof labels visible when they change what may be said or done. Hide
   proof administration that does not affect the decision.
8. Exclude numbers that do not alter priority, risk, or action.

## Top three highest-return moves

### 1. Separate the reader surface from the evidence system

The source receipts, weekly file, content vault, ledgers, and six-line execution
cut already exist. The daily brief should stop duplicating them.

**Result:** faster comprehension without deleting research.

### 2. Replace section compliance with a handoff test

Judge the brief by whether another human or AI can create the right asset from
the handoff alone. A complete section list is not evidence of usable direction.

**Result:** fewer examples, stronger choices, and one production priority.

### 3. Shadow-test before promotion

For three research runs, use one evidence set to render both formats. Compare
comprehension, usefulness, handoff quality, and information loss. Do not repeat
the research.

**Result:** proof that compression improves the work rather than merely cutting
words.

## Implementation brief

### Phase 1: Preserve the working parts

Keep the 2026-08-28 brief as the negative fixture. Preserve source receipts,
append-only ledgers, vault assets, offer canon, claim boundaries, and no-contact
rules. This repair changes presentation and ownership, not source truth.

### Phase 2: Repair the recurring prompt

Edit
`_active/knowledge/health-performance-ip-library/AUTOMATION_PROMPT.md`.
Replace the reader-facing 0-to-11 structure with the four-artifact contract.
Make the Director Brief primary. Move current Sections 5, 6, 9, and 11 to their
existing owners. Keep Friday synthesis separate. Change the content factory
from every format every day to one flagship plus a justified second format.

### Phase 3: Extend the existing verifier

Extend `execution/verify_health_performance_geo_prompt.py`; do not create a new
command. Check the word budget, answer-first opening, one lead decision,
complete handoff, companion links, separate Friday synthesis, and intact proof
boundaries.

Add four fixtures to the verifier's existing fixture area: the current
over-complete brief, a compliant daily brief, a compliant Friday brief, and a
sabotage set. Sabotage cases must reject hidden process logs, repeated theses,
fake compression that deletes proof, and forced format volume.

### Phase 4: Run the shadow comparison

Use the same research state for both versions across three runs. Record how
quickly Farrice identifies the market change, whether the recommendation is
clear from the opening, whether a collaborator can begin from the handoff, and
which decision-changing facts disappear.

Promote the new format only after Farrice can finish it without cognitive drag
and the handoff produces one strong asset without reopening the research.

## Acceptance test

1. Farrice can explain the market change after the first 150 words.
2. One content territory is clearly recommended.
3. Each signal includes its meaning and use.
4. Another human or AI can begin from the handoff alone.
5. Proof remains inspectable without dominating the reading experience.
6. The Director Brief contains no more than 1,200 words.
7. Repeated thesis language, process theater, and forced format volume are gone.
8. Uncertainty, claim risk, and commercial proof state remain honest.

## Existing capabilities to compound

1. **Clear Depth** shapes the opening around answer, consequence, and action.
2. **`LATEST-EXEC-CUT.md`** demonstrates compression without becoming another
   duplicated section.
3. **Source receipts** become the Evidence Pack.
4. **Content vault** owns finished assets instead of repeating them in the
   brief.
5. **Weekly synthesis file** owns Friday depth while the daily brief carries
   the conclusion.

The compound play is simple: execution cut for orientation, Director Brief for
judgment, Production Pack for making, and Evidence Pack for inspection.

## Locked, parked, next

- **LOCKED:** source rigor, claim boundaries, Angle Map canon, ledgers, and
  no-contact rules.
- **PARKED:** a new command, another research system, more agents, or live
  automation changes in this planning turn.
- **NEXT:** patch the existing prompt and verifier, then run the three-cycle
  shadow comparison.
