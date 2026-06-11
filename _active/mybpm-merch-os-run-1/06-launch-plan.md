# Phase 4 — LAUNCH PLAN

Channel: Shopify (existing store: mybpm.store)

---

## Test Strategy (Smallest Honest Test First)

**Doctrine**: Find one shirt people actually want, not build a whole brand yet. (Josh V1 principle)

**Test slate**: 3 LEAD designs (Phase 2 scorecards ≥4.8)
- **Design 1**: The Kandi Keeper (5.0) — highest-confidence LEAD
- **Design 2**: Stranger-to-Friend (5.0) — tied highest
- **Design 3**: Sunrise Survivor (4.8) — third strongest

**Why 3**: Hits different identity angles; allows portfolio cohesion test (do people buy 2+ from the slate?); minimal SKU complexity.

**Timeline**: 14 days (July 1–14, 2026)

**Budget floor**: $200 Meta Ads spend (test velocity; can scale if ROAS ≥ 2.5)

**Success criteria**: 
- ≥1 design hits ROAS 2.5+ (scale trigger)
- ≥1 design hits ATC 7%+ (product resonance proof)
- ≥3 sales total across the slate (demand signal)

**Kill criteria**:
- ROAS < 2.0 across all three after $200 spend (market doesn't care)
- Zero multi-buys (portfolio doesn't cohere)
- ATC < 5% across slate (description/mockup problem)

---

## Collection Architecture (Shopify Product Placement)

**New collection**: "PLUR Soul" (or "Raver Identity" — finalize per brand feel)

**Why a collection, not a campaign**?
- Easier A/B testing on the store itself (mockup swaps, copy edits, price tests)
- Builds portfolio for AOV stacking (multi-buy in same checkout)
- Lays foundation for catalog cohesion (per Meg's AOV framework: "shipping arbitrage via catalog coherence, not upsell funnels")

**Collection structure**:

```
/collections/plur-soul/
├── Product 1: The Kandi Keeper
├── Product 2: Stranger-to-Friend
└── Product 3: Sunrise Survivor
```

**Collection page copy** (short):
- **Headline**: "PLUR Soul — Raver Identity Tees"
- **Body**: "Three designs for ravers who know: it's not about the party. It's about the person you become. The people you find. The commitment you make."
- **CTA**: "Pick the one that's yours."

**Product page structure** (per Phase 3 — LISTING):
- Headline + Recognition Lead (top)
- Identity + Social Moment (middle)
- Logic + Secondary CTA (bottom)
- Images: mockup (flat-lay clean), lifestyle (person wearing), close-up (text clarity)

---

## Email Announce Sequence

**Audience**: Existing MyBPM list (if <1K subscribers, this is the full reach; if larger, segment by engagement or purchase history)

**Sequence timing**:
1. **Email 1 — Launch day (Day 1)**: "We made three shirts just for you"
2. **Email 2 — Midweek (Day 4)**: "Which one are you?" (single design deep-dive)
3. **Email 3 — End of test window (Day 12)**: "Last chance" (urgency + full slate reminder)

### Email 1 Copy

**Subject**: "We made three shirts just for you"

**Body**:
```
Hey [First Name],

We just launched three new designs for the people who actually GET rave culture.

Not the party. Not the aesthetic. The FEELING.

—The Kandi Keeper (I still have your kandi)
—Stranger-to-Friend (Met strangers, found family)
—Sunrise Survivor (I walked out changed)

Each one is for a specific person. Which one is yours?

[CTA: See the collection]

Made with love (and respect),
Farrice & the MyBPM Crew

P.S. We're testing this small before we go bigger. These three are the real deal.
```

### Email 2 Copy (Day 4 — Single Design Focus)

**Subject**: "The Kandi Keeper (because you know what this means)"

**Body**:
```
We've gotten so many comments on this one.

People asking: "How did you know?"

—The answer is: we've been there. We know what kandi means. We know you still have the ones from the people who changed your life.

This shirt is for you.

[CTA: Get the Kandi Keeper]

Questions? Reply to this email. We read every message.

—MyBPM Crew
```

### Email 3 Copy (Day 12 — End of Window)

**Subject**: "Last 48 hours for the PLUR Soul collection"

**Body**:
```
These three designs are only here for 14 days.

After that, we're bringing in the ones that won. The ones you picked.

If one of these is yours—
—The Kandi Keeper
—Stranger-to-Friend
—Sunrise Survivor

—grab it before we rotate them out.

[CTA: Shop the collection]

See you at the next event.

—MyBPM
```

---

## Founder Approval Checklist (Farrice — MUST SIGN OFF)

Before design execution or launch, review and approve:

### Design Review
- [ ] **Mockup quality**: Clean, professional, POD-ready. Does the design read at 50ms? At 5 feet?
- [ ] **Text legibility**: Can someone in a crowd see and read the shirt?
- [ ] **PLUR integrity**: Does each design honor the four pillars (Peace, Love, Unity, Respect)? Would you wear it?
- [ ] **Niche resonance**: Does a raver immediately GET it without explanation?

### Copy Review
- [ ] **Listing copy**: Does it sound like you (MyBPM voice)? No generic "here's why you love raves" pablum?
- [ ] **Email copy**: Would you send this to a friend? Does it feel warm, not salesy?
- [ ] **Product descriptions**: Do they match the listing copy tone?
- [ ] **Art/IP**: Are we clear on design credits? (Artist name, if commissioned? "By Satori Graphics"?)

### Launch Logistics
- [ ] **Pricing**: [$25–32 for POD tees + shipping]; margin acceptable?
- [ ] **POD vendor**: Bonfire or Printful? Delivery time acceptable for test (2–3 week lead)?
- [ ] **Announcement timing**: Ready to send Email 1 on launch day?
- [ ] **Ad account ready**: Meta pixel installed, conversion tracking on, audience built?

### Tone Fit
- [ ] **Brand alignment**: Does this set feel like MyBPM's voice? (Show against past emails, Instagram captions, etc.)
- [ ] **Humor check**: Are we punching WITH the rave community or AT them? (If "at," kill and revise.)
- [ ] **Belonging**: Would a newer raver feel included, or does this feel gatekeeping?

**SIGN-OFF**: Farrice approves (or revision requested)

---

## 48-Hour Read Protocol (Post-Launch)

**Day 1–2 post-launch**: Track and read the market signal in real-time.

### What to Monitor (Daily)

| Metric | Healthy | Issue |
|---|---|---|
| **CPC** | $0.55–0.75 (Meg's POD default) | < $0.40 = low creative resonance; > $1.20 = targeting or placement issue |
| **ATC** | 7–8% | < 5% = product page problem (description, mockup, price) |
| **ROAS** (if ads running) | 2.5+ = scale trigger; 2.0 = break-even | < 2.0 after $50 spend = design or targeting issue |
| **Email open rate** | 25%+ (list-dependent) | < 15% = subject line or send-time issue |

### Debug Sequence (if metric weak)

1. **CPC high, ATC low?** → Mockup swap. Test different product image (lifestyle vs. flat-lay). Rerun ads. ($50 follow-up spend)
2. **ROAS < 2.0?** → Check Shopify conversion metrics (is it a cart/checkout issue, not an ad issue?). Audit: shipping clarity, reviews, mobile CTA position.
3. **Email poor open?** → Subject line might be too subtle. Consider A/B: "Which PLUR Soul design is yours?" vs current.
4. **Zero ATC across all 3?** → The person might be wrong, not the designs. Loop back to Phase 0 (GROUND) analysis; this is a diagnostic signal.

### Win Condition (Day 2)
- ≥1 product at ROAS 2.5+ OR ≥5% ATC after first $50 spend → **Confidence to continue to Day 14.**
- All metrics healthy, at least one product resonating → **Scale spend to $150+ over next 10 days.**

---

## End-of-Test Verdict (Day 14)

**After 14 days**:

| Scenario | Action |
|---|---|
| **1+ design ROAS 2.5+, ATC 7%+** | LEAD — scale this design (increase daily ad budget). Keep the other two as portfolio complements. |
| **All 3 design ROAS 2.0–2.5** | REVISE — mockup swap or email-announce refresh (the market is interested but price/presentation needs tuning). Extend test 7 days. |
| **All 3 design ROAS < 2.0** | KILL — person might be wrong. Return to Phase 0 (GROUND). Hypothesis: "Raver as Identity Keeper" needs refinement. OR designs need redesign. Do not add budget. |
| **1 design ROAS 3.5+, others < 2.0** | LEAD + KILL — run the winner at scale. Archive the others. Test new concepts Phase 1 again. |

---

## Smallest Honest Test (Final Statement)

**Do not**: Launch all 12 concepts. Build a whole brand. Run a big campaign with big assumptions.

**Do**: Run 3. Get data. Kill 2. Double-down on 1. Repeat.

This is Meg's discipline: volume at data, not taste. After the test, the leading design becomes your first "proven concept." Then Phase 1 again: 12 new concepts. Score them. Launch 3. Repeat.

---

## Success = Launch Phase 5 (DIAGNOSE)

Once test data lands, proceed to Phase 5 — set up the **6-metric weekly cadence** and the **kill/scale rules** for the winning design(s).

---

