---
description: Build AI-powered micro-apps with ad revenue and affiliate monetization — calculator, converter, and analyzer apps
---

# AI App Revenue Builder

Design, build, and monetize AI-powered micro-applications (SaaS tools, calculators, converters, analyzers) that generate revenue through ads, affiliate links, and premium tiers. Based on Darrel Wilson's approach to building utility tools that monetize through natural usage patterns.

## Input Required

- **App Category**: What problem does it solve? (Finance, health, productivity, data analysis)
- **Revenue Model**: Ads, affiliate, freemium, or hybrid?
- **Technical Level**: No-code (Lovable/Bolt) vs code (React/Next.js)?
- **Target Users**: Who uses this daily?

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

### Step 1: App Concept Validation

Run the "Would They Bookmark It?" test:

| App Type | Example | Revenue Model | Daily Use Score |
|----------|---------|---------------|-----------------|
| **Calculator** | Mortgage calculator, calorie counter, currency converter | Ads + affiliate (lender links, food delivery, Wise) | ⭐⭐⭐⭐⭐ |
| **Analyzer** | Crypto signal analyzer, SEO checker, grammar scorer | Freemium + affiliate (Coinbase, Ahrefs, Grammarly) | ⭐⭐⭐⭐ |
| **Converter** | File converter, unit converter, timezone converter | Ads (high volume, low intent per visit) | ⭐⭐⭐⭐⭐ |
| **Generator** | AI text generator, image creator, code snipper | Freemium (free tier + paid API credits) | ⭐⭐⭐ |
| **Comparison** | Price comparison, product matcher, tool selector | Affiliate (per-comparison click) | ⭐⭐⭐⭐ |

**Validation**: If Daily Use Score < 3 stars → redesign. The app must solve a recurring problem.

### Step 2: Architecture Blueprint

```
User Interface
├── Input (form, upload, search)
├── Processing indicator (loading state)
├── Output (results, analysis, conversion)
├── Monetization zones:
│   ├── Banner ad (top/bottom — Google AdSense/Mediavine)
│   ├── Native affiliate CTA (contextual, after output)
│   └── Premium gate (advanced features behind paywall)
└── SEO pages:
    ├── Individual tool pages (e.g., /usd-to-eur)
    ├── Blog/guide section (content marketing)
    └── Sitemap + schema markup

Backend
├── API integration (data source: CoinGecko, ExchangeRate, etc.)
├── AI layer (GPT-4 for analysis/recommendations)
├── User accounts (optional, for saving preferences)
└── Analytics (Google Analytics 4, PostHog)
```

### Step 3: Revenue Integration

**Ad Revenue Setup:**
1. Apply for Google AdSense (1,000+ visitors/month minimum)
2. Place ads in non-intrusive positions (below results, sidebar)
3. At 50K+ monthly visitors → switch to Mediavine ($15-25 RPM vs AdSense $3-8 RPM)

**Affiliate Integration:**
- Define ONE affiliate link per partner product
- Place at natural decision points (after user sees analysis/result)
- Use contextual CTAs: "Ready to convert? Transfer with Wise →"
- Track clicks per CTA position for optimization

**Freemium Tiers:**
| Tier | Price | Access | Conversion Target |
|------|-------|--------|-------------------|
| Free | $0 | 5 uses/day, basic features | Everyone (high volume) |
| Pro | $9.99/month | Unlimited uses, advanced AI | 2-5% of free users |
| API | $29.99/month | API access, bulk processing | Developers, agencies |

### Step 4: Build & Deploy

**No-Code Path (2-4 hours):**
1. Use Lovable or Bolt.new with detailed prompt
2. Connect data API (free tier)
3. Add Google AdSense code
4. Deploy to custom domain via Vercel/Netlify

**Low-Code Path (1-2 days):**
1. Cursor + Next.js template
2. Build UI with Tailwind/shadcn
3. Wire AI analysis with OpenAI API
4. Add revenue integrations
5. Deploy to Vercel

### Step 5: Traffic Flywheel

Drive users to the app:
1. **SEO**: Individual pages per tool function rank independently
2. **YouTube**: "How to [solve problem]" tutorials that use the app
3. **Parasite SEO**: Medium/LinkedIn articles about the problem → link to app
4. **Reddit/Communities**: Answer questions, share the tool as a resource

### Step 6: Portfolio Multiplication

Once one app works:
- Build 3-5 apps in the same niche (converters → calculators → analyzers)
- Cross-link between apps
- Bundle under one brand domain
- Revenue compounds: 5 apps × $500/month each = $2,500/month

## Output Schema

A complete AI app revenue blueprint, delivered as these fields:
- **App Concept** (text): category, problem solved, Daily Use Score (⭐ 1-5) with validation reasoning
- **Technical Architecture** (diagram + build instructions): frontend zones, backend stack, no-code or low-code build path with step count
- **Revenue Integration Plan** (table): ad-network tier + RPM, affiliate CTA placement points, freemium tier pricing ($0 / $9.99 / $29.99-style ladder)
- **Traffic Strategy** (list of items): SEO page structure, YouTube tutorial angle, parasite SEO tie-in, community channels
- **Portfolio Expansion Plan** (text): number of apps in the niche cluster, cross-link structure, shared brand domain
- **Revenue Projection** (numeric): $/month at 1,000 / 10,000 / 50,000+ monthly visitor tiers, split by ad vs. affiliate vs. subscription

## Creative Latitude

The app categories above are proven models. Where creative intelligence identifies underserved niches, unique data sources, or unexploited utility gaps — pursue them. The best utility apps are the ones where people say "I can't believe this didn't exist before."

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
