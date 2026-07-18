# PROVENANCE — higgsfield-creative-studio repair

Anchor → source file + location. Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED table lives in
`references/source-ledger.md`; this is the compact anchor index the ENVELOPE asks for.

| Anchor used in genius.md / workflows | Source file | Location |
|---|---|---|
| "Use the orchestrator for routing and stacking, but let `gpt-image-2-director` and `marketing-studio-director` control their own final prompt formats." | `skills/higgsfield-creative-studio/references/genius-patterns.md` | line 4 |
| "Do not add the package wrapper when the user asked only for a single GPT Image 2.0 prompt or a single Marketing Studio prompt..." | `skills/higgsfield-creative-studio/SKILL.md` | line 78 |
| "Every real Higgsfield generation must pass through `execution/higgsfield_budget_guard.py check`..." | `directives/higgsfield-usage-policy.md` | "Hard Rule" section |
| "Disambiguation: Higgsfield GPT-2 ... ≠ OpenAI GPT Image 2..." | `skills/higgsfield-creative-studio/SKILL.md` | line 38 |
| "The still image and video prompt should share one strategy spine." / "The orchestrator can accidentally break source-skill output formats by over-explaining." | `skills/higgsfield-creative-studio/references/hidden-knowledge.md` | lines 4, 6-7 |
| "Nano Banana Pro represents a fundamental shift in diffusion technology..." — Rus Syzdykov, Nov 21, 2025 | `extractions/creative-direction/higgsfield.ai_blog_Nano-Banana-Pro-Expert-Use-Cases.md` | lines 46-56 |
| "Unlike generic trend tools, it provides creative structure rather than imitation..." — byline "Mariam Barova," Nov 26, 2025 | `extractions/creative-direction/higgsfield.ai_blog_Best-Ways-to-Organize-Your-Workflow-on-Higgsfield-AI.md` | lines 48-52, 96 |
| "Your scene comes together when each tool does one job well..." | `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md` | lines 25-27 |
| Real tool catalog (Nano Banana Pro/2, Soul 2.0/Cinema/Cast, Soul ID, GPT Image 1.5, Popcorn, Recast, Seedance 2.0, Kling 3.0, WAN 2.6, Cinema Studio 3.0, Sora 2/Max, Veo 3.1) | `extractions/creative-direction/higgsfield_notes.md`; `higgsfield_pipeline.md` | notes.md lines 9-48; pipeline.md lines 5-44 |
| Higgsfield HQ address | `extractions/creative-direction/higgsfield.ai_blog_Prompt-Guide-to-Cinematic-AI-Videos.md` | line 117 |
| Credit Guard numbers (3%/8%/15%/2-failure circuit/1 retry/1,200 credits) | `directives/higgsfield-usage-policy.md` | "Current Baseline" + "Balanced Defaults" sections |
| Byline spelling gap (Mariam Barova vs. Mairam Bairova) | `extractions/creative-direction/higgsfield.ai_blog_Best-Ways-to-Organize-Your-Workflow-on-Higgsfield-AI.md` | line 48 vs. lines 125/129/133 |
| Workflow Output Schema/Quality Gate content | `skills/higgsfield-creative-studio/references/prompts-v2/combined-asset-package.md`; `guarded-generation-request.md` | full files (read, not altered — new `workflows/*.md` wraps them without changing their locked protocol) |
| "GPT-2" naming gap (UNCONFIRMED, inherited, not introduced) | `extractions/creative-direction/higgsfield_notes.md`; `higgsfield_pipeline.md` | notes.md line 16; pipeline.md line 16 — cross-checked against `skills/banana-pro-director/genius.md`'s independent documentation of the same gap |

All byte sizes verified with `wc -c` (recorded in `references/source-ledger.md`). Negative-result
claim (no dedicated `higgsfield-creative-studio` extraction folder) verified by actual `find`/`ls`
directory search, not assumed — commands and zero-match results logged in the ledger.
