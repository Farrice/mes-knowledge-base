---
title: "Codex on gpt-6-astra explains failures and stops: restore the two base-prompt rules Sol had"
date: 2026-09-09
status: solved
tags: [codex, gpt-6-astra, model-dialect, hooks, jen]
---

# Symptom

Codex sessions on Jen's content studio (Sept 4–9, 2026) narrate the failure correctly, then end the turn. Farrice: "you're able to articulate why we get the problem… but then you're not able to deliver on the execution or fix." Same harness as the Sol era: approval policy, sandbox, hooks byte-identical. Tool calls per user turn fell from 37 (gpt-5.6-sol) to 13 (gpt-6-astra); prose per tool call tripled; raising effort made it worse.

# Cause (verified from `session_meta` in `~/.codex/sessions/2026/09/**`)

OpenAI's Astra base prompt dropped two rules Sol carried:

1. Skill on description match went from "you must use that skill for that turn" to "use reasonable judgement… do not use a skill based solely on… availability." SKILL.md references per turn: 7.4 → 0.4.
2. The request-type routing table (Answer / Diagnose / Change-or-build / Monitor, with "Diagnose: do not implement the fix") was removed. A compound ask ("this is bad, fix it") now resolves to Diagnose.

Also new: permission framing leads the prompt; "do not treat exceptions to requirements in local markdown and skill files as automatically requiring user approval" (Astra acted on it by suppressing Farrice's global steering rules on 09/08). OpenAI's own guide says Astra "sometimes stops where users expect it to keep going" and is "more sensitive to contradictory instructions in AGENTS.md." Community reproductions: openai/codex #43329, #43193.

Not the cause: Farrice's prompting (sufficient in both eras), the workspace (the approved caption came from the "wrong" workspace), effort level.

# Fix (one lane, one re-trust)

- `directives/model-dialects/gpt-6-astra.md`: card with machine-dialect JSON (route ANSWER / DIAGNOSE / BUILD; skill-on-match = must; receipts, never claims; his rules outrank judgement).
- `AGENTS.md` § Execution Bias Contract rewritten in place to restore both rules plus OpenAI's two recommended bias-to-action sentences.
- `semantic_libraries/antigravity/primitives/operating-alignment-contract.md` outcome-next-proof block: four route/receipt lines, Codex-only per-turn path.
- `execution/hooks/steering_loop_hook.py`: `_under_codex()` + `_codex_config_model()`; under Codex the model resolves from `config.toml`, never the Claude default seat.
- `.codex/tools/codex_hook_runner.py`: TARGETS gained steering-loop, session-brief, session-alarm, lane-bootstrap, superseded-read; plain stdout is wrapped in `hookSpecificOutput.hookEventName` (Codex hard-requires it); `ANTIGRAVITY_HARNESS=codex` set for shared hooks.
- `.codex/hooks.json`: SessionStart (bootstrap, alarm, brief), UserPromptSubmit steering-loop, Stop steering-loop, PostToolUse superseded-read. One edit → one Desktop re-trust.
- `execution/verify_dialect_injector.py`: five Astra cases (31/31 pass).

# How to verify it fired (config presence is not proof)

```bash
codex exec --skip-git-repo-check --sandbox read-only "Run exactly one shell command: echo probe. Then stop."
```
Then grep the newest `~/.codex/sessions/2026/MM/DD/rollout-*.jsonl` for `card: gpt-6-astra` and `SESSION BRIEF`. Runner-level probe without Codex: pipe a UserPromptSubmit payload into `codex_hook_runner.py steering-loop prompt` and expect the JSON envelope with the card.

# Reuse

Any model swap on Codex = new card in `directives/model-dialects/` with `model_match` and the `config.toml` id; no hook code changes. If a future base prompt restores the routing table, the card's deliverable lines can shrink; the re-probe triggers are in the card.
