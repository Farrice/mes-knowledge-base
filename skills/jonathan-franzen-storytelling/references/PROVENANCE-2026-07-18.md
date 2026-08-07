# PROVENANCE — jonathan-franzen-storytelling repair

Anchor → source file + location. All primary quotes are drawn from one transcript
file, located by CONTENT grep of `_archive/claude-export-2026-07-01.tar.gz` after
`extractions/` and the codex-harvest mirror both came up empty (see
`references/source-ledger.md` for the full discovery trail and sizes).

| Anchor in genius.md | Source file | Location |
|---|---|---|
| "How to Use This Skill" — cliché-per-book / minor-character / weather-page quotes | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/147f009c-5f9f-48fa-87df-89381c48dcbb.md` | line 30 (full transcript, single paragraph) |
| Pattern 1 quote ("I'm looking for a comic problem...") | same tarball/file | line 30 |
| Pattern 2 quotes ("distance is really really critical" / victim-positioning) | same tarball/file | line 30 |
| Pattern 3 quotes (shame / "pile on the ugliness") | same tarball/file | line 30 |
| Pattern 4 quotes (weather page / two sentences) | same tarball/file | line 30 |
| Pattern 5 quote (plane want-collision) | same tarball/file | line 30 |
| Pattern 6 quotes (iron bridge / girders) | same tarball/file | line 30 |
| Pattern 7 quotes (outline-visible / adventure) | same tarball/file | line 30 |
| Anti-Pattern: victim-positioned protectiveness | same tarball/file | line 30 |
| Anti-Pattern: outline-visible plotting | same tarball/file | line 30 |
| Anti-Pattern: cliché tolerance | same tarball/file | line 30 |
| Anti-Pattern: trauma-dumping self-focus | same tarball/file | line 30 |
| Anti-Pattern: breaking the vivid dream | same tarball/file | line 30 |
| Anti-Pattern: ornamental description | same tarball/file | line 30 |
| Video title / speaker / publish date (2025-11-26) | External — YouTube, `youtube.com/watch?v=7fpr4055HBY` | confirmed via WebSearch this session (title + date match; not a repo file) |
| Recognition-test language ("recognize this as literary work in his tradition") | `skills/jonathan-franzen-storytelling/genius.md` (pre-existing, unchanged) | "How to Use This Skill" section, original line 9 |
| Hall of Fame Exemplars 1 & 2 | `skills/jonathan-franzen-storytelling/genius.md` (pre-existing, unchanged prose; provenance note added) | — labeled UNCONFIRMED/synthetic by the file's own pre-existing text ("reconstructed" / "Generated from Franzen's patterns") |

## Absence claims — how they were checked (not assumed)

1. `ls extractions/ | grep -i franzen` → empty.
2. `grep -rli franzen extractions/` → one incidental hit only (`extractions/steven-pressfield/extraction-report.md`, 27,217 bytes — a cross-reference mention, not a Franzen source).
3. `_active/harness/codex-harvest-2026-06-11/` — has a `jonathan-franzen-storytelling/genius.md` (13,738 bytes) and `agents/jonathan-franzen/AGENT.md` (3,428 bytes). Diffed byte-for-byte against the live skill file — identical except the live file has one extra section. Not an independent source.
4. `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — filename listing (`tar -tzf`) showed nothing; **content** grep (`tar -xzOf ... | grep -a -c -i franzen`) returned 83 hits, which located the real transcript. Extracted to scratchpad (1.1GB uncompressed) and read directly.

This confirms rule #2 from the envelope: a "no source" claim without a content grep would have been false here.
