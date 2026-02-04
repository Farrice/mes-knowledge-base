---
name: creative-assembly
version: 1.0.0
description: Multi-expert parallel production pipeline with structured handoffs and quality gates
expert: System (synthesized from Boris, Lance & Yichao)
domain: Creative Production
---

# Creative Assembly Skill

Multi-expert creative production with parallel execution, structured handoffs, and quality gates.

## The Core Shift

**Before:** Manually prompt one expert, get output, switch context, prompt another, switch again...
**After:** Describe what you want. Experts work in stages, hand off through structured contracts, refine, deliver polished output.

---

## Two Operating Modes

### Mode 1: Full Assembly (Default)
Experts produce → hand off → refine → deliver **one polished piece**

**Trigger:** "Write me..." / "Create a..." / "I need a..."

### Mode 2: Selection Assembly  
Experts create multiple versions → you pick → then polish

**Trigger:** "...show me options" / "...give me versions"

---

## The Pipeline

```
MAESTRO (You)
    ↓
DECOMPOSE → What components/versions needed
    ↓
ASSIGN EXPERTS → Based on task type (see matrix below)
    ↓
PRODUCE → Each expert creates their component/version
    ↓  
ASSEMBLE → Best elements combined (Full) OR presented for selection (Selection)
    ↓
EDITOR PASS → Tighten, ensure coherence, quality gate
    ↓
DELIVER → Polished piece with confidence level
```

---

## Expert Assignment Matrix

| Task Type | Primary Experts | Support Experts |
|-----------|-----------------|-----------------|
| Sales email | @david-deutsch, @cardinal-mason | @harry-dry (hooks), @nicolas-cole (clarity) |
| LinkedIn post | @kallaway, @nicolas-cole | @shaan-puri (stories) |
| Sales page | @david-deutsch, @alen-sultanic | @bond-halbert (fascinations) |
| Video script | @kallaway, @seena-rez | @oscar-hoglund (pacing) |
| Story/narrative | @mitch-albom, @lucas-alpay | @donald-miller (structure) |
| Hooks/headlines | @kallaway, @harry-dry | @bond-halbert |
| Email sequence | @cardinal-mason | @david-deutsch |

---

## Handoff Protocol

Each handoff includes structured context:
```
HANDOFF BRIEF
━━━━━━━━━━━━━
From: [Role]
To: [Role]  
Task completed: [What was done]
Key decisions: [Creative choices made]
Ready for: [Next step]
```

---

## Quality Gates

Before any handoff:
1. Self-verify output against brief
2. Flag gaps or concerns
3. State confidence level
4. No handoff if below quality threshold — retry first

Editor has explicit permission to:
- Reject weak outputs and request revision
- Push back on assembly decisions
- Flag when final piece isn't good enough

---

## Prompts Index

| # | Prompt | Purpose |
|---|--------|---------|
| 01 | [full-assembly-orchestrator](references/prompts/01-full-assembly-orchestrator.md) | Default mode: experts collaborate → one polished piece |
| 02 | [selection-assembly-orchestrator](references/prompts/02-selection-assembly-orchestrator.md) | Multiple versions → user selects → polish |
| 03 | [editor-pass](references/prompts/03-editor-pass.md) | Final quality gate and refinement |

---

## Invocation

This skill activates automatically when you request creative production. Natural language triggers the appropriate mode.

**"Write me a sales email for my consulting offer"** → Full Assembly
**"Write me a LinkedIn post — show me options"** → Selection Assembly
