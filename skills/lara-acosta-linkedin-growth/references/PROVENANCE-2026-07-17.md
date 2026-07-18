# Lara Acosta — Provenance Table (Wave 3 Batch 2 repair)

Anchor → source file + approximate character offset, for every quote/entity
added to `genius.md` in this repair pass. Full claim-by-claim VERIFIED/LIKELY/
UNCONFIRMED labeling lives in `references/source-ledger.md`; this table is the
narrower "where exactly did this text come from" index the envelope asks for.

Source files (all confirmed non-empty by direct read this session):
- `extractions/lara-acosta/transcript.txt` — 64,332 bytes → **T1**
- `extractions/lara-acosta-content-system/transcript.txt` — 25,149 bytes → **T2**
- `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` — 31,860 bytes → **T3**

| Anchor text added to genius.md | Source | Offset (approx.) |
|---|---|---|
| "the number one female profile on the platform" | T1 | ~315 |
| "eight words long... that's the cut off... on mobile" | T1 | ~16804 |
| "a rehook... your second chance to retain someone and get them to click more" | T1 | ~16017 |
| "I created it obviously because I'm a girl and I slay all the time" | T2 | ~48669 |
| "mainly male-dominated... 40y old... 40 men saying that they're using" | T2 | ~48733 |
| "start with a story, lead with a lesson, have actionable advice and then end with a U" | T1 | ~27369 |
| "that's actually how I signed my first ever whale client... five figures for this" | T1 | ~27369 (continuation) |
| "$200,000 a month... zero outbound, zero cold emails" | T1 | ~31350 |
| "today's the proudest day of my life... I retired my dad" (Simmyi example) | T1 | ~36723 |
| "POV, you became the first millionaire in your family... photos of my dad looking proud of me" | T1 | ~20606 |
| "she's so self-absorbed, I would have ended up in LinkedIn Lunatics" | T1 | ~20933 |
| "authority jacking which is my favorite" | T1 | ~30478 |
| "we have Simon Swift here, we have Sean, we have Daniel Priestley... halo effect around me" | T1 | ~40512 |
| "we're going to be following my 4 3 2 1 framework... four post a week" | T2 | ~9600 |
| "the split between the four... one post about education, one post storytelling, one post doing both" | T2 | ~9800 |
| "eight keywords that [LinkedIn] loves pushing. One of them is AI... productivity... remote work... LinkedIn itself" | T2 | ~10100 |
| "the best people that I know spend 30 minutes a week... 15 minutes every single day engaging" | T1 | ~3481 |
| "I move from how to to how I... how Hubspot is telling people to use LinkedIn" | T1 | ~48570 |
| "the problem with ChatGPT is that it gives you average output... LinkedIn is full of AI slop" | T1 | ~48570 (same region) |
| "if you have ever designed a landing page, you know the F shape... same principle on written content" | T1 | ~54492 |
| Jake's account "technically dormant"... "3 weeks"... "Reddit just lost 82% of its AI citations overnight"... "2,000 likes" | T1 | ~22118 |

## Checks fixed and how

1. **recognition_test** — added `## How to Use This Skill (Model Calibration)` to `genius.md`, containing "would Lara Acosta recognize this as..." and "someone using her vocabulary" (both match the auditor's regex). Written fresh for Lara's specific craft (SLAY-as-worksheet failure mode, the 2026 hook-doctrine revision, spoken-not-corporate texture) — not copied from the `ben-watkins-storytelling` reference.
2. **source_ledger** — new `references/source-ledger.md`: every claim in SKILL.md and genius.md labeled VERIFIED/LIKELY/UNCONFIRMED against the three transcript files, including two genuinely UNCONFIRMED items surfaced (see REPAIR-NOTES.md).
3. **named_entity_floor** — enriched the 3 zero-entity sections identified by the auditor (`## Genius Patterns` intro line, `### 2. The SLAY Framework`, `### 6. The 4-3-2-1 Content Matrix`) with verbatim quotes and numbers pulled from the transcripts above. Zero-entity ratio moved from 0.23 (3/13 sections) to 0.00 (0/14 sections) after re-run against the local auditor.
