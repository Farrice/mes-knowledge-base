---
name: banana-squad-spawn
description: Master spawn prompt to create the full Banana Squad agent team in Claude Code for professional image generation
category: workflow-deployment
expert: mark-kashef
---

# Banana Squad Spawn

## Purpose
Deploy the full Banana Squad agent team in Claude Code to generate professional-grade images using the PaperBanana agentic framework + Gemini 3 Pro Image API.

## Prerequisites
- Claude Code with experimental agent teams enabled
- `GEMINI_API_KEY` set in `.env`
- Dependencies installed: `pip install google-genai Pillow python-dotenv`

## Usage
Copy the contents of `banana-squad/spawn-team-prompt.md` and paste as your first message in Claude Code. The Lead agent will initialize the team and ask clarifying questions.

## When To Use
- Creating content graphics, thumbnails, or social media images
- Generating brand-consistent illustrations
- Building visual assets that need to match a specific style guide
- Batch-generating image variations for A/B testing

## Key Configuration
| Parameter | Default | Notes |
|-----------|---------|-------|
| Prompt variations per brief | 5 | Prompt Architect generates 5 options |
| Maximum reference images | 14 | 3-5 recommended for best results |
| Critic threshold | 7/10 | Images below this are auto-rejected |
| Output format | PNG | Also supports JPEG, WebP |

## Workflow
1. Paste spawn prompt → Team initializes
2. Tell Lead what you need → Lead asks clarifying questions
3. (Optional) Drop reference images in `reference-images/` folders
4. Research Agent analyzes references → extracts visual DNA
5. Prompt Architect creates 5 narrative prompts
6. Generator Agent creates images via Gemini API → saves to `outputs/`
7. Critic Agent scores and ranks → Lead presents top results
8. Iterate conversationally until satisfied
