# Final verification matrix — run against growth-lab/farrice-parallax when flagship completes

**CORRECTED SEQUENCE (Farrice 2026-08-27 — his critiques are HOLISTIC, applied to the entire deliverable set before he judges anything):**
1. Verify (checks below) → 2. FIX every defect found (not note — fix) → 3. **ENRICH: fire /gb-enrich on the farrice-parallax pack (paid calls OK, show cost receipt) and RE-RENDER every artifact so the judged set is data-enriched, not educated-guess** → 4. Reader-purity REWRITE pass on all client forms (not just lint — rewrite leaks to reader language) → 5. Package E2E → 6. Judging surface with the enriched artifacts. Farrice sees NOTHING until all six steps pass.

Already verified this session (2026-08-27, live browser + real data):
- ✅ Lead magnet FULL FLOW (live pack bake): 5/5 real videos wired, 0 placeholders, gate disabled→enabled on 3 answers, conversion-goal reorders whitespace-first, CTA + UTM correct, 0 console errors
- ✅ build_lead_magnet.py standalone from live pack ($0, one command)
- ✅ export_growth_package.py pdf: fixture client brief + mini-report → clean premium PDFs (visually verified)
- ✅ Positioning Wheel (mid-run state): 8 wedges, wedge click → 5-beat panel with real content, real niche channels (@AlexHormozi, @DavieFogarty, @foundr...), 0 JS errors
- ✅ Engine, heartbeat 7/7, template lint 0, radar Homebase row

## Run when flagship lands (per artifact in growth-lab/farrice-parallax/exports/):
1. **Console**: load each HTML over localhost:8477 in Playwright → 0 errors (ignore favicon 404 from ad-hoc server).
2. **Click contract** ("a click that does nothing is a bug"): wheel wedges + channel bubbles → cards/panels; bullseye ring taps → detail cards; 3-2-1 card-rack bench swap actually swaps (narrow-for-narrow enforced); matrix cells → specimen; every `.tap` instruction does what it says.
3. **Receipts (surpass bar Q2)**: every attribute score / whitespace verdict / top-50 row carries specimen links (YouTube URLs from the pack). ⚠ OPEN FLAG: wheel had 0 youtube links mid-run — verify wired at final; if absent = defect, fix before surpass presentation.
4. **Real-data wiring**: grep client HTML for actual pack video_ids/titles + verify numbers match `.agent/outlier-radar/packs/farrice-parallax/latest.json`; zero {{placeholders}}; zero FIXTURE strings.
5. **Reader-purity sweep (BINDING rule 2026-08-27)**: client-facing forms (`*-client.html`, blueprint, lead magnet, PDFs) contain NO repo paths, commands, tier jargon ("pack", "data_tier", "niche slug", "[NEED]", "manifest"), system names (outlier radar, growth-lab), or workflow refs. Run `client_package_lint.py` on each + grep the jargon list. Tier states must read as reader language. Operator notes exist as separate `operator/*-notes.md` files.
6. **Standalone reproduction**: re-run ONE workflow's artifact solo (e.g. re-render whitespace-map client HTML from its brief JSON via `render_brief.py --client`) — proves standalone producibility, byte-diff sanity.
7. **Package E2E**: `export_growth_package.py package --niche farrice-parallax` → every HTML gets a PDF, CONTENTS.md client-clean, OPERATOR-NOTES.md outside the zip, zip opens.
8. **Surpass side-by-side**: pair each artifact vs `extractions/kallaway/source-skills/baseline-outputs/` equivalent → present to Farrice for verdict → `blind_pass.py record` → `chain_runner.py finalize`.

Server for testing: `.venv/bin/python3 -m http.server 8477 --directory <worktree>` (background task b7oijjxsn may still be running).
