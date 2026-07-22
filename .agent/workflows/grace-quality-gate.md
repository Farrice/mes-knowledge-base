---
description: Pre-publish quality gate
---

# /grace-quality-gate

> **When to use**: Before publishing any high-stakes content piece. Chains Grace Andrews' quality workflows with the system-wide slop detector for a comprehensive pre-publish audit.

## Usage
```
/grace-quality-gate
```
Or: "run grace-quality-gate", "@grace-quality-gate", "is this ready to publish?"

## What It Does

Four-layer quality gate before any content goes live:

### Layer 1: Bar-Raising Audit (Workflow 16)
— Competitive scan, differentiation claims, anti-romanticism check, testing protocol

### Layer 2: Emotional Residue Check (Workflow 15)
— 48-Hour Memory Test, residue moment identification, relief-seeking compliance

### Layer 3: Niche Precision Check (Workflow 17)
— Named person verification, relief-first design, multi-touchpoint entry design

### Layer 4: AI Slop Detector (/slop-check)
— Vocabulary kills, em-dash abuse, structural tropes, rhythm uniformity, emotional tells

## Steps

1. **Load Context**
   - Read `skills/grace-andrews-media-company/genius.md`
   - Read `skills/grace-andrews-media-company/workflows/16-bar-raising-audit.md`
   - Read `skills/grace-andrews-media-company/workflows/15-emotional-residue-engineer.md`
   - Read `skills/grace-andrews-media-company/workflows/17-audience-niche-laser.md`

2. **Collect the Content Piece**
   - Get the draft from the user (text, document, or file path)
   - Identify platform, trust stage tag, and intended audience

3. **Layer 1: Bar-Raising Audit** (Workflow 16)
   - Competitive scan (top 3 alternatives)
   - Differentiation claims (what's categorically different?)
   - Anti-romanticism audit (section-by-section data vs. feeling)
   - Pre-publish test variants (5+ title/hook variants, 3+ opening variants)
   - **Score**: Differentiation /10

4. **Layer 2: Emotional Residue Check** (Workflow 15)
   - 48-Hour Memory Test (both questions)
   - Identify the ONE residue moment
   - Verify architectural placement (buildup + afterglow)
   - Classify residue type
   - **Score**: Memorability /10

5. **Layer 3: Niche Precision Check** (Workflow 17)
   - Named person identification (can you name the specific reader?)
   - Relief-seeking compliance (upfront relief before strategic goal?)
   - Multi-touchpoint entry design (works as standalone entry point?)
   - Breadth paradox (specific enough to feel personal?)
   - **Score**: Precision /10

6. **Layer 4: Slop Check** (if content was AI-assisted)
   - Run `/slop-check` on the final draft
   - Flag: vocabulary kills, em-dash abuse, "nestled," "tapestry," "I found myself"
   - **Score**: Authenticity /10

7. **Composite Verdict**
   ```
   # Quality Gate Report: [Content Title]

   ## Layer 1 — Bar-Raising: [X/10]
     - Differentiation: [specific claims]
     - Romanticism: [any emotional-only sections flagged]
   ## Layer 2 — Emotional Residue: [X/10]
     - Residue Moment: [one sentence]
     - 48-Hour Test: [PASS/FAIL]
   ## Layer 3 — Niche Precision: [X/10]
     - Named Person: [name + situation]
     - Relief-First: [PASS/FAIL]
   ## Layer 4 — Slop Check: [X/10]
     - Flags: [any AI artifacts detected]

   ## COMPOSITE: [avg/10]
   ## VERDICT: [PUBLISH / ITERATE (weakest layer) / KILL]
   ```

8. **Quality Gate Thresholds**
   - **Composite ≥7**: PUBLISH
   - **Composite 5-6**: ITERATE — fix the weakest layer, re-run that layer only
   - **Composite <5**: Back to drafting. Piece needs fundamental rework
   - **Anti-perfectionism guard**: If composite ≥7 and you're still hesitating → SHIP IT. Testing > perfection (HK-6)

**Execution prompts**: before producing the deliverable, check `skills/grace-andrews-media-company/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
