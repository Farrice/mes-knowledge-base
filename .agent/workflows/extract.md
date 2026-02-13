---
description: Extract expert knowledge from source material and convert to an Antigravity skill
---

# /extract — Mastery Extraction Workflow

Extract expert knowledge from any source material and produce a deployable Antigravity skill.

## Usage

```
/extract [source material — paste transcript, provide URL, or reference a file]
```

## Steps

### 1. Receive Source Material
Accept transcript, article, course content, interview, or any knowledge-dense material. If the user provides a URL, read the content first.

### 1.5. Expert Identification (CRITICAL)
Before extraction, explicitly confirm the **expert/speaker** identity:
- The "by [Name]" in transcript headers (e.g. "Transcript for [Title] by [Merlin AI]") often refers to the **transcription tool**, NOT the speaker
- Common transcription tools: Merlin AI, Otter.ai, Tactiq, YouTube auto-captions — these are NEVER the expert
- Check the video title, channel name, and transcript content for the actual expert
- If the expert is already in the system (check `GEMINI.md` agent/skill tables), note existing skills for dedup in Step 3
- If ambiguous, **ask the user** before proceeding — never guess
- Record: `Expert: [Name] | Transcribed by: [Tool]`

### 2. Run Extraction
Read and execute `directives/mes-3.0-extract.md`.

- Determine extraction tier (Light / Standard / Deep) based on material depth
- Produce the extraction report
- Generate crown jewel prompts
- Run each prompt through the internal validation checklist before finalizing

### 2.5. Applied Intelligence Analysis (MANDATORY)
After extraction, perform a second pass focused on **deployable capability**:

**A. Meaning Mining** — Go beyond what the expert said. What are they *trying to express*? What insight lives between the lines? What would you only understand after watching them work for a year? Capture what Farrice's pattern recognition would flag.

**B. Capability Unlock** — For each major insight, answer:
- What can Farrice **BUILD** with this that he couldn't before?
- What **decisions** can he now make better?
- How does this **stack** with existing Antigravity skills?
- What **agent, product, workflow, or revenue stream** does this enable?

**C. Market Signal Reading** — If the expert discusses market data, ecosystem trends, or user behavior patterns:
- What is the market *signaling* it wants?
- Where are the underserved verticals?
- What would a functioning agent/product look like in this space?

**D. System Enhancement** — Could any insight improve how Antigravity itself operates?
- Better agent architectures?
- Better prompt design patterns?
- Better workflow structures?
- New skill stacking combinations?

Fold these findings into the extraction report under an **"Applied Intelligence"** section, and ensure relevant crown jewel prompts reflect this applied depth.

### 3. Validate (Recommended)
// turbo
Read and execute `directives/mes-3.0-validate.md`.

- Run all 4 validation checks
- Auto-fix any practitioner mode failures
- Flag CEV or dedup issues for user review
- If validation passes clean, proceed to conversion

### 4. Convert to Skill
// turbo
Read and execute `directives/extraction-to-skill.md`.

- Create skill directory structure
- Map extraction components to skill files
- Generate SKILL.md with overview and prompt arsenal listing
- Place crown jewel prompts in `references/prompts/`
- Place genius patterns in `references/genius-patterns.md`

### 5. Register
// turbo
Add the new skill and its prompts to `GEMINI.md` in the Available Skills and Skill Prompt Quick Reference sections.

If the expert already has an agent (`agents/[expert-name]/AGENT.md`), update it with the new skill. If not, create the agent directory and AGENT.md.

### 6. Report
Present a summary to the user:
- Expert name and domain
- Extraction tier used
- Number of genius patterns identified
- Number of crown jewel prompts generated
- **Applied Intelligence highlights** — top 2-3 capability unlocks
- Validation result (if run)
- Skill location in the system
- Any flags or decisions needed

## Options

- **Skip validation**: User can say "skip validation" or "light extract" to bypass Step 3
- **Deep extract**: User can say "deep extract" to force Deep tier regardless of material size
- **Validate only**: User can say "/validate [skill name]" to run validation on an existing extraction

## Extraction Philosophy

This system exists to build Farrice's Iron Man suit — each extraction adds a new module. We don't extract to document; we extract to **deploy**. Every extraction should leave Farrice with a capability he didn't have before. Surface-level pattern matching is failure. We go deep into what the expert means, what they enable, and how it compounds with everything else in the arsenal.

The goal: a solopreneur operating with 30-40 experts worth of compound intelligence, producing work that's grounded in world-class methodology, deployed through agentic workflows, and generating real revenue.
