# Scrapes Skill Systems — Resume Brief (LIVING; update in place)

*Last updated 2026-09-02 late session (lane `worktree-scrapes-routing`, Farrice asleep, full permission granted for reconcile + land). Paste the "Kickoff prompt" at the bottom into a fresh session to start hot.*

## Where we are, in one breath
The 36 Scrapes skills and 4 workers are vendored, on main, and — as of tonight — **reachable from intent**: six bindings open six front doors (`/social-carousel`, `/social-post`, `/social-repurpose`, `/deck-build`, `/video-to-shorts`, `/video-to-ebook`), every door opens with a **BRAND LOCK** (`execution/scrapes_brand.py`; farrice / jen / andrea registered; ambiguity asks, never guesses), our pens own the copy seams (Scrapes runs Scenario A), and every run writes to the loops (`context/learnings.md` is live, finalize, asset manifest, handoffs). Design + seam map: `ORCHESTRATION-DESIGN.md`. Jen's canvas thread is **parked** (his call, 2026-09-02); nothing further on her run until her six inputs land.

## What he still has to tap (his verdicts, in order)
1. **Approve his template pool** — BUILT 2026-09-03: 4 templates in `brand_context/templates/linkedin-carousel/` (cover · kicker stack · marker body · dark CTA), all pure HTML, $0 GPT Image. His first Studio pass: "typography, spacing, hierarchy done poorly on some" → craft pass done (headlines back to the brand's 72px h1, ref rhythm restored; `REVIEW-NOTES.md` in the pool). `scrapes_brand.py check farrice --pool linkedin-carousel` → READY (4/4). Open the Template Studio (`python3 .claude/skills/00-social-content/scripts/content-studio/content_studio.py brand_context/templates/linkedin-carousel --mode template --brand-context brand_context`) and click Approve per template. G2 warning stands: two image-bearing moves (evidence-crop, original-portrait) have no photo-zone template — add one photo ref later or flip them to `image_bearing:false`. Rule learned: headline values carry `<br>` line breaks or the renderer's autosize shrinks them.
1b. **`/scrapes`** is the one door (raw text in); user's guide `USER-GUIDE.md`.
2. **Blind bar #1** — one supplement teardown through `/social-carousel` vs the current LinkedIn carousel path. Judge: hook slide, visual floor, voice.
3. **Precedence map** — any FLIP / KEEP he disagrees with (`PRECEDENCE-MAP.md`).
4. **Jen v2 copy (cover A)** — 9 or not, which frame is short (thread `jen-canvas`, parked).
5. **Gigi** — register her `BRAND.yaml` when lane `worktree-gigi-engine-run` lands (her root is not on main yet).

## Do NOT rebuild
Brand context (all three), the six front doors, `scrapes_brand.py`, the bindings, the budget guard, the precedence map, the constitution block, the canvas artboards, the intake pack. Extend, never regenerate. Never edit inside `.claude/skills/*`.

## Harness state that matters
- `worktree_lane.py merge` now verifies its abort (main can no longer be left mid-merge by the tool); `worktree_lane.py preserve` moves stranded human work off main into its own lane; `main_write_guard.py --self-test` pins the cwd rules (21 cases). Tests: `tests/test_worktree_lane_merge.py`, `tests/test_scrapes_routing.py`.
- `.agent/openai-usage.json` is TRACKED and is written by `openai_budget_guard.py status/check` — it should join `SPEND_LINKS` in `worktree_lane.py` (untrack on main first) so lanes never churn it. Not done tonight; one-line follow-up.
- `tool-zernio-social/SKILL.md` frontmatter does not parse (unquoted colons); it is DO-NOT-USE anyway, so it is the one vendor skill the router does not index.

## Files
`_active/harness/scrapes-skill-systems/{ORCHESTRATION-DESIGN,PRECEDENCE-MAP,INTEGRATION,RESUME-BRIEF}.md` · `execution/scrapes_brand.py` · `.agent/workflows/{social-carousel,social-post,social-repurpose,deck-build,video-to-shorts,video-to-ebook}.md` · `context/learnings.md` · `brand_context/` + `_active/farrice-brand/brand_context/BRAND.yaml` (Farrice) · `_active/clients/jen-listings/brand_context/` (Jen) · `_active/clients/andrea-dj/brand_context/BRAND.yaml` (stub) · `directives/openai-usage-policy.md` · canvas https://claude.ai/code/artifact/084b1bd6-f6b0-4a4a-b1dd-9ddb6d611fb1 (parked)

## Kickoff prompt (paste into the new session)
```
Resume thread scrapes-integration. Read _active/harness/scrapes-skill-systems/RESUME-BRIEF.md, then ORCHESTRATION-DESIGN.md §3–4. First: build my linkedin-carousel template pool (refs from premium-minimal/package/templates/carousel, ssc-template-builder per ref, state cost before each GPT Image call, I approve in Template Studio). Then run /social-carousel on one supplement teardown for my brand as blind bar #1 against the current LinkedIn carousel path. BRAND LOCK on every step. No Chain ceremony until something ships.
```
