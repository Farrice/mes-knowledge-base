# Gate Record — 03-BUILD-THIS-FIRST.md

**Date:** 2026-07-09
**Reviewed file:** `07-cooz-playbook/03-BUILD-THIS-FIRST.md`
**Spec:** `00-strategy/DOC-FORMAT-SPEC.md`

---

## Applied (MUST-FIX / must-fix-equivalent)

1. **IMPLEMENTABILITY — MUST-FIX — device ambiguity.**
   Added one line under the After-this banner: *"Cards 1-4 are 40 min at your laptop. Card 5 is the phone test — do that from the couch."*
   Closes the 60-second-test gap: a phone-reading coach now knows whether tonight's move is "skim now, build tomorrow at the desk" instead of closing the doc undecided.

2. **FACT ACTIONS — CONTRADICTION — "FIX BEFORE COOZ ACTS."**
   Card 3 ("Point the QR landing page's three buttons at the new address") assumed `coachcooz.com/stop-feeling-like-shit` already exists. Cross-doc check confirmed it does not (`04-FLYER-KIT.md`, `04-visuals/README`, `RAW-PROOF-INVENTORY.md §3`). Added a "Before you start" line to that card pointing to `04-FLYER-KIT.md` as the prerequisite build step, so the doc no longer asserts a false premise to the reader.

---

## Reviewed, not applied (MEDIUM / LOW — scope was MUST-FIX/MUST-CUT only)

Left as-is per review severity; flagged here for a future pass if Farrice wants them:

- **MEDIUM (implementability):** slash-notation (`/briefing`, `/book-in-person`) reads as operator shorthand rather than coach language. Title and first-mention could be plain-English with the slug introduced after.
- **MEDIUM (implementability):** Card 2 breaks the checkbox format (prose + blockquote) and never checks for Save — Squarespace won't persist a paste without it.
- **MEDIUM (voice):** Line 42, "90-Day Resurrection Protocol" in body copy — voice profile D2 restricts "resurrection" to brand-name-only usage, not cold-scanner body text. Needs a deliberate keep/cut decision, not a silent one.
- **LOW (implementability):** Card 1 has no fallback if Squarespace won't duplicate the page cleanly.
- **LOW (implementability):** Header says "30-45 minutes"; card math floors at ~40-45. Change to "About 45 minutes" for honesty.
- **LOW (voice):** Line 40 "It's a paid session, not a free consult" — mild negation-reveal scaffold.
- **LOW (voice):** Line 40 "That's the whole audit. Not a warm-up, not a pitch." — echoes documented mic-drop tell; likely fine for Cooz's register but flagged as a choice.
- **LOW (voice):** Line 3 "Every flyer, every QR code, every click..." — rule-of-three anaphora, borderline.
- **LOW (voice):** Lines 7/101 "founder/executive-track/empire" — acceptable, describes the OLD `/briefing` audience by contrast; confirmed none of that language is in the new page copy itself.

---

## prose_classifier.py result (post-edit)

```
Verdict:    WARNING
AI Score:   2/10
Words:      1054
Signals:    1
Rhythm CV:  1.14 (varied)
DETECTED PATTERNS:
  [2.0] parallel_structure_overuse — 16 parallel blocks found
```

Not treated as a fix-required flag: the "parallel structure" signal is the mandated card anatomy itself (five cards, each with a repeated `Do it: [ ] / [ ] / [ ]` checklist block per `DOC-FORMAT-SPEC.md`). Verdict is WARNING, not FAIL/BLOCK, at a low 2/10 score. Rewriting to reduce repetition would violate the "keep the spec's card anatomy intact" constraint on this pass, so left unchanged.

---

## Factual grounding

- FACT ACTION 1 (Triage price, credit mechanic, session framing) — VERIFIED, no change needed; traces to `RAW-PROOF-INVENTORY.md §3`, `STRATEGY-SPINE` addendum, `CONCEPT-V2 §3b-F`, `SQUEEZE-PAGE Section E`.
- FACT ACTION 2 (squeeze page existence) — CONTRADICTION, fixed above.

## Not applied to the client file

Per instruction, no gate record language, operator tags, or "MUST-FIX" markup was appended to `03-BUILD-THIS-FIRST.md` itself — it stays client-facing and jargon-free per the Zero-Jargon Law. This record lives here instead.
