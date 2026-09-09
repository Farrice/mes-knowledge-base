# PSA Cross-Platform Deployment Guide

## Overview

The Prompt System Architecture skill is designed to work across multiple AI development environments. This guide covers deployment for:

1. **Claude (Anthropic)** - Native skill format
2. **Google Antigravity** - Adapted skill format  
3. **Cursor** - Rules-based format
4. **Generic** - Portable prompt format

---

## Claude Deployment

### Installation
1. Package the skill: Upload the `/psa-skill/` folder to Claude
2. Or use the packaged `.skill` file directly

### Triggering
The skill activates when users mention:
- Prompt audit / prompt analysis
- AI output quality issues
- Inconsistent AI outputs
- Brand voice preservation
- Prompt engineering / prompt design

### Usage Example
```
Audit this prompt using PSA methodology:
[paste prompt]
```

---

## Google Antigravity Deployment

### Skill Adaptation

Create a skill in Antigravity's format at `~/.antigravity/skills/psa/`:

**skill.yaml**
```yaml
name: prompt-system-architecture
description: Transform inconsistent AI outputs into reliable, production-grade deliverables
version: 1.0.0
triggers:
  - prompt audit
  - prompt analysis
  - AI quality
  - output inconsistency
  - brand voice
```

**instructions.md**
[Copy the content from SKILL.md]

**scripts/audit.py**
[Copy audit_prompt.py - Antigravity executes Python directly]

### Antigravity-Specific Features

Leverage Antigravity's multi-agent capability:
```
Agent 1: Run PSA audit on current prompt
Agent 2: Research competitor approaches for this use case
Agent 3: Generate optimized prompt using 4-layer architecture
```

This parallel execution is unique to Antigravity and accelerates the full audit-to-redesign workflow.

---

## Cursor Deployment

### Rules Format

Add to `.cursorrules` in project root:

```markdown
# Prompt System Architecture Rules

When working with prompts or AI outputs:

## Audit Framework
Score prompts on 5 dimensions (1-5 each):
1. Context Clarity - Role, audience, constraints defined?
2. Process Structure - Reasoning sequence specified?
3. Output Precision - Deliverable specs concrete?
4. Voice Preservation - Brand voice captured?
5. Reliability Mechanisms - Self-checks embedded?

## 4-Layer Architecture
Always structure prompts with:
1. Context Foundation (role, audience, standards, boundaries)
2. Process Architecture (reasoning sequence, decision framework)
3. Output Specification (structure, tone, format, examples)
4. Feedback Loops (quality checklist, failure recovery)

## Red Flags
- "helpful assistant" → Replace with specific role
- "engaging content" → Define what engaging means
- "match brand voice" → Specify voice characteristics
- No process steps → Add reasoning sequence
- No validation → Add quality checklist
```

---

## Portable Prompt Format

For environments without skill systems, use this meta-prompt:

```markdown
You are now operating as a Prompt System Architect. Your role is to analyze 
and improve prompts using a rigorous 4-layer methodology.

# Your Methodology

## Diagnostic Framework (Score each 1-5)
1. **Context Clarity**: Role definition, audience awareness, constraints
2. **Process Structure**: Reasoning sequence, decision points, checkpoints
3. **Output Precision**: Structure, tone, format, quality anchors
4. **Voice Preservation**: Characteristics captured, anti-patterns identified
5. **Reliability Mechanisms**: Self-checks, failure recovery, iteration triggers

## Improvement Architecture
When redesigning prompts, always include:
- Layer 1: Context Foundation
- Layer 2: Process Architecture  
- Layer 3: Output Specification
- Layer 4: Feedback Loops

## Common Failure Patterns
- Vague roles ("helpful assistant")
- Missing process (jumps to output)
- Generic specs ("make it engaging")
- Absent voice ("match brand voice" without definition)
- No validation (no self-checks)

When asked to audit a prompt, provide:
1. Score across 5 dimensions
2. Top 3 findings
3. Redesigned prompt using 4-layer architecture
4. Expected improvement
```

---

## Selling the Skill

### Value Proposition by Platform

| Platform | Buyer | Value |
|----------|-------|-------|
| Claude | Agencies using Claude.ai | Consistent quality without per-prompt engineering |
| Antigravity | Dev shops on Google stack | Multi-agent prompt optimization workflows |
| Cursor | Engineering teams | Automated prompt quality in development |
| Generic | Anyone | Portable methodology that works everywhere |

### Pricing Tiers

**Skill License Only**: $500-1,000
- Packaged skill files for their platform
- Documentation
- Basic support

**Skill + Training**: $1,500-3,000
- Everything above
- 2-hour implementation session
- Custom voice framework for their brand
- 30 days email support

**Full Implementation**: $5,000-10,000
- Everything above
- Audit of existing workflows
- Custom skill adaptations
- Team training (up to 5 people)
- 90 days support

---

## Quick Conversion Reference

### Claude → Antigravity
- SKILL.md → skill.yaml + instructions.md
- references/ → context/ 
- scripts/ → scripts/ (direct Python execution)
- assets/ → assets/

### Claude → Cursor
- SKILL.md body → .cursorrules
- references/ → Additional .cursorrules or inline
- scripts/ → Not supported (Cursor doesn't execute)

### Key Differences

| Feature | Claude | Antigravity | Cursor |
|---------|--------|-------------|--------|
| Script execution | Via bash | Native Python | No |
| Multi-agent | No | Yes | No |
| Auto-trigger | Description match | Trigger keywords | Always active |
| File creation | Full | Full | Project-scoped |
