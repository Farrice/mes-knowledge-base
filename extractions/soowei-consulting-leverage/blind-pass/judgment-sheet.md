# SooWei A-Tier Blind Judgment Sheet

Status: **SUPERSEDED BY RANDOMIZED REVIEW SURFACE**

Open [`review/judgment-sheet.md`](review/judgment-sheet.md). Do not open `.sealed-mapping.json` before recording both pair judgments and the final verdict.

The rubric below is retained as the pre-assembly template only.

## Pair 1 — Content Operation

Preferred: A / B / TIE  
Identified as real SooWei: A / B / UNSURE  

| Criterion | A | B | What gave it away? |
|---|---:|---:|---|
| Diagnoses the founder bottleneck before prescribing roles | /10 | /10 | |
| Connects marketing, sales, fulfillment, and attribution | /10 | /10 | |
| Assigns work by leverage rather than adding a generic team | /10 | /10 | |
| Protects founder-only judgment while systematizing execution | /10 | /10 | |
| Feels direct, specific, and underexplained rather than consultant-polished | /10 | /10 | |

## Pair 2 — Trust and Proof

Preferred: A / B / TIE  
Identified as real SooWei: A / B / UNSURE  

| Criterion | A | B | What gave it away? |
|---|---:|---:|---|
| Uses proof while refusing unsupported outcome promises | /10 | /10 | |
| Treats mistakes, refunds, and limitations as reputation decisions | /10 | /10 | |
| Separates credibility infrastructure from attention spectacle | /10 | /10 | |
| Preserves the expert's confrontational but self-implicating texture | /10 | /10 | |
| Makes one clear trust decision instead of reciting every framework | /10 | /10 | |

## Recognition Test

Would SooWei recognize the generated decisions as his—or as someone repeating his vocabulary with the labels still on?

Verdict: PASS / FAIL  
Weakest tell:  
One repair, if needed:  

## Promotion Decision

- **A-tier PASS:** generated work is indistinguishable or preferred, generation receipt is clean, and Farrice explicitly approves.
- **FAIL → one retry:** name the weakest tell, patch only that criterion, regenerate once from fresh context.
- **B-tier hold:** if the retry still fails, preserve the gap and do not promote.

Recording command after—not before—Farrice's decision:

```text
python3 execution/blind_pass.py record --expert soowei-consulting-leverage --verdict PASS|FAIL --notes "[Farrice judgment and tell]" --generated "[candidate path]" --reference "[matching reference path]"
```
