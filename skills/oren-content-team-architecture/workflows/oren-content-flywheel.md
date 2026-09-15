# Content Marketing Flywheel Engine

> **Expert**: Oren — Content-Team Architecture
> **Produces**: Flywheel Map + Gap Analysis + Priority Fix Plan
> **Use When**: Mapping the complete content-to-revenue circuit and identifying where it breaks
> **Load First**: [genius.md](../genius.md) — Patterns 2 (Marketing World Flywheel), 8 (External Creator Integration), 12 (Agency Integration)

---

## Step 1: Intake

Collect:
1. **Brand/org** — what they sell, primary revenue channels
2. **Current marketing channels** — what's active today?
3. **Team structure** — who works on what?
4. **Agency partners** — any external agencies? What do they handle?
5. **Revenue attribution** — do they know where sales come from?

---

## Step 2: Map the Five Nodes

For each node of the flywheel, assess current state:

### Node 1: Owned Organics
- Which social accounts exist?
- Posting frequency per platform?
- Who creates the content?
- Content types (video, carousel, stories, static)?
- Engagement benchmarks (avg. views, saves, shares)?

### Node 2: Owned Paid
- Active ad accounts? (Meta, TikTok, Google, YouTube)
- Monthly ad spend?
- Who creates ad assets?
- Are organic posts being repurposed as ads?
- ROAS/CPA benchmarks?

### Node 3: Brand World (External Organic)
- Any external creators posting about the brand?
- Seeding program? Gifting? Affiliate?
- Founder personal brand content?
- Employee advocacy content?
- Creator content being pulled into ad account?

### Node 4: Conversion
- Landing page / PDP quality?
- Messaging alignment with content voice?
- Same characters/faces used across content AND conversion pages?
- Conversion rate benchmarks?
- Agentic commerce layer? (Swap or equivalent)

### Node 5: Communications
- Email list size + engagement rate?
- SMS program?
- Are email/SMS assets using the same content from organic/paid?
- Automation sequences?
- Content creator faces/stories in email?

---

## Step 3: Circuit Analysis

For each connection between nodes, score flow strength (1-5):

```
Owned Organic ←→ Owned Paid:      [score] — do organic assets feed ad account?
Owned Paid ←→ Brand World:        [score] — is external creator content sparked/boosted?
Brand World ←→ Conversion:        [score] — do creator endorsements drive to landing pages?
Conversion ←→ Communications:     [score] — does email use content-first assets?
Communications ←→ Owned Organic:  [score] — does email drive back to social engagement?
```

**The flywheel only works when ALL connections flow.** A broken link = a broken flywheel.

---

## Step 4: Gap Diagnosis

For each connection scoring below 3:
1. **What's broken** — specific description of the gap
2. **Why it matters** — revenue/efficiency impact
3. **The fix** — exact action to close the gap
4. **Owner** — who should execute the fix
5. **Timeline** — days to implement

---

## Step 5: Priority Fix Plan

Rank all gaps by:
- **Revenue impact** (high/medium/low)
- **Implementation speed** (fast/medium/slow)
- **Dependency** (blocks other fixes? or independent?)

Produce the top 3 fixes in priority order with full implementation detail.

---

## Step 6: Output Schema — Flywheel Map

Produce:
```
BRAND: [Name]
FLYWHEEL HEALTH SCORE: [X/25]

NODE SCORES:
├── Owned Organic:      [X/5]
├── Owned Paid:         [X/5]
├── Brand World:        [X/5]
├── Conversion:         [X/5]
└── Communications:     [X/5]

CONNECTION SCORES:
├── Organic → Paid:     [X/5]
├── Paid → Brand World: [X/5]
├── World → Conversion: [X/5]
├── Conversion → Comms: [X/5]
└── Comms → Organic:    [X/5]

[Visual flywheel diagram with broken links highlighted]

TOP 3 PRIORITY FIXES:
1. [Fix] — [Impact] — [Owner] — [Timeline]
2. [Fix] — [Impact] — [Owner] — [Timeline]
3. [Fix] — [Impact] — [Owner] — [Timeline]

BUDGET REALLOCATION:
→ Kill: [What to stop spending on]
→ Shift: [Where to redirect those dollars]
```

---

## Quality Gate

- [ ] All 5 nodes AND all 5 connections are scored 1-5 — no node left blank
- [ ] Every connection scoring below 3 carries a Step 4 gap diagnosis (what's broken, why it matters, the fix, owner, timeline)
- [ ] Top 3 fixes are ranked by revenue impact and implementation speed, not listed in discovery order
- [ ] Budget reallocation names both a "kill" AND a "shift" — never one without the other
- [ ] Flywheel health score is a real X/25, not a placeholder

---

## Stacking

| After This Workflow | Stack With | For |
|:-------------------|:-----------|:----|
| Weak paid node | `/full-stack-ad` | Luke Iha ad creative pipeline |
| Weak brand world | `/oren-creator-network` | Build external creator network |
| Weak conversion | `/oren-funnel-flywheel` | Map the full conversion journey and isolate the broken handoff; route full copy afterward |
| Weak communications | `/email-narrative` | Email sequence architecture |
| Agency doesn't get flywheel | `/oren-content-team-audit` | Full team diagnostic including agencies |
