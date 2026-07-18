# Provenance — enrico-incarnati-instagram-realestate repair

Anchor → source file + location. All quotes spot-checked verbatim via `grep -o` against `extractions/enrico-incarnati/transcript.txt` before inclusion.

| Anchor (used in) | Source | Verified how |
|---|---|---|
| Billboard quote ("Let's be honest, nobody's reading that") | `extractions/enrico-incarnati/transcript.txt`, Mistake #1 section | `grep -o` exact match confirmed |
| Dump quote (carousel of 10 photos) | same file, Mistake #1 section | Read in full; substring present |
| Lazy Reel quote ("it's lazy") | same file, Mistake #1 section | Read in full; substring present |
| Boring Professor quote ("You are that boring professor") | same file, Mistake #2 section | `grep -o` exact match confirmed |
| Generic Profile quote ("You literally just lost the lead") | same file, Mistake #4 section | `grep -o` exact match confirmed |
| "Link in Bio" quote ("It is killing your engagement") | same file, Mistake #4 section | `grep -o` exact match confirmed |
| One-Format Trap quote | same file, Mistake #2 section | `grep -o` exact match confirmed |
| Spec Sheet (LIKELY, not verbatim-named) | same file, golf anecdote, Mistake #1 section | Read in full; no verbatim "spec sheet" phrase exists — labeled LIKELY per envelope Rule 1 |
| Follower/reach self-claims (300K+, 40M/day, "third largest podcast") | same file, opening ~400 words | Read in full; self-reported by Enrico, not externally re-verified this pass (no WebSearch run) |
| Trent Miller / Lisa Dubois / Tampa Brie / Margie Morasco / Eric Thurwood | same file, Mistake #1 exemplar section | Read in full; all 5 names + format descriptions present verbatim |
| Nava Realy / Your New Texas Home | same file, Mistake #3 section | Read in full; both names + their specific claimed coverage present |
| Ryan Sirhan, Freddy, Adrienne, Tom | same file, scattered mentions | Read in full; present as transcribed (Ryan Sirhan flagged as likely ASR misspelling of "Ryan Serhant") |
| SKILL.md "Core Philosophy" quote (line 12) | Checked against same file — **NOT FOUND verbatim** | Full-text read; this line does not appear in the source transcript. Flagged UNCONFIRMED in `references/source-ledger.md`, left uncorrected (out of this repair's scope — SKILL.md content accuracy, not a failing heartbeat check) rather than silently passed over. |
| @_jiing audit data | `_active/codex-harvest-2026-06-11/brain/121fe594-3b12-4ae1-9339-c14ac503ee83/enrico_audit_jiing.md` | Read in full; a prior system deliverable, not an Enrico-teaching source — used only to confirm workflow output shape |
| Absence check: claude-export tarball | `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) | `tar -tzf ... \| grep -i enrico` — zero matches, confirmed by command output not assumption |
| Absence check: codex-harvest broader directory | `_active/codex-harvest-2026-06-11/` | `find -iname "*enrico*"` — only the one audit file found |
| ben-watkins-storytelling genius.md calibration model | `skills/ben-watkins-storytelling/genius.md` lines 7-16 | Read directly per envelope instruction; new Enrico section modeled on structure, written fresh for Enrico's own texture (direct-to-camera coach voice, specificity-over-category), never copied |

No quote in any changed file was invented — every blockquote in `genius.md`'s Anti-Patterns section and every claim in `references/source-ledger.md` traces to one of the two files above or is explicitly labeled UNCONFIRMED/LIKELY where it does not.
