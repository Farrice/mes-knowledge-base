---
description: Stack — April Dunford's 5-component positioning methodology supplies the truth spine, Kallaway's Illusion of Novelty engine runs a per-component pass on HOW each claim is expressed, so a positioning statement in a saturated category reads as genuinely new without becoming untrue
---

# `/kallaway-x-dunford`: Kallaway × Dunford, Truth-Bound Novelty

*Wave 3 opener, promoted from Wave 2 bench (matrix score 4.0).*

The compound output: Dunford builds the position first. Competitive alternatives, differentiated attributes, value, target segment, category, and every claim in it is true, checkable, defensible. Kallaway then runs a second pass over the same five components, asking only how each one is *worded*, never what it *claims*. Dunford alone produces a position that is correct and forgettable, because every supplement brand's positioning deck says "clean," "data-driven," "science-backed" in the same order. Kallaway alone produces language that stops a scroll but has no spine underneath it; it collapses under a compliance review or a sharp prospect's second question. Together, the position is both true and impossible to skim past, because the novelty lives entirely in the frame and never in the fact.

## Stacking Partners
- **Dunford (positioning)**: the truth spine. Competitive alternatives, differentiated attributes, value, target segment, market category. Supplies what is claimed. Nothing here is negotiable; the novelty pass never touches this layer.
- **Kallaway (Illusion of Novelty)**: the 5-component novelty engine, applied per Dunford component to control how it lands. New Reveal framing finds the fresh angle into the same fact. Contrast Framing positions it against the category's tired version of the same claim. Bullseye Proof climbs the trust ladder without inventing a rung that isn't there.

## When to Use
- A positioning statement is factually sound but reads exactly like every other player's deck in a saturated category. "Clean," "data-driven," "premium," "results-driven" are doing the work, and a prospect has seen the sentence shape a dozen times before you finish it.
- Dunford's build is done (competitive alternatives mapped, differentiated attributes real, value proven) and the deliverable is stalling not on truth but on delivery. The words themselves are the stock phrases of the category.
- A founder or brand team keeps reaching for the same three adjectives every competitor uses, and no one on the team can tell whether the underlying claim actually differs or is just described the same way.

## Not This
Novelty here **never changes what is claimed, only how it lands.** If a component in the pass makes a stronger claim than the Dunford input supports (a proof point promoted a rung on the trust ladder it hasn't earned, an urgency window that isn't real, a differentiator restated as bigger than it is), that is truth-bending. It is an instant kill, not a style note. The novelty pass rewrites *packaging*; it never touches *substance*. Two adjacent workflows own what this one doesn't:
- **Full positioning build from scratch** (no existing Dunford artifact yet) routes to Dunford's own Tier 1 front doors: `dunford-positioning-diagnostic` or `product-positioning-blueprint`. Build the truth spine there first, then bring the finished positioning here.
- **Premise validation** (the positioning question itself is suspect: wrong category, wrong differentiator) routes to `/godin-handshake-dunford`. That crossing interrogates the premise before Dunford builds on it. This crossing assumes the premise already cleared and the build is done; it only re-expresses it.

## Inputs
- `[DUNFORD_POSITIONING]`: the finished or near-finished 5-component positioning (competitive alternatives, differentiated attributes, value, target segment, category), from a prior Dunford workflow or an existing doc
- `[CATEGORY_STOCK_PHRASES]`: the tired claims the category runs on ("clean," "data-driven," "science-backed," "personalized"). Pull from competitor copy if not already known.
- `[AVATAR_HELD_BELIEF]`: what the buyer already assumes about brands making this kind of claim, needed for Contrast Framing per component

## Execution

### Step 1: Dunford Canvas In
Take the finished positioning as-is. Do not touch the claims. List the five components plainly: competitive alternatives, differentiated attributes, value, target segment, category. Each one should already be checkable against evidence. If a component isn't, that's a Dunford gap, not a Kallaway one. Send it back to the source workflow before continuing.

### Step 2: Per-Component Novelty Pass (Kallaway, run on EACH of the five)
For every component, hold the claim exactly fixed and ask the three Kallaway questions of the *expression* only:
- **New Reveal**: is there a fresher angle into this same fact, or is the current wording the first cliché anyone reaches for? Never invent a new fact. Find the door into the existing one that the category hasn't used yet.
- **Contrast Framing**: what does the buyer already believe about brands claiming this? Position the true claim against that held belief as a real opposite, not a strawman.
- **Bullseye Proof**: what's the closest-to-the-buyer proof this component can *honestly* carry? Self-identification beats a third-party stat, but never climb a rung higher than the evidence supports.
Score each component: **fresh, decaying (stock but salvageable), or stale (verbatim category phrase).**

### Step 3: Saturation Check
Run every re-expressed component against the category's stock-phrase list from `[CATEGORY_STOCK_PHRASES]`. Any sentence that could be lifted unchanged and dropped into a competitor's deck fails the check, even if the underlying claim differs from theirs. Dunford already secured originality of fact in Step 1; this step tests only whether the *sentence* reads as interchangeable. Rewrite anything that fails, still without moving the claim.

### Step 4: Out, Same Truth, Non-Stock Expression
Deliver the five components with the claim unchanged and the wording passed. Mark each with the original expression, the novelty-passed expression, and a one-line note on which Kallaway lever did the work: reveal, contrast, or proof.

## Output Format
```
DUNFORD SPINE (unchanged)
Competitive Alternatives: [claim]
Differentiated Attributes: [claim]
Value: [claim]
Target Segment: [claim]
Category: [claim]

Per-Component Novelty Pass
[Component] | novelty verdict (fresh/decaying/stale) | before | after | lever used (reveal/contrast/proof)
...

Saturation Check
[component] | stock phrase it risked blending into | pass/fail | fix if failed

Truth-Bend Audit
Any claim strengthened, promoted, or invented during the pass: [none, or flag + revert]
```

## What This Replaces
Replaces running Dunford's positioning build and then handing the finished deck straight to a copywriter with no intermediate check. The claims are true but the sentences are stock, and the copywriter either repeats the stock phrasing or, worse, "punches it up" by quietly overstating a claim to make it sound fresher. Also replaces running `/novelty-forge` directly on a positioning claim with no Dunford spine underneath it. Novelty applied to an unverified or undifferentiated claim produces language that stops a scroll and then loses the deal the moment a sharp buyer asks a follow-up question the position can't survive. This crossing is the only one in the stack that gates novelty on a truth artifact before applying it.

## Quality Gate
- [ ] Every one of the five Dunford components run through the novelty pass, not just the headline or category line
- [ ] No claim strengthened, promoted, or invented during the pass; truth-bend audit is clean or every flag is reverted
- [ ] Every re-expressed component failed the saturation check against a real category stock phrase before the fix. If it never risked sounding stock, the pass wasn't necessary.
- [ ] Contrast Framing anchored to the buyer's actual held belief about this claim type, not a strawman
- [ ] Bullseye Proof never climbs a rung the underlying evidence doesn't support
- [ ] Differentiation preserved: full-build-from-scratch routes to Dunford's Tier 1 front doors; premise doubt routes to `/godin-handshake-dunford`; this workflow only re-expresses a finished, already-true position

## Pairs With
- `dunford-positioning-diagnostic` / `product-positioning-blueprint`: builds the truth spine this workflow re-expresses. Run first if no finished positioning exists.
- `/godin-handshake-dunford`: upstream premise gate. Clears the positioning question itself before Dunford builds, well before this crossing touches the wording.
- `dunford-positioning-to-copy`: downstream. Hands the novelty-passed positioning to production copy experts (Wiebe, Sultanic, Kallaway word-mastery) once the frame is locked.
- `/novelty-audit`: the general-purpose diagnostic this crossing specializes for positioning claims, with a truth-bend gate Dunford alone doesn't provide and `/novelty-audit` alone doesn't require
