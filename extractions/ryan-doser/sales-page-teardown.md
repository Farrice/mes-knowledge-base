# Ryan Doser — Claude-Skills Business Teardown (Live Truth)

Captured 2026-07-15 for extraction grounding. Every claim tagged OBSERVED (saw it directly) or INFERRED. Source URLs per claim. Tool used noted where relevant (WebFetch = static render; Playwright = JS render).

---

## 1. THE SALES PAGE — skills.ryandoser.com
Source: https://skills.ryandoser.com/ (WebFetch, rendered fully — SSR)
CONFIDENCE: HIGH on structure, product, price, CTA, guarantee, checkout (all OBSERVED verbatim). MODERATE on exact ordering of lower sections (WebFetch summarized; not screenshot-verified pixel order).

### Product name
- "Claude Code Skills Stack" (also referred to as "The Skills Stack"). OBSERVED.

### Headline (verbatim)
- **"Turn Claude Code Into Your Marketing Team"** OBSERVED.

### Subhead (verbatim)
- **"Get the exact 40+ skills I use daily to run a six-figure marketing business"** OBSERVED.

### Price / tiers
- **$99 one-time. No subscription.** Single tier — there is no good/better/best ladder. OBSERVED.
- Framed as locking in **lifetime updates ("free, forever")** at the $99 price — a "buy now before it goes up / updates included" anchor. OBSERVED.

### Guarantee / refund (verbatim)
- **"All digital product sales are final. Products are delivered instantly and cannot be returned due to the downloadable nature of this product."** OBSERVED.
- Note: this is a NO-refund policy stated as a feature of instant delivery, not a money-back guarantee. No risk-reversal offered. OBSERVED.

### License terms
- No explicit license text (no "personal use / no resale" clause captured). INFERRED gap — may exist in delivered files, not on page.
- Cross-platform claim: works with Claude Code, Cowork, Cursor, ChatGPT, etc. (V2 positioning = platform-agnostic). OBSERVED.

### What's inside the pack
- **40+ skills across 8 categories**: SEO, content, social, email, YouTube, images, web, system. OBSERVED.
- Named skills shown (19 listed as examples): Content Repurposing, SEO Blog Post Writer, Email Newsletter Writer, LinkedIn Post Writer, Anti-Slop, YouTube SEO Packaging, Short Form Video Scripts, Keyword Research, Paid Ads, Local SEO Strategist, GEO/AI Search Optimizer, Listicle & Roundup Writers, Comparison Writer, Social Media Manager, Landing Page Designer, Infographic Generator, YouTube Thumbnail Designer, Skill Creator. OBSERVED.
- Also bundled: his **AGENTS.md** personal setup config, a **"Start Here" guide**, system skills (Skill Creator, MCP Setup, Troubleshooting), tips/shortcuts doc, lifetime updates. OBSERVED.
- **V2 (July 2026) update block** on page = 5 new feature categories + cross-platform support. Signals active product iteration. OBSERVED.

### Section order (top to bottom, as rendered)
1. Hero — name + $99 + CTA. OBSERVED.
2. Demo — CLI-style simulated command outputs (SEO, repurposing, anti-slop) → technical credibility. OBSERVED.
3. Problem/Solution — 5 pain points vs 5 benefits (✓/✗ comparison table). OBSERVED.
4. Social proof — **live search-console metrics: 5.77K clicks, 890K impressions, 12.1K AI citations**. OBSERVED (numbers shown on page; not independently verified = the metrics themselves are INFERRED-true).
5. Revenue claim — "$100K+ in revenue" business-impact statement. OBSERVED on page / claim UNVERIFIED.
6. Testimonials — 6 quotes with headshots + titles. OBSERVED.
7. Skills list — 19 skills across 8 categories. OBSERVED.
8. Package details — deliverables checklist (40+ skills, guides, updates). OBSERVED.
9. V2 updates block (July 2026). OBSERVED.
10. Buyer personas — 4 ideal-customer segments. OBSERVED.
11. Exclusions — "who should NOT buy" (3 scenarios) = qualification/negative-sell. OBSERVED.
12. FAQ — 7 Q&As (setup, compatibility, refunds). OBSERVED.
13. Final CTA — closing pitch + free Anti-Slop skill download (lead magnet at the bottom). OBSERVED.

### CTAs (verbatim)
- Primary: **"Get Instant Access →"** OBSERVED.
- Secondary: **"Get the Skills Stack for $99 →"** OBSERVED.
- Free/tertiary: **"Download the Anti-Slop Skill Free ↓"** OBSERVED.

### Upsells
- No formal upsell package on the page. Consulting is referenced inside a testimonial ("already planning to book consulting time") — soft cross-sell only. OBSERVED. Consulting is sold on the main site, not bolted to checkout. INFERRED (funnel is decoupled).

### Email capture
- No opt-in gate before checkout. The **free Anti-Slop skill** at the bottom is the only capture mechanic (lead magnet). OBSERVED.

### Checkout provider
- **Stripe** — page states "Secure checkout via Stripe." OBSERVED.
- Note: a Cloudflare Workers deploy mirror exists (claude-code-skills-stack.rdoser13.workers.dev) → page is hosted on CF Workers. OBSERVED (search result).

### Design quality
- Clean, minimal, high-trust. Heavy ✓/✗ comparison tables, CLI demo blocks for technical credibility, headshot testimonials, versioned changelog. Multiple CTAs (hero/mid/bottom/footer). Reads as a competent solo-operator SaaS-style landing page, not a bloated guru page. OBSERVED/INFERRED (aesthetic judgment).

---

## 2. MAIN SITE — ryandoser.com
Source: https://ryandoser.com (WebFetch). CONFIDENCE: HIGH on nav/funnel; MODERATE on blog internals (sampled 1 post fully).

### What it is
- **Personal brand + services hub + SEO blog**, not a pure agency site. Positions Ryan as an AI-marketing operator. OBSERVED.
- Nav: Home, About, Consulting, Community (Skool), My Claude Code Skills, Blog. OBSERVED.
- Trust bar: Forbes, Yahoo, People Magazine, Better Homes & Gardens, MarketWatch logos. OBSERVED.
- Claims **30K+ YouTube subs / 2M+ views** on site (actual channel now 38K — see §3). OBSERVED.

### Offer stack (funnels)
- Free AI Marketing Guide → **Kit (ConvertKit) email capture** — top of funnel. OBSERVED.
- Services: AI Concierge, AI Personal Branding, AI Consulting. OBSERVED.
- Community: "AI Marketing Insiders" on Skool. OBSERVED.
- Product: Claude Code Skills Stack ($99) via "Get Instant Access". OBSERVED.
- Homepage explicitly hooks the product: "20+ Claude Skills That Run My Business" → skills.ryandoser.com. OBSERVED.

### The SEO blog loop (the mechanic the video describes)
Source: https://ryandoser.com/blog + https://ryandoser.com/make-money-with-claude/ (WebFetch). CONFIDENCE: HIGH — the loop is self-documented on-page.
- Blog is a **video-to-blog repurposing engine**: posts are generated by "a Claude Code loop that converts videos to blog posts." The post literally says it was made this way. OBSERVED (self-stated).
- Sample post "How I Make Money with Claude Selling Skills ($10K Example)" structure: Video Guide → What It Means → How to Build a Skill → Why Small Skills Beat One Giant Skill → Skills Work Everywhere → Turning a Skill Into a $10K Digital Product → Distribution Is the Real Way → Why Your Expertise Matters → Final Thoughts → FAQ → author bio. OBSERVED.
- **Internal linking pattern**: dense cross-links to sibling posts (Claude skills vs custom GPTs, vibe-code a digital product, repurpose YouTube videos, why marketers should use Claude Code) + funnels to newsletter. Classic topic-cluster interlinking. OBSERVED.
- **CTA placement**: skills.ryandoser.com referenced twice mid-body (primary), plus Skool + consulting nav + newsletter capture at the bottom. Every post routes to the $99 product and/or the email list. OBSERVED.
- **Revenue claim in-post (verbatim):** "That product has made over $10,000 passively since I launched it in March." Also discloses **~25% of revenue from products, ~75% from marketing agency.** OBSERVED / self-reported UNVERIFIED.

### Blog post inventory (page 1 of paginated blog, ≥5 pages)
All slugs are exact-match keyword targets. OBSERVED:
- /ai-second-brain/ · /make-money-with-claude/ · /claude-code-skills-stack-v2-update/ · /claude-skills-vs-perplexity-spaces/ · /claude-skills-vs-gemini-gems/ · /free-vs-paid-claude-skills/ · /best-free-claude-skill-repos/ · /turn-claude-projects-into-skills/ · /claude-skills-for-seo/ · /claude-skills-marketplace/
- Plus (from search): /sell-claude-skills/ · /claude-ai-side-hustle/ · /claude-code-for-marketing/ · /ai-marketing-guide/

---

## 3. YOUTUBE — @RyanDoserAI
Source: Playwright (JS-rendered channel page). CONFIDENCE: HIGH on subs/video count (OBSERVED); MODERATE on "top" videos (YouTube ignored the popular-sort param — list below is the LATEST/default grid, not sorted by views).

- **38K subscribers. 984 videos.** OBSERVED (Playwright DOM).
- Per-video views are LOW relative to sub count: recent videos show **~465–3.6K views each** (sampled: 590, 1.6K, 529, 3.6K, 751, 465, 794). OBSERVED. → high-volume publishing, modest per-video reach; audience is niche/buyer-intent, not viral.
- Cadence: very high output (984 videos) — near-daily or multi-weekly. Format skews to **long interview/podcast-style videos (20–42 min)** + shorter tactical how-tos (8–17 min). OBSERVED.
- Recent titles (default grid) — note the guru-interview pattern and $-in-title hooks. OBSERVED:
  - "He Sells AI Second Brains to Businesses (For $1000s)" (32m)
  - "Try These Claude Code Hacks from a Top 1% User" (42m)
  - "How She Went From $0 to $50K/Month With AI in 6 Months" (35m)
  - "How I Build AI Landing Pages That Convert (With Free Skill)" (14m)
  - "He Makes $100K/Month With Rank & Rent (AI Proof)" (35m)
  - "This AI Side Hustle Made Me Over $5K (Claude Skills)" (24m)
  - "How to Build $10K Websites with Claude Code (RIP WordPress)" (27m)
  - "How I Create a Month of Social Content in 15 Minutes With AI" (14m)
- Title formula: **social-proof interview ("He/She Makes $X") + dollar figure + platform-kill hook ("RIP WordPress", "Did Claude Code Kill n8n?")**. Buyer-intent, money-outcome framing. OBSERVED.
- Free-skill giveaways baked into titles ("With Free Skill") = YouTube → lead-magnet → email → $99 product loop. OBSERVED/INFERRED.

---

## 4. SEO / RANKING CHECK
Source: WebSearch (July 2026). CONFIDENCE: MODERATE — SERP snapshots are volatile and personalization/geo can shift positions.

- **"sell claude skills"** → ryandoser.com/sell-claude-skills/ ranks **~#2 (page 1)**, plus a 2nd Doser result (/claude-ai-side-hustle/) also on page 1. STRONG exact-match win. OBSERVED.
- **"claude skills pack marketing ryan doser"** (branded) → he owns the whole SERP (skills page, guide, PR, blog). OBSERVED.
- **"how to make money with claude skills"** (head term) → Doser NOT on page 1; crowded by Medium/Sabrina Ramonov/Artificial Corner. OBSERVED.
- **"claude skills for seo"** (head term) → Doser NOT on page 1; dominated by GitHub repos, Ahrefs, SE Ranking, dedicated SEO-skill sites. OBSERVED — despite him having a /claude-skills-for-seo/ post. Head term too competitive.
- **"claude code skills pack"** → Doser NOT on page 1; Anthropic docs, GitHub, Firecrawl, marketplaces. OBSERVED.
- **Pattern:** Doser wins **exact-match, lower-competition, buyer-intent long-tail** ("sell claude skills", comparison posts vs Gems/Spaces). He is NOT winning crowded head terms. His moat is programmatic long-tail volume (984 videos → topic-cluster blog), not head-term authority. INFERRED from SERP pattern.
- Extra distribution move: **einpresswire PR** ("Ryan Doser Ships V2 of the Claude Code Skills Stack…") — he issues press releases for product updates. OBSERVED (search result).

---

## 5. SECONDARY ECOSYSTEM (same "sell AI skills/systems" niche)
CONFIDENCE: HIGH (OBSERVED via WebFetch).

### skool.com/sandyleeai (interviewer Sandy Lee — note: community is "AI Content Systems")
- **201 members. $97/month, increasing to $117/mo.** Creator: Sandy Lee. OBSERVED.
- Value stack: Slee Studio Pro ($59/mo value), 8-agent AI content pipeline template, members templates, weekly live Q&As, 5-month curriculum, private vault, weekly AI briefing. OBSERVED.
- Monetization = **recurring paid community** (vs Doser's one-time $99 product). Different model, same audience.

### sleeautomation.com/resources
- **Free lead-magnet page** — name+email capture for "resources shared in my videos," "instant access," "only valuable emails." No paid product on this page. OBSERVED.
- Classic top-of-funnel list-builder; monetization downstream (community/consulting). INFERRED.

---

## CROSS-CUTTING NOTES FOR EXTRACTION
- Doser's model = **low-ticket one-time ($99) digital product + high-ticket services/consulting + email list**, fed by a **content flywheel (YouTube → repurposed SEO blog → newsletter → product)**. The $99 product is the tripwire; agency/consulting is the real revenue (self-stated 75% agency / 25% products).
- Honesty signal: he openly discloses revenue split and the AI-repurposing method on the blog — transparency is part of the positioning.
- The whole business is **dogfooded**: the product (skills) builds the marketing (blog/social skills) that sells the product. That recursion IS the pitch.

## UNVERIFIED / COULDN'T CONFIRM
- "$100K+ revenue", "$10K passive", search-console metrics (5.77K clicks / 890K impressions / 12.1K AI citations) — all shown on his own properties, none independently verified.
- YouTube "top videos by views" — could not force popular-sort; only latest grid + sampled low view counts captured.
- Exact license/resale terms of the pack — not visible pre-purchase.
