# Mission Card — Calibration Closure: arm the rubric (2026-07-24)
Tier: T2
Produced: 2026-07-24 (loop-engineering brief candidate 2 — Farrice all-12 GO)

## Objective (≈15 min of Farrice, nothing else)
Ratify pending eval entries in `evolution_store/ground_truth/eval_set_v1.jsonl`.
Status: **66/85 calibrated · threshold 68 · 2 net ratifications arm the judge.**
Arming flips `rubric_load_bearing: true` → the already-written R2 precedent gate
in `chain_runner.py` goes live with zero further code. Ratifying an entry
already in the set nets a FULL +1 (appending new rows raises the bar — don't).

## How (per entry, one of)
- **AGREE**: flip `"calibrated_by_human": false` → `true`, add
  `"human_calibration_notes": "<one-line felt verdict>"`.
- **ADJUST**: fix scores/verdict first (bimodal, narrow marginal band,
  −1/dim on real failures, when in doubt fail harder), then flip.
- **SKIP**: EVAL-011 is an unfilled placeholder — leave it.

After any 2+: `python3 execution/eval_harness.py status` → expect `"rubric_load_bearing": true`.
Protocol detail: `evolution_store/ground_truth/REVIEW-PROTOCOL.md`.

## The 19 pending (mostly your own blind-pass records needing a felt AGREE)
- **EVAL-011** [Content/TBD] "USER TO FILL: a recent finalize that scored 7.0-7.5 — the 'marginal pass' band" — proposed: intent None / expert None / adv None / factual None → composite None, verdict **TBD** | anchors: (none named)
- **EVAL-029** [Extraction/satori-graphics] "extract-forge on 5 Satori design-thinking videos -> executable creative-strategy" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **BLIND-PASS** | anchors: (none named)
- **EVAL-030** [System/fantastic-posters] "enrich fantastic-posters into a high-taste, non-redundant, multi-model image eng" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-032** [Extraction/claim-safe-health-marketing] "E5 harvest wave Target #1 -- build claim-safe/regulatory health marketing skill " — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP (B-tier)** | anchors: (none named)
- **EVAL-034** [Extraction/dara-denney-static-ads] "run /extract-forge on Dara Denney 'How I Make AI Static Ads' (5C5VhqW9HCc) + /wa" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP (B+/A-eligible)** | anchors: (none named)
- **EVAL-036** [Extraction/sean-dollwet-kdp-publishing] "blind-pass verdict for extraction 'sean-dollwet-kdp-publishing' (instrumented ri" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-037** [Extraction/jeremy-haynes-cold-offer] "blind-pass verdict for extraction 'jeremy-haynes-cold-offer' (instrumented ritua" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-040** [Extraction/jenny-hoyos-shorts] "blind-pass verdict for extraction 'jenny-hoyos-shorts' (instrumented ritual)" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-041** [Extraction/jenny-hoyos] "blind-pass verdict for extraction 'jenny-hoyos' (instrumented ritual)" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-046** [Extraction/nathan-gotch-ai-seo] "blind-pass verdict for extraction 'nathan-gotch-ai-seo' (instrumented ritual)" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-047** [Extraction/david-baldacci-books-that-sell] "blind-pass verdict for extraction 'david-baldacci-books-that-sell' (instrumented" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-048** [Extraction/oren-dara-ad-psychology] "blind-pass verdict for extraction 'oren-dara-ad-psychology' (instrumented ritual" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-049** [Extraction/jason-fladlien-marketing] "blind-pass verdict for extraction 'jason-fladlien-marketing' (instrumented ritua" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-050** [Extraction/paolo-trivellato-lead-magnet-engine] "blind-pass verdict for extraction 'paolo-trivellato-lead-magnet-engine' (instrum" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-051** [Extraction/ray-amjad-agentic-ladder] "blind-pass verdict for extraction 'ray-amjad-agentic-ladder' (instrumented ritua" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-052** [Extraction/satori-graphics] "blind-pass verdict for extraction 'satori-graphics' (instrumented ritual)" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-053** [Extraction/matthew-lakajev-linkedin] "blind-pass verdict for extraction 'matthew-lakajev-linkedin' (instrumented ritua" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-054** [Extraction/matthew-lakajev-linkedin] "blind-pass verdict for extraction 'matthew-lakajev-linkedin' (instrumented ritua" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
- **EVAL-055** [Extraction/riley-brown-marketing-automation] "blind-pass verdict for extraction 'riley-brown-marketing-automation' (instrument" — proposed: intent ? / expert ? / adv ? / factual ? → composite ?, verdict **SHIP** | anchors: (none named)
## Constraints
- T2: human judgment IS the deliverable — the runner must never execute this
  (human-optional review is a standing refusal in the integration brief).
- One sitting; density over completeness; stop at the felt verdict.
