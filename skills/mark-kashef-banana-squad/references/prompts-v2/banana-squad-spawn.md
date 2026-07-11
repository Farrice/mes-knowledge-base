---
name: "Banana Squad Spawn"
source_prompt: "skills/mark-kashef-banana-squad/references/prompts/banana-squad-spawn.md"
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

## Execution Protocol
1. Paste spawn prompt → Team initializes
2. Tell Lead what you need → Lead asks clarifying questions
3. (Optional) Drop reference images in `reference-images/` folders
4. Research Agent analyzes references → extracts visual DNA
5. Prompt Architect creates 5 narrative prompts
6. Generator Agent creates images via Gemini API → saves to `outputs/`
7. Critic Agent scores and ranks → Lead presents top results
8. Iterate conversationally until satisfied

## Output Contract
A completed spawn session delivers:
- Confirmation that the 4-agent team (Lead, Research, Prompt Architect, Generator+Critic loop) is live and configured against the Key Configuration table
- If references were supplied: one visual DNA report (style / composition / color / lighting / mood)
- Exactly 5 narrative prompt variations per brief from the Prompt Architect
- One or more generated image files per accepted prompt, saved to `outputs/`
- One Critic scorecard per generated image, with a PASS/ITERATE/REJECT verdict against the configured threshold
- A ranked shortlist (top results only) presented back to the user for the next iteration or sign-off

## Output Skeleton
```
TEAM STATUS: [initialized / awaiting brief / mid-session]
CONFIG IN USE: [prompt variations count] / [max reference images] / [critic threshold] / [output format]

VISUAL DNA REPORT: [present / not applicable — no references supplied]

PROMPT VARIATIONS (5):
  1. [one-line description of creative direction]
  2. [one-line description of creative direction]
  3. [one-line description of creative direction]
  4. [one-line description of creative direction]
  5. [one-line description of creative direction]

GENERATED IMAGES:
  [filename] — CRITIC VERDICT: [PASS / ITERATE / REJECT] — [weighted score]/10

TOP RESULTS PRESENTED: [count] of [total generated]
NEXT STEP: [awaiting user iteration note / session complete]
```

## Quality Gate
- [ ] Team confirms all 4 roles (Lead, Research, Prompt Architect, Generator/Critic) are active before any generation begins
- [ ] If reference images were provided, a visual DNA report exists before the Prompt Architect runs
- [ ] Exactly 5 prompt variations are produced per brief — no fewer, no silent collapsing to one
- [ ] Every generated image carries a Critic verdict before being shown to the user
- [ ] Only images meeting the configured threshold are surfaced as "top results"
- [ ] Output files are saved to `outputs/` in the configured format
