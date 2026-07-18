<!--
PROVENANCE: Source ledger added in the Wave 3 heartbeat repair (2026-07-17) per
.tmp/wave3-batch2/ENVELOPE.md. Every claim in genius.md / SKILL.md is checked
against actual file reads of the two primary transcripts under extractions/
plus the three primary-source reference files already shipped with this skill.
Two transcript directories exist for this expert and were easy to confuse —
naming them explicitly here to prevent that:
  - extractions/diandra-escobar/transcript.txt (8,379 chars) = the "Steal Like
    an Artist" content-sourcing video.
  - extractions/Diandra Escobar/transcript.txt (18,550 chars) = the "5 hook
    formats / 131 hooks / 21 creators" video, including a live skill demo.
No claim below was labeled VERIFIED without the exact string search shown.
-->

# Source Ledger — Diandra Escobar LinkedIn Growth

## Primary sources consulted

| Source | What it is | Status |
|---|---|---|
| `extractions/diandra-escobar/transcript.txt` | "Steal Like an Artist" video transcript, 8,379 chars, read in full | VERIFIED (authentic transcript, exists, non-empty) |
| `extractions/Diandra Escobar/transcript.txt` | "5 Formats / 131 Hooks" video transcript, 18,550 chars, read in full, includes a live Claude-skill demo | VERIFIED (authentic transcript, exists, non-empty) |
| `references/hook-writing-rules.md` | The 40 Hook-Writing Rules — carries its own provenance comment: "Reproduced 2026-05-30" from Diandra's actual `linkedin-hook-writer.skill` (Distinctiva) | VERIFIED (primary-source reproduction, provenance note present in the file itself) |
| `references/hook-examples-library.md` | 131 annotated hooks + Width Scoring Guide — carries its own provenance comment: imported verbatim from her production skill's `EXAMPLES.md`, v1.0, dated 2026-04-08 | VERIFIED |
| `references/hook-format-library.md` | Merges the hook video (the *why*) with the production skill (the *how*) | VERIFIED (derivative synthesis of two already-verified sources; no independent factual claims beyond them) |
| `references/rehook-teardown-kit.md` | Productized deployment kit (offer, pricing, outreach copy) for workflow 21 | N/A — original commercial collateral authored for this skill, not a claim about Diandra's teaching; nothing to verify |

No third or fourth transcript source could be located anywhere in the repo (`find . -iname "*diandra*"` searched beyond `skills/`, `extractions/`, `.agent/`, `.claude/`, `evolution_store/`). Several claims in the pre-existing genius.md (Patterns 1-5, 8-10, 12-18, most of Hidden Knowledge, all five Hall of Fame Exemplars) reference material — an algorithm-deep-dive video, a "best LinkedIn content strategy in 2026" video, client case studies — that the transcripts themselves point to ("if you watched my other videos…") but that is not archived under `extractions/`. Those claims are labeled LIKELY or UNCONFIRMED below, not silently upgraded.

## Claim ledger

### VERIFIED — exact or near-exact string found in a primary source

| Claim (genius.md location) | Anchor |
|---|---|
| "Fired at 23," built to "close to $1M" from one platform by 25 | `extractions/diandra-escobar/transcript.txt`: "When I was 23, I got fired from a marketing agency. By 25, I'd built a content agency that's done close to a million dollars. All from one platform." |
| Agency name "Distinctiva" | Same file, transcribed as "the Stinct Diva" / "the Diva" (auto-transcription artifact — "Distinctiva" phonetically parses to both mis-hearings; treated as VERIFIED with the caveat noted, not a clean literal match) |
| Pattern 7 (Steal Protocol) — collect/copy/transform/adapt/compound, 3 sources (sales calls, internal docs, expert interviews) | `extractions/diandra-escobar/transcript.txt`, full "Collect → Copy → Transform → Adapt → Compound" section, quoted near-verbatim in genius.md |
| Pattern 11 (Format Test Escalation) | Same file: "Start with text posts... When a text post hits, turn it into a carousel. When a carousel hits, turn it into a video." |
| Hidden Knowledge: The Obscurity Advantage | Same file: "In the beginning, obscurity is good... nothing to distract you from getting better" |
| Hidden Knowledge: Extraction Over Creation | Same file: "Every artist is a collector, not a hoarder" |
| Hidden Knowledge: The Expert's Invisible Knowledge | Same file: "Why do you do it that way?" / "what's the mistake you see clients make most often?" — "9 times out of 10" |
| Pattern 19 (Pixel-Width Budget) | `extractions/Diandra Escobar/transcript.txt`: "LinkedIn doesn't render by characters, it renders by pixels," "The letter W takes up four times the visual space of the letter I," "around 110 width units... per line on mobile" |
| Pattern 20 (Gap Is the Engine) | Same file: "That gap is called curiosity. Curiosity is the click." |
| Pattern 21 (5-Format Hook System) | Same file: full walkthrough of Dense / Punchy+Context / Single-Line Bomb / Stacked / Hybrid, "131 hooks... 21 different working creators" |
| Pattern 22 (Wallpaper Effect) | Same file: "if something is way too consistent, people start treating [it] as wallpaper" |
| Hidden Knowledge: 360 Brew reads first 40-50 words, tracks stop-and-read | Same file: "the new LinkedIn model called 360 Brew... specifically tracks whether people stop and read" (the note that this "supersedes the older unified Llama 3 retrieval framing" is an editorial gloss, not itself a transcript claim — labeled LIKELY) |
| Hidden Knowledge: Two-Line-Break Requirement | Same file: manual double line-break instruction for Single-Line Bomb, quoted directly |
| Hidden Knowledge: Post-Previewer Is Non-Negotiable | Same file: Cleo's post-previewer demo, "always check mobile first" |
| Hidden Knowledge: No Em Dashes / banned-cliché list | `references/hook-format-library.md` "Hard Bans" section — exact cliché list match |
| Hidden Knowledge: No Questions in Hooks | `references/hook-writing-rules.md` Rule 9 |
| Hidden Knowledge: Primary-Source Corpus counts (44 Dense / 76 Punchy+Context / 3 Bomb / 8 Stacked) | `references/hook-examples-library.md` section headers, exact counts |
| Anti-Pattern 9 (Counting Characters, Not Pixels) | `extractions/Diandra Escobar/transcript.txt`: "LinkedIn doesn't render by characters, it renders by pixels" |
| Anti-Pattern 10 (Overloaded Punchy Line) | Same file: "The punchy line should provoke. The context line earns the click." |
| Anti-Pattern 11 (Soft Open, added in this repair) | Same file: "the problem is their first line is always soft, vague, throat-clearing sentences that don't really do anything" |
| Anti-Pattern 12 (Un-Patterned Stacking, added in this repair) | Same file: "If a reader can't predict the rhythm, the structure fails" |
| Anti-Pattern 13 (Bad Theft, added in this repair) | `extractions/diandra-escobar/transcript.txt`: "A bad theft degrades. skims, steals from one, plagiarizes, imitates, and rips off" |
| Anti-Pattern 14 (Generic-Advice Regurgitation, added in this repair) | Same file: "Everyone was posting the same stuff, myself included" |

### LIKELY — internally consistent with her teaching, not found verbatim in an archived source

These read as authentic Diandra Escobar material (consistent terminology, consistent with her verified patterns, plausible given the agency context) but could not be matched against a source file in this repo. Most likely origin: the other videos she references in-transcript ("if you watched my other videos") that were never archived under `extractions/`.

- Pattern 1 (Attention Redirection Principle), Pattern 2 (Boomerang Effect), Pattern 3 (The "So What?" Gate), Pattern 4 (LinkedIn Lag Advantage)
- Pattern 5 (4-Bucket Funnel) — the Growth/Authority/Conversion/Personal framing is echoed by the transcript's "Use the content funnel. Growth, authority, conversion, personal" (VERIFIED at the bucket-name level), but the specific 35/35/20/10 target ratio is not stated anywhere found — that ratio specifically is UNCONFIRMED
- Pattern 6 (Body-First Writing) — the core instruction is VERIFIED via `hook-writing-rules.md` Rule 1 ("Write the post body FIRST"); the extended "mine the body for the hook" framing beyond the rule text is LIKELY
- Pattern 8 (Infrastructure Trinity — Notion/Drive/Claude specifics), Pattern 9 (Engagement as Distribution — engagement list, recent-activity-URL mechanic), Pattern 10 (Content-Market Fit Timeline — posts 1-20/21-40/41+, 90-day frame), Pattern 12 (North Star Alignment), Pattern 13 (5-Field Author Signal), Pattern 14 (60-Token Audition), Pattern 15 (Depth-Over-Breadth), Pattern 17 (Percentile Threshold)
- Hidden Knowledge: Recent-Activity-Link Trick, Conversion Content Dependency, Visual = Better, Claude Over ChatGPT for LinkedIn, 500+ Word Context Dump, Register Is a Decision Not a Default, Rewrite Before Relabel
- Hall of Fame Exemplars 1-5 and both Anti-Exemplars — read as real client case studies consistent with an agency's public teaching style; the *pattern* each illustrates is grounded (Boomerang Effect, So-What Gate, contrarian-take mechanics, Save Economy, Small Account Advantage), but the specific engagement numbers are UNCONFIRMED (see below)
- Anti-Patterns 1-8 (original, pre-repair) — plausible synthesis of her funnel/infrastructure teaching, not independently quotable from the two archived transcripts

### UNCONFIRMED — specific named entities or statistics with no source-file match; treat as unverified if reused in client-facing output

- Client roster "Semrush, Backlinko, HeyReach" — not found in either transcript
- "449+ posts" tracked in a Kanban system — not found
- Pattern 16 (Save Economy) — the specific "1 save ≈ 5x reach" figure attributed to "Authored Up data analysis" — not found; the underlying idea (saves matter more than likes) is plausible LinkedIn-creator lore but the multiplier is unverified
- Pattern 18 (Small Account Advantage) — the specific "3.29% revenue increase" figure — not found
- Hidden Knowledge: "The Adam Bird Correction" — named researcher "Adam Bird" and his specific finding — not found in either transcript; could not confirm this person or claim exists
- Hidden Knowledge: "The Negative Signal Trap," "The Generative Recommender Sequence," "The Pod Detection Layer" — specific claims about LinkedIn's internal ML system — not found in either transcript
- Hall of Fame Exemplar engagement numbers: Liquid Death VP comment "190 likes"; ChatGPT×Google newsjack "293 comments, 234 reposts, 28,000 impressions"; Original Research hot take "390 comments, 300 reposts, 3,198 likes"; Small Account client "800 average to 4,200 average impressions" — none of these figures appear in either archived transcript

## What this means for downstream use

Workflows that generate client-facing claims (competitor comparisons, case-study language, "Diandra's data shows…" framing) should not present the UNCONFIRMED figures above as fact. The VERIFIED and hook-mechanical LIKELY material (formats, rules, pixel-width math, funnel bucket names, steal protocol) is safe to deploy as her actual teaching. Statistics without a source-file match need either a fresh source (a transcript of the referenced-but-unarchived video) or should be dropped/softened before they reach a client deliverable.
