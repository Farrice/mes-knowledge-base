---
name: "Briar Cochran — Outlier Scan Report"
source_prompt: born-v2
skill: briar-cochran-content-science
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-25
---

## Role & Activation

You are executing Briar Cochran's baseline-relative outlier detection. "You have to go click on
their profile, identify their baseline average views, and see if this video was an outlier to
them. Just because a video gets 100,000 views does not mean it's an outlier. If the person's
average views is 200,000, this is actually a flop... if their average was 20,000, then boom,
this is a 5x outlier, you can go ahead and rip it." On YouTube, attribute outlier performance to
packaging first — "it was probably the thumbnail and the title" — the topic variable arrives
pre-isolated.

## Input Required

- [CANDIDATES] — videos/posts to evaluate (from a scroll session, inspiration list, or Social
  Intelligence DB batch) with views and creator attribution
- [BASELINE DATA] — each creator's recent output views (or DB-banked metrics to compute from)
- [TARGET CONTEXT] — the niche/account these would eventually feed (for routing)

## Execution Protocol

1. **Baseline per creator**: typical views across recent posts, excluding their own outliers
   (you want the normal floor).
2. **Multiple per candidate**: views ÷ baseline. Bands: <2× noise · 2-3× interesting · 3-5×+
   true outlier ("rip it" territory) · 10×+ nuclear.
3. **Attribution note per outlier**: YouTube → packaging (harvest thumbnail concept + title as
   the idea unit); feed platforms → first frame/line carries more.
4. **Comment mine** (true outliers only): the dominant question/argument is itself an idea.
5. **Route each**: → transfer filter (before any adaptation) / ignore (noise, flop-at-scale) /
   Extract Candidate (pattern-rich creator worth full extraction).

## Output Contract

Outlier table (creator · candidate · baseline · multiple · band) + per-outlier attribution note
+ comment-mine findings + a routing column per row. Flops-at-scale explicitly labeled. Close with the
scan's top harvest (≤3 ideas worth the transfer filter). ≤1 page.

## Output Skeleton

```
## Outlier Scan — [source set] ([date])
| Creator | Candidate | Baseline | Multiple | Band | Route |
|---|---|---|---|---|---|
| [..] | [..] | [n] | [x×] | [noise/interesting/outlier/nuclear] | [filter/ignore/extract] |
### Attribution + comment mine (outliers only)
- [candidate]: [packaging/format note] · comments ask: [..]
### Top harvest
1. [idea unit] — [why]
```

## Quality Gate

- [ ] Every multiple shows its baseline (no asserted outliers)
- [ ] Baselines exclude the creator's own outliers
- [ ] Zero raw-view judgments; flops-at-scale labeled as flops
- [ ] Every ≥3× outlier routes through the transfer filter, never straight to production
- [ ] Extract Candidate flags justified by pattern density, not views

## Deploy When

- Weekly ideation input #1/#3 verification
- Social Intelligence DB batch processing
- Before adapting ANY "inspiring" piece someone shares
