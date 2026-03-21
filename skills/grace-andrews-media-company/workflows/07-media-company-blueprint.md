---
description: "Build a complete creator-to-media-company transition blueprint grounded in deep research"
---

# Media Company Blueprint

> **Produces**: Full media company architecture with market research, revenue model, content infrastructure, and phased build plan  
> **Used When**: A creator or brand is ready to transition from individual content creation to media company operations  
> **Time**: 2-3 hours (includes research phase)  
> **Genius Patterns**: Media Company Default, Niche Precision Despite Breadth, Bar-Raising Reflex  
> **Cross-Stack**: Dan Koe (one-person business), Samuel Thompson (market validation), Perplexity Deep Research  
> **Research**: Requires deep research — this workflow fires Perplexity `sonar-deep-research` queries and parallel agents

---

## Pre-Flight Check

- [ ] Loaded `genius.md` for quality ceiling calibration
- [ ] User's current business model is understood (what they sell, how they sell, who they serve)
- [ ] User's current content footprint is known (platforms, volume, performance)
- [ ] Budget gate: check `.agent/perplexity-usage.json` — this workflow uses ~$0.75-1.50 for deep research

---

## Step 1: Deep Research Foundation

Before designing the architecture, ground the blueprint in reality. Fire 2-3 Perplexity `sonar-deep-research` queries:

### Query 1 — Comparable Creator Analysis (MANDATORY)
```
"Analyze 5-10 creators/media companies in [user's niche] who successfully transitioned from individual creator to media company. 
For each: revenue model, team size, content formats, pivot point (when they shifted), growth trajectory.
Include specific revenue figures where available. Focus on creators with $500K-$10M revenue."
```

### Query 2 — Format & Revenue Benchmarks (MANDATORY)
```
"What content formats are growing fastest in [user's niche] in 2025-2026?
What are the typical revenue per format unit (CPM, sponsor rate, course conversion, etc.)?
What's the industry benchmark for audience-to-revenue conversion in this space?
Include emerging formats and platforms."
```

### Query 3 — Audience Intelligence (if budget allows)
```
"What do audiences in [user's niche] actually want from media companies vs individual creators?
What are they willing to pay for? What are the top complaints about existing content?
Use Reddit, YouTube comments, and forum data."
```

**Save raw results to**: `.tmp/grace-blueprint/research-[query].md`

**Compress into**: Key benchmarks, comparable case studies, format trends, revenue data points.

---

## Step 2: Current State Audit

Map the user's existing "city" before redesigning it:

| Dimension | Current State | Gap |
|-----------|--------------|-----|
| **Grand Central Station** | [Current mission — articulated or implicit?] | [Is it clear enough to guide all content?] |
| **Content Lines** | [List all active formats + frequency] | [Which trust stages are missing?] |
| **Trust Pathway** | [Where does trust currently break?] | [Stage where audience drops off] |
| **Revenue Model** | [How money is currently made] | [Single revenue stream? Fragile?] |
| **Team** | [Solo? VA? Editor?] | [What can't scale without people?] |
| **Brand Equity** | [What would a sponsor/partner pay for?] | [Is brand > person or person > brand?] |

**Critical question**: "Is the current business a personal brand that would die without the founder's face, or could it operate as a media property with the founder as one voice among several?"

---

## Step 3: Media Company Architecture Design

Design the target-state using Grace's City Map as the structural metaphor:

### 3a. Grand Central Redesign
Evolve the mission from personal brand to media company:
- **Personal brand mission**: "I help X do Y" → centers on the creator
- **Media company mission**: "[Company Name] exists to [mission]" → centers on the audience

### 3b. Content Infrastructure (The Lines)

Design 3-5 content lines as media products, not personal projects:

| Content Line | Format | Frequency | Audience Served | Trust Stage | Revenue Path | Team Needs |
|-------------|--------|-----------|----------------|-------------|--------------|------------|
| [Line 1 — Flagship] | [e.g., long-form video] | [Weekly] | [Core audience] | [Trust → Conversion] | [Sponsors + product CTAs] | [Editor, thumbnail, scripting] |
| [Line 2 — Discovery] | [e.g., short-form clips] | [Daily] | [New audience] | [Attention → Discoverability] | [Platform monetization] | [Clip editor] |
| [Line 3 — Depth] | [e.g., newsletter] | [2x/week] | [Engaged segment] | [Connection → Trust] | [Premium tier, sponsorship] | [Writer/editor] |
| [Line 4 — Community] | [e.g., Skool/Discord] | [Always-on] | [Most invested] | [Trust → Conversion] | [Membership fee] | [Community manager] |

### 3c. Revenue Architecture

Apply the research benchmarks from Step 1 to design a multi-stream revenue model:

| Revenue Stream | Trust Stage Required | Expected Revenue Range | Timeline to Activate |
|---------------|---------------------|----------------------|---------------------|
| **Sponsorships** | Attention + Discoverability | [from research benchmarks] | Immediate if audience exists |
| **Digital Products** | Trust | [from research benchmarks] | 60-90 days |
| **Membership/Community** | Connection + Trust | [from research benchmarks] | 90-120 days |
| **Services/Consulting** | Deep Trust | [from research benchmarks] | Existing — systemize |
| **Events/Experiences** | Advocacy | [from research benchmarks] | 6-12 months |

**Quality gate**: Revenue model must:
- ✅ Have 3+ revenue streams
- ✅ Not be >60% dependent on any single stream
- ✅ Include at least one stream that works while the founder sleeps
- ❌ NOT depend entirely on the founder's real-time presence

---

## Step 4: Phased Build Plan

Design a 12-month transition from current state to media company:

### Phase 1: Foundation (Months 1-3)
- [ ] Articulate media company mission (Grand Central Redesign)
- [ ] Hire/systematize first key role (editor, writer, or community manager)
- [ ] Launch or refine flagship content line with consistent schedule
- [ ] Build first trust pathway bridge content
- [ ] Set up measurement for each trust stage

### Phase 2: Expansion (Months 4-6)
- [ ] Launch second content line (different trust stage)
- [ ] Activate first non-obvious revenue stream
- [ ] Begin cross-platform distribution (content orbit)
- [ ] First guest/collaboration from outreach layer (Workflow 05)
- [ ] Run first Content Portfolio Audit (Workflow 04)

### Phase 3: Scale (Months 7-9)
- [ ] Launch third content line or convert existing line to team-operated
- [ ] Diversify revenue — target 3+ active streams
- [ ] Brand identity begins operating independently of founder
- [ ] First "the team did this without me" milestone
- [ ] Introduce experimental content lane (30% of Consistency × Experimentation)

### Phase 4: Media Company (Months 10-12)
- [ ] All content lines running with team support
- [ ] Revenue model has 3+ streams, none >50% of total
- [ ] Founder can take 2+ weeks off without content stopping
- [ ] Brand equity audit: would someone pay to acquire this media company?

---

## Step 5: Validation Through Research Triangulation

Cross-reference the blueprint against Deep Research findings:

| Blueprint Element | Research Validation | Confidence |
|-------------------|-------------------|------------|
| Revenue targets | [Does comparable data support these numbers?] | [H/M/L] |
| Format choices | [Are these formats growing or declining in the niche?] | [H/M/L] |
| Team timeline | [How did comparable creators staff up?] | [H/M/L] |
| Revenue diversification | [What streams worked for comparable media companies?] | [H/M/L] |

---

## Output Format

Deliver:
1. **Research Foundation Brief** — compressed findings from deep research (comparable creators, benchmarks, audience intelligence)
2. **Current State Audit** — honest assessment of where the creator is today
3. **Media Company Architecture** — target-state City Map with content lines, trust pathways, and revenue streams
4. **12-Month Build Plan** — phased milestones with specific deliverables per phase
5. **Revenue Model Blueprint** — multi-stream revenue architecture with timeline and expected ranges
6. **Risk Assessment** — what could derail the transition, informed by research failures/counter-narratives
