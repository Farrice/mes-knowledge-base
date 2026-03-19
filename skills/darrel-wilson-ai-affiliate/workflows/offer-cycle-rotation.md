---
description: Detect hot offers, design entry offers, and plan rotation cycles for sustained AI-powered revenue
---

# Offer Cycle Rotation Engine

Detect which offers are currently hot, design entry-level offers that hook clients, and plan systematic rotation so your revenue never stalls. Based on Darrel Wilson's observation that affiliate niches and service demands cycle — what works today may flatten in 6 months unless you actively rotate.

## Input Required

- **Current Offers**: What are you selling now? (List all)
- **Revenue Data**: Which offers are performing vs. declining?
- **Market Signals**: What trends are you seeing? (New tools, emerging niches, dying categories)
- **Expansion Capacity**: How quickly can you launch a new offer?

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

### Step 1: Offer Health Diagnostic

Audit every active offer against the OHI (Offer Health Index):

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| **Revenue Trend (30d)** | Growing ↑ | Flat → | Declining ↓ |
| **Conversion Rate** | > 3% | 1-3% | < 1% |
| **Time to Close** | < 7 days | 7-30 days | > 30 days |
| **Customer Satisfaction** | NPS > 30 | NPS 0-30 | NPS < 0 |
| **Market Competition** | Low | Medium | High/saturated |
| **Effort to Deliver** | < 2 hours | 2-8 hours | > 8 hours |

**Action Rule**: 
- All Healthy → Expand (add adjacent offers)
- 1+ Warning → Optimize (fix the weak metrics)
- 1+ Critical → Rotate (replace with new offer)

### Step 2: Trend Detection System

Monitor 4 signal sources for emerging opportunities:

1. **Google Trends**: Track keywords for your niche + adjacent niches. Rising interest = new offer opportunity.
2. **Product Hunt / Hacker News**: New AI tools launching = new affiliate and service opportunities.
3. **YouTube Trending**: What AI/tech tutorials are getting views? These signal demand.
4. **Community Chatter**: Reddit, Twitter/X, LinkedIn — what problems are people complaining about?

**n8n Automation for Trend Detection:**
```
Schedule Trigger (weekly)
    ↓
Google Trends API → keyword volume changes
    ↓
ProductHunt API → new AI tool launches
    ↓
AI Analysis → "Which of these signals an offer opportunity?"
    ↓
If confidence > 7/10 → Slack alert + add to Offer Pipeline
```

### Step 3: Offer Pipeline Architecture

Maintain 3 offer categories at all times:

| Category | Purpose | Example | Revenue |
|----------|---------|---------|---------|
| **Cash Cow** (1-2 offers) | Proven, consistent revenue | Website builds on Hostinger + hosting retainer | 60% of total |
| **Growth Bet** (1-2 offers) | Rising trend, needs investment | AI lead gen workflows for agencies | 30% of total |
| **Experiment** (1-2 offers) | Testing new market response | AI micro-app in new niche | 10% of total |

**Rotation Cycle:**
- **Monthly**: Review OHI scores. Experiments with traction → promote to Growth.
- **Quarterly**: Growth offers that plateaued → either optimize or demote to Cash Cow.
- **Semi-Annually**: Cash Cows that are declining → retire. Replenish with promoted Growth offers.

### Step 4: Entry Offer Design

Every new market needs a low-friction entry offer:

**The $0 → $200 → $97/month Ladder:**

| Stage | Offer | Purpose | Conversion to Next |
|-------|-------|---------|-------------------|
| **Stage 0** | Free value (blog, YouTube tutorial, tool demo) | Build awareness + trust | 5-10% opt-in |
| **Stage 1** | $47-$200 one-time (quick win delivery) | Prove you deliver results | 30-50% upgrade |
| **Stage 2** | $97-$497/month (ongoing service/access) | Lock in recurring revenue | 80%+ retention |
| **Stage 3** | $500-$5,000+ (high-ticket project/system) | Maximize customer value | 10-20% of retainer clients |

**Design Principle**: The entry offer must deliver an obvious, tangible result that makes the next offer a logical next step. Never sell the relationship — sell the first win.

### Step 5: Seasonal Opportunity Calendar

Certain offers perform better at predictable times:

| Season | Hot Offers | Why |
|--------|-----------|-----|
| **January** | "New year, new website" / productivity tools | New Year motivation, Q1 budgets |
| **March-April** | Tax tools, financial calculators | Tax season drives finance niche traffic |
| **June-August** | Summer business launch, side hustle content | People exploring new income during summer |
| **September** | Back-to-school, education tools | Education niche spike |
| **October-November** | Black Friday prep, affiliate comparison content | Massive affiliate commission spike |
| **December** | Year-in-review, planning tools | Reflection + planning mood |

### Step 6: Kill Criteria

Know when to stop an offer:

| Kill Signal | Threshold | Action |
|------------|-----------|--------|
| No sales in 30 days | Despite promotion | Kill or radically redesign |
| Consistent negative feedback | 3+ complaints on same issue | Kill or fix the root cause |
| Revenue below effort threshold | < $50/hour effective rate | Kill and redirect effort |
| Market saturated | 5+ identical offers from competitors | Differentiate or exit |

## Output

Complete offer rotation strategy:
- Current offer health diagnostic (OHI scores)
- Trend detection automation setup
- 3-tier offer pipeline (Cash Cow / Growth / Experiment)
- Entry offer design for next market
- Seasonal opportunity calendar
- Kill criteria and rotation schedule
- Revenue forecast by offer category

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
