---
description: Evaluate whether a company or product should rename using Placek's empirical evidence and structured decision framework
---

# Rename Evaluation Workflow

## Prerequisites
- Load `skills/david-placek-naming/SKILL.md` (Tier 1)
- For complex decisions: also load `genius.md` (Tier 2) for case studies and evidence base

## Steps

### 1. Intake
Gather from the user:
- Current name
- How long in use
- What prompted the rename discussion (growth stall, pivot, M&A, embarrassment?)
- Brand equity indicators (revenue, following, search volume)
- Has the product/company changed since naming?

### 2. Current Name Assessment
Deploy `comfort-trap-audit` on the current name:
- Score on 8 criteria
- Zone classification

### 3. Rename Decision Analysis
Deploy `rename-decision-framework` prompt:
- Build the plus-minus table
- Apply Placek's empirical evidence base
- Score the 6 decision indicators

### 4. Verdict
- **4+ Yes indicators → Rename Recommended**: Route to `naming-sprint` workflow
- **2-3 Yes → Evolve**: Suggest name modifications, tagline additions, or phonemic shifts
- **0-1 Yes → Keep**: Recommend alternative brand investments

### 5. If Rename Recommended
Present:
- Why the current name sits in the invisible zone
- Windsurf case study as evidence (Kodium → Windsurf, rename = launch moment)
- Naming sprint scope and timeline
- Psychological preparation: validate the "killing the baby" feeling, then present evidence

### 6. Deliverable
One-page rename decision brief:
- Current assessment summary
- Plus-minus analysis
- Decision score
- Recommended path forward
- Next steps with timeline

## Quality Gate
- [ ] Plus-minus analysis completed with scored evidence
- [ ] Placek evidence base applied (not just opinions)
- [ ] Competitive courage frame deployed
- [ ] Clear action path recommended
