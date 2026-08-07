---
description: Mid/post-extraction enrichment
---

# /extract-amplify — Extraction Amplification

Take an existing extraction or skill and find the value the first pass left behind. Produces additional workflows, deeper genius patterns, cross-expert stacking chains, and creative applications.

This is the "I want more from this" command. Use it during an extraction to go deeper, or after an extraction is complete to revisit with fresh eyes.

## Usage

```
/extract-amplify [expert name or skill directory]
```

Can also be invoked contextually mid-conversation: "amplify this extraction" or "I want more from this."

## Steps

### 1. Load the Existing Extraction

Read, in order:
1. The source material (transcript/article) — `extractions/[expert]/transcript.txt` or equivalent
2. The current skill files — `skills/[skill-name]/SKILL.md`, `genius.md`
3. All existing workflow files — `skills/[skill-name]/workflows/*.md`

Build a coverage map: what is currently captured vs. what exists in the source.

### 2. Run the Four Scans

Execute all four scans against the source material. Each scan produces specific, actionable findings.

#### Scan A: Gap Scan — What's Missing?

Re-read the source material line by line. For every technique, insight, or methodology:
- Is it captured in a workflow? → Mark as COVERED
- Is it in genius.md but not a workflow? → Mark as LATENT
- Is it not captured anywhere? → Mark as MISSED

Focus on MISSED items. For each:
```
MISSED: [Technique/insight name]
Source quote: "[exact quote from transcript]"
Why it matters: [what it enables]
Workflow potential: [HIGH/MEDIUM/LOW]
Proposed name: [if HIGH]
```

#### Scan B: Depth Scan — What Could Be Deeper?

Existing workflows may be surface-level or overly broad. For each current workflow:
- Could it be split into 2+ more granular tools?
- Does it have untapped content-type adaptations?
- Is the quality rubric specific enough?

Example: A generic "story structure" workflow might split into:
- Opening architecture (the first 200 words)
- Mid-piece pivot (the structural hinge)
- Ending engineering (the hammer/landing)

Flag any workflow where splitting would produce more deployable, practitioner-grade tools.

#### Scan C: Cross-Expert Stacking Scan — Who Does This Pair With?

For each existing AND proposed workflow, map stacking opportunities with other Antigravity experts:

```
STACK: [Workflow] × [Expert Skill/Workflow]
What it produces: [the compound output]
Deploy when: [trigger scenario]
Example chain: [specific step-by-step]
```

Check these expert categories for stacking:
- **Writing craft**: Eric Roth, Michael Connelly, Wright Thompson, Steven Pressfield
- **Copy & persuasion**: Luke Iha, Joanna Wiebe, David McRaney
- **Content strategy**: Lara Acosta, Kallaway, Nicolas Cole, Diandra Escobar
- **Brand & creative**: Oren, Grace, Greg Hoffman
- **Business**: Samuel Thompson, Seena Rez, Nick Saraev
- **Consumer psychology**: Dai Media, Dan Koe

#### Scan D: Creative Application Scan — What Else Could This Do?

The most valuable extractions find non-obvious applications. For each major technique:
- **Ghostwriting application**: How does this change how Farrice writes for clients?
- **Content application**: How does this change LinkedIn/newsletter/Substack output?
- **Client service application**: Could this become a deliverable Farrice sells?
- **System application**: Could this improve how Antigravity itself works?

Be creative. The best applications are the ones that make you think "I never would have thought to use it that way."

### 3. Produce the Amplification Report

```markdown
# Amplification Report: [Expert Name]

## Coverage Summary
- Techniques in source: [N]
- Currently captured: [N] (X%)
- Latent (in genius.md, no workflow): [N]
- Missed entirely: [N]

## Proposed New Workflows
| # | Name | Source Technique | Leverage | Pairs With |
|---|------|-----------------|----------|-----------|
| 1 | ... | ... | ... | ... |

## Depth Expansion Candidates
| Current Workflow | Split Into | Why |
|-----------------|-----------|-----|
| ... | ... | ... |

## Top Stacking Chains
1. [Workflow] × [Expert] = [Output] — [when to deploy]
2. ...

## Non-Obvious Applications
1. [Application] — [which technique + how it applies]
2. ...

## Recommended Actions (Priority Order)
1. [Highest-impact action]
2. ...
```

### 4. Checkpoint

Present the Amplification Report. The user decides:
- **Build proposed workflows** → Execute workflow creation for approved items
- **Update existing workflows** → Add stacking guides, content-type adaptations, depth
- **Add to genius.md** → Incorporate missed patterns into the genius context
- **Log and move on** → Save the report as reference, no immediate action

---

## When to Use
- After any extraction when you feel there's more to get
- When an expert's source material is particularly rich (10,000+ words, multi-topic)
- When you discover a new application for an existing skill weeks/months later
- When a new expert extraction reveals stacking opportunities with an older one
- When Farrice says "I want more from [expert]" or "go deeper on this"

## When NOT to Use
- During initial extraction (use `/extract-vision` instead to front-load the enrichment)
- For extractions with thin source material (< 3,000 words) — there may not be more to find
- When the issue is workflow QUALITY not quantity — refine existing workflows instead

## Pairs With
- `/extract-vision` — the vision document tells amplify what "more" means
- `/extract` — amplify is the natural follow-up to any standard extraction
- `/extract-forge` — forge has amplification built in; use this standalone when revisiting older extractions
