---
name: prompt-system-architecture
description: Transform inconsistent AI outputs into reliable, production-grade deliverables through systematic prompt engineering. Use when AI outputs are inconsistent, generic, or failing to capture brand voice. Use for prompt audits, system design, output quality improvement, brand voice preservation, and building reusable prompt frameworks. Targets AI agencies, marketing consultancies, and teams struggling with AI quality control.
---

> **Provenance:** Imported from Cowork 2026-09-01 (Fresh's exported skills package).

# Prompt System Architecture (PSA)

## Purpose

Convert chaotic prompting into systematic architectures that produce consistent, high-quality outputs. This skill operationalizes the gap between "AI can do this" and "AI reliably does this at production quality."

## Core Framework: The 4-Layer Architecture

### Layer 1: Context Foundation
Establish persistent context that grounds all outputs.

**Components:**
- Domain expertise profile (who is the AI being?)
- Audience awareness (who receives the output?)
- Quality standards (what defines "good"?)
- Constraint boundaries (what to avoid?)

**Pattern:**
```
You are [ROLE] with expertise in [DOMAINS].
Your audience is [AUDIENCE PROFILE].
Quality means [SPECIFIC CRITERIA].
Never [BOUNDARIES].
```

### Layer 2: Process Architecture
Define the cognitive workflow the AI follows.

**Components:**
- Reasoning sequence (think → plan → execute → validate)
- Decision frameworks (how to choose between options)
- Checkpoint gates (where to pause and verify)

**Pattern:**
```
Before responding:
1. [ANALYSIS STEP]
2. [PLANNING STEP]
3. [EXECUTION STEP]
4. [VALIDATION STEP]
```

### Layer 3: Output Specification
Define exact deliverable requirements.

**Components:**
- Structure templates (headers, sections, flow)
- Tone calibration (voice characteristics)
- Format requirements (length, style, elements)
- Example anchors (concrete references)

**Pattern:**
```
Output must include:
- [STRUCTURAL ELEMENTS]
- [TONE: specific descriptors]
- [FORMAT: length/style]

Example of target quality:
[CONCRETE EXAMPLE]
```

### Layer 4: Feedback Loops
Build self-correction mechanisms.

**Components:**
- Quality checklist (self-review criteria)
- Failure recovery (what to do when stuck)
- Iteration triggers (when to refine)

**Pattern:**
```
Before finalizing, verify:
□ [QUALITY CHECK 1]
□ [QUALITY CHECK 2]
□ [QUALITY CHECK 3]

If any fail, revise accordingly.
```

## Diagnostic Protocol: The PSA Audit

When assessing existing prompts or AI workflows, evaluate across five dimensions:

### 1. Context Clarity (Score 1-5)
- Is the AI's role explicitly defined?
- Is audience awareness embedded?
- Are domain constraints specified?

### 2. Process Structure (Score 1-5)
- Is there a defined reasoning sequence?
- Are decision points explicit?
- Does it prevent premature output?

### 3. Output Precision (Score 1-5)
- Are deliverable specs concrete?
- Is the quality bar exemplified?
- Are format requirements unambiguous?

### 4. Voice Preservation (Score 1-5)
- Is brand voice captured (not just described)?
- Are anti-patterns identified?
- Does it pass the "sounds like them" test?

### 5. Reliability Mechanisms (Score 1-5)
- Are self-checks embedded?
- Is there failure recovery?
- Can outputs be validated against criteria?

**Scoring:**
- 20-25: Production-ready system
- 15-19: Functional with gaps
- 10-14: Needs architectural work
- Below 10: Rebuild recommended

## Common Failure Patterns

### The Vague Role
❌ "You are a helpful assistant"
✅ "You are a senior content strategist specializing in B2B SaaS, writing for marketing leaders who are skeptical of AI-generated content"

### The Missing Process
❌ "Write me a blog post about X"
✅ "First, identify the core insight. Then, outline the argument structure. Then, draft with concrete examples. Finally, review for [specific criteria]."

### The Generic Output Spec
❌ "Make it engaging and professional"
✅ "Tone: Confident but not arrogant. Use 'we' for company, 'you' for reader. One surprising stat per section. Open loops between sections."

### The Absent Voice
❌ "Match our brand voice"
✅ "Voice characteristics: Contrarian takes delivered conversationally. Uses analogies from [specific domains]. Never uses: 'leverage,' 'synergy,' 'utilize.' Sentences average 12 words."

## Implementation Workflow

### Phase 1: Discovery
1. Audit existing prompts/workflows
2. Collect output samples (good and bad)
3. Interview stakeholders on quality gaps
4. Map current failure patterns

### Phase 2: Architecture
1. Design 4-layer system for each use case
2. Build voice preservation framework
3. Create output specification templates
4. Develop quality validation checklists

### Phase 3: Testing
1. Run system against historical inputs
2. Compare outputs to known-good examples
3. Identify edge cases and failure modes
4. Refine based on results

### Phase 4: Deployment
1. Document the system for team use
2. Create quick-reference guides
3. Build feedback collection mechanism
4. Schedule iteration cycles

## Deliverable Templates

See `references/templates.md` for:
- Prompt Audit Report template
- 4-Layer System Design document
- Voice Preservation Framework
- Quality Validation Checklist

See `references/examples.md` for:
- Before/after prompt transformations
- Industry-specific adaptations
- Common use case architectures

## Pricing Guidance

| Service | Scope | Price Range |
|---------|-------|-------------|
| PSA Audit | Single workflow assessment | $300-500 |
| System Design | Complete 4-layer architecture | $1,500-3,000 |
| Voice Framework | Brand voice preservation system | $800-1,500 |
| Full Implementation | Discovery → Deployment | $5,000-10,000 |
| Retainer | Ongoing optimization | $1,000-2,000/mo |

## Quick Commands

**Run audit on existing prompt:**
"Analyze this prompt using the PSA 5-dimension diagnostic. Score each dimension and identify the top 3 improvements."

**Design new system:**
"Create a 4-layer prompt architecture for [USE CASE] targeting [AUDIENCE] with [QUALITY CRITERIA]."

**Extract voice:**
"Analyze these [N] samples and create a Voice Preservation Framework capturing the distinctive patterns, anti-patterns, and quality markers."
