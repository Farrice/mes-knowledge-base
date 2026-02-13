---
name: mark-kashef-banana-squad
description: AI-powered image generation via multi-agent orchestration using the PaperBanana framework + Gemini 3 Pro API
---

# Mark Kashef — Banana Squad Image Agent Team

## Overview

A deployable Claude Code agent team ("Banana Squad") that generates professional-grade images through a 5-agent pipeline: Research → Prompt Architect → Generator → Critic → Lead. Built on the PaperBanana agentic framework and powered by the Gemini 3 Pro Image API.

## Core Architecture

| Agent | Function |
|-------|----------|
| **Lead** | Orchestrates workflow, asks clarifying questions, presents results |
| **Research Agent** | Extracts visual DNA from reference images (style, composition, color, lighting, mood) |
| **Prompt Architect** | Creates 5 narrative prompts per brief using photography terminology |
| **Generator Agent** | Calls Gemini 3 Pro API, manages references, saves outputs |
| **Critic Agent** | Scores on 5 KPIs (composition, color, detail, brand, impact), gatekeeps quality |

## Deployable Prompts

| Prompt | Purpose |
|--------|---------|
| `banana-squad-spawn` | Deploy the full agent team in Claude Code |
| `reference-reverse-engineer` | Extract visual DNA from any image for style-matching |
| `visual-capitalist-infographic` | Generate data visualizations in Visual Capitalist style |
| `critique-loop-optimizer` | Configure quality thresholds and iteration depth |

## Key Principles

1. **Narrative over keywords** — Paragraph prompts outperform comma-separated tags
2. **5 variations per brief** — Prevents premature convergence
3. **Quantified critique** — Scores not opinions; quality floor enforced
4. **Reference-driven** — 3-5 reference images establish visual DNA
5. **Conversational iteration** — Multi-turn editing, not one-shot generation

## Quick Start

```bash
# 1. Install dependencies
pip install google-genai Pillow python-dotenv

# 2. Set up API key
cp banana-squad/.env.template banana-squad/.env
# Edit .env with your GEMINI_API_KEY

# 3. Open Claude Code with agent teams enabled
# 4. Paste contents of banana-squad/spawn-team-prompt.md
# 5. Tell the Lead what you need
```

## Project Directory

The working project lives at `banana-squad/` in the workspace root. See `banana-squad/CLAUDE.md` for full documentation.
