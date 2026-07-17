---
description: The Expansion Lab — collaborative ideation that escapes Farrice's default frame; mechanism-driven divergence → collision candidates → gut round → route to /jam or production
---

# /ideate — The Expansion Lab

`/ideate "<seed>"` (expand any seed: content idea, offer, project, problem, objective)
`/ideate blank` (no seed — mine memory/thought-bank/episodic for latent threads, propose 3 seeds)
`/ideate content` (content mode — winners feed the SLL lane bank / farrice-engine / parallax)

## Why this exists (Farrice, 2026-07-17)

"Ideation is one of the big bottlenecks... I don't want to just be thinking through the
limited range of my own thoughts anymore. I want to be able to collaboratively expand and
create things with you and come out with new, novel, and also beneficial ideas and concepts."

The failure this kills: brainstorm lists that are just Farrice's own frame echoed back with
bullet points. The whole point is ideas he would NOT have reached alone — so the novelty bar
is structural, not decorative. /ideate sits UPSTREAM of `/jam` (which refines a chosen thing);
this workflow decides what's worth refining.

## Posture

Runs at PARTNER dial (CO-CREATION-CARD, Step 0): memory-first, then at most ONE stretch
question aimed past his current frame, then produce. Rounds cost ≤2 minutes of Farrice's
attention each. Claude states an opinion every round — a partner with no stake is a vendor.

## The Session

### Round 0 — PRIOR (silent, before anything)
- `python3 execution/memory_facade.py "<seed>" --top 10` + read `.agent/ideation/idea-ledger.jsonl`
  (if present) + scan `_active/farrice-brand/thought-bank/inbox/` for adjacent captured thoughts.
- Read `.agent/cos/goals.json` — candidates must later tie to a goal or be flagged.
- State the prior in ONE line ("your last 3 sessions killed every meta-content idea — noted").
- Capture any vision language in the seed VERBATIM as the felt standard.

### Round 1 — STRETCH (optional, one question max)
Only if the seed is foggy: one question aimed PAST his frame — never "what do you want?",
always "what would this look like if [assumed constraint] were false?" grade. Skip when the
seed is sharp; never interview about what memory already knows.

### Round 2 — DIVERGE (the engine — 5 mechanisms × 3-5 sparks each)
Every spark is one line + its mechanism tag. A spark without a mechanism is list-slop; cut it.

1. **INVERT** — flip the seed's load-bearing assumption ("what if the bottleneck is the asset?")
2. **TRANSFER** — steal a structure from an unrelated extracted expert (the 222-expert registry
   is an idea collider: "what would Stanton's spine test / Priestley's lane bank / Hawley's
   ending-first do to this seed?"). Name the expert per spark.
3. **COLLIDE** — force-merge the seed with a live thread from memory/goals/thought-bank
   ("this × the bowling league × the invisible-expert ICP").
4. **AMPLIFY-THE-WEIRD** — take the strangest TRUE detail in the seed's territory and scale it
   until it becomes a concept.
5. **ZEITGEIST** — what's genuinely moving in the world right now that multiplies this
   (Priestley's ×News logic generalized; verify trends, no phantom research).

**Kill rule**: delete any spark Farrice would have produced alone in 10 minutes. If a lens
yields only obvious sparks, say so and drop it — 12 honest sparks beat 25 padded ones.
Deep sessions MAY fleet the lenses (one agent per mechanism, Tier 3); quick sessions run
solo in-thread. Fleet before, never during, the gut round.

### Round 3 — CANDIDATES (collide sparks into 3-5)
Each candidate carries exactly four lines:
- **What**: the concept in one sentence.
- **New because**: names the default frame it escapes ("you'd have framed this as X; this is Y").
- **Beneficial because**: ties to a named goal in goals.json (else flag `ORPHAN ⚑` — compass,
  never cage).
- **Fastest proof**: the cheapest same-week test (a post, a DM, a landing page, a 30-min build).

### Round 4 — GUT ROUND
Present candidates via AskUserQuestion with previews, jam grammar verdicts (`A` / `A but
<dial>` / `mix:` / `neither — <word>`), plus Claude's one-line pick with reason. Append every
verdict to `.agent/ideation/idea-ledger.jsonl`:
`{ts, seed, candidates, verdict, dials, goal, note}` — killed ideas get a one-word why; the
kill-pattern is as compounding as the pick-pattern. Patterns repeating 3+ sessions graduate
to a proposed memory line (never silently).

### Round 5 — ROUTE (never end on a list)
Winner goes somewhere concrete, same session:
- **Refine** → `/jam new "<winner>"` (taste loop)
- **Produce** → the owning engine (`/daniel-priestley-sll-engine` workflow 02 for short-form,
  `/parallax`, `/ghostwrite`, `/copy-engine`, `/forge-os` for tools…)
- **Park** → thought-bank inbox (retrievable shelf, one-line hook)
Losers → ledger. Session closes with the standard Steering block.

## Hard Rules

- Novelty bar is structural: every candidate names the frame it escapes. No named frame = not novel = not a candidate.
- One question per round, substance first, opinion required, disagreement allowed once (jam rules inherit).
- Mechanism tags mandatory in Round 2; "more ideas" is never the fix — better collisions are.
- This workflow generates and selects; it never bypasses Chain gates when a winner goes to production.

## Composition (options, never pipeline steps)

`/gw-*` deep thought-partner modes for strategy-grade seeds · `luke-iha-insight-vectors` /
`sean-three-vector-idea-forge` / `novelty-forge` / `divergent-ideation` as heavier lens
plug-ins when a single mechanism deserves a full workflow · `/convene` when the seed is a
decision, not an idea.

## Standing option (propose-only)

An **Expansion Hour** can run as a recurring event (e.g. 1st/15th cloud routine: run
`/ideate blank` overnight, stage Round 3 candidates so the gut round is waiting with coffee,
morning-after-jam style). Not scheduled until Farrice ratifies — say the word and it gets wired.
