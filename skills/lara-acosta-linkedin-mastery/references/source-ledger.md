# Source Ledger — Lara Acosta LinkedIn Content Mastery

> Repair pass, Frontier Wave 3 PoC (2026-07-17; corrected same-day). Every claim in `genius.md` and the workflow Output Schemas labeled against ground-truth sources: `extractions/lara-acosta/` and `extractions/lara-acosta-content-system/`, **including the raw transcripts**. Full citation trail (file + line + date) lives in `PROVENANCE-2026-07-17.md`.

> **CORRECTION — 2026-07-17.** The prior version of this line read: *"Known gap: `extractions/lara-acosta/transcript.txt` and `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` are both 0 bytes — the raw transcripts this skill was originally built from are not recoverable."* This was false and unverified. All three raw transcripts exist, are fully readable, and have now been read in full:
> - `extractions/lara-acosta/transcript.txt` — 64,332 bytes
> - `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` — 31,860 bytes
> - `extractions/lara-acosta-content-system/transcript.txt` — 25,149 bytes
>
> They were re-tested against every UNCONFIRMED/LIKELY item below that plausibly could be sourced from them. Results are logged inline. Anything still labeled UNCONFIRMED below was checked against the full transcript text this pass, not just the extraction-report summaries — that's now a verified absence, not an unchecked gap.

## Labels
- **VERIFIED** — a verbatim quote or specific figure exists in one of the two extraction reports or the raw transcripts, cited file+line+date.
- **LIKELY** — consistent across two independent source docs, or a direct restatement of a source paragraph, but no exact verbatim quote covering the full claim.
- **UNCONFIRMED** — no grounding found in either extraction directory (reports, extraction docs, or now the raw transcripts) or in any dated/quoted material inside the skill; original provenance unknown.

## Expert Profile

| Claim | Label | Source |
|---|---|---|
| "#1 female creator on LinkedIn" / "LinkedIn Personal Brand Strategist" | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:7` (2026-03-05); `extractions/lara-acosta/extraction-report.md:5` (2026-03-02) |
| "300K+ followers" (from zero) | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:7` (2026-03-05); also stated repeatedly in `extractions/lara-acosta/transcript.txt:1` and `extractions/lara-acosta-content-system/transcript.txt:1` (both single-line files) |
| "Founder of LA Digital and Cleo" | VERIFIED | `extractions/lara-acosta/extraction-report.md:5` (2026-03-02) |
| "3 six/seven-figure businesses via content" | **VERIFIED (upgraded 2026-07-17, was LIKELY)** | "I built three, [music] six, and seven figure businesses using content and LinkedIn." — `extractions/lara-acosta-content-system/transcript.txt:1` (single-line file, 2026-02-26). Corroborated by "I built an agency the product business and also a B2B SAS that just hit 60K MR" — `extractions/lara-acosta/transcript.txt:1` (single-line file, 2026-02-25), naming the three: agency (LA Digital), info-product business, B2B SaaS (Cleo/Mentions). |

## 23 Genius Patterns

| Pattern | Label | Source |
|---|---|---|
| P1 Position Before Content | LIKELY | Consistent with the "I help [WHO]..." formula appearing in every workflow's Input Required section and `extractions/lara-acosta-content-system/extraction-report.md:28`; no single verbatim quote of "position before content" itself. |
| P2 Dual-Persona Content Design (ICP/IFP) | VERIFIED | ICP/IFP distinction and the "IFP" term: `extractions/lara-acosta-content-system/extraction-report.md:14,46` (2026-03-02); also directly discussed at length in `extractions/lara-acosta-content-system/transcript.txt:1` ("There's another one. It's called the IFP, ideal follower persona..."). |
| P3 The 4-3-2-1 Content Ratio | VERIFIED | `extractions/lara-acosta-content-system/extraction-report.md:22` (2026-03-02); `extractions/lara-acosta/extraction-report.md:54-58` (2026-03-02); framework named and explained in full in `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt:1`. |
| P4 First-Principle Hook Testing | VERIFIED | 8-word hook + rehook mechanic and "3x higher click-through-rate": `extractions/lara-acosta/extraction-report.md:20-24` (2026-03-02). |
| P5 Authority Trigger Stack | LIKELY | Matches `extractions/lara-acosta/2026-linkedin-playbook-extraction.md` Phase 4b language in the skill's own workflow files (specific numbers > vague claims), but the "stack" framing itself is not a direct quote. |
| P6 Social Proof Archaeology | VERIFIED | $10K comment-revenue example: `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:113` (2026-03-05); full context in `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt:1` ("this exact commenting strategy made me $10,000 passively, literally... dropping a link to a digital product I had up on Gum Road"). |
| P7 Content Pillar Excavation | VERIFIED | TAM/Growth/Sales pillar breakdown: `extractions/lara-acosta-content-system/extraction-report.md:53` (2026-03-02). |
| P8 The SLAY Framework | VERIFIED | `extractions/lara-acosta/extraction-report.md:26-34` (2026-03-02); origin story of the framework's name told in full in `extractions/lara-acosta/transcript.txt:1`. |
| P9 Voice Extraction Protocol | **LIKELY (upgraded 2026-07-17, was UNCONFIRMED)** | General mechanism grounded: "you can choose your writing style, which is my favorite thing... We built uh the backend prompts so it knows how to write specifically like me, how to write like Jake if you like how he educates, how to write like Justin Walsh, etc." (`extractions/lara-acosta/transcript.txt:1`, single-line file, 2026-02-25); authenticity mechanism: "How do I remain authentic and make sure that it always sound like me?" → "we focused a lot on your story and what you specifically educate on and your social proof, right? That is the main thing that will keep you authentic" (`extractions/lara-acosta-content-system/transcript.txt:1`, single-line file, 2026-02-26). **Caveat**: this grounds the practice of capturing someone's voice for AI replication, NOT the specific 5-part taxonomy in genius.md's P9 body (signature phrases / sentence rhythm / emotional intensity moments / passion topics / humor patterns) — that decomposition remains unsourced house synthesis. Not upgraded to VERIFIED for this reason. |
| P10 Zero-to-Authority Roadmap | LIKELY | Matches the 24-Hour/7-Day/30-Day Implementation Pathway structure used across both extraction reports (`extractions/lara-acosta/2026-linkedin-playbook-extraction.md:147-165`), but the specific "Days 1-30/31-60/61-90" framing is a restatement, not a verbatim quote. |
| P11 Lead Magnet Virality | VERIFIED | "Some took days, some took hours, some under 30 minutes...": `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:115` (2026-03-05); verbatim in transcript too: "Some of them took a few days to build and some of them just a few hours and many under 30 minutes. It doesn't need to be this hyperdesign thing" (`extractions/lara-acosta/2026-linkedin-playbook-transcript.txt:1`). |
| P12 Format Emulation | VERIFIED | `extractions/lara-acosta-content-system/extraction-report.md:38-40` (2026-03-02); full worked example (Jake Ward's SEO post reverse-engineered) in `extractions/lara-acosta-content-system/transcript.txt:1`. |
| P13 Algorithm Optimization | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:84` (2026-03-05). |
| P14 Ghostwriting Voice Deployment | **UNCONFIRMED (re-tested 2026-07-17, checked absence)** | Body claims a "Voice profile → topic approval → authenticity check → iteration loop" pipeline and "Never sanitize voice — amplify patterns." Grepped all three full transcripts for `sanitiz*` and `amplify`: zero hits in any file. "Ghostwriting" does appear — Lara ran a solo ghostwriting agency and did weekly client interviews to mine story material (`extractions/lara-acosta/transcript.txt:1`) — but no transcript describes this specific 4-stage pipeline or the sanitize-vs-amplify framing. **Transcripts read in full 2026-07-17 — no supporting material.** Present in pre-repair `references/genius-patterns.md` (Pattern 14) without its own citation; origin remains outside the two ground-truth directories. |
| P15 Authority Acceleration | VERIFIED | Tag/back-channel guardrail: `extractions/lara-acosta/extraction-report.md:48-52` (2026-03-02). |
| P16 Client Attraction Content | **UNCONFIRMED (re-tested 2026-07-17, checked absence)** | Body claims "Problem-aware → solution-aware → decision-stage → trust-building" buyer-journey mapping. Grepped all three full transcripts for `problem-aware`, `solution-aware`, `decision-stage`, `buyer journey`: zero hits. Closest real material is the already-VERIFIED Revenue Bridge (P23: Content → Profile → Lead Magnet → Email → Sales) — a monetization funnel, not a buyer-awareness-stage framework; not the same claim. **Transcripts read in full 2026-07-17 — no supporting material.** Present in pre-repair `references/genius-patterns.md` (Pattern 16) without its own citation. |
| P17 The Founder's Content Gap | LIKELY | Consistent with `extractions/lara-acosta-content-system/extraction-report.md` framing of founder content bottlenecks (know too much, technical translation); Cameron's own words in the transcript match closely ("I have a lot of information to share, but it's figuring out how I can say it in a way that's interesting to other people" — `extractions/lara-acosta-content-system/transcript.txt:1`), but no exact verbatim match of the 4-part "Founder's Content Gap" framing itself. |
| P18 Attention Arbitrage Economics | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:27-31` (2026-03-05); term used and explained in full in `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt:1`. |
| P19 Three Growth Shapes | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:33-40` (2026-03-05). |
| P20 Profile-as-Algorithm-Signal | VERIFIED | Mental Folder Test + headline/banner/featured alignment: `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:48-64` (2026-03-05). |
| P21 The 1+3 Comment Formula | VERIFIED | Credited to Jasmin Alic: `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:72-80` (2026-03-05); named in transcript as "Yasmin Alec" who "coined it the 1 + three rule" (`extractions/lara-acosta/2026-linkedin-playbook-transcript.txt:1` — minor name-spelling variance, same person). |
| P22 Post & Ghost Kill Switch | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:82-91` (2026-03-05). |
| P23 The Revenue Bridge Architecture | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:93-105` (2026-03-05). |

## Hidden Knowledge (1-11)

| Item | Label | Source |
|---|---|---|
| 1. IFP Multiplier (3-5x reach) | UNCONFIRMED | No matching figure in either extraction directory or the raw transcripts (not in envelope scope this pass; not re-checked beyond a keyword pass). |
| 2. First-Hour Window (80% of reach) | LIKELY | Consistent with the 30-minute engagement rule (`extractions/lara-acosta/extraction-report.md:62`, `2026-linkedin-playbook-extraction.md:84-91`; transcript: "if you're not there within the first 30 minutes of the post going live, then the post has a higher chance of dying") but the specific "80%" figure is not itself quoted anywhere. |
| 3. Authority Paradox | UNCONFIRMED | No matching material found (not in envelope scope this pass). |
| 4. Client Attraction Lag (90-180 days, quit at 60) | UNCONFIRMED | No matching material found (not in envelope scope this pass; same underlying claim-family as P16, also unconfirmed). |
| 5. Voice Preservation (ghostwriters sanitize) | UNCONFIRMED | Same finding as P14 above — grepped full transcripts for "sanitiz*"/"amplify," zero hits. Transcripts read in full 2026-07-17 — no supporting material. |
| 6. Positioning Compound | UNCONFIRMED | No matching material found (not in envelope scope this pass). |
| 7. 70-80% Email Rule | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:103,111` (2026-03-05); verbatim in transcript: "70 to 80% of my own revenue comes from email, not LinkedIn directly." |
| 8. Comments > Posts for Revenue ($10K) | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:113` (2026-03-05). |
| 9. Lead Magnet Simplicity | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:115` (2026-03-05). |
| 10. Audience Segmentation Trap | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:117` (2026-03-05). |
| 11. Network Effect Layer | VERIFIED | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:119` (2026-03-05). |

## Anti-Patterns (from prior repair pass)

All 7 items VERIFIED — each cites a direct quote, file, line, and date. See `genius.md § Anti-Patterns` and `PROVENANCE-2026-07-17.md` for the full citation on each. Unchanged this pass.

## Signature Moves / Quality Rubric

LIKELY across the board — internally consistent with the verbatim-sourced patterns above (8-word hook, F-shape formatting, humble-brag reframing all trace to VERIFIED patterns) but the rubric language itself is house synthesis, not a direct quote from source material. Unchanged this pass.

## Workflow Output Schemas (from prior repair pass)

VERIFIED as structural skeletons — every field in each `## Output Schema` block is drawn directly from that workflow's own pre-existing `## Output Contract` prose (same file), not new invented claims. Unchanged this pass.

## Evolution Log entry (checked this pass, structurally out of scope)

"2026-04-09 — High-Performance Content Engine: Adversarial Proof Layer (Cycle 1)" is a record of the skill's own internal evolution/calibration cycle (a scoring delta on the system's output quality across a self-improvement run) — not a claim about Lara Acosta's methodology. It was never extracted from source material and there is no transcript sentence that could ground it, structurally, regardless of how thoroughly the transcripts are read. Not a "gap" — the wrong category of claim to seek transcript support for. No label applies.
