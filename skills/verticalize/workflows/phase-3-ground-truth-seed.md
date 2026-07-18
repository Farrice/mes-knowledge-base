# Phase 3 — Ground-Truth Seed

**Duration**: variable — gated on user PASS, not on generation speed. Only fires after an explicit `continue` verdict from Phase 2.5.

## Required inputs

Approved ICP master + voice document from Phases 1-2, plus 0-3 `--reference-creator` URLs supplied at kickoff.

## Steps

1. Register the domain:
   ```bash
   python3 execution/ground_truth.py init-domain <slug> \
       --description "<from Phase 0 capture>" \
       --expert "<owner or reference creator>" \
       --output-type "<deliverable type 1>" \
       --output-type "<deliverable type 2>"
   ```
   `execution/ground_truth.py:init_domain` writes to `knowledge/expert-benchmarks/_registered_domains.json` and raises `ValueError` if the slug is already registered or the description is blank — this is the same file every prior registered vertical lives in (as of this repair pass, that file is `{}` — no vertical has completed this phase in production yet).
2. For each `--reference-creator`, invoke `/extract` to pull high-signal samples into `extractions/<slug>/`.
3. From extractions + the voice document, generate candidate seed samples and register each one only after user approval:
   ```bash
   python3 execution/ground_truth.py add <slug> <sample-file> \
       --expert <name> --type <output-type> \
       --notes "Seed sample; PASS per Farrice taste"
   ```

## Output Schema

- **`knowledge/expert-benchmarks/_registered_domains.json`** — the new domain entry (slug, description, experts, output_types, `registered_via: "init_domain"`, `registered_at` date).
- **`extractions/<slug>/`** — raw reference-creator samples, if any were supplied.
- **`knowledge/expert-benchmarks/<slug>/samples.json` + exactly 5 `sample-NNN.md` files** — each one carrying an explicit user-approved PASS note, not an auto-generated one. Fewer than 5 approved samples is not a partial pass; it is a failed phase.

## Quality Gate

Before advancing to Phase 4:
- [ ] Domain registered in `_registered_domains.json` with a non-blank description
- [ ] Exactly 5 (not fewer) samples carry an explicit user-approved PASS note in `--notes`
- [ ] Each sample's `--type` matches one of the `--output-type` values registered in step 1 — no orphaned sample types
- [ ] If reference-creator extraction was used, `extractions/<slug>/` exists and the samples are traceable back to it

Per SKILL.md's Anti-pattern #3 and this phase's own stop condition: "If fewer than 5 samples reach user-approved PASS, halt. Don't ship a vertical with under-calibrated ground-truth." A domain with 4 samples calibrates its future quality gate against noise, per the same 2026-05-03 grade-inflation finding that makes Phase 2.5 non-skippable.
