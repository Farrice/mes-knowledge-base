# Chris Cimorelli — Source Ledger

> Claim-by-claim provenance for `skills/chris-cimorelli-copywriting/`. Labels: **VERIFIED** (confirmed against a primary or in-repo document with an exact quote/anchor) / **LIKELY** (plausible, consistent with stated provenance, not independently re-checked) / **UNCONFIRMED** (no primary source located; treat as synthesized, not verbatim).

## Provenance search performed (2026-07-17)

- `ls extractions/ | grep -i cimorelli` → **0 results**. No `extractions/chris-cimorelli*` directory or file exists anywhere in the repo.
- `grep -ril cimorelli extractions/` → exactly one hit, `extractions/sam-parr/vision-copywriting.md`. Read in full at the matching line: Cimorelli's name appears once, in a list of 12 copywriting experts ("Chris Cimorelli (big idea/financial DR)") — zero verbatim quotes, techniques, or transcript material attributed to him in that file.
- No transcript, interview, podcast episode, or swipe-file document for Cimorelli exists in `extractions/`, `knowledge/`, or `research_outputs/` (checked by name and surname across those trees).
- Only documented origin found: `_active/codex-harvest-2026-06-11/agents/chris-cimorelli/AGENT.md` frontmatter — `source: "Perplexity research — FMS FinPub Pro Podcast, Agora case studies, industry analysis"`, `last_updated: 2026-03-19`. This is a Perplexity-research synthesis pass, not a primary Cimorelli-authored or -spoken document held locally.
- File-size / non-corruption check (per envelope instruction, `wc -c` not `wc -c` line count): `skills/chris-cimorelli-copywriting/genius.md` = 17,705 bytes; `SKILL.md` = 3,310 bytes; `workflows/01-front-end-promotion.md` = 10,918 bytes; `workflows/02-back-end-promotion.md` = 7,418 bytes; `workflows/03-copy-diagnostic.md` = 5,205 bytes; `references/prompts-v2/*.md` = 7,918 / 6,864 / 11,490 bytes. All files are populated real content — none are 0-byte, truncated, or corrupted stubs.

## Claim ledger

| Claim | Label | Anchor |
|---|---|---|
| Cimorelli is "Agora's #1 newsletter promo copywriter for 7+ consecutive years" / "7-figure revenue from single promotions" / "100+ FinPub promos deployed" | LIKELY | Asserted verbatim in `_active/codex-harvest-2026-06-11/agents/chris-cimorelli/AGENT.md` frontmatter (`credentials:` field) and body. Sourced there to Perplexity research, not to a primary Agora record, press release, or interview transcript held in this repo. Treat as industry-reputation claim, not independently re-verified here. |
| "Newsletter funnels in the $50M+/year range" (SKILL.md description) | UNCONFIRMED | No source document in this repo substantiates this specific dollar figure. Not present in AGENT.md either — appears to be an elaboration added when the skill was authored, with no traceable anchor. |
| The 8 Genius Patterns (Big Idea Architecture, Front-End/Back-End Calibration, Skeptic-Proofing, Cimorelli Lead Framework, Proof Pyramid, Momentum Copy, Asymmetry Principle, A/B Testing Mentality) | UNCONFIRMED as verbatim Cimorelli methodology | These read as coherent direct-response structure consistent with the broader Halbert/Bencivenga DR teaching tradition, synthesized under Cimorelli's name during the original Perplexity research pass (AGENT.md, 2026-03-19). No verbatim Cimorelli quote in this skill states these frameworks in his own words; no swipe file or interview is cited anywhere in the skill files. |
| Hall of Fame Exemplars 1-2 ("Hidden Loophole" lead, "Skeptic-Proofed" proof stack) and the Anti-Exemplar | UNCONFIRMED as actual Cimorelli-published copy | Explicitly illustrative material built to demonstrate the framework — no URL, swipe-file reference, or archived-promo citation anywhere in the skill. Genuine as verbatim TEXT of this skill file (quotable, checkable against these files), but not verified as Cimorelli's actual published work. |
| Evolution Log entry, 2026-04-09 (Consumer Posture Translation Layer) | VERIFIED as an in-system record | Confirmed present verbatim in `genius.md` § Evolution Log with dated hypothesis/result/change/lesson structure. This documents an internal skill-evolution event, not an external Cimorelli claim. |
| `workflows/03-copy-diagnostic.md` Metric 9 quote ("No 'guaranteed' language? No claims without substantiation? Legally clean?") | VERIFIED | Quote confirmed verbatim against `skills/chris-cimorelli-copywriting/workflows/03-copy-diagnostic.md`, line 39, during this repair. |
| Handoff-protocol adjacent experts (Luke Iha, Alex Copper, Cardinal Mason, Alen Sultanic, Eric Roth, Shaan Puri) | VERIFIED against local system | All named skill directories exist under `skills/` in this repo — confirmed by directory presence, not by re-verifying each expert's own provenance. |
| Workflow files (`01-front-end-promotion.md`, `02-back-end-promotion.md`, `03-copy-diagnostic.md`) and `references/prompts-v2/*.md` structure/contracts | VERIFIED | Read in full during this repair; all carry Output Schema + Quality Gate sections as required by `directives/skill-craft-standard.md` (pre-existing PASS, unchanged by this repair). |

## Bottom line

This skill is a **Perplexity-research synthesis**, not a transcript-grounded extraction. It should be treated as directionally useful DR-copywriting structure attributed to Cimorelli's known reputation, not as a verbatim capture of his own words or a documented swipe-file archive. Anyone extending this skill with a real Cimorelli interview, podcast transcript, or swipe file should update this ledger and re-label the corresponding claims to VERIFIED.
