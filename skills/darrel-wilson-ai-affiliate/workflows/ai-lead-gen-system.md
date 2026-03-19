---
description: Build a ready-to-deploy AI lead generation workflow using n8n or Make.com for any industry
---

# AI Lead Generation System

Build an automated lead generation pipeline that scrapes RFPs, job boards, and public listings, scores leads with AI, and delivers qualified opportunities to your inbox or CRM. Based on Darrel Wilson's n8n architecture for finding $30-100K web design contracts.

## Input Required

- **Industry/Niche**: What types of leads are you looking for?
- **Lead Sources**: Where do your ideal clients post needs? (Job boards, RFP sites, Reddit, government portals)
- **Keywords**: What terms signal buying intent in your niche?
- **Automation Platform**: n8n (self-hosted, free) or Make.com (cloud, $9-29/month)?
- **Output Destination**: Google Sheets, CRM (HubSpot), Slack, email?

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution

### Step 1: Lead Source Mapping

Identify 3-5 sources where high-intent buyers publicly announce needs:

| Source Type | Examples | Signal Strength |
|-------------|---------|----------------|
| **RFP Sites** | Government procurement portals, SAM.gov, local municipality sites | 🔥 Highest — budget allocated, deadline set |
| **Job Boards** | Upwork, Fiverr Business, Indeed (contract roles) | 🔥 High — actively hiring |
| **Industry Forums** | Reddit (r/forhire, niche subs), Hacker News | 🟡 Medium — expressing need |
| **Social Signals** | LinkedIn posts, Twitter "looking for" threads | 🟡 Medium — soft intent |
| **Directory Listings** | Google Maps (businesses with bad websites), Yelp | 🟢 Low — implied need |

### Step 2: Keyword Matrix Design

Build a keyword matrix combining:
- **Service keywords**: "web design," "AI automation," "marketing agency"
- **Intent keywords**: "request for proposal," "looking for," "need help with," "hiring"
- **Budget keywords**: "$5,000," "budget," "contract value"
- **Niche modifiers**: Industry-specific terms

**Formula**: [Service Keyword] + [Intent Keyword] + [Niche Modifier] = Lead Query

### Step 3: n8n Workflow Architecture

```
┌─────────────────┐
│   Cron Trigger   │  (Every 2 hours)
│   (Schedule)     │
└────────┬────────┘
         │
┌────────▼────────┐
│  HTTP Request    │  Scrape target URLs via API/Apify/Puppeteer
│  (Data Fetch)    │
└────────┬────────┘
         │
┌────────▼────────┐
│  Keyword Filter  │  Match against keyword matrix
│  (IF Node)       │  Reject: no intent keywords found
└────────┬────────┘
         │
┌────────▼────────┐
│  AI Scoring      │  OpenAI node: Score lead 1-10 on intent,
│  (GPT-4)         │  budget, timeline, fit
└────────┬────────┘
         │
┌────────▼────────┐
│  Quality Gate    │  Filter: Score ≥ 7 only
│  (IF Node)       │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼──────┐
│ Sheets │ │  Slack   │  Dual output: persistent record + instant alert
│ Append │ │  Notify  │
└────────┘ └─────────┘
```

### Step 4: AI Scoring Prompt

```
You are a lead qualification expert. Score this lead 1-10 based on:

LEAD DATA:
{lead_title}
{lead_description}
{lead_source}
{lead_budget_if_available}

SCORING CRITERIA:
- Budget clarity (1-10): Is a budget mentioned or implied?
- Timeline urgency (1-10): Is there a deadline?
- Service match (1-10): Does this match [USER_NICHE] services?
- Accessibility (1-10): Can we realistically win this?

OUTPUT:
- Overall Score: [1-10]
- Recommended Action: [PURSUE / MONITOR / SKIP]
- One-line pitch angle: [How to approach this lead]
```

### Step 5: Dual Monetization Strategy

Every lead gen workflow has two revenue paths:

1. **Use the leads yourself**: Take the contracts, close the deals
2. **Sell the leads**: Package qualified lead lists and sell to agencies/freelancers who need clients

**Pricing for lead lists**: $97-497/month subscription depending on niche competitiveness and lead quality.

### Step 6: Deployment & Testing

1. Deploy n8n (self-hosted on VPS for $5/month or n8n cloud for $20/month)
2. Build the workflow node by node
3. Run 24-hour test cycle
4. Validate: Are leads qualified? Is scoring accurate?
5. Tune keyword matrix based on false positive rate
6. Set up monitoring alerts for workflow failures

## Output

A complete, deployable lead generation system:
- n8n workflow JSON export (ready to import)
- Keyword matrix document
- AI scoring prompt (fine-tuned for the user's niche)
- Google Sheets template with lead columns
- Slack bot configuration
- Dual monetization plan (use leads + sell leads)

## Creative Latitude

The n8n architecture above is the foundation. Where niche-specific intelligence reveals better data sources, more precise scoring criteria, or unexpected lead channels — deploy them. The best lead gen systems find opportunities nobody else is looking at.

---

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
