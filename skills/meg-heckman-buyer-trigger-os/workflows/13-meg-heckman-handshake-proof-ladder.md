---
description: Handshake — Meg's 6-trigger buyer diagnosis selects which proof rungs matter before Iha's proof-ladder architecture builds them
---

# `/meg-heckman-handshake-proof-ladder` — Meg Heckman × Luke Iha Handshake

The compound output: a **trigger-ranked proof ladder** — not a generic 5-tier proof stack, but the subset of rungs that actually move THIS buyer, ordered by which of Meg's 6 triggers they serve. Meg diagnoses what fires the purchase; Iha builds only the proof that backs it. Sequential handshake, not parallel stacking: her trigger map is the INPUT the ladder is built FROM, not a co-equal lens applied after.

## Stacking Partners
- **Meg Heckman** (buyer-trigger-os) — supplies the **trigger diagnosis**: which of the 6 triggers (Identity Signal, Recognition Speed, Specificity, Social Currency, Familiar/Twist, Emotion-First) this buyer/product activates, and what passes the 50ms gate. She decides WHAT fires the purchase.
- **Luke Iha** (proof-ladder) — supplies the **proof-rung architecture**: the 5-tier ladder (Personal → Demonstrable → Social → Scientific → Aspirational) and the 22-type arsenal, ordered into a ladder that closes the sale. He decides HOW proof gets built and sequenced.

**Split**: Meg selects; Iha builds. Trigger map in, trigger-ranked proof ladder out — never the reverse. A ladder built before the trigger diagnosis is a generic proof stack wearing psychology vocabulary.

## Not This
If the job is overcoming **skepticism or armor** — an audience that actively defends against being sold to, objection-heavy, distrustful of the category — route to `/sean-armor-iha-proof` instead. That crossing selects proof by what the audience DEFENDS AGAINST. This crossing selects proof by what TRIGGERS PURCHASE. Sean × Iha = defense; Meg × Iha = offense. Don't run this handshake on a skeptical-armor problem — it will over-index on emotion-first proof and under-build the objection-neutralizing rungs Sean's diagnosis catches.

## When to Use
- A physical/visual product or PDP where identity/emotion drives the buy, but the proof stack still needs architecture (supplement, performance-brand, apparel, POD)
- Ad creative or launch messaging where you know the trigger but the proof underneath it is generic or absent
- A claim-safe category (supplement/performance) where emotion-first buying still needs FTC/FDA-appropriate proof scaffolding — the trigger tells you WHERE to spend proof budget, so you don't over-prove what doesn't move the buyer and under-prove what does
- Any buyer/product pairing where a generic proof audit (Iha alone) would stack all 5 tiers evenly, but the actual buyer only responds to 2-3 of them

## Handoff Contract
**In**: product/offer + buyer description (or existing concept/PDP/ad to diagnose)
**Meg's output**: trigger map — which trigger(s) fire for this buyer, ranked by strength, each with the 50ms-gate answer (5-word describable version) and the mirror-vs-poster verdict
**Iha's output**: proof ladder built FROM the trigger map — each rung tagged with the trigger it serves, tiers that don't back a live trigger demoted or cut
**Out**: trigger-ranked proof ladder — a proof architecture where every rung has a named trigger dependency, not a generic 5-tier stack

## Fused Sequence

### Step 1 — Trigger Diagnosis (Meg leads)
Run Meg's Decision Framework (7 questions, `genius.md`) against the buyer:
1. WHO is the one specific person? (behavioral moment, not demographic)
2. What does this let them SAY about themselves?
3. Mirror or poster?
4. Familiar element + twist?
5. Future social moment — who reacts, who buys because of it?
6. 5-word describable version (50ms gate)?
7. Feeling first — what does the buyer FEEL before any reason appears?

Score the 6 triggers for THIS buyer/product (not all 6 fire equally — that's the point). Output: 2-4 triggers ranked by strength, each with a one-line justification tied to the buyer's actual behavior, not the category's.

### Step 2 — Trigger-to-Proof-Tier Mapping (handshake point)
For each ranked trigger, name which of Iha's 5 tiers naturally backs it — this is the fusion logic, not two lists run side by side:

| Meg's Trigger | What it needs proof OF | Iha's tier that serves it |
|---|---|---|
| Identity Signal | The claim is true of people LIKE the buyer, not just true | Tier 3 (Social) — testimonials/community from the specific sub-identity |
| Recognition Speed | Nothing — this is a 50ms visual/copy gate, not a proof claim. Proof here is nearly zero-weight. | None (or Tier 1 only, as texture) |
| Specificity | The mechanism/result is real for THIS specific person's situation | Tier 2 (Demonstrable) — before/after, process breakdown naming the exact scenario |
| Social Currency | Other people actually reacted this way | Tier 3 (Social) — user count, name drops, community proof |
| Familiar/Twist | The twist claim (the surprising part) is defensible, not just clever | Tier 4 (Scientific) — the twist usually IS the claim that needs the hardest backing |
| Emotion-First Reason | The buyer's self-supplied logic has SOMETHING to lean on after the emotional decision | Tier 1 (Personal) — light-touch, post-purchase rationalization fuel, not pre-purchase persuasion |

This table is the fusion mechanism: it is not "run Meg then run Iha" — it is "Meg's ranked triggers determine which rows of this table activate, and only those tiers get built out."

### Step 3 — Build the Ladder (Iha leads, Meg's ranking constrains it)
For each trigger that scored in the top 2-4 (Step 1), build the actual proof rung using Iha's proof-audit method (mark claim → assess adjacent proof → check tier match → "so what?" test). For every trigger that did NOT rank — including triggers a generic proof audit would have covered by default (most commonly Recognition Speed and Familiar/Twist when the product doesn't lean on cleverness) — explicitly state what tier of proof gets CUT or DEMOTED, and why building it would be wasted proof budget.

Order the final ladder by trigger strength (Step 1 ranking), not by Iha's default tier order (1→5). The strongest trigger's proof rung ships first/most-prominent, regardless of which tier it lives in.

### Step 4 — Tag and Ship
Every rung in the final ladder carries a tag: `[TRIGGER: <name>] [TIER: <n>] <the actual proof asset or proof-building action>`. No untagged rungs — an untagged rung is either a generic stack leftover or an unjustified inclusion.

## Output Schema

```markdown
# [Product/Offer] Trigger-Ranked Proof Ladder — [Date]

## Trigger Diagnosis (Meg)
- Ranked triggers: [1. ... 2. ... 3-4 optional]
- 50ms gate (5-word version): [...]
- Mirror or poster: [verdict]
- Feeling before reason: [...]

## Trigger → Tier Fusion Map
[Table: ranked trigger | tier it demands | why]

## Trigger-Ranked Proof Ladder (Iha, built from the map)
1. [TRIGGER: X] [TIER: n] — proof asset/action
2. [TRIGGER: Y] [TIER: n] — proof asset/action
[...]

## Cut/Demoted Rungs (the subtraction — evidence of fusion, not decoration)
- [Tier N, would-be rung]: CUT/DEMOTED because [trigger it would have served didn't rank]

## What This Replaces
Neither a Meg trigger audit alone (tells you what fires purchase, leaves proof generic/absent) nor an Iha proof audit alone (builds a technically sound 5-tier stack that over-proves what doesn't move this specific buyer and under-proves what does).
```

## What This Replaces
- **A standalone Meg trigger audit** (`/meg-trigger-audit`) — correctly diagnoses what fires purchase but stops short of building the proof underneath it; ships a trigger score with no proof architecture attached.
- **A standalone Iha proof-ladder build** (`/proof-ladder-builder`) — builds a complete, well-architected 5-tier stack that treats all tiers as equally worth building, which over-invests proof budget in tiers the buyer never checks (often Scientific/Aspirational for an emotion-first buyer) and under-invests in the one or two tiers actually gating the purchase.
- **Generic "proof + psychology" copywriting** that names both vocabularies without the handshake — labeling a rung "Tier 3 Social Proof, taps Identity Signal" without the trigger ranking ever having constrained which rungs got built in the first place.

## Quality Gate
- Trigger ranking happened BEFORE any proof tier was selected — if tiers were chosen first and triggers retrofitted, rebuild
- At least one tier is explicitly cut or demoted (Step 3) — a ladder with all 5 tiers present at full weight means the fusion didn't happen
- Every rung carries both a `[TRIGGER:]` and `[TIER:]` tag — untagged rungs fail the gate
- Would Meg recognize the top-ranked trigger as a MIRROR, not a POSTER, before its proof rung got built? Would Iha recognize the proof as "architected, not decorated" (his own Recognition Test)? Both must pass.

## Pairs With
- `/meg-trigger-audit` — run first if the trigger diagnosis itself is uncertain (kill/revise verdict) before handing off to the ladder build
- `/meg-50ms-gate` — pre-flight the visual/copy gate on the top-ranked trigger's execution before the proof ladder ships
- `/proof-audit-360` — run on the finished ladder as an independent check that no naked claims slipped through
- `/sean-armor-iha-proof` — the defense-side counterpart; route here instead if the presenting problem is skepticism, not purchase-triggering
