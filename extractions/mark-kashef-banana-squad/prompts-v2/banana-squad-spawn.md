---
name: "Banana Squad Spawn"
source_prompt: "extractions/mark-kashef-banana-squad/prompts/banana-squad-spawn.md"
skill: mark-kashef-banana-squad
standard: structure-pure-v2
refactored: 2026-07-11
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

## Output Contract
- **Deliverable**: the Lead agent's initialization response confirming the team is live and gathering what it needs to start the first brief — not an image, not code.
- **Format**: a single chat/markdown response.
- **Length**: under ~250 words — confirm the roster and environment state, ask what's missing, stop.
- **Required components**: (a) confirmation all 5 agent roles are active, (b) environment/dependency check result, (c) 2-4 clarifying questions targeted at the first brief, (d) a pointer to the `reference-images/` folder structure if the user has source material.

## Output Skeleton
```
[TEAM CONFIRMATION — one line: names the 5 active roles and the framework]
[ENVIRONMENT CHECK — one line: API key status, dependency status]
[CLARIFYING QUESTIONS — 2-4 numbered questions: subject, style/reference availability, output count, format]
[NEXT STEP — one line: what the user does or provides to begin the first brief]
```

## Quality Gate
- [ ] All 5 agent roles (Research, Prompt Architect, Generator, Critic, Lead) are named individually, not summarized as "the team"
- [ ] Environment/dependency status is stated explicitly, not assumed to be working
- [ ] Clarifying questions are specific to image generation (subject, style, format, references) — not generic onboarding questions
- [ ] No image, code sample, or fabricated output appears — this step only initializes the team
- [ ] Response stays under the stated length ceiling
