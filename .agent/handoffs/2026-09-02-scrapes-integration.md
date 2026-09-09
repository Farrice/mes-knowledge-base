---
thread: scrapes-integration
status: done
resume_hint: Scrapes routed from intent: six doors + BRAND LOCK landed; next = his template pool + blind bar #1
branch: worktree-scrapes-routing
pin: true
---

# Handoff — scrapes-integration (2026-09-02, late session, lane `worktree-scrapes-routing`)

## Shipped (on main, pushed)
- **Routing:** the 36 Scrapes skills are indexed by the per-prompt router (`find_skill.py`, tag `[SCRAPES]`); six bindings open six front doors: `/social-carousel`, `/social-post`, `/social-repurpose`, `/deck-build`, `/video-to-shorts`, `/video-to-ebook` (`routing_enforcer.py` + `directives/routing-bindings.md`, thin wrappers in `.agent/workflows/`, shims minted).
- **BRAND LOCK:** `execution/scrapes_brand.py` (`list` / `resolve --from-prompt … --cwd …` / `check <brand> --pool …`). Brands: farrice (root `brand_context/`), jen (`_active/clients/jen-listings/brand_context/`), andrea (stub). Ambiguity refuses; a client alias beats the owner default; cross-brand path leaks fail the check.
- **Seams:** our pens write caption + slide script → `claim_audit --strict` + `prose_classifier` → Scrapes Scenario A runs the machinery. Research via `research.py` into their cache (`<brand>--slug`). Craft-map master + `openai_budget_guard.py check` before any AI slide.
- **Compounding:** `context/learnings.md` (their hook, now live) + finalize + asset manifest + handoffs per door.
- **Design (LIVING):** `_active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md`; pointers in PRECEDENCE-MAP.md and INTEGRATION.md; RESUME-BRIEF.md rewritten.
- **Harness fixes:** `worktree_lane.py merge` verifies its abort (fallback + loud warning), wraps the merge body, refuses a foreign MERGE_HEAD, tracks `merge_in_flight`; new `worktree_lane.py preserve` moves stranded human work off main loss-free (used tonight: 8 drift paths → lane → merged back). `main_write_guard.py` judges the effective tree (`cd <lane> &&`, `git -C`), `--self-test` 21 cases. Tests: `tests/test_worktree_lane_merge.py` (8), `tests/test_scrapes_routing.py` (23).
- **Lanes:** `codex/scrapes-trial` merged (via this lane) and torn down; preserve lane merged and torn down; main and origin in sync at the time of writing.

## Needs Farrice
1. Template pool for his brand: 4 refs staged in `brand_context/visual_refs/` (Premium Minimal carousel frames). Run `00-social-content` onboarding Phase 5 (one `ssc-template-builder` per ref; GPT Image ≈ $0.17/image; month $0.00/$15.00), approve in Template Studio. Until then `scrapes_brand.py check farrice --pool linkedin-carousel` reports `render path: blocked` on purpose.
2. Blind bar #1: one supplement teardown through `/social-carousel` vs the current LinkedIn carousel path.
3. Precedence FLIP/KEEP disagreements; Jen v2 cover verdict (thread `jen-canvas`, parked).
4. One-line follow-up: `.agent/openai-usage.json` is tracked and written by `openai_budget_guard.py status/check`; move it into `SPEND_LINKS` (untrack on main first).

## Cost
$0.00 spent this session (no AI generation; GPT Image month at $0.00/$15.00).

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
