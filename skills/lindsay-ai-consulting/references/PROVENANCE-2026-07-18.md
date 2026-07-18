# PROVENANCE.md — lindsay-ai-consulting repair pass (2026-07-18)

Anchor → source file+location table for every new/changed claim. Full
claim-by-claim ledger with VERIFIED/LIKELY/UNCONFIRMED labels lives in
`references/source-ledger.md`; this file is the compact anchor index the
envelope asks for.

| Anchor in genius.md | Source file + location |
|---|---|
| "How to Use This Skill (Model Calibration)" section — structural model | `skills/ben-watkins-storytelling/genius.md` lines 7-16 (read directly this pass, per envelope instruction) |
| "Recognition Test" section language | Authored this pass; not a factual claim about Lindsay Gonzalez, no source label applies |
| Anti-Patterns item 1 (generic subject lines) | `skills/lindsay-ai-consulting/genius.md` (pre-repair) — Hall of Fame Exemplars → Anti-Exemplar block, verbatim quote "Unlock the Power of AI for Your Business" |
| Anti-Patterns item 2 (buzzword stacking) | same pre-repair genius.md, Anti-Exemplar block, verbatim quotes "cutting-edge technology," "leverage the latest advancements" |
| Anti-Patterns item 3 (vague benefit framing) | same pre-repair genius.md, Anti-Exemplar block, verbatim quote "optimize your processes and drive growth" |
| Anti-Patterns item 4 (30-minute ask) | same pre-repair genius.md, Anti-Exemplar block ("30-minute discovery call") + Pattern 8 ("15-minute quick chat") |
| Anti-Patterns item 5 (4th follow-up) | same pre-repair genius.md, Pattern 7 ("3-Email Maximum") + Pattern 4 (temperature calibration) |
| Anti-Patterns item 6 (leading with credentials) | same pre-repair genius.md, Pattern 6 (proof stacking without paid clients) |
| Pattern 6 success-metric entity ("10 total proof points") | Authored this pass — illustrative extrapolation of the pre-existing "3+ case studies" metric; UNCONFIRMED external fact, flagged in source-ledger.md |
| Pattern 7 success-metric entity ("roughly 60%") | Authored this pass — illustrative extrapolation of the pre-existing "replies on email 1-2" metric; UNCONFIRMED |
| Pattern 11 success-metric entity ("90-day window") | Authored this pass — illustrative extrapolation of the pre-existing referral-leads metric; UNCONFIRMED |
| Pattern 13 success-metric entity ("12+ months," "30 days") | Authored this pass — illustrative extrapolation of the pre-existing "6+ months" metric; UNCONFIRMED |
| Expert's real name "Lindsay Gonzalez" (source-ledger.md, referenced in "How to Use" provenance-caution note) | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/1fe0e0e6-7322-44ae-9067-9a2cb3b509af.md` (22,944 bytes) and `.../c8a90370-5bb5-4daa-8dc9-992284edb76e.md` (32,289 bytes) — located via full-archive `tarfile` content scan, read in context, VERIFIED as an identity fact independent of this skill's own files |

## Search method (for the adversarial verifier)

1. `ls extractions/ | grep -i "lindsay"` — 0 matches.
2. Repo-wide `grep -rli "lindsay"` across `.md`/`.txt`/`.json` (excluding
   `skills/lindsay-ai-consulting` itself and `node_modules`) — 20+ hits,
   all inspected; relevant clusters listed in source-ledger.md.
3. `find . -iname "*.tar.gz" -o -iname "*.tar"` to locate compressed
   archives that a plain-text grep would miss.
4. `python3 tarfile` scan of `_archive/claude-export-2026-07-01.tar.gz`
   (332,779,255 bytes, 7,728 total members): filename pass (0 hits),
   then content pass across 7,712 text-like members (18 hits, all read
   in surrounding context, not just matched-line snippets).
5. No claim of "source absent" was made without this full search
   sequence completing first, per the envelope's rule against false
   "unrecoverable" claims.
