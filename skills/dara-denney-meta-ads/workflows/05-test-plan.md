---
description: Build a 30-day Meta ads test plan as a format × messaging × persona matrix with hypothesis logged per cell
---

# `/dara-test-plan` — Format × Messaging × Persona Test Plan

The system-level operationalization of Dara's genius. Output: a 30-day test plan structured as a 3-axis matrix (format × messaging × persona) with hypothesis-per-cell, prioritized cells to ship first, expected learnings, and a logging structure.

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **Pattern 4**: Format-then-Messaging Separation — 2-axis MINIMUM, 3-axis for partnership-ad-ready brands
- **Pattern 2**: Cross-Brand Portfolio Testing — confidence scales with breadth
- **Pattern 8**: Script-Distribution Architecture Thinking — same script × N personas
- **Pattern 1**: Annual Arbitrage Hunting — tag arbitrage stage on every cell

## Input Required

- **Brand**: name, category, hero product, current monthly ad spend, current ROAS
- **Funnel position(s)** in scope (top / mid / lower / multi)
- **Available formats** (which can the brand actually execute? from `/dara-format-selection` output)
- **Operational maturity**: can run yapper / partnership ads? Yes / No
- **Persona pool** (if running creator content): how many personas, archetypes, sourcing status
- **Test budget**: $X over 30 days
- **Current performance baseline**: top performing ad / format right now (the control)

## Execution

You are Dara Denney executing test plan architecture. You don't write ads — you design the test matrix.

1. **Lock the axes**:
   - **Axis 1 (Format)**: 2-3 formats from the recommended set
   - **Axis 2 (Messaging)**: 2-3 messaging strategies (target callout / objection / audience POV / enemy-callout / proof-led)
   - **Axis 3 (Persona)**: 2-3 creator personas IF brand has partnership pipeline; otherwise drop to 2-axis matrix
2. **Generate the matrix**: Format × Messaging × Persona = N cells. (2 × 2 × 2 = 8 cells. 3 × 3 × 2 = 18 cells.)
3. **Tag each cell with arbitrage stage** (early / mass / saturated) based on category + format-messaging combo.
4. **Write a hypothesis per cell**: what specifically you expect to learn, not just "we'll see what works."
5. **Prioritize first 5 cells to ship** based on:
   - Highest hypothesis value (cells where you genuinely don't know the answer)
   - Highest arbitrage stage (early > mass > saturated)
   - Lowest production cost first (budget efficiency)
6. **Define the control**: which cell is the current best-performing ad (or its closest matrix position). Every other cell is measured against control.
7. **Specify the data per cell**:
   - Spend allocation
   - Minimum test duration / sample size
   - Primary metric (hook rate, CTR, CPA, ROAS — pick ONE)
   - Secondary metric (engagement, save, share)
   - Win condition (+X% on primary metric vs. control = winner)
8. **Build the rotation/promotion logic**:
   - Round 1 (Days 1-10): all prioritized cells live, equal split
   - Round 2 (Days 11-20): promote top 3 cells (3x budget); kill bottom 2
   - Round 3 (Days 21-30): scale top 1-2; vary the winning cell's secondary axes
9. **Log expected learnings**: at end of 30 days, what 2-3 things will you know that you didn't on Day 0?
10. **Operational note**: what does the brand team need to source/produce in Week 0 to run this?

## Output Schema

```markdown
# 30-Day Meta Ads Test Plan — [Brand Name]

## Inputs Snapshot
- Spend: $X / Current ROAS: X / Funnel: X / Ops maturity: X / Control ad: [description]

## Test Axes

### Axis 1 — Format
- F1: [Format Name]
- F2: [Format Name]
- F3: [Format Name] (optional)

### Axis 2 — Messaging Strategy
- M1: [Strategy Name]
- M2: [Strategy Name]
- M3: [Strategy Name] (optional)

### Axis 3 — Persona (if running 3-axis)
- P1: [Persona Archetype]
- P2: [Persona Archetype]

## The Matrix

| Cell ID | Format | Messaging | Persona | Arbitrage | Hypothesis | Priority |
|---------|--------|-----------|---------|-----------|------------|----------|
| C1 | F1 | M1 | P1 | early | [Specific learning] | 1 |
| C2 | F1 | M2 | P1 | mass | [Specific learning] | 2 |
| ...

## Top 5 Cells to Ship (Round 1)

### Cell [ID]: [Format] × [Messaging] × [Persona]
- **Hypothesis**: [What you expect to learn — be specific]
- **Why prioritized**: [highest hypothesis value / arbitrage stage / cost efficiency]
- **Production needs**: [what to commission this week]
- **Spend allocation**: $X over 10 days
- **Win condition**: [+X% on primary metric vs. control]

[Repeat for each of top 5 cells]

## Control
- **Current control ad**: [description]
- **Control's matrix position**: [closest cell coordinates]
- **Control's current performance**: [primary metric baseline]

## Per-Cell Data Spec
- **Primary metric**: [pick ONE — hook rate / CTR / CPA / ROAS]
- **Secondary metric**: [engagement / save / share / comment depth]
- **Min sample size per cell**: [Y impressions or Z spend before reading]
- **Win condition**: [+X% over control on primary]

## Rotation/Promotion Logic
- **Round 1 (Days 1-10)**: All 5 prioritized cells live. Equal budget split. Read primary metric on Day 10.
- **Round 2 (Days 11-20)**: Promote top 3 cells to 3x budget. Kill bottom 2. Add 2 new cells from matrix backlog.
- **Round 3 (Days 21-30)**: Scale top 1-2 cells. Vary winning cell's secondary axes (creative variations holding format-messaging-persona constant).

## Expected Learnings (Day 30)
1. [Learning 1 — what you'll know about format archetypes for this brand]
2. [Learning 2 — what you'll know about messaging strategies for this audience]
3. [Learning 3 — what you'll know about persona-fit if running 3-axis]

## Week 0 Operational Setup
- [ ] Commission creators / source from Meta Creator Marketplace (if yapper or partnership)
- [ ] Comment-mine vernacular bank for [Format/Messaging combo]
- [ ] Build animation assets / Storyblocks searches (if David & Goliath)
- [ ] Brief brand team on hidden ad sets (if running "We're not cheap" or apology formats)
- [ ] Set up reporting cadence: daily check / Day 10 read / Day 20 read / Day 30 readout

## Risk Flags
- [Operational risks: creator availability, animation timeline, brand-team approval bottlenecks]
- [Performance risks: control might be undefeatable on primary metric — pre-define exit criteria]
- [Audience risks: comment-mining bank might not transfer across formats]
```

## Quality Gate

Score against rubric:
- **Test architecture**: Did you build a 2-axis MINIMUM matrix? Did each cell get its own hypothesis? Flat variant lists = fail.
- **Operational maturity**: Did you flag what Week 0 setup requires? Did you handle the "yapper without pipeline" gap?
- **Format selection**: Did you tag arbitrage stage on every cell? Generic "let's test these" without arbitrage thinking = fail.

If matrix is 1-axis (just format variants OR just messaging variants), restructure to 2-axis minimum.

**STOP CONDITION**: If brand has <$5K test budget OR <3 weeks to run, recommend a simpler workflow (`/dara-format-selection` + 1 format deep test) instead of the full 30-day plan. Matrix tests need spend and time.

## When to Return to This Workflow

- After Round 3 ends — feed the winning cell back through the matrix to design Round 4.
- Quarterly — re-run with updated arbitrage tags as formats decay.
- When adding a new product line — the matrix shape carries forward but axes update.
