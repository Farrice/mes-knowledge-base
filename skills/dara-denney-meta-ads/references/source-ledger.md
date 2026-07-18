# Source Ledger — Dara Denney Meta Ads

Claim-by-claim source audit for `skills/dara-denney-meta-ads/`. VERIFIED = quote/claim re-checked against a source file read in full during this repair pass. LIKELY = consistent with verified material and the original extraction's stated method, not independently re-checkable against a raw transcript in this repo. UNCONFIRMED = no source file located anywhere in the repo; expert-plausible but unproven.

## Sources Consulted (file + size, read in full this pass)

| Source | Path | Size (wc -c) | Status |
|---|---|---|---|
| Raw transcript, "Top Creative Formats for 2026" | `extractions/dara-denney/transcript.txt` | 15,690 bytes | VERIFIED — primary source, read in full |
| MES extraction report (distilled from transcript) | `extractions/dara-denney/extraction-report.md` | 20,481 bytes | VERIFIED — cross-checked against transcript.txt, quotes match verbatim |
| Static-ads-masterclass extraction vision | `extractions/dara-denney/static-ads-masterclass/VISION.md` | 5,293 bytes | VERIFIED as a planning doc, read in full — its own sourcing claim ("watched, frames + grounded transcript, 5,412 words") is LIKELY, not independently re-checkable (no raw transcript file for this video exists in the repo) |
| Static ad exemplars (frame-grounded) | `skills/dara-denney-meta-ads/references/static-ad-exemplars.md` | 8,681 bytes | VERIFIED — read in full; carries its own self-correction note (a prior draft's invented headlines/stats were caught and purged) |

## Claim-by-claim

### Video: "Top Creative Formats for 2026" (source: `transcript.txt`)
- **VERIFIED** — "I bet against this at the agency, and I was proved wrong" (format #5) — transcript.txt, opening paragraph.
- **VERIFIED** — "We're not cheap, and we don't want to be" / "Shout out to our creative strategist Nika" — transcript.txt, We're-not-cheap section.
- **VERIFIED** — "the big differentiator that I see between the large eight and nine-figure brands and the six and seven-figure brands... is that the eight and nine-figure brands have figured out partnership ads" — transcript.txt, yapper/partnership section.
- **VERIFIED** — David & Goliath 3-beat structure (enemy callout → contrast with brand → science proof, animations improve retention) — transcript.txt, David & Goliath section.
- **VERIFIED** — Apothékary anti-exemplar quote ("Put the wine down and pick up true relaxation...") — transcript.txt, yapper section.
- **VERIFIED** — 55+ audiences respond better to stock footage; younger audiences to iPhone/UGC — transcript.txt, TikTok love letter section.
- **VERIFIED** — Meta Creator Marketplace hook-rate filter (50% hook-rate / 7% interaction-rate example) — transcript.txt, yapper/partnership section.
- **VERIFIED** — The Woobles same-script/multiple-creator-personas example — transcript.txt, listical section.
- **VERIFIED** — "sadly worth a try just to hide it from your brand team" (We're-sorry ads) — transcript.txt, We're-sorry section.

### Video: "How I Make AI Static Ads (in minutes)" (YouTube 5C5VhqW9HCc, 2026-06-25)
- **LIKELY** — All 7 static format archetypes + exemplars (Wandering Bear, TIME/supplement, Happy Tuesdays, GRO Shampoo, dandruff transformation, Cook & Bake grid, totallee) — grounding is the frame-watch documented directly in `static-ad-exemplars.md`; no raw transcript file exists in `extractions/` for this video, so quotes are not independently re-checkable against a second source in this repo. The file's own history (a purge of invented headlines/stats caught after the fact) is a reason for LIKELY rather than VERIFIED, even though the current content reads as internally consistent and frame-specific.
- **LIKELY** — Layer 1/2/3 static system, 8 copy mechanics, 3 production levels — same sourcing basis as above (VISION.md + static-ad-exemplars.md).
- **VERIFIED** — The purge/self-correction note itself — `static-ad-exemplars.md` line 5, read directly this pass: "an earlier draft of this file invented headlines... and fake '5/5 tester' stats. Those are PURGED."

### Two additional video transcripts cited in genius.md / SKILL.md
Genius.md (line ~166-168 in the pre-repair file) and SKILL.md's References section cite two further sources: "I tested over 1000 ads. Here are the hooks ACTUALLY making MONEY" (YouTube `t-Xf12o4jt4`) and "The Ultimate Guide to Founder Ads on Meta" (YouTube `ToTQBWHm38I`), attributing the 4-Layer Hook Anatomy, the 10-family Winning-Hook Taxonomy, and the Founder Ad content (six plays, 7-beat script spine, interview-style shoots, the "Andromeda Shift" insight) to a "claude.ai export — Dara Denney conversations (2026-07-01)."

- **UNCONFIRMED** — Searched `extractions/` (`ls extractions/ | grep -i denney` and `grep -i dara`): only one directory, `extractions/dara-denney/`, containing the three files above — no file or subfolder matching either video ID or title. Searched repo root and `_archive/` for a claude-export artifact: found `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — not extracted or grepped in this repair pass (too large to safely open within this task's scope; doing so risks corrupting the shared working tree per the fleet's read-only mandate). No raw transcript or extraction-report file for either video exists anywhere searchable in the repo as of this repair.
- Genius.md's own text states "MES-wrapper inflation and invented stats from the export conversations were discarded" — i.e., the original author reports reviewing the raw export and filtering it, but the filtered/kept transcript was never saved into `extractions/`. This means the entire block (4-Layer Hook Anatomy, Winning-Hook Taxonomy, Founder Ad six-play menu, 7-beat spine, interview-style shoots, Andromeda Shift) is **UNCONFIRMED provenance** in the strict sense of this ledger: internally plausible, consistent with Dara's documented persona and technique, but not re-verifiable against any source file currently in this repo.
- **Recommendation for a future pass**: extract `t-Xf12o4jt4` and `ToTQBWHm38I` directly, or locate and grep the two video IDs inside `claude-export-2026-07-01.tar.gz`, before treating any specific number or verbatim quote in this block as VERIFIED.

## Gap named honestly

The static-ads-masterclass video and the two claude-export-sourced videos have no raw transcript files preserved in `extractions/`. This ledger does not claim "no source exists" without having searched — the search paths and file sizes above are recorded so a future worker can pick up the archive lookup rather than re-litigating whether the search was done. Per the fleet envelope's hard rule #2: absence-of-source is itself a provenance claim, and it is recorded here with the evidence that backs it (directory listing, archive size), not asserted from memory.
