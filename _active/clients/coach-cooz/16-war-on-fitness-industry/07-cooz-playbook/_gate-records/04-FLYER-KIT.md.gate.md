# Gate Record — 04-FLYER-KIT.md

Date: 2026-07-09
Reviewer input: IMPLEMENTABILITY + VOICE + FACT ACTIONS (review skill output)
Status: Fixes applied. Ships.

---

## IMPLEMENTABILITY

**MUST-FIX 1 (Card 1 contradicts the kit / phantom asset) — FIXED.**
Card 1 rewritten from scratch. Removed the ad-hoc "build the squeeze page" / "duplicate booking page" / inline rewritten copy steps entirely — those steps live in `03-BUILD-THIS-FIRST.md` (booking page build, verbatim copy already pasted there) and `00-THE-PLAYBOOK.md` section 1 (abs-line swap). Card 1 is now a one-line gate that points at both, never re-derives. Removed the phantom "squeeze page build, tracked separately" line — no such doc exists; the squeeze page is confirmed live (per 03 card 3 and 00 section 3, both treat `coachcooz.com/stop-feeling-like-shit` as existing).

**MUST-FIX 2 (60-second test fails on card 1) — FIXED.**
Slug now stated inline on the card face (`coachcooz.com/stop-feeling-like-shit`). First checkbox is a physical open-this action: "Open `coachcooz.com/stop-feeling-like-shit` in Squarespace edit mode." Time is one honest number for the whole card (10 min), with the heavier 03-doc build time (30-45 min) named separately as a conditional branch ("Not done yet? Stop here and finish that doc first"), not folded into card 1's own total.

**SHOULD-FIX 1 (Card 6 tracking location / measurability / metric-set mismatch) — FIXED.**
Named the exact location: Squarespace Analytics → Traffic, filtered to `utm_campaign=war-on-fitness-industry` (UTM string confirmed against `02-landing-page/SQUEEZE-PAGE.md`, "QR / UTM parameter" section). Stated plainly that a plain-URL QR gives no raw scan count and that visits are the stand-in. Reconciled card 6's raw-count kill/print-more signals with the doc 00 scoreboard percentages (3% / 0.6% / 1%+) so one metric set runs across the kit — added the percentage figures alongside the existing raw counts rather than replacing either, since doc 00's own scoreboard states both.

**SHOULD-FIX 2 (outcome banner run-on) — FIXED.**
Banner rewritten as three short beats instead of one four-clause sentence. No participial pileup.

**NICE (terminology drift "90-Day Protocol" vs "90-Day Resurrection Protocol") — FIXED.**
Standardized to "90-Day Resurrection Protocol" (matches 03-BUILD-THIS-FIRST.md and 00-THE-PLAYBOOK.md).

---

## VOICE

**Medium 1 (outcome banner AI rhythm tell) — FIXED.** Covered by SHOULD-FIX 2 above.

**Medium 2 (negation-reveal "aren't comps... they're the actual artwork") — FIXED.**
Rewritten to lead with the command: "Don't treat these as comps. The text is vectored and the QR code is live — touch the layout and you break the scan." One em dash, within the ≤2/doc cap (only em dash in the doc's own authored prose; the other em dash in the doc is inside a quoted section title from `CONCEPT-V2-MARKETABLE.md`, not original prose).

**Low 1 (triple anaphora "wrong tone, wrong reveal, wrong guy") — RESOLVED BY DELETION.** That line lived in the old card 1 "Why it matters," which was fully replaced under MUST-FIX 1. No longer in the doc.

**Low 2 ("Scale signal" reads as growth-bro / voice-killer list D1) — FIXED.**
Renamed to "Print-more signal" (matches the "print more" plain-English verb already used elsewhere in the same card and in the "Done when" line).

**Low 3 (title tricolon + em dash) — FIXED.**
Title changed from "The Flyer Kit — Printed, Placed, and Working" to "The Flyer Kit: Printed, Placed, Working." Removes the em dash and drops the "and" that made the tricolon read more like deck copy.

---

## FACT ACTIONS

**VERIFIED (ask script, spec details) — no change made.** Confirmed against `01-flyer/FLYER-COPY-AND-SPEC.md` ("The ask") and `04-visuals/README.md` / FLYER-COPY-AND-SPEC ("Print notes," "Distribution note"). Matches verbatim.

**DRIFTED (scan-test distance "~25 feet") — FIXED.**
Source of truth: `01-flyer/FLYER-COPY-AND-SPEC.md` line 66 — minimum scan distance ~12-15" (arm's length, 4x6 hand-to-hand) and ~25-30" (across a counter, placard). Confirmed independently in `04-visuals/README.md` ("~30\""). Card 2's test-scan checkbox corrected to "from arm's length (about 12-15 inches) and from across a counter (about 25-30 inches)" — a ~10x unit error (inches misread as feet) is gone. A 2.5-3" QR code was never scannable from 25 feet; this could have caused a false proof rejection.

---

## PROSE CLASSIFIER

`python3 execution/prose_classifier.py check 07-cooz-playbook/04-FLYER-KIT.md` → **AI Score 2/10, Verdict WARNING** (single signal: `parallel_structure_overuse`, 5 parallel blocks).

Not actioned further. This flag is inherent to the mandated card/checklist anatomy in `DOC-FORMAT-SPEC.md` (repeated `[ ]` step lines read as parallel structure by design) and is present at a *higher* rate in sibling docs in the same kit that already ship: `03-BUILD-THIS-FIRST.md` (16 parallel blocks, same 2/10 score) and `00-THE-PLAYBOOK.md` (14 parallel blocks, same 2/10 score). Forcing artificial variation into the checklists to chase a lower parallel-block count would break the spec's own card anatomy (verb-led steps, consistent shape) for no reduction in actual AI score. Treated as accepted baseline for this doc type, consistent with the rest of the kit.

---

## Card anatomy check

All 6 cards still: bold imperative header · "Why it matters" (one sentence) · "Do it (TIME + who)" with verb-led checkboxes (max 7, all cards well under) · "Done when" (binary, visible) · "Go deeper →" (named doc + section). Doc-level: outcome banner first line, "Not now" section intact and unedited. Spec anatomy preserved through every fix.
