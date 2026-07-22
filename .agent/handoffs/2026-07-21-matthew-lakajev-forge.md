---
thread: matthew-lakajev-forge
status: ready
resume_hint: Farrice blind pass on the Lakajev specimen → A-tier; then /ml-closed-lost for Signal Pilot sends
unfinished: A-tier pending human blind pass; closed-lost + opinion-ladder not yet deployed on Farrice's own pipeline
branch: main
pin: true
---

# Matthew Lakajev Skill — Forge Expansion #2 (Six Gates + Closed-Lost + /ml-*)

## Purpose
- **Next session should do:** (1) Run Farrice's blind pass — specimen vs the two real published posts, felt verdict, then `python3 execution/blind_pass.py record` an updated Farrice-judged entry if PASS → A-tier promotion. (2) Deploy the two send-systems for Signal Pilot: `/ml-closed-lost` on Farrice's own everyone-ever-chatted-to list and `/ml-opinion-ladder` on live LinkedIn engagement signals (send-before-build binding — these ARE sends).
- **Not in scope:** Re-extracting the Agency Podcast (fully mined — extend, never rebuild); new workflow builds for this skill; funnel/content builds ahead of sends.

## Load First
- `extractions/matthew-lakajev-linkedin/blind-pass-specimen-closed-lost-post.md` — the generated specimen for Farrice's side-by-side
- `extractions/matthew-lakajev-linkedin/reference-corpus/` — the 2 real published Lakajev posts (provenance-lined)
- `skills/matthew-lakajev-linkedin/SKILL.md` — v3.0 manifest: 13 workflows in 3 tiers, stacking guide, 8 v2 prompts
- `skills/matthew-lakajev-linkedin/genius.md` — expanded spine (Six Gates named model, closed-lost, opinion ladder, quality-time doctrine)
- `extractions/matthew-lakajev/mastery-extraction-agency-podcast.md` — vision + full MES extraction (checkpoint artifacts for review)

## Current State
- **Objective:** Lakajev conversation-layer expansion shipped and registered; awaiting human blind pass; ready for production use.
- **What is already done:** 10 new workflows (04-13), 5 new born-v2 prompts (8 total, renaissance audit 0 fail, pointers wired), 13 `/ml-*` commands live (wrappers + .claude/commands shims + SLASH_COMMANDS), AGENT.md expanded, heartbeat gate 6/6, blind pass EVAL-053 model-judged PASS, chain finalize 8.33 PASS (Notion logged), forge_gate recorded, memory saved (`project_matthew-lakajev-conversation-layer`), committed to main `21ca8201f` and pushed.
- **What is uncertain or stale:** A-tier pending Farrice's blind pass (model-judged only so far; noted tell: specimen slightly tidier than real Lakajev's inconsistent numbering). Visual context was auto-skipped (109-min video > 10-min cap) — acceptable, talking-head interview.
- **Latest proof/receipt:** trace_20260721_142944_matthew-lakajev-linkedin.json (composite 8.33) · EVAL-053 in evolution_store/ground_truth/eval_set_v1.jsonl · extractions/matthew-lakajev-linkedin/blind-pass-log.md

## Suggested Skills / Workflows
- `/ml-closed-lost` — first Signal Pilot send-work deployment (Farrice's own dormant list)
- `/ml-opinion-ladder` — convert current LinkedIn engagement signals into conversations
- `/ml-six-gates` — audit the Signal Pilot outreach path (where cold execs stall)
- `docs/solutions/2026-07-21-linkedin-authwall-corpus-via-public-post-permalinks.md` — reuse for any other "A-tier awaits blind pass" LinkedIn expert lacking a corpus

## Exact Next Prompt
```text
Run my blind pass on the Lakajev expansion: show me extractions/matthew-lakajev-linkedin/blind-pass-specimen-closed-lost-post.md side-by-side with the two posts in extractions/matthew-lakajev-linkedin/reference-corpus/ — no labels, let me guess which is generated, then take my felt verdict and record it. If PASS, promote to A-tier. Then /ml-closed-lost on my own network for Signal Pilot.
```

## Acceptance Criteria
- Farrice verdict recorded via blind_pass.py (PASS → A-tier noted in memory + blind-pass-log; FAIL → weakest checklist item fixed once, retried)
- At least one real closed-lost send batch drafted in Farrice's voice (voice-card layered, BLEND) and approved for sending

## Risk Notes
- Concurrent-session tree: another session holds the lock for signal-pilot work — coordinate before multi-file edits; this thread's remaining work is review/deploy, not builds.
- All Lakajev revenue numbers are his own claims from the podcast — presented as his claims; keep that framing in any public-facing reuse.
- Never pitch anywhere in deployed sends — one "buy now" line breaks the system's single rule.
