---
description: Build an AI-powered utility website with embedded affiliate monetization — not reviews, but tools people actually use
---

# AI Utility Site Builder

Design and architect an AI-powered utility website that provides genuine standalone value while monetizing through naturally embedded affiliate links. Follows Darrel Wilson's "build the tool, not the review" philosophy.

## Input Required

- **Niche/Industry**: What space should the tool serve?
- **Target Affiliate Programs**: Which programs should be monetized?
- **Technical Comfort**: No-code (Lovable, Bolt) vs code (Next.js, React)?
- **Revenue Model**: Ads, affiliate-only, or hybrid (affiliate + subscription)?

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

### Step 1: Utility Concept Generation

The core question: **What tool would people in this niche use daily, regardless of whether they ever click an affiliate link?**

Apply the Darrel Wilson utility framework:

| Niche | Utility Site Concept | Affiliate Integration |
|-------|---------------------|----------------------|
| Finance/Travel | Live currency exchange rate comparator with fee analysis | Wise, Revolut links at conversion point |
| Crypto | AI-powered buy/sell/hold signal analyzer per coin | Coinbase, Binance links on each recommendation |
| Web Design | AI website audit/grade tool | Hosting (Hostinger), themes, page builders |
| Fitness | Workout/macro calculator with product recommendations | Supplement, equipment affiliate links |
| SaaS | Tool comparison calculator with live pricing | Individual SaaS affiliate links per tool |

**Validation Test**: Would someone bookmark this? If yes → proceed. If no → redesign.

### Step 2: Architecture Blueprint

Produce a technical architecture:

```
Frontend (UI/UX)
├── Input interface (what does the user enter?)
├── Output display (what do they get back?)
├── Affiliate CTAs (where do buy/signup buttons appear?)
└── SEO structure (meta tags, schema markup, sitemap)

Backend (Logic)
├── Data source (API, scraping, AI generation?)
├── Calculation engine (what transforms input → output?)
├── Affiliate link config (single source of truth, auto-propagated)
└── Analytics (click tracking, conversion pixels)

AI Layer (Intelligence)
├── What AI does (analysis, prediction, recommendation?)
├── Model selection (GPT-4, Claude, specialized?)
└── Update frequency (real-time, daily, on-demand?)
```

### Step 3: AI Builder Selection

| Tool | Best For | Cost | Limitations |
|------|----------|------|-------------|
| **Lovable** | Full-stack apps with Supabase backend | Free tier → $20/month | Complex state management |
| **Bolt.new** | Quick prototypes, static sites | Free tier → $20/month | Less backend control |
| **Hostinger Horizons** | WordPress-adjacent, hosting included | $10/month hosting | WordPress ecosystem |
| **Cursor + Next.js** | Maximum control, custom features | $20/month | Requires coding knowledge |

### Step 4: Affiliate Integration Architecture

**The One-Link Rule**: Define each affiliate link exactly once in a config/variable. The AI builder propagates it across every relevant CTA, button, and conversion point. Zero manual link placement.

**CTA Placement Strategy**:
1. **Primary CTA**: At the natural decision point (after seeing analysis/comparison)
2. **Secondary CTA**: In sidebar or footer (persistent, non-intrusive)
3. **Contextual CTA**: Inline within relevant content sections
4. **Exit CTA**: When leaving the tool, offer the "next step"

### Step 5: Traffic Integration Plan

How this site connects to the broader traffic strategy:
- **Long-form video**: YouTube tutorials demonstrating the tool → link in description
- **Parasite SEO**: Medium/LinkedIn articles about the problem the tool solves → link to tool
- **Short-form**: Quick demos of the tool in action → bio link

## Output Schema

A complete AI utility site blueprint, delivered as these fields:
- **Concept Description** (text): niche, the daily-use function the tool serves, result of the "would someone bookmark this?" validation test
- **Technical Architecture** (diagram): frontend (input/output/CTAs/SEO), backend (data source/calc engine/link config/analytics), AI layer (model + update frequency)
- **AI Builder Recommendation** (text): tool name (Lovable / Bolt.new / Hostinger Horizons / Cursor+Next.js), cost tier, build-step count
- **Affiliate Link Placement Map** (list): primary CTA / secondary CTA / contextual CTA / exit CTA → which affiliate link at each
- **Traffic Integration Plan** (list): long-form video angle, parasite SEO tie-in, short-form demo angle
- **Revenue Model** (formula): monthly visitors × conversion rate × avg commission = $/month, plus any display-ad RPM add-on

## Creative Latitude

The utility concepts above are starting points. Where creative intelligence sees a more compelling tool concept, a better data source, or a non-obvious affiliate integration — take it. The best utility sites solve problems people didn't know they had.

## Example Output

**Context**: User wants to build a crypto affiliate site using Coinbase partnership

**THE DELIVERABLE:**

**Concept: CoinSignal — AI Crypto Analysis Dashboard**

A real-time cryptocurrency analysis tool that uses AI to generate buy/sell/hold signals for the top 100 coins. Users see signal strength, risk level, technical analysis, and reasoning. Each coin page includes a "Buy on Coinbase" button using the affiliate link.

**Architecture:**
- Frontend: Next.js with Tailwind UI, responsive dashboard layout
- Data: CoinGecko API (free) for price/volume data
- AI: GPT-4 API for technical analysis interpretation and signal generation
- Affiliate: Single Coinbase affiliate link in env variable, auto-populated on all coin pages
- SEO: Individual pages per coin (e.g., `/bitcoin`, `/ethereum`) for organic traffic

**Monetization Math:**
- 10,000 monthly visitors × 3% conversion × $10 avg Coinbase commission = $3,000/month
- Add display ads at $5 RPM = additional $50/month
- Total: ~$3,050/month from a single utility site

**What elevates this**: The site provides genuine analytical value. Users come for the signals, not the affiliate pitch. Coinbase appears only at the natural decision point — when the user has already decided to buy.

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
