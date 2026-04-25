# Multi-Pod Scaling Protocol

> **Expert**: Oren — Content-Team Architecture
> **Produces**: Scaling Readiness Assessment + Multi-Pod Architecture + Resource Sharing Blueprint
> **Use When**: Pod 1 is mature and the org is ready to scale to 2+ pods
> **Load First**: [genius.md](../genius.md) — Patterns 13 (Multi-Pod Scaling), 1 (Pod Architecture), 5 (Cadence), 12 (Agency Integration)

---

## Step 1: Scaling Readiness Gate

Before adding Pod 2, Pod 1 must pass ALL of these gates:

```
READINESS CHECKLIST:
├── [ ] Pod 1 consistently hits 10+ concepts/week for 8+ weeks
├── [ ] Quality standard maintained (80%+ Ship rate at Friday review)
├── [ ] Strategist is coaching, not drowning
├── [ ] Weekly cadence followed without reminders
├── [ ] Analytics review is a habit, not an event
├── [ ] External creator network has 3+ reliable contributors
├── [ ] Organic → paid pipeline is flowing
├── [ ] Monthly creative audit completed at least twice
└── [ ] Clear demand signal for more content (more platforms, more products, more campaigns)
```

**If any gate fails → fix it before scaling. Scaling a broken pod just creates two broken pods.**

---

## Step 2: Pod 2 Design Decision

### Option A: Platform Pod
A new pod dedicated to a specific platform.
- Example: Pod 1 owns Instagram + TikTok. Pod 2 owns YouTube.
- When: The brand needs long-form or platform-specific expertise
- Requires: Platform-native strategist and creator

### Option B: Audience Pod
A new pod dedicated to a different audience segment.
- Example: Pod 1 targets customers. Pod 2 targets industry/B2B.
- When: The brand sells to multiple distinct audiences
- Requires: Audience-specific strategist

### Option C: Product Pod
A new pod dedicated to a product line or category.
- Example: Pod 1 covers core brand. Pod 2 covers new product launch.
- When: Product lines are distinct enough to warrant different content
- Requires: Product-specific knowledge

### Option D: Founder Pod
A dedicated pod for the founder's personal content.
- Example: Pod 1 is brand content. Pod 2 is the founder's show.
- When: Founder content has outgrown shared strategist time
- Requires: Run `/oren-founder-content` first

---

## Step 3: Resource Sharing Architecture

Not every resource needs to be duplicated. Design the shared layer:

```
SHARED RESOURCES (Cross-Pod):
├── Editors
│   └── Pool model: 2-3 editors serve both pods, assigned by priorities
├── Designers
│   └── Typically Contra/freelance, shared across pods
├── Producer (if enterprise)
│   └── Handles locations, props, talent, logistics for all pods
├── Analytics platform
│   └── Single dashboard with pod-specific views
├── PM tool
│   └── Single workspace with pod-specific boards/projects
└── Brand assets
    └── Shared asset library (logos, fonts, templates, approved music)

POD-SPECIFIC (NOT shared):
├── Strategist — each pod has their own
├── Creator — each pod has their own
├── Content calendar — each pod manages their own pipeline
├── External creators — assigned to specific pods (no overlap)
└── Performance metrics — tracked at pod level
```

### The Handoff Problem
When pods share resources, define explicit handoff protocols:
- **Editor capacity allocation**: Pod A gets X hours/week, Pod B gets Y hours/week
- **Priority conflicts**: How to resolve when both pods need the editor simultaneously
- **Quality standards**: Shared rubric so editors maintain consistency across pods
- **Communication channel**: Dedicated Slack channel for shared resource coordination

---

## Step 4: Cross-Pod Narrative Coherence

Multiple pods creating content about the same brand can fragment the story. Prevent this:

### Weekly Cross-Pod Sync (30 minutes)
**Who**: All pod strategists + Creative Director
**Agenda**:
1. Theme alignment — are we telling a coherent story this week?
2. Narrative conflicts — anything contradicting across pods?
3. Amplification opportunities — can Pod B amplify Pod A's best content?
4. Resource sharing — any capacity to share this week?

### Monthly Narrative Review
- Pull content from all pods and review as a single corpus
- Does it feel like ONE brand or multiple fragmented voices?
- Is there POV consistency even with different formats and platforms?
- Are pods building on each other's narratives or creating isolated islands?

---

## Step 5: Scaling Timeline

```
WEEK 1-2: Design Phase
├── Select Pod 2 type (Platform/Audience/Product/Founder)
├── Design pod structure using /oren-pod-architect
├── Define resource sharing architecture
├── Budget approval for new hires

WEEK 3-4: Hiring Phase
├── Post strategist role (always hire strategist first)
├── Begin creator search in parallel
├── Brief shared resources on new pod scope

WEEK 5-6: Onboarding Phase
├── Strategist onboarded + shadowing Pod 1 for 1 week
├── Creator onboarded + first test concepts
├── PM workspace configured for Pod 2
├── External creator onboarding begins

WEEK 7-8: Pilot Phase
├── Pod 2 producing first concepts (5/week target, building to 10)
├── Pod 1 strategist mentoring Pod 2 strategist
├── Weekly cross-pod sync begins
├── Shared resources tested under dual-pod load

WEEK 9-12: Normalization
├── Pod 2 hitting 10 concepts/week
├── Cross-pod narrative coherence confirmed
├── Resource sharing model stabilized
├── Monthly cross-pod creative audit established
```

---

## Step 6: Output — Scaling Blueprint

```
BRAND: [Name]
CURRENT STATE: [N pods, N total headcount]
TARGET STATE: [N pods, N total headcount]

POD 2 TYPE: [Platform / Audience / Product / Founder]
POD 2 RATIONALE: [Why this pod type]

POD 2 STRUCTURE:
├── Strategist: [Hire spec]
├── Creator: [Hire spec]
├── External contributors: [Target count]
└── Shared resources: [What's shared, what's new]

RESOURCE SHARING:
[Full sharing architecture from Step 3]

NARRATIVE COHERENCE:
├── Weekly sync: [Day/time]
├── Monthly review: [Date]
└── Creative Director oversight: [Yes/No/Hire?]

TIMELINE:
[12-week plan from Step 5]

BUDGET IMPACT:
├── New hires: $[N]/month
├── Shared resource scaling: $[N]/month
├── Tools/infrastructure: $[N]/month
└── Total incremental: $[N]/month

READINESS GATES:
[All gates from Step 1 with current status]
```

---

## Stacking

| After This Workflow | Stack With | For |
|:-------------------|:-----------|:----|
| Pod 3+ scaling | Re-run this workflow iteratively | |
| Creative Director hire needed | `/oren-pod-architect` | CD role spec |
| Cross-pod standards failing | `/taste-cev` | Re-calibrate editorial standards |
| Agency needs to evolve with scale | `/oren-content-team-audit` | Full audit including agency |
| Pods need distinct series | `/oren-signature-series` | Series per pod |
