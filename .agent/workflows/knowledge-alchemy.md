---
description: Turn any expert video, article, or course into a reusable AI coaching prompt using Dan Koe's three-stage Knowledge Alchemy Pipeline
---

# /knowledge-alchemy — Expert Content → AI Coaching Prompt

Transform any expert content into a permanently deployable AI coaching prompt. Feeds source material through three refinement stages: Source → Compressed Guide → Phased Coaching Prompt.

## Usage

```
/knowledge-alchemy [YouTube URL, transcript, or pasted content]
```

## Steps

### 1. Load Skill Context
// turbo
Read these files in order:
1. `skills/dan-koe-ai-leverage/genius.md`
2. `skills/dan-koe-ai-leverage/workflows/01-knowledge-alchemy-engine.md`

### 2. Source Intake
Accept the user's source material. If a YouTube URL is provided:
```bash
// turbo
python3 execution/fetch-transcript.py "<youtube_url>" "<expert-name>"
```

Confirm:
- Expert identity
- Extraction focus (what methodology to capture)
- Coaching intent (what the final prompt should help the user DO)

### 3. Stage 1 — Knowledge Compression
Transform raw source into a Compressed Executive Guide:
- Strip filler and engagement-only content
- Extract core methodology as executable steps
- Preserve the expert's unique angle
- Surface hidden knowledge (what they do but don't explain)

Present guide to user for review.

### 4. Stage 2 — Prompt Alchemy
Transform the approved guide into a Phased Coaching Prompt:
- **Phase 1**: Context gathering — AI asks user situational questions
- **Phase 2**: Gated execution — guided step-by-step with feedback loops
- **Phase 3**: Adversarial review — stress-test the output

Run all 5 quality gate checks before delivering.

### 5. Stage 3 — Deployment
Present the complete coaching prompt with:
- Usage instructions
- Stacking suggestions from existing Antigravity skills
- "Prompt compounding" evolution note

## Quality Standard
- **$5K Test**: Would someone pay $5K for a mentor who coaches like this prompt?
- **Sovereignty Test**: Does the user maintain creative direction?
- **Compound Test**: Will using this prompt make the user's NEXT prompt better?
