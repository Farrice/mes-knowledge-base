---
description: Pre-extraction creative brief
---

# /extract-vision — Extraction Vision Brief

Capture your creative direction for an extraction AND let the system autonomously identify highest-leverage opportunities from the source material. The two inputs merge into an **Extraction Vision Document** that guides every workflow decision downstream.

Run this alongside or immediately after `/extract`. It replaces the long-winded explanation with a structured, repeatable process.

## Usage

```
/extract-vision [expert name or source reference]
```

Run AFTER source material is available (transcript fetched, article read) but BEFORE workflow planning begins.

**Visual context note**: If the source is a video and `extractions/<expert-name>/visual-context.md` exists (auto-fetched by `/extract` Phase 1.6), **load it alongside the transcript** before answering the 5 vision questions below. Visual material directly informs Question 1 ("What grabs you?") — emotional center of gravity often lives in gesture, energy, on-screen choices, not just words. See [`directives/video-vision-protocol.md`](../../directives/video-vision-protocol.md).

If visual-context.md does not exist but the source is a video URL, you can opportunistically fetch it now:
```bash
// turbo
python3 execution/fetch-video-context.py "<source>" "<expert-name>" || true
```

## Steps

### 1. Capture the User's Creative Direction

Ask Farrice these 5 questions. If he's already provided context (in the same message or earlier), extract answers from what he said — don't re-ask what's already been answered.

**The 5 Vision Questions:**

1. **What grabs you?** — What about this expert or material got your attention? What instinct fired? (This reveals the emotional center of gravity — the workflows should orbit this.)

2. **What do you want to DEPLOY?** — Not just "learn" — what do you want to be able to DO after this extraction? Write differently? Diagnose problems? Build a new type of deliverable? (This determines whether workflows are diagnostic, generative, or editorial.)

3. **Creative latitude level?** — Scale of 1-3:
   - **1 — Guided**: "I know exactly what workflows I want, here they are"
   - **2 — Collaborative**: "I have some ideas, but surprise me with what you find"
   - **3 — Autonomous**: "Pull the highest-leverage things out — I trust the system"

4. **Workflow depth target?** — How many workflows, and how deep?
   - **Standard** (3-5): Core methodology capture
   - **Expanded** (6-10): Methodology + creative applications + cross-expert stacking
   - **Mastery** (10-15): Full practitioner-grade toolset, Eric Roth / Wright Thompson level

5. **Specific angles?** — Any specific techniques, quotes, or moments from the source material that MUST become workflows? (These get priority. Everything else is system-determined.)

### 2. Run the System's Leverage Analysis

With the source material loaded, autonomously analyze:

#### A. Uniqueness Audit
- What does this expert do that NO other Antigravity expert currently does?
- Where does their methodology overlap with existing experts? (Overlap = stacking opportunity, not redundancy)
- What's their "only they" insight — the one idea that, if you had nothing else, would justify the entire extraction?

#### B. Business Leverage Map
Score each major technique/insight on two axes:
- **Deployability** (1-5): How quickly can Farrice use this in client work, content, or products?
- **Differentiation** (1-5): How much does this separate Farrice's output from competitors?

Plot the top techniques on the matrix:

```
                    HIGH DIFFERENTIATION
                           │
          NICE-TO-HAVE     │     GOLD
          (workflow if     │  (workflow MANDATORY)
           budget allows)  │
    ───────────────────────┼───────────────────────
          SKIP             │     TACTICAL
          (reference only) │  (workflow if it's
                           │   fast to build)
                           │
                    LOW DIFFERENTIATION
    LOW DEPLOYABILITY ←────┼────→ HIGH DEPLOYABILITY
```

#### C. Cross-Expert Stacking Map
For each high-leverage technique, identify which existing Antigravity experts it stacks with:

```
[Technique] × [Expert] = [What the combination produces]
```

Example from Wright Thompson extraction:
- Thompson's Interiority Bridge × Nicolas Cole's Ghostwriting = Voice capture that goes beyond words to capture how a client THINKS
- Thompson's Hammer × Eric Roth's Erosion = Ending-first architecture refined through daily rewrite passes

#### D. Gap Fill Analysis
What capability does the Antigravity roster currently LACK that this expert provides? This is the strategic justification — it answers "why this extraction matters."

### 3. Produce the Extraction Vision Document

Merge the user's direction with the system's analysis into a single document:

```markdown
# Extraction Vision: [Expert Name]

## Creative Direction (from Farrice)
- **Emotional center**: [what grabbed him]
- **Deployment target**: [what he wants to DO]
- **Latitude**: [1-3]
- **Depth**: [Standard / Expanded / Mastery]
- **Priority techniques**: [any specifics]

## System Leverage Analysis
- **"Only they" insight**: [the one idea that justifies the extraction]
- **Gold quadrant techniques**: [high deploy × high differentiation]
- **Top stacking opportunities**: [technique × expert = output]
- **Gap filled**: [what capability this adds to the roster]

## Workflow Recommendations
| # | Workflow Name | Source Technique | Leverage Score | Rationale |
|---|-------------|-----------------|---------------|-----------|
| 1 | ... | ... | ... | ... |

## Vision Statement
[2-3 sentences: what this extraction will enable Farrice to do that he couldn't do before]
```

### 4. Checkpoint

Present the Extraction Vision Document. Wait for approval before proceeding to workflow creation.

If running alongside `/extract`, this document replaces the standard "Proposed 3-5 workflows" checkpoint — it IS the checkpoint, but richer.

---

## When to Use
- At the START of any new extraction
- When Farrice has strong opinions about what he wants from the source material
- When the source material is dense enough to support 6+ workflows
- When you want the extraction to be strategically targeted, not just comprehensive

## When NOT to Use
- Quick/light extractions where 3 standard workflows are sufficient
- When Farrice says "just do the standard extract"
- Reconversions of existing skills (use `/convert-extraction` instead)

## Pairs With
- `/extract` — vision feeds into extract's workflow planning step
- `/extract-forge` — forge has vision built in; use this command standalone when you want vision WITHOUT the full forge pipeline
- `/extract-amplify` — the vision document becomes the reference for what "more" means during amplification

## Downstream Contract (added 2026-07-19)

Vision is a planning artifact — it builds nothing itself. Whichever build path consumes this Vision Document (`/extract`, `/extract-forge`, or a manual build) MUST ship the **Prompt Forging Gate** (`directives/prompt-forging-spec.md`): born-v2 structure-pure prompts in `references/prompts-v2/` + the four wiring steps (renaissance_audit 0-fail → prompt_library build → wire_prompt_pointers --write → per-workflow cross-ref lines). A vision that hands off to a build without this gate is handing off half-finished work — carry this clause into the build checkpoint.
