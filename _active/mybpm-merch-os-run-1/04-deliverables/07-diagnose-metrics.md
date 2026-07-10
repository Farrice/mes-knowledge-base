# Phase 6 — DIAGNOSE: MyBPM Factory Loop (6 Metrics + Ongoing Cadence)

> Install 6-metric instrumentation post-launch. Monitor daily for Week 1, weekly for Month 1, then monthly. Pre-committed kill/scale rules operational.

---

## 6-Metric Instrumentation

### Core Metrics (Direct Revenue Signals)

#### Metric 1: Add-to-Cart Rate (% of Email Opens)

**What it measures:** Recognition speed + copy resonance. High rate = the moment lands instantly; low rate = concept needs clarification.

**Formula:**
```
Add-to-Cart Rate = (Total Add-to-Carts) / (Email Opens) × 100%
```

**Tracking:**
- Shopify GA4: Custom event "add_to_cart" tagged per product
- Email platform: Open count (Klaviyo or Mailchimp)
- Daily review: Are all three SKUs hitting ≥8%? Which is highest?

**Target per SKU:**
- Still Synced: ≥8% (recognition speed champion)
- Sunday/Monday: ≥9% (outside-scene legibility)
- Resting Heart Rate: ≥7% (family complexity)

**Red flag:** If any SKU <5% → the concept isn't landing; revise PDP copy or test new segment.

---

#### Metric 2: Revenue Per Concept (First Week, Week 2, Week 3)

**What it measures:** Concept strength (holds intent → completes purchase). Revenue is the final vote.

**Formula:**
```
Revenue Per Concept = (Total Purchase $ SKU-specific) / (Days since launch)
```

**Tracking:**
- Shopify revenue report (filter by SKU: MYBPM-SYNCED-001, MYBPM-SUNDAY-001, MYBPM-RHR-*)
- Weekly snapshot (Mon, Mon+7, Mon+14)
- Raw total: Do not discount by email list size; pure revenue signal

**Target per SKU:**
- Still Synced: ≥$150 first week (strong visual + recognition)
- Sunday/Monday: ≥$150 first week (highest composite score, easiest design)
- Resting Heart Rate family: ≥$200 first week (5 variants, should capture genre-specific buyers)

**Red flag:** If any SKU <$75 first week → pause, audit messaging. Concept isn't converting.

---

#### Metric 3: Average Order Value (AOV) — Single & Multi-SKU

**What it measures:** Pairing strategy effectiveness + basket expansion.

**Formula:**
```
AOV = (Total Revenue) / (Total Orders)
Single-SKU AOV = (Revenue from 1-SKU orders) / (1-SKU order count)
Multi-SKU AOV = (Revenue from 2+ SKU orders) / (Multi-SKU order count)
```

**Tracking:**
- Shopify order data: Manual count or GA4 "purchase" event with item quantity
- Weekly snapshot: What % of orders are multi-SKU?
- Target: >20% multi-SKU orders (the pairing works)

**Target:**
- Single-SKU AOV: $45 (expected; one shirt)
- Multi-SKU AOV: ≥$85 (two shirts + shipping justifies expansion)
- Multi-SKU % of orders: ≥20% (pairing strategy is working)

**Red flag:** If multi-SKU <15% → the "Complete the Moment" recommendation isn't landing; boost visibility on PDPs.

---

### Engagement Metrics (Validation Signals)

#### Metric 4: Email Engagement (Open Rate, CTR, Unsubscribe)

**What it measures:** Hypothesis validation (emotion-first framing works). Open rate vs. baseline shows if the lead-line lands.

**Formula:**
```
Open Rate = (Unique Opens) / (Delivered) × 100%
CTR = (Unique Clicks) / (Unique Opens) × 100%
Unsubscribe Rate = (Unsubscribes) / (Delivered) × 100%
```

**Tracking:**
- Email platform native reporting (Klaviyo, Mailchimp, ConvertKit)
- Snapshot at 24 hours, 72 hours, 7 days post-send
- Compare to MyBPM baseline (24% open, 8% CTR)

**Target:**
- Open rate: ≥24% (match baseline; emotion-first hypothesis holds)
- CTR: ≥9% (beat baseline; copy is resonating)
- Unsubscribe: <0.5% (topic isn't alienating)

**Green flag:** If open >28%, CTR >11% → emotion-first subject line can be replicated; use for future runs.

---

#### Metric 5: Social Sharing & Organic Mention (Qualitative + Quantitative)

**What it measures:** Concept strength (buyers want to broadcast it). Organic reach = confidence in the moment.

**Formula:**
```
Organic Mentions = (Instagram tags with #MyBPMBetweenRaves) + (TikTok mentions) + (Reddit/Discord group chat screenshots)
Sentiment = % positive mentions (aspirational, funny, "this is me") vs. negative (confused, disappointed)
```

**Tracking:**
- Weekly hashtag search: #MyBPMBetweenRaves
- Group chat monitoring (via Farrice or community Discord if exists)
- Set Google Alert for "MyBPM" + "Sunday" OR "Synced" OR "Resting Heart Rate"
- Qualitative note: *Why* are they sharing? Recognition ("this is me")? Funny? Gift signal?

**Target:**
- ≥5 organic mentions by end of Week 2 (proof the moment resonates outside email)
- ≥70% sentiment positive (aspirational, not aspirational-but-confused)

**Green flag:** If mentions trend toward "this is exactly me" + tagged friends → concept is *working*. Leaning into UGC for Wave 2.

---

#### Metric 6: Bounce Rate & Return/Refund Rate (Satisfaction Proxy)

**What it measures:** Design quality + expectation match. Returns = the shirt didn't land emotionally or physically.

**Formula:**
```
Return Rate = (Returned Items) / (Shipped Items) × 100%
Bounce Rate = (Visitors to PDP who leave without action) / (PDP visits) × 100%
```

**Tracking:**
- Shopify returns dashboard (track by SKU)
- GA4 exit page analysis (which PDPs have high bounce?)
- Track reason for return (fit? design didn't match? buyer's remorse?)

**Target:**
- Return rate: <5% (industry standard for POD apparel is 8–10%; aiming for premium)
- Bounce rate: <40% (copy is clear enough to hold attention)

**Red flag:** If return rate >10% → design didn't match expectations; revise mockups or add fit notes to PDP.

---

## Monitoring Dashboard (Notion Template)

Create a simple Notion table:

| Date | Synced Revenue | Synced ATC | Sunday Revenue | Sunday ATC | RHR Revenue | RHR ATC | Email Open | Email CTR | Organic Mentions | Notes |
|------|---|---|---|---|---|---|---|---|---|---|
| Mon | $45 | 2 | $90 | 4 | $135 | 3 | 28% | 10% | 1 | First day; strong momentum |
| Tue | $90 | 4 | $65 | 3 | $90 | 2 | — | — | 2 | Sunday slowing; continue monitoring |
| Wed | $60 | 2 | $45 | 2 | $120 | 2 | — | — | 1 | RHR maintaining; consider paid test Wed PM |
| Thu | $75 | 3 | $50 | 2 | $100 | 2 | — | — | 2 | Synced recovering; end-of-week sentiment check |
| Fri | $80 | 3 | $60 | 2 | $110 | 2 | — | — | 3 | Friday lift (weekend energy)? |
| **Week 1 Total** | **$350** | **14** | **$310** | **13** | **$555** | **11** | **28%** | **10%** | **9** | **ON TRACK** |

**Weekly Snapshot (Fri 5 PM):**
- Total revenue: $1,215 (target: ≥$450, hit ✓)
- Best performer: RHR ($555 = 45% of total)
- Email engagement: Open 28% (beat baseline +4%), CTR 10% (beat baseline +2%)
- Organic: 9 mentions by end of week (target ≥5, hit ✓)

---

## Factory Loop: Ongoing Cadence (Month 1+)

### Week 1: Daily Monitoring (24-Hour Response Window)

**Every morning (9 AM):**
- Check overnight revenue + add-to-cart counts
- Review Shopify notifications (new orders, returns, customer feedback)
- Quick scan of Instagram/TikTok for mentions
- Decision point: If red flag detected, email Farrice immediately (don't wait for weekly)

**Every Friday 5 PM:**
- Full metric review (6 metrics + notes)
- Summary decision: Continue? Scale? Revise?
- Communicate decision to team (Satori, Shopify, email platform)

### Week 2–4: Weekly Monitoring (Thursday Review)

**Every Thursday:**
- Revenue trend analysis (is momentum building or declining?)
- Email segment performance (warm vs. cold if tested)
- Organic mention qualitative review (what are people saying?)
- Action decision: Prepare Wave 2? Adjust messaging? Allocate paid budget?

### Month 2+: Monthly Review + Factory Loop Adjustments

**First Monday of each month:**
- Full quarter-to-date analysis
- Concept performance ranking (which concepts are carrying the brand?)
- Seasonal trend analysis (which moments resonate when?)
- Product roadmap update: What concepts work enough to ship? What needs revision?

---

## Pre-Committed Kill/Scale Rules (Operational)

### Immediate Kill (Stop the Test)

| Condition | Action | Timeline |
|-----------|--------|----------|
| **Any SKU <$75 first week** | Pause SKU (remove from Shopify). Audit PDP copy. Re-test with holdout segment. | Within 48 hours of detection |
| **Email open rate <15%** | Subject line failed. Re-test with emotion-forward variant. | Immediately (re-send to 20% holdout) |
| **Checkout abandonment >45%** | Price/shipping objection suspected. Lower price to $40, re-test. | Within 24 hours |
| **Return rate >10%** | Design or fit issue. Pause production; audit returns reason. | Within 7 days of first returns |
| **Technical failure** | Fix first. Then re-launch. Not a concept failure. | Immediate |

### Revise (Adjust, Don't Kill)

| Condition | Action | Timeline |
|-----------|--------|----------|
| **Revenue $75–150 per SKU** | PDP copy isn't landing. Rewrite emotion-first lead (top 3 lines). | Within 5 days |
| **Email open 18–23%** | Close to baseline but not beating it. Add storytelling depth to subject line. | Next email send (holdout segment) |
| **Organic mentions 1–4** | Low social reach. Create TikTok video of the moment (co-worker recognition for Sunday/Monday). | Within 14 days |
| **Multi-SKU <15%** | Pairing strategy not visible. Feature "Complete the Moment" bundle on PDPs. | Within 7 days |

### Scale (Double Down)

| Condition | Action | Timeline |
|-----------|--------|----------|
| **Email open ≥30%** | Emotion-first hypothesis confirmed. Allocate $100 paid ad budget to cold traffic. | Immediately |
| **Email CTR ≥12%** | Copy resonating hard. Test new subject lines on this theme. | Next email send |
| **First-week revenue ≥$500 per SKU** | All three concepts are strong. Plan Capsule 1 Wave 2 (5 more concepts). | Within 7 days |
| **AOV >$90** | Pairing works. Create "Bundle Discount" ($40 off 2-pack) for Wave 2. | Within 14 days |
| **Organic mentions ≥7** | Concept is resonating. Invest in UGC (re-post customer photos, create "Moment Spotlights" series). | Ongoing |

---

## Sample Week 1 Monitoring (Hypothetical Success Scenario)

### Daily Logs

**Monday (Launch Day)**
```
9 AM: Email sends. Open tracking begins.
3 PM (6 hours post-send): 12% open, 9% CTR (on pace for 30%+ open)
   → Good emotional hook. Continue monitoring.

7 PM: Revenue snapshot: $45 (Still Synced) + $90 (Sunday/Monday) + $135 (RHR) = $270 same-day
   → Strong start. POD orders processing within expected window.
```

**Tuesday**
```
9 AM: Overnight revenue: $90 (revenue up). Email open now 24% (still climbing, good).
   → Organic mention #1: Instagram DM from customer: "this is literally me on Tuesday mornings"
   
5 PM: Weekend is approaching; momentum expected to dip. Observation: RHR (Dubstep) is strongest performer.
   → Decision: Plan for Wed afternoon content push (TikTok teaser for Sunday/Monday moment).
```

**Wednesday**
```
9 AM: Email open 28% (beat baseline by 4%). CTR 10% (beat baseline by 2%).
   → Hypothesis validated. Emotion-first subject line is working.
   
Revenue: $60 (Synced) + $45 (Sunday) + $120 (RHR). Weekly trend shows RHR maintaining lead.
   → Decision: For Wave 2, prioritize genre-tribal positioning (Resting Heart Rate was the AOV driver).
```

**Thursday**
```
9 AM: Organic mentions now #3, #4 (Reddit/Discord group chat screenshots).
   Sentiment: 100% positive ("This is so me", "Tag everyone", gift signals).
   → Recommendation: Feature UGC early. Re-post customer mentions in MyBPM Stories.

Revenue: $75 (Synced recovering) + $50 (Sunday holding) + $110 (RHR stable).
```

**Friday 5 PM (Weekly Snapshot)**
```
WEEK 1 TOTALS:
- Revenue per SKU: Synced $350, Sunday $310, RHR $555
- Email open: 28% (beat baseline ✓)
- Email CTR: 10% (beat baseline ✓)
- Organic mentions: 9 (exceed target ✓)
- AOV: $92 (multi-SKU pairing working ✓)
- Add-to-cart rate: Synced 8%, Sunday 9%, RHR 7.5% (all on target ✓)

DECISION: All metrics GREEN. Scale immediately.
ACTION PLAN for Week 2:
1. Launch Capsule 1 Wave 2 (5 concepts) in 5–7 days
2. Allocate $100 paid ad budget to cold traffic (Sunday/Monday + Resting Heart Rate)
3. Begin UGC feature series (#MyBPMBetweenRaves customer spotlights)
4. Prepare Josh's swing-nerd brand Run 1 (same /merch-os system, different niche)
```

---

## Factory Loop Template (Repeating Monthly)

### Monthly Factory Loop (1st Monday)

**Metrics Review:**
- [ ] Last 30 days revenue per concept
- [ ] YoY comparison (if applicable)
- [ ] Email engagement trend (are opens declining? Are subjects losing novelty?)
- [ ] Organic mention trend
- [ ] Seasonal factor: Which moments peak when? (e.g., does "Post-Rave Tuesday" spike after weekends?)

**Concept Performance Ranking (What's Working?):**
1. Best performer: _______ (revenue, organic mentions, AOV impact)
2. Strong secondary: _______
3. Needs revision: _______
4. Wave 2 candidate: _______

**Roadmap Decision:**
- Which concepts graduate from "test" to "permanent SKU"?
- Which concepts are ready for paid ad spend?
- Which concepts need design revision before Wave 2?

**Resource Allocation:**
- Budget for next wave (concepts to produce)
- Design priority (which briefs to send Satori next)
- Email cadence (how often to announce new drops without fatigue)

---

## Success Case Study (Target: Month 1 Wrap-Up)

**If all metrics hit GREEN:**

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| First-week revenue per SKU | ≥$150 | $350–$555 | ✓ EXCEED |
| Email open rate | ≥24% | 28% | ✓ BEAT |
| Email CTR | ≥9% | 10% | ✓ BEAT |
| Multi-SKU orders | ≥20% | 23% | ✓ BEAT |
| Organic mentions | ≥5 | 9+ | ✓ EXCEED |
| Return rate | <5% | 3.2% | ✓ PASS |

**Narrative:** MyBPM test validates /merch-os system. Emotion-first, behavioral-mirror concepts outperform traditional identity messaging by +4% email open, +2% CTR, +18% AOV. System ready for Josh's swing-nerd brand Run 1.

