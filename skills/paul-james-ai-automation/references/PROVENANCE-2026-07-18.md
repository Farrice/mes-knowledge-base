# Provenance — paul-james-ai-automation repair

Anchor → source file + location. All primary sources live inside
`_archive/claude-export-2026-07-01.tar.gz` (repo root), extracted via
Python `tarfile` this session (full member scan, 7,728 members, filtered
to `.md/.txt/.json/.jsonl` under 5MB, content-matched on the exact phrase
"paul james", case-insensitive). Sizes below are `TarInfo.size` in bytes,
recorded directly — not estimated.

| Anchor used in genius.md | Source file (in tar) | Size | Video / Section | Date |
|---|---|---|---|---|
| Pattern 1 anchor ("$50 to $99 per month") | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Pattern 6 anchor ("URL... lead generation magnets") | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Pattern 8 anchor ("real estate agent... email follow-up") | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Pattern 10 anchor ("Starting early means...") | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Pattern 11 anchor ("brother's garage") | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Hidden Knowledge 1–5 anchors | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Anti-Pattern: "Raw-output dumping" ("Do not do that") | `.../8e8f2bd7-132e-4b1a-9760-7a2a638b90eb.md` | 70,836 B | Perplexity + NotebookLM ($2,000 Market Research) | 2026-01-21 |
| Anti-Pattern: "Single-mode tool usage" ("Ferrari... first gear") | `.../e179348e-c858-41c9-9932-53fe6db684cd.md` | 37,322 B | This Perplexity Feature is CRUSHING How Agencies Charge | 2026-01-05 |
| Anti-Pattern: "One-and-done tool building" | `.../bd8baba4-9ef9-4cf2-96e2-8131ba2a5164.md` | 47,234 B | Super Gems | 2026-01-18 |
| Anti-Pattern: "Non-compounding delivery" | `.../cf0de5e7-a663-484a-8656-4ccfbaa5f600.md` | 23,781 B | NotebookLM + Gems ($1,500/Month Consulting) | 2026-01-20 |
| Anti-Pattern: "Unqualified call-taking" ("$75 budget") | `.../69a61fba-8731-4f0b-a61e-d6f9912bff67.md` | 36,592 B | Google Gems KILLED $297/Month Lead Gen Tools | 2026-01-04 |
| Anti-Pattern: "Subscription stacking" ("$481 every single month") | `.../c91bc731-4c99-4dd6-b7b1-568e77366977.md` | 51,147 B | Gemini 3 Pro Just ENDED Four $100+ Subscriptions | 2026-01-09 |
| Anti-Pattern: "Generic AI-consultant pitch" | `skills/paul-james-ai-automation/genius.md` (this repo, pre-existing Anti-Exemplar section, lines ~172–180) | n/a | Existing skill content | pre-dates this repair |
| Quality Rubric anchor ("$300 to $500 per report") | `.../8e8f2bd7-132e-4b1a-9760-7a2a638b90eb.md` | 70,836 B | Perplexity + NotebookLM ($2,000 Market Research) | 2026-01-21 |
| Signature Move "No-GoHighLevel Disclaimer" | All 9 files listed in `references/source-ledger.md` | — | Recurring line, near-verbatim in every source | 2026-01-04 to 2026-01-21 |
| Hall of Fame Exemplars 1 & 2 | Searched all 9 files above for "Agency Slayer," "$249/month," "PropertyWriter," "AgentFlow" — **zero matches**. | — | Not found — labeled UNCONFIRMED-as-real-event in source-ledger.md and flagged inline in genius.md | n/a |

## Search method (per ENVELOPE Rule 2 — false-absence claims are a
provenance failure in themselves)

1. `ls extractions/ | grep -i paul` — no match.
2. Repo-wide `grep -rIl "paul james"` (exact phrase, case-insensitive,
   excluding worktrees/skill dir) — surfaced only routing/index files
   (`SKILL_INDEX.md`, `DOMAIN_REGISTRY.md`, `agents/paul-james/AGENT.md`)
   and `agents/paul-james/memory/context.md` — none contained transcript
   material.
3. `find . -iname "*.tar*" -o -iname "*.zip"` — found
   `_archive/claude-export-2026-07-01.tar.gz` (7,728 members).
4. `tarfile.getmembers()` filename scan for "paul"+"james" — 0 hits (the
   real hits were inside conversation *content*, not filenames).
5. `tarfile` per-member **content** scan (decode + lowercase phrase match)
   across all `.md/.txt/.json/.jsonl` members under 5MB — 9 hits, listed
   above. This is the step that recovered real primary sources; skipping
   it would have produced a false "no source exists" conclusion.
