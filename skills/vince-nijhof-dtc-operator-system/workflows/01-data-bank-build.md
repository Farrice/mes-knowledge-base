---
description: Build a customer voice data bank — systematic angle library mined from Trustpilot, Amazon, support tickets, and competitor reviews
---

# `/vince-data-bank-build` — Build the Customer Voice Data Bank

The foundational workflow for every other Vince Nijhof skill. Builds the systematic customer voice extraction layer that all downstream angle generation depends on.

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **Pattern 1: The Data Bank as Source-of-Truth Angle Generator**
- **Pattern 2: Messaging-Market Fit as the Second-Order Unlock**
- **Hidden Knowledge 1: The 150-Character Filter**

Then read `references/data-bank-source-mining.md` for the full extraction process.

## When to Run

- New brand onboarding (build the data bank from scratch)
- Existing brand has never systematically mined customer voice
- Quarterly refresh of an existing data bank
- Pre-launch when product is in market but messaging-MF unclear
- Stale ad performance — angles feel invented, not extracted

## Pre-Flight Gate (from genius.md)

| Question | If NO → |
|---|---|
| Does brand have ≥100 reviews across Trustpilot/Amazon/site? | Either too early (data bank can come later) or running customer interviews instead is faster |
| Can you access support tickets (Gorgias / Zendesk export)? | Workflow still runs — tickets are bonus, reviews are minimum viable |
| Will at least 1 strategist USE the data bank for ideation? | Don't build a bank no one queries — invest energy elsewhere first |

## Input Required

- **Brand name**, category, hero product
- **Review source URLs**: Trustpilot listing, Amazon product pages (yours + 3-5 top competitors)
- **Support ticket export**: 90-day CSV from Gorgias / Zendesk (if available)
- **Email export**: any "tell me about your experience" thread / NPS survey (if available)
- **Direct customer comment threads**: Instagram comments on best-performing organic posts (if available)
- **Competitor list**: 3-5 direct competitors whose reviews to mine

## Execution

You are Vince Nijhof's strategist building a data bank. You don't summarize — you extract verbatim quotes, categorize by emotion, and produce angle seeds the creative team can deploy tomorrow.

### Step 1: Source Inventory
List every source you can access. Note source quality (Trustpilot rich, Amazon rich, support tickets dependent on team discipline, emails depend on existence).

### Step 2: Pull + Filter
For each source:
- Pull all available content (or top 200-300 for Amazon, all for Trustpilot)
- Apply 150-character filter — discard anything shorter
- For Amazon: prefer "Verified Purchase" reviews
- Date filter: last 12 months (older = stale messaging-MF risk)
- Bot filter: remove obviously templated reviews

Report: How many reviews per source survived filter? What % of total?

### Step 3: Set Up the AI Project
Create a Claude/Gemini project specifically for this brand's data bank. Upload all filtered reviews + tickets + emails as documents. Standing instruction:

> "You are the customer voice analyst for [BRAND]. When asked, surface specific quotes that match emotional, use-case, or pain themes. Always cite the review source (review #, source platform, date). Filter for substantive (150+ char) content only. Group by emotion when asked."

### Step 4: Categorize by Emotion
Read through filtered reviews. Tag each substantive review with primary emotion (use the 8-emotion framework from `references/emotional-angle-library.md`):
- Fear / Loss / Confidence / Convenience / Belonging / Status / Relief / Curiosity

Many reviews will hit 2-3 emotions. Tag primary + secondary.

### Step 5: Extract 30+ Angle Seeds
For each emotion category, surface the 3-5 strongest verbatim quotes. Total target: 30-50 angle seeds. Format each:

```
EMOTION: [Primary]
SECONDARY: [If applicable]
QUOTE (verbatim, with source): "..."
USE CASE: [Who this customer is, situation]
PAIN POINT: [What they were avoiding / fixing]
OUTCOME LANGUAGE: [Specific phrasing of the win]
HOOK CANDIDATE: [Lift the line that could open an ad]
```

### Step 6: Identify Repeating Themes
Look for emotion-language patterns that appear across 5+ reviews:
- Same phrase variations ("blacked out sleep", "knocked out cold", "didn't hear a thing")
- Same pain point reframings ("I'd tried everything", "I gave up before this")
- Same comparison-anchors ("I had spent $X on others before")

These repeating themes are your messaging-MF spine — the language the customer USES vs. the language the brand currently uses.

### Step 7: Compare to Current Brand Copy
Pull current ad copy + landing page headlines + email subject lines. Audit gap:
- What does the brand say?
- What do customers say?
- Where is the divergence largest?

The gap = your scaling ceiling. Closing the gap = unlocking messaging-MF.

### Step 8: Build the Refresh Cadence
Document the refresh process:
- Monthly: pull new reviews / tickets, add to AI project, surface new themes
- Quarterly: re-categorize the full bank (themes shift over time)
- Pre-campaign: query the bank for the specific emotion the campaign targets

## Output Schema

```markdown
# [Brand] — Customer Voice Data Bank v1

## Sources Mined
| Source | Total Reviews | After 150-char Filter | % Useful |
|---|---|---|---|
| Trustpilot (own) | N | N | % |
| Amazon (own) | N | N | % |
| Trustpilot (Competitor 1) | N | N | % |
| ...etc | | | |

## AI Project Setup
- **Project name**: [Brand] Customer Voice Bank
- **Platform**: Claude / Gemini
- **Standing instruction**: [Full instruction text]
- **Access**: [Who can query]

## 30-50 Angle Seeds (Organized by Emotion)

### FEAR (count: N)
[Angle seed 1, full format]
[Angle seed 2, full format]
...

### LOSS (count: N)
[...]

### CONFIDENCE (count: N)
[...]

[All 8 emotions]

## Repeating Themes (Messaging-MF Spine)
1. **[Theme name]** — appears in N reviews. Customer phrasing: "..."
2. **[Theme name]** — appears in N reviews. Customer phrasing: "..."
...

## Brand-vs-Customer Language Gap
| Brand says | Customer says | Gap implication |
|---|---|---|
| "Premium quality" | "Held up after 2 years of daily use" | Brand abstract; customer specific |
| "Innovative formula" | "Nothing else worked until this" | Brand internal; customer outcome |
| ...etc | | |

## Refresh Cadence
- **Monthly**: [Owner] pulls new reviews, runs categorization
- **Quarterly**: Full re-categorization
- **Pre-campaign**: Query bank for campaign's primary emotion

## Immediate Top 10 Angle Recommendations (Ranked)
1. [Hook candidate + emotion + estimated funnel stage + which campaign to deploy in]
2. ...
```

## Quality Gate

Before delivering, score against `genius.md` rubric. Critical dimensions for this workflow:
- **Customer Voice Grounding**: every angle seed must cite specific verbatim review (9+ required)
- **Emotion Specificity**: each seed must name primary emotion clearly (8+ required)
- **System vs. Tactic**: this is a SYSTEM workflow (refresh cadence, AI project setup, ongoing query pattern) not a one-off audit (9+ required)

If Customer Voice Grounding < 6: automatic veto. Re-run Step 5 with verbatim quotes only.

## Content Type Adaptations

| If output deploys to... | Adjust by... |
|---|---|
| **Static ad copy** | Lift hook candidates verbatim; pair with one image |
| **VSSL script** | Use 3-5 angle seeds for beat structure (pain → discovery → outcome) |
| **Landing page headline** | Test top 3 hook candidates as H1 split tests |
| **Email subject lines** | Repeating themes become subject line A/B variants |
| **Influencer brief** | Send creator the angle seeds + emotion target, not a script |
| **Cold ad concept** | Combine 2-3 seeds across emotions for layered narrative |

## Pairs With

- `/vince-messaging-market-fit-diagnostic` — uses data bank to diagnose brand-vs-customer gap
- `/vince-emotional-angle-engine` — uses data bank seeds to generate ad concepts
- `/vince-x-luke-data-driven-hooks` — feeds Luke Iha's vicious hook craft with real customer voice
