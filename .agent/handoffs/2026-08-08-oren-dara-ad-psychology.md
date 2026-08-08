---
thread: oren-dara-ad-psychology
status: ready
resume_hint: Approve render (gate clears gemini-image/higgsfield-nano) and run the 3-variation Sunday/Monday batch from the locked spec
unfinished: Render + 2 practitioner receipts + Farrice blind-pass verdict for A-tier
branch: main
pin: true
---

# Extraction: Oren×Dara Ad Psychology - Forged and Deployed

## Purpose
- **Next session should do:** (1) render the MyBPM Sunday/Monday static — cost-gate approval was the only blocker (hook denied `generate_image.py` as 'fal-poster'; both `gemini-image` and `higgsfield-nano` CLEAR the gate at $0.05-0.10, budget untouched); (2) run the two practitioner receipts gating the LinkedIn founder-mirror concepts (anchor the $40K story to the real instance; actually run the nine-homepage sweep, ~10 min); (3) get Farrice's blind-pass verdict on `oren-dara-ad-psychology` for A-tier promotion (EVAL-048 is model-judged PASS only).
- **Not in scope:** re-extracting the source video (done, forge-tier); rebuilding any dara-denney or oren-* skill (extend never rebuild); posting the LinkedIn concepts before their receipts + writers-room pass.

## Load First
- `skills/oren-dara-ad-psychology/SKILL.md` + `genius.md` — the new skill: six tactics, rubric, vetoes (10 workflows `/adpsy-*`, front door `/oren-dara`)
- `_active/mybpm/mybpm-merch-os-run-1/04-deliverables/11-adpsy-chain-sunday-monday-static.md` — locked static spec (KEEP verdict) awaiting render
- `_active/mybpm/mybpm-merch-os-run-1/04-deliverables/12-sunday-monday-yapper-script.md` — shoot-ready video script (prose CLEAN)
- `_active/farrice-brand/content/bank/2026-07-19-adpsy-founder-mirror-concepts.md` — 3 concepts, CLEAN 0/10, receipts owed
- `_active/linkedin/02-offer/AD-PSYCHOLOGY-AUDIT-MODULE.md` — P2M Stage-2 module (extends the OS)
- `extractions/oren-dara-ad-psychology/` — extraction report, amplification report, blind-pass sample + corpus

## Current State
- **Objective:** turn the Oren John × Dara Denney Cannes 2026 video (FFU45SKaeYM) into deployed arsenal + first revenue-pointed deployments.
- **What is already done:** forge-tier extraction (frame-verified), skill built + registered (renaissance audit 0-fail, heartbeat 6/6, blind-pass EVAL-048 model-PASS), first full chain run on MyBPM (tactic brief → taboo build with veto log → 3-layer static spec KEEP → yapper script), 3 LinkedIn founder-mirror concepts (prose CLEAN after one gate-forced rewrite), Ad Psychology Audit module filed. Finalizes logged (composites 8.0 / 7.67 / 8.0). All committed + pushed (`895471ba3`, `5290371`).
- **What is uncertain or stale:** the render never happened (gate denial, surfaced); MyBPM customer voice is community-lexicon (pre-launch, MEDIUM confidence — first real comment mine due 7-14 days after any ad goes live); the one-raver register check on the Sunday/Monday line is owed before spend.
- **Latest proof/receipt:** chain_runner traces 2026-07-19 (3 finalizes), eval_set_v1 EVAL-048, forge_gate record for oren-dara-ad-psychology.

## Suggested Skills / Workflows
- `/adpsy-comment-mine` — run 7-14 days after the MyBPM test goes live (first real customer voice)
- `/dara-static-production` — the render path once the gate is approved
- `writers-room` — final pass on the 3 LinkedIn concepts after receipts
- Forge Radar item: `creative_router.py` regex false-positives on "no people" → routes to higgsfield-soul; 5-min negation fix

## Remaining Priority
Render the Sunday/Monday static (gate-approved route), close the two practitioner receipts, and record Farrice's blind-pass verdict for A-tier.

## Exact Next Prompt
```text
Approve and run the MyBPM Sunday/Monday render: route through the cleared image service (gemini-image or higgsfield-nano, both pass cost_gate check), 3-variation batch at 4:5 from the locked spec in _active/mybpm/mybpm-merch-os-run-1/04-deliverables/11-adpsy-chain-sunday-monday-static.md, then edit-to-refine the winner and file renders + QA sheet. After that: run the nine-homepage sweep and anchor the $40K receipt so the LinkedIn concepts are ship-true.
```

## Acceptance Criteria
- Rendered 4:5 static files exist in the MyBPM deliverables dir, gate-logged with actual cost
- Both practitioner receipts recorded in the concepts file (sweep screenshots exist; $40K story anchored or softened)
- Farrice's blind-pass verdict recorded via `blind_pass.py record` (A-tier or named gap)

## Risk Notes
- Concurrent sessions have been active on this tree all week — claim `session_lock` before multi-file work
- Do not bypass the cost gate; the denial path is approve-then-run, logged
- LinkedIn concepts carry hard vetoes (teardown rule: no named brands publicly; claim-safe editorial-only)

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-07-19-oren-dara-ad-psychology.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
