---
description: Set up a fully context-loaded, scope-defined AI session with quality gates at every phase using Dan Koe's 4C framework
---

# /4c-architect — Architect a High-Stakes AI Work Session

Structure any important AI interaction through the 4C Cognitive Architecture: Context → Clarification → Creation → Concerns. Ensures maximum output quality by checking all four gates before accepting any result.

## Usage

```
/4c-architect [describe what you're trying to accomplish]
```

## Steps

### 1. Load Skill Context
// turbo
Read these files in order:
1. `skills/dan-koe-ai-leverage/genius.md`
2. `skills/dan-koe-ai-leverage/workflows/03-4c-interaction-architect.md`

### 2. Session Scoping
Define the session architecture:
- **Objective**: What specific deliverable is the user producing?
- **Stakes level**: Casual / Working / Final / Strategic
- **Output format**: Conversation (interactive) / Structured output (one-shot) / Defined task (delegation)
- **Expert sources**: Any specific methodologies or Antigravity skills to load

Set quality threshold based on stakes level.

### 3. C1 — Context Loading
Curate and load context sources:
- Check `SKILL_INDEX.md` and `AGENT_INDEX.md` for relevant Antigravity skills
- If user provides external sources (YouTube URLs, articles), process them
- If no expert source exists, generate top approaches and let user select
- Compress each source into operational methodology

Present loaded context to user for confirmation.

### 4. C2 — Clarification
Surface every dimension only the user can define:
- Taste & style preferences
- Hard constraints and boundaries
- Audience expectations
- Voice and tone
- Relevant precedent (what worked, what failed)

Explicitly state all AI assumptions and get user correction before proceeding.

### 5. C3 — Creation
Produce the deliverable matching the objective and format:
- **Conversation**: Iterative dialogue with decision points
- **Structured output**: Complete deliverable in one pass
- **Defined task**: Direct execution with constraints applied

### 6. C4 — Concerns
Run the Concerns pass before finalizing:
- **Self-audit**: Surface assumptions made during creation
- **Proactive disclosure**: Present output WITH its known weaknesses
- **Adversarial invitation**: Offer to run `/adversarial-refine` on the output

### 7. Deliver
Present final output with:
- Session architecture summary
- Context sources used
- Assumptions confirmed
- Known limitations flagged

## Quality Standard
- **Completeness Test**: All four C's checked — none skipped
- **Employee Test**: Output quality exceeds what a trained employee would produce
- **Sovereignty Test**: User maintained creative direction throughout
