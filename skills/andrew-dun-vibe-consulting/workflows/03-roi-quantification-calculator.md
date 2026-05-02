# Workflow 03: ROI Quantification Calculator

> Convert every identified inefficiency into a dollar figure that makes NOT acting feel irrational.

## Prerequisites
- **Load**: [genius.md](../genius.md)
- **Input Required**: Process maps from Workflow 02 (or Workflow 01 discovery notes), employee counts per process, approximate loaded hourly costs
- **Dependencies**: Works standalone with interview notes, but best after Workflow 02

## Produces
A complete ROI quantification report containing:
1. Per-process waste calculations using the Andrew Dun formula
2. Aggregate annual waste total across all identified bottlenecks
3. Conservative / moderate / aggressive scenario modeling
4. 12-month payback analysis
5. Investment recommendation with ROI multiple

---

## Step 1: Bottleneck Inventory

List every inefficiency identified from discovery/process mapping:

```
BOTTLENECK INVENTORY

| # | Department | Process | Current State | Time Wasted Per Occurrence | Frequency |
|---|-----------|---------|--------------|---------------------------|-----------|
| 1 | [Dept] | [Process name] | [What happens now] | [X min/hr per occurrence] | [X times/day per person] |
| 2 | [Dept] | [Process name] | [What happens now] | [X min/hr per occurrence] | [X times/day per person] |
| 3 | [Dept] | [Process name] | [What happens now] | [X min/hr per occurrence] | [X times/day per person] |
...
```

---

## Step 2: Apply the ROI Formula

For EACH bottleneck, calculate:

```
THE ANDREW DUN ROI FORMULA

Time Wasted × People × Working Days/Year × Loaded Hourly Cost = Annual Waste

VARIABLES:
- Time Wasted: Minutes or hours wasted PER DAY per person on this process
- People: Number of employees affected by this specific process
- Working Days/Year: 260 (standard) or company-specific
- Loaded Hourly Cost: Salary + benefits + overhead ÷ 2,080 hours
  Rule of thumb: Multiply base hourly rate by 1.3-1.5 for loaded cost

EXAMPLE (SDR Team — from Andrew's case study):
- Time Wasted: 2 hours/day (manual morning prospecting)
- People: 8 SDRs
- Working Days: 260
- Loaded Hourly Cost: $40/hr
- CALCULATION: 2 × 8 × 260 × $40 = $166,400/year

This is ONE process. Most companies have 5-15 identifiable waste areas.
```

---

## Step 3: Per-Process Calculation Sheet

```
ROI QUANTIFICATION — PER PROCESS

BOTTLENECK #[X]: [Process Name]
Department: [Department]
Affected Employees: [Number]

Current State:
- Time spent per occurrence: [X minutes]
- Occurrences per day per person: [X]
- Total daily waste per person: [X minutes = X hours]
- Total daily waste (all people): [X hours]

AI/Automation Target State:
- Estimated time after optimization: [X minutes per occurrence]
- Time savings per person per day: [X minutes]
- Reduction percentage: [X%]

ANNUAL WASTE CALCULATION:
┌─────────────────────────────────────────────────────┐
│ [X hrs/day] × [X people] × [260 days] × [$X/hr]   │
│ = $[ANNUAL WASTE]                                    │
│                                                      │
│ With [X%] reduction: $[ANNUAL SAVINGS]               │
└─────────────────────────────────────────────────────┘

Confidence Level: [HIGH / MEDIUM / LOW]
Data Source: [Operator interview / Time tracking / Estimate]
```

---

## Step 4: Scenario Modeling

```
THREE-SCENARIO ROI MODEL

| Bottleneck | Conservative (50% reduction) | Moderate (70% reduction) | Aggressive (90% reduction) |
|-----------|------------------------------|--------------------------|---------------------------|
| [Process 1] | $[X] | $[X] | $[X] |
| [Process 2] | $[X] | $[X] | $[X] |
| [Process 3] | $[X] | $[X] | $[X] |
| [Process 4] | $[X] | $[X] | $[X] |
| [Process 5] | $[X] | $[X] | $[X] |
| **TOTAL** | **$[X]** | **$[X]** | **$[X]** |

NOTES:
- Conservative: Only the easiest wins, partial automation
- Moderate: Full automation of identified processes with expected adoption friction
- Aggressive: Full automation + team fully adopts + secondary efficiencies captured
- ALWAYS present the conservative number to the client first (underpromise)
```

---

## Step 5: 12-Month Payback Analysis

```
PAYBACK ANALYSIS

Total Investment Required:
- Diagnostic/Audit Fee: $[X]
- Implementation Cost (estimated): $[X]
- Tool/Platform Costs (annual): $[X]
- Training/Change Management: $[X]
- TOTAL INVESTMENT: $[X]

Annual Savings (Conservative): $[X]
Annual Savings (Moderate): $[X]

PAYBACK PERIOD:
- Conservative: [X] months
- Moderate: [X] months

ROI MULTIPLE:
- Conservative: [X]x return on investment in Year 1
- Moderate: [X]x return on investment in Year 1

BENCHMARK: Enterprise considers 10-year payback acceptable.
Under 12 months = HOME RUN by any standard.

3-YEAR VALUE:
- Conservative 3-year savings: $[X]
- Minus total 3-year investment: $[X]
- NET VALUE CREATED: $[X]
```

---

## Step 6: Executive Summary for Client

```
ROI QUANTIFICATION — EXECUTIVE SUMMARY

Client: [Company Name]
Date: [Date]
Prepared By: [Your Name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUR BUSINESS IS CURRENTLY WASTING:

$[TOTAL ANNUAL WASTE] per year
across [X] identified process bottlenecks
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TOP 3 WASTE AREAS:
1. [Process] — $[X]/year ([X] hrs/day across [X] people)
2. [Process] — $[X]/year ([X] hrs/day across [X] people)
3. [Process] — $[X]/year ([X] hrs/day across [X] people)

PROPOSED SOLUTION INVESTMENT: $[X]
EXPECTED PAYBACK: [X] months (conservative)
YEAR 1 ROI: [X]x return

"Every month you wait costs approximately $[monthly waste]."

NEXT STEP: Review the Opportunity Matrix (Workflow 04) to determine
implementation priority and phasing.
```

---

## Quality Gate

Before delivering, verify:
- [ ] Every bottleneck has all four formula variables filled with REAL data (no placeholders)
- [ ] Loaded hourly cost includes benefits + overhead (not just base salary)
- [ ] Three scenarios presented (conservative, moderate, aggressive)
- [ ] Conservative scenario STILL shows compelling ROI (>2x)
- [ ] Payback period calculated against 12-month benchmark
- [ ] Monthly waste figure included to create urgency ("every month you wait...")
- [ ] All numbers traceable back to operator interview data
- [ ] Executive summary is jargon-free and presents the total waste figure PROMINENTLY
