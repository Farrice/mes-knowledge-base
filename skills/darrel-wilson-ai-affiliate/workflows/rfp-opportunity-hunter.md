---
description: Automated RFP and contract opportunity hunter for finding $30K-$100K government and enterprise contracts
---

# RFP Opportunity Hunter

Build an automated system that finds, filters, and delivers high-value RFP (Request for Proposal) and contract opportunities. Based on Darrel Wilson's approach to finding $30K-100K web design and AI automation contracts through government and enterprise portals.

## Input Required

- **Service Category**: What do you deliver? (Web design, AI automation, consulting, marketing)
- **Budget Floor**: Minimum contract value worth pursuing ($5K, $10K, $30K?)
- **Geographic Scope**: Local, state, federal, or international?
- **Platform Preference**: n8n (self-hosted) or Make.com (cloud)?

## Execution

### Step 1: RFP Source Identification

Map high-value contract sources by tier:

| Tier | Source | Contract Range | Example Keywords |
|------|--------|---------------|-----------------|
| **Federal** | SAM.gov, FPDS, GovWin | $50K-$500K+ | "website redesign," "digital transformation," "IT modernization" |
| **State/Local** | State procurement sites, BidNet, GovSpend | $10K-$100K | "web services," "marketing services," "technology consulting" |
| **Enterprise** | RFP360, RFP.io, corporate procurement pages | $20K-$200K | "agency of record," "digital partner," "automation vendor" |
| **Job Boards** | Upwork Enterprise, Toptal, LinkedIn Jobs (contract) | $5K-$50K | "contract," "project-based," "6-month" |

### Step 2: Keyword Matrix

Build category-specific keyword combinations:

**Service Match**: `[your service] + [RFP language]`
- "website redesign" + "request for proposal"  
- "AI automation" + "vendor selection"
- "digital marketing" + "scope of work"
- "software development" + "statement of work"

**Budget Signals**: "budget range," "not to exceed," "estimated value," "contract ceiling"

**Timeline Urgency**: "due date," "response deadline," "submission by"

### Step 3: n8n Automation Build

```
┌──────────────┐
│ Cron Trigger  │  Every 2 hours (business hours)
└──────┬───────┘
       │
┌──────▼───────┐
│ Multi-Source  │  Parallel scrape: SAM.gov API + BidNet + 
│ Fetch         │  Upwork RSS + LinkedIn Jobs API
└──────┬───────┘
       │
┌──────▼───────┐
│ Keyword      │  Match against service + budget + timeline keywords
│ Filter       │  
└──────┬───────┘
       │
┌──────▼───────┐
│ Budget Gate  │  Extract dollar amounts; reject below floor
│ (IF Node)    │  
└──────┬───────┘
       │
┌──────▼───────┐
│ AI Scoring   │  Score 1-10: fit, budget, timeline, win probability
│ (GPT-4)      │  
└──────┬───────┘
       │
┌──────▼───────┐
│ Quality Gate │  Score ≥ 7 → proceed
│ (IF Node)    │  
└──────┬───────┘
       │
  ┌────┴─────┐
  │          │
┌─▼──┐  ┌──▼──────┐
│ CRM│  │ Slack   │  + email digest (daily summary)
│    │  │ Alert   │
└────┘  └─────────┘
```

### Step 4: Win Probability Assessment

AI scoring prompt for each RFP:

```
Assess this RFP opportunity:
Title: {title}
Description: {description}
Budget: {budget_if_stated}
Deadline: {deadline}
Source: {source}

Score 1-10 on:
1. Service Match: Does this match [USER_SERVICES]?
2. Budget Adequacy: Is the budget realistic for quality delivery?
3. Timeline Feasibility: Can we deliver by the deadline?
4. Competition Level: Is this oversaturated or niche enough to win?
5. Relationship Potential: Could this lead to recurring work?

Output: Overall Score, Win Probability %, Recommended Approach
```

### Step 5: Response Template Library

For each opportunity type, maintain response templates:
- **Quick proposal** (under $10K): 1-page scope + price
- **Standard proposal** ($10K-$50K): 3-5 page proposal with case studies
- **Full RFP response** ($50K+): Formal response document with methodology, timeline, team

### Step 6: Pipeline Dashboard

Track opportunities through stages:
1. **Identified** → 2. **Qualified** → 3. **Proposal Sent** → 4. **Follow-up** → 5. **Won/Lost**

## Output

- Working n8n/Make workflow (JSON export)
- Keyword matrix document
- AI scoring prompt (calibrated)
- Google Sheets pipeline tracker template
- 3 proposal templates by contract size
- Daily email digest configuration

## Creative Latitude

The sources above cover the standard RFP landscape. Where domain-specific intelligence reveals hidden procurement channels, niche job boards, or industry-specific contract platforms — deploy them. The highest ROI is often in niche sources nobody else monitors.
