---
description: Fire for a SOLD, REPEATABLE client deliverable (Jen's per-listing production sheet, an Andrea/Resonance event-ops route, a MyBPM drop) that needs its production route wargamed ONCE at frontier tier so every future instance executes at cheap tier. Never fires for a one-off client ask — that's a normal expert workflow, not this.
---

# /wargame-client — Bank The Judgment Once, Spend It Repeatedly

The economics that make sold work margin-positive: "Make the smartest model you'll ever rent do the thinking while it's still on salary. You pay for the genius once. You keep it forever." A conductor — it composes Tier 1 wargaming against exactly one repeatable client route, then hands every future instance to `/wargame-execute` at cheap tier.

## Why Client Work Gets Its Own Tier 3 Workflow

`/wargame-mission` decides WHETHER to wargame inside someone else's mission. This workflow assumes the answer is already yes and is entirely about WHERE the resulting judgment lives afterward: not in a transient `.agent/missions/` folder that gets archived at session end, but inside the client's own project directory, where it survives across every future engagement with that client. The distinction matters economically — a mission wargame is spent once; a client wargame is an asset the relationship keeps earning against.

## Pre-Flight Gate

- **Repeatability check**: will this exact deliverable run again with new inputs (a new listing, a new event, a new drop)? A one-off client ask doesn't earn the frontier-tier investment — use the normal expert workflow for it instead.
- **Sold-work check**: is the client relationship active and this deliverable already committed, not speculative positioning work? Per the Path Decision binding, strategy-shaped or repositioning work surfaces before anything else runs — this workflow is for production routes on work already sold.
- **Client-context check**: does the client already have a CLAUDE.md (voice rules, format contracts)? If not, that IS the recon this workflow reads first — never freeze a production route without the client's actual constraints loaded.

## Skill Acquisition

- The client's own CLAUDE.md (e.g. `_active/clients/jen-listings/CLAUDE.md`, `_active/clients/andrea-dj/CLAUDE.md`) — the frozen-choice source: voice rules and format contracts, read in full before any freeze decision
- `genius.md` — the Economics section ("judgment arbitrage," "pay for the genius once, keep it forever"), Decision Heuristic 2 (freeze ambiguous choices now)
- Tier 1 workflows (`wargame-order`, `wargame-run`, `wargame-grade`, `wargame-execute`) and `/wargame-brief` — pointed to for mechanics, never duplicated here

## The Bank-Once-Spend-Repeatedly Shape

This is the same conductor pattern as `/wargame-mission` (compose Tier 1, don't duplicate it) applied to a different trigger: instead of a mission's riskiest workstream, the unit here is a CLIENT DELIVERABLE that recurs. The frontier-tier pass happens exactly once per deliverable type; every subsequent instance is `/wargame-execute` at whatever tier the client relationship can sustain economically. If a deliverable's wargame needs re-running every time a new instance comes in, it was never actually banked — that's a sign the mission brief (step 3) didn't freeze enough, and step 2 needs another pass at the client's CLAUDE.md.

## Execution

1. **Pick the exact repeatable unit.** Name it precisely — "one listing's content sheet," not "all of Jen's marketing." The wargame scopes to a single instance's production route, replayed across many future instances.
2. **Load the client's CLAUDE.md in full.** Every voice rule and format contract becomes a FROZEN CHOICE in the mission brief — Heuristic 2: freeze it now so no future instance re-litigates tone or structure.
3. **Write the mission brief per `/wargame-brief`**, with the client's format contract as the physical constraint. Jen's precedent: per-asset labeled production-sheet cards, never prose blobs (`feedback-client-content-production-format.md`) — that discipline gets written into the brief as a hard rule, not a style preference.
4. **Run `/wargame-order` → `/wargame-run` → `/wargame-grade` at frontier tier, highest effort.** This is the one expensive pass the economics section describes — "pay for the genius once."
5. **Grade to DONE before storing anything.** A client route that hasn't survived a red-team pass isn't bankable — it's still a draft that happens to have the client's name on it.
6. **Store the DONE wargame under the client project**, not `.agent/missions/` — e.g. `_active/clients/jen-listings/wargames/<deliverable-slug>.md`, `_active/clients/andrea-dj/wargames/<deliverable-slug>.md`. Client-owned artifacts live with client context, since they outlive any single mission session.
7. **Each new instance runs `/wargame-execute`** with the stored wargame as its route plus that instance's specific inputs — at cheap tier, since the judgment is already banked. This is the repeated, margin-positive execution the whole workflow exists to produce.
8. **Re-run from step 2 if the format contract changes.** A wargame's frozen choices are only valid as long as they match the client's actual current constraints — client feedback that shifts voice or format invalidates the old freeze.

## Content Type Adaptations

| Client deliverable type | Frozen-choice source | Stored-route location pattern |
|---|---|---|
| **Listing/production content** (Jen) | Client CLAUDE.md + production-sheet format contract | `_active/clients/jen-listings/wargames/` |
| **Event/ops route** (Andrea/Resonance) | Client CLAUDE.md + Ticket Tailor/venue constraints | `_active/clients/andrea-dj/wargames/` |
| **Launch/drop content** (MyBPM) | Brand voice doc + launch-week format | `mybpm-streetwear-brand` project wargames dir |
| **Any new repeatable client engagement** | That client's CLAUDE.md, once one exists | `<client-project>/wargames/` — create the dir on first use |

## Worked Example

Jen's per-listing content sheet: the repeatable unit is "one listing → one production sheet" (per-asset labeled cards, never prose blobs — the format contract already logged in her CLAUDE.md). Frozen choices: SFV specialist voice, ADU-as-bonus framing, hook style from the golden reference (6853 Willis). The frontier-tier pass wargames the ONE route — pull comps, draft hooks, format the sheet, verify against the golden reference — once. Every new listing after that runs `/wargame-execute` with that route plus the new address, square footage, and comps, at whatever tier keeps the engine margin-positive.

## When The Client Has No Format Contract Yet

If step 3's `/wargame-brief` pass finds the client's CLAUDE.md has voice rules but no explicit format contract (the physical shape of the deliverable — cards vs. prose, sheet vs. doc), that gap gets written into the client's CLAUDE.md as a decision FIRST, not guessed into the wargame. A format contract invented inside a wargame instead of ratified in the client's own context file will drift the next time someone edits that CLAUDE.md without knowing the wargame depends on it.

## Output Requirements

DONE-graded wargame at `<client-project>/wargames/<deliverable-slug>.md`, plus a one-line economics note appended to the client project's context file (e.g. its CLAUDE.md or handoff doc) confirming what's now bankable at cheap-tier execution versus what still requires a frontier-tier pass.

## Quality Gate

- [ ] Never wargames a one-off — the repeatability check from Pre-Flight is the hard gate, checked again before storing
- [ ] Client CLAUDE.md loaded and read in full before any freeze decision — a frozen choice made without reading the client's actual voice rules is a guess wearing a wargame's costume
- [ ] DONE bar is identical to Tier 1's — all 8 `SUCCESS.md` points plus a recorded red-team survival. Client work gets no rigor discount for being "just production," per the standing client-spec-first binding
- [ ] Stored under the client project, not `.agent/missions/` — a client-owned artifact left in transient mission state is a resurfacing failure waiting to happen
- [ ] The economics note names, in plain terms, what's now cheap-tier-executable versus what still needs a frontier-tier human decision
