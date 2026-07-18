# Provenance — stockton-walbeck-lead-magnets repair

Anchor → source file + location, for every claim/quote added or cited in this repair.

| Anchor (as written in genius.md) | Source file | Location |
|---|---|---|
| "genius-patterns.md's Expert Heuristics... 'Don't count opt-ins, count conversions to paid'" | `skills/stockton-walbeck-lead-magnets/references/genius-patterns.md` (pre-existing, unmodified) | Expert Heuristics section, bullet 1 |
| "extraction-report.md's Hidden Knowledge section" — 6,000 analyzed transactions | `skills/stockton-walbeck-lead-magnets/references/extraction-report.md` (pre-existing, unmodified) | "Hidden Knowledge" → "Lead magnets are better as middle-of-funnel" |
| "genius.md's 'Rule 5 Is the Only Profitability Gate'" | This file, Hidden Knowledge section (pre-existing content, unmodified — only new sections were added around it) | "### Rule 5 Is the Only Profitability Gate" |
| "2026-04-09 evolution entry... 'This is NOT segmentation...'" | This file, Hidden Knowledge section (pre-existing) | "### Buyer Identity Crystallization (Evolution: 2026-04-09)" — confirmed as auto-evolution addition via `git show 1b2a0045b` |
| "extraction-report.md's Charge-Worthy Quality Standard (Genius Pattern 4)... 'most prone to being thin'" | `skills/stockton-walbeck-lead-magnets/references/extraction-report.md` (pre-existing, unmodified) | "Genius Patterns" → "4. The 'Charge-Worthy' Quality Standard" — "Especially important when creating shortcut and starter lead magnets, which are most prone to being thin." |
| "12-8-25 packaging-frameworks video... 'theory alone is just noise'... https://www.youtube.com/watch?v=5GxB_VIgpYU" | `_archive/claude-export-2026-07-01.tar.gz` → member `claude-export/normalized/conversations/761a8d76-2c97-4b47-98fa-68abd6ba184c.md` (mirrored at `references/archive-evidence/761a8d76-2c97-4b47-98fa-68abd6ba184c.md` in this output) | Title line 4/13: "💎🧑🏽‍💻💡 12-8-25 Stockton Walbeck: How Top Creators Make Simple Ideas Feel Mind-Blowing (The Packaging Trick)"; transcript line 28: "But theory alone is just noise if you don't actually leave this video with something tactical."; transcript line 26 for URL: "Transcript for [How Top Creators Make Simple Ideas Feel Mind-Blowing (The Packaging Trick)](https://www.youtube.com/watch?v=5GxB_VIgpYU) by [Merlin AI]" |
| "$25 million" revenue figure | Same archive member as above | "...everything that we have used to sell over $25 million of our own online courses." (verbatim, near end of transcript) |
| Recognition-test sentence ("would Stockton Walbeck recognize this as his own diagnostic-to-bridge logic...") | Newly written for this repair, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 structure, grounded in this skill's own Rule 5 / Charge-Worthy Quality Standard content (not a verbatim Stockton quote — it is the required recognition-test framing, written for this expert's actual patterns per the envelope). | genius.md, "How to Use This Skill (Model Calibration)" section |

## Search trail (for the adversarial verifier)

1. `ls extractions/ | grep -i stockton` / `grep -i walbeck` → no results.
2. `grep -rli "walbeck"` across repo excluding `skills/` → only index/registry files that point back at this skill; none are a primary source.
3. Per SOURCE-SEARCH DISCIPLINE, ran a Python `tarfile` per-member content scan of `_archive/claude-export-2026-07-01.tar.gz` (confirmed 332,779,255 bytes via `wc -c`) for the regex `stockton|walbeck` case-insensitive across all 7,728 members. 5 members matched; 4 were the place-name "Stockton, California" (false positives, checked by hand with `grep -n -B2 -A2`); 1 (`761a8d76-...md`, 59,382 bytes per `wc -c`) is a genuine Stockton Walbeck YouTube transcript.
4. That transcript is a **different video** (content-packaging frameworks, not lead magnets) — used only for corroborated biographical facts and one honestly-labeled cross-video anti-pattern anchor, never presented as the source of the 4-Type Taxonomy / 5-Rule Scorecard.
5. No raw transcript for the lead-magnet video itself was recoverable anywhere. This absence is recorded in `references/source-ledger.md`, not asserted as a claim of certainty — per the envelope's rule that "a claim that sources are ABSENT is itself a provenance claim."
