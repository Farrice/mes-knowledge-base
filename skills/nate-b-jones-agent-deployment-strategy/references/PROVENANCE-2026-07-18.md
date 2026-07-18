# Provenance — nate-b-jones-agent-deployment-strategy repair

Anchor → source file + location. Full claim-by-claim detail lives in `references/source-ledger.md`; this is the compressed anchor table.

| Anchor (in modified genius.md) | Source file | Location | Status |
|---|---|---|---|
| Anti-Patterns section, item 1 ("30% organization... design team's existing footprint") | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/1b8a489c-6d96-42da-a68c-81f082353bbc.md` | raw transcript body, ~35% through file | VERIFIED |
| Anti-Patterns section, item 2 ("three seats on the creative team... point solution value") | same file | raw transcript body, ~80% through file | VERIFIED |
| Anti-Patterns section, item 3 ("viral trends... systematically underestimate") | same file | raw transcript body, opening paragraph | VERIFIED |
| Anti-Patterns section, item 4 ("accepting outdated materials or... dedicating a lot of headcount") | same file | raw transcript body, ~75% through file | VERIFIED |
| Anti-Patterns section, item 5 ("growth plan assumes... always require human involvement") | same file | raw transcript body, closing questions section | VERIFIED |
| Genius Pattern 2 entity-floor addition (billion images / 53 days) | same file | raw transcript body, opening line | VERIFIED |
| Genius Pattern 9 entity-floor addition (viral trends / underestimate quote) | same file | raw transcript body, opening paragraph | VERIFIED |
| Genius Patterns 3, 4, 6, 7, 8 and Hidden Knowledge 3, 5 entity-floor additions | this skill's own `genius.md` (Evolution Log 2026-04-09 entry, Exemplar 1, Exemplar 2, Anti-Exemplar, Hidden Knowledge #4) | internal cross-references within the same file, pre-existing content | VERIFIED as internal record; underlying pattern claims remain UNCONFIRMED (see ledger) |
| "How to Use This Skill (Model Calibration)" section, structural model | `skills/ben-watkins-storytelling/genius.md` | lines 7-16 | structural reference only, no factual claim about Jones |
| Genius Patterns 1, 5 and all 6 Hidden Knowledge items, Hall of Fame Exemplars, Anti-Exemplar, Signature Moves, Quality Rubric | none located | searched: `extractions/nate-b-jones/*` (5 files, 91,449 bytes total), `knowledge/extractions/inbox/...JARVIS Protocol...md` (349,923 bytes), `_archive/claude-export-2026-07-01.tar.gz` (3,711 conversation files) | UNCONFIRMED — genuine absence, verified by actual reads, not assumed |

No quote in this repair pass was used without being located and re-read verbatim in its source file. No "source absent" claim above was made without the corresponding grep/read having actually been run this session.
