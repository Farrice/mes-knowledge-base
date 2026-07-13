---
name: "Market Intelligence — Strategic IQ Brief"
source_prompt: born-v2
skill: market_intelligence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are producing the **Strategic Briefing layer** of Market Intelligence — SKILL.md names this
target directly: "A $5,000 SEO agency report," built via Entity Understanding, Agentic Keyword
Research, and fully sourced claims. This is Phase 3 ("Build the Strategy") — the synthesis
deliverable that assumes Trend Hunt Scan and Keyword Intent Audit findings (or equivalent fresh
research) are feeding in. It runs on the same governing protocols as the rest of this skill's
methodology (`references/genius-patterns.md`): Wallet-Out intent tiers, Entity Understanding,
Shadow Market opportunity scoring, the Retrieval Layer (AI-citation) audit, and the Data Grounding
Mandate. The brief's own template header identifies the output as prepared under this skill's
"Strategic Data Broker" framing, not any individual named guru — do not attribute it to a person
this skill's material doesn't name.

## 🛑 Grounding Gate — the Data Grounding Mandate

**"THE RULE: If you can't cite it, don't claim it."** Every claim in this brief must trace to a
source. Required data points and their acceptable sources:

| Data Point | Acceptable Sources |
|---|---|
| Search Volume | Ahrefs, SEMrush, Google Keyword Planner, Moz |
| CPC Estimates | Google Ads Keyword Planner, WordStream benchmarks |
| Market Size / Stats | Industry reports (CAR, NAR, Statista, IBISWorld, etc.) |
| Competition | Live SERP analysis — who are the actual top 3 results? |

Ground everything through:
```bash
python3 execution/research.py "<query>" --depth [standard|deep|max]
```
Use `deep`/`max` for this deliverable given its scope — it's the highest-stakes output this skill
produces. Anything you cannot source gets the explicit `ESTIMATE` tag inline; never omit the tag
to make the brief read cleaner. `keyword_auditor.py`'s SERP simulation is never a valid source.

## Input Required

```
[NICHE NAME] — the market/niche this brief covers
[PRIOR FINDINGS — optional] — Trend Hunt Scan and/or Keyword Intent Audit outputs already produced this session
[SCOPE] — full dossier | specific section refresh (e.g. "just the 30-day plan")
[DEPTH] — standard | deep | max (default: deep, given this is the synthesis deliverable)
```

## Execution Protocol

**Step 1 — Entity Understanding.**
Classify the niche (Product / Service / Demographic / Program per the standard table) before
generating any keyword. This determines the correct keyword strategy shape for Sections 2-3 below
— e.g. a Demographic niche gets "programs that serve them" keywords, never "buy [demographic]."

**Step 2 — Shadow Market synthesis (Executive Summary).**
Apply the Shadow Market equation — `Desperation × Money ÷ Competition Quality` — to produce the
market verdict and "unfair advantage" framing. This must read as a synthesized insight from actual
research (demand velocity signals, competition quality observed in live SERPs), not a restated
formula. If prior Trend Hunt Scan findings exist, this section should draw on them rather than
re-deriving from scratch.

**Step 3 — Money Keywords (Transactional intent table).**
Surface keywords carrying Transactional/Commercial-Investigation intent (Wallet-Out Protocol,
tiers 1-2). Each keyword needs difficulty and CPC — sourced per the Data Grounding table above, or
`ESTIMATE`. If Keyword Intent Audit output already exists for this niche, pull from it rather than
re-running the classification from zero.

**Step 4 — Traffic Engine (informational clusters).**
Identify the dominant informational pillar topic and its sub-topics (Informational tier, tier 3).
This is the top-of-funnel authority-building layer — organize as one pillar with a checklist of
sub-topic articles, each tagged with the keywords it targets.

**Step 5 — Topical Authority Map (Retrieval Layer Audit).**
Origin: Nathan Gotch (AI SEO) — in 2026 the metric that matters beyond ranking is **Citational
Authority**: does the keyword/topic trigger an AI Overview, and if so, is the content structured
(tables, lists, clear definitions) to be picked up as training/retrieval data? Map the niche's core
entity and its 2-4 semantic pillars, and flag which topics should be structured for AI-overview
retrieval specifically.

**Step 6 — 30-Day Content Attack Plan.**
Sequence into three weeks, matching the template's own escalation logic:
- Week 1 (Foundation/Money): launch the highest-priority Money Keyword page(s) from Step 3.
- Week 2 (Authority/Trust): answer the top questions/objections surfaced by the Traffic Engine
  cluster (Step 4), typically a comparison/"vs" piece.
- Week 3 (Velocity/Traffic): target a trending angle — pull from Trend Hunt Scan findings if
  available, otherwise flag that a fresh trend scan should precede this week's task.

## Output Contract

- Full dossier covering all five content sections (Executive Summary, Money Keywords, Traffic
  Engine, Topical Authority Map, 30-Day Attack Plan) unless `[SCOPE]` requests a single-section
  refresh.
- Every data point sourced or `ESTIMATE`-tagged — no exceptions, including CPC/difficulty figures
  and market-size stats in the executive summary.
- Money Keywords presented as a table (keyword / difficulty / CPC / intent tier).
- Topical Authority Map rendered as a mermaid `graph TD` (or equivalent explicit hierarchy if
  mermaid isn't renderable in the delivery context) showing core entity → pillars → sub-topics.
- 30-Day plan names concrete deliverables per week, each traceable back to a specific
  keyword/cluster/trend from earlier sections — not generic tasks.

## Output Skeleton

```
# Strategic IQ Brief: [Niche Name]
Date: [date] | Prepared By: Antigravity Intelligence
Market Verdict: [one-line verdict]

## 1. Executive Summary (The Shadow Market Opportunity)
Insight: [shadow market synthesis — sourced]
- Demand Velocity: [reasoning + source/ESTIMATE]
- Competition Quality: [reasoning + source/ESTIMATE]
- The Unfair Advantage: [what this brief's holder can exploit that incumbents aren't]

## 2. The Money Keywords (Transactional Intent)
| Keyword | Difficulty | CPC (source/ESTIMATE) | Intent Tier |
|---|---|---|---|
[rows]
Action: [landing page priority order]

## 3. The Traffic Engine (Informational Clusters)
Pillar: [dominant informational topic]
- [ ] [sub-topic 1] (Keywords: [...])
- [ ] [sub-topic 2] (Keywords: [...])
[...]

## 4. Topical Authority Map
[mermaid graph TD: core entity -> pillars -> sub-topics]
AI-Overview flags: [which topics need retrieval-optimized structuring, and why]

## 5. 30-Day Content Attack Plan
Week 1 (Foundation/Money): [task, tied to Section 2]
Week 2 (Authority/Trust): [task, tied to Section 3]
Week 3 (Velocity/Traffic): [task, tied to trend scan or flagged as needing one]

---
Generated by Antigravity Market Intelligence
```

## Quality Gate

- [ ] Entity Understanding ran before keyword generation; niche correctly typed (no demographic-as-product errors anywhere in the brief)
- [ ] Every number (volume, CPC, market size, difficulty) is sourced with a URL or explicitly labeled ESTIMATE
- [ ] Shadow Market verdict is a synthesis of actual evidence, not a restated formula with no backing
- [ ] Topical Authority Map covers the core entity plus at least 2 real semantic pillars, not filler sub-topics
- [ ] Each week of the 30-Day plan ties to a specific keyword/cluster/trend named earlier in the brief
- [ ] No section presents `keyword_auditor.py` mock output or unvalidated reasoning as "live data"

## Creative Latitude

Sections 1 and 5 are where this brief earns the "$5,000 agency report" framing or falls short of
it — push there. The Executive Summary's "unfair advantage" line should name the *specific*
structural weakness in the competition (not a vague "low competition" claim) and the specific
angle that exploits it; write it like a strategist making a case, not a form field being filled.
The 30-Day plan's task descriptions should read as decisions with reasoning attached, not a
checklist — explain why Week 1 leads with that particular keyword and not another. Section 4's
pillar selection is a taste call: choose the semantic groupings that best set up AI-citation
retrieval for this specific niche, not a generic 3-pillar template.

## Deploy When

- Operator needs the full go-to-market content strategy for a niche, sourced and ready to hand to
  a writer or content team (`/generate-brief "[Niche]"`).
- As the capstone of the Hunt → Audit → Brief pipeline, once Trend Hunt Scan and/or Keyword Intent
  Audit findings exist for the niche.
- When a stakeholder needs the "why we're betting on this niche" case made with sourced evidence,
  not just a keyword list.
