---
name: "offer-adoption-and-proof-loop"
produces: "Internal conditional-module adoption and proof return with only the source mechanics supported by the named trigger"
expert: "Jason Fladlien"
load_context: "references/offer-terms.md"
menu_exempt: "internal-component-invoked-by-fladlien-terms"
source_id: "JF-TERMS-2026-08-02"
---

# Jason Fladlien — Offer Adoption and Proof Loop

## Internal Role

This is a bounded internal specialist invoked by `offer-terms-diagnostic-and-rebuild`. It is not a second public front door and must not run by default.

Its job is to connect the offer’s promise to actual use without inventing a bundle. Three-win design, routine fit, a respectful re-entry path, visible progress, and proof permission are independent submodules. Activate only what the named trigger and evidence support.

## Trigger Required

Run only when the TERMS packet names at least one:

- Delayed or unclear first tangible win.
- Recurring behavior required for success.
- Known or credible non-use, drop-off, retention, or re-entry risk.
- Social connection required for the outcome.
- Real progress expected but capture, consent, or reuse is undefined.

If no trigger is present, return `NOT TRIGGERED` and stop. A trigger for one submodule does not activate the others.

## Inputs Required

- Accepted primary burden and selected TERMS changes.
- Purchased outcome and honest time horizon.
- Current path from decision or payment to first value.
- Essential buyer actions and any recurring behavior.
- Known drop-off evidence; hypotheses must remain labeled.
- Delivery capabilities, channel limits, privacy rules, and preservation locks.
- Existing proof objects and consent status.
- Remaining change budget from the public TERMS run.

## Execution Protocol

### 0. Module Activation Matrix

Map each trigger to a module before designing anything:

| Module | Activate only when |
|---|---|
| Three-Win Ladder | The initial decision win, first tangible win, or ideal-win boundary is unclear. |
| Routine Hinge | A recurring behavior is required and evidence supports a habit, cue, chunk, or context problem. |
| Positive-Intent Check-In | Observed or credible drop-off, re-entry risk, or necessary social connection exists. |
| Visible Progress | A meaningful earned progress event exists or is expected and visibility helps the purchased outcome. |
| Permission Chain | Capture, sharing, or reuse of a real progress or outcome object is proposed or already occurs. |

For every inactive module, return `NOT APPLICABLE — no evidence`. Never create a habit because permission is unclear, a check-in because the first win is slow, or a proof object because recurring use exists.

### 1. Three-Win Ladder (Conditional)

Define:

- **Initial decision win:** an immediate, truthful improvement in clarity, relief, access, or direction.
- **First tangible win:** the earliest progress observable during or after use. Attribution remains unproven unless separate evidence establishes it.
- **Ideal win:** the credible purchased outcome with conditions and timing.

For each, name the event, evidence object, timing, owner, and what it does **not** prove.

If this module is inactive, return `NOT APPLICABLE — no evidence`.

### 2. One Habit, Cue, and Context (Conditional)

Preserve existing good routines. Require at most one pivotal new habit. Attach it to an existing cue, define the smallest first chunk, and change the context before adding instruction.

Do not remove essential clinical, legal, safety, quality, or evidentiary work.

If recurring behavior or routine friction is not supported, return `NOT APPLICABLE — no evidence`.

### 3. Positive-Intent Check-In (Conditional)

Write one check-in that:

- Leads with care or useful observation.
- Makes help or a smaller re-entry path explicit.
- Allows a clean pause or exit.
- Never asks why the buyer failed to use what they paid for.
- Never uses guilt, sunk cost, forced community, or manufactured urgency.

If no drop-off, re-entry, or necessary social trigger is supported, return `NOT APPLICABLE — no evidence`.

### 4. Visible Progress and Legitimate Status (Conditional)

Design one visible progress state that is meaningful to the buyer’s result. It may be a completed decision, artifact, milestone, streak, acknowledgement, or dashboard state. It must be earned, accurately named, and optional to share.

Reject fake badges, meaningless gamification, public leaderboards that distort the outcome, and superiority claims.

If no meaningful earned progress event is supported, return `NOT APPLICABLE — no evidence`.

### 5. Proof and Permission Chain (Conditional)

Keep these separate:

`usage -> observed outcome -> voluntary sharing -> named permission -> external reuse`

For a proposed proof object, define:

- What event it actually shows.
- Attribution and confounders.
- Whether personally sensitive or client-confidential information appears.
- Redaction required.
- Who may see it, where it may appear, for how long, and whether identity is shown.
- Revocation or expiry path.

No permission means no external reuse. Internal process evidence is not demand, conversion, revenue, or outcome proof.

If nobody proposes capture, sharing, or reuse, return `NOT APPLICABLE — no evidence`.

### 6. Handoff Back to the Owner

Return only the minimum adoption changes needed for the selected burden. Give every proposed module-level offer change a change ID and count it against the remaining public change budget. The Revenue Offer Agent accepts, modifies, rejects, or holds each one and runs cross-term non-regression.

## Output Contract

## Output Schema

```markdown
# Adoption and Proof Loop — [Offer]

## Trigger
- Triggered by:
- Evidence state:
- Scope boundary:

## Module Activation Matrix
| Module | ACTIVE / NOT APPLICABLE | Evidence | Change-budget effect |

## Three-Win Ladder
| Win | Event | Timing | Evidence object | Owner | Does not prove |

## Routine Hinge
- Existing behavior preserved:
- One pivotal habit:
- Cue:
- Minimum first chunk:
- Context change:
- Essential work protected:

## Positive-Intent Check-In
- Trigger:
- Exact message:
- Help path:
- Re-entry or exit path:

## Visible Progress
- State or milestone:
- Why it matters:
- Capture moment:
- Optional sharing path:

## Permission Chain
| Event | Current state | Evidence | Permission scope | Next gate |

## Owner Handoff
| Change ID | Proposed change | TERMS lever | Burden reduced | New burden risk | Acceptance test | Remaining budget |

## Proof Boundary
[What the loop can and cannot establish]
```

## Quality Gate

- [ ] A named TERMS trigger exists; otherwise the component stopped.
- [ ] Each submodule has its own activation verdict; one trigger did not force the full bundle.
- [ ] When active, initial, first tangible, and ideal wins are distinct and observable.
- [ ] When active, at most one pivotal new habit is required.
- [ ] When active, a cue, minimum chunk, and context change are concrete.
- [ ] When active, the check-in communicates positive intent and allows a non-coercive exit.
- [ ] When active, visible progress is meaningful, earned, and optional to share.
- [ ] When active, usage, outcome, sharing, permission, and reuse remain separate events.
- [ ] When active, permission names use, audience, duration, identification, redaction, and revocation or explicitly remains absent.
- [ ] No fake status, guilt, compelled consumption, fabricated testimonial, or automatic screenshot reuse appears.
- [ ] The output says what each proof object does not prove.
- [ ] No more than the minimum changes needed for the selected burden are returned.
- [ ] Every proposed module-level offer change fits inside the public workflow’s remaining three-change budget.
