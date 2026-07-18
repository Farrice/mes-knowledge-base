# PROVENANCE — ethan-smith-aeo repair

Source root: `extractions/ethan-smith/` — VERIFIED present, non-thin.
- `ethan-smith-aeo-extraction-report.md` — 23,554 bytes (`wc -c`)
- `transcript.txt` — 78,468 bytes (`wc -c`)
Report header (line 6): "Source: Podcast interview (Lenny's Podcast), ~60 min, 14,438 words."
No need to fall back to codex-harvest or claude-export tarball — primary extraction source is present and sufficient for all anchors below.

| Anchor added to | Claim | Source location | Quote (verbatim) |
|---|---|---|---|
| Anti-Pattern: Manipulation with a half-life | Platform-applause test | `extractions/ethan-smith/ethan-smith-aeo-extraction-report.md` line 47 | "If someone at [platform] saw what I'm doing, would they applaud or would they build an algorithm to stop me?" |
| Anti-Pattern: Single-rank optimization | Citation frequency > rank | same file, line 34 | "In Google, position #1 wins. In LLMs, *frequency of citation* across the summary wins — the answer mentioned most often across sources becomes the top recommendation." |
| Anti-Pattern: Derivative content | Information gain / typicality | same file, line 82 | Ethan identifies "information gain" as the fundamental quality signal... combined with "typicality" detection — if your content is too similar to what already exists, it gets flagged as derivative. |
| Anti-Pattern: Single-surface blindness | ChatGPT/Perplexity overlap % | same file, line 76 | "ChatGPT citations overlap only 35% with Google results; Perplexity overlaps 70%." |
| Anti-Pattern: Referral-click measurement | Hidden attribution | same file, line 94 | "users don't click citations — they copy the brand name, open a new tab, type it into Google or directly navigate to the site. This shows up as 'branded Google search' or 'direct traffic,' completely masking the LLM's role." |
| Anti-Pattern: Broad-keyword-only coverage | Longtail resurrection | same file, line 52 | "25 words per query vs. 6 in Google. The tail is massive again." |
| Anti-Pattern: Generic corporate voice | Reddit Authenticity Protocol | same file, line 64 | winning strategy is "embarrassingly simple: be a real person, say who you are and where you work, and give useful information." |
| Calibration section: "sells fear" distancing | What makes Ethan different | same file, line 19 | "most AEO voices are selling fear ('SEO is dead') or selling tools" |
| Calibration section: distrust of "too clean" claims | 2007 antibody origin | same file, line 46 | "His 2007 experience of watching entire categories of spam sites get wiped out by algorithm updates created permanent antibodies against short-term manipulation." |

The 4 anti-pattern items already source-attributed pre-repair (The 2018 "Ultimate Guide" play; Inauthentic community presence; Anecdote-driven strategy; Flat lead weighting) were left untouched — passing content, no rewrite per additive-first rule.

Recognition-test language: added inside the new "How to Use This Skill (Model Calibration)" section, genius.md — modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per envelope instruction, written fresh against Ethan Smith's actual texture (scientific rigor, historian's pattern-matching, anti-hype), not copied.
