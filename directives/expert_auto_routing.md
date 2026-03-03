# Expert Auto-Routing — Domain Tables & Ensembles

> **Role**: Reference tables for domain detection, ensemble patterns, and output standards.
> **Pipeline**: Intent handling moved to `directives/intent-pipeline.md` (Stage 3: ROUTE uses these tables).
> **Full Domain Registry**: `DOMAIN_REGISTRY.md` — 15 domains, 94 agents with swim lanes, routing trees, handoff chains, and compound combinations.
> **Effective**: 2026-02-05 | **Updated**: 2026-03-03 (domain registry expanded to 15 domains)
> **Router**: See `directives/router_agent.md` for fast-path dispatch
> **Loading Protocol**: See `directives/agent-loading-protocol.md` for tiered loading chain

---

## Domain Detection Table

| Request Type | Signals | Default Experts |
|:---|:---|:---|
| **Research/Intelligence** | "analyze", "research", "find out", "what's the market" | Manus.AI + relevant domain expert |
| **Content Creation** | "write", "create", "draft", "content" | Appropriate content expert(s) |
| **Strategy/Decision** | "should I", "what's the best", "how do I approach" | Jim O'Shaughnessy + domain experts |
| **Copywriting** | "sales page", "email", "headline", "convert" | Cardinal Mason + Harry Dry |
| **Personal Brand** | "LinkedIn", "positioning", "brand", "authority" | Lara Acosta + Tom Noske |
| **Ghostwriting** | "ghostwrite", "write as", "voice capture", "proof run" | Ghostwriting Voice Engine (`/ghostwrite`) |
| **Product/Offer** | "product", "offer", "pricing", "launch" | Samuel Thompson + Monk.AI |
| **Sales/Persuasion** | "objection", "close", "persuade", "sell" | Jeremy Miner + Alen Sultanic |
| **Storytelling** | "story", "narrative", "hook", "engage" | Shaan Puri + Lucas Alpay |
| **Video/TikTok** | "video", "TikTok", "viral", "hook" | Seena Rez + Kallaway |
| **AI/Automation** | "automate", "workflow", "agent", "AI" | Nick Saraev + Boris |
| **SEO/Search** | "rank", "SEO", "keywords", "traffic" | Nathan Gotch + Adam Enfroy |
| **Design/Visual** | "design", "visual", "aesthetic", "creative" | Oren + Kittl |
| **Launch/Innovation** | "launch", "validate", "early adopter", "monitor" | Seena Rez + Samuel Thompson |

---

## Expert Ensemble Patterns

### For Innovation/Launch
1. Seena Rez (early adopter signal)
2. Samuel Thompson (shadow markets)
3. Oren (identity aesthetics)

### For Market Research + Content
1. Manus.AI (research depth)
2. Kallaway (content psychology)
3. Nathan Gotch (SEO/retrieval)

### For Product Launch
1. Samuel Thompson (shadow markets, economics)
2. Monk.AI (offer architecture)
3. Cardinal Mason (conversion copy)

### For Personal Brand Building
1. Lara Acosta (LinkedIn mastery)
2. Tom Noske (magnetic personal brand)
3. Dan Koe (multipassionate positioning)

### For Strategic Decisions
1. Jim O'Shaughnessy (philosopher-financier)
2. Manus.AI (competitive intelligence)
3. Domain-specific expert(s)

### For High-Converting Copy
1. Harry Dry (Three Rules Test)
2. Cardinal Mason (conversion systems)
3. Alen Sultanic (buyer psychology)

### For Coach Ghostwriting
1. Ghostwriting Voice Engine (`/ghostwrite` — full pipeline)
2. Lara Acosta (voice extraction + LinkedIn mastery)
3. Nicolas Cole (sentence refinement + voice preservation)

### For Viral Content
1. Seena Rez (TikTok commerce)
2. Kallaway (dopamine ladder)
3. Shaan Puri (storytelling)

---

## McKinsey-Grade Execution Standard

All intelligence/research outputs must follow this format:

### Minimum 8 Sections for Strategic Briefs
1. **Executive Summary** — Verdict + 5 key insights with data
2. **Market Sizing** — TAM/SAM/SOM with numbers and sources
3. **Buyer/Customer Profile** — Psychographics, pain points, verbatims
4. **Competitive Intelligence** — SERP/market landscape + exploitable gaps
5. **Options/Paths** — Decision tree or program matrix
6. **Economic Model** — ROI projections, break-even analysis
7. **Risk Matrix** — Probability/Impact/Mitigation
8. **Execution Playbook** — Day-by-day or week-by-week actions

### Every Insight Must Have
- **A data point** (number, statistic, quote)
- **A source** (URL or publication)
- **An action** (what to DO about it)

### No "Glob of Words" Allowed
If an output reads like a report without clear actions, it has FAILED. Every paragraph must either:
- State a fact with a source, OR
- Give a specific instruction

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | *Not yet activated* |
| **Activation Count** | 0 |
| **30-Day Review Date** | 2026-04-01 |

**Update Rule**: When domain tables or ensembles are referenced, update the date and increment count.

---

*Effective: 2026-02-05 | Updated: 2026-03-02*
*Classification: Reference Document (active pipeline: `directives/intent-pipeline.md`)*
