---
description: Generate a McKinsey-Grade Strategic Dossier for any niche using Agentic Research and Expert Ensembles.
---

# 🏛️ McKinsey-Grade Strategic Dossier Generator

> **Standard**: All briefs must follow the 8-Section McKinsey Format.
> **Reference**: `directives/expert_auto_routing.md`

---

## ⚠️ CRITICAL MANDATES

1. **LIVE RESEARCH ONLY** — No templates, no mock data
2. **AUTO-INVOKE EXPERTS** — Manus.AI + domain-specific expert(s)
3. **8-SECTION FORMAT** — Every brief follows this structure
4. **SOURCE EVERYTHING** — Every data point has a citation

---

## Phase 1: Entity Classification

Before any research, classify the input:

| Entity Type | Examples | Research Angle |
| :--- | :--- | :--- |
| **Product** | Running Shoes, Software | "best [product]", reviews, comparisons |
| **Service** | Plumbing, Legal, Consulting | "[service] near me", pricing, providers |
| **Demographic** | First Time Buyers, Parents, Seniors | Programs SERVING this group, needs, pain points |
| **Program** | CalHFA, FHA Loan, Grant | Eligibility, requirements, application process |
| **Location** | Los Angeles, Texas | Market conditions, local programs |

**Output**: "This is a [ENTITY TYPE]. Research angle: [ANGLE]."

---

## Phase 2: Expert Ensemble Invocation

Based on the niche, auto-invoke the right experts:

| Niche Type | Expert Ensemble |
| :--- | :--- |
| Real Estate/Finance | Manus.AI + Nathan Gotch (SEO depth) |
| Product/Launch | Samuel Thompson + Monk.AI |
| Service Business | Manus.AI + Kallaway (content psychology) |
| B2B/Consulting | Lindsay + Monk.AI |
| Personal Brand | Lara Acosta + Tom Noske |

**Read their genius-patterns.md before proceeding.**

---

## Phase 3: Deep Research (Perplexity-First Protocol)

> **Tier Classification**: Strategic Dossiers are **Tier 1: Foundation** by definition. Use Perplexity Deep Research or Sonar Pro.

### Step 3A: Budget Check
1. Read `.agent/perplexity-usage.json` — verify remaining budget
2. If budget allows ($2+ remaining): proceed with Perplexity
3. If budget tight ($0.50-$2): use Sonar only, batch aggressively
4. If exhausted: fall back to `search_web`, notify user

### Step 3B: Perplexity Research Queries (3-5 batched via Collapsing Rule)

Use `mcp_perplexity-ask_perplexity_ask` for each:

1. **Market Size + Landscape**: `"What is the current market size, growth rate, and key trends for [niche] in 2026? Include TAM/SAM/SOM estimates with sources."`
2. **Buyer Psychology + Pain Points**: `"What are the top pain points, frustrations, and unmet needs for [target buyer] in [niche]? Include verbatim quotes from Reddit, forums, and review sites."`
3. **Competitive Intelligence**: `"Who are the top 5-10 competitors in [niche]? What are their pricing models, positioning, and key weaknesses?"`
4. **Opportunities + Gaps**: `"What gaps exist in the [niche] market that new entrants could exploit? Include emerging trends and underserved segments."`

### Step 3C: Supplementary Web Search

Use `search_web` for anything Perplexity didn't cover:
- SERP/SEO landscape: `"[niche] keywords site:ahrefs.com OR site:semrush.com"`
- Programs/options: `"[niche] programs options alternatives"`

### Step 3D: Log & Tag
1. Log all Perplexity queries to `.agent/perplexity-usage.json`
2. Tag all findings with provenance: 🟢 GROUNDED (Perplexity-sourced) or 🟡 SUPPLEMENTED (web search)

**Extract**:
- Actual numbers (TAM, market size, income data) — with citations
- Verbatim quotes from real buyers/users
- Competitor gaps and weaknesses — named competitors, real pricing
- Time-sensitive opportunities — current-year sources only

---

## Phase 4: Synthesize into 8-Section Format

### MANDATORY SECTIONS

1. **Executive Summary**
   - Verdict: 🟢 Blue Ocean / 🟡 Yellow Ocean / 🔴 Red Ocean
   - 5 key insights with data points

2. **Market Sizing**
   - TAM (Total Addressable Market)
   - SAM (Serviceable Addressable Market)  
   - SOM (Serviceable Obtainable Market)
   - All with sources

3. **Buyer/Customer Profile**
   - Demographics + psychographics
   - Pain point hierarchy (ranked)
   - Verbatim frustrations (from Reddit/forums)
   - Emotional state and primary fears

4. **Competitive Intelligence**
   - SERP landscape (who ranks for head terms?)
   - Exploitable gaps (what's missing?)
   - Weakness analysis

5. **Options/Program Matrix**
   - Decision tree or comparison table
   - When to use each option

6. **Economic Model**
   - Revenue potential
   - ROI projections
   - Break-even analysis
   - Cost assumptions

7. **Risk Matrix**
   | Risk | Probability | Impact | Mitigation |
   | :--- | :--- | :--- | :--- |

8. **Execution Playbook**
   - Week-by-week or day-by-day actions
   - Specific deliverables
   - Success metrics

---

## Phase 5: Quality Gate & Red Team Validation

Before delivering, verify:

- [ ] Every data point has a source
- [ ] Every insight has an action
- [ ] No "glob of words" — all paragraphs are specific
- [ ] Decision tree or matrix included
- [ ] Week-by-week playbook included

**RED TEAM VALIDATION (Adversarial Check)**:
Run a mandatory adversarial pass against the brief before final output:
1. **The Cynical Buyer Test**: Why would the target buyer reject this thesis immediately? Add a section addressing this friction.
2. **Competitor Blind Spots**: Who was missed in the landscaping? Are we underestimating the market leader?
3. **The 'So What' Filter**: Is this actually a disruptive insight, or just a summary of what's already known? 

*If the brief is too safe, rewrite the Executive Summary to take a polarizing, opinionated stance based on the data.*

---

## Output

Save to: `strategy_briefs/Strategy_Brief_[Niche_Clean_Name].md`

Include "Sources" section at bottom with:
| Claim | Source | Date Accessed |

---

*Effective: 2026-02-05*
*Standard: McKinsey-Grade Execution*
