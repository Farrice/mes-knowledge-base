---
description: "Full media diagnostic — Content Portfolio Audit + deep research on audience behavior + parallel swarm expert review"
---

# /grace-media-diagnostic — Full Media Company Diagnostic

The "where am I losing people?" diagnostic. Combines Grace's Content Portfolio Audit (Workflow 04) with live audience behavior research via Perplexity and a multi-expert review via parallel swarm. Produces a scored diagnostic report with prioritized fixes.

**When to use**: Content isn't driving business outcomes, growth has stalled, post-viral confusion, or the brand feels strategically lost. This is the MRI before the surgery.

## Usage

```
/grace-media-diagnostic [brand/creator name]
/grace-media-diagnostic "My Brand" --focus "trust-to-conversion" --platforms "youtube,newsletter,linkedin"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`
3. `skills/grace-andrews-media-company/workflows/04-content-portfolio-audit.md`

### 2. Execute Content Portfolio Audit
Run the full Workflow 04 — produces:
- Forgettable/memorable split
- Trust pathway coverage gaps
- Business outcome linkage assessment
- Consistency × Experimentation balance

### 3. Deep Research — Audience Behavior

Check `.agent/perplexity-usage.json` for budget. If budget allows ($0.50-0.75 estimated):

**Query 1** (sonar-deep-research): "What content performance patterns indicate trust-building vs attention-only in [niche]? What metrics separate creators who convert audiences to buyers from those who just accumulate followers? Include case studies."

**Query 2** (sonar-deep-research): "What are audiences in [niche] actually saying about content fatigue, creator trust, and purchasing decisions? Use Reddit, YouTube comments, Twitter/X. Include verbatim quotes."

Save to `.tmp/grace-diagnostic/research-*.md`

If budget insufficient: Fall back to `search_web` + `read_url_content` for 3-5 queries covering the same ground.

### 4. Deploy Expert Review Swarm

// turbo
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py --grounded \
  --agents "dan-koe,seth-godin,lara-acosta" \
  "[INJECT: Content Portfolio Audit results from Step 2]
  [INJECT: Research findings from Step 3]
  
  You are reviewing [brand name]'s content strategy diagnostic. Based on the audit and research data:
  1. What is the SINGLE biggest problem in their content strategy?
  2. What would you change FIRST and why?
  3. What are they doing well that they should double down on?
  4. What is the blind spot they can't see from the inside?
  
  Be specific. Reference the audit data. No generic advice."
```

### 5. Synthesize Diagnostic Report

Combine the audit, research, and expert review into a single diagnostic:

**Scoring Framework**:
| Dimension | Score (1-10) | Evidence |
|-----------|-------------|---------|
| Trust Pathway Health | [score] | [from Workflow 04 audit] |
| Memorable/Forgettable Ratio | [score] | [from Workflow 04 audit] |
| Business Outcome Linkage | [score] | [from Workflow 04 audit] |
| Consistency × Experimentation Balance | [score] | [from Workflow 04 audit] |
| Audience Trust Signals | [score] | [from deep research] |
| Revenue Architecture | [score] | [from expert review] |
| **Composite Score** | **[average]** | |

### 6. Generate Prioritized Fix Plan

Rank fixes by impact/effort:

| Priority | Fix | Impact (H/M/L) | Effort (H/M/L) | Timeline | Evidence |
|----------|-----|----------------|----------------|----------|---------|
| 1 | [Fix] | [Impact] | [Effort] | [Days/weeks] | [Which data supports this?] |
| 2 | | | | | |
| 3 | | | | | |

### 7. Save Output
Save to `research_outputs/[date]-media-diagnostic-[brand-slug].md`

## Output Structure

```
# Media Diagnostic: [Brand Name]

## Executive Summary (BLUF — what's wrong and what to fix first)
## Content Portfolio Audit Results (from Workflow 04)
## Audience Behavior Research (from Perplexity)
## Expert Review Panel (from parallel swarm)
## Scored Diagnostic Dashboard
## Prioritized Fix Plan (ranked by impact/effort)
## 30-Day Recovery Sprint (immediate actions)
```
