# SooWei Blind Assembly Receipt

Status: **READY FOR HUMAN JUDGMENT**

- Source-integrity audit: PASS for corpus use.
- Clean-room generator access audit: PASS; only the sealed packet and six authorized skill files were read.
- Clean-room task: `01a06dad-1cd2-76f1-aa55-e4ef3f168c56`.
- Preserved generator commit: `3d233a1168340bf0485642bbe0120dda4615f4cc`.
- Comparison form: normalized spoken transcript versus normalized spoken transcript.
- Randomization: independent cryptographic A/B draw for each pair.
- Identity mapping: sealed in `../.sealed-mapping.json`; do not open before recording the verdict.
- Integration: held; all work remains on the isolated `codex/soowei-organic-content-v2` lane.

## Neutral Normalization

Only presentation artifacts were removed: provenance headers, timestamps, the acquisition-only `Transcript` label, generated speaker-name prefixes, and generator receipts. Whitespace was collapsed and every sample was wrapped to the same width. Substantive wording and order were preserved.

## Public Sample Receipt

| Pair | Sample A words | Sample B words | A hash prefix | B hash prefix |
|---|---:|---:|---|---|
| Pair 1 | 2221 | 2467 | `9e485ecabb5d` | `a5b8f5d63a77` |
| Pair 2 | 2501 | 2541 | `477faeb0a090` | `c02a8d3f0eae` |
