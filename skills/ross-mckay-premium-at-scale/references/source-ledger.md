# Source Ledger — Ross McKay: Premium at Scale

Every factual/attribution claim used in `SKILL.md` and `genius.md`, labeled
VERIFIED / LIKELY / UNCONFIRMED against the only primary source in this
repo: `extractions/ross-mckay/transcript.txt` (podcast interview transcript,
116,706 bytes, 116,684 characters, confirmed via direct file read — not a
0-byte or missing file). Supporting extraction artifacts: `extractions/ross-mckay/extraction-report.md`
(9,201 bytes) and `extractions/ross-mckay/validation-report.md` (1,209 bytes).
The transcript carries no title card, upload date, or channel metadata in
the raw text; the interviewer is referred to in-line as "Maddie," and Ross
McKay names his prior company "Daring" and current company "Cadence"
himself. No independent second source (article, second transcript, or
external corroboration) exists in this repo for this expert — every VERIFIED
label below means "verbatim or near-verbatim in this one transcript," not
"cross-source confirmed."

## VERIFIED — verbatim or near-verbatim quote located in transcript.txt

| Claim | Transcript anchor (search string / approx. char offset) |
|---|---|
| "We're not going to win on capital. We're not going to win on resources. We're going to win on speed." | offset ~0–150 (opening lines) |
| Cadence positioned as sub-$3 / "world's first $2 luxury" beverage | offset ~150–350 |
| Cadence did "just under $10 million" in "600 days" | offset ~940–1010 |
| Next-year target discussed as "40 million" | offset ~1010, ~97707 |
| "I don't need you all to believe in me. I just need people to buy this at Target." | early section, near offset ~200–300 |
| Can redesign: same liquid, sales "three times" after a packaging-only change | opening section, ~200–500 |
| 500mg sodium formulation claim, contrasted against Gatorade (100mg) and "Barcode" (60mg) — McKay caveats "I'm using those example numbers, I don't actually know" | offset ~59450–59750 |
| Trade spend "20 to 30%" on top of "50 plus%" gross margin | offset ~19150–19450 |
| "Sold out 200 plus days" framed as "terrible problem," not a win, because daily-consumption brands can't afford stockouts | offset ~48088–48434 |
| "Don't think anyone's loyal... that's a massive mistake brands make" | offset ~49027 |
| "I think launching too many products... putting all your wood behind one arrow" | offset ~51998 |
| Brokers/distributors "one or of five guys" — direct distribution vs. distributor tradeoff | offset ~24623–25260 |
| "Don't go to sleep at night thinking that this guy girl is doing anything on your behalf... build your own sales team. I'm my own sales guy." | offset ~29660 |
| "Don't go into retail till you're ready for that scale" (unit-economics gate on retail entry) | offset ~21750–22550 |
| Natural/specialty retail (farmers markets, Sprouts, Whole Foods, Bristol Farms) framed as the obsolete/"obscure" route vs. convenience-led mass retail | offset ~22994 |
| Hiring generalists 0→10M, "spikes" from 10M→50M+, referencing Eric Glimman (Ramp founder) as the model | offset ~81704–82256 |
| Prior company named "Daring"; zero-to-100-person hiring arc discussed there | offset ~81376, ~34360 |
| DTC "sold out" hype vs. B2B/retail sold-out being a demand-planning failure that gets facings pulled | offset ~48088–51024 |

## LIKELY — consistent with transcript's throughline but not a single verbatim line

| Claim | Basis |
|---|---|
| "Anchor Customer" as a named framework term | McKay's actual language is about winning the retailer/PO before the distributor (verified in substance across offset ~24623–26073); "Anchor Customer" itself is the extraction's label for the pattern, not his spoken term. |
| "Shelf-Test Simulation" and "SKU Scythe Protocol" as named signature moves | Grounded in verified substance (packaging-vs-shelf decision at the transcript's opening; single-SKU focus at offset ~51998) but the move *names* are extraction-authored shorthand, not McKay's own phrasing. |
| Precise "30–50%" timeline-compression figure in the Signature Moves table | Consistent with McKay's stated speed obsession (offset ~0–150) but no single transcript line states a 30–50% range; treat the number as illustrative, not a McKay quote. |

## UNCONFIRMED — no locatable transcript support

| Claim | Note |
|---|---|
| Exact source video title, publish date, host/channel name | Not present anywhere in `transcript.txt`; no metadata file accompanies it in `extractions/ross-mckay/`. Do not present a specific episode title or air date as fact. |
| "On Running" comparison as a named example of a brand that achieved premium-at-scale | The string "On running" appears twice in the transcript (offset ~1935, ~61411) confirming the topic is discussed, but the exact framing/claim attributed to it in any downstream content should be checked against the live context before being asserted as McKay's verbatim assessment. |

## How to extend this ledger
When a new claim is added to `SKILL.md`, `genius.md`, or a workflow file,
grep `extractions/ross-mckay/transcript.txt` for the closest distinctive
phrase before labeling. If no hit, label UNCONFIRMED — never silently drop
the label or assume absence without the grep.
