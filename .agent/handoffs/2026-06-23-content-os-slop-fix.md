# HANDOFF — Fix the Content OS AI-slop gate (thread: geo-content)

**Date:** 2026-06-23 · **Workspace:** `/Users/farricecain/Google Antigravity` · **Resume:** `/resume geo-content` (chain pinned this thread)

---

## WHY A NEW SESSION
The prior session ran long and fired too many parallel workflows — quality degraded (context rot). Farrice read the Content OS exemplar posts and **still saw AI tropes / banned words / same AI formatting** in the bodies. Root cause: the deterministic prose gate (`prose_classifier.py`) and a real anti-slop **skill** were never enforced as a HARD gate on the *post bodies*. The build's QA agent **self-reported** "fixed em-dashes / passed" — the banned "AI-memory-dependent observability, no deterministic backstop" failure mode. The post-level `prose_classifier` run came back "Signals: 1 / parallel_structure" — a **false pass**: it was flagging the doc's label-tables, not auditing the prose. Felt verdict: not sharp enough. The *strategy is right*; the execution gate failed.

## THE ONE JOB THIS SESSION (focused cleanup — do NOT rebuild)
The Content OS architecture, research, and the `/geo-content` command are DONE and good. The only job is making the **exemplar posts actually clean + sharp**:

1. **Hard anti-slop pass, one pillar at a time.** For each file in `_active/linkedin-launch/04-content-os/exemplars/_p1..p5` and `starter-content-batch.md`: run a REAL skill — **`/anti-slop-audit`** (or `/slop-check`) + **`prose-doctor`** (structural AI MOVES: negate-then-reveal "not X it's Y", twin-sentence endings, triple anaphora, "Here's what/why" openers, mic-drop, cheap-question closes, reveal-leadins) — and **actually apply the fixes**. Then the deterministic floor: `python3 execution/prose_classifier.py check <file>` pointed so it audits the **post text**, and re-run until genuinely clean. Verify; never trust a self-report.
2. **Felt-verdict pass.** Does each read like a credentialed operator settling a live fight (Farrice's 8/10 "would post as-is"), or does it still carry the AI shape/sameness? Rewrite the ones that don't via **`writers-room`** or **`/really-real-social`** — surgical, one engine; preserve the strong ones (the "don't rebuild elevated content / multi-engine degrades" lesson). P5 + P1 were the cleanest on arrival; P2/P3/P4 had the most fixes.
3. **Re-collate** the cleaned best into `starter-content-batch.md`.

**Do NOT** re-fire the multi-agent build. This is content-quality surgery, not a rebuild.

## LESSONS TO APPLY (this is why we degraded)
- Enforce the DETERMINISTIC gate on the actual prose, not doc scaffolding. Verify with the tool; never accept an agent's "QA passed."
- Don't run 8–11 parallel agents for content *caliber*. Caliber needs one engine, careful passes, the gate between each.
- Felt verdict > system QA self-scores (memory: `auto-evolution-cant-substitute-for-ground-truth`, `multi-engine-rebuild-degrades-elevated-content`). Farrice catching slop in post #1 IS the signal.
- Strategy is locked and correct: **edu-FIRST adjudication spine, value-first, offer soft (`--cta` ~1-in-5)**. Don't relitigate it; fix the prose.

## STATE — WHERE EVERYTHING IS (reference, don't duplicate)
- **Strategy spec (read, don't re-derive):** `_active/linkedin-launch/01-research/CONTENT-DOMINATION-RESEARCH.md` (thesis, blend map, formula, jacking) + `_active/linkedin-launch/04-content-os/CONTENT-OS.md` (master) + `content-os/content-creation-system.md` + `content-os/social-playbook.md`. Audience: `research/MARKET-ICP-DOSSIER-2026-06.md`.
- **The posts to fix:** `content-os/exemplars/_p1..p5` (15 posts) + `content-os/starter-content-batch.md` (14 collated).
- **The command (DONE, value-first):** `.agent/workflows/geo-content.md` (rebuilt) + `SLASH_COMMANDS.md` entry updated.
- **SUPERSEDED (ignore / can delete later):** `content-os/CONTENT-OS.md` supersedes the old `_active/linkedin-launch/content-engine/CONTENT-ENGINE.md` (offer-coupled 5-pillar engine).
- **Voice law / slop bank:** `_active/farrice-brand/CLAUDE.md` + `directives/ai-slop-ban-bank.md` (64 entries, what `prose_classifier` enforces).

## OPEN ITEMS (not done)
- **[PRIMARY] The content-os AI-slop fix above.**
- `P3-3` (GLP-1 "patch notes" gaming-seasoning post): weakest, rests on 2 `[VERIFY LIVE]` literature claims — likely cut or rewrite, don't ship as-is.
- All **5 newsjack posts are `[VERIFY LIVE]` scaffolds** — swap a real, screenshotted moment before posting (facts/physiology are real; the triggering example is a pattern).
- **Not committed:** `content-os/` files + the rebuilt `.agent/workflows/geo-content.md` + the `SLASH_COMMANDS.md` edit. (The earlier launch package WAS committed as `61b590a6` — but on branch **`session/session-pin-formula`**, not `main`; merge to main if desired.)
- **Drive copy of `content-os/`** into the folder `Farrice — GEO-SEO Health Brand Launch` (`1rSrzr8jYYlwbICfvcNRshhNAo5FhlLOz`, docs 00–15 already there) — NOT done.

## ALSO SHIPPED EARLIER THIS SESSION (good, committed, leave alone)
The full LinkedIn launch package: `MARKET-ICP-DOSSIER`, `CANONICAL-OFFER-BRIEF`, `LAUNCH-DECK-2026-06-23`, `featured-section-and-profile`, `lead-magnet-ai-search-visibility-test`, `claim-safe-citation-audit-TEMPLATE/EXAMPLE`, `lead-gen-playbook`, `START-HERE-2026-06-23` — all under `_active/linkedin-launch/`, committed `61b590a6`, mirrored to Drive (docs 00–08). This is the launch Farrice can ship today; it is NOT the thing that needs fixing.

## SUGGESTED SKILLS (invoke these)
- **`/anti-slop-audit`** and/or **`/slop-check`** — the real anti-slop workflows (the missing gate).
- **`prose-doctor`** — structural AI-MOVE removal (subagent; no shell).
- **`prose_classifier.py check`** — deterministic floor, run on cleaned prose.
- **`writers-room`** or **`/really-real-social`** — rewrite below-bar posts to caliber (one engine, surgical).
- **`/resume geo-content`** — loads this pinned thread.
- Keep the build small: no `/jarvis-command-center:deploy`, no big Workflow fan-outs — this is surgery.
