# PROVENANCE — coaching-business-os repair

Anchor → source file + location, for every quote/claim added or newly labeled in this repair pass. All quotes below were confirmed verbatim against the cited in-repo file before use (not invented, not paraphrased into a quote).

| Anchor (as it appears in new genius.md sections) | Source file | Location | Verbatim confirmed |
|---|---|---|---|
| "Ads guarantee visibility, NOT conversions" | `skills/coaching-business-os/references/field-guide.md` | line 48, Predictable Prospecting bullet | Yes — read in full before use |
| "lose their shirt very quickly" | `skills/coaching-business-os/references/field-guide.md` | line 53, Preconditions paragraph | Yes |
| "$2,500 mentorship, $99 content mastery, $99 PT kit" | `skills/coaching-business-os/references/field-guide.md` | line 30, Work Backwards bullet (also `genius.md` original line 8, Revenue-Backwards pattern) | Yes |
| "converts ~1 in 100" | `skills/coaching-business-os/references/field-guide.md` | line 31, Indirect Beats Direct bullet (also `genius.md` original line 13) | Yes |
| "not teach to teach" | `skills/coaching-business-os/references/field-guide.md` | line 49, Teach to Sell bullet (also `genius.md` original line 23) | Yes |
| "multiple seven figures... ONE pipeline... no social channels" | `skills/coaching-business-os/references/field-guide.md` | line 55, Structural Facts paragraph (also `genius.md` original line 34) | Yes |
| "accumulated expertise becomes unfindable" | `skills/coaching-business-os/references/field-guide.md` | line 11, Jonathan Mast section opening | Yes |
| "if you're charging five, seven, even $10K... you're still undercharging" | `skills/coaching-business-os/genius.md` (original) | line 60, Hidden Knowledge — High-Ticket Pricing insight | Yes |
| Source dates (Aug 2025 Smith, May 2025 Elkaim, Dec 2025 Mast) | `skills/coaching-business-os/references/field-guide.md` | lines 9, 26, 44 (each section's "Source:" line) | Yes |
| `_archive/claude-export-2026-07-01.tar.gz` exists, 332,779,255 bytes | Direct filesystem check | `ls -la _archive/claude-export-2026-07-01.tar.gz`, run 2026-07-17 | Yes — command output recorded |
| No `extractions/` file matches Smith/Elkaim/Mast/Healthpreneur | Direct filesystem check | `ls extractions/ | grep -i -E "smith|elkaim|mast|healthpreneur"` → empty; `ls extractions/ | wc -l` → 193, run 2026-07-17 | Yes — command output recorded |
| 7 routed lane directories exist (Welch, Hiette, Novotny, Elkaim, Kotler, Eyal, Manson) | Direct filesystem check | `find`/`test -d` against each `skills/<name>/` path, run 2026-07-17 | Yes — all 7 confirmed present |
| `skills/greg-hickman/` does not exist; actual dir is `skills/greg-hickman-service-scaling/` | Direct filesystem check | `ls skills/ | grep -i "greg-hickman"`, run 2026-07-17 | Yes — flagged in source-ledger.md, SKILL.md left untouched (out of scope) |

## What was NOT independently re-verified

- The raw text of the three source talks (Smith Aug 2025, Elkaim May 2025, Mast Dec 2025) beyond what `field-guide.md` already quotes — the 332MB `_archive/claude-export-2026-07-01.tar.gz` was confirmed to exist and sized, but not extracted/opened during this repair (out of scope for a targeted heartbeat fix; extracting a 332MB archive to re-verify a handful of already-quoted lines was judged disproportionate to the task). This is disclosed in `references/source-ledger.md` as LIKELY, not silently upgraded to VERIFIED.
- External existence of the "Natalie" prompt-writing GPT (Mast's tool) — not web-checked, out of scope.
