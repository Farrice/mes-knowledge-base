---
description: Fire when Farrice hands over a laundry list of 2+ missions (a portfolio, not a single ask) that all need wargamed routes before any executor touches them — new client onboarding, a multi-workstream launch, a backlog of "get to this eventually" tasks. Operationalizes Kashef's /goal contract (breadth-first draft) then the /loop contract (weakest-first refinement) verbatim.
---

# /wargame-batch — The /goal Contract, Run

This workflow IS the `/goal` and `/loop` prompts from `references/goal-and-loop-contracts.md` adapted to Antigravity's mission-folder convention. It doesn't reinterpret them — it executes them. "Don't Run Them One by One. Run the List."

## Pre-Flight Gate

- **Portfolio check**: is this actually 2+ independent missions? A single mission doesn't earn breadth-first sequencing — route it straight through `/wargame-order` → `/wargame-run` → `/wargame-grade` instead. Heuristic 5 ("draft all ten before polishing any") only applies once there's a list to sequence.
- **Tier-gap check**: will these missions execute on a cheaper/different model than the one drafting them? Heuristic 1 — "wargame it, don't plan it" — fires specifically when the drafting tier and executor tier diverge. If they're identical, a plan may suffice; confirm the gap exists before spending the drafting budget.
- **Effort ceiling set first**: per the effort-economics note in `goal-and-loop-contracts.md`, drafting runs at the highest effort available; decide the ceiling and the degrade order (refinement drops first, drafting never does — Heuristic 10) BEFORE the fan-out starts, not mid-cycle.
- **Recon targets named**: each mission needs its read-only recon source identified (reference site, voice samples, transcripts, machine specs — whatever the domain requires). If unnamed, run `/wargame-recon` per mission first; this workflow assumes recon targets are already on the mission brief, not still being elicited.
- **Naming check**: does the portfolio have a folder-safe name (`<name>` in `.agent/missions/<name>/`)? Pick one before scaffolding — a portfolio that never gets a stable name is a portfolio nobody can resume mid-loop.

## Skill Acquisition

- `genius.md` — full Decision Heuristics section (1, 5, 6, 7, 10 are load-bearing here); Anti-Patterns 3, 4, 6
- `references/goal-and-loop-contracts.md` — the verbatim `/goal` and `/loop` text this workflow adapts; re-read before every batch, don't paraphrase from memory
- `references/eight-point-standard.md` — the SUCCESS.md grading discipline used at both the draft self-grade and the refinement re-grade
- `assets/wargame-folder-template/` — `SUCCESS.md`, `LEDGER.md`, the `tasks/`/`wargames/` folder contract to scaffold from
- `references/mission-brief-library.md` — if a laundry-list item matches one of the 10 Kashef domains (website/copy/offer/bugs/tax/local-ai/chatbot/model/competitors/automation), pull its starting brief and placeholder map instead of writing cold

## Execution

1. **Scaffold the mission folder.** For portfolio `<name>`, create `.agent/missions/<name>/{tasks,wargames}/` and copy `SUCCESS.md` + a blank `LEDGER.md` from `skills/mark-kashef-wargame-os/assets/wargame-folder-template/`. Command: `mkdir -p .agent/missions/<name>/{tasks,wargames}` then `cp` the two template files in.
2. **Write one mission file per laundry-list item** into `tasks/<NN>-<slug>.md`. Each is the executor's definition of done, never a wargame itself.
   - Domain-matched items pull their starting brief straight from `references/mission-brief-library.md`.
   - Everything else gets written fresh under `/wargame-brief` discipline, keeping the "the executor's orders, not yours" framing.
   - Number files `01-`, `02-`, ... in laundry-list order — the numbering is what the ledger and the wargame filenames key off of downstream.
3. **Fan out one Agent-tool call per mission, in parallel** — single message, multiple Agent invocations, never sequential.
   - This is the `/goal` contract's "fan out a series of parallel agents" and Farrice's standing binding: ad-hoc Agent-tool dispatch, never `.claude/agents/` personas.
   - Each agent receives the identical WARGAME ORDER preamble (only the recon-target line changes per mission, per the Signature Move in genius.md) and writes `wargames/<NN>-<slug>.md` move by move.
   - Recon inside each agent's run stays read-only — no state-mutating commands, per Anti-Pattern 7.
4. **Each agent logs its own LEDGER.md entry** on finishing: mission name, draft location, honest point-by-point self-grade against all 8 points of `SUCCESS.md` — never a single holistic score (eight-point-standard.md grading discipline).
5. **Unfilled `{{PLACEHOLDER}}`s BLOCK the mission**, not the batch. Log exactly what's needed in LEDGER.md and move to the next mission — never invent the missing input (Anti-Pattern 3 / Heuristic 4).
6. **Hard stop for drafting**: every mission is DRAFTED or BLOCKED in LEDGER.md. No mission gets polished while others sit undrafted (Anti-Pattern 6).
7. **Run the `/loop` cycle verbatim**:
   - Grade every DRAFTED wargame point by point against `SUCCESS.md`, log in LEDGER.md.
   - Take the WEAKEST draft — the lowest point-count, not the most recently touched — and red-team it: play the executor following it blind, attack the route, find the move where it breaks.
   - Patch the break, add the branch that catches it next time, upgrade vague moves with expected observations, convert unstated assumptions to RECON NEEDED marks with settling checks.
   - Re-grade the patched draft and log what changed, including the attack that failed against the new version.
8. **Stop the loop** when every wargame is DONE or BLOCKED, or two consecutive cycles improve nothing. Post the final ledger.
9. **Effort discipline**: drafting (steps 3–6) stays at the ceiling set in Pre-Flight. If budget tightens mid-loop, degrade the refinement loop's tier/effort first — consistent with the Opus-fallback policy (degrade a tier, don't stall). Drafting never degrades.

## Content Type Adaptations

| Type | Domain match (mission-brief-library) | Recon source | Note |
|---|---|---|---|
| **Code build** | 01-website (XHIGH), 07-bugs (XHIGH) | reference site / repo, README, core-flow trace | Highest-stakes tier — never let these degrade to skip the red-team |
| **Copy/content** | 02-copy (HIGH), 05-offer (XHIGH) | voice samples, current pitch/page | Frozen choices = voice adjectives + CTA, decided once, not per instance |
| **Research/analysis** | 04-tax (XHIGH), 09-competitors (HIGH) | statements/categories, competitor properties | Evidence rule fires: "anything you cannot verify gets marked unverified" |
| **Ops/automation** | 03-localai (HIGH), 06-chatbot (HIGH), 08-model (HIGH), 10-automation (HIGH) | machine specs, transcripts, process description | Verification runs are mechanical (tokens/sec, formula sanity-check) — spell out the pass state exactly |

## Effort Tag Reference

Mission-brief-library.md tags each of the 10 Kashef domains HIGH or XHIGH. Carry that tag onto every laundry-list item, matched or not, so the drafting pass knows where it can least afford to degrade:

| Effort tag | Meaning for this workflow | Domains |
|---|---|---|
| **XHIGH** | Drafting AND refinement both stay at max effort as long as budget allows; if forced to degrade, do it last and log the tradeoff explicitly | website, tax, offer, bugs |
| **HIGH** | Drafting stays at max effort; refinement is the first and expected place to degrade under budget pressure | copy, local-ai, chatbot, model, competitors, automation |

An unmatched laundry-list item defaults to HIGH unless Farrice names it higher — never assume XHIGH without a reason, and never silently downgrade a mission Farrice flagged as high-stakes.

## Output Requirements

1. `.agent/missions/<name>/tasks/*.md` — one mission brief per laundry-list item
2. `.agent/missions/<name>/wargames/*.md` — one wargame per mission, schema per genius.md Document Schema section (mission spec, RECON NEEDED, Moves 1–N, abort conditions, verification runs)
3. `.agent/missions/<name>/LEDGER.md` — every draft and refinement entry, point-by-point grades, patches logged as they happen, never batched after the fact
4. A final ledger post at loop-stop stating DONE/BLOCKED per mission and, for BLOCKED ones, the exact input needed

## Resuming A Batch Mid-Loop

A batch spanning multiple sessions resumes from LEDGER.md, not from memory: read the last entry per mission, confirm its DRAFTED/BLOCKED/DONE state, and continue the loop from there — never re-draft a mission that already has a logged grade. If a BLOCKED mission's input has since arrived, treat it as newly DRAFTED and fold it into the next refinement cycle rather than running it separately.

## Quality Gate

- [ ] No mission was polished before every mission in the portfolio reached DRAFTED or BLOCKED (Anti-Pattern 6)
- [ ] No LEDGER.md entry is a single holistic score — every grade is point-by-point against all 8 `SUCCESS.md` criteria
- [ ] No `{{PLACEHOLDER}}` was silently filled with an invented value — every gap is BLOCKED and named (Anti-Pattern 3)
- [ ] Every DONE wargame's LEDGER entry records the red-team attack that failed against it, not just a passing grade (Anti-Pattern 2 — softened grading fails this outright)
- [ ] Drafting effort never degraded; only the refinement loop dropped tier if budget tightened
- [ ] Loop-stop condition is one of the two named states (all DONE/BLOCKED, or two flat cycles) — not an arbitrary time cutoff
