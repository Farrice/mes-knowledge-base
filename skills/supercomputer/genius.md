# Antigravity Supercomputer — Genius

The philosophy doc. Read this when the SKILL.md isn't enough — when you need to understand *why* the design choices are what they are, not just what to execute.

---

## How to Use This Skill (Model Calibration)

The four phases are load-bearing tool calls, not a narrative frame to gesture at. If the output narrates "loading anchor memory" and "checking the cost gate" in confident prose without the actual `anchor_memory.py` / `cost_gate.py` / `anchor_verify.py` invocations underneath, the mission has failed — regardless of how fluent the phase-by-phase narration reads. The test: would a careful reviewer recognize this as a real Supercomputer mission — anchors that literally propagate the earlier deliverable's actual terms into later prompts, dollar figures pulled from a real SERVICES lookup — or as a task list wearing Supercomputer vocabulary (four phase headers, the word "anchor" used once, a plausible-sounding dollar figure that was never looked up)? If it's the second, rebuild before shipping.

Specifically:
- Do NOT print the Mission Plan banner and then skip straight to output. "Proceed? (y / adjust / cancel)" is a real gate, not a stage direction — wait for the explicit approval.
- Do NOT invent a cost estimate. Every dollar figure traces to `execution/cost_gate.py`'s SERVICES dict or an actual `creative_router.py` route call — a plausible "$0.75" that wasn't looked up is the single most common Supercomputer failure mode, and it is exactly the failure this skill exists to prevent: "Our cost gate shows USD. That alone is a moat" only holds if the USD figure is real.
- Do NOT skip Phase 3 because the deliverables "look" coherent. `anchor_verify.py` scoring is the only thing separating a Supercomputer mission from "ChatGPT + image gen plugged in" — a mission that never runs the verifier hasn't earned the label no matter how good the prose reads.
- Polish is the tell here in a specific way: a mission that narrates all four phases smoothly, in order, with confident phase headers, but never actually shells out to `anchor_memory.py`, `cost_gate.py`, or `anchor_verify.py` has reproduced the exact "credit math obscures actual spend" failure this system was built to route around — self-inflicted instead of vendor-inflicted.

---

## The Single Thesis

**Higgsfield Supercomputer is not a novel AI architecture. It is a UX pattern.**

The pattern: take a sequence of disconnected generative calls (image, video, copy, brief) and make them feel like one unified agent through two mechanics:

1. **Anchor memory** — early outputs become persistent context that later outputs must reference.
2. **Pre-flight cost preview** — every paid call shows estimate before render and waits for approval.

That's it. Strip those two mechanics away and Higgsfield Supercomputer is "ChatGPT with image gen plugged in." Add them, and the same toolchain feels like a Creative Director who remembers what you decided and won't waste your money.

Both mechanics are non-technical. Anyone with a directory of files and a cost table can implement them. The reason Higgsfield charges $99/mo for them is distribution + brand, not technology. Hermes Agent (the open-source framework underneath their Supercomputer) is MIT-licensed.

## Why "Anchor Memory" Is the Killer Mechanic

Without it: you generate a product hero shot in step 3, then in step 4 you ask for "3 listing visuals" and the model invents 3 unrelated product orientations because it has no memory of what step 3 looked like. Result: incoherent listing.

With it: step 3's output is registered as an anchor with `ref_for: [listing_visuals, ad_concepts]`. In step 4, the prompt explicitly loads the anchor — the product orientation, lighting, framing all become required references. Listing visuals stay coherent with the hero.

This is the difference between a "marketing assistant" that produces 8 things and a "brand operator" that produces 8 cohesive things. Same models, same prompts, completely different output quality. The anchor is the unifying thread.

**Practical implementation rule**: every deliverable in `projects/<slug>/state.yaml` `anchors` list with a non-empty `ref_for` field is a HARD requirement for the downstream phases listed there. Failing to reference = mission failure, regardless of individual deliverable quality.

## Why "Pre-Flight Cost Preview" Is the Trust Mechanic

The Bad Decisions Studio review of Higgsfield: $200/mo plan, two chats, 4% of budget burned. Without preview, every prompt is a potential bill surprise. With preview, every prompt is a transparent transaction.

This is not just a budget feature. It's a **trust feature**. When the agent shows you a $1.40 plan and you approve it, you're not just authorizing spend — you're entering a contract: "I trust you to deliver these specific things at this specific cost." When delivery matches the contract, trust compounds. When it doesn't, trust collapses faster than any single failed deliverable could cause.

Higgsfield's failure mode here: they show *credit costs*, not dollar costs. Credit math obscures actual spend. Our cost gate shows USD. That alone is a moat.

**Practical implementation rule**: every paid creative API call passes through `cost_gate.py check` BEFORE firing. No exceptions. The auto-approve threshold ($0.20 default) exists only to prevent micro-friction on the cheapest calls — anything cinema-tier or video-tier always asks.

## Why This Is a System, Not an Atom

Per CLAUDE.md's atom-vs-system convention (added 2026-05-12), atoms are single-tool single-job deliverable producers. Systems orchestrate multiple atoms with phase gates and shared state.

Supercomputer is unambiguously a system:
- Composes 6+ existing skill systems (BOS, parallax, ghostwrite, fantastic-posters, design-md, jcc-deploy)
- Composes 5+ paid creative APIs (Fal modes, Higgsfield MCP variants, Veo, Gemini Image)
- Has explicit phase gates (Phase 0 → 1 → 2 → 3 → 4)
- Maintains shared state across phases via anchor_memory.py
- Has human-in-loop checkpoints (cost gate, plan approval, finalize quality scoring)

It is the **system of systems** for the marketing/creative domain — the single conversational front door that makes the 232 existing skills feel like one unified agent rather than a toolbox.

## Why Build Instead of Subscribe

The Higgsfield Ultra subscription is $99/mo + credit burn (real-world ~$200-2000/mo for serious workflows). The build cost is ~8-10 hours of one-time work. Beyond cost:

1. **Confidentiality**: Higgsfield ToS grants them irrevocable rights to user content. Building locally keeps client work confidential.
2. **Audio consistency**: Higgsfield's multi-clip Seedance videos have audio drift (reviewer-confirmed). Our `creative_router.py` routes multi-shot to Kling v3 (no drift) or single-take Seedance — turning their failure into our default.
3. **Skill compounding**: Every new skill we build in `skills/` automatically becomes available to the Supercomputer. Higgsfield's marketplace is thin. Ours is 232 skills deep.
4. **Brain choice**: Higgsfield defaults to Gemini 3.1 Pro as Orchestrator. We use Gemini Ultra ($100/mo flat) for the same brain with zero credit-per-call cost.
5. **Direct model access**: Higgsfield MCP gives us the same Soul / Cinema Studio / Seedance / Nano Banana / Kling models without the Supercomputer credit markup.

## The Higgsfield Failure Mode (Don't Replicate)

Higgsfield's UGC ad workflow stitches multiple Seedance clips together. Each clip has its own internal TTS state. Result: voice/audio inconsistency across cuts — the same character sounds different in clip 1 vs clip 2.

Our `creative_router.py` defaults multi-shot video signals to Kling v3 Pro instead, because Kling generates multi-shot natively in one pass. For single-take cinematic, Seedance 720p is fine. The router note on the Seedance rule explicitly warns: "Audio NOT consistent across multi-clip stitches — use single-take only."

This kind of constraint encoding is what taste looks like in code. Don't strip these notes when refactoring.

## Anti-Patterns (Sourced)

Every item below is a real, dated failure or rule — pulled from this skill's own build history and its production trace log, not inferred from general orchestration theory.

- Batch-finalizing collapses the mission's real quality signal — the Resonance launch mission's five deliverables were finalized in five separate `chain_runner.py` calls one minute apart on 2026-05-25 (`evolution_store/v2_traces/trace_20260525_232154_supercomputer.json` through `trace_20260525_232226_supercomputer.json`), each carrying its own anchor id ("Anchor-004" through "Anchor-010") and its own adversarial score — batch them into one call and that per-deliverable signal disappears.
- Anchor propagation must be verified, not assumed — this file's own Open Questions log records the fix, dated 2026-07-09 (Wave 2): "`execution/anchor_verify.py check --anchor <path> --targets <paths>` grep-detects anchor key-term coverage in dependent deliverables and scores propagation 1-10" — before that date, Phase 3 was aspirational language with no enforcement mechanism behind it.
- Never silently bypass a cost-gate denial — `directives/supercomputer-mode.md` (dated 2026-05-28, the skill's build commit) states the rule flatly on one line: "Never silently re-route. Never silently skip. Always surface the choice." — swapping a cheaper model on a denial without asking violates this the moment it happens.
- Never substitute a model the user didn't approve — `SKILL.md`'s own Anti-Patterns list (same 2026-05-28 build, last touched 2026-07-13) states it as a standalone rule: "If the user approved Seedance and you'd prefer Kling, ASK — don't substitute." — this is the Higgsfield audio-drift fix turned into a consent rule, not a silent routing upgrade.
- A retry-once policy only works if the retry fixes the actual failure — two consecutive `daily-zeitgeist-brief` supercomputer traces on 2026-07-01 (`evolution_store/v2_traces/trace_20260701_063818_supercomputer.json` and `trace_20260701_063839_supercomputer.json`) both scored `intent_alignment: 4.0` even though the second run's own notes say "Retry after intent-alignment receipt patch" — the retry fixed the receipt, not the alignment, and the mission shipped at the same broken score anyway.
- Reimplementing an existing skill inside the mission workflow defeats the composition model — `SKILL.md`'s Anti-Patterns item 3 states it plainly: "If `/parallax` exists, you compose it; you don't rewrite its logic inside the supercomputer workflow." — every layer in the Composes table exists precisely so this orchestrator never needs its own copy of another skill's logic.

## When to Break the Pattern

Three legitimate reasons to bypass the Supercomputer workflow:

1. **Single-deliverable scope.** "Write me one LinkedIn post" → use `/ghostwrite` directly. Anchor memory is overhead.
2. **Existing project incremental work.** "Add a hero image to the [existing-project] brand" → load `projects/<existing>/state.yaml` manually, run the right skill directly. Don't re-trigger the full 4-phase flow.
3. **Diagnostic / review work.** "Look at this draft and tell me what's weak" → that's `/writers-room` or `/adversarial-review`, not a multi-phase mission.

If you're not sure: lean Supercomputer. The overhead is small (one anchor_memory call + one cost_gate call per phase) and the cohesion gain is large.

## The Open Questions

Things we don't yet know — will discover after 5-10 real missions:

1. **Optimal auto-approve threshold.** $0.20 is a guess. Likely too low for "make 10 variations" workflows ($1 total but per-call is cheap), likely too high for habitual users.
2. **Anchor-memory propagation enforcement.** ~~Currently relies on the workflow being followed.~~ **Answered (Wave 2, 2026-07-09):** `execution/anchor_verify.py check --anchor <path> --targets <paths>` grep-detects anchor key-term coverage in dependent deliverables and scores propagation 1-10; Phase 3 now gates on overall ≥7. Remaining open sub-question: the right term weights for image-heavy missions.
3. **Cross-project anchor sharing.** When building two brands in the same niche, should anchor learnings (audience insights, palette experiments) cross-pollinate? Probably yes, but the mechanism is TBD.
4. **Scheduled / recurring missions.** "Every Monday, run a content drop based on last week's thought-bank." Claude Code's `/schedule` and `/loop` provide the hook. Wiring it into Supercomputer is Phase 2.
5. **Public skill marketplace.** When external collaborators want to contribute skills, do we use Hermes Agent's marketplace format or our own? Defer until we have collaborators.

## The Reading List

If you only have time for two things:
1. The Higgsfield Supercomputer demo video (May 19, 2026) — for the UX pattern.
2. `extractions/creative-direction/higgsfield_pipeline.md` (in this repo) — for the tool surface.

If you have an hour:
- Hermes Agent technical review (tokenmix.ai) — for the architecture we're emulating without paying for.
- The Bad Decisions Studio critical review — for the failure modes we're routing around.
- CLAUDE.md "Skill Architecture — Atoms vs Systems" section — for why this is a system.
