# Content Pod Architecture Builder

> **Expert**: Oren — Content-Team Architecture
> **Produces**: Pod Structure Blueprint + Hiring Spec + Role Definitions
> **Use When**: Designing the content team structure for any org size
> **Load First**: [genius.md](../genius.md) — Patterns 1 (Pod Architecture), 5 (Cadence), 6 (10-Asset Standard), 13 (Multi-Pod Scaling)

---

## Step 1: Org Assessment

Collect:
1. **Current headcount** dedicated to content (0 = starting from scratch)
2. **Budget range** for content team (monthly)
3. **Tier from diagnostic** (iPhone / Mid / Enterprise) — or determine from context
4. **Primary platforms** — which channels are priority?
5. **Founder involvement** — is the founder willing to be on camera?

---

## Step 2: Pod Design

Based on tier, design the pod architecture:

### iPhone-Tier (0-1 current content people)

```
POD 1: The Starter Pod
├── Strategist (hire or train existing person)
│   Responsibilities: briefs, shot lists, analytics, posting,
│   scheduling, ideation, cross-org communication
│
└── Creator (hire)
    Responsibilities: shooting (iPhone), editing (CapCut/mobile),
    being on camera, ideation collaboration
    
OUTPUT TARGET: 10 concepts/week (5 organic, 5 ad)
GEAR: iPhone + Osmo + Amaran 300 lights
```

### Mid-Tier (2-5 people)

```
POD 1: Core Brand
├── Strategist
├── Internal Creator
└── External Contributors (3-5)
    Sourced via: miniocial, Super Affiliate, Outer Signal

POD 2: Founder Content (if founder is on camera)
├── Strategist (can be Pod 1 strategist initially)
└── Videographer/Editor
    
OUTPUT TARGET: 10+ concepts/week per pod
SHARED: Editor (if separate from creator), Designer (Contra)
```

### Enterprise-Tier (5+ people, scaling)

```
LEADERSHIP LAYER
├── Creative Director — vision, standards, coaching strategists
├── E-com Repurposing Lead — pulling pod content into conversion
└── Channel Comms Lead — partner/channel coordination

POD 1: Core Brand Social
├── Strategist
├── Internal Creator
└── 3-5 External Contributors

POD 2: Founder Content
├── Strategist
├── Videographer/Editor
└── 2-3 Collaborators

POD 3: Platform-Specific (TikTok/YouTube)
├── Strategist
├── Creator (platform-native)
└── External Contributors

SHARED RESOURCES
├── Editors (cross-pod)
├── Designers (Contra/in-house)
└── Producer (locations, props, talent)

OUTPUT TARGET: 10+ concepts/week per pod
```

---

## Step 3: Role Specifications

For each role in the designed structure, produce:

1. **Title** — aligned with industry standards
2. **Core responsibilities** — 5-7 bullet points
3. **Must-have skills** — non-negotiable competencies
4. **Nice-to-have** — differentiating capabilities
5. **Compensation range** — based on tier and market
6. **Reporting line** — who they report to
7. **Success metric** — how you know they're working

### The Head of Growth / Head of Social Spec

This is always the hardest hire. Produce a detailed spec:
- Senior/director level, NOT entry-level
- Translates the flywheel concept into daily action
- Operates relentlessly — this person is the engine
- Can coach creators AND read analytics
- Understands paid + organic integration

---

## Step 4: Hiring Sequence

Produce the hiring order. Rule: **Never hire the creator before the strategist.**

For each hire, specify:
- Order priority (1st, 2nd, 3rd...)
- Why this sequence (dependency logic)
- Where to source (job boards, creator communities, portfolios)
- Interview signal — what to look for in candidates

---

## Step 5: Output Schema — Pod Architecture Blueprint

Produce a single artifact:

```
ORG: [Name]
TIER: [iPhone / Mid / Enterprise]
TOTAL PODS: [N]
TOTAL HEADCOUNT: [N internal + N external]

[Visual pod diagram]

HIRING SEQUENCE:
1. [Role] — [Rationale] — [Source] — [Timeline]
2. [Role] — [Rationale] — [Source] — [Timeline]
...

WEEKLY OUTPUT TARGET: [N concepts × N pods]
GEAR BUDGET: [List]
PM TOOL: [Recommendation]
```

---

## Quality Gate

- [ ] Pod design matches the org's actual tier (iPhone/Mid/Enterprise) from Step 1 — never over-architect a 0-1 person team into a multi-pod structure
- [ ] Hiring sequence never places Creator before Strategist (Step 4's non-negotiable rule)
- [ ] Every role spec includes compensation range and reporting line — no role left undefined
- [ ] Output target is stated as concepts/week × number of pods, matching the 10-concept floor from Pattern 6
- [ ] Gear budget matches the tier's gear ceiling (iPhone + Osmo + Amaran 300s for iPhone-tier — never RED/Arri per Pattern 11)

---

## Stacking

| After This Workflow | Stack With | For |
|:-------------------|:-----------|:----|
| Pods designed | `/oren-pod-cadence` | Build the operating rhythm |
| Head of Growth spec | `/cs-launcher` | Creative strategist hiring pipeline |
| External contributors | `/oren-creator-network` | Source and manage creator network |
| Founder pod designed | `/oren-founder-content` | Architect the founder's content identity |
