# Workflow 04: Opportunity Matrix Builder

> Prioritize everything from the audit into a phased implementation roadmap.

## Prerequisites
- **Load**: [genius.md](../genius.md)
- **Input Required**: ROI calculations from Workflow 03, process maps from Workflow 01/02
- **Dependencies**: Best after Workflow 03 (needs dollar figures)

## Produces
1. 2×2 Opportunity Matrix (Value × Difficulty)
2. Quick Wins shortlist (deploy first 30 days)
3. Big Swings pipeline (Phase 2-3)
4. Phased implementation timeline with cost estimates
5. Client-ready roadmap presentation

---

## Step 1: Score Each Opportunity

For every bottleneck with an ROI figure, score on two axes:

```
OPPORTUNITY SCORING

| # | Bottleneck | Annual Waste | Value Score (1-10) | Difficulty Score (1-10) | Quadrant |
|---|-----------|-------------|-------------------|----------------------|----------|
| 1 | [Process] | $[X] | [Higher $ = higher] | [Tech complexity + change mgmt] | [QW/BS/FI/DP] |
| 2 | [Process] | $[X] | [Score] | [Score] | [Quadrant] |
...

VALUE SCORING CRITERIA:
- 8-10: >$100K annual waste, affects core revenue process
- 5-7: $25K-$100K annual waste, affects supporting process
- 1-4: <$25K annual waste, convenience improvement

DIFFICULTY SCORING CRITERIA:
- 1-3: Off-the-shelf solution, minimal behavior change, <1 week
- 4-6: Custom configuration needed, moderate training, 2-4 weeks
- 7-10: Complex integration, significant change management, 1-3 months

QUADRANTS:
- QW (Quick Wins): High Value + Low Difficulty → DO FIRST
- BS (Big Swings): High Value + High Difficulty → PLAN FOR PHASE 2
- FI (Fill-Ins): Low Value + Low Difficulty → DO IF TIME ALLOWS
- DP (Deprioritize): Low Value + High Difficulty → DON'T DO
```

---

## Step 2: Quick Wins Shortlist

```
QUICK WINS — DEPLOY FIRST (Next 30 Days)

These are the "springboard" — prove ROI fast to fund the big swings.

| Priority | Bottleneck | Annual Savings | Implementation Cost | Payback | Difficulty |
|----------|-----------|---------------|--------------------|---------|-----------| 
| 1 | [Easiest high-value win] | $[X] | $[X] | [X] days | [Low] |
| 2 | [Second easiest] | $[X] | $[X] | [X] days | [Low] |
| 3 | [Third] | $[X] | $[X] | [X] days | [Low] |

TOTAL QUICK WIN VALUE: $[X]/year
TOTAL QUICK WIN COST: $[X]
COMBINED PAYBACK: [X] days

PURPOSE: These results become the proof that sells Phase 2.
"We saved you $[X] in the first month. Here's what Phase 2 looks like."
```

---

## Step 3: Phased Implementation Roadmap

```
PHASED ROADMAP

PHASE 1: QUICK WINS (Weeks 1-4)
├── [Win 1]: [Description] — $[savings/yr] — [owner]
├── [Win 2]: [Description] — $[savings/yr] — [owner]
└── [Win 3]: [Description] — $[savings/yr] — [owner]
    Investment: $[X] | Expected Savings: $[X]/year
    Success Metric: [Measurable outcome by Day 30]

PHASE 2: BIG SWINGS (Months 2-4)
├── [Swing 1]: [Description] — $[savings/yr] — [owner]
├── [Swing 2]: [Description] — $[savings/yr] — [owner]
└── [Swing 3]: [Description] — $[savings/yr] — [owner]
    Investment: $[X] | Expected Savings: $[X]/year
    Prerequisites: Phase 1 results proven, AI Champion engaged
    Success Metric: [Measurable outcome by Month 4]

PHASE 3: OPTIMIZATION (Months 5-6)
├── Fine-tune Phase 1-2 implementations
├── Fill-in opportunities from the matrix
└── Establish maintenance/advisory cadence
    Investment: $[X]/month | Advisory Retainer: $[X]/month

TOTAL 6-MONTH INVESTMENT: $[X]
TOTAL ANNUAL SAVINGS: $[X]
ROI MULTIPLE: [X]x
```

---

## Step 4: Chassis Check

Before finalizing the roadmap, apply the Lamborghini Chassis test:

```
CHASSIS ASSESSMENT

"Where does all your company data live?"

If the answer involves 5+ disconnected systems:
→ INSERT "Phase 0: Centralized Knowledge Base" before Phase 1
→ This is the chassis that everything else bolts onto
→ Without it, you're putting Lamborghini parts on a Toyota Corolla

Current Data Architecture:
- CRM: [Tool name]
- Project Management: [Tool name]
- Communication: [Tool name]
- Documents: [Tool name]
- Finance: [Tool name]
- Other: [List all]

TOTAL DISCONNECTED SYSTEMS: [X]

CHASSIS RECOMMENDATION:
□ Systems < 5: Proceed to Phase 1 (chassis adequate)
□ Systems 5-10: Add Phase 0 lightweight integration layer
□ Systems 10+: Phase 0 is MANDATORY — centralized knowledge base first
```

---

## Output Schema

The deliverable is a **Phased Opportunity Roadmap** containing:

```
1. Opportunity Scoring table (# | Bottleneck | Annual Waste | Value Score |
   Difficulty Score | Quadrant [QW/BS/FI/DP]) — every scored opportunity
   from the ROI report appears exactly once
2. Quick Wins Shortlist table (Priority | Bottleneck | Annual Savings |
   Implementation Cost | Payback | Difficulty) — ranked, <30-day payback
3. Phased Roadmap block (Phase 1 Quick Wins / Phase 2 Big Swings /
   Phase 3 Optimization) each with Investment, Expected Savings, and a
   named Success Metric
4. Chassis Assessment block — Current Data Architecture inventory,
   Total Disconnected Systems count, and the explicit recommendation
   (Proceed / Add Phase 0 lightweight layer / Phase 0 mandatory)
5. Totals: 6-Month Investment, Total Annual Savings, ROI Multiple
```

Fill-Ins and Deprioritized items must be listed explicitly, not omitted — their presence is what proves the matrix is complete rather than cherry-picked.

## Quality Gate

- [ ] Every opportunity scored on both Value AND Difficulty axes
- [ ] Quick wins identified with <30 day payback
- [ ] Big swings have clear prerequisites (including Phase 1 proof)
- [ ] Chassis check completed (data fragmentation assessed)
- [ ] Roadmap phased in logical order (never big swing before quick win)
- [ ] Each phase has a success metric and investment figure
- [ ] Fill-ins and deprioritized items explicitly listed (shows thoroughness)
