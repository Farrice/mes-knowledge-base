# Source Ledger: Adil Amarsi Creative Strategy

**Status:** All three checkpoints approved; Phase 8 local closeout complete
**Build state:** Luke Iha in-place extension built, locally verified, and recorded as shipped in isolated-worktree telemetry; no external or global deployment.

## Phase Progress

Phase | State
---|---
Source capture | Complete
Vision checkpoint | Approved by Farrice
Deep extraction | Complete in `deep-extraction.md`
Architecture checkpoint | Approved by Farrice
Skill build and registration | Complete locally; verification approved
Runtime observation | `RUNTIME_OBSERVED — ONE FROZEN FIXTURE`
Behavioral reliability | Untested
Formal Luke blind pass | Unavailable; 0/2 unseen reference-corpus pieces
Market performance | Untested
Phase 8 finalizer | `KEEP — 7.67/10`; intent 8, expert 7, adversarial 8, factual 7
Forge telemetry | Shipped locally; production uses 0

## Primary Source

 Field | Value
---|---
 Source | [Billion-Dollar Copywriter Exposes Creative Strategy (No BS)](https://www.youtube.com/watch?v=zX61pyC1vLM)
 Video ID | `zX61pyC1vLM`
 Channel / host | Matthew Volkwyn
 Primary guest expert | Adil Amarsi
 Published | 2026-07-23
 Duration | 1:02:57 (`3,777` seconds)
 Captured transcript | 13,605 words
 User-supplied start anchor | 10:32

The 10:32 anchor lands at the end of Matthew Volkwyn's summary that strategy is not hook rewording. Adil's German collagen case begins at approximately 10:53, followed by the language-market discussion at 14:54. The anchor is therefore treated as a **LIKELY emphasis signal**, not as an instruction to ignore the rest of the source.

## Local Evidence

 Artifact | Purpose | Receipt
---|---|---
 `source/transcript.txt` | Complete clean transcript used for full-source review | SHA-256 `d5db63c24f7bccdfab02c442cbc97fc12a17645b49a7440a6aed469bef43ad52`
 `focused-visual-10m32/download/video.en-orig.vtt` | Timestamped native-caption evidence around the supplied anchor and across the video | SHA-256 `d7bdfa1db86439a36adc502cccb0e140ab72562007b8c9b02393ff5eba0d0a60`
 `focused-visual-10m32/download/video.info.json` | Public metadata and chapter map | Captured with `yt-dlp`

Whole-video visual capture was skipped by the deterministic 10-minute safety cap. A focused four-frame attempt around 10:32 retrieved native captions and metadata but the public video stream returned HTTP 403 before frames were produced. The relevant section is a spoken interview case, so no unseen on-screen artifact is being used as evidence. Any later claim that depends on a visual must remain `UNCONFIRMED` until frames are available.

## Chapter Map

 Start | Chapter
---:|---
 00:00 | Intro
 03:59 | What is Creative Strategy?
 06:55 | Tapping the Right Audiences
 10:53 | The German Brand that 10X'd Sales Overnight
 14:54 | Using Translation as a CS Tool
 21:02 | The Rigidity Trap
 30:45 | The Return of the Work Experience Requirement
 35:43 | Is E-commerce Strategy Easier than Info?
 56:44 | Cold Outreach Strategies

## Attribution Boundary

### Adil Amarsi

Adil owns the discussion of concept, audience, buying situation, channel, and market selection before wording. His other source-native ideas include product truth x overlooked segment, audience and complementary-demand adjacency, language or geography as a market-entry variable, the Profit Finder role, human buying invariants across niches, info-to-e-commerce experience translation, private practice, speculative samples, and live demonstration.

### Matthew Volkwyn

Matthew owns the current job-market observations, experience requirements, Dojo and student examples, current-account workflow observations, the Dubai lower-CPA anecdote, and several summaries about why e-commerce execution is easier than information-product execution.

Shared conversation does not make every host statement part of Adil's methodology. Downstream files must retain speaker attribution where ownership affects the method or a factual claim.

## Evidence Classes

 Claim or source element | Status | Handling
---|---|---
 Adil says he has 24 years of experience and has worked across 433 niches/markets/industries | `SELF-REPORTED` | His official site repeats these claims; do not upgrade them to independent proof.
 German campaign produced about EUR 700K-710K in a short launch window | `SELF-REPORTED + FIRST-PARTY CORROBORATED` | The interview and Adil's official case-study page align. Useful as an exemplar, not causal proof.
 The associated company later sold for about 165M and founders received specific payouts | `UNCONFIRMED` | No independent match was established. Do not use as credibility proof.
 Story insertion alone moved monthly email revenue from 8K to 80K | `ANECDOTAL / CAUSALITY UNPROVEN` | Preserve as a source story only; other changes may have contributed.
 Collagen-loss rates, menopause effects, body-type science, aerosol harm, and natural-product safety | `unverified health or science claims` | Block from operational marketing output until product-specific clinical, legal, and regulatory evidence clears them.
 Italian/Brazilian licensing results, foreign-market CPA, pay multiples, and 10K retainers | `ANECDOTAL` | Treat as opportunity hypotheses requiring current market validation.
 “1,000 sales letters in a year” and “three and a half per day” | `INTERNALLY INCONSISTENT` | Do not turn the arithmetic into a factual benchmark.

## External Corroboration Boundary

[Adil Amarsi's official About page](https://adilamarsi.com/about/) repeats the 24-year, 433-market, revenue, and exit claims. This is first-party biography, not independent verification.

[Adil Amarsi's official case-study page](https://adilamarsi.com/) describes a German-language e-commerce campaign producing EUR 710,000 in four days. This corroborates what he reports across his own properties, but remains first-party.

No independent source was found that verifies the 165M exit as described in the interview.

## Downstream Usage Rules

1. Source-native mechanics may become workflows only when they add a capability the roster does not already own.
2. Overlapping creative-research, hook, production, portfolio, and story mechanics should route to existing owners rather than be copied into a new Adil mega-skill.
3. Health, scientific, financial-result, and exit claims must retain their evidence labels.
4. Registration or promotion requires behavior proof beyond structural checks; source capture and a Vision document are not runtime proof.
