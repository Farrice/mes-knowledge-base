---
thread: kallaway-hook-mastery
status: ready
resume_hint: Judge the blind-pass sample vs the real corpus for A-tier, then run /hook-anything on the next three Cash Launch posts
unfinished: A-tier verdict pending Farrice; hook-landscape-scan never run against a live niche
branch: main
pin: true
---

# Kallaway Hook Mastery — Interrupt Theory Forge (watch + extract-forge, same-day source)

## Purpose
- **Next session should do:** Farrice judges the blind-pass sample side-by-side against the real Kallaway corpus for A-tier promotion, then deploys `/hook-anything` on the LinkedIn Cash Launch send queue.
- **Not in scope:** rebuilding or re-extracting the skill (it shipped and passed all gates); re-running the video watch (transcript + frames are stored).

## Load First
- `skills/kallaway-hook-mastery/SKILL.md` — workflow table (10 workflows, 3 tiers) + stacking guide
- `skills/kallaway-hook-mastery/genius.md` — 12 patterns, 7 exemplars, 10-dim rubric, sourced anti-patterns, recognition test
- `extractions/kallaway-hook-mastery/blind-pass-generated-sample.md` — the generated output awaiting Farrice's felt verdict
- `extractions/kallaway-hook-mastery/reference-corpus/` — 2 real-corpus pieces (his top-performing hooks; his own video's annotated open)
- `_active/linkedin/CAMPAIGN.md` — the active campaign whose posts are the first deployment target

## Current State
- **Objective:** turn Kallaway's "The Psychology of Killer Hooks" (YouTube pNIYikmYsyw, published 2026-08-05) into a deployable hook operating system covering any asset type.
- **What is already done:** full watch (deduped transcript + 100 scene-aware frames); forge pipeline complete — vision doc, `genius.md` (Interrupt Theory, 4 S's, triple-hook alignment, text-hook primacy, power-word mining, five visual categories, Lock-In Zone + four trust levers), 3 reference files, 10 workflows, 7 born-v2 execution prompts (renaissance audit 3804 pass / 0 fail), agent expansion, registries synced, 9 menu commands minted, heartbeat gate 7/7, blind pass recorded as EVAL-060. Committed and pushed as `8753da92e` (53 files).
- **What is uncertain or stale:** blind-pass PASS is **model-judged only** — A-tier requires Farrice's own side-by-side verdict. The mining tactics in the source lean on Kallaway's tool (Sandcastles); the protocol was extracted tool-agnostically, so `hook-landscape-scan` runs on Playwright/exports and has not yet been executed against a real niche.
- **Latest proof/receipt:** `python3 execution/skill_auditor.py check --skill kallaway-hook-mastery` → 0/7 failing, gate clear; `blind_pass.py record` → EVAL-060 in `evolution_store/ground_truth/eval_set_v1.jsonl`.

## Suggested Skills / Workflows
- `/hook-anything` — universal adapter; maps triple-hook channels onto LinkedIn posts, DMs, emails (campaign deployment)
- `/power-word-mine` — build Farrice's personal power-word bank from his own LinkedIn winners (needs real performance data)
- `/interrupt-hook-engine` — front door for any new content piece
- `/hook-alignment-audit` — diagnostic on existing underperforming posts
- `/kallaway-hook` — skill front door if a full structured run is wanted

## Exact Next Prompt
```text
Read extractions/kallaway-hook-mastery/blind-pass-generated-sample.md next to
extractions/kallaway-hook-mastery/reference-corpus/ and give me your felt verdict —
if it passes, promote kallaway-hook-mastery to A-tier and record it. Then run
/hook-anything on the next three LinkedIn Cash Launch posts in
_active/linkedin/CAMPAIGN.md, in my voice.
```

## Acceptance Criteria
- A-tier verdict recorded (or gap named and skill left at B-tier with the reason logged)
- Three campaign posts carry engineered hooks: 4 S's clean, channels aligned, lock-in zone with a real proof anchor

## Risk Notes
- Do not let generated hooks ship unverified proof claims — the lock-in trust anchor must reference real receipts (factual veto applies to paid/outbound assets)
- Power phrases in the sample are flagged untested; treat as hypotheses until real performance data validates them
- `hook-landscape-scan` requires live research tools — never generate a "landscape" from training memory

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
