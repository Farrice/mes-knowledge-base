---
description: Deploy Instagram content system across a real estate team or brokerage — onboarding, training, and ongoing production
---

# /enrico-team — Team Deployment Engine

Deploy the complete Incarnati Instagram system across a real estate team or brokerage. Handles onboarding, individual format discovery, shared asset creation, production workflows, and performance tracking. Designed for MyHouseSellers (5 agents) and scalable to Equity Union (100+ agents).

## Usage

```
/enrico-team [team name] [number of agents]
```

Examples:
- `/enrico-team "MyHouseSellers" 5`
- `/enrico-team "Equity Union" 100`

## Context Loading

// turbo-all

Before executing, read:
1. `skills/enrico-incarnati-instagram-realestate/genius.md` — Full genius context
2. All workflow files (01-09) — need full system context for team deployment
3. `skills/enrico-incarnati-instagram-realestate/references/profile-optimization-checklist.md`

## Steps

### Step 1: Team Intelligence

```
TEAM PROFILE
────────────
Team/Brokerage: [Name]
Owner/Team Lead: [Name]
Number of Agents: [N]
Market Area(s): [Cities/regions served]
Current Instagram Presence: [Does the TEAM have a page? Individual agents?]
Tech Stack: [ManyChat? CRM? Email platform? Currently: NONE]
Budget: [For tools, content production, design]

AGENTS ROSTER:
| # | Name | Handle | Market | Niche | Experience | Content Status |
|---|------|--------|--------|-------|-----------|----------------|
| 1 | [Name] | @[handle] | [City] | [Niche] | [Years] | [Active/Inactive/None] |
| 2 | ... | | | | | |
| 3 | ... | | | | | |
```

### Step 2: Team Audit (Batch)

Run `/enrico-audit` (workflow 09) on each agent. Produce a comparative analysis:

```
TEAM INSTAGRAM SCORECARD
────────────────────────
                    Agent 1   Agent 2   Agent 3   Agent 4   Agent 5   TEAM AVG
SEO Name:          [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
Bio:               [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
Link Store:        [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
Content Strategy:  [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
Local Authority:   [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
Lead Capture:      [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
Stories:           [X/10]    [X/10]    [X/10]    [X/10]    [X/10]    [X/10]
────────────────────────────────────────────────────────────────────────────
TOTAL:             [XX/70]   [XX/70]   [XX/70]   [XX/70]   [XX/70]   [XX/70]
GRADE:             [Grade]   [Grade]   [Grade]   [Grade]   [Grade]   [Grade]

TOP WEAKNESS ACROSS TEAM: [e.g., "Nobody has lead capture set up"]
BIGGEST QUICK WIN: [e.g., "Fix all 5 bios in an afternoon = immediate improvement"]
```

### Step 3: Shared Assets Creation

Build team-wide assets that ALL agents use:

```
SHARED ASSET LIBRARY
────────────────────

1. LEAD MAGNET SUITE (branded to team, not individual agents)
   □ "[City] First-Time Buyer Checklist" — [Team Name] branded
   □ "[City] Buyer's Guide [Year]" — [Team Name] branded
   □ "Moving to [City] Relocation Kit" — [Team Name] branded
   □ "Off-Market Listings This Week" — team-wide insider list
   
2. MANYCHAT TEMPLATES
   □ Master ManyChat account (or individual accounts with shared flows)
   □ Keyword trigger library (standardized across team)
   □ Auto-DM templates for each lead magnet
   □ Follow-up sequences (hot/warm/future)
   
3. STAN STORE / LINK STORE
   □ Individual link stores per agent (personalized but templated)
   □ Each follows the same structure: Lead magnet → Work with me → Listings → Market update
   
4. CONTENT TEMPLATES
   □ Canva template for market update pin post (swap data monthly)
   □ Canva template for Digital Clipboard overlay
   □ Canva template for S-Tier Ranking visual
   □ Reel cover templates (consistent brand look)
   □ Story templates (polls, questions, branded)
   
5. HASHTAG LIBRARY
   □ 20 city-specific hashtags (shared across team)
   □ 10 niche-specific hashtags per agent
   □ 10 general real estate hashtags
```

### Step 4: Individual Agent Onboarding (Per Agent)

Run this sequence for each agent on the team:

```
AGENT ONBOARDING SEQUENCE — [Agent Name]
─────────────────────────────────────────

WEEK 1: PROFILE + FORMAT
Day 1-2: Run /enrico-curb-appeal → Fix profile
Day 3-4: Run /enrico-format → Discover their signature format
Day 5: Set up link store + lead magnet page
Deliverable: Optimized profile + format blueprint

WEEK 2: FIRST CONTENT
Day 1: Run /enrico-expand → Pick their first topic, generate 5 scripts
Day 2-3: Batch film all 5 pieces
Day 4: Edit and schedule
Day 5: Run /enrico-stories → Set up stories system
Deliverable: First week of content scheduled + stories flowing

WEEK 3: LEAD ENGINE
Day 1: Set up ManyChat account
Day 2: Configure keyword triggers + auto-DMs
Day 3: Launch Friday Night Strategy
Day 4: Run /enrico-leads → Full lead pipeline setup
Day 5: First lead magnet live and delivering
Deliverable: Complete lead capture system operational

WEEK 4: PROXIMITY + SPRINT MODE
Day 1-2: Run /enrico-proximity → Local content strategy
Day 3: Film first local business spotlight
Day 4-5: Run /enrico-sprint → First full production week
Deliverable: Agent in self-sustaining sprint mode
```

### Step 5: Ongoing Production System

```
TEAM WEEKLY WORKFLOW
────────────────────

MONDAY (Team Lead):
□ Share weekly market data with all agents (for market update content)
□ Share any local news/development stories (for green screen reactions)
□ Distribute content topics for the week

TUESDAY-THURSDAY (Each Agent):
□ Batch film 3-5 Reels (2-3 hour session)
□ Edit and schedule content for the week
□ Post daily stories

FRIDAY (Everyone):
□ Deploy Friday Night Strategy at 5 PM
□ Monitor "checklist" keyword DMs

WEEKEND (Team Lead):
□ Review team performance metrics
□ Share top-performing content across team chat
□ Identify what to double down on next week

MONTHLY (Team Lead):
□ Run /enrico-audit on each agent → track score progression
□ Compile team performance report
□ Update shared lead magnets with fresh data
□ Analyze which formats/topics generate the most leads
```

### Step 6: Performance Dashboard

```
TEAM PERFORMANCE METRICS (MONTHLY)
───────────────────────────────────

                    Agent 1   Agent 2   Agent 3   Agent 4   Agent 5   TOTAL
Reels posted:       [N]       [N]       [N]       [N]       [N]       [N]
Stories/day avg:    [N]       [N]       [N]       [N]       [N]       [N]
Keyword comments:   [N]       [N]       [N]       [N]       [N]       [N]
DM conversations:   [N]       [N]       [N]       [N]       [N]       [N]
Emails captured:    [N]       [N]       [N]       [N]       [N]       [N]
Leads generated:    [N]       [N]       [N]       [N]       [N]       [N]
Deals closed:       [N]       [N]       [N]       [N]       [N]       [N]
Revenue from IG:    $[N]      $[N]      $[N]      $[N]      $[N]      $[N]

AUDIT SCORE PROGRESSION:
Month 1: [XX/70] → Month 2: [YY/70] → Month 3: [ZZ/70]

TOP PERFORMING:
- Best Reel this month: [Agent] — [Title] — [Views/Engagement]
- Most leads captured: [Agent] — [N leads]
- Biggest deal from Instagram: [Agent] — $[Amount]
```

### Step 7: Equity Union Pitch Package

```
THE PITCH (for 100+ agent deployment):
──────────────────────────────────────

PROBLEM:
"Your agents are spending money on Zillow leads and cold calling
while their competitors are building audiences on Instagram for free.
The agents who invest in social-first marketing NOW will dominate in 2026."

PROOF:
"We deployed this system on MyHouseSellers (5 agents) and here's what happened:
- Average audit score went from [X]/70 to [Y]/70 in 30 days
- [N] leads generated in month 1 from Instagram alone
- [N] deals closed that originated from Instagram content
- Each agent now has [N]+ email subscribers they OWN"

THE OFFER:
Phase 1 (Month 1): Audit all agents → Identify top 20 for pilot program
Phase 2 (Month 2-3): Onboard pilot group → Full system deployment
Phase 3 (Month 4+): Rolling onboarding for remaining agents

WHAT AGENTS GET:
1. Complete profile optimization (Digital Curb Appeal)
2. Signature format discovery (unique to each agent)
3. Weekly content sprint calendar with scripts
4. ManyChat lead capture system
5. Lead magnet suite (team-branded)
6. Monthly performance tracking

WHAT THE BROKERAGE GETS:
1. Differentiation — "The brokerage where agents are Instagram-famous"
2. Recruitment magnet — "Join us and get a social media system built for you"
3. Client pipeline — every agent generating leads independently
4. Brand visibility — 100+ agents posting quality content = market saturation

PRICING MODEL:
Option A: Per-agent monthly retainer ($X/agent/month)
Option B: Team package (flat fee for all agents)
Option C: Revenue share on deals sourced from Instagram
```

### Step 8: Deliverable

Produce a conversation artifact containing:
1. Team Scorecard (all agents audited)
2. Shared Asset Library — spec sheets for everything to build
3. Individual Onboarding Sequences (per agent)
4. Weekly Team Workflow
5. Performance Dashboard template
6. Equity Union Pitch Package (ready to present)
7. Tech Stack Recommendations (ManyChat, Stan Store, Canva, Meta Business Suite)
8. Cost analysis (tools needed, time investment per agent)
9. 90-day projected outcomes

---

## Stacking Chains

- **After running `/enrico-audit` on @_jiing** → Use her as Case Study #1 for the pitch
- **Compound with Samuel Thompson** → Layer business growth frameworks onto the pitch
- **Compound with Sabri Suby** → Design the pitch presentation using selling frameworks
- **This workflow IS the Equity Union consulting play** — it turns Antigravity into a brokerage-scale service
