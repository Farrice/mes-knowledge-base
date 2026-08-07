# Gate Record — 01-THE-TRUTH.md

Operator-only. Not client-facing. Traces the review pass and every fix applied 2026-07-09.

---

## Source review

Three findings sets: IMPLEMENTABILITY (60-second test / card anatomy, verdict REJECT — 2 of 3 cards failed), VOICE (ai-slop-detector + structural bans), FACT ACTIONS (claim-to-Receipts trace). Full findings supplied inline in the applying prompt, not duplicated here.

## IMPLEMENTABILITY — applied

- **MUST-FIX (Card 1 had no physical action, feeling-based done-when).** Rewrote the whole card. Header changed from "Keep the anti-industry wedge" to "Keep pointing at the industry's bullshit, not at wanting a body." The three mental-reframe steps ("Say your wedge as...," "Read these out loud," restate zero-hedge) were replaced with a real artifact task: open a blank note titled THE ANGLE, type the line, pin it above the desk, plus the existing flyer-line-preservation step. Done-when changed from "You can say your zag out loud with zero hedge" (a feeling) to "That sentence exists in writing where you'll see it every day, and the flyer hook hasn't changed" (visible, binary).
- **MUST-FIX (Card 3 promised three paste-ready assets, delivered zero, at a dishonest 30-min estimate).** Split the card's scope. The qualifying question is now delivered as exact, paste-ready copy: "Before we talk, one question: what's the one thing you've quietly stopped doing since you stopped feeling good in your body?" Monthly billing and the stated guarantee were pulled out — they're real business-model decisions Cooz hasn't made (price terms, refund/continuation language), not a 30-minute copy task, and inventing exact guarantee wording would violate the doc's own "no new facts" rule. Both moved into the Go-deeper note and a new Not-now bullet, explicitly labeled as pricing decisions for later. Time estimate dropped from 30 to 15 min to match the now-honest scope (one intake line, one language discipline, one avoid-list). Header renamed "Take three moves..." → "Steal McBroom's qualifying question, skip his price tag and his headline" so the header itself doesn't overpromise.
- **MUST-FIX (outcome banner promised "exact words" the doc didn't deliver on card 3).** Rewritten entirely: "Your angle is pinned in writing above your desk, two liar-lines are gone from your squeeze page and replaced, and one new qualifying question is live wherever people book a call with you." Matches each card's actual done-when 1:1, no overpromise left standing.
- **SHOULD-FIX (Card 2 deleted two lines, supplied one replacement, left a hole).** Step now reads explicitly: "Replace 'Nobody hires a coach for abs' with: [line]. 'Abs don't feel like anything' just goes. Nothing fills that spot." No ambiguity left for a tired reader to resolve mid-edit.
- **SHOULD-FIX (jargon on the card face — "wedge," "zag," unexplained "the man who went dormant").** "Wedge"/"zag" replaced with "angle" throughout Card 1 (including the note title, changed from a literal "WEDGE" label to "THE ANGLE" so the fix didn't just relocate the jargon). "The man who went dormant" in Card 3 kept — checked against SQUEEZE-PAGE.md Section E, where "went dormant" is Cooz's own established copy, not invented jargon — but reworded inline to "the man whose life went dormant, not his abs" so it reads as self-contained instead of an unexplained aside.

## VOICE — applied

- **HIGH (Take A line 11, "It's not your line. It's the market's own." — negation-reveal, banned per spec line 91).** Rewritten as declarative + imperative inside the Card 1 rebuild: "The market already wrote your best line. Don't improve it." No contrast scaffolding, no em dash.
- **MEDIUM (banner's "you know exactly what's proven, what's wrong, and the exact words" — info-product outcomes-header framing with a rule-of-three).** Resolved as part of the banner rewrite above — the new banner states three concrete, distinct deliverables (a pinned note, two edited lines, one live question), not an abstract-noun triad.
- **MEDIUM (card-anatomy labels read as a coaching worksheet — "Why it matters / Do it / Done when / Go deeper").** Left as-is. This is the mandated card anatomy from DOC-FORMAT-SPEC.md, which this rebuild was explicitly instructed to keep intact. Renaming or folding the labels into prose would break the format every other doc in this package follows.
- **LOW (closing "You can't replicate that this year. Don't try." mic-drop-plus-deflation).** Left as-is per the reviewer's own framing ("only a flag, not a mandate") — genuinely Cooz-terse, not engineered.
- **LOW ("Straight talk first." throat-clear opener).** Left as-is per the reviewer's own note ("acceptable as-is").

## FACT ACTIONS — applied

Both claim groups traced VERIFIED with no figure changes required (Reddit quotes/upvote counts to SOCIAL-LISTENING.md; wedge quotes, the abs-swap line, and McBroom-machine figures to TRUTH-README/SQUEEZE-PAGE/MCBROOM-READOUT.md). One upgrade applied beyond the "no change" instruction: Card 3's "do not chase" list was tightened from vague ("his episode count, his 7-person team, his exact headline") to the specific VERIFIED figures already on file — 1,069 episodes, 7-person team, $497/month — so the card cites real numbers instead of a hand-wave. Confirmed the two exact strings Card 2 depends on ("Nobody hires a coach for abs," "Abs don't feel like anything") exist verbatim in SQUEEZE-PAGE.md Sections A and B — the VERIFY item cleared, no card rewording needed on that front.

## Prose classifier

`python3 execution/prose_classifier.py check 01-THE-TRUTH.md` post-edit: **CLEAN, AI score 1.5/10**, single signal `parallel_structure_overuse` (3 blocks), rhythm CV 1.09 (varied).

Reviewed and dismissed: the 3 flagged blocks are the mandatory `Why it matters / Do it / Done when / Go deeper` checklist rows repeated across three cards — required by DOC-FORMAT-SPEC.md's card anatomy, same false-positive class already dismissed in sibling gate records (e.g., 02-THE-PLAY.md.gate.md). No prose rewrite applied; verdict is CLEAN and score is well below any threshold.

## Declined / not applied

- VOICE MEDIUM (fold card-anatomy labels into prose / rename "Done when") — declined, conflicts with the explicit instruction to keep the spec's card anatomy intact.
- VOICE LOW x2 (closing deflation, "Straight talk first" opener) — declined per the reviewer's own "acceptable as-is" / "only a flag" framing.

Every MUST-FIX applied. Every SHOULD-FIX applied. All VERIFIED fact actions applied (including the precision upgrade on Card 3's avoid-list).
