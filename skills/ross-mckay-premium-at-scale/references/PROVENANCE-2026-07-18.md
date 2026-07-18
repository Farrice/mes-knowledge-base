# Provenance — ross-mckay-premium-at-scale repair

Ground truth: `extractions/ross-mckay/transcript.txt` (116,706 bytes, verified
via direct read + `wc`/`ls -la`, not empty/missing) plus
`extractions/ross-mckay/extraction-report.md` (9,201 bytes) and
`validation-report.md` (1,209 bytes). No second independent source exists in
this repo for Ross McKay (`ls extractions | grep -i mckay` → one directory only).

| Anchor (in repaired genius.md) | Source file + location |
|---|---|
| "We're not going to win on capital... win on speed" | transcript.txt, offset ~0–150 |
| "$10 million" in "600 days," "40 million" next-year target | transcript.txt, offset ~940–1010, ~97707 |
| 500mg sodium vs. Gatorade 100mg / "Barcode" 60mg | transcript.txt, offset ~59450–59750 |
| Trade spend "20 to 30%" / "50 plus%" gross margin | transcript.txt, offset ~19150–19450 |
| "Sold out 200 plus days... terrible problem" | transcript.txt, offset ~48088–48434 |
| "Don't think anyone's loyal... massive mistake" | transcript.txt, offset ~49027 |
| "Launching too many products... one arrow" | transcript.txt, offset ~51998 |
| "One or of five guys" (distributor line) | transcript.txt, offset ~24623–25260 |
| "Build your own sales team. I'm my own sales guy." | transcript.txt, offset ~29660 |
| "Don't go into retail till you're ready for that scale" | transcript.txt, offset ~21750–22550 |
| Natural/specialty retail as obsolete route | transcript.txt, offset ~22994 |
| Generalists → "spikes," Eric Glimman/Ramp reference | transcript.txt, offset ~81704–82256 |
| "Daring" as prior company | transcript.txt, offset ~81376, ~34360 |

All offsets are approximate Python-string char positions confirmed by direct
`python3` slicing of `transcript.txt` at repair time — not estimated or
guessed. Full detail + VERIFIED/LIKELY/UNCONFIRMED labels:
`references/source-ledger.md` in this output directory.
