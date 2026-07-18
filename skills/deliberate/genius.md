# /deliberate — Genius

The philosophy doc. Read this when the SKILL.md isn't enough — when you need to understand *why* contradiction-preservation matters more than synthesis.

## How to Use This Skill (Model Calibration)

These five steps are intuition primitives, not a checklist to stamp through in order. If the output visibly narrates "Step 2: Claude take, Step 3: Gemini take, Step 4: Synthesis" as bureaucratic section labels with no live thinking underneath, the mechanism has failed even though every header is present. The test: would a reader who has seen Perplexity's "model council" blend two opinions into managerial mush recognize this as genuine cross-model deliberation — or as one model wearing deliberation's vocabulary? If it reads like the second, the tell is almost always that the Gemini take was paraphrased instead of rendered verbatim, or that the Claude take was written retroactively to agree with wherever Gemini landed.

Specifically:
- Do NOT write the Claude take (Step 2) after seeing Gemini's response. Post-hoc agreement is the exact failure this file's "Why Synthesis-Blending Is the Failure Mode" section (below) warns against — commit to a position and a disconfirming consideration BEFORE running `execution/deliberate.py`.
- Do NOT let "Where they disagree" default to restating both surface positions. Per the Output Contract in `skills/deliberate/references/prompts-v2/deliberation-synthesis.md`, name the underlying assumption — a pricing disagreement is usually a positioning-premium-vs-accessibility disagreement wearing dollar signs.
- This skill's texture is adversarial, not diplomatic. A deliberation that reads as courteous consensus-building has drifted into `/council` territory — a different mechanism with a different job (see the comparison table in SKILL.md).
- Polish is the tell here in a specific way: if the "Gemini take" section sounds suspiciously like it was written in Claude's own cadence, that's the sign the call was skipped or the response was summarized instead of rendered verbatim. The raw, occasionally-clunkier voice of an actual second model is the proof of a genuine run — smoothing it over defeats the entire mechanism.

---

## The Single Thesis

**Two models that disagree tell you more than two models that agree.**

When Claude and Gemini converge, the prompt was likely consensus-shaped — the answer was downstream of training-data overlap or shared cultural priors. Convergence isn't proof of correctness; it's proof of agreement.

When Claude and Gemini diverge on a high-stakes prompt, the disagreement is the signal. It points to either:
1. A genuinely contested underlying assumption (where YOU need to decide which assumption you accept)
2. A blind spot in one model's training the other didn't share
3. A taste call neither model can resolve without your context

In all three cases, the contradiction is more informative than the synthesized middle.

## Why "Synthesis-Blending" Is the Failure Mode

Perplexity's "model council" pitch (as best we can infer) is: query routes through multiple models, the synthesizer composes their outputs into one answer. The user sees the synthesized output, not the underlying disagreement.

This is exactly the failure mode `/deliberate` is built to prevent. When you blend Claude's "I'd price at $5K" and Gemini's "Price at $7.5K" into "$6.25K seems reasonable," you have produced an output that NEITHER model would actually defend, AND you've hidden the genuine question (which is: "what's your underlying assumption about positioning premium vs. accessibility?").

Contradiction-preservation is honest. Synthesis-blending is comfortable. Comfort fails at high stakes.

## Why Two Models Beats One + Persona Simulation

The existing `/council` workflow uses one model (Claude) to simulate 3-4 different personas. This is a perfectly good pattern — it catches stakeholder perspectives the user hadn't considered, and the personas can be tuned (skeptic, optimist, accountant, growth advocate).

But persona simulation has a structural ceiling: all personas share Claude's training, biases, blind spots, and confidence calibration. A "skeptic persona" played by Claude is still Claude's idea of skepticism. Three Claude voices in different costumes don't break Claude's cognitive frame.

Two real models from different training labs do break the frame. Claude's blind spots are not Gemini's blind spots. When they disagree, you're seeing through ONE frame and into another — not pivoting within a single frame.

Both mechanisms have their use:
- `/council` — when you don't know which stakeholder perspectives are missing
- `/deliberate` — when you suspect Claude (or any single model) might be confidently wrong

## Why This Beats Perplexity's Multi-Model Pitch

Perplexity's bet (inferred): "multiple model perspectives synthesize into higher confidence." Their UX renders one final answer.

Our bet: "multiple model perspectives surface contradictions, and contradictions are the real value." Our UX renders the disagreement explicitly.

If Perplexity is right and synthesis-confidence is what users want, they win the casual market. If we're right and contradiction-honesty is what users want for high-stakes work, we win the consequential market.

Critically — we have no way of forcing Farrice to pick which we want. We just have to default to honesty and let the choice play out. If `/deliberate` outputs feel "harder" than `/council` outputs, that's not a UX bug — that's the design.

## Why This Is an Atom, Not a System

Per CLAUDE.md's atom-vs-system convention, atoms are single-tool single-job deliverable producers. Systems orchestrate multiple atoms with phase gates.

`/deliberate` is unambiguously an atom:
- One deliverable type (a deliberation block)
- One workflow file (5 steps, all in-band)
- No internal phase gates
- No multi-skill composition (just Claude + one Gemini call)

It can be COMPOSED INTO systems. A `/supercomputer` brand build can invoke `/deliberate` at the positioning decision step — "Claude says premium, Gemini says accessible, surface the disagreement before locking the brand bible." But `/deliberate` itself doesn't orchestrate anything; it's a tool.

## Anti-Patterns (Sourced)

Every anti-pattern below is already load-bearing in this skill's own build files — cited here so the audit trail runs through real, dated content rather than fresh assertion. Skill built 2026-05-25 (commit `30a0d6345`, "feat(deliberate+anchor-memory): multi-model deliberation + mission templates + visual board"); reissued as a structure-pure v2 prompt 2026-07-13 (commit `8ae51279c`, "feat(wiring): forge wave 3 — 161 born-v2 prompts across 25 skills").

1. **Blending contradictions away.** `skills/deliberate/SKILL.md` (2026-05-25): "'Both make good points' is not synthesis — it's avoidance. Name a winner or explain the synthesis condition."
2. **Picking Claude every time.** `skills/deliberate/SKILL.md` (2026-05-25): "Confirmation bias dressed as deliberation. If Claude wins 5 in a row, audit your synthesis for self-favoring."
3. **Picking Gemini every time.** `skills/deliberate/SKILL.md` (2026-05-25): "Reverse bias. Same audit needed" — the mirror-image failure, named separately so self-audit doesn't stop after checking one direction.
4. **Skipping the disconfirming consideration in Step 2.** `.agent/workflows/deliberate.md` (2026-05-25): "Skipping Step 2's 'strongest argument against' — false confidence enters Step 3."
5. **Silently falling back to Claude-only when Gemini fails.** `.agent/workflows/deliberate.md` (2026-05-25): "Silently falling back to Claude-only when Gemini fails — defeats the entire point. Always surface the failure to user."
6. **Grounding a pure judgment call.** `skills/deliberate/SKILL.md` (2026-05-25): "Adding `--grounding` to a judgment-call prompt makes Gemini fetch web context that pollutes the deliberation. Use grounding only when factual surface exists."
7. **Using this for low-stakes work.** `skills/deliberate/SKILL.md` (2026-05-25): "If the decision's marginal value is under $100 or you've already made up your mind, single-model is fine. Don't burn the deliberation overhead."

## The Open Questions

Things we don't yet know — will discover after 5-10 real deliberations:

1. **How often Claude and Gemini actually disagree.** If they converge 80% of the time, the skill's value is in the 20% where they don't. If they converge 95% of the time, the skill is overkill for most prompts.
2. **Whether "name a winner" or "explain the synthesis condition" is the better default.** Step 4 currently requires picking a side. Maybe some prompts genuinely warrant "both are right under different conditions."
3. **What grounding does to disagreement rate.** Adding `--grounding` (Google Search on the Gemini side) might collapse disagreement (both models now reading the same web facts) or expand it (Gemini brings external facts Claude doesn't have).
4. **When a third voice (OpenAI GPT) would meaningfully add signal vs. add noise.** Two-voice is a clear binary. Three-voice introduces majority/minority dynamics that might be worse than two-voice clarity.
5. **Whether deliberation outputs should be anchor-memory'd by default.** If we log every deliberation as an anchor, the project's state.yaml becomes a record of "every contested decision and how we resolved it" — potentially the most valuable artifact a long-running project produces.

## The Reading List

If you only have time for one thing:
- Skill SKILL.md Step 4 "Hard rules" — the contradiction-preservation discipline

If you have an hour:
- Re-read the existing `.agent/workflows/council.md` to see how the single-model multi-persona pattern works
- Re-read `execution/gemini_client.py` to understand what Gemini's giving us
- Read CLAUDE.md "Skill Architecture — Atoms vs Systems" to see why this is an atom

## What This Skill Is Not

This is NOT:
- A truth-finder. Both models can be wrong. The deliberation just makes one model being wrong harder to hide.
- A consensus engine. Convergence is a finding, not a feature.
- A "find the right answer" tool. The user still has to decide. The skill makes the decision-shape clear.
- A research tool. Use `/deep-research-gemini` if you need ground-truth facts.

It IS:
- A frame-breaker. When you're stuck in Claude's frame, Gemini's frame is the cheap way out.
- A confidence calibrator. Cross-model disagreement is a strong signal that your own confidence should adjust.
- A decision-shaper. After a good deliberation, you know what assumption you're actually making.
