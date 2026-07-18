# Source Ledger — banana-pro-director

Repair pass: Wave 3 Lane 4 Batch 2. This is a **tool skill** (a locked Higgsfield image-prompt grammar), not a person extraction — "sources" means the skill's own locked SKILL.md plus real Higgsfield platform documentation, not a personality transcript. Every claim used in `genius.md`, `workflows/*.md`, and this ledger is labeled below. File sizes recorded via `wc -c` (bytes, not lines) to verify presence/absence honestly.

## Sources consulted

| # | Source | Path | Size (bytes, `wc -c`) | Role |
|---|---|---|---|---|
| 1 | The skill's own locked grammar | `skills/banana-pro-director/SKILL.md` | 127,722 | Primary ground truth — every mode, rule, and locked prompt structure this repair cites |
| 2 | Higgsfield official blog — Nano Banana Pro prompt-engineering guide | `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md` | 5,661 | Real-world Higgsfield-authored guidance (Rus Syzdykov, Head of Prompt Engineering, Nov 21, 2025) |
| 3 | Higgsfield production-pipeline research notes | `extractions/creative-direction/higgsfield_pipeline.md` | 4,286 | Real tool ecosystem list, 9-step pipeline |
| 4 | Higgsfield platform research notes | `extractions/creative-direction/higgsfield_notes.md` | 4,297 | Tool-by-tool catalog, prompt-structure patterns from official examples |
| 5 | Higgsfield official blog — cinematic AI video prompt guide | `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md` | 5,418 | Company address, Seedream/Veo/Recast prompt examples |
| 6 | `extractions/` directory scan for a dedicated Banana Pro / Nano Banana source folder | `extractions/` (find, maxdepth 1, `-iname "*banana-pro*" -o -iname "*nano-banana*"`) | n/a — zero matches returned | Confirms no dedicated extraction exists for this specific skill; ruled out by an actual directory search, not assumed |
| 7 | Adjacent but non-source extraction (checked, ruled irrelevant) | `extractions/mark-kashef-banana-squad/extraction-report.md` | 4,212 | A different tool (Gemini 3 Pro multi-agent image pipeline), not Higgsfield Banana Pro — read and excluded as a source, noted here so the exclusion is auditable |

## Claims, labeled

| Claim | Label | Anchor |
|---|---|---|
| "Pure white seamless is now the explicit-request exception... When in doubt, default to gray." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 228 (read verbatim) |
| "Soul Cinema is a two-step process. Do not skip Step 1B.1 and jump straight to compositing." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 527 |
| "Never propose this format. It only runs when the user names it." (6-panel sheet) | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 696 |
| "That grammar is deprecated for prose composition. It made the model overcorrect and confuse spatial relationships." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 967 |
| "A 2500-character Banana Pro prompt with strong references beats a 5000-character prompt every time." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 278 |
| "The user sets aspect ratio in the Higgsfield UI directly." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 1077 |
| "Format: clean bullet points only. No quote blocks, no em-dash prose lines, no narrative wrapper." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 109 |
| "This skill does not output negative prompt blocks." | VERIFIED | `skills/banana-pro-director/SKILL.md`, line 1071 (Universal Rule 7) |
| "Nano Banana Pro represents a fundamental shift in diffusion technology. The model prioritizes comprehension and logical interpretation of the prompt." — Rus Syzdykov, Head of Prompt Engineering, Higgsfield, Nov 21, 2025 | VERIFIED | `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md`, lines 46–56; URL https://higgsfield.ai/blog/Nano-Banana-Pro-Expert-Use-Cases |
| Real Higgsfield tools: Nano Banana Pro, Nano Banana 2, Soul 2.0 / Soul Cinema / Soul Cast, Soul ID Character, GPT Image 1.5, Higgsfield Popcorn, Recast, Seedance 2.0, Kling 3.0, WAN 2.6, Cinema Studio 3.0 | VERIFIED | `extractions/creative-direction/higgsfield_notes.md`, lines 9–48; `higgsfield_pipeline.md`, lines 5–44 |
| Higgsfield Popcorn "locks tone and composition" | VERIFIED | `extractions/creative-direction/higgsfield_notes.md`, line 51; `higgsfield_pipeline.md`, line 63 |
| Recast "swaps characters while preserving motion, lighting, atmosphere" | VERIFIED | `extractions/creative-direction/higgsfield_notes.md`, line 25 |
| Higgsfield HQ: 535 Mission St, 14th floor, San Francisco, CA, 94105 | VERIFIED | `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md`, line 117 |
| SKILL.md's "GPT-2" tool-fork option corresponds to Higgsfield's real "GPT Image 1.5" product | UNCONFIRMED | No source lists a Higgsfield product literally named "GPT-2." Closest confirmed real product is "GPT Image 1.5" (`extractions/creative-direction/higgsfield_notes.md`, line 16; `higgsfield_pipeline.md`, line 16). Whether "GPT-2" is intentional internal shorthand in this skill or an unverified label was not resolved by this repair pass — flagged in `genius.md` "Tool Facts (Grounding)," not silently corrected (out of scope: SKILL.md content is untouched, additive-first). |
| A dedicated `extractions/` source folder exists for "Banana Pro Director" or "Nano Banana Pro" as a named person/expert extraction | UNCONFIRMED — verified absent | Directory search returned zero matches (see row 6 above); this is a checked absence, not an assumed one |
| This skill (`banana-pro-director`) is itself sourced from an official Higgsfield internal document (as opposed to being an internally authored locked grammar cross-checked against public Higgsfield material) | UNCONFIRMED | No such internal Higgsfield document exists in `extractions/` or `references/`; SKILL.md reads as originally authored prompt-engineering IP, not a copy of an official Higgsfield artifact — treated as such throughout `genius.md` |

## What this ledger does NOT claim

This skill's locked prompt grammar (the flat-grade physics, the mode-gating order, the cinema-prose register, the 3-panel-over-6-panel default) is **not** asserted to be verbatim Higgsfield product documentation — it is this repo's own prompt-engineering system for driving Higgsfield's tools, cross-checked against real Higgsfield tool names and one real Higgsfield-authored prompt guide where overlap exists. Anywhere this ledger cites SKILL.md as the anchor, the claim is "this is what the skill's own locked rule says," not "this is what Higgsfield officially mandates."
