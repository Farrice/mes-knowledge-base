# Provenance — Lara Acosta LinkedIn Content Mastery Repair

> Every grounded addition made during this repair pass (Frontier Wave 3 PoC, 2026-07-17), with exact source file, line, and date. Labels (VERIFIED/LIKELY/UNCONFIRMED) live in `references/source-ledger.md`; this file is the raw citation trail behind them.

> **CORRECTION — 2026-07-17 (same-day, second pass).** The prior version of this file stated `transcript.txt` and `2026-linkedin-playbook-transcript.txt` in `extractions/lara-acosta/` and `transcript.txt` in `extractions/lara-acosta-content-system/` were "0 bytes — unusable." This was false and was never actually verified before being written — an adversarial verifier caught it. All three are full, non-empty, readable transcripts:
> - `extractions/lara-acosta/transcript.txt` — **64,332 bytes**. Full podcast-interview transcript (Lara + host, LinkedIn playbook for 2026).
> - `extractions/lara-acosta/2026-linkedin-playbook-transcript.txt` — **31,860 bytes**. Full solo-camera breakdown transcript (the 4-step LinkedIn attention-arbitrage playbook).
> - `extractions/lara-acosta-content-system/transcript.txt` — **25,149 bytes**. Full 1:1 coaching-call transcript (Lara + Cameron, building his LinkedIn content system live).
>
> All three are effectively single-line files (no embedded newlines), which is the likely reason a prior pass that ran a shallow check (or read a stale/empty intermediate artifact) concluded they were empty. They have now been read in full and re-tested against P9, P14, P16, and the zero-entity evolution-log entry below.

Two source directories remain ground truth, now including the raw transcripts:
- `extractions/lara-acosta/` — `2026-linkedin-playbook-extraction.md` (dated 2026-03-05 by git history), `extraction-report.md` (2026-03-02), `validation-report.md` (2026-03-02), **`transcript.txt` (64,332 bytes, 2026-02-25)**, **`2026-linkedin-playbook-transcript.txt` (31,860 bytes, 2026-03-05)**.
- `extractions/lara-acosta-content-system/` — `extraction-report.md` (2026-03-02), **`transcript.txt` (25,149 bytes, 2026-02-26)**.

## genius.md — Anti-Patterns section (from prior pass, unchanged, still accurate)

| # | Claim added | Verbatim source quote | File : Line | Date |
|---|---|---|---|---|
| 1 | Never schedule-and-ghost | "If you can't be there to engage, don't post at all during that day." | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:84` | 2026-03-05 |
| 2 | Never lean on AI-written comments | "Don't use AI comments" | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:137` | 2026-03-05 |
| 3 | Never open with "How to" | "'How to' is AI slop. ChatGPT writes 'How to.' True experts write 'How I.'" | `extractions/lara-acosta/extraction-report.md:63` | 2026-03-02 |
| 4 | Never tag an authority without back-channel confirmation | "DO NOT physically tag their @ handle in the post unless you have back-channel confirmation they will comment within 30 minutes" | `extractions/lara-acosta/extraction-report.md:50` | 2026-03-02 |
| 5 | Never niche the hook down to the buyer only | "'My business gets 10 leads every week without outbound' outperforms 'If you're a B2B business owner making over $10M a year, here's how...'" | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:117` | 2026-03-05 |
| 6 | Never announce a win as raw "I" | "100% positive sentiment in comments, avoiding the 'LinkedIn Lunatics' backlash" (Success Metric for the Humble Brag pattern) | `extractions/lara-acosta/extraction-report.md:46` | 2026-03-02 |
| 7 | Never let content try to sell | "Content's job: attract the right people. NOT to sell." | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:100` | 2026-03-05 |

These 7 were already grounded in the `*-extraction.md` / `extraction-report.md` files, which is legitimate — those files are themselves derived from the transcripts and their quotes check out. No change needed here.

## genius.md — Named-entity groundings added to existing patterns (10 sections, from prior pass, unchanged, still accurate)

| Pattern | Grounding added | File : Line | Date |
|---|---|---|---|
| P3 — 4-3-2-1 Content Ratio | "Split them into 1 Education, 1 Storytelling, 1 'Edu-Telling' (both combined), and 1 Education (again)" | `extractions/lara-acosta-content-system/extraction-report.md:22` | 2026-03-02 |
| P4 — First-Principle Hook Testing | "a 3x higher click-through-rate on the 'see more' expansion" | `extractions/lara-acosta/extraction-report.md:24` | 2026-03-02 |
| P6 — Social Proof Archaeology | "made $10K passively from comments (linking to a Gumroad product in replies)" | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:113` | 2026-03-05 |
| P7 — Content Pillar Excavation | "Define the TAM topics (AI, Productivity, Remote Work, LinkedIn), Growth topics (building a SaaS, quitting 9-to-5), and Sales topics" | `extractions/lara-acosta-content-system/extraction-report.md:53` | 2026-03-02 |
| P8 — The SLAY Framework | "High comment volume and high average read time (time-on-post)" | `extractions/lara-acosta/extraction-report.md:34` | 2026-03-02 |
| P11 — Lead Magnet Virality | "Some took days, some took hours, some under 30 minutes. It doesn't need to be a hyperdesigned thing." | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:115` | 2026-03-05 |
| P12 — Format Emulation | "Find a viral post from an unrelated industry. Strip away the niche-specific words, keep the formatting... and inject your own industry's context." | `extractions/lara-acosta-content-system/extraction-report.md:40` | 2026-03-02 |
| P13 — Algorithm Optimization | "LinkedIn distributes based on network engagement. No engagement = content dies." | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:84` | 2026-03-05 |
| P15 — Authority Acceleration | "DO NOT physically tag their @ handle in the post unless you have back-channel confirmation they will comment within 30 minutes" | `extractions/lara-acosta/extraction-report.md:50` | 2026-03-02 |
| P19 — Three Growth Shapes | "the slowest because you reset every time you change direction" | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md:38` | 2026-03-05 |

## genius.md — NEW groundings from full-transcript read (this pass, 2026-07-17)

| Pattern / Claim | Grounding added | File : Line | Date |
|---|---|---|---|
| P9 — Voice Extraction Protocol (**UNCONFIRMED → LIKELY**) | "you can choose your writing style, which is my favorite thing... We built uh the backend prompts so it knows how to write specifically like me, how to write like Jake if you like how he educates, how to write like Justin Walsh, etc." | `extractions/lara-acosta/transcript.txt:1` (single-line file) | 2026-02-25 |
| P9 — supporting quote (authenticity mechanism) | "How do I remain authentic and make sure that it always sound like me?" → "we focused a lot on your story and what you specifically educate on and your social proof, right? That is the main thing that will keep you authentic" | `extractions/lara-acosta-content-system/transcript.txt:1` (single-line file) | 2026-02-26 |
| Expert Profile — "3 six/seven-figure businesses" (**LIKELY → VERIFIED**) | "I built three, [music] six, and seven figure businesses using content and LinkedIn." (`[music]` is a transcription tag mid-sentence, not spoken content) | `extractions/lara-acosta-content-system/transcript.txt:1` (single-line file) | 2026-02-26 |
| Expert Profile — corroborating detail | "I built an agency the product business and also a B2B SAS that just hit 60K MR." | `extractions/lara-acosta/transcript.txt:1` (single-line file) | 2026-02-25 |

**Caveat on the P9 upgrade**: the grounding above supports the *underlying mechanism* — Cleo (Lara's tool) captures an individual's writing voice/context so AI output "sounds like them" — as a real, stated practice. It does **not** verbatim- or substance-support the specific 5-part decomposition genius.md's P9 body currently lists ("signature phrases, sentence rhythm, emotional intensity moments, passion topics, humor patterns"). That taxonomy is house synthesis layered on top of a now-grounded mechanism, not itself sourced. Labeled LIKELY, not VERIFIED, for this reason.

## genius.md — Sections re-tested against full transcripts and confirmed still ungrounded (honest verified-absence, this pass, 2026-07-17)

Unlike the prior pass — which declared these UNCONFIRMED without ever reading the transcripts that supposedly didn't exist — this pass actually opened and grepped all three full transcripts for the relevant language before keeping the label. That makes these three items and one log entry a **checked absence**, which is a stronger and more honest claim than the prior pass's unchecked one.

- **P14 — Ghostwriting Voice Deployment.** Body claims: "Voice profile → topic approval → authenticity check → iteration loop. Never sanitize voice — amplify patterns." Grepped all three transcripts for `sanitiz*` and `amplify` — **zero hits in any file**. "Ghostwriting"/"ghost writing" does appear (Lara describes running a ghostwriting agency and doing weekly client interviews to mine story material — `extractions/lara-acosta/transcript.txt:1`, 2026-02-25), but no transcript describes the specific 4-stage pipeline or the sanitize-vs-amplify framing. **Transcripts read in full 2026-07-17 — no supporting material.** Kept UNCONFIRMED.
- **P16 — Client Attraction Content.** Body claims: "Problem-aware → solution-aware → decision-stage → trust-building. Map posts to buyer journey stages." Grepped all three transcripts for `problem-aware`, `solution-aware`, `decision-stage`, `buyer journey` — **zero hits**. The closest real material is the already-VERIFIED Revenue Bridge (P23: Content → Profile → Lead Magnet → Email → Sales), which is a monetization funnel, not a buyer-awareness-stage framework — they are not the same claim. **Transcripts read in full 2026-07-17 — no supporting material.** Kept UNCONFIRMED.
- **Evolution Log — "2026-04-09 — High-Performance Content Engine: Adversarial Proof Layer (Cycle 1)."** This entry documents the *skill's own* internal evolution/calibration cycle (a scoring delta on the system's own output quality across a self-improvement cycle) — it is not a claim about Lara Acosta's methodology at all, and was never extracted from source material to begin with. There is no sentence in any transcript that could ground it, structurally, regardless of how thoroughly the transcripts are read. **Confirmed out of scope for transcript grounding — not merely unfound, but the wrong kind of claim to look for a transcript citation on.** Left as-is (no label change; it was never a sourceable claim in the first place).

These three patterns plus the evolution-log entry still exist, uncredited, in `skills/lara-acosta-linkedin-mastery/references/genius-patterns.md` (Patterns 9, 14, 16) — that file itself carries no dates, quotes, or source citations, and reads as a pre-2026 synthesis, not a primary transcript. With the raw transcripts now confirmed readable and confirmed *not* to contain this material, the honest conclusion is that P14 and P16's origin is genuinely outside the two ground-truth extraction directories — not merely "unrecoverable due to a corrupted file."

## genius.md — "How to Use This Skill (Model Calibration)" section

Unchanged from prior pass — rewritten (not newly sourced) to be Lara-specific (SLAY labeling, dwell-time engineering, "How I" vs "How to") instead of generic Opus-instruction-following framing. References already-VERIFIED patterns (P4, P8, the "How I" anti-pattern) — no new factual claims.

## workflows/*.md — Output Schema sections (9 files, from prior pass, unchanged)

Every field in every `## Output Schema` skeleton is a direct restatement of that same workflow file's own pre-existing `## Output Contract` section. Source = the workflow file itself. See `REPAIR-NOTES.md` (in `skills/`) for the file-by-file mapping.
