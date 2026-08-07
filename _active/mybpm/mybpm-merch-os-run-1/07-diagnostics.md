# Phase 5 — DIAGNOSTICS (Metrics Instrumentation)

**Purpose**: Install the instruments BEFORE you need them. Know which 6 numbers matter, what healthy looks like, and the pre-committed kill/scale rules so taste can't veto data later.

**Cadence**: Weekly (every Monday morning, same time). 30-minute review.

**Ownership**: Farrice (decision-maker on kill/scale verdicts).

---

## The 6-Metric Dashboard (Weekly Tracking)

Per Meg Heckman's Layer 4 (DIAGNOSTICS) framework:

| Metric | Healthy | The One Question | Weak? Fix THIS Stage |
|---|---|---|---|
| **CPC** | $0.55–0.75 | Does this creative stop people? | Mockup/presentation FIRST, targeting second |
| **ROAS** | 2.5–3.5 scale; 2.0 = floor | Dollars back per dollar spent? | Usually a Shopify conversion problem in disguise (not Meta) |
| **ATC %** | 7–8% | Do they actually want it? | Images, description, price, mobile CTA position |
| **IC % (Initiate Checkout)** | 5–6% | Does this store feel trustworthy? | Cart-page trust: shipping clarity, returns, reviews |
| **CVR % (Conversion)** | 3–4% | How easy is it to buy? | Checkout friction, load speed, payment options, mobile |
| **AOV** | $45+ | Profit per order? | Collection cohesion + shipping arbitrage (DON'T use upsell apps yet) |

**Calculation helpers** (if tracking in Shopify):
- CPC = Total Ad Spend / Total Clicks (from Meta Ads Manager)
- ROAS = Revenue / Ad Spend (Meta or Shopify Ads dashboard)
- ATC = (Add-to-Cart Events / Total Sessions) × 100
- IC = (Checkout Initiated / Add-to-Cart) × 100
- CVR = (Orders / Checkout Initiated) × 100
- AOV = Total Revenue / Total Orders

---

## Weekly Review Template (Monday, 9 AM)

**Copy-paste and fill in each Monday:**

```
# MyBPM Merch OS — Week [X] Diagnostic

**Week of**: [Date]
**Products in test**: The Kandi Keeper, Stranger-to-Friend, Sunrise Survivor
**Ad spend (week)**: $[X]
**Total revenue (week)**: $[X]

## Metric Review

| Metric | Target | Actual | Status | Note |
|---|---|---|---|---|
| CPC | $0.55–$0.75 | $[X] | 🟢/🟡/🔴 | |
| ROAS | 2.5+ | [X] | 🟢/🟡/🔴 | |
| ATC % | 7–8% | [X]% | 🟢/🟡/🔴 | |
| IC % | 5–6% | [X]% | 🟢/🟡/🔴 | |
| CVR % | 3–4% | [X]% | 🟢/🟡/🔴 | |
| AOV | $45+ | $[X] | 🟢/🟡/🔴 | |

## Diagnosis

**CPC issue?** → [Yes/No] Fix: [Mockup swap / audience refinement / placement test]
**ROAS issue?** → [Yes/No] Fix: [Shopify analytics audit / checkout flow test / pricing test]
**ATC issue?** → [Yes/No] Fix: [Product image swap / description rewrite / mobile CTA position]
**IC issue?** → [Yes/No] Fix: [Add shipping clarity / show reviews / add return policy link]
**CVR issue?** → [Yes/No] Fix: [Reduce form friction / add payment options / mobile load test]
**AOV issue?** → [Yes/No] Fix: [Collection cohesion / bundling ideas / shipping arbitrage test]

## Action Items (Next Week)

1. [Debug or scale action]
2. [If test continues: debug + continue OR if test ends: kill + launch new Phase 1]
3. [Document learning]

## Verdict

- **Continue testing?** [Yes/No]
- **Scale spend?** [Yes/No → increase to $[X] if yes]
- **Kill design?** [Yes/No → which design, why]
- **Launch new Phase 1?** [Yes/No]

**Notes**: [Any observations about the market, the person, the product?]

---
```

---

## Pre-Committed Kill/Scale Rules (Non-Negotiable)

**These rules are decided NOW, before emotion enters.**

### SCALE Triggers (increase daily ad budget by 2x)
1. **ROAS ≥ 2.5** AND **ATC ≥ 7%** AND **CVR ≥ 3%** → Scale spend. Increase daily budget. Run for 21 days.
2. **AOV > $50** with any design → Increase budget on that design; test collection bundling.

### REVISE Triggers (optimize before killing)
1. **ROAS 2.0–2.5** (break-even range) → Mockup swap OR email-announce refresh. One test cycle (3 days), then reassess.
2. **ATC < 7%** but ROAS ≥ 2.0 → Product page issue. Revise images, description, or mobile CTA. Retest.
3. **IC < 5%** → Trust issue on cart page. Add shipping info, show reviews, clarify returns. Retest.

### KILL Triggers (end immediately, no second-guessing)
1. **ROAS < 2.0** after $100 spend across all designs → Hypothesis wrong or execution broken. KILL all three. Return to Phase 0 (GROUND).
2. **Zero ATC across all 3 designs** after 7 days → No one wants to buy. Design or person wrong. KILL and return to Phase 1 (CONCEPT).
3. **IC < 4%** after cart-page trust revisions → Store fundamentals broken (checkout speed, payment options, trust signals). KILL test until Shopify backend fixed.
4. **CPC > $1.50** after audience refinement → Targeting wrong. KILL ads. Revise audience. Restart with fresh daily budget.

**No exceptions to these rules.** Data > Taste. When a kill rule fires, execute it same day.

---

## The Factory Loop (Post-Test, if Winning Design Found)

If the test produces a **LEAD** design (ROAS 2.5+, ATC 7%+, CVR 3%+):

1. **Keep that design LIVE** on the collection (don't archive it).
2. **Scale ad spend** to $500/week for 21 days (proven model).
3. **Run Phase 1 again** (new 12 concepts, different angles on the same person).
4. **Score Phase 1 output** (Phase 2).
5. **Launch 3 new designs** (Phase 3–4) to test diversity.
6. **Continue 6-metric cadence** (weekly, same rules).

This is the **5-step loop** (Meg's Layer 3 mechanics):
- Generate (Phase 1: 12 concepts)
- Test (Phase 3–4: 3 designs)
- Scale or cut (Phase 5: data verdict)
- Email (to the list: announce winners)
- Repeat

**Scale rule at MyBPM**: When a design hits $2K+ in revenue in one month, move it to a permanent collection. Don't cycle it out.

---

## Weekly Check-In Cadence (Calendar)

| Day | Task | Owner | Duration |
|---|---|---|---|
| **Monday, 9 AM** | Metrics review + diagnosis | Farrice | 30 min |
| **Tue–Thu** | Execute debug action (mockup swap, copy rewrite, etc.) | Farrice or designer | 2–4 hours |
| **Friday** | Ad performance check-in (if ROAS trending down, prep kill decision) | Farrice | 15 min |
| **Week 2** | Reassess kill/scale trigger status | Farrice | 10 min |

---

## Grounding Rule (Layer 4 Discipline)

**All 6-metric thresholds are POD/Meta 2026 defaults, not laws.**

- Recalibrate after 4 weeks of data (does your list, audience, or category perform different than Meg's calibration?)
- If your thresholds shift, document the change. (e.g., "MyBPM list has 15% higher AOV than POD average; new healthy AOV floor = $50+")
- Never lower a threshold to justify keeping a losing design.

---

## Sample Diagnostics Report (Week 1 Example)

```
# MyBPM Merch OS — Week 1 Diagnostic

**Week of**: July 1–7, 2026
**Products in test**: The Kandi Keeper, Stranger-to-Friend, Sunrise Survivor
**Ad spend (week)**: $150
**Total revenue (week)**: $340

## Metric Review

| Metric | Target | Actual | Status | Note |
|---|---|---|---|---|
| CPC | $0.55–$0.75 | $0.62 | 🟢 | Perfect |
| ROAS | 2.5+ | 2.27 | 🟡 | Close to scale trigger |
| ATC % | 7–8% | 8.3% | 🟢 | Strong |
| IC % | 5–6% | 5.8% | 🟢 | Solid |
| CVR % | 3–4% | 3.1% | 🟢 | Healthy |
| AOV | $45+ | $48.50 | 🟢 | Good |

## Diagnosis

All metrics healthy except ROAS (just below scale trigger). Strong ATC + good CVR suggest the products resonate. The 2.27 ROAS is likely due to small sample size (week 1). Continue test, increase spend to $250 next week to gather signal.

## Action Items

1. Increase daily ad budget from $20 to $35 (Mon, July 8).
2. A/B test email open rate: subject line "Which PLUR Soul design?" vs. current next send.
3. Monitor CPC (if it rises above $0.85, mockup swap).

## Verdict

- **Continue testing?** Yes
- **Scale spend?** To $250/week for next cycle
- **Kill design?** No
- **Launch new Phase 1?** No (too early; get 2 weeks of data first)

**Notes**: The Stranger-to-Friend and Sunrise Survivor designs are tracking slightly ahead of The Kandi Keeper (ROAS 2.4 vs. 2.1). This is small sample size, but worth watching. Week 2 will clarify.
```

---

## Success = Repeatable Loop

When Phase 5 (DIAGNOSTICS) is installed and the weekly cadence is running:

✓ You know which 6 numbers matter
✓ You know what healthy looks like
✓ You have pre-committed rules (no opinion, just data)
✓ You can run the 5-step loop repeatedly (generate → test → scale/kill → email → repeat)
✓ **The OS is self-reinforcing**: each cycle produces better designs because you're learning from the market

**This is the Meg Heckman operating system in full production.**

---

