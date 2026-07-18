# PROVENANCE — nick-saraev-bottleneck-thinking repair (Wave 3 Lane 4 Batch 12)

Anchor → source table for every claim added or re-labeled in this repair. Full claim-by-claim ledger with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.

| Anchor (in repaired genius.md) | Source file + location | Verification method |
|---|---|---|
| Model Calibration section — "$10K, $25K, $72K/mo," "8-10 doors/hour" | `extractions/nick-saraev-bottleneck-thinking/transcript.txt` | Direct read of the full 13,589-byte transcript; figures cross-checked verbatim against the file |
| Core Thesis quote — "the fluid inside of the pipeline... narrowest part" | `transcript.txt` | Exact-string match confirmed by reading the full file |
| Pipeline Visualization — "inquiry received, proposal sent, invoice paid" | `transcript.txt` | Exact-string match confirmed by reading the full file |
| Business Improvement Flywheel — "Identify, widen, um, look for new ones, repeat" | `transcript.txt` | Exact-string match confirmed by reading the full file |
| Oscillation Pattern — "30k a month" swap point | `transcript.txt` | Exact-string match confirmed by reading the full file |
| Anti-Pattern 1 — "it doesn't matter how fast your sales step is..." | `transcript.txt` | Exact-string match |
| Anti-Pattern 2 — "you are wasting time, energy, and resources" | `transcript.txt` | Exact-string match |
| Anti-Pattern 3 — "I could just knock on doors faster..." | `transcript.txt` | Exact-string match |
| Anti-Pattern 4 — "you can point to exactly ONE constraint at any given time..." | `extractions/nick-saraev-bottleneck-thinking/extraction-report.md`, Genius Pattern 2 success metric | Exact-string match, full 8,773-byte file read |
| Anti-Pattern 5 — "Most people panic when a previously-fixed area breaks again" | `extraction-report.md`, Hidden Knowledge #2 | Exact-string match; labeled LIKELY (extraction's own characterization, not a Nick quote) |
| Anti-Pattern 6 — "Some are load-bearing walls..." | `extraction-report.md`, Hidden Knowledge #3 | Exact-string match; labeled LIKELY |
| Book identification — *The Goal* / Eliyahu Goldratt | `extraction-report.md` (2 mentions) vs. `transcript.txt` (0 mentions) | `grep -c "Goldratt\|The Goal"` run against both files; confirmed the attribution is the extraction's research, not a Nick quote — re-labeled LIKELY in `genius.md` and the ledger |
| "10x shorter" feedback-cycle claim | Not found in `transcript.txt` or `extraction-report.md` | Removed the invented multiplier from the Hidden Knowledge section; retained the verified underlying mechanic ("months to a few days") |
| Hall of Fame Exemplars (3 scenarios) | Checked `transcript.txt` and `extraction-report.md` for "A/B," "button colors," "course creator," "$7K," "Optimization Treadmill" | `grep -c` → 0 matches in both files; confirmed synthesized, not transcript-sourced — added an explicit UNCONFIRMED banner above the section rather than deleting it |
| "Patterns from claude.ai export" section (Driver Trees / Three Equations / Pyramid Principle / FAST) | Checked all 5 `extractions/*saraev*` paths for "driver tree," "Leftclick," "pyramid principle," "first principles," "triangulate" | `grep -c` → 0 matches everywhere in the live extraction tree; likely source is the un-extracted `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via `ls -la`) — not opened this session; added an inline provenance-gap note in `genius.md` rather than deleting the content |
| `extractions/nick-saraev/transcript.txt`, `Nick Saraev/transcript.txt`, `nick-saraev-outreach/transcript.txt`, `nick-saraev-cold-outreach/transcript.txt` ruled OUT as sources for the consulting-frameworks section | `wc -c` = 276,999 bytes each (identical cold-outreach copywriting course, different domain) | Read + grepped directly; not assumed absent |

No quote in this repair was written without first being located verbatim in the cited source file via direct read or `grep`. No claim was labeled UNCONFIRMED without a search command being run first (commands recorded in the Absence Check section of `references/source-ledger.md`).
