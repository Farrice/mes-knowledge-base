# Source Ledger — paul-james-ai-automation

> Claim-by-claim provenance for `genius.md`. Labels: **VERIFIED** (verbatim
> quote confirmed in a primary source file, checked directly this session),
> **LIKELY** (consistent with verified material, not itself a direct quote),
> **UNCONFIRMED** (no source file contains it — treat as illustrative only,
> never as a citable Paul James claim).

## Primary sources recovered (2026-07-18)

Prior versions of this skill (SKILL.md, genius.md, the `references/`
prompt files) contained no pointer to raw source material — no
`extractions/paul-james*` file exists in this repo (`ls extractions/ |
grep -i paul` returns nothing). Before labeling anything UNCONFIRMED, a
full-repo phrase search for `"paul james"` (exact phrase, not fragments —
this is a common two-word name) was run, followed by a `tarfile`
per-member content scan of `_archive/claude-export-2026-07-01.tar.gz`
(7,728 members total). That scan found 9 real conversation exports
containing full verbatim YouTube transcripts of Paul James's own videos,
transcribed by a third-party service ("Merlin AI"). These are now the
grounding source for this skill.

| # | File (within tar) | Size (bytes) | Video title | YouTube URL | Harvested date |
|---|---|---|---|---|---|
| 1 | `claude-export/normalized/conversations/bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 | Google Gemini's NEW Super Gems DESTROYS $99/Month Automation Tools | https://www.youtube.com/watch?v=9RdGqmSiuyo | 2026-01-18 |
| 2 | `claude-export/normalized/conversations/dff61093-dba0-42b7-870f-c40ad8d3f960.md` | 50,993 | Google's NotebookLM Just KILLED $500/Hour Client Research | https://www.youtube.com/watch?v=MflmRBjM0O4 | 2026-01-09 |
| 3 | `claude-export/normalized/conversations/8140bf9c-38e7-4163-9ccb-b874dd05253d.md` | 23,491 | Google Gems is CRUSHING $300B Industry | https://www.youtube.com/watch?v=zAvsQZZcIg0 | 2026-01-06 |
| 4 | `claude-export/normalized/conversations/c91bc731-4c99-4dd6-b7b1-568e77366977.md` | 51,147 | Gemini 3 Pro Just ENDED Four $100+ Subscriptions | https://www.youtube.com/watch?v=I_W-9gAfCHc | 2026-01-09 |
| 5 | `claude-export/normalized/conversations/1fe0e0e6-7322-44ae-9067-9a2cb3b509af.md` | 22,944 | (Expert roster listing, mentions Paul James as #20: "AI automation consulting") | n/a — index doc, not a transcript | 2026-01-xx |
| 6 | `claude-export/normalized/conversations/69a61fba-8731-4f0b-a61e-d6f9912bff67.md` | 36,592 | Google Gems KILLED $297/Month Lead Gen Tools | https://www.youtube.com/watch?v=YMKIcOWAVrY | 2026-01-04 |
| 7 | `claude-export/normalized/conversations/e179348e-c858-41c9-9932-53fe6db684cd.md` | 37,322 | This Perplexity Feature is CRUSHING How Agencies Charge | https://www.youtube.com/watch?v=gRGULoe9WiI | 2026-01-05 |
| 8 | `claude-export/normalized/conversations/cf0de5e7-a663-484a-8656-4ccfbaa5f600.md` | 23,781 | Google NotebookLM + Gems ENDED $1,500/Month Consulting | https://www.youtube.com/watch?v=gQmzZ3LfR38 | 2026-01-20 |
| 9 | `claude-export/normalized/conversations/8e8f2bd7-132e-4b1a-9760-7a2a638b90eb.md` | 70,836 | Perplexity + Google NotebookLM ENDED $2,000 Market Research | https://www.youtube.com/watch?v=umc4vXfE1xY | 2026-01-21 |

All 9 files confirmed non-empty by direct read (sizes above are exact,
recorded via `tarfile.getmembers()`, not estimated). File #5 is a routing
index (agent roster list), not a transcript — kept in the count because it
independently corroborates Paul James's domain ("AI automation consulting")
but contributes no quotable content.

## Claim-by-claim labels

| Section in genius.md | Label | Basis |
|---|---|---|
| Pattern 1 (Zero-Cost Positioning Flip) | **VERIFIED** | Direct quote, source #1, 2026-01-18 |
| Pattern 2 (Modular Service Framework) | **LIKELY** | "Puzzle pieces"/"checkpoints" language appears in source #1's fuller transcript ("Picture nodes like checkpoints in a process") but the pattern's generic phrasing predates this repair's anchor pass — not independently re-anchored this session |
| Pattern 3 (Specificity Revenue Multiplier) | **LIKELY** | Consistent with source #1's "The secret is avoiding generic solutions"; not directly re-anchored |
| Pattern 4 (Time-Recovery Value Proposition) | **LIKELY** | "Give a business owner back five hours weekly" is a close paraphrase of source #1: "When you give a business owner back five hours weekly... they happily pay monthly" |
| Pattern 5 (Zero-Marginal-Cost Scaling) | **LIKELY** | Consistent with all 9 sources' "free infrastructure" framing; no single verbatim anchor found |
| Pattern 6 (URL Lead Magnet Strategy) | **VERIFIED** | Direct quote, source #1, 2026-01-18 |
| Pattern 7 (Agency Arbitrage Positioning) | **LIKELY** | Consistent with source #1 ("agencies bill clients thousands... your margins are enormous") |
| Pattern 8 (Service Layering Dependency Model) | **VERIFIED** | Direct quote, source #1, 2026-01-18 |
| Pattern 9 (White-Label Revenue Architecture) | **LIKELY** | Consistent with source #1 white-labeling passage; no exact-match short quote found |
| Pattern 10 (Expertise Timing Advantage) | **VERIFIED** | Direct quote, source #1, 2026-01-18 |
| Pattern 11 (Vulnerability-to-Authority Bridge) | **VERIFIED** | Direct quote, source #1, 2026-01-18; corroborated near-verbatim in sources #2, #3, #4, #6 (all open with a "brother's garage" beat) |
| Pattern 12 (Multimodal Expansion Vision) | **LIKELY** | Consistent with source #1's multimodal passage (photographer/video producer examples) |
| Pattern 13 (Iterative Enhancement Architecture) | **LIKELY** | Consistent with source #1 ("checkpoint-based design... your clients never see behind the scenes") |
| Pattern 14 (30-Day Transformation Frame) | **LIKELY** | Consistent with source #1's "Imagine what your next 30 days look like" close |
| Hidden Knowledge 1–5 | **VERIFIED** (anchor lines added) | Direct quotes, source #1, 2026-01-18 |
| Anti-Patterns (all 7 items) | **VERIFIED** | Direct quotes, sources #9, #7, #1, #8, #6, #4, plus this skill's own pre-existing Anti-Exemplar text |
| Hall of Fame Exemplars 1 & 2 ("Agency Slayer," "PropertyWriter.ai"/"AgentFlow AI") | **UNCONFIRMED as real events** | Searched all 9 sources for "Agency Slayer," "$249/month," "PropertyWriter," "AgentFlow" — zero hits. These are illustrative compositions built from the verified patterns, not direct Paul James claims. Flagged inline in genius.md with a provenance note. |
| Signature Move "No-GoHighLevel Disclaimer" (new, added this session) | **VERIFIED** | Appears near-verbatim in all 9 sources — the single most-repeated line in the corpus |
| Quality Rubric anchor ($300–$500/report) | **VERIFIED** | Direct quote, source #9, 2026-01-21 |

## Pre-existing reference files (unchanged this session)

`references/genius-patterns.md` and `references/hidden-knowledge.md` are
verbatim duplicates of the corresponding genius.md sections (confirmed via
diff), split out for token efficiency at an earlier date. They carry the
same labels as their genius.md counterparts above and were not
independently re-verified. `references/quality-rubric.md` and
`references/implementation.md` are pre-existing and out of scope for this
repair (no failing check touches them).
