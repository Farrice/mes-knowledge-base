# Provenance — banana-pro-director repair

Anchor → source file + location, for everything added in `genius.md`, `references/source-ledger.md`, and `workflows/*.md`.

| Anchor / claim | Source file | Location |
|---|---|---|
| "Pure white seamless is now the explicit-request exception... default to gray" | `skills/banana-pro-director/SKILL.md` | line 228 |
| "Soul Cinema is a two-step process. Do not skip Step 1B.1..." | `skills/banana-pro-director/SKILL.md` | line 527 |
| "Never propose this format. It only runs when the user names it." (6-panel) | `skills/banana-pro-director/SKILL.md` | line 696 |
| "That grammar is deprecated for prose composition..." (X/Y coordinates) | `skills/banana-pro-director/SKILL.md` | line 967 |
| "A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time." | `skills/banana-pro-director/SKILL.md` | line 278 |
| "The user sets aspect ratio in the Higgsfield UI directly." | `skills/banana-pro-director/SKILL.md` | line 1077 (Universal Rule 13) |
| "Format: clean bullet points only. No quote blocks..." | `skills/banana-pro-director/SKILL.md` | line 109 |
| "This skill does not output negative prompt blocks." | `skills/banana-pro-director/SKILL.md` | line 1071 (Universal Rule 7) |
| "The flattering-realism ceiling (LOCKED...)" blockquote | `skills/banana-pro-director/SKILL.md` | line 143 |
| Mode 3 cinema-prose example ("A cinematic anamorphic still photograph...") blockquote | `skills/banana-pro-director/SKILL.md` | line 897 |
| "Nano Banana Pro represents a fundamental shift in diffusion technology..." — Rus Syzdykov | `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md` | lines 46–56 |
| Author credit: Rus Syzdykov, Head of Prompt Engineering, Higgsfield, Nov 21, 2025 | `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md` | lines 46–54 |
| Tool list: Nano Banana Pro/2, Soul 2.0/Cinema/Cast, Soul ID Character, GPT Image 1.5, Higgsfield Popcorn, Recast, Seedance 2.0, Kling 3.0, WAN 2.6, Cinema Studio 3.0 | `extractions/creative-direction/higgsfield_notes.md` | lines 9–48 |
| Same tool list, cross-check | `extractions/creative-direction/higgsfield_pipeline.md` | lines 5–44 |
| Higgsfield Popcorn "locks tone and composition" | `extractions/creative-direction/higgsfield_notes.md` | line 51 |
| Recast "swaps characters while preserving motion, lighting, atmosphere" | `extractions/creative-direction/higgsfield_notes.md` | line 25 |
| Higgsfield HQ address, 535 Mission St, San Francisco | `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md` | line 117 |
| "GPT-2" naming gap (SKILL.md uses "GPT-2"; no source confirms that literal product name — closest is "GPT Image 1.5") | `skills/banana-pro-director/SKILL.md` lines 350, 390 vs. `extractions/creative-direction/higgsfield_notes.md` line 16 | UNCONFIRMED — flagged, not resolved (out of scope, additive-only) |
| No dedicated Banana Pro / Nano Banana extraction folder exists | `extractions/` directory search | `find extractions -maxdepth 1 -iname "*banana-pro*" -o -iname "*nano-banana*"` → zero results (run 2026-07-17, this session) |
| `mark-kashef-banana-squad` extraction is a different tool (Gemini 3 Pro multi-agent pipeline), not a source for this skill | `extractions/mark-kashef-banana-squad/extraction-report.md` | 4,212 bytes, read in full and excluded |

All file sizes for absence/presence claims recorded via `wc -c` (bytes) — see `references/source-ledger.md` table for the full byte-count log.
