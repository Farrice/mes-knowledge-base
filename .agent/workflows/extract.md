---
description: Extract expert knowledge from source material and convert to a completion-engine skill
---

# /extract — Mastery Extraction Workflow (v2.0 — Completion Engine)

Extract expert knowledge from any source material and produce a deployable completion-engine skill with 3-5 end-to-end workflows.

## Usage

```
/extract [source material — paste transcript, provide URL, or reference a file]
```

## Steps

### 1. Receive Source Material
Accept transcript, article, course content, interview, or any knowledge-dense material. If the user provides a URL, read the content first.

**If the user provides a YouTube URL**, auto-fetch the transcript:
```bash
// turbo
python3 execution/fetch-transcript.py "<youtube_url>" "<expert-name>"
```
This saves the transcript to `extractions/<expert-name>/transcript.txt`. If expert name is unknown yet, omit it and the transcript saves to `extractions/transcripts/<video_id>.txt` — move it after expert identification in step 1.5.

### 1.5. Expert Identification (CRITICAL)
Before extraction, explicitly confirm the **expert/speaker** identity:
- The "by [Name]" in transcript headers often refers to the **transcription tool**, NOT the speaker
- Common transcription tools: Merlin AI, Otter.ai, Tactiq, YouTube auto-captions — these are NEVER the expert
- Check the video title, channel name, and transcript content for the actual expert
- If the expert is already in the system (check `AGENT_INDEX.md`), note existing skills for dedup
- If ambiguous, **ask the user** before proceeding — never guess
- Record: `Expert: [Name] | Transcribed by: [Tool]`

### 2. Run Extraction
Read and execute `directives/mes-3.0-extract.md`.

- Determine extraction tier (Light / Standard / Deep) based on material depth
- Produce the extraction report with genius patterns, hidden knowledge, and methodology
- Run each finding through the internal validation checklist before finalizing

### 2.5. Applied Intelligence Analysis (MANDATORY)
After extraction, perform a second pass focused on **deployable capability**:

**A. Meaning Mining** — Go beyond what the expert said. What insight lives between the lines?

**B. Capability Unlock** — For each major insight:
- What can Farrice **BUILD** with this?
- What **decisions** can he now make better?
- How does this **stack** with existing skills?

**C. Market Signal Reading** — If market data discussed:
- What is the market signaling it wants?
- Where are underserved verticals?

**D. System Enhancement** — Could any insight improve Antigravity itself?

Fold findings into the extraction report under an **"Applied Intelligence"** section.

### 3. Validate (Recommended)
Read and execute `directives/mes-3.0-validate.md`.

### 4. CHECKPOINT 1: Workflow Planning
**This is a user decision point.** Present:

- Expert name and domain
- Number of genius patterns + hidden knowledge items extracted
- **Proposed 3-5 workflows** — for each:
  - Name and what it produces
  - Which aspects of the expert's methodology it captures
  - When a user would trigger it
- Any flags or concerns

**Wait for user approval/adjustment before proceeding.**

If user approves, continue. If user adjusts, incorporate changes.

### 5. Generate Completion Engine Skill
// turbo

#### 5a. Create Skill Directory
```bash
mkdir -p skills/[skill-name]/workflows agents/[expert-name]/memory
```

#### 5b. Create genius.md
Merge all genius patterns + hidden knowledge into a single unified genius context file:
```
skills/[skill-name]/genius.md
```

#### 5c. Generate Workflow Files
For each approved workflow, generate an end-to-end workflow file:
```
skills/[skill-name]/workflows/01-[workflow-name].md
skills/[skill-name]/workflows/02-[workflow-name].md
skills/[skill-name]/workflows/03-[workflow-name].md
```

Each workflow MUST:
- Load the full genius context (genius.md)
- Produce a specific, defined deliverable
- Mirror how the expert actually thinks (integrated flow, not decomposed steps)
- Embed genius patterns INLINE where they apply
- Include Output Contract (exact specification of deliverable)
- Include Quality Gate (expert-specific criteria)

Alternatively, use the conversion swarm for parallel generation:
```bash
python execution/skill_converter.py --skill "skills/[skill-name]"
```

#### 5d. Write SKILL.md
Use the completion engine format:
```markdown
---
name: "[Expert] — [Domain]"
description: "[Value prop]"
version: "2.0"
format: "completion-engine"
workflows: [N]
---

# [Expert] — [Domain]

[2-3 sentence expert context + core genius]

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 01 | [Name] | [Deliverable] | [Trigger] |
...

## Quick Reference
- **Genius Context**: [genius.md](genius.md)
```

### 6. Create Agent Files
// turbo

#### AGENT.md
Standard agent template with identity, competencies, decision framework, voice, and available workflows.

#### memory/context.md
Initialize with activation date. Will be updated as the agent is used.

### 7. Register
// turbo
Add to `AGENT_INDEX.md` and `SKILL_INDEX.md` with the new format indicators.

### 8. CHECKPOINT 2: Quality Verification
**User reviews one workflow output** to confirm quality meets expectations.

Present:
- One sample workflow file (the primary/most important one)
- Workflow count and names
- Registration confirmation

If quality passes, skill is DEPLOYED. If not, iterate on specific issues.

### 9. Performance Log
Log this extraction to the feedback ratchet (see `directives/feedback-ratchet.md`):

```python
from execution.log_performance import log_output

log_output(
    output="[Expert Name] — [Domain] extraction ([tier] tier)",
    agent="[expert-agent-name]",
    skill="[skill-directory-name]",
    workflow="extract",
    task_type="Extraction",
    quality_score=[1-10 composite from quality gate],
    intent_alignment=[1-10],
    expert_standard=[1-10],
    adversarial_resilience=[1-10],
    status="Keep",  # or "Needs Improvement" if quality < 7
    notes="[genius patterns count], [workflows count], [key insight]",
)
```

If this is the first extraction for this skill, set status to "Baseline".

### 10. Report
Present summary:
- Expert name and domain
- Extraction tier used
- Genius patterns + hidden knowledge counts
- **Workflows created** (count + names)
- Applied Intelligence highlights
- Skill location in the system
- **Quality Score** (from performance log)

## Options

- **Skip validation**: "skip validation" or "light extract" to bypass Step 3
- **Deep extract**: "deep extract" to force Deep tier
- **Validate only**: "/validate [skill name]" for existing extractions

## Extraction Philosophy

This system builds Farrice's Iron Man suit — each extraction adds a new module. We don't extract to document; we extract to **deploy**. Every extraction leaves Farrice with a capability he didn't have before.

The completion engine format ensures that each capability is a **self-contained workflow** that carries the expert's full genius and produces a finished deliverable. No more fragmented prompts that dilute the nuance. The expert's integrated thinking stays integrated.
