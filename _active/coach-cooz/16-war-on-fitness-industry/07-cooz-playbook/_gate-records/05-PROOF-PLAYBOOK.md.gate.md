# Gate Record — 05-PROOF-PLAYBOOK.md

Review-and-fix pass. This record stays in Receipts; it is never referenced from the client-facing card.

---

## IMPLEMENTABILITY — MUST-FIX (both applied)

1. **Card 2 missing assets (Buzz/Johnny/Melissa quotes not on the card).** Pulled the three verbatim testimonials from `03-testimonial-weaponization/RAW-PROOF-INVENTORY.md` (#3 Melissa, #11 Buzz, #33 Johnny) and printed them inline under Card 2 as a labeled "Buzz, Johnny, Melissa, verbatim:" block, matching Card 1's "The 5, verbatim:" convention. Excerpted with `...` the same way Card 1's five quotes are excerpted (full text is longer; trimmed to the same clauses PLAN.md §2 already uses to describe each). Coach can now execute the IG and Google Business steps without leaving the card.
2. **"Squeeze page" jargon in the banner and Card 2.** Replaced every instance with "landing page" — Cooz's own term for it in his raw voice memo (`00-strategy/RAW-MEMO-2026-07-08.md`) and the term `00-strategy/STRATEGY-SPINE.md` already uses. Fixed in the After-this banner, Card 1's Why-it-matters line, and Card 2's first checkbox.

## IMPLEMENTABILITY — SHOULD-FIX / LOW (not applied this pass)

Left as-is per scope (Jessica in/out vs. in/swap consistency, "already built/already locked" checkbox phrasing, GBP spell-out, "Log ... verbatim, dated" destination, banner's "5 quotes locked" vs. Jessica-pending overstatement, em-dash attribution count). None block tonight's execution; flagging here so a future pass can pick them up without re-deriving them.

## FACT ACTIONS — DRIFTED (all three applied)

1. **"Forty-two people" → "Forty-two testimonials"** (both instances, lines ~77 and ~85). PLAN.md §5's own gate record already corrected this exact drift once — duplicate authors exist across sources (Robin x3, Johnny/Kimmi/Sam/Mario x2 each, plus non-clients like McBroom) — so "42 people" overstates distinct individuals and invites a skeptic's challenge. Reverted to the corrected phrasing.
2. **"Falling out last July" → "falling out back in July 2024."** Source (`RAW-PROOF-INVENTORY-V2.md` §1b, quoting Cooz's own backstory doc) dates the falling-out to July 2024. "Last July" reads as July 2025 relative to the doc's current date; fixed to an unambiguous date.
3. **Robin father-disclosure flag — added.** `06-market-truth/CONCEPT-V2-MARKETABLE.md` §3b-D and `03-testimonial-weaponization/RAW-PROOF-INVENTORY-V2.md` §1a/§2 both flag that Robin is Cooz's father and that an undisclosed-parent testimonial is a live integrity landmine if a skeptic connects it — the live site version already runs this quote undisclosed. The doc had dropped this entirely and instead discussed *strengthening* Robin's quote without surfacing the disclosure question. Added one paragraph directly under Robin's swap note in Card 1, framed as a flag-not-a-block per the standing "flag, never cage" rule: names the risk, leaves the call to Cooz, does not stall the rest of the card.

## FACT ACTIONS — VERIFIED (no change)

Locked-5 quotes, operational anchors (Celine/wedding-couple ask, Buzz-for-Robin swap, IG top-8, Yelp four names, ask/consent scripts), the held-back Robin LinkedIn upgrade, and the "Not now" open items (Roni/Veronica, Ish/Ismael, Brian's release, unlabeled Drive folders, untranscribed Robin audio) all traced cleanly to PLAN.md / RAW-PROOF-INVENTORY(-V2).md / CONCEPT-V2-MARKETABLE.md. No text changes.

## VOICE

Not in scope for this pass per the run instruction (MUST-FIX/MUST-CUT + prose_classifier only). The reviewer's HIGH note — line ~36's "turns proof into a liability... turns proof into trust" engineered-antithesis — was not rewritten. Flagging it here for whoever takes the next pass: it's the single most-copied AI structure and worth a rewrite to something concrete and asymmetric before this doc is treated as final-final.

## prose_classifier — rerun after fixes

```
Verdict:    WARNING
AI Score:   2/10
Words:      1127
Signals:    1
Rhythm CV:  0.67 (varied)
DETECTED PATTERNS:
  [2.0] parallel_structure_overuse — 12 parallel blocks found
```

Traced all 12 flagged "parallel blocks" line-by-line: every one is a markdown checklist bullet (`- [ ]`) or a blockquote line (`>`) sitting three-or-more in a row — i.e., the card's own checklist and inline-verbatim-quote structure, which DOC-FORMAT-SPEC mandates ("Do it" checklists, "Assets sit inline"). Zero hits on banned vocabulary, hedging, AI transitions, empty openers, rhythm uniformity, or adjective stacking — the only signal is a markdown-syntax artifact, not a prose-level AI tell. Rewriting to kill this signal would mean converting checklists/quote blocks to prose paragraphs, which breaks "keep the card anatomy intact." Left as-is; treating WARNING-via-structural-signal as reviewed and accepted, not fixed.
