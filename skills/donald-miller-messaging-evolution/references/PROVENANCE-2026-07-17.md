# PROVENANCE — donald-miller-messaging-evolution repair

All anchors below verified by direct string search against the actual source file
(`extractions/Donald Miller/transcript.txt`, 44,426 bytes, confirmed via `wc -c` —
not 0-byte, not unrecoverable). No quotes were invented; every anchor quote below
was located verbatim (or near-verbatim, transcript disfluencies like "Mhm"/"Yeah"
elided) in the source file before being written into genius.md.

| Anti-pattern | Quote used | Verified at (char offset in transcript.txt) |
|---|---|---|
| The completeness trap | "If you say all the stuff that you say on the fourth date on the first date, they're not going to go out with you again." | ~6211 |
| Lane flooding | "They smell money on the other side of the fence..." / "Have you figured out something to sell the 9,950 people you can't hire?... Nope, we're staying in here." | ~9496 / ~18012 |
| Word-clinging | "What don't you like about the word virtual? I feel like it undermines the human element and quality of person." / "We are modern staffing for you... that is a high cognitive load message." | ~27584-27738 / ~7043 |
| Customer-only optimization | "When we reduced the cognitive load on our internal team and on the customer, sales went up." | ~37056 |
| Rebrand impatience | "You should not expect the ship to be righted for 3 years. And also 3 years only if you're aggressive. Only if you're constantly saying it." | ~24156 |
| Spec-sheet persuasion | "They just didn't think the quality was going to be there with a battery... a hockey stick happened in sales... when they started calling their electric tools fuel." | ~29223-29284 |
| One-and-done messaging | "Play with your messaging until you find something that works. And keep going. And keep going." / "We would be antiquated Blockbuster... We must constantly innovate." | ~39261 / ~242 |

## Note on a provenance gap found during repair (not in my failing-checks scope, flagged honestly)

`references/source-quotes.md` and `genius.md`'s opening Sources block both cite a
"Source 3 — PRIMARY" published book, *How to Grow Your Small Business* (Donald
Miller, HarperCollins Leadership, 2023), as the origin of several quotes: the
6-part sales color key, the S-curve, the rule of proportion, "kill your darlings,"
the product brief, and the "at-home chef" example. I searched both actual
extraction files in this repo (`extractions/Donald Miller/transcript.txt`, 44,426
bytes, and `extractions/Donald Miller Grow/transcript.txt`, 45,960 bytes) for the
distinctive phrases from every one of those quotes ("color key," "three-step plans
work well," "kill your darlings," "product brief," "s-curve," "rule of
proportion," "Beware of looking successful," "professionalize your operation,"
"wind tunnel," "at-home chef," "Close the Client Kit," "Fully Booked") — zero
matches in either file. No book file exists anywhere under `extractions/`. This
means the "Source 3" material is currently **UNCONFIRMED against any file in this
repo** — it may be accurately transcribed from the real book (which is a real,
purchasable title), but there is no local source file to verify it against. This
is outside my two assigned failing checks (anti_patterns_sourced, recognition_test)
so I did not touch source-quotes.md, but flagging it per the envelope's
unforgivable-failure rule rather than staying silent.
