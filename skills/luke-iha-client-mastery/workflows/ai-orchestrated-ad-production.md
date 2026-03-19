---
name: "AI-Orchestrated Ad Production"
description: "AI production pipeline + human judgment layer + signal vs slop filtering. The creative strategist as orchestrator."
expert: "Luke Iha"
skill: "luke-iha-client-mastery"
---

# AI-Orchestrated Ad Production

## Purpose
Set up a complete AI ad production pipeline with the creative strategist functioning as orchestrator and judge — not writer. The system generates at scale, the human curates at precision.

## When to Use
- When setting up a creative production system for a DTC client
- When you need to produce 20+ ad variations efficiently
- When training yourself or a team on the "orchestrator, not writer" paradigm
- When deploying `/creative-diversity` and need the production engine behind it

---

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Step 1: The Orchestrator Mindset

### Completion Target
User has fully internalized the production/judgment separation.

### The Paradigm
**Old model**: Creative strategist writes ads → tests → iterates
**New model**: Creative strategist directs AI → AI writes → strategist judges → selects → tests

"There's such an overabundance of content and creative that we need people to sit at the hub, organize it, and make decisions about what to test and what not to test."

### What the Orchestrator Does
1. **Sets the brief** — strategic inputs (audience, awareness, mechanism, proof)
2. **Directs AI** — prompts, constraints, examples, tone guides
3. **Judges output** — applies the Feeling Test, copy block analysis
4. **Makes test decisions** — what gets budget, what gets killed
5. **Reads data** — performance analysis feeds next brief

### What the Orchestrator Does NOT Do
- Write ads from scratch (unless for taste calibration)
- Edit AI output word-by-word (judge holistically instead)
- Get attached to any single ad (volume > perfection)

---

## Step 2: Production Pipeline Setup

### Completion Target
A repeatable pipeline from brief to upload-ready ads.

### Phase 1 — Brief (15 min)
Create a structured AI brief:
```
PRODUCT: [What it is, what it does, price point]
AUDIENCE: [Who feels the pain most acutely]
AWARENESS LEVEL: [Unaware / Problem / Solution / Product / Most Aware]
MECHANISM: [The named system/method that makes it work]
PROOF POINTS: [3-5 specific proof items — stats, testimonials, results]
COMPOSITION: [Static / Video / Carousel / Advertorial]
VIBE: [Educational / Emotional / Urgent / Contrarian / Humorous / Raw]
REFERENCE AD: [Link to an ad you like the structure of]
```

### Phase 2 — Generation (30 min)
1. Input the brief into your AI tool (Claude, ChatGPT, Gemini)
2. Generate 15-25 variations in a single batch
3. Request variations across different hooks, different body structures, different CTAs
4. Explicitly ask for "5 completely different angles" to prevent AI homogeneity
5. For video scripts: generate hook + first 10 seconds, full 30s, and full 60s versions

### Phase 3 — The Judgment Sweep (15 min)
Apply the `/paid-to-feel` process:
1. **Feeling Sweep**: Read each variation without editing. Rate bodily response 1-10.
2. **Sort**: SIGNAL (7+), MAYBE (4-6), SLOP (1-3)
3. **Delete SLOP** immediately
4. **Analyze SIGNAL**: Copy block audit — does it have Pain, Promise, Proof, Constraints?
5. **Promote MAYBEs**: Can targeted edits (add proof, sharpen hook) elevate 1-2 pieces?

### Phase 4 — Finalization (15 min)
1. Final 5-7 pieces selected
2. Format for platform (headline, body, CTA, image specs)
3. Assign awareness-level tags
4. Rank by conviction (highest feeling + strongest analysis = most budget)
5. Set kill criteria before upload

---

## Step 3: Quality Calibration System

### Completion Target
System for continuously improving AI output quality and your judgment accuracy.

### Prompt Evolution
After each production cycle, note what worked and didn't:
- "AI defaults to generic hooks — add constraint: 'First 3 words must be surprising or specific'"
- "AI buries the mechanism — add constraint: 'Name the mechanism in the first sentence'"
- "AI doesn't layer proof — add constraint: 'Include 2 specific proof points in the body'"

Save these constraints as a growing **Prompt Library** for each client/product.

### Judgment Accuracy Tracking
After 2-4 weeks of running ads:
1. Compare your SIGNAL picks vs actual performance
2. Calculate: What % of your top-rated ads were actually top performers?
3. Track accuracy over time (target: 50%+ in month 1, 65%+ by month 3)
4. Identify your blind spots — are you consistently wrong about certain vibes or compositions?

---

## Step 4: Client Delivery System

### Completion Target
Weekly deliverable structure for client engagements.

### Weekly Deliverable
| Day | Action | Output |
|-----|--------|--------|
| Monday | Brief creation from last week's data | 1-2 production briefs |
| Tues-Wed | AI generation + Judgment Sweep | 15-25 variations → 5-7 finalists |
| Thursday | Finalization + upload | Ready-to-test ads |
| Friday | Performance review of running ads | Kill/scale decisions + next week brief |

### Client Communication
```
Weekly Report:
- New ads uploaded: [X]
- Top performer this week: [Ad name] — [CPA, ROAS]
- Ads killed: [X] (below CPA threshold)
- Total active ads: [X]
- Next week focus: [Awareness level / composition / vibe shift]
```

---

## Step 5: Scaling to Multiple Clients

### Process
Once the pipeline is established for one client, scale by:
1. **Templatize the brief**: Each new client gets a brief template pre-filled with their product/audience
2. **Batch production**: Run multiple client briefs through AI in the same session
3. **Judgment separation**: Judge each client's output separately (don't mix)
4. **Hire a production assistant**: Train someone on Phase 2 (generation) while you focus on Phase 1 (brief) and Phase 3 (judgment)

### Capacity Planning
| Clients | Weekly Production Time | Revenue Potential |
|---------|----------------------|-------------------|
| 1-2 | 4-6 hours/week | $3-10K/month |
| 3-4 | 8-12 hours/week | $10-20K/month |
| 5+ | Need production assistant | $20K+/month |

---

## Quality Gate

- [ ] Orchestrator mindset articulated (what you do vs don't do)
- [ ] Production pipeline set up with all 4 phases
- [ ] First production cycle completed (brief → generate → judge → finalize)
- [ ] Prompt Library started with at least 5 constraints
- [ ] Client delivery template drafted


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
