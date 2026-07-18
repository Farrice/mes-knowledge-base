# PROVENANCE — andy-lo-premium-websites repair

Anchor → source file + location. All source-text checks done with real file
reads and `grep -n` (not assumed); sizes recorded with `wc -c` per envelope
rule 2.

| # | Anchor text added | Source file | Location | Verified how |
|---|---|---|---|---|
| 1 | "first frame" / "last frame" | extractions/andy-lo/extraction-report.md | line 31 | `grep -n "first frame"` |
| 2 | "Frames to Video" | extractions/andy-lo/extraction-report.md | line 139 | `grep -n "Frames to Video"` |
| 3 | "$5K-$15K per site" | extractions/andy-lo/extraction-report.md | line 185 | `grep -n "\$5K"` |
| 4 | "$20K" | extractions/andy-lo/extraction-report.md | line 197 | `grep -n "\$20K"` |
| 5 | Level 3 Option B = 11 steps | extractions/andy-lo/extraction-report.md | lines 159-171 | direct Read, manually counted 11 numbered steps |
| 6 | "just drag and drop" | extractions/andy-lo/extraction-report.md | line 114 | `grep -n "just drag and drop"` |
| 7 | "24-Hour Quickstart" | extractions/andy-lo/extraction-report.md | line 209 | `grep -n "24-Hour Quickstart"` |
| 8 | "6,375 total words" / 3 videos | extractions/andy-lo/extraction-report.md | line 6 | `grep -n "6,375 total words"` |
| 9 | "nice to have" | extractions/andy-lo/extraction-report.md | line 117 | `grep -n "nice to have"` |
| 10 | "connect to content generation agents for CMS publishing" | extractions/andy-lo/extraction-report.md | line 224 | `grep -n "connect to content generation"` |
| 11 | Anti-Pattern items 1-6 | extractions/andy-lo/extraction-report.md | Genius Patterns 2/3/4/7/11 (lines 30-45, 84-88), Hidden Knowledge #2 (lines 101-102) | direct Read of each section; anti-patterns are inversions of documented patterns, not Andy Lo quotes — labeled as such in genius.md intro line |
| 12 | Extraction file exists / size | extractions/andy-lo/ | whole dir | `find extractions/andy-lo -type f -exec wc -c {} \;` → extraction-report.md = 19,714 bytes. No other file in that directory (confirmed via `find -type f`) — no second source to omit or misclaim as absent |

## Absence claims — verified, not assumed

- No `references/*ledger*` or `*source*` file existed in
  `skills/andy-lo-premium-websites/references/` prior to this repair —
  confirmed via `find skills/andy-lo-premium-websites -type f | sort`
  (full listing captured, no ledger/source file present).
- No `## Anti-Patterns` heading existed anywhere in `skills/andy-lo-premium-websites/genius.md`
  prior to this repair, despite 5 workflow files referencing
  "genius.md § Anti-Patterns" — confirmed via
  `grep -rin "anti-pattern" skills/andy-lo-premium-websites/`, which returned
  only the 5 workflow cross-references and zero hits inside genius.md itself.
- No recognition-test language existed in SKILL.md or genius.md prior to
  this repair — confirmed via the same grep pass (`recognition` search hit
  nothing).
- `extractions/andy-lo/` contains exactly one file
  (`extraction-report.md`, 19,714 bytes) — not a 0-byte or missing source;
  confirmed by direct `find`/`wc -c`, not inferred.
