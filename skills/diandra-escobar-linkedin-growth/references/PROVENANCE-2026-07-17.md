# PROVENANCE — diandra-escobar-linkedin-growth repair (Wave 3, 2026-07-17)

Anchor → source file + location, for every new or newly-sourced claim added in this repair. Full claim-by-claim status (VERIFIED/LIKELY/UNCONFIRMED) for the *entire* skill, not just what changed, lives in `references/source-ledger.md`.

| Anchor added | Source file | Location / exact string |
|---|---|---|
| Model Calibration example: "$4.8M in 2 years" | `skills/diandra-escobar-linkedin-growth/references/hook-writing-rules.md` | Rule 4 (pre-existing, unmodified — cited as an example, not a new claim) |
| Model Calibration example: "293 comments, 234 reposts, 28,000 impressions" | `skills/diandra-escobar-linkedin-growth/genius.md` | Hall of Fame Exemplar 2 (pre-existing; ledger labels this UNCONFIRMED as a factual claim — cited here only as an illustration of her register, not asserted as verified fact) |
| Anti-Pattern 9 quote: "LinkedIn doesn't render by characters, it renders by pixels" | `extractions/Diandra Escobar/transcript.txt` | Mid-transcript, the "technical part we get wrong" section on pixel-width rendering. Verified via exact-string Python search. |
| Anti-Pattern 10 quote: "The punchy line should provoke. The context line earns the click." | `extractions/Diandra Escobar/transcript.txt` | Format 2 (Punchy + Context) breakdown, immediately after "the mistake we see constantly with this format." Verified via exact-string search. |
| Anti-Pattern 11 (new) quote: "the problem is their first line is always soft, vague, throat-clearing sentences that don't really do anything" | `extractions/Diandra Escobar/transcript.txt` | Opening section, right after "I'll see people write genuinely brilliant posts." Verified via exact-string search. |
| Anti-Pattern 12 (new) quote: "If a reader can't predict the rhythm, the structure fails" | `extractions/Diandra Escobar/transcript.txt` | End of Format 4 (Stacked) breakdown. Verified via exact-string search. |
| Anti-Pattern 13 (new) quote: "A bad theft degrades. skims, steals from one, plagiarizes, imitates, and rips off" | `extractions/diandra-escobar/transcript.txt` | Early in the "good theft vs. bad theft" framing, right after "There's a difference between a good theft and a bad theft." Verified via exact-string search. |
| Anti-Pattern 14 (new) quote: "Everyone was posting the same stuff, myself included" | `extractions/diandra-escobar/transcript.txt` | "6 months in, something shifted" section. Verified via exact-string search. |
| Recognition Test criteria (post-type declared before copy, pixel-width budget, real-entity growth posts, builder-with-receipts language) | `skills/diandra-escobar-linkedin-growth/genius.md` | Synthesized from Pattern 5, Pattern 19, Pattern 1, and the Core Genius "$1M revenue" line (itself VERIFIED — see source-ledger.md) — no new factual claim introduced, only a test built from already-anchored patterns |
| Header version bump note "v4.2 repair (2026-07-17)" | This repair | Self-referential — documents the repair itself, not a claim about Diandra |

## Verification method

Every quote above was checked with a Python exact-substring search (`quote in transcript_text`) against the actual file contents, not recalled from memory or re-typed from the existing genius.md prose (which in several places lightly paraphrases the transcript). Two anti-patterns (9 and 10) already existed pre-repair with no source anchor; this repair added the anchor without changing the claim itself. Four anti-patterns (11-14) are net-new list items, each built around a verbatim quote found first, then written up — quote-first, not claim-first, per the envelope's "unforgivable failure is invented provenance" rule.

Two claims that were floated during drafting and then DROPPED because they could not be verified:
- Considered sourcing Anti-Pattern 7 ("Just Start Fallacy") to the "131 hooks from 21 creators" research framing — rejected because the anti-pattern's specific language ("researching competitors... ICP behavior") does not match anything in either transcript; left unsourced rather than force a weak connection.
- Considered quoting "AI can only think within a box" from `extractions/Diandra Escobar/transcript.txt` as a clean VERIFIED anchor for Hidden Knowledge's "AI Thinks Inside the Box" — the exact phrase is present, but genius.md's existing quoted text merges it with a separate nearby sentence ("Your job is to think outside it"), so the ledger labels this LIKELY, not VERIFIED, rather than upgrading a paraphrase to a verbatim citation.
