---
name: Listing URL → Sendable Package Pipeline (register-ladder, claims-ledger, one checkpoint)
problem_signature: a client listing url or property drop produces surface-level ai listing copy in the wrong register with unverified claims and a package that needs manual editing before it can be forwarded, because research, register selection, fact provenance, compliance, and the send shape all lived in memory instead of machinery
domain: creative
tags: [real-estate, jen-santulan, listing-content, hooks, register-ladder, claims-ledger, fair-housing, send-package, pipeline]
date: 2026-08-05
status: active
session: listing-engine-v2
---

# Solution Card — Listing URL → Sendable Package Pipeline (2026-08-05)

**Problem:** A listing URL dropped in chat used to produce generic hook sets: wrong register for the price tier (FTHB rent-math hooks on a $3.2M listing), claims asserted without provenance (a "pool + spa" line when the MLS said Spa: None; a phantom "finished basement"; a wrong bath count in copy that shipped), fair-housing steering risks (school-targeting on camera), and a robust internal sheet that still wasn't forwardable to the client without manual rebuilding.

**Context it was cracked in:** 5200 Armida Dr (Woodland Hills, $3.199M), 2026-08-05 — three hook generations (feature-recital → fact-in-tension → the winner: authority-POV "Quiet Flex"), two taste rejections (Farrice's, then Jen's), full manual claims verification. The whole arc was then codified the same day as `/listing-package`.

**The approach (repeatable recipe):**
1. **Deterministic intake** — `execution/listing_intel.py parse|diff|ledger`: fetch dump → `listing.json` + `claims-diff.json` + `claims-ledger.json`. The MLS-fields-vs-description DIFF is the core mechanic — contradictions (spa, basement, bath arithmetic, price-jump/Zestimate ambush, brand claims) are code-detected and land in the don't-say list automatically.
2. **Fetch ladder, never fabricate** — Playwright (isolated from sibling-session locks) → Apify `web` actor (~$0.003) → ask-for-paste.
3. **Receipts-only market layer** — `execution/research.py --depth standard` for zip medians/$psf/DOM/rents/schools; honesty anchors ($/sqft vs median) computed BEFORE writing so no "deal" framing survives on an above-median listing.
4. **Register ladder before generation** — tier → register (`_active/clients/jen-listings/CLAUDE.md`): <$1.5M warm FTHB (FTHB-Permission hook mandatory) / ≥$2M Quiet Flex authority-POV (FTHB hook forbidden). Three hook species with fixed roles: authority-POV leads luxury hooks; fact-in-tension mines bodies/cover text; warm anticipation retired as opener.
5. **One taste checkpoint** — strategy card + hooks + scripts pause for Farrice (spiral brake: 2 rejections → back to inputs); caption/send text render only after his verdict. Felt verdicts → `voice_ratchet.py add --client jen`.
6. **Compliance floor as code** — `execution/fair_housing_lint.py` (steering language, schools-in-script, absolutes; exit 2 = no ship) + `client_package_lint.py` on the send text.
7. **Send shape** — `references/prompts-v2/listing-send-package.md`: one forwardable text (numbers block → pick-one options → HOOK/TOUR/CLOSE → cover-text→photo pairs → caption with fine-print block → filming notes → don't-say list). Robustness in the sheet, simplicity in the send.

**Why it works:** each failure mode is owned by the layer that can't forget it — facts by a parser, contradictions by a diff, compliance by a linter, register by a price gate, taste by exactly one human checkpoint, and the deliverable's shape by a template; the contracts between layers are files (listing.json, claims-ledger.json, SEND-TO-JEN-text.md), not memory.

**Reuse trigger:** any listing URL/address/description dropped for content — `/listing-package <input>`. Also the pattern donor for any "client content with verifiable facts + a register decision + a forwardable deliverable" pipeline (second client = voice pack + register file + send template drop-in; core is client-agnostic).
