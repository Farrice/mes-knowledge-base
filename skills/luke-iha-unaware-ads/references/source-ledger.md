# Luke Iha (Unaware Ads) — Source Ledger

Claim-by-claim provenance for `skills/luke-iha-unaware-ads/`. Ground truth is unusually
strong for this skill: two dedicated transcripts exist in `extractions/` — one an
explicit "unaware ads" masterclass, one on hook-writing that repeatedly cross-references
the unaware-ads video by name. Every quote below was located with a direct `grep` string
match against the live file, not recalled from memory.

## Sources Consulted

| File | Size (`wc -c`) | Landed in repo (git log, `--diff-filter=A`) | Relevance |
|---|---|---|---|
| `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` | 55,910 bytes | 2026-03-10 | Direct source — full "unaware ads" masterclass transcript |
| `extractions/luke-iha/video-3-levels-of-awareness/extraction-report.md` | 13,497 bytes | 2026-03-10 | Genius Patterns 1-8 and Hidden Knowledge in `genius.md`/`references/genius-patterns.md`/`references/hidden-knowledge.md` are paraphrased directly from this report, which is itself a synthesis of the transcript above |
| `extractions/luke-iha-hooks/transcript.txt` | 25,569 bytes | 2026-03-20 | "Vicious hooks" video — explicitly tells viewers to "watch the video that I did on unaware ads on this channel," confirming it's a companion source for this exact skill. Source of all 6 anti-pattern quotes below. |
| `extractions/luke-iha/transcript.txt` (= `extractions/luke-iha-creative-strategist/transcript.txt`, byte-identical) | 32,648 bytes | 2026-03-02 | Proof-mechanisms video (22 proof weapons) — adjacent domain, checked for overlap, not directly quoted in this skill |
| `extractions/luke-iha-avatar-machine/`, `extractions/luke-iha-client-acquisition/`, `extractions/luke-iha-insight-mastery/` | n/a | n/a | Checked via `ls`/`grep` for unaware-ads content; none found — these feed sibling skills (avatar-machine, client-mastery, insight-vectors), not this one |

## Claims

| Claim | Label | Basis |
|---|---|---|
| "most people hedge... they usually start their ad actually three to four sentences in" (opener-hedging anti-pattern) | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`, located via exact-string grep. Quoted in full in `genius.md` → Anti-Patterns. |
| "A polite hook is a dead hook. A comfortable hook is a dead hook." | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`. Transcript has a stray duplicated word ("pre personally called out") immediately after; the ledger and genius.md render that clause as "[get] personally called out" to preserve meaning without misquoting — bracketed insertion is disclosed. |
| Fake-open-loop anti-pattern ("they'll write a hook and they think that they're doing some sort of open loop... they have no business to actually read the ad") | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`. Minor filler words ("I I wish I'm trying to think of") elided with `...` per standard transcript-cleanup practice; no substantive words changed. |
| "a mistake that people do is they try to put that mechanism first" | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`, immediately follows the "relevance/consequence before mechanism" principle. |
| "99% of drop shippers don't know what awareness levels are and 99% of drop shippers are competing and creating ads that are designed for these lower levels of awareness" | VERIFIED | Verbatim in `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt`. |
| "People don't want to lean into conspiracy oftentimes because they're afraid... most people would be surprised at how well people respond to the sort of conspiratorial type of angles" | VERIFIED | Verbatim in `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` (two clauses from the same sentence/paragraph, joined with `...`; nothing inserted). |
| "It doesn't read like an ad. It should read like information that's promising some sort of new insight, or it's a story, or it's a confession" | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`, quoted in the new Model Calibration section. |
| "my doctor accused me of lying" | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`, offered by Iha as a vicious-hook example. |
| "my husband came out as gay after 26 years of marriage and it nearly killed me" | VERIFIED | Verbatim in `extractions/luke-iha-hooks/transcript.txt`, offered by Iha as a vicious-hook example. |
| Genius Patterns 1-8 (Curiosity×Relevance, Worldview Porn, Open Loop Engine, Organic Hook Theft, Paradox Hook, Conspiracy Frame, Lost Wisdom Hook, Vectors of Winning Angles) | VERIFIED | Directly paraphrased from `extractions/luke-iha/video-3-levels-of-awareness/extraction-report.md` "Genius Patterns" section, which itself synthesizes the transcript. Pre-existing content, not rewritten by this repair. |
| Hidden Knowledge bullets (Unaware Ads = 10x Value / Ad Structure Isn't Linear / Transformation > Information / Hook Banks Are Gold Mines) | VERIFIED | Directly paraphrased from the same extraction-report.md "Hidden Knowledge" section. Pre-existing, not rewritten. |
| Hall of Fame Exemplar hooks ("The 'healthiest' breakfast you eat every morning is actually killing your energy...", "They don't want you to know the real reason you procrastinate...") | UNCONFIRMED as verbatim Iha quotes | Searched all 8 luke-iha extraction transcripts for these exact phrases — zero matches. These are skill-authored illustrative hooks written to demonstrate the Paradox Hook and Conspiracy Frame + Open Loop patterns, not things Iha said on record. Pre-existing content (not written by this repair); flagged here so nobody mistakes them for direct quotes. The 10 Archetypes list and 6-part ad structure they illustrate ARE sourced (see extraction-report.md, "Methodology: Unaware Ad Architecture" section). |
| Anti-Exemplar hook ("Tired of low energy? Our new supplement boosts your vitality!") | UNCONFIRMED as verbatim Iha quote | Same status as above — an authored contrast example, not a transcript quote. Its underlying claim (problem-aware-register copy fails unaware audiences) IS sourced — see the "99% of drop shippers" anti-pattern above, which makes the identical point about awareness-level mismatch. |
| Bio claims in the hooks transcript: "over $100 million in sales, at least one VSL doing $100 million," Genesis program "around 400 different marketers," named student results (Cosmin/Bashier from Uganda ~11K/mo, one student ~40K/mo, a "$37,000" record month) | LIKELY (self-reported, not independently verified) | Verbatim in `extractions/luke-iha-hooks/transcript.txt` as Iha's own spoken bio/testimonial claims. Not used as sourced content inside `genius.md`, `SKILL.md`, or the workflows for this skill — noted here only because they sit in the same source file and a future editor could be tempted to cite them as verified revenue/results figures. They are not independently verified against any external record (no LinkedIn, no case-study page, no third-party confirmation was checked as part of this repair — out of scope per the envelope). |
| Skill's own file sizes (confirm no silent 0-byte/truncated files caused the failing checks) | VERIFIED | `wc -c`, run directly this session: SKILL.md 3,990 B, genius.md (pre-repair) 9,187 B, references/genius-patterns.md 6,300 B, references/hidden-knowledge.md 2,625 B — all real, non-empty. The 3 failures (anti_patterns_sourced, recognition_test, source_ledger) were genuine content gaps, not file-corruption artifacts. genius.md's Quality Rubric table (last line, pre-existing) is genuinely truncated mid-header — a real defect, but not one of the 3 assigned checks; left untouched. |

## What This Repair Changed vs. Left Alone

- **Added** to `genius.md`: `## How to Use This Skill (Model Calibration)` (fixes `recognition_test`) and `## Anti-Patterns Iha Would Reject` with 6 source-anchored bullets (fixes `anti_patterns_sourced`, need ≥5).
- **Added**: this file, `references/source-ledger.md` (fixes `source_ledger`).
- **Untouched**: `SKILL.md`, `references/genius-patterns.md`, `references/hidden-knowledge.md`, all 6 `references/prompts-v2/*.md`, all 7 `workflows/*.md`, and every pre-existing `genius.md` section (Core Philosophy, Genius Patterns 1-8, Hidden Knowledge, Hall of Fame Exemplars, Signature Moves, the truncated Quality Rubric table header). The rubric table's missing data rows are a pre-existing defect outside the 3 failing checks assigned to this repair and were left as-is per the additive-first, minimal-touch boundary.
