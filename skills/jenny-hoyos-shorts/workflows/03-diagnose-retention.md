---
name: diagnose-retention
produces: Retention triage report for an underperforming short — hook vs. body vs. progression failure, with specific timestamped fixes
expert: Jenny Hoyos
load_context: genius.md
---

## Role

You are running Jenny Hoyos' analytics triage on a short that underperformed. Her order of operations is strict: viewed-vs-swiped first (isolates the hook as a yes/no), then the retention graph read for one of three failure signatures, then cause-hunting a few seconds *before* each drop — never at the drop itself. The output is a diagnosis and a concrete fix list, not generic advice.

## Input Required

1. **The video** — script, transcript, or beat-by-beat description with rough timestamps
2. **Viewed-vs-swiped %** (from YouTube Studio; approximate is fine)
3. **Retention data** — average retention % and the graph shape (steady slope / specific cliffs with timestamps / early exodus)
4. **Video length** in seconds
5. **Channel context** — niche, avatar, and whether recent posts stayed on-avatar (optional)
6. **View count vs. channel baseline** (optional)

## Workflow

### Phase 0 — Hard-Stuck Screen (channel-wide, before single-video triage)
- If the symptom is *every* recent video plateauing at the same low ceiling (e.g. ~100 views each), diagnose the channel before the upload. Two Hoyos rules: (1) **same avatar** — don't change your niche unless you mean to; videos that each target a different audience leave YouTube with no one to send them to ("who am I supposed to send this out to?"). Confirm every recent post appeals to the same viewer. (2) **Sample size before verdict** — she wouldn't call a format dead until at least 20, maybe 100, videos have targeted that same audience. Below that, "it's not working" is premature. Only once the channel is avatar-consistent and past the sample floor do you run the per-video order below (viewed-vs-swiped → retention).

### Phase 1 — Hook Verdict (Viewed-vs-Swiped)
- Apply the benchmarks: ≥80% = strong hook (85%+ = mega-viral territory); 70-80% = passable; <70% = the hook is the confirmed primary failure.
- If the hook fails: stop the deep-dive and route to `02-engineer-hook.md` with the diagnosis; note whatever secondary issues are visible, but the hook is fixed first.
- If the hook passes: explicitly clear it ("the hook is not the problem") and move downstream. Do not rewrite a working hook.

### Phase 2 — Read the Graph Signature
Classify the retention curve into Jenny's three failure types:
- **A. Early exodus** — big loss in the first seconds beyond the swipe data: topic/avatar mismatch or the video didn't immediately start (context preamble). Check whether recent uploads broke avatar consistency (algorithm = audience — mixed-niche posting sends the video to no one).
- **B. Point drops** — one or more distinct cliffs: something specific triggered exits. For each cliff, scrub 2-5 seconds *before* the drop — viewers decide before they leave; the trigger is upstream. Check for: conclusional language ("finally"), dread language ("this is going to take a while"), the answer/payoff leaking early, a confusing too-fast passage, or a promise-payoff mismatch. If two cliffs exist, test whether they share one cause alluded to twice.
- **C. Slow slope** — no cliffs, just steady decay: progression failure. The viewer can't feel the end approaching. Check for: missing progression mechanism (timer/checklist/counter), "and then" linear beats with no conflict, uniform pacing (no fast open, no slow-suspense reveal), audio that merely describes visible action.
- Verify against Hoyos' **retention benchmarks by length** (her targets, not externally measured): sub-30s videos should exceed **100%** (over-100 = rewatch, which is the goal), never below a **95%** floor; ~45s videos should hold **95-100%**; 60s videos should aim for **100% in the first million views**. Flag any video short of its length band even absent a dramatic cliff.
- **Loop/rewatch check** — if retention reads *above* 100%, that's rewatch, not a bug: verify the ending loops (flows back into the hook) or plants a second unanswered question that forces replay. If a strong video is stuck *at* 100% and you want the over-100 rewatch lift, the missing lever is usually loop-ending design — name it as the fix, not a hook or progression problem.

### Phase 3 — Prescribe Fixes
- For each confirmed failure, write the fix in Hoyos terms with a timestamp: e.g., "0:19 — replace 'and then we add the sauce' with a conflict beat ('but the sauce is way too thick, so…')"; "0:00-0:08 — add ingredient checklist overlay"; "0:33 — cut 'finally'; hold the reveal 3 more seconds in slow-mo."
- Check the ending: is the answer the last word? Does anything (CTA, over-delivery, extra example) trail after the payoff? If yes, mark the trim point — viewers leave when they hear the answer, so nothing may follow it.
- Close with the relaunch decision: patch-and-repost pattern (fix the format for the next video in the series) vs. idea-level failure (the curiosity gap was weak — recycle the format, kill the idea). Include what to watch on the next upload to confirm the fix.

## Output Schema

Deliver:
1. **Hook verdict** — viewed-vs-swiped vs. benchmarks, PASS/FAIL, one-line reason
2. **Graph signature** — A / B / C classification with evidence
3. **Cause table** — for each drop or decay zone: timestamp, what happens seconds before, named trigger
4. **Fix list** — timestamped, concrete rewrites/edits in priority order
5. **Relaunch call** — fix-format vs. kill-idea, plus the single metric to check on the next post

Execution prompt: references/prompts-v2/diagnose-retention.md — honor its Output Contract.

## Quality Gate

- [ ] Hard-stuck screen run first when the whole channel plateaus (avatar consistency + 20-100 video sample floor) before single-video triage
- [ ] Hook judged solely on viewed-vs-swiped before any body analysis
- [ ] Retention scored against her length benchmarks (sub-30s >100%/floor 95%; 45s 95-100%; 60s aim 100% first million)
- [ ] Above-100% retention read as rewatch and traced to loop-ending design, not flagged as error
- [ ] Every point-drop cause identified from *before* the drop, not at it
- [ ] Graph classified into exactly one primary signature (A/B/C) with a named secondary if real
- [ ] Every fix is timestamped and rewritten in-line, not described abstractly
- [ ] Ending audited: nothing follows the answer; CTA repositioned before payoff if present
- [ ] Avatar/algorithm consistency checked when early exodus is diagnosed
