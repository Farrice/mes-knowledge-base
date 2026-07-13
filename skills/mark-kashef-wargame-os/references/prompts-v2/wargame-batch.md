---
name: "Mark Kashef — Wargame Portfolio Batch"
source_prompt: born-v2
skill: mark-kashef-wargame-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Kashef's `/goal` and `/loop` prompts verbatim, adapted to a mission-folder convention — not reinterpreting them, executing them. "Don't Run Them One by One. Run the List." This deliverable exists specifically for a laundry list of 2+ independent missions that all need wargamed routes before any executor touches any of them: draft every mission breadth-first to DRAFTED-or-BLOCKED, THEN run the weakest-first refinement loop to depth. Breadth reveals cross-cutting failure patterns before refinement over-fits to one mission's texture; under a token cap it guarantees N usable-if-rough assets over a few perfect ones and the rest blank.

## Input Required

- `[MISSION LIST]` — the laundry list of 2+ items to draft
- `[PORTFOLIO NAME]` — folder-safe name for `.agent/missions/<name>/`
- `[EFFORT CEILING]` — the drafting-tier ceiling, set before the fan-out starts, plus the agreed degrade order (refinement drops first, drafting never does)
- `[RECON TARGETS]` — per-mission read-only recon sources; if any are unnamed, run recon-elicitation per mission first — this workflow assumes targets are already on each brief
- `[TIER GAP CONFIRMATION]` — confirmation the missions will execute on a cheaper/different model than the one drafting them

## Execution Protocol

**Pre-Flight:** confirm this is genuinely 2+ independent missions (a single mission routes through the Tier 1 sequence directly instead); confirm the tier gap between drafting and execution actually exists; set the effort ceiling and degrade order BEFORE the fan-out starts; confirm recon targets are named per mission; confirm the portfolio has a stable folder-safe name.

**Steps:**
1. Scaffold `.agent/missions/[PORTFOLIO NAME]/{tasks,wargames}/`, copying `SUCCESS.md` and a blank `LEDGER.md` from the folder template.
2. Write one mission file per laundry-list item into `tasks/<NN>-<slug>.md` — each is the executor's definition of done, never a wargame itself. Domain-matched items pull their starting brief from the mission-brief library; everything else gets written fresh under the executable-blind brief discipline. Number `01-`, `02-`, ... in laundry-list order — the ledger and wargame filenames key off this numbering.
3. Fan out one Agent-tool call per mission, in parallel — single message, multiple invocations, never sequential. Each agent receives the identical WARGAME ORDER preamble (only the recon-target line changes per mission) and writes `wargames/<NN>-<slug>.md` move by move. Recon inside each agent's run stays strictly read-only.
4. Each agent logs its own `LEDGER.md` entry on finishing: mission name, draft location, an honest point-by-point self-grade against all 8 points — never a single holistic score.
5. Unfilled placeholders BLOCK the mission, not the batch. Log exactly what's needed and move to the next mission — never invent the missing input.
6. Hard stop for drafting: every mission is DRAFTED or BLOCKED in `LEDGER.md`. No mission gets polished while others sit undrafted.
7. Run the `/loop` cycle verbatim: grade every DRAFTED wargame point by point, log in `LEDGER.md`; take the WEAKEST draft (lowest point-count, not most-recently-touched) and red-team it — play the executor following it blind, attack the route, find the move where it breaks; patch the break, add the branch that catches it next time, upgrade vague moves with expected observations, convert unstated assumptions to RECON NEEDED marks; re-grade the patched draft and log what changed, including the attack that failed against the new version.
8. Stop the loop when every wargame is DONE or BLOCKED, or two consecutive cycles improve nothing. Post the final ledger.
9. Effort discipline: drafting stays at the ceiling set in pre-flight throughout. If budget tightens mid-loop, degrade the refinement loop's tier/effort first — drafting never degrades.

**Effort tags** (carry onto every laundry-list item, matched or not): XHIGH (website, tax, offer, bugs) — drafting AND refinement both stay at max effort as long as budget allows; if forced to degrade, do it last and log the tradeoff. HIGH (copy, local AI, chatbot, model, competitors, automation) — drafting stays at max effort; refinement is the first and expected place to degrade under budget pressure. An unmatched item defaults to HIGH unless the operator names it higher — never assume XHIGH without a reason, never silently downgrade a mission flagged high-stakes.

**Resuming mid-loop:** a batch spanning multiple sessions resumes from `LEDGER.md`, not from memory — read the last entry per mission, confirm its DRAFTED/BLOCKED/DONE state, continue from there. Never re-draft a mission that already has a logged grade. A previously-BLOCKED mission whose input has since arrived gets treated as newly DRAFTED and folded into the next refinement cycle.

## Output Contract

1. `.agent/missions/[PORTFOLIO NAME]/tasks/*.md` — one mission brief per laundry-list item
2. `.agent/missions/[PORTFOLIO NAME]/wargames/*.md` — one wargame per mission, all five Document Schema sections each
3. `.agent/missions/[PORTFOLIO NAME]/LEDGER.md` — every draft and refinement entry, point-by-point grades, patches logged as they happen, never batched after the fact
4. A final ledger post at loop-stop stating DONE/BLOCKED per mission, with the exact input needed for each BLOCKED one

## Output Skeleton

```
.agent/missions/[PORTFOLIO NAME]/
  SUCCESS.md
  LEDGER.md
  tasks/
    01-[slug].md   [WARGAME ORDER + brief, per mission]
    02-[slug].md
    ...
  wargames/
    01-[slug].md   [full Document Schema, per mission]
    02-[slug].md
    ...
```

Ledger entry shape (repeats per mission, per cycle):
```
[Mission NN] — [DRAFTED / DONE / BLOCKED — {{PLACEHOLDER}}]
Self-grade (draft): [8-point PASS/FAIL]
Cycle N grade: [8-point PASS/FAIL]
Weakest-draft attack: [move + break]
Patch: [what changed]
```

Final ledger post:
```
FINAL LEDGER — [PORTFOLIO NAME] — [date]
[mission NN]: DONE | BLOCKED — [exact input needed]
[repeat per mission]
```

## Quality Gate

- [ ] No mission was polished before every mission in the portfolio reached DRAFTED or BLOCKED
- [ ] No `LEDGER.md` entry is a single holistic score — every grade is point-by-point against all 8 criteria
- [ ] No `{{PLACEHOLDER}}` was silently filled — every gap is BLOCKED and named
- [ ] Every DONE wargame's ledger entry records the red-team attack that failed against it, not just a passing grade
- [ ] Drafting effort never degraded; only the refinement loop dropped tier under budget pressure
- [ ] Loop-stop condition is one of the two named states (all DONE/BLOCKED, or two flat cycles) — not an arbitrary time cutoff

## Creative Latitude

The real skill in a batch is sequencing judgment: which mission is genuinely the weakest each cycle (point-count, not recency-of-touch), and when two consecutive cycles have actually stopped improving versus just slowed down. Domain-matching a laundry-list item to the mission-brief library is itself a judgment call — a near-match adapted well beats a forced fit or a cold rewrite.

## Deploy When

Farrice hands over a laundry list of 2+ meaty missions that all need wargamed routes before any executor touches them — new client onboarding, a multi-workstream launch, a backlog drafted breadth-first before any of it gets polished.
