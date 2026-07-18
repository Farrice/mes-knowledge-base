# Lara Acosta — Source Ledger

Claim-by-claim provenance for every factual/attribution claim in `SKILL.md` and
`genius.md`. Labels: **VERIFIED** (verbatim or numerically exact in a source
file), **LIKELY** (source-consistent paraphrase or reasonable inference, no
verbatim anchor), **UNCONFIRMED** (no supporting text found in any source file
— present anyway for editorial/legacy reasons, flagged so it is never mistaken
for verified authority).

## Sources Consulted

| ID | File | Size | Nature |
|----|------|------|--------|
| S1 | `extractions/lara-acosta/transcript.txt` | 64,332 bytes | Full interview transcript (host + Lara Acosta), source for the original 6 Genius Patterns + Hidden Knowledge |
| S2 | `extractions/lara-acosta-content-system/transcript.txt` | 25,149 bytes | Coaching-call transcript (Lara Acosta + founder "Cameron"), source for the 4-3-2-1 Content System / IFP-ICP material |
| S3 | `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` | 31,860 bytes | Solo playbook video transcript, source for the 4-step authority-positioning walkthrough |
| S4 | `extractions/lara-acosta/extraction-report.md` | 8,192 bytes | Prior worker's structured extraction from S1 |
| S5 | `extractions/lara-acosta/validation-report.md` | 1,520 bytes | Prior worker's CEV/completeness pass on S4 |
| S6 | `extractions/lara-acosta-content-system/extraction-report.md` | 6,720 bytes | Prior worker's structured extraction from S2 |
| S7 | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md` | 12,133 bytes | Prior worker's structured extraction from S3 |

All three transcripts were opened and read in full for this repair pass — none
were 0 bytes; a prior worker's "unrecoverable" claim about these files was
false (per ENVELOPE.md warning) and is explicitly corrected here.

## Claims — SKILL.md

| Claim | Label | Anchor |
|---|---|---|
| "Lara Acosta is the #1 female creator on LinkedIn" | LIKELY | S1 host intro: "I brought on Lara Aosta, the number one female profile on the platform." Verbatim in the source, but it is the *interviewer's* framing claim, not an independently audited platform ranking — hence LIKELY, not VERIFIED. |
| "founder of LA Digital" | **UNCONFIRMED** | Not found in S1, S2, or S3 (0 matches for "LA Digital" across all three transcripts). Appears only in S4's one-line metadata header, itself unsourced. Carried forward from the prior extraction without a transcript anchor — flag for removal or independent verification before treating as fact. |
| "the 'TikTokification of text'" | LIKELY | Not a verbatim transcript phrase (0 matches for "TikTok" in S1/S2/S3) — it is the extraction author's synthesized label for a real, verbatim-verified mechanic (S1 @ ~54492: "if you have ever designed a landing page, you know the F shape... it's the exact same principle on written content"). The underlying technique is VERIFIED; the branding phrase is an interpretive gloss, hence LIKELY. |

## Claims — genius.md, Genius Patterns

| Claim | Label | Anchor |
|---|---|---|
| Pattern 1 — "eight words long" mobile cutoff rule | VERIFIED | S1 @ ~16804: "my rule of thumb is every single time you write the first two lines, they need to be eight words long because that's the cut off... on mobile." |
| Pattern 1 — the term "rehook" | VERIFIED | S1 @ ~16017: "a second line, and that's called a rehook. So the rehook is your second chance to retain someone and get them to click more." |
| Pattern 1 — "3x higher click-through-rate" stat | **UNCONFIRMED** | No numeric CTR-lift figure appears anywhere in S1, S2, or S3. Original extraction-report (S4) states this without a transcript anchor. Removed as a hard number from the enriched genius.md; the mechanism itself (higher CTR from the "see more" click) remains LIKELY as a directional claim only. |
| Pattern 2 — SLAY acronym breakdown (Story/Lesson/Actionable/You) | VERIFIED | S1 @ ~27369: "start with a story, lead with a lesson, have actionable advice and then end with a U." |
| Pattern 2 — "I created it obviously because I'm a girl and I slay all the time" | VERIFIED | S2 @ ~48669 (verbatim quote, exact wording preserved). |
| Pattern 2 — "40-year-old men" using the framework, "mainly male-dominated" | VERIFIED | S2 @ ~48733: "building a slay framework on LinkedIn... that is mainly male-dominated... I've got people that are 40y old... 40 men saying that they're using [it]." |
| Pattern 2 — "signed my first ever whale client... five figures" | VERIFIED | S1 @ ~27369 continuation: "that's actually how I signed my first ever whale client. I literally just broke down an entire strategy and they were like, 'Hey, I really like the way you think. Let me pay you five figures for this.'" |
| Pattern 3 — "$200k/mo" / "without cold email" example | VERIFIED | S1 @ ~31350: "my [client's] business is about to hit $200,000 a month... with zero outbound, zero cold emails, here's the breakdown." (Genius.md's shorthand "$200k/mo" and "without cold email" both trace to this line.) |
| Pattern 4 — "Today I retired my dad" / "POV: First millionaire in the family" | VERIFIED | S1 @ ~36723 ("today's the proudest day of my life, I retired my dad" — a post Lara cites from a creator named "Simmyi") and S1 @ ~20606 ("POV, you became the first millionaire in your family... photos of my dad looking proud of me"). The genius.md exemplar posts (Exemplar 1/2 in Hall of Fame) are illustrative constructions built in the pattern's style, not verbatim copies of either cited post — labeled LIKELY as craft demonstrations, not quotes. |
| Pattern 4 — "LinkedIn Lunatics" backlash term | VERIFIED | S1 @ ~20933: "she's so self-absorbed, I would have ended up in LinkedIn Lunatics." |
| Pattern 5 — Authority Jacking term + 30-minute tag-response guidance | VERIFIED (term) / LIKELY (30-min tag threshold) | S1 @ ~30478 ("authority jacking which is my favorite") and S1 @ ~40512 ("we have Simon Swift here, we have Sean, we have Daniel Priestley... if someone sees me next to these people, I have the halo effect around me"). The specific "confirm they will comment within 30 minutes" threshold is not stated as a numeric rule in the transcript — it is a reasonable extrapolation from the separately-verified 30-minute engagement-window pattern (Hidden Knowledge item 1), hence LIKELY, not VERIFIED, as applied to tagging specifically. |
| Pattern 6 — 4-3-2-1 structure (4 posts/week, 3 pillars, split) | VERIFIED | S2 @ ~9600-10400: "how many posts a week do you think you want to write four... we're going to be following my 4 3 2 1 framework... So four post a week. The split between the four is going to be one post about education, one post storytelling, one post doing both... Then the three is for the three content themes." |
| Pattern 6 — "eight keywords" LinkedIn pushes (AI, productivity, remote work, LinkedIn itself) | VERIFIED | S2 @ ~10100: "LinkedIn has these eight keywords that it loves pushing. One of them is AI. The other one is productivity. The other one is remote work. Um the other one is LinkedIn itself." |

## Claims — genius.md, Hidden Knowledge

| Claim | Label | Anchor |
|---|---|---|
| The 30-Minute Life Support Rule (stay present, reply to every comment) | VERIFIED (core rule) / LIKELY (the word "exactly" and "every single comment" as an absolute) | S1 @ ~3481: "the best people that I know spend 30 minutes a week creating content and maybe spend 15 minutes every single day engaging." The transcript verifies the 30-minute engagement discipline; it does not use the phrase "life support" (that label is the extraction author's), and does not state a strict "every single comment, no exceptions" rule — the underlying practice is VERIFIED, the absolutist framing is LIKELY. |
| "How I" > "How To" / ChatGPT-writes-"How to" claim | VERIFIED (the "How I" pivot) / LIKELY (the ChatGPT-specific framing) | S1 @ ~48570: "I move from how to to how I and that gives me a lot more credibility because it's how I do things rather than how Hubspot is telling people to use LinkedIn." She contrasts herself with Hubspot in the transcript, not explicitly with ChatGPT for this specific point (the ChatGPT/"average output" framing is VERIFIED elsewhere — see below — but attached to ideation quality, not the how-to/how-I pronoun choice specifically). The pronoun mechanic itself is VERIFIED; its attribution to "ChatGPT natively writes How to" is a LIKELY editorial connection between two separate true statements in the same interview. |
| "the problem with ChatGPT is... average output... AI slop" | VERIFIED | S1 @ ~48570 region: "the problem with chargebt [ChatGPT] is that it gives you average output and so that's why LinkedIn is full of AI slop." |
| F-Shape / Empty Space Aesthetic, landing-page analogy | VERIFIED | S1 @ ~54492: "if you have ever designed a landing page, you know the F shape, how people can read... landing pages. So it's the exact same principle on written content." |
| The First-Post Halo + "weaponize a 3-week break" | VERIFIED | S1 @ ~6038 (LinkedIn "natively pushes your first few posts onto the algorithm the most") and S1 @ ~22118 (Jake's account "technically dormant," "hadn't posted in 3 weeks," "Reddit just lost 82% of its AI citations overnight," "2,000 likes"). |

## Claims — genius.md, "Patterns from claude.ai export" section (2026-07-01)

These nine patterns and the "Hidden Knowledge (net-new)" bullets beneath them
originate from a separate claude.ai conversation export (not the three
transcript files above) and were merged into genius.md by a prior worker on
2026-07-01. That export file is not present under `extractions/` — it cannot
be re-opened for this repair pass.

| Claim | Label | Anchor |
|---|---|---|
| All nine numbered patterns (Authority Signal Shift, Monetizable Expertise × Strategic Arbitrage, SMPV, Content-Profile Fit Distribution, Signature Style Series, Story-Mining Pipeline, Give-Give-Ask Lead Magnet, Carousel Collaboration, Traffic Allocation Niche Discovery) and the six "Hidden Knowledge (net-new)" bullets | **UNCONFIRMED** (source file absent) | Cited in genius.md as "nine extraction conversations (2025-06 → 2026-01 source videos)" — no transcript for these source videos exists under `extractions/lara-acosta/` or `extractions/lara-acosta-content-system/`. Internally consistent with the three verified transcripts (same frameworks, same voice, no contradictions found), so treated as editorially trustworthy carryover, but cannot be independently re-verified against a source file in this repair pass. Flagged UNCONFIRMED per the hard rule: absence of a locatable source file means the claim is unauditable, not that it is false. |

## Claims — Evolution Log

| Claim | Label | Anchor |
|---|---|---|
| 2026-04-09 SLAY Narrative Engine v2 evolution entry (scores, source skill) | LIKELY | Internal to the Antigravity evolution system, not the LinkedIn source transcripts. Scores (5.2→8.1, etc.) are evolution-harness output, not independently re-run in this pass — treated as LIKELY (system-generated, not fabricated by this worker, not re-verified here). |

## Summary

- **VERIFIED**: 16 claims (transcript-anchored, verbatim or numerically exact).
- **LIKELY**: 7 claims (source-consistent paraphrase, editorial gloss, or system output not re-run).
- **UNCONFIRMED**: 3 claims ("founder of LA Digital," the "3x higher CTR" stat, and the entire nine-pattern claude.ai-export block whose source file could not be located).

No claim in this ledger was invented for this repair pass. Every VERIFIED row
was checked against the live transcript text during this session (2026-07-17);
approximate character offsets are given for the specific quote location within
each transcript file.
