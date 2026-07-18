# Source Ledger — skills/jiang-xueqin-cognitive-autonomy

Repair target: `references/source-ledger.md` (new file; skill had none).

## Sources Consulted

1. **S1** — *"Become Mentally Unbreakable Like the Top 1% — In 30 Days || PROF JIANG XUEQIN"* (Merlin AI transcription). YouTube: https://www.youtube.com/watch?v=BJX13jZxx_w. Extracted via claude.ai MES 3.0, conversation dated 2026-02-08. Location: `claude-export/normalized/conversations/7a3d28e5-5cd5-4d7c-a11f-b01f0d414d8f.md` (100,519 bytes) inside `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes total). Full transcript text is preserved **verbatim** in message 1 of the export (~9,195 words, one continuous block). The claude.ai extraction artifacts the assistant built from it (Content Assessment, 7 Crown Jewel Prompts, Expert Operating System) are **not recoverable** — every artifact block in the export renders as the literal string "This block is not supported on your current device yet."
2. **S2** — *"Game Theory #1: The Dating Game || Professor Jiang Xueqin Explains"* (Merlin AI transcription). YouTube: https://www.youtube.com/watch?v=uxIQoSfbFMI. Extracted 2026-02-08. Location: `claude-export/normalized/conversations/5ce34135-b064-4be9-b627-5d215e5cc77a.md` (81,061 bytes). Full transcript verbatim in message 1 (~5,500 words per the assistant's own content assessment inside that same message). Extraction artifacts again not recoverable (same "not supported" placeholder).
3. **S3** — *"Jiang Xueqin: Humanity's patterns, the nature of reality, and the battle for your mind"* interview (host: Alex Ray, "All Quiet on the Inner Front"). YouTube: https://www.youtube.com/watch?v=CRw5CCq8Uf4. Extracted 2026-02-08. Location: `claude-export/normalized/conversations/360aca39-4293-403c-bf29-d84b65c6df55.md` (138,285 bytes). Full transcript verbatim in message 1. Discusses psycho-history and applies game-theory/incentive analysis to named geopolitical actors (Putin, Trump) — informs the "real game" applied-analysis framing referenced in `workflows/02-map-the-real-game.md`, not directly quoted in genius.md.

A fourth match (`f12761ef-f991-4feb-9fb1-550a972b87e4.md`, 752,424 bytes) contains "Jiang" but is an unrelated medical-citation export (Liu/Wang/Jiang co-authors of an inflammation study) — confirmed irrelevant and excluded.

## Absence Check (an absence claim is itself a provenance claim — verified, not assumed)
- `extractions/` has **zero** files matching `jiang` or `xueqin` (`ls extractions/ | grep -i jiang` → empty).
- `_active/codex-harvest-2026-06-11/` — zero filename or content matches (`grep -rli "xueqin\|jiang"` → empty).
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — `tar tzf | grep -i` on filenames returned zero (source text is embedded inside conversation markdown files, not named for the expert). A first-pass content check via `tar xzOf | grep -a -l` also returned a **false negative** (zero) because `grep -l` cannot attribute matches across a single concatenated stdin stream when `tar` decompresses all members into one pipe. Corrected by iterating the tarball member-by-member in Python and decoding each file individually — that pass found the 4 files listed above (161 total content hits for "jiang|xueqin", case-insensitive). Recorded here so the "false unrecoverable" failure mode (flagged in the envelope as caught by adversarial verification this session) isn't repeated.
- `agents/jiang-xueqin/AGENT.md` (4,675 bytes) and `agents/jiang-xueqin/memory/context.md` (524 bytes) exist — read in full; persona/routing scaffolding only, no new factual claims beyond what's in genius.md already.

## Claim-by-Claim Labels (genius.md — Genius Patterns + Hidden Knowledge)

| # | Claim / Pattern | Label | Basis |
|---|---|---|---|
| 1 | Predictability, Not Obedience (power's arc: violence → belief → internalized surveillance → standardization → calibrated emotion) | VERIFIED | S1 — paraphrase of "predictability, not obedience... obedience is crude... religion... education... media" sequence |
| 2 | The Three Locks — Language, Emotion, Identity | VERIFIED | S1 — verbatim quotes anchored directly in genius.md ("defines what can be thought"; "heart rate increases... jaw clenches"; identity/self-dismantling passage) |
| 3 | Horizontal Enforcement (ostracism, peer policing) | VERIFIED | S1 — "Most control today is horizontal, not vertical... Ostracism is the ultimate deterrent" (near-verbatim) |
| 4 | Structure Over Belief (the elite method) | VERIFIED | S1 — "structure over belief and models over morals and history without heroism" (verbatim) |
| 5 | Belief as Tool — Elites Believe Less | VERIFIED | S1 — verbatim quotes anchored ("Elites believe less than regular people"; "belief systems are tools") |
| 6 | Strategic Silence | VERIFIED | S1 — "Expression creates commitment and commitment creates vulnerability... Silence is... strategic positioning" (near-verbatim) |
| 7 | Unprogrammable, Not Unprogrammed | VERIFIED | S1 — "This phrase is misleading and there's no neutral mind... becoming unprogrammable" (verbatim) |
| 8 | Find the Real Game (players/rules/incentives) + dating/status/Instagram demonstration | VERIFIED | S2 — "there are three components to a game... the players... the rules or the constraints... the incentives" + the five-boys-five-girls Nash-equilibrium demonstration and the Instagram quote (verbatim) |
| 9 | Superstructure Determines the Game (three named superstructure examples) | VERIFIED | S2 — "the superstructure... is what determines the nature of the game" + the low-population/growing-population/overpopulation examples (verbatim detail) |
| 10 | Belief Crystallization — The Predictable Snap-Back | VERIFIED | S1 — "This is called belief crystallization... a psyche protecting itself from dissolution" — the term is Jiang's own, not a paraphrase |
| 11 | Conspiracies Are Comforting | VERIFIED | S1 — verbatim quote anchored ("conspiracies are actually comforting... if there's a villain, you can fight the villain") |
| 12 | Awareness Has a Price — Choosing the Cage Is Rational | VERIFIED | S1 — "Awareness does not make you happier... double consciousness... most people... rationally choose programming" (near-verbatim) |
| 13 | Emotional Reaction Precedes Thought — Then Hires It | VERIFIED | S1 — verbatim quote anchored ("Your heart rate increases. Your jaw clenches... milliseconds, way faster than conscious thought") |
| 14 | The Boundary Test — Which Questions Get You Labeled | VERIFIED (close paraphrase) | S1 — "how does photosynthesis work... why do we spend six hours a day sitting in rows"; "what year did World War II start... who benefited from the war and who made money from the war" — genius.md compresses the second clause to "who profited from it" (same meaning, not a fabrication) |
| 15 | "23 unconscious mastery behaviors detected" and the original Crown Jewel Prompt titles (Moral Reflex Suspension Analysis, Structural Analysis Engine, etc.) | UNCONFIRMED | These are the assistant's own MES 3.0 extraction labels inside S1/S2/S3, not Jiang's language, and the artifact bodies that would substantiate the count/titles are unrecoverable ("not supported on your current device yet"). **Not asserted anywhere in genius.md or SKILL.md** — recorded here only so this count is never re-added as if sourced. |

## Anti-Patterns Section (genius.md)
All 7 items VERIFIED against S1 — each quote checked character-for-character against the extracted transcript text before being anchored.

## Workflows (`workflows/*.md`, `references/prompts-v2/*.md`)
Not modified this pass — `workflow_contracts` was already PASS in the heartbeat audit (all 3 workflow files carry Output Schema + Quality Gate). Not re-verified against source line-by-line; flagged for a future pass if the skill is audited again.
