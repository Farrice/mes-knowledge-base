# PROVENANCE — bitbranding-fashion-shopify repair

Anchor → source file+location table for every quote/anchor added or referenced in this
repair. All entries confirmed by direct read of `extractions/BitBranding/transcript.txt`
(55,127 bytes, single-line raw transcript, `wc -l` = 0) during this session — not carried
forward from the pre-existing skill without re-checking.

| # | Anchor text (as it appears in the repaired genius.md) | Source location | Verified how |
|---|---|---|---|
| 1 | "I rebuilt Represent's collection page from scratch" | `extractions/BitBranding/transcript.txt` | Python exact-substring match against full file text |
| 2 | "No custom code, no expensive apps, nothing like that" | `extractions/BitBranding/transcript.txt` | Python exact-substring match |
| 3 | "hover effects, quick add, color swatches, how they make 127 products feel like something you can actually navigate" | `extractions/BitBranding/transcript.txt` | Python exact-substring match; quote stops before a `[music]` transcription tag that interrupts the sentence |
| 4 | "get rid of spacing in between products, get rid of spacing left and right on mobile, I would definitely do that" | `extractions/BitBranding/transcript.txt` | Python exact-substring match |
| 5 | "we want to connect it with the dynamic source and connect the image" | `extractions/BitBranding/transcript.txt` | Python exact-substring match — quote itself VERIFIED, the anti-pattern framing built on top of it is labeled LIKELY (inference, see source-ledger.md) |
| 6 | "I did try to do a couple things with the description to try to do the truncation, the read more read less" | `extractions/BitBranding/transcript.txt` | Python exact-substring match |
| 7 | "one of the reasons why I love Horizon. It's like they do give you all these little little things that you can manipulate" | `extractions/BitBranding/transcript.txt` | Python exact-substring match |
| 8 | "It's not custom code. Almost everything they're doing can be rebuilt on a standard Shopify theme for free" | `extractions/BitBranding/transcript.txt` | Python exact-substring match (source has a stutter "It's It's not custom code"; citable form uses the single clean "It's") |
| 9 | "maybe it was too much for for Sidekick to do" (used in Model Calibration section) | `extractions/BitBranding/transcript.txt` | Python exact-substring match |
| 10 | "is there a dynamic source? No... let's just try connecting the dynamic source" (used in Model Calibration section, paraphrase-with-ellipsis of two adjacent transcript beats) | `extractions/BitBranding/transcript.txt` | Both fragments — "is there a dynamic source? No" and "let's just try connecting the dynamic source and then doing what was it" — individually confirmed present near each other in the badge-configuration segment; joined with an ellipsis for readability, not presented as one continuous verbatim sentence |
| 11 | "Section → Collection heading → Image block → Dynamic source" (pre-existing, genius.md pattern 3, re-cited in Model Calibration section) | Not a literal transcript quote | UNCONFIRMED as verbatim — pre-existing extraction's compressed notation for a demonstrated click-path, not a spoken line. Flagged in source-ledger.md; left in place as pre-existing content, not re-verified as a direct quote by this repair. |

## Verification method (reproducible)

```python
text = open("extractions/BitBranding/transcript.txt", encoding="utf-8").read()
"<candidate quote>" in text   # True/False — used for every row above except #11
```

Run against every anchor before it was placed in genius.md. Row 11 was checked the same
way and returned False — it is called out as UNCONFIRMED rather than silently anchored.
