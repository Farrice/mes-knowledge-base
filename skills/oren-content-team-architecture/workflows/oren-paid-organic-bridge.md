# Paid-Organic Bridge Architecture

> **Expert**: Oren — Content-Team Architecture
> **Produces**: Paid-Organic Integration Protocol + Asset Pipeline + Testing Framework
> **Use When**: Connecting organic content production to paid media performance
> **Load First**: [genius.md](../genius.md) — Patterns 9 (Paid Creative Ops), 2 (Flywheel), 6 (10-Asset Standard)

---

## Step 1: Current State Assessment

Collect:
1. **Monthly ad spend** — total across platforms
2. **Creative volume** — how many new ad concepts per month?
3. **Organic volume** — how many organic posts per month?
4. **Current crossover** — does organic content ever become ads? (and vice versa)
5. **Performance mediator** — who manages paid? Internal, agency, or hybrid?
6. **Attribution model** — how do you credit content to revenue?

---

## Step 2: The Bridge Framework

Organic and paid are NOT separate channels. They are the same flywheel. The bridge operates in both directions:

### Organic → Paid Pipeline

```
STAGE 1: Production
Pod produces 10 concepts/week
→ 5 organic-native
→ 3 paid-ready (shot with ad specs in mind)
→ 2 flex (can go either direction)

STAGE 2: Organic Testing
All concepts published organically first (unless time-sensitive campaign)
→ Track: Views, saves, shares, comments, completion rate
→ 7-day organic performance window

STAGE 3: Paid Graduation
Top performers "graduate" into the ad account
→ Criteria: Top 20% by engagement OR high save rate OR strong comment sentiment
→ Creative brief includes: original organic metrics, suggested targeting, CTA addition

STAGE 4: Paid Optimization
Ad team runs graduated content through standard testing protocol
→ A/B test hooks, CTAs, thumbnails
→ Scale winners, kill losers at pre-set CPA thresholds
```

### Paid → Organic Pipeline

```
STAGE 1: Ad Winners
Top-performing ads (based on ROAS/CPA/CTR)
→ Identify what made them work structurally (hook, story, format)

STAGE 2: Organic Adaptation
Reverse-engineer winning ad structures into organic content
→ Strip the CTA
→ Add platform-native elements (trending audio, platform-specific edits)
→ Publish as organic with the proven structure

STAGE 3: Pattern Library
Document winning structures in the pod's playbook
→ "This hook pattern converts at 3x baseline"
→ Create brief templates based on winning patterns
```

---

## Step 3: Creative Format Spec

For content that needs to work across both organic and paid:

```
FORMAT REQUIREMENTS:
├── Aspect ratio: 9:16 primary, 1:1 secondary crop
├── Safe zones: Keep key visuals/text within platform safe zones
├── Hook window: First 3 seconds must work WITHOUT audio
├── Branding: Logo in last 3 seconds, not first 3
├── Duration tiers: 15s / 30s / 60s versions
├── CTA: Removable layer (add for paid, strip for organic)
└── Captions: Burned in always
```

---

## Step 4: The Testing Protocol

### Volume Rule
At the spend levels Oren describes ($10K-$100K/month), you need high creative volume:

```
MONTHLY CREATIVE TARGETS BY SPEND:
├── $10K-$25K/month:   20-30 new concepts
├── $25K-$50K/month:   30-50 new concepts
├── $50K-$100K/month:  50-80 new concepts
└── $100K+/month:      80+ (multi-pod required)
```

### Testing Framework

```
TEST HIERARCHY:
1. Hook test (first 3 seconds) — highest impact variable
2. Format test (format A vs format B) — second highest
3. CTA test — medium impact
4. Audience test — test creator's content against different audiences
5. Platform test — same concept across Meta, TikTok, YouTube Shorts
```

### Kill Criteria

```
KILL AT:
├── CPM > 2x benchmark after 24 hours
├── Hook rate < 30% (video)
├── CTR < 0.8% (image)
├── CPA > 1.5x target after $100 spend
└── ROAS < breakeven after $200 spend
```

---

## Step 5: Agency-Pod Integration

If paid media is managed by an agency:

### What the Agency Needs from the Pod
- Weekly creative drops (pre-formatted, tagged with source data)
- Organic performance data on graduated concepts
- Creative notes: what the strategist believes made each piece work
- Quick-turn iterations on winning concepts (variations within 48 hours)

### What the Pod Needs from the Agency
- Weekly performance report with creative-level data
- Top/bottom creative performers with analysis
- Audience insights that inform organic content direction
- Budget allocation transparency

### Red Flag: Agency Can't Articulate Which Creatives Work
If the agency reports on campaign-level metrics but can't tell you which specific creative drove performance — that's a broken bridge.

---

## Step 6: Output — Bridge Protocol Document

```
BRAND: [Name]
MONTHLY SPEND: [Amount]
CREATIVE VOLUME TARGET: [N concepts/month]

ORGANIC → PAID PIPELINE:
├── Graduation criteria: [Specific metrics]
├── Graduation cadence: [Weekly/biweekly]
├── Handoff process: [Who passes what to whom, in what format]
└── Feedback loop: [How paid data returns to organic strategy]

PAID → ORGANIC PIPELINE:
├── Winner analysis cadence: [Weekly/monthly]
├── Pattern documentation: [Where stored, who updates]
└── Brief template evolution: [How winning patterns become standard briefs]

TESTING PROTOCOL:
├── Test hierarchy: [Hook → Format → CTA → Audience]
├── Kill criteria: [Specific thresholds]
└── Reporting: [Who reviews, when, what decisions result]

AGENCY INTEGRATION:
├── Weekly sync: [Day/time]
├── Creative handoff: [Format/tool]
└── Performance feedback: [Format/cadence]
```

---

## Stacking

| After This Workflow | Stack With | For |
|:-------------------|:-----------|:----|
| Need more ad creative volume | `/creative-diversity` | Meta Andromeda creative diversity |
| Need better hooks | `/hook-forge` | Hook generation engine |
| Need full ad pipeline | `/full-stack-ad` | Luke Iha complete ad system |
| Agency evaluation | `/oren-content-team-audit` | Full team + agency audit |
| Need more organic → paid wins | `/oren-pod-cadence` | Tighten the weekly review cycle |
