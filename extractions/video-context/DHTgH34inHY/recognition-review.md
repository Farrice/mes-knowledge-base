# Godin Recognition and Blind-Pass Review

## Corpus Gate

`python3 execution/blind_pass.py prepare --expert seth-godin-marketing-mind` passed against two existing, provenance-verified Seth Godin blog pieces:

- “Is it okay if I share my screen?”
- “Two kinds of word salad”

These are the only existing Godin reference-corpus pieces in the repository. They belong to the marketing-mind extraction but are valid cross-layer recognition references for the same expert.

## Recognition Judgment

The generated `recognition-sample.md` preserves the recognizable operating shape:

- one clean distinction rather than a framework recital;
- short, unhedged sentences;
- a concrete responsibility boundary;
- the smallest viable audience and observed return behavior;
- no invented Godin quote, biography, or numerical claim;
- an ending that returns agency to the reader.

## Weakest Criterion and One Repair

**Weakest criterion:** the first sample was more abstract than the two corpus pieces, which both make their argument through a specific medium and moment.

**Single repair:** added the claim-safe-brief example: inventory and citation checking may be delegated; brand promise and review signature may not. No other section was rewritten.

## Fresh-Context Blind Verdict

A read-only reviewer with no parent context received three neutral files: the repaired candidate and the two frozen corpus pieces. The reviewer was not given the implementation, prior tier, source labels, or build history.

- Generated-piece identification: candidate correctly identified with **98% confidence**.
- Blind-pass verdict: **FAIL** under the “indistinguishable from or preferred to the real pieces” rule.
- Strongest match: ending discipline; the close returns cleanly to the governing idea.
- Weakest criterion: internalized judgment versus imitation. The polished symmetry, abstract imperatives, and conspicuous claim-safe example made the candidate feel engineered.
- Implementation change during blind review: **none**; `recognition-sample.md` remained frozen.

The result was recorded as `EVAL-067` in `evolution_store/ground_truth/eval_set_v1.jsonl` and in `extractions/seth-godin-marketing-mind/blind-pass-log.md`.

## Honest Tier

**B — practitioner-ready, but detectably generated.**

A-tier is not earned. The fresh blind reviewer failed the indistinguishability bar, and `directives/embodiment-standard.md` reserves A-tier promotion for a Farrice-judged blind pass even when a model reviewer passes.
