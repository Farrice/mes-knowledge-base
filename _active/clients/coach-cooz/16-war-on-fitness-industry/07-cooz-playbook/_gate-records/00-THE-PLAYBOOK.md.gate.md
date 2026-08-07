# Gate Record — 00-THE-PLAYBOOK.md

Date: 2026-07-09
Reviewer input: implementability review (SHIP WITH FIXES), voice review, fact-check pass
Applied by: Claude (Edit tool), reviewed against `00-strategy/DOC-FORMAT-SPEC.md`

---

## MUST-FIX — all applied

1. **Card 1 couldn't reach its own Done-when** (only deleted one of two denial sentences in Section A). Fixed: deletion now covers all three denial lines ("Nobody hires a coach for abs," "Nobody hires a coach to hit a number on a scale," "Abs don't feel like anything"), opener rewritten to affirm the want.
2. **Card 1 pointed at the wrong artifact** (`02-landing-page/SQUEEZE-PAGE.md` instead of the live page). Fixed: now points to `coachcooz.com/stop-feeling-like-shit` in Squarespace edit mode, matching doc 03's pattern.
3. **Ambiguous single swap-in for two sections.** Fixed: exact paste-ready replacement text given separately for Section A and Section B, no guesswork on placement.
4. **"Wait behind the yes" contradicted the five action cards.** Fixed in the 10-line read: Card 1 (landing page fix) and Card 5 (weekly ask) are explicitly called out as not waiting on the `/book-in-person` build; only printing (Card 4) waits.
5. **Effort dishonesty on who builds `/book-in-person`.** Fixed: 10-line read now states "you spend 30 to 45 minutes in Squarespace building it yourself."

## SHOULD-FIX — all applied

6. **Scoreboard contradictions.** Bookings row label corrected to "cards handed out that turn into a booked Triage" (matches the per-500 denominator). Print-more close-rate condition raised from "1 close of 5" (20%, inside the stop-and-fix zone) to "2 closes of 5" (40%, clear of it).
7. **Section 4 skipped the print-gate.** Added a lead line before the flyer card: "Don't print a single card until your landing page and coachcooz.com/book-in-person are both live and tested."

## MINOR — all applied

8. Raw filepaths/slugs replaced with plain URLs coach will actually see (`coachcooz.com/book-in-person`, `coachcooz.com/briefing`), "squeeze page" replaced with "landing page" on card faces.
9. Card 2 Done-when now matches its own 10-minute task (table saved to phone), with the batch print/stop decision logic moved to a "How to read it" line instead of masquerading as the completion proof.

## VOICE — applied

- Line 30 negation-reveal ("You're not arguing... You're arguing...") replaced with a direct statement: "The want stays. The misery-as-toll is what's gone."
- Line 17 triple "every X" anaphora collapsed into a causal chain: "The flyer sends them to a QR code, the QR code to a click, the click to a page that isn't built yet."
- Line 17 banned ICP word ("founder") and corporate word ("optimizing") replaced: "The old page talks to a guy who's already winning. Your scanner isn't. He's losing quietly."
- Line 76 mic-drop + deflation tail cut, folded into one line: "No warm-up, no pitch. That's the audit."
- Line 15 colon-before-list removed (colon habit flagged separately from the negation-contrast finding on the same line).
- Line 23 "Its heart is one correction" (writerly/abstract) replaced with "It comes down to one correction."
- Section 4 intro participial pileup ("backed by... tracked by...") broken into three short sentences.

## VOICE — flagged, not changed

- **Line 82, "90-Day Resurrection Protocol."** Voice profile D2 bans "resurrection" in client-facing body copy, reserving it for the brand header/URL. This is the literal program name inside paid-page copy that ships to Cooz's buyers. Per Client-Spec-First — do not unilaterally rename a client's product. **Needs confirmation from Cooz**: is "The 90-Day Resurrection Protocol" the locked program name? If not locked, swap to "90-Day Rebuild" or "90-Day Comeback" in this body line, keeping Resurrection for the brand line only.

## Not applied (out of scope for this pass)

- DOC-FORMAT-SPEC requires a mandatory "## Not now" section in every action doc; `00-THE-PLAYBOOK.md` currently has none. Not a review finding for this pass, so not added here — flagging for the next structural pass so scope stays finite and doesn't drift beyond what was reviewed.

## Fact actions

- McBroom figures ($497/mo, 1,069 episodes, 7-person team) — **VERIFIED**, traces to `MCBROOM-READOUT.md` §2. No change required.

## Automated check

`python3 execution/prose_classifier.py check 00-THE-PLAYBOOK.md` → **WARNING, AI Score 2/10**, single signal `parallel_structure_overuse` (14 blocks) — expected from the DOC-FORMAT-SPEC's mandated `[ ]` checkbox card anatomy, not an AI-slop tell. Card anatomy kept intact per instruction; no further changes made on this signal.
