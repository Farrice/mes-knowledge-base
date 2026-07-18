# Source Ledger — pj-accetturo-ai-video

Claim-by-claim provenance for every factual/attributed claim used in `SKILL.md`, `genius.md`, and the workflow files. Labels: **VERIFIED** (independently confirmable against a primary source), **LIKELY** (internally consistent, traceable to a single secondhand source, not independently corroborated), **UNCONFIRMED** (asserted somewhere in the chain but no primary source available to check it).

## Source-search discipline followed

- `extractions/` was searched for `accetturo` (case-insensitive, punctuation stripped) — no dedicated PJ Accetturo extraction file exists. `extractions/tao-prompts/extraction-report.md` covers a *different* expert (Tao Prompts) whose report explicitly notes it "compliments PJ Accetturo" rather than being sourced from him — not used as a PJ Accetturo primary source here.
- No hits under `extractions/` or `knowledge/` for "accetturo" beyond the above.
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `wc -c`) was scanned member-by-member for byte-content matches on "accetturo" (not filename matching) via `python3 tarfile`, across all 7,720 file members. Two hits:
  - `claude-export/raw/batch-0001/conversations.json` (867,859,945 bytes raw export — not read directly, superseded by the normalized file below)
  - `claude-export/normalized/conversations/6bf72208-81f6-47e9-a5a1-aa7a34b2a2d3.md` (119,243 bytes) — the actual MES 3.0 extraction session that built this skill, dated 2026-01-23. This is the ground-truth source used throughout this repair.

## Claims

| Claim | Label | Basis |
|---|---|---|
| PJ Accetturo created a David Beckham / IM8 AI video ad that generated "233M views in 3 days" | UNCONFIRMED | Appears in `SKILL.md` line 11 and the 2026-01-23 extraction transcript (Content Assessment, line 77) as a self-reported credential from the source interview/course material. No independent primary source (press coverage, platform analytics, IM8's own channel) was available to corroborate the view count. The underlying claim that PJ made an IM8/Beckham AI ad is plausible and internally consistent across all skill artifacts but the number itself is unverified. |
| PJ Accetturo created a viral Kalshi NBA Finals ad "seen during primetime" | UNCONFIRMED | Same source and same caveat as above — self-reported in the 2026-01-23 extraction transcript, Content Assessment line 77. No independent broadcast record checked. |
| The 5-role production model (Writer → Director → Cinematographer → Animator → Editor) is PJ's actual production structure | LIKELY | Named consistently in the 2026-01-23 extraction transcript (lines 204, 213, 241, 440, 560) as "Prompt 6: Production Team Orchestration." Traces to a single secondhand extraction summary of the source interview (the raw transcript text itself was not recoverable from the archive — the export only preserved the extraction assistant's narration, with source blocks collapsed to placeholder text), so it is internally consistent but not verifiable against PJ's own words directly. |
| 2x2 Grid Consistency technique for cross-shot character/environment consistency | LIKELY | Same transcript, line 244. Same caveat: extraction-summary provenance, not verbatim source text. |
| Motion Control / "Avatar technique" for performance-driven dialogue shots | LIKELY | Same transcript, line 245 ("Motion Control Performance Driving (the 'Avatar technique' for authentic dialogue shots)"). Referenced in `references/prompts-v2/prompt_07_advanced_techniques.md` scope but not directly quoted in genius.md. |
| Sacred Equity Audit / PR Risk Matrix framework ("cutting corners" vs. "scrappy innovation") | VERIFIED (in-skill) | Verbatim present in `workflows/strategic-creative-direction.md` line 31 and mirrored in `references/prompts-v2/prompt_05_brand_strategy.md`. This is skill-authored production methodology (written during the 2026-07-11 v2 refactor), not a verbatim PJ quote — "verified" here means confirmed to exist at the cited file+line, not confirmed as PJ's literal words. |
| "No invented statistic, dollar figure, or percentage appears anywhere the underlying number wasn't supplied in the input" | VERIFIED (in-skill) | Verbatim in `references/prompts-v2/prompt_05_brand_strategy.md` line 152, confirmed via direct grep against the live file. Skill-authored Quality Gate language, not a PJ quote. |
| "Silence and Breath Engineering" / minimum-2-second unscored beat rule | VERIFIED (in-skill) | Verbatim in `workflows/strategic-creative-direction.md` lines 55-56. Skill-authored, confirmed present at cited location. |
| Anti-Exemplar ("Generic AI Video Tool Listicle") and its stated flaws | VERIFIED (in-skill) | Verbatim in `genius.md` (this file), Hall of Fame Exemplars section, pre-existing content — confirmed present, not newly authored by this repair. |
| Expert-Specific Quality Rubric wording (e.g., "clunky, requiring significant manual intervention where AI could assist") | VERIFIED (in-skill) | Verbatim in `genius.md` (this file), Expert-Specific Quality Rubric table, pre-existing content — confirmed present. |

## What this means for downstream use

Treat the named production techniques (5-role model, 6-10 second chunking, 2x2 grid consistency, Sacred Equity triage) as the skill's working methodology — internally consistent and usable — but do not present the "233M views in 3 days" or Kalshi-primetime figures to a client as verified facts. If those numbers matter to a deliverable, re-verify against a primary source (IM8's own channel, a press writeup, Kalshi's own posting) before repeating them.
