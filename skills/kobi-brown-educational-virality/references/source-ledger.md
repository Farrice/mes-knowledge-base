# Source Ledger — kobi-brown-educational-virality (repair pass, Wave 3 Lane 4 Batch 8)

> This skill's `references/source-quotes.md` and `references/validation-report.md` already
> satisfy the `source_ledger` heartbeat check (it PASSED pre-repair). This file is additive:
> it documents the specific sources used to add anchors to the genius.md Anti-Patterns
> section during this repair.

## Ground Truth Used
| Source | Path | Size (wc -c) | Status |
|---|---|---:|---|
| Full interview transcript | `extractions/kobi-brown-educational-virality/transcript.txt` | 34,664 | VERIFIED — read directly |
| Timestamped transcript | `extractions/kobi-brown-educational-virality/transcript-timestamped.txt` | 35,696 | VERIFIED — used to confirm timestamps below verbatim |
| Verbatim quote bank | `skills/kobi-brown-educational-virality/references/source-quotes.md` | n/a | VERIFIED — pre-existing, all quotes traced to transcript |
| Skill's own source ledger | `extractions/kobi-brown-educational-virality/source-ledger.md` | 3,450 | VERIFIED — confirms 2026-06-14 capture, yt-dlp en-orig auto-captions |

No absence claim was made for this skill — extraction sources are substantial (34.6KB
transcript) and were read directly, not assumed thin.

## Anti-Pattern Anchors Added (genius.md) — Claim-by-Claim
| Anti-pattern (abbreviated) | Anchor quote | Timestamp | Verified against transcript-timestamped.txt line | Status |
|---|---|---|---|---|
| Teaching before curiosity exists | "sneak the vegetables in education...my goal" | [16:40]/[17:48] | Pre-existing in source-quotes.md §Education vs. Entertainment | VERIFIED |
| Watering down the idea | "present real serious hard physics...earns the audience's attention" | [17:48] | Pre-existing in source-quotes.md | VERIFIED |
| Clickbait/conspiracy as default lever | "dive into conspiracies...clickbaity content...divisive commentary...easy, cheap way to draw attention" | [17:03] | Confirmed verbatim at transcript-timestamped.txt line 97 | VERIFIED |
| Claiming legitimacy instead of earning it | "I'm not being like 'Hey guys, I'm a physicist, you can trust me.'" | [13:37] | Confirmed verbatim at transcript-timestamped.txt line 79 | VERIFIED |
| Mistaking proximity for accuracy | "Going to NASA doesn't necessarily grant you accuracy and legitimacy" | [14:00] | Pre-existing in source-quotes.md | VERIFIED |
| Competing on a copyable craft edge | "with generative AI...barriers to entry are being lowered...conscious thing trying to separate myself" | [13:15] | Pre-existing in source-quotes.md | VERIFIED |
| Padding a short idea into long-form | "taking ideas that could be good for a short-form and just leaving them as a short-form" | [26:08] | Pre-existing in source-quotes.md | VERIFIED |
| Milking a trend past the honest version | "I could have got a few extra million views...by making follow-ups and four or five videos...crosses the line" | [24:40] | Confirmed verbatim at transcript-timestamped.txt line 137 | VERIFIED |
| Over-polishing a meaning piece | "a bit rough around the edges, which on YouTube sometimes I think is good" | [31:00] | Pre-existing in source-quotes.md | VERIFIED |
| Treating short-form virality as the end state | "top of funnel for your overall content and to bring new people into your audience" | [23:32] | Pre-existing in source-quotes.md | VERIFIED |

No UNCONFIRMED labels were required — all 10 anti-pattern anchors trace to verbatim quotes
already captured in `references/source-quotes.md` and independently spot-checked (3 of 10)
against the raw timestamped transcript line-by-line.
