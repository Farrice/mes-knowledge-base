---
description: Diagnose the ONE real constraint in any business — not the symptom, not the wish, the actual bottleneck
---

# Constraint Isolation Audit

> Load `skills/sharran-srivatsaa-scaling/genius.md` before executing.

## Inputs Required
- **Business description** (What does the business do? Revenue? Team size? Stage?)
- **Perceived problem** (What does the owner THINK is wrong?)
- **Recent metrics** (Last 90 days: revenue, leads, conversion rates, churn, capacity utilization — whatever is available)
- **Optional**: Previous strategic actions taken and their results

> **🔒 Pre-Flight Gate**: This workflow is for businesses that feel "stuck." If the business is growing on trajectory and the owner just wants optimization, route to `/10x-diagnostic` instead.

## The Process

### Step 1 — Map the Business Machine

Diagram the value chain from customer acquisition to delivery:

| Stage | Current State | Metric | Bottleneck? |
|-------|--------------|--------|-------------|
| **Awareness** | How do prospects find you? | [reach/impressions] | |
| **Lead Generation** | How do leads enter the funnel? | [leads/week] | |
| **Qualification** | How are leads filtered? | [qualified %] | |
| **Sales/Conversion** | How do leads become customers? | [close rate] | |
| **Delivery** | How is the product/service delivered? | [capacity %] | |
| **Retention** | How are customers kept? | [churn rate] | |
| **Expansion** | How is revenue expanded per customer? | [LTV trend] | |

### Step 2 — The Constraint Interview

Run through these diagnostic questions to find where the REAL constraint lives:

**Revenue Constraint?**
- Where does money enter the business? What blocks more from entering?
- If I gave you 100 more leads tomorrow, could you handle them? (If no → capacity constraint, not lead constraint)
- What is your close rate? What was it 6 months ago? (Declining = sales process constraint)

**Time Constraint?**
- What does the CEO spend 80% of their time on?
- Is that the highest-leverage activity? Or are they trapped in fulfillment?
- What would they do with 20 extra hours per week?

**People Constraint?**
- What role, if filled tomorrow, would unlock the most growth?
- Who on the team is underperforming? What has been done about it?
- Are turning points in this business's history marked by hiring/firing decisions?

**Systems Constraint?**
- What process is running on tribal knowledge instead of documentation?
- What breaks when a key person takes a week off?
- Where is the business "hoping" instead of measuring?

**Strategy Constraint?**
- Is the business trying to do too many things? (Violation of Singularity of Focus)
- Can the owner explain the business model on a napkin?
- What is the ONE metric that matters most right now?

### Step 3 — The 60-Minute Constraint Meeting Technique

Sharran's method: spend the entire meeting ONLY agreeing on the constraint, not solving it.

Format:
1. Each stakeholder proposes what they believe the constraint is (1 sentence each)
2. Group clusters the proposals into themes
3. Debate: Is each proposed constraint a ROOT CAUSE or a SYMPTOM?
4. Apply the "If we solved this, would the business actually move?" test to each
5. Vote on the ONE true constraint
6. Write it in one sentence. If it takes more than one sentence, you haven't isolated it.

### Step 4 — Triple-S Diagnosis

Determine which layer the constraint lives in:

| Layer | Question | If Yes → |
|-------|----------|----------|
| **Strategy** | Do we know what to work on but don't know WHY it matters or HOW it fits? | Strategy failure — need clarity on positioning, offer, or market |
| **Systems** | Do we know what to do but it keeps breaking or can't scale? | Systems failure — need process documentation, automation, or tooling |
| **Skills** | Do we have the strategy and systems but the team can't execute? | Skills failure — need training, hiring, or firing |

### Step 5 — Energy Allocation Plan

Now that the constraint is isolated, apply the energy allocation:

**Constraint Statement:**
> "[One sentence naming the specific bottleneck]"

**Triple-S Layer:** [Strategy / Systems / Skills]

**Energy Allocation:**
| Priority | Action | Energy Level | Timeline |
|----------|--------|-------------|----------|
| 1 (The Constraint) | [Specific action to solve it] | 80% of available energy | [Timeline] |
| 2 (Maintenance) | [Keep other areas from regressing] | 15% | Ongoing |
| 3 (Preparation) | [Prepare for the NEXT constraint] | 5% | Background |

**What NOT to Do:**
- [List 2-3 tempting actions that would scatter energy away from the real constraint]

## Output Format

### Constraint Isolation Audit: [Business Name]

**Business**: [description] | **Revenue**: [current] | **Team**: [size] | **Stage**: [startup/growth/scale]

**PERCEIVED PROBLEM** (what the owner thinks)
> [Owner's stated problem]

**BUSINESS MACHINE MAP**
[Value chain table with bottleneck identification]

**THE REAL CONSTRAINT** (one sentence)
> [Isolated constraint — specific, measurable, zero buzzwords]

**Triple-S Layer**: [Strategy / Systems / Skills]

**ENERGY ALLOCATION PLAN**
[Priority table with actions and timelines]

**THINGS TO STOP DOING**
[Energy leaks and distractions to eliminate]

**EXPECTED NEXT CONSTRAINT**: After this is solved, the constraint will likely move to [prediction of next bottleneck].

---

## Quality Gate
- [ ] Business machine map covers all 7 stages with actual metrics (not guesses)
- [ ] Constraint interview completed — at least 3 of 5 categories explored
- [ ] Constraint stated in one sentence with specific numbers where possible
- [ ] Triple-S diagnosis identifies which layer the constraint lives in
- [ ] Energy allocation follows 80/15/5 distribution
- [ ] "What NOT to Do" section names specific tempting distractions
- [ ] Next constraint predicted (because it WILL move)

> **🛡️ Anti-Pattern Check**: If the constraint can't pass the "If we solved this, would the business actually move?" test, it's a symptom, not the constraint. Go deeper.
