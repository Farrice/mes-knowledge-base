---
description: Track and manage the consulting practice's revenue pipeline — prevent the "great at delivery, no pipeline" failure mode
---

# Consulting Pipeline Dashboard

> Load `genius.md` before executing. Research: 5% of consulting practice failures come from ignoring sales pipeline. $300K+ solos spend 8 hrs/week on acquisition.

## When to Use
- Weekly pipeline review (every Monday morning)
- Monthly revenue forecasting
- Diagnosing why revenue is stalling despite good delivery
- Planning acquisition activities for the week
- Preparing for quarterly business reviews

## Steps

### 1. Pipeline Stage Definitions

Every prospect moves through these stages:

| Stage | Name | Description | Avg. Duration | Conversion Rate |
|-------|------|-------------|---------------|-----------------|
| **S0** | Suspect | Identified as potential fit — no contact yet | — | — |
| **S1** | First Contact | Initial outreach or inbound — conversation started | 1-2 weeks | 40% → S2 |
| **S2** | Discovery Call | Scheduled or completed exploratory conversation | 1 week | 60% → S3 |
| **S3** | Scorecard/Mini-Audit | Delivering AI Readiness Scorecard (Workflow 13) | 1-2 weeks | 65% → S4 |
| **S4** | Diagnostic Proposed | Full diagnostic engagement proposed (Workflow 12) | 1-2 weeks | 65% → S5 |
| **S5** | Diagnostic Active | Full diagnostic underway | 2-4 weeks | 85% → S6 |
| **S6** | Implementation Proposed | Post-diagnostic, implementation contract proposed | 1-2 weeks | 70% → S7 |
| **S7** | Active Client | Engaged in implementation or retainer | Ongoing | 80% → S8 |
| **S8** | Retainer Client | Monthly advisory/maintenance retainer | Ongoing | — |

### 2. Weekly Pipeline Snapshot

Every Monday, populate this dashboard:

```
PIPELINE DASHBOARD — Week of [Date]

REVENUE TARGETS
├── Monthly target: $[X]
├── Quarterly target: $[X]
├── YTD actual: $[X]
└── YTD target: $[X]

PIPELINE HEALTH
├── Total pipeline value: $[X] (sum of all active deals × probability)
├── Weighted pipeline: $[X] (each deal × stage conversion rate)
├── Pipeline-to-target ratio: [X]x (need 3x minimum)
└── Average deal size: $[X]

STAGE COUNTS
├── S0 Suspects: [N]
├── S1 First Contact: [N]
├── S2 Discovery: [N]
├── S3 Scorecard: [N]
├── S4 Diagnostic Proposed: [N]
├── S5 Diagnostic Active: [N]
├── S6 Implementation Proposed: [N]
├── S7 Active Client: [N]
└── S8 Retainer: [N]

THIS WEEK'S PRIORITY ACTIONS
1. [Move X from S_ to S_]
2. [Follow up with Y]
3. [Send proposal to Z]
```

### 3. Acquisition Activity Tracker

Track the 8 hrs/week dedicated to pipeline building:

| Activity | Weekly Target | Actual | Channel |
|----------|--------------|--------|---------|
| LinkedIn posts published | 3 | [N] | Content marketing |
| LinkedIn DMs sent | 10 | [N] | Direct outreach |
| POC Teardown videos created | 1 | [N] | Authority content |
| Discovery calls completed | 2 | [N] | Pipeline conversion |
| Scorecards delivered | 1 | [N] | Pipeline conversion |
| Referral requests made | 2 | [N] | Referral flywheel |
| Community engagement actions | 5 | [N] | Network building |

**Rule**: If any activity is at 0 for 2 consecutive weeks, that channel is dying. Diagnose and fix.

### 4. Revenue Forecasting Model

**Monthly Revenue Calculation:**

```
Forecast = (Active Diagnostics × $Avg × Close Rate)
         + (Proposed Implementations × $Avg × Close Rate)
         + (Active Retainers × Monthly Rate)
         + (Pipeline S3-S4 × $Avg × 0.30)
```

**Revenue Mix Health Check:**

| Revenue Type | Healthy % | Your % | Status |
|-------------|-----------|--------|--------|
| Project revenue (diagnostics + implementations) | 40-60% | [X]% | [OK/WARNING] |
| Recurring revenue (retainers + advisory) | 40-60% | [X]% | [OK/WARNING] |
| New client revenue | 30-50% | [X]% | [OK/WARNING] |
| Existing client revenue | 50-70% | [X]% | [OK/WARNING] |

**Warning signals:**
- Recurring < 30% → You're on the project treadmill
- New client < 20% → Pipeline is drying up
- Pipeline-to-target ratio < 3x → Not enough deals in the funnel

### 5. Client Lifecycle Tracker

For each active/past client, track the lifecycle value:

```
CLIENT: [Name]
Entry Date: [Date]
Entry Point: [Scorecard / Diagnostic / Referral]
Engagement History:
  ├── Phase 1: [Diagnostic] — $[X] — [Date]
  ├── Phase 2: [Quick Win Implementation] — $[X] — [Date]
  ├── Phase 3: [Full Implementation] — $[X] — [Date]
  └── Phase ∞: [Retainer] — $[X]/mo — [Start Date]
Total LTV: $[X]
Referrals Generated: [N]
Case Study: [Yes/No]
Testimonial: [Yes/No]
NPS Score: [N]
Next Action: [Date + Description]
```

### 6. Monthly Pipeline Review

On the 1st of each month, run this diagnostic:

**Pipeline Health Metrics:**
- **Velocity**: How fast are deals moving through stages? (Avg days per stage)
- **Conversion**: Where are deals dying? (Stage with lowest conversion rate)
- **Value**: Is average deal size growing or shrinking?
- **Mix**: Are you too dependent on one client or one engagement type?

**Decision Framework:**

| Metric | If Healthy | If Warning | Action |
|--------|-----------|------------|--------|
| Pipeline velocity | < 4 weeks avg per stage | > 6 weeks | Follow up more aggressively or disqualify stale deals |
| Stage conversion | > 50% at each stage | < 40% at any stage | Diagnose: bad qualification, weak proposals, or wrong audience? |
| Deal size | Growing quarter-over-quarter | Shrinking | Are you discounting? Competing on price? Check positioning |
| Client concentration | No client > 30% of revenue | One client > 50% | Urgent: diversify immediately |

## Output Schema

The deliverable is a **Weekly Pipeline Dashboard** (Step 2 format) plus its two supporting trackers, refreshed every Monday:

| Component | Required Fields |
|---|---|
| Pipeline Dashboard | Revenue targets (monthly/quarterly/YTD), pipeline health (total, weighted, ratio, avg deal size), stage counts S0-S8, this week's priority actions |
| Acquisition Activity Tracker | All 7 activities with Weekly Target vs. Actual, channel labeled |
| Revenue Forecasting Model | The 4-term forecast formula computed with real numbers, plus the Revenue Mix Health Check table (4 rows, OK/WARNING flagged) |

Monthly (1st of month) additionally requires the **Monthly Pipeline Review** — velocity, conversion, value, mix metrics against the Decision Framework table, each flagged Healthy or Warning with a named action if Warning.

## Quality Gate

| Criterion | Pass Threshold |
|-----------|---------------|
| Dashboard populated weekly | Every Monday |
| Pipeline-to-target ratio | ≥ 3x |
| Recurring revenue % | ≥ 30% |
| Acquisition activities logged | ≥ 6/7 categories active |
| Monthly review completed | By 5th of each month |

## Pairs With
- `09-first-client-engine.md` — Feeds S0-S2 with warm outreach
- `13-ai-readiness-scorecard.md` — Feeds S3 with qualified prospects
- `12-proposal-sow-architect.md` — Converts S4-S6 with phased proposals
- `08-advisory-retainer-builder.md` — Converts S7 to S8
- `@sharran` — Sharran's constraint-based scaling identifies which pipeline stage is the bottleneck
- `@lara-acosta` — Lara's Revenue Bridge feeds S1-S2 through LinkedIn acquisition
