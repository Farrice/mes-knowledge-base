# Source Ledger — sam-parr-copywriting-mechanics

Claim-by-claim provenance for this skill's grounded content. Labels: **VERIFIED** (quote/fact confirmed against a primary source file, byte size recorded), **LIKELY** (strong contextual inference, not independently confirmed), **UNCONFIRMED** (asserted in the video but explicitly flagged by the speaker as unverified, or a name/attribution the source itself garbles).

## Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Plain transcript (no timestamps) | `extractions/sam-parr/transcript.txt` | 68,567 bytes | Canonical, read in full |
| MES 3.0 deep extraction | `extractions/sam-parr/copywriting-extraction.md` | 19,451 bytes | Canonical, read in full |
| Roster-fit scoping note | `extractions/sam-parr/vision-copywriting.md` | 5,074 bytes | Canonical, read in full |
| Timestamped raw captions | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/transcript.txt` | 265,316 bytes | Found this pass — not yet ported to canonical `extractions/`; read and spot-checked, not fully re-read line by line |
| Video context ledger (structured) | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/video-context-ledger.md` | 479,184 bytes | Located, not opened (redundant with transcript.txt for this pass's needs) |
| Video context ledger (JSON) | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/video-context-ledger.json` | 974,207 bytes | Located, not opened |
| Analysis summary | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/analysis.md` | 2,167 bytes | Read in full |
| Uncertainty report | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/uncertainty-report.md` | 2,337 bytes | Read in full — confirms 3,988 spoken-evidence rows, 0 visual/OCR rows |
| OCR notes | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/ocr-notes.md` | 111 bytes | Read in full — "No on-screen text was extracted... skipped because mode is transcript" |
| Frame notes | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/frame-notes.md` | 119 bytes | Read in full — "No frames were extracted... skipped because mode is transcript" |
| Video metadata | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/metadata.json` | 273 bytes | Read in full — title/uploader/duration all empty (yt-dlp network failure at capture time) |

**Note on the timestamped source**: it exists (confirmed via `wc -c`, real content, not a 0-byte placeholder) but lives outside canonical `extractions/` — under `_active/harness/codex-harvest-2026-06-11/`, a Codex-fork harvest directory. SKILL.md already flagged this as "NOT YET PORTED" before this repair pass; that claim is accurate and preserved. Porting it into canonical `extractions/` is out of scope for this repair (write-scope is limited to this repair's output directory).

## Claims and Anchors

| Claim / Quote | Used In | Label | Basis |
|---|---|---|---|
| "You're reading this not because you want to, but because I want you to. Now, you're reading this second sentence because again, I'm telling you and forcing you to read this. This is called copyrighting." | genius.md, Verbatim Exemplars | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt` (opening lines of file). "copyrighting" is the file's own auto-caption rendering of "copywriting" — preserved verbatim, not corrected. |
| "Good copywriting means getting what's in my head into yours and influencing your behavior, getting you to do what I want." | genius.md, Verbatim Exemplars | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt`. |
| "Story, story, story, story. A lot of people are afraid to add stories in their uh when they're trying to sell stuff with copyrightiting because they think it's going to make it too long. There's no such thing as too long, just too boring." | genius.md, Verbatim Exemplars / Anti-Patterns (Pattern 6, 9) | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt`. Disfluency ("uh") preserved verbatim. |
| "Did you know that there's more Ecoli in your in your Tupperware container than there is your toilet bowl?" | genius.md, Verbatim Exemplars | VERIFIED (as a real quote) / UNCONFIRMED (as a factual E. coli claim) | Exact substring match, `extractions/sam-parr/transcript.txt`. Sam prefaces this one breath earlier with "I'm going to make up all the details" — the quote is real, the underlying stat is explicitly not. |
| "Nightly Rest is within arms reach." | genius.md, Anti-Patterns | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt` — the weak-ad example the host reads aloud for Sam to critique. |
| "No one will read this or watch this. This is too long. No, it's not interesting enough." | genius.md, Anti-Patterns | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt` — opening lines of the interview, spoken by the host as the objection Sam's whole framework answers. |
| "that would probably be a pretty good ad. Now everything I just said was fake. I don't know if that's true." | genius.md, Anti-Patterns | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt`. |
| "He doesn't say they're waterproof. He says, I wore them in the shower." | genius.md, Anti-Patterns | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt`. |
| "they, um, write drunk and edit sober." | genius.md, Anti-Patterns | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt`. |
| "I'm a [ __ ] writer. I'm a great editor." | genius.md, Anti-Patterns | VERIFIED (as transcript text) | Exact substring match, `extractions/sam-parr/transcript.txt`. The bracketed blank is the source file's own profanity-filter artifact — reproduced as-is. |
| Attribution of the above line to "David Olga" | genius.md, Anti-Patterns | LIKELY | The transcript's auto-caption spells the name "David Olga." This is almost certainly a phonetic mis-transcription of "David Ogilvy" (the quote — "I'm a [bad] writer, I'm a great editor" — is a well-known Ogilvy line elsewhere in advertising literature), but this source file alone does not spell "Ogilvy" correctly anywhere, so the attribution is not independently confirmed by this source. `copywriting-extraction.md` makes the same inference silently; this ledger surfaces it explicitly rather than passing it through as fact. |
| "we always talk about this like when you meet somebody new and you start like testing the water with jokes to see what you can land, what you can't, what you have to take back." | genius.md, Anti-Patterns | VERIFIED | Exact substring match, `extractions/sam-parr/transcript.txt`. |
| The 15 numbered Genius Patterns' `00:MM:SS` source anchors (Patterns 1–13 currently active in genius.md) | genius.md, Genius Patterns | LIKELY (spot-checked, not exhaustively re-verified) | 8 anchors (`00:00:41`, `00:01:01`, `00:01:19`, `00:35:17`, `00:02:26`, `00:11:50`, `00:03:01`, `00:04:24`) were checked this pass against `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/transcript.txt` — all 8 land on lines whose spoken content matches the pattern they're cited for. The remaining anchors were not individually re-checked in this pass; treat as LIKELY until spot-checked. |
| Sam Parr = founder of The Hustle, co-host of My First Million | SKILL.md, genius.md (implicit), `copywriting-extraction.md` | VERIFIED | Stated directly in the interview's own intro: "This is Sam Parr, founder of The Hustle... co-host of one of the leading business podcasts in the world, My First Million" (`extractions/sam-parr/transcript.txt`). |
| Evidence limit — transcript-only, no visual/OCR evidence available | SKILL.md, genius.md Source Boundary | VERIFIED | `ocr-notes.md` and `frame-notes.md` both state extraction was "skipped because mode is transcript"; `uncertainty-report.md` confirms 0 visual, 0 OCR rows against 3,988 spoken-evidence rows. |
| "Tale of Two Boys" WSJ ad ran ~28 years, Sam "mercilessly copying it" for Trends | `copywriting-extraction.md` (pre-existing, referenced not re-authored this pass) | VERIFIED | Exact substring match for "mercilessly copying" and "tale of two boys" confirmed in `extractions/sam-parr/transcript.txt` this pass. The precise "28 years" / "$2B" figures in `copywriting-extraction.md` were not independently re-verified against transcript this pass — treat those two numbers as LIKELY (consistent with the interview's framing, not re-confirmed word-for-word). |

## Guardrail (carried from `copywriting-extraction.md`, reaffirmed)

Sam repeatedly demonstrates copy structure using improvised, admittedly fake statistics ("everything I just said was fake, I don't know if that's true"). Any numeric claim sourced from this material must be treated as illustrative of structure only. Real deployment requires independent fact verification (Chain Step 5.5) before any stat ships in production copy.
