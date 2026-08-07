# E3 Blind Bake-Off — Farrice's 30 Minutes

**Do:** open `E3-blind-packet.md`, and for each of the 15 comparisons fill the row in `E3-rating-sheet.md`:
- **Real one is**: A / B / can't tell (gut read — your bimodal taste signature is the instrument)
- **Better one is**: A / B / tie (which would you rather publish/run?)
- Notes optional but gold (one phrase on *what gave it away* teaches E4 more than the verdict).

**Don't:** open `E3-ANSWER-KEY-SEALED.json` until all 15 rows are filled.

**What a skill's grade means afterward** (scored per skill, 3 comparisons each):
- **PASS (blind-pass)**: you couldn't reliably spot the real one, or you preferred the generated one — the skill replicates its expert at publish grade.
- **FAIL**: generated pieces were identifiable and worse — retrofit (or reroute usage to a better sibling skill).

**What happens when you're done** (say "E3 ratings done" in a session): the 15 ratings get ingested as human-calibrated entries into `evolution_store/ground_truth/eval_set_v1.jsonl` (≥15 threshold → kills the 7.25 score-flattening), validate the E2 census at ground truth, settle retrofit-vs-reroute for lara-linkedin-mastery + luke-copy-blocks, and gate E4 (encoding the standard into the factory).

**Methodology notes** (for honest interpretation):
- Generators saw ONLY their skill dir + task briefs — never the real pieces, extractions, or sibling skills. Same model (Opus 4.8) across all five skills.
- Real pieces: verbatim, provenance-verified; 13/15 VERIFIED, 2 LIKELY (Hormozi book ladder single-source on later rungs; Suzuki #3 has one unconfirmable mid-post segment joined at a natural break).
- Known residual limits: famous experts (Stanton TED, Hormozi) exist in model training data — briefs banned their signature phrases to force skill-driven generation, but training-bleed cannot be fully excluded; comparison 15's shared "do you want me to show you" line is dictated by the brief, not leakage.
