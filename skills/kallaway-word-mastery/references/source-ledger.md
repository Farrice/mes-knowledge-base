# Source Ledger — kallaway-word-mastery

Every claim added or reformatted in this repair pass, traced to its source and
labeled VERIFIED / LIKELY / UNCONFIRMED. Sizes confirmed via `wc -c` (not
`wc -l`) on 2026-07-18, per the "verify absence, don't assume it" rule.

## Sources on disk (confirmed by direct read + `wc -c`)

| File | Size | Role |
|---|---|---|
| `extractions/kallaway/word-mastery-extraction.md` | 16,292 bytes | PRIMARY — Buckets 1-3 (GP-WM-01 through GP-WM-14) map 1:1 to `genius.md`'s existing content. Git-committed 2026-03-19. |
| `extractions/kallaway/extraction-report.md` | 6,971 bytes | SECONDARY — "Constraint-Free Bridge," "Latent Desire Mirroring," "Subject-Switching Matrix," Mad Lib templates. Feeds `genius.md`'s Hall of Fame Exemplars and Signature Moves sections. Git-committed 2026-03-02. |
| `extractions/kallaway/transcript.txt` | 34,072 bytes | NOT a source for this skill — content-checked and confirmed to be the "Illusion of Novelty" transcript (a different Kallaway topic, feeds `kallaway-illusion-of-novelty`). Not cited anywhere in this repair. |
| `extractions/kallaway/internet-money-machine-extraction.md` + `-transcript.txt` | 12,864 + 24,657 bytes | NOT a source for this skill — "Internet Money Machine Playbook" is a monetization/offer topic, not articulation/rhythm. Read and confirmed off-topic; not cited. |
| `extractions/kallaway-content-system/*` | up to 398,725 bytes (vtt) | NOT a source for this skill — content-operating-system domain (script/voice pipeline stage, not sentence-level rhythm mechanics). Grepped for rhythm/breather/HTBT/voice-pocket terms; one incidental hit ("voice/rhythm profile" as a pipeline step name, `extraction-report.md` line 49) is a different, unrelated use of the word "rhythm" — not cited. |

## VERIFIED (verbatim in `word-mastery-extraction.md` or `extraction-report.md`)

| Claim / Quote | Location |
|---|---|
| "I think maybe this could potentially work for some people" | `word-mastery-extraction.md`, GP-WM-08 |
| "This incredible framework will transform your ability to maybe eventually start thinking about ideas." | `word-mastery-extraction.md`, GP-WM-09 |
| "I grew my account really fast." / "I grew from 2,000 to 47,000 followers over 3 months on Instagram with these three methods" | `word-mastery-extraction.md`, GP-WM-12 |
| "Reader thinks 'this person is being honest with me' — not 'this person is performing vulnerability'" | `word-mastery-extraction.md`, GP-WM-14 Success Metric |
| "Replace 'Are you struggling with [Problem]?' with 'I just achieved [Dream Outcome] using [Simple Method].'" | `extraction-report.md`, "Latent Desire Mirroring" |
| "If the method requires a $1,200 machine, the relatability breaks." | `extraction-report.md`, "Condition-Free Framing" (Hidden Knowledge) |
| All GP-WM-01 through GP-WM-14 pattern text already present in `genius.md` Buckets 1-3 | `word-mastery-extraction.md`, matches section-by-section |
| "Constraint-Free Bridge," "Desire-First Hook Architect," "Gravedigger Lens" signature-move language already present in `genius.md` | `extraction-report.md`, Genius Patterns section |

## LIKELY (consistent with source, not a fresh verbatim pull this pass)

| Claim | Basis |
|---|---|
| Hall of Fame Exemplar 1 ("$12,473 added income... 3 simple word patterns") and Exemplar 2 ("Rhythm Code" admission example) — pre-existing in `genius.md` | These read as composite illustrations built to demonstrate GP-WM-01/02/11/13 in combination, consistent with the extraction's patterns but not verbatim lines from either source file. Left in place (additive-first, pre-dates this repair pass) — flagged here so they are never mistaken for direct Kallaway quotes. |
| Tone Calibration System table (5 registers, Formality-Trust Axis) — pre-existing in `genius.md` | Consistent with the Rhythm Architecture and Likable Expert Dynamics buckets in `word-mastery-extraction.md`, but presented as a structured table not found verbatim in either source file — reads as extractor synthesis/research enrichment, matching the file's own "parallel research enrichment" framing (see `genius.md` line 3). |

## UNCONFIRMED (source explicitly absent — verified by search, not assumed)

| Claim | Status |
|---|---|
| Bucket 9 (GP-WM-23 "Term Branding," GP-WM-24 "Thought Narration," GP-WM-25 "Embedded Truths") — attributed in `genius.md` to "a second batch of claude.ai extraction conversations ('Say This in Your Videos' — the 'Story Locks' video), 2026-07-10" | No file matching "Say This in Your Videos," "Story Locks," "Term Branding," "Thought Narration," or "Embedded Truths" exists anywhere under `extractions/` — confirmed via repo-wide grep, not just the `kallaway/` folder. The same unsourced Bucket-9-style content is cross-referenced from `kallaway-content-psychology/genius.md` and `kallaway-addictive-storytelling/genius.md`, meaning this is a pre-existing, repo-wide provenance gap predating this repair pass, not something introduced here. Left in place per additive-first boundary (the content itself is plausible and internally consistent, and deleting established skill content is out of scope for a repair pass) but labeled UNCONFIRMED — treat as unverified until a source transcript surfaces. |
| Anti-Exemplar passage ("Are you struggling to write compelling content that converts?...") — pre-existing in `genius.md`, reformatted as a sourced list item in the new Anti-Patterns section | This is internal skill-authoring (an illustrative bad example built to demonstrate GP-WM-07/08 failure), not a quote pulled from either source file. Reformatted from prose to a list bullet per the `anti_patterns_sourced` check's requirement (list items only), but its provenance is the skill file itself, not an extraction — labeled UNCONFIRMED as a Kallaway quote (it is not one), while noting it correctly illustrates a real, sourced failure pattern (GP-WM-07/08, which ARE Verified above). |

## Absence check (performed, not assumed)

- `ls extractions/ | grep -i kallaway` → two folders: `kallaway/` and `kallaway-content-system/`. Both read in full; contents itemized above.
- All five files in `extractions/kallaway/` opened and read; sizes confirmed via `wc -c`: `extraction-report.md` 6,971 bytes, `internet-money-machine-extraction.md` 12,864 bytes, `internet-money-machine-transcript.txt` 24,657 bytes, `transcript.txt` 34,072 bytes, `word-mastery-extraction.md` 16,292 bytes. None are 0-byte or truncated.
- Repo-wide grep for the Bucket 9 claude.ai-export claim terms returned zero hits under `extractions/`; the only hits are downstream skill files (`kallaway-content-psychology/genius.md`, `kallaway-addictive-storytelling/genius.md`) referencing the same unsourced content, plus a codex-harvest implementation-plan mention — none of which is a primary transcript.
- No "unrecoverable" or "0-byte" claim is made anywhere in this ledger.
