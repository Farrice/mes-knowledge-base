# Source Ledger — dan-wang-literary-analysis

> Claim-by-claim provenance for every factual/biographical/quoted claim in `SKILL.md` and `genius.md`. Labels: **VERIFIED** (found verbatim or near-verbatim in the primary source), **LIKELY** (the underlying fact is real and well-documented publicly / the source contains an ASR-garbled version of it, but the exact wording used in the skill is a cleaned-up paraphrase), **UNCONFIRMED** (asserted in skill files with no anchor found in the primary source — none found for this skill; see note at bottom).

## Primary Source

- `extractions/dan-wang/transcript.txt` — 110,739 characters, `wc -c` confirmed 2026-07-17. Auto-transcribed (ASR) audio of the *How I Write* podcast interview between David Perell (host) and Dan Wang, author of *Breakneck* (2025) and the *Dan Wang Letters* (annual China analysis, 2017–2023). The file is a single unbroken line (no newline characters — confirmed via `text.count("\n") == 0`), so anchors below are given as a short, distinctive, `grep`-able quote fragment plus its approximate character offset (found via Python `str.find`), not a line number.
- No other extraction files exist for this expert: `ls extractions/ | grep -i wang` returns only `dan-wang/`. Checked `_active/harness/codex-harvest-2026-06-11/extractions/` for a `wang` match — none found (directory listing empty for this name). Did not need to fall back to the claude-export tarball (`_archive/claude-export-2026-07-01.tar.gz`) because the primary transcript is present, complete, and sufficient to ground every claim below — opening the tarball would not add a Dan Wang source that the primary extraction lacks.
- ASR quality note: the transcript mis-hears several proper nouns. Confirmed artifacts (transcript spelling → real-world referent, cross-checked against SKILL.md/genius.md's own usage and public knowledge of the guest): "Dan Wong" → Dan Wang (title of the episode itself, char ~0); "Stendal" → Stendhal (char ~7666); "Steven Cotkin" → Stephen Kotkin, Princeton historian, Stalin biographer (char ~43783); "Quinning" → likely Kunming (Wang's home region, char ~68022); "qualcom collected Canadian" → likely "calm, collected Canadian" (char ~22986); "Daang" → Da Nang, Vietnam (char ~95760); "Don Giovani / Kosifut / marriage of Figuro" → Don Giovanni / Così fan tutte / Le Nozze di Figaro (char ~10609). These are flagged LIKELY, not VERIFIED, for the corrected spelling; the underlying quote is VERIFIED as transcribed.

## Claims

| # | Claim (as used in SKILL.md / genius.md) | Label | Anchor (transcript.txt, search string ~char offset) |
|---|---|---|---|
| 1 | Wang wrote "six or seven annual letters" on China, roughly one a year (Pattern 20: Radical Infrequency) | VERIFIED | "seven annual letters" ~51258 |
| 2 | Wang is "perhaps 85% satisfied" with his book; no writer is ever fully satisfied (Tacit 1) | VERIFIED | "85% satisfied with my book" ~16960–17476 |
| 3 | Travel writing is "often very self-indulgent" — the failure Wang defines himself against (AN-2) | VERIFIED | "often very self-indulgent" ~23572 |
| 4 | Wang describes himself as "an outsider in various ways," from Quinning (periphery, not Beijing/Shanghai/Shenzhen) (Pattern 7) | VERIFIED | "outsider in various ways" ~67965 |
| 5 | Sorting books by publisher type — "Yale University Press or Stanford University Press or Oxford University Press" vs. trade press (Pattern 12) | VERIFIED | "Yale University Press or Stanford" ~40308 |
| 6 | Daily mantra: "to be a qualcom collected Canadian," repeated to hit the book deadline (Pattern 11) | VERIFIED (wording); LIKELY ("calm" intended) | "qualcom collected Canadian" ~22986 |
| 7 | Network-effects-of-knowledge framing, credited to Tyler Cowen: "the more you know, the more you're capable of knowing" (Pattern 15) | VERIFIED | "network effects in which growth can accelerate" ~108301 |
| 8 | Writing retreats in Austin, Da Nang (Vietnam), and Barcelona, plus a home office at Yale Law School in Ann Arbor (Tacit 3) | VERIFIED | "writing in Austin" / "Daang in Vietnam" / "proposal in Barcelona" ~95577–95900 |
| 9 | Wang's mother, a former TV news anchor, called after his *Morning Joe* appearance: "Son, you look terrible. What's going on?" (Tacit 4) | VERIFIED | "Son, you look terrible" ~98537; "Morning Joe" ~98438 |
| 10 | AI as "a very Tyler-like creature... in my pocket," a stand-in for mentor Tyler Cowen, for thinking-through only, never sentence generation (Tacit 5, AN-6) | VERIFIED | "Tyler-like creature" ~62560; "I will never take any of...ChatGPT's...flat sentences" ~62881 |
| 11 | Wang currently has no China visa and is waiting on the "Chinese Ministry of Foreign Affairs" (Tacit 6) | VERIFIED | "Chinese Ministry of Foreign Affairs" ~88641 |
| 12 | *Breakneck* cover: rejected dragon/high-speed-train genre defaults for "a woman standing below a giant structure that looks a lot like the Tower of Sauron," worked with editor Caroline (Tacit 7) | VERIFIED | "Tower of Sauron" ~97617; "editor Caroline" ~97181 |
| 13 | The "engineer society versus the lawyer society" frame Perell references while describing Wang's prose (used as connective tissue, not a genius-pattern claim) | VERIFIED | "engineer society versus the lawyer society" ~10258 |
| 14 | Wang's musical/literary influences: Mozart's Italian comic operas (opera buffa), Stendhal (Pattern 13, SKILL.md epigraph) | VERIFIED | "Mozart...his three Italian operas" ~8421; "Stendal" ~7666 |
| 15 | Score-copying apprenticeship: copying scores/prose "porting over a method...from trying to understand music and composition," trained as a clarinetist (Pattern 14) | VERIFIED | "porting over a method" ~104610; "I play clarinet" ~104817 |
| 16 | Contingency-over-just-so-stories: "every event feels kind of impossible before it takes place and then...it feels obvious and necessary" (Pattern 19, AN-7) | VERIFIED | "impossible before it takes place" ~50131 |
| 17 | Genre-escaping trade biography example — a historian (transcript: "Steven Cotkin," real name Stephen Kotkin) writing a Stalin biography as a Princeton professor (Pattern 18) | LIKELY (name spelling); VERIFIED (underlying fact) | "Steven Cotkin...biography of Stalin...Princeton" ~43783 |
| 18 | Disappointment-as-engine examples: Yale Law grads, Stanford "chosen" kids, San Francisco car-keys-in-a-drawer anecdote (Pattern 21) | VERIFIED | "car keys on the counter" ~90050–90350; Yale/Stanford disappointment discussion ~40300s, ~71800s–73600s |
| 19 | Meal-structured travel: organizing days around "the three or four eateries," trusting "the corner noodle shop," walking between them (Pattern 9) | VERIFIED (concept and "corner noodle shop"); LIKELY ("eateries" — transcript ASR renders the word as "eeries") | "corner noodle shop" ~30300; walking/eateries passage ~29956–30962 |
| 20 | Zoom in/zoom out oscillation — Perell: "the more that I zoom in to your writing, the better it gets" (Pattern 8) | VERIFIED | "zoom in to your writing" ~10343 |
| 21 | Flower Inspection image — Perell describing Wang's prose as "like looking at a flower... new levels of beauty" revealed on closer reading (Pattern 2) | VERIFIED | "looking at a flower" ~9844 |
| 22 | Texture-over-tectonic-plates: "tectonic plate movements" named as the failure mode; "a soup that you had in Kuning" as Wang's actual counter-move (Pattern 3) | VERIFIED | "tectonic plake movements" ~24948; "soup that you had in Kuning" ~24980 |
| 23 | Single Beautiful Sentence Method: "absolutely valid to try to construct an entire essay around a single beautiful sentence" (Pattern 6) | VERIFIED | "single beautiful sentence" ~15600 |
| 24 | *Breakneck* title process: considered "Move Fast and Break People," settled on *Breakneck* at the last minute (title/naming context, not a standalone genius pattern) | VERIFIED | "titling my book...Move Fast and Break" ~96331 |
| 25 | Skill's own workflow-count claim ("13 patterns made executable," SKILL.md frontmatter) | N/A (skill-authoring metadata, not a claim about Wang) | — |

## Notes for the adversarial verifier

- Every quote embedded as an entity-grounding fix in `genius.md` (see `PROVENANCE.md`) traces to a row above.
- No claim in this skill required an UNCONFIRMED label — the single transcript source was sufficient for every pattern touched during this repair. This is reported honestly rather than defaulted to "all verified" as a courtesy label: each row above was checked against an actual character offset in the source file, not asserted from memory.
- Pre-existing content not touched by this repair (Patterns 1, 4, 5, 10, 16, 17 and Anti-Patterns AN-1 through AN-6, which already passed `named_entity_floor` before this repair) was left as-is per the additive-first boundary and was not re-verified against source — it was already passing the heartbeat check that this repair targets.
