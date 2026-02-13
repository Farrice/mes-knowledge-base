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

## Phase 3: Deep Research (Manus.AI Protocol)

Execute at least 5 search queries:

1. **Market Size**: `"[niche] market size statistics 2026"`
2. **Competitor Landscape**: `"[niche] top companies competitors 2026"`
3. **Buyer Psychology**: `"[niche] customer pain points frustrations reddit OR forum"`
4. **SERP/SEO**: `"[niche] keywords site:ahrefs.com OR site:semrush.com"`
5. **Programs/Options**: `"[niche] programs options alternatives"`
6. **News/Trends**: `"[niche] news trends 2026"`

**Extract**:
- Actual numbers (TAM, market size, income data)
- Verbatim quotes from real buyers/users
- Competitor gaps and weaknesses
- Time-sensitive opportunities

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

## Phase 5: Quality Gate

Before delivering, verify:

- [ ] Every data point has a source
- [ ] Every insight has an action
- [ ] No "glob of words" — all paragraphs are specific
- [ ] Decision tree or matrix included
- [ ] Week-by-week playbook included

---

## Output

Save to: `strategy_briefs/Strategy_Brief_[Niche_Clean_Name].md`

Include "Sources" section at bottom with:
| Claim | Source | Date Accessed |

---

*Effective: 2026-02-05*
*Standard: McKinsey-Grade Execution*
