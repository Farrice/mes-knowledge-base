---
name: "Satori Graphics — Feeling Calibration Spec"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running Satori's **Feeling Calibration**: retuning a fixed asset's feeling (premium / cheap / playful / reassuring) using visual language alone — typography, color, layout, surface. The content does not change; only the feeling moves, through four levers, gated by an audience-fit veto and a locked walk-away emotion.

> "we can take the same burger for our design here and we can make it appear cheap using layout, color, and typography choices. Or we can conversely make it feel more expensive and more premium... achieved with the visual language decisions alone." — Satori
> "It is no good trying to make your design premium if the end users are teenagers or students with little to no money at disposal." — Satori

## Input Required

- **[LOCKED CONTENT]** — the headline text, body copy, offer, price, logo, product — verbatim, and NOT allowed to change during this workflow
- **[CURRENT FEELING]** — the asset's feeling as it stands today, if known
- **[TARGET FEELING]** — premium / cheap-value / playful / reassuring, or a stated other
- **[ACTUAL AUDIENCE]** — who really sees this (not the aspirational viewer) — required for the audience-fit veto in Step 2

## Execution Protocol

### Step 1 — Lock the Content, Name the Current Feeling

Copy the fixed content into the spec as LOCKED. Name the current feeling in one word + one clause ("cheap — the price shouts louder than the product," "sterile — technically clean but cold," "loud — assumes I'm already sold"). A vague "meh" is not a diagnosis.

### Step 2 — Set the Target Feeling, Then Run the Audience-Fit Veto

Pick ONE target: **Premium** ("worth more than it costs; I belong with this"), **Cheap/value** ("a deal — grab it before it's gone"), **Playful** ("fun — I'm allowed to enjoy this"), or **Reassuring** ("safe — I can relax and trust it"). This is a match to a specific viewer, not a taste preference.

Run the veto — any "no" halts the calibration:
- Who actually sees this? (the real viewer, not the aspirational one)
- Can they act on the target feeling? (premium to a broke audience creates unmonetizable aspiration; cheap to a luxury buyer reads as untrustworthy)
- Does the target feeling match the price/offer/brand promise? (a $9 product dressed as $900 reads as a lie)

If the veto fails, **re-choose the target** — never override the veto.

### Step 3 — Match the Arrival Emotion

Name the viewer's state 30 seconds before contact (distracted mid-scroll? skeptical, comparing prices? bored, hungry, hurried?). The gap between arrival emotion and target feeling is the work — a big gap (bored-scroller → premium reverence) needs a stronger lever set than a small one. If the gap is too large for one asset to cross, stage it in sequence or soften the target.

### Step 4 — Prescribe the Per-Lever Moves (all four dials, no vague adjectives)

1. **Typography psychology** — weight, serif vs. sans, tracking/leading, case.
2. **Color scheme** — temperature, saturation/chroma, value contrast, hue count. (Pair with the Strategic Color System prompt for a deep pass.)
3. **Layout** — density, whitespace, alignment, hierarchy dominance.
4. **Surface treatment** — solid flat vs. gradient, texture, finish cues (matte/gloss/foil/emboss), effects.

Calibration matrix (starting prescription, tailor to the asset):

| Lever | → Premium | → Cheap/value | → Playful | → Reassuring |
|---|---|---|---|---|
| Typography | High-contrast serif or thin refined sans; wide tracking on caps; light-regular weight; restraint | Heavy/black condensed sans; ALL-CAPS; tight tracking; multiple weights shouting | Rounded/hand-drawn sans; mixed case; bouncy baseline; script accents | Humanist sans, medium weight; sentence case; comfortable leading; soft terminals |
| Color | 1-2 colors + neutral; low saturation; deep neutrals; high value contrast, low chroma | Many saturated hues; hot reds/yellows; max chroma; "sale" red | Bright multi-hue; unexpected pairings | Cool blues/soft greens/warm neutrals; low-mid saturation |
| Layout | Extreme whitespace; low density; one leverage point; disciplined alignment | High density; packed; starbursts/banners; price dominates | Asymmetric; tilted/overlapping; deliberate grid-breaks | Generous breathing space; calm alignment; one trust cue |
| Surface | Solid flat or subtle matte; matte/uncoated/foil/emboss cues | Glossy gradients; shiny highlights; drop shadows/bevels; badges | Soft gradients; stickers; organic blobs; tactile texture | Solid soft fills or gentle low-contrast gradient; matte |
| Walk-away | Quiet confidence | Urgency / "get the deal" | Mischievous delight | Calm reassurance |

Write each move: `LEVER: [...] · FROM: [current property+value] · TO: [target property+value] · WHY: [target-feeling driver served]`. **Rent check**: every move must pay rent toward the target — a move present because it "looks designy" gets evicted.

### Step 5 — Render the Contrast

Where feasible, spec two calibrations of the identical locked content side by side, as a delta table (Content · Typography · Color · Layout · Surface · Reads-as), so the client compares *feelings*, not two unrelated designs. If shipping only one, still spec the rejected opposite in one line — proving the chosen feeling was a decision, not a default.

### Step 6 — Lock the Walk-Away Emotion

State the single emotion the viewer carries out. This is the acceptance criterion: if the levers are pulled to "premium" but the viewer walks away feeling *pressured* or *priced-out*, the calibration failed regardless of beauty. Confirm the arc: arrival emotion (Step 3) → walk-away emotion (locked, ONE only — two competing emotions cancel and the asset reads as confused).

### Step 7 — Re-Run the Audience-Fit Veto on the Finished Calibration

Levers can drift past the target during execution ("premium" quietly becoming "unreadably subtle" for a fast-scroll feed) — re-check before delivery.

## Output Contract

A Feeling Calibration Spec: locked content, current-vs-target feeling, the audience-fit veto verdict, the emotion arc (arrival→walk-away, locked), all four lever moves written as FROM→TO→WHY, a contrast delta table (or a one-line rejected-opposite note), and an anti-pattern checklist.

## Output Skeleton

```markdown
# Feeling Calibration — [asset name]

## Locked Content (does NOT change)
- Headline / copy / offer / price / logo: [verbatim — LOCKED]

## Feeling Shift
- Current feeling: [one word + one clause]
- Target feeling: [premium / cheap / playful / reassuring / other]

## Audience-Fit Check (VETO)
- Who actually sees this: [...]
- Can they act on the target feeling? [Y/N — reason]
- Does target match price/offer/brand? [Y/N — reason]
- Verdict: [PASS / RE-CHOOSE TARGET]

## Emotion Arc
- Arrival emotion (in): [...]
- Walk-away emotion (out, locked, ONE): [...]

## Per-Lever Moves
- Typography: FROM [...] → TO [...] · WHY [...]
- Color: FROM [...] → TO [...] · WHY [...]
- Layout: FROM [...] → TO [...] · WHY [...]
- Surface: FROM [...] → TO [...] · WHY [...]

## Contrast (same content, two feelings)
[delta table: rejected calibration vs. chosen calibration]
Rejected opposite (if shipping one): [one line]

## Anti-Pattern Check
- [ ] Content unchanged (feeling moved, message didn't)
- [ ] ONE target feeling, ONE walk-away emotion
- [ ] Audience-fit veto passed on the FINISHED calibration
- [ ] Every lever move pays rent toward the target
```

## Quality Gate

- Content is demonstrably unchanged — only the feeling moved
- Exactly one target feeling and one walk-away emotion (never two competing)
- The audience-fit veto passed on the finished calibration, not just the initial plan
- All four levers are prescribed as executable FROM→TO moves, no naked adjectives
- At least one deliberate human-imperfection survives a "premium" calibration so restraint reads as intent, not emptiness

## Creative Latitude

The calibration matrix is a starting prescription, not a formula to fill in — the craft is in the specific FROM→TO values chosen for this asset's actual content, and in recognizing when the brief calls for a target the matrix doesn't cleanly cover (a fifth feeling word extending the canonical four). Push the target as far as the audience-fit veto allows rather than settling for a timid, half-committed calibration — a "premium" pass that's only slightly more premium than the original hasn't earned the label.

## Deploy When

The content is locked and correct but the feel is wrong for the target; you need to move an asset up- or down-market without touching the offer/copy/price; a client says "make it feel more expensive/approachable/fun" and needs that converted into concrete moves; or you're producing two versions of the same asset for different tiers. Do not use when the content itself is the problem (fix with the Why-Before-What Rent Test Audit first), when there's no fixed audience yet, or at concept/sketch stage before the primitive and leverage point are locked.
