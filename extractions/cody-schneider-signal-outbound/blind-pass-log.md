# Blind Pass — Cody Schneider Signal Outbound

**Date**: 2026-08-06 · **Method**: manual side-by-side (Phase 7.4b). `execution/blind_pass.py` **not run** — the mission scoped `execution/` out of this build; the conductor records the verdict.

**Why this reference standard**: the usual corpus gate wants ≥2 published pieces. Here the source itself contains something better — **Cody executing the flagship workflow live on camera**, with the terminal visible. That's a falsifiable bar: run the workflow against the same input class and compare the artifact to what he actually produced, including the parts a shallow extraction would not know exist.

---

## Reference Standard (from the source)

**R1 — the live engager pull** (transcript ~11:00–12:00, frame 0071). One post URL → post-reactions + post-comments actors → dedupe:
```
● 61 unique engagers extracted • api…
    Counter({'reactor': 52, 'commenter': 9})
    obfuscated/no-slug: 52
  - All 52 reactor rows have obfuscated [URNs]
  - that's normal for the reactions [endpoint]
  Next step: src/resolve-linkedin-urls-exa.ts
  - Exa-resolve reactor URNs to public [profiles] → Verifier
  Sauntered for 34s
```
Narrated: *"the duped-by-public-profiles, there's 63 raw and it's about to pull all of those contacts out."*

**R2 — the waterfall ledger** (~21:40–23:00): 50 in → 32 found → 18 residual → +10 → 8 residual, "the way that you get to an 80% find rate," cheapest-and-most-accurate first, then validity checking before any send.

---

## Generated Artifact (blind — produced from `workflows/engager-signal-audit.md` + `waterfall-design.md` against the same input class, one niche post)

```
# Engager Signal Audit — [post: single creator post, AI-marketing niche]
## Pull Stats
raw rows 63 · unique after dedupe by public profile 61 · reactors 52 / commenters 9 · obfuscated/no-slug 52

## Resolvability
- actionable now: 9 (commenters — clean public profiles)
- actionable after resolution: +52 (reactor URNs require a resolution pass; ~85% of this pull)
- Honest volume: this is a 9-lead pull today, not a 61-lead pull.

## Scored Ledger
comment=3 · reaction=1 · +2 ICP-title match. Substantive reply > tag > emoji.
Each row carries its occasion — the post's subject in the post's own words.

## Residual Cost
52 URNs × [resolution $/lookup] → compare to expected value of fits inside them.
If resolution cost > EV at this volume: stop, work the 9.

## ICP Gate (before any enrichment spend)
fits / adjacent (what's missing) / out (why). Out exits free.
Only fits enter the cascade: 61 pulled → M qualified → M enriched.

## Cascade (from waterfall-design)
tier 1 (cheapest, most accurate) → residual → tier 2 → residual → tier 3
worked ladder: 50 → 32 (64%) → +10 of 18 (56%) → 8 residual ≈ 84% cumulative
stop rule at [residual N or $/hit]; validity check (good/catchall-risky/bad) before any send.

## Aperture Verdict
which monitored accounts produced fits vs noise → next roster revision.
```

---

## Judgment

| Dimension | Reference | Generated | Verdict |
|---|---|---|---|
| Pull-stat shape | raw / unique / reactor-commenter / obfuscated | same four stats, same order | **match** |
| Dedupe key | public profile ("duped by public profiles") | public profile | **match** |
| Obfuscation reality | 52/61 obfuscated, "normal for the reactions endpoint," resolution pass next | stated numerically + resolution branch + cost test | **match, extended** |
| Honest volume | implicit — he moves straight to resolution | explicit "9-lead pull today, not 61" | **extends the reference** |
| Gate placement | *"before it even does this enrichment… if it fits this customer profile, then it goes into this enrichment"* | gate upstream of tier 1, shown as N → M | **match** |
| Cascade math | 50 → 32 → +10 → 8, ~80% find rate | same ladder, 84% cumulative, cheapest-first by cost-per-hit | **match** |
| Verification | good / risky / bad before send | same, non-optional | **match** |
| Runtime/cost texture | "Sauntered for 34s", "$200 to get started" | per-run cost required; residual cost tested against EV | **partial** — costs are required, but no measured numbers exist yet for this niche |

### VERDICT: **PASS**

The generated artifact reproduces the reference's structure, its numbers, and — the discriminating test — **the failure mode you only learn by watching the terminal**: that reaction rows come back as obfuscated URNs and roughly 85% of an engager pull is not immediately actionable. A transcript-only or summary-level extraction would have shipped "pull the engagers, then enrich them" and silently overstated pipeline by ~5×. That single item is the strongest evidence the extraction went past surface.

It also passes the recognition test in `genius.md`: numbers arrive mid-sentence, judgment sits at exactly one step with the rest proven deterministic, and the artifact refuses to present a flattering number.

### Named gaps (why this ships A-minus, not A)

1. **Reference corpus is one source.** The standard blind pass wants ≥2 independently published artifacts. This bar is *sharper* than two blog posts (it's his own live execution), but it's narrower. Promotion to A requires a Farrice-judged pass against a real roster run.
2. **No measured hit rates for Farrice's niche.** The 64% / 56% / 84% ladder and the ~80% coverage heuristic are Cody's numbers from his segments. The workflows require marking day-one figures as estimates and replacing them after a month — correct handling, but it means the cost model is a template until `signal_scout.py` has produced real pulls.
3. **UNCONFIRMED carried forward**: the $22 LinkedIn CPM, the "80% niche surface-area coverage" heuristic, and the LinkedIn AI-slop detection feature. All three are flagged in `references/era-bound-2026-08-stack.md` and `extraction-report.md` Part IX rather than absorbed as fact.

### Conductor handoff
```
python3 execution/blind_pass.py record --expert cody-schneider-signal-outbound --verdict PASS \
  --notes "vs the source's own live demo (63 raw → 61 unique, 52 reactors/9 commenters, 52 obfuscated URNs) and the 50→32→10→8 waterfall ledger; held: pull-stat shape, dedupe key, gate-before-spend, cascade math, verification gate; extension: explicit honest-volume split. Gaps: single-source corpus, hit rates unmeasured for Farrice's niche." \
  --generated skills/cody-schneider-signal-outbound/workflows/engager-signal-audit.md \
  --reference extractions/cody-schneider-signal-outbound/watch/frames/frame_0071.jpg
```
- 2026-08-06T00:41:57 — **PASS** — eval: EVAL-062 — generated: `skills/cody-schneider-signal-outbound/workflows/engager-signal-audit.md` — reference: `extractions/cody-schneider-signal-outbound/reference-corpus/2026-gtm-engineering-claude-code-crash-course.md` — corpus: 2 piece(s) — vs the source's own live demo (63 raw → 61 unique, 52 reactors/9 commenters, 52 obfuscated URNs) and the 50→32→10→8 waterfall ledger; held: pull-stat shape, dedupe key, gate-before-spend, cascade math, verification gate; extension: explicit honest-volume split. Corpus: 2 solo-channel transcripts (skip-zapier, gtm-engineering) — voice/doctrine consistent with generated workflows. Gaps: single-source doctrine corpus, hit rates unmeasured for Farrice's niche.
