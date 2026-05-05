# Reference — Meta Andromeda Mechanics (Operational)

> Reference loaded by any workflow that touches Meta paid ads. Standalone — link from workflow instead of repeating.

---

## What Andromeda Is

Meta's algorithm update (rolled out 2024, deepening through 2025) that fundamentally changed how ads are classified, served, and budget-allocated. Two main mechanisms:

### 1. Entity ID Classification

Meta categorizes every ad on its platform by an **Entity ID** — a fingerprint that groups conceptually-similar ads together regardless of which advertiser made them or surface differences (color, copy variation, image angle).

**Operational reality**: 10 ads with the same product on the same background with the same offer in the corner — even with different colors and slightly different copy — get grouped under ONE Entity ID. Meta then treats them as ONE ad, competing against itself for one ad slot.

**The Vacation Test maps directly**: if a viewer who saw Ad A a week ago thinks "I've seen this" when shown Ad B, those two ads share an Entity ID. Meta has the same intuition the viewer does.

### 2. Creative ID

Each individual ad still has its own **Creative ID**, but Creative ID matters less than Entity ID for spend decisions. Two ads with different Creative IDs but the same Entity ID = treated as one for serving decisions.

---

## The Economic Logic Underneath

**Why Meta cares about diversity**: not because they "prefer variety" (they don't have aesthetic preferences). Because:
- Meta makes money when advertisers spend money.
- Advertisers spend more when ads convert.
- Ads convert when viewers don't skip the ad slot.
- Viewers skip slots when they've already seen the ad.
- Therefore: Meta serves diverse ads to keep slot value high → keeps advertiser spend high → keeps Meta revenue high.

**Implication**: Frame diversity as "what makes a viewer not skip the next slot" — not "what Meta wants." If you frame it as Meta-pleasing, you over-optimize on metadata. If you frame it as viewer-fatigue-avoidance, you naturally pass the Entity ID classifier.

---

## What Changed With Andromeda's Auto-Targeting

Andromeda also massively improved Meta's media-buying algorithm. Practical effect:
- You can now ship an ad with no audience targeting and Meta's algorithm will find an audience by scanning the copy + creative.
- This makes media-buying easier (the algorithm does more) but makes creative quality MORE important (because there's nothing else to differentiate on).
- "Just give it the ad and run it" is increasingly viable for sufficiently diverse, high-quality creative.

---

## The Budget-Not-Spending Pathology

Common symptom: client has a $10K/day budget cap; daily spend is $1,500.

**Diagnosis**: Meta has decided your ads aren't going to perform well enough to justify the slot value. So Meta declines to spend the budget — protecting its own slot economics by giving the slot to an advertiser more likely to drive engagement.

**Almost always the cause**: low Entity ID diversity. The whole ad set is grouped as one entity, Meta has data on that entity's underperformance, refuses to spend.

**Fix**: not "increase budget cap" or "refresh creative" — rebuild the test set at the FUNDAMENTAL diversity layer (Idea, Style, Hook all distinct), not the surface layer.

---

## The Operational Diagnostic — Vacation Test

The single highest-signal field test for Andromeda compliance:

1. Pull last 10 ads from the account.
2. For each pair of consecutive ads, ask: "If a viewer saw Ad A a week ago and is now shown Ad B, would they think 'I've seen this' or 'this is new'?"
3. Count "I've seen this" answers. Each one is an Entity ID grouping.
4. If 3+ pairs are "I've seen this," the account has a fundamental diversity problem regardless of how many ads are shipping.

**Pass condition**: across 10 ads, a viewer can recall each as a distinct experience.

---

## Diversity Layers (in order of impact)

| Layer | Example variation | Andromeda impact |
|---|---|---|
| **Idea** (what is being said) | "headaches?" → "nosebleeds?" → "neck stiffness?" | High — different Entity ID |
| **Style** (how it's communicated) | Static image → UGC → founder-to-camera → versus-format | High — different Entity ID |
| **Hook** (first 2-3 seconds) | Same idea & style, different opening seconds | Medium — sometimes different Entity ID |
| **Offer / Price** | $19 → $29 → bundle | Medium |
| **Color / background** | Green → blue → yellow | **Zero** — same Entity ID |
| **Copy line tweak** | "Save $10" → "$10 off" | **Zero** — same Entity ID |
| **Image angle** | Front → 3/4 → side | **Zero** — same Entity ID |

**Rule**: real diversification happens at Idea, Style, or Hook. Surface variation does NOT escape Entity ID grouping.

---

## What Brand-Side People Don't Know (Almost Universally)

Per Alex's experience inside Meta's "Creative Strategy Camp":
- ~80% of DTC brands have a fundamental diversity problem they can't see.
- Most "we run lots of ads" accounts are running 1-3 entities × many surface variants.
- Most agencies that report "we shipped 30 ads this month" shipped 30 surface-variants of 4 entities.

**Implication for Farrice**: walking into a client account with a Vacation Test diagnostic + Andromeda Audit + Content Grid rebuild plan is a huge wedge. The client doesn't know what they don't know; the diagnostic reveals it; the rebuild is the engagement.

---

## Useful Pre-Briefing Checklist (per ad)

Before any ad goes into production, the brief specifies:

- [ ] **Idea** — what message is this ad making? (1 sentence)
- [ ] **Style** — what format/genre is it? (UGC, founder, expose, versus, narrated, doctor-interview, etc.)
- [ ] **Hook** — what are the first 2-3 seconds? Which of the 5 hook types?
- [ ] **Avatar** — which test-specific Avatar is this for?
- [ ] **Andromeda Entity ID intent** — explicitly: is this ad designed to share an Entity ID with anything else in the test? (Should usually be NO.)
- [ ] **Vacation Test pre-check** — would a viewer who saw any other ad in this batch recognize this as "different" or "same"?

---

## Sources & Caveats

- Alex's Andromeda intelligence comes from being inside Meta's "Creative Strategy Camp" 2024-25 — Meta's own training program for creative strategists, where they explained the algorithm reasoning. This is closer to primary-source intelligence than most public Andromeda content.
- The exact technical naming ("Entity ID" vs other internal Meta terms) may have shifted. The MECHANISM (similar-ad grouping with budget consequences) is stable and verified.
- Andromeda continues to evolve. Check Meta's developer/business announcements quarterly for material algorithm changes.
