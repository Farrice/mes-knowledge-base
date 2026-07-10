# Gate Record — 02-THE-PLAY.md

Operator-only. Not client-facing. Traces the review pass and every fix applied 2026-07-08.

---

## Source review

Three findings sets: IMPLEMENTABILITY (60-second test / card anatomy), VOICE (ai-slop-detector + structural bans), FACT ACTIONS (claim-to-Receipts trace). Full findings supplied inline in the applying prompt, not duplicated here.

## IMPLEMENTABILITY — applied

- **MUST-FIX (Card 2 was a mindset lecture, no physical action).** Replaced "Aim the enemy at the hype, not at fitness" with "Search your page for 'no one cares about abs' and delete it" — an actual find-and-delete card with a binary done-when. The retained principle ("point at the hype, never at the guy") moved to a `Not now` bullet as a writing rule, since it governs future copy, not tonight's task.
- **MUST-FIX (Not-now contradicted cards 3-6).** Picked interpretation (a): the booking page and booking button already work today: leads can book a Triage on it now. Added a one-line clarifier up top and rewrote the `/book-in-person` Not-now bullet to state it's a separate, later project that doesn't block the print run. This was a judgment call in the operator's absence — flag to Cooz that this is the assumed sequence; if the booking page is in fact not live, cards 5-6 (printing, scoreboard) need to move to Not-now instead and this doc needs a second pass.
- **SHOULD-FIX ("squeeze page" jargon).** Replaced with "booking page" everywhere (banner, card 3 header/body, card 4 body, Not-now section). Also reworded Card 4's header off "callout line" to "Swap the next line that makes the same mistake."
- **SHOULD-FIX (Card 5 missing print asset).** Named the actual file: `04-visuals/flyer-4x6-variant1.svg` (confirmed present on disk), plus the print specs already documented in `01-flyer/FLYER-COPY-AND-SPEC.md` (300 DPI, CMYK, 0.125" bleed, vector QR). Card now tells Cooz exactly what to hand the print shop instead of pointing at a go-deeper link for the asset itself.
- **MINOR (Card 1 "pick" felt cosmetic).** Added one sentence to Why-it-matters tying the pick to downstream cards: Line A becomes the page headline, Cards 3-4 are the body copy under it.
- **MINOR (Card 6 Done-when mixed proof with go/no-go logic).** Done-when now tests only the card's own action (table screenshot saved). The go/no-go thresholds moved to a plain note under the table, unchanged in substance.

## VOICE — applied

- **HIGH (Card 2 negation-reveal, "isn't at X. It's at Y.").** Removed by rewriting Card 2 entirely (see above) — the sentence no longer exists in the doc.
- **MEDIUM (opening "Not the idea. One sentence." double-beat).** Flattened to "The idea was right. One sentence was off."
- **LOW (Card 4 second negation-reveal, clustering with the HIGH one).** Since the HIGH instance was removed, this one was still de-shaped per the reviewer's conditional note (fixing 28 alone would still leave two matching shapes in-doc) — "Not because they're weak. Because nobody built them..." → "They're not weak. Nobody built them a version that survives a real week."
- **LOW (Card 4 "A six-pack is real. It just isn't...").** Left unchanged per reviewer's explicit guidance — with the other two instances de-shaped, this one reads as in-voice, not a pattern.
- **LOW (Line A tagline "Come for X, stay for Y").** Left unchanged — reviewer flagged as a deliberate, labeled choice, not a defect.

## FACT ACTIONS — applied

All four claims traced VERIFIED against `CONCEPT-V2-MARKETABLE.md` and `STRATEGY-SPINE.md` with no substance changes required. One precision fix applied: the Bookings row said "clicks that turn into a booked Triage" but the underlying 0.6%/3-of-500 anchor is against **cards distributed**, not clicks — reworded to "cards that turn into a booked Triage" to match the source anchor. Added one line noting Scans/Closes thresholds are first-batch calibration targets (source tags them `[ASSUMPTION]`; translated per the doc's zero-jargon law to "our best guess for the first batch").

## Prose classifier

`python3 execution/prose_classifier.py check 02-THE-PLAY.md` post-edit: **WARNING, AI score 2/10**, single signal `parallel_structure_overuse` (10 blocks), rhythm CV 1.04 (varied/human-like), zero banned-vocabulary/hedging/transition/opener hits.

Reviewed and dismissed: the parallel-structure detector flags 3+ consecutive lines sharing a first token. Every hit here is markdown checklist rows (`[ ] verb...`) required by `DOC-FORMAT-SPEC.md`'s card anatomy — same false-positive class already logged and dismissed in `01-flyer/FLYER-COPY-AND-SPEC.md`'s own audit notes for its print-spec table rows. No prose rewrite applied; converting the checklists to non-parallel prose would break the card format the spec mandates.

## Declined / not applied

None. Every MUST-FIX and SHOULD-FIX from IMPLEMENTABILITY, every MINOR, every non-conditional VOICE finding, and the FACT ACTIONS precision fix were applied.
