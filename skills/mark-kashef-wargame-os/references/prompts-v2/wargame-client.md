---
name: "Mark Kashef — Client Wargame Bank"
source_prompt: born-v2
skill: mark-kashef-wargame-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are banking the judgment for a SOLD, REPEATABLE client deliverable once, at frontier tier, so every future instance executes at cheap tier — the economics that make sold work margin-positive: "make the smartest model you'll ever rent do the thinking while it's still on salary. You pay for the genius once. You keep it forever." Unlike a one-off mission wargame that gets spent once and archived, a client wargame is an asset the relationship keeps earning against — it lives inside the client's own project directory, not a transient mission folder, because it survives across every future engagement with that client.

## Input Required

- `[CLIENT DELIVERABLE]` — the exact repeatable unit, named precisely (e.g. "one listing's content sheet," never "all of Jen's marketing")
- `[CLIENT CLAUDE.MD]` — the client's full context file: voice rules, format contracts, prior precedent
- `[REPEATABILITY CONFIRMATION]` — will this exact deliverable run again with new inputs? A one-off client ask doesn't earn this investment
- `[SOLD-WORK CONFIRMATION]` — is the client relationship active and this deliverable already committed, not speculative positioning work?
- `[FORMAT CONTRACT]` — the deliverable's physical shape (cards vs. prose, sheet vs. doc); if the client's CLAUDE.md has voice rules but no explicit format contract, that gap gets ratified in the client's CLAUDE.md FIRST, never guessed into the wargame

## Execution Protocol

**Pre-Flight:**
- Repeatability check: will this exact deliverable run again with new inputs (a new listing, a new event, a new drop)? If not, use the normal expert workflow instead — this investment is only justified by recurrence.
- Sold-work check: is the client relationship active and this deliverable already committed? Strategy-shaped or repositioning work surfaces before anything else runs; this is for production routes on work already sold.
- Client-context check: does the client already have a CLAUDE.md? If not, THAT is the recon this workflow reads first — never freeze a production route without the client's actual constraints loaded.

**The bank-once-spend-repeatedly shape:** the same conductor pattern as the mission pre-flight offer (compose Tier 1, don't duplicate it), applied to a different trigger — instead of a mission's riskiest workstream, the unit is a CLIENT DELIVERABLE that recurs. The frontier-tier pass happens exactly once per deliverable type; every subsequent instance runs at whatever tier the client relationship can sustain economically. If a deliverable's wargame needs re-running every time a new instance comes in, it was never actually banked — that's a sign the mission brief step didn't freeze enough.

**Steps:**
1. Pick the exact repeatable unit — name it precisely, scoped to a single instance's production route, replayed across many future instances.
2. Load the client's CLAUDE.md in full. Every voice rule and format contract becomes a FROZEN CHOICE in the mission brief — freeze it now so no future instance re-litigates tone or structure.
3. Write the mission brief per the brief-writing discipline, with the client's format contract as the physical constraint — a hard rule, not a style preference.
4. Run the order → run → grade sequence at frontier tier, highest effort. This is the one expensive pass the economics describe — "pay for the genius once."
5. Grade to DONE before storing anything. A client route that hasn't survived a red-team pass isn't bankable — it's a draft that happens to have the client's name on it.
6. Store the DONE wargame under the client project, not a transient mission folder — e.g. `<client-project>/wargames/<deliverable-slug>.md`. Client-owned artifacts live with client context, since they outlive any single mission session.
7. Each new instance runs the execution step with the stored wargame as its route plus that instance's specific inputs, at cheap tier, since the judgment is already banked.
8. Re-run from step 2 if the format contract changes — a wargame's frozen choices are only valid as long as they match the client's actual current constraints; client feedback that shifts voice or format invalidates the old freeze.

**When the client has no format contract yet:** if the brief-writing pass finds voice rules but no explicit format contract, that gap gets written into the client's CLAUDE.md as a decision FIRST, not guessed into the wargame. A format contract invented inside a wargame instead of ratified in the client's own context file will drift the next time someone edits that CLAUDE.md without knowing the wargame depends on it.

**Frozen-choice source and storage location by deliverable type:**
- Listing/production content: client CLAUDE.md + production-sheet format contract → `<client-project>/wargames/`
- Event/ops route: client CLAUDE.md + venue/platform constraints → `<client-project>/wargames/`
- Launch/drop content: brand voice doc + launch-week format → `<client-project>/wargames/`
- Any new repeatable engagement: that client's CLAUDE.md, once one exists → `<client-project>/wargames/`, created on first use

## Output Contract

A DONE-graded wargame at `<client-project>/wargames/<deliverable-slug>.md`, plus a one-line economics note appended to the client project's own context file confirming what's now bankable at cheap-tier execution versus what still requires a frontier-tier human decision.

## Output Skeleton

```
# Client Wargame — [client] — [deliverable-slug]
Repeatable unit: [the exact single-instance production route this banks]
Frozen from: [client]/CLAUDE.md, read [date]

## Frozen Choices (from client context)
- Voice: [frozen]
- Format contract: [frozen]
- [additional client-specific frozen choices]

## Mission Spec / RECON NEEDED / Moves / Abort Conditions / Verification Runs
[full Document Schema, per the wargame-run protocol, scoped to this one
repeatable route]

## Grade
[8-point PASS/FAIL, red-team attack + patch, VERDICT: DONE]

## Economics Note (appended to client CLAUDE.md / context file)
This route is now cheap-tier-executable per new instance: [what's banked].
Still requires a frontier-tier pass if: [format contract changes / voice
rules change / anything else that invalidates the freeze].
```

## Quality Gate

- [ ] Never wargames a one-off — the repeatability check is the hard gate, checked again before storing
- [ ] Client CLAUDE.md loaded and read in full before any freeze decision — a frozen choice made without reading the client's actual voice rules is a guess wearing a wargame's costume
- [ ] DONE bar is identical to Tier 1's — all 8 points plus a recorded red-team survival; client work gets no rigor discount for being "just production"
- [ ] Stored under the client project, not a transient mission folder
- [ ] The economics note names, in plain terms, what's now cheap-tier-executable versus what still needs a frontier-tier human decision

## Deploy When

A sold, repeatable client deliverable (a per-listing production sheet, an event-ops route, a launch/drop content route) needs its production route wargamed ONCE at frontier tier so every future instance executes at cheap tier. Never for a one-off client ask.
