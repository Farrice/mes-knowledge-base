---
thread: customer-truth-map
status: ready
resume_hint: Optionally commit/PR the CTM skill + token_meter; then run /customer-truth-map BUILD on a real audience (Jen FTHB)
unfinished: Production CTM run not yet done; nothing committed
branch: main
pin: true
---

# Customer Truth Map OS — Skill Build + Token Cost Ledger

**Session date:** 2026-07-06 · **Status:** ready (both deliverables shipped, registered, verified; optional commit/PR + production run pending)

## What this session built

Two independent, shipped deliverables. Nothing committed yet.

### 1. Customer Truth Map — new primary skill (Extract-Forge)
Extracted the **Blazing Zebra "Customer Truth Map"** Voice-of-Customer methodology (from the uploaded PDF + video `youtube.com/watch?v=GAVILEkfsvE`, transcript at `extractions/customer-truth-map/transcript.txt`) into a full registered skill.
- **Skill:** `skills/customer-truth-map/` — SKILL.md + genius.md + 9 references + **13 workflows** (`/customer-truth-map` orchestrator + 12 `/ctm-*`). Agent persona at `agents/customer-truth-map/`.
- **Registered:** in SKILL_INDEX.md + AGENT_INDEX.md (via `sync_registries.py`); 13 shims in `.agent/workflows/ctm-*.md` + `customer-truth-map.md`; entries in SLASH_COMMANDS.md. Invokable now as `/customer-truth-map` (alias `/ctm`).
- **Method (6 phases):** gather → clean (verbatim) → map (Say/Think/Feel/Do + Pains/Gains) → JTBD + gap table → put-to-work (copy/content/offer) → triangulate + refresh. Honesty spine = organize real customer words, never invent.
- **Wired to real tools (surpasses the manual original):** Apify Reddit + NotebookLM + Playwright gather (`references/tool-wiring.md`), Recall + memory_facade grounding, composes `/buyer-sourcer` + `/mcraney-deep-canvass` + `/consumer-posture-profile`, feeds `/copy-engine` + `/novelty-forge`.
- **Deterministic no-fabrication gate:** `execution/ctm_verbatim_check.py` — substring-checks every extracted quote against source (proven: caught a planted fabrication on real data, exit 1). Replaces the banned "AI-eyeballs-it" pattern.
- **Live-proven:** real Reddit scrape of first-time-homebuyers ($0.065 Apify spend) → real worked map at `skills/customer-truth-map/references/worked-exemplar-jen-fthb.md` (18/18 quotes verified).
- **Adversarial-reviewed + fixed:** rerouted an archived/banned `fact-verifier` dependency to the Step-5.5 Verification protocol; corrected `/consumer-posture-profile` command name + NotebookLM CLI note.
- Provenance: `extractions/customer-truth-map/extraction-report.md`.

### 2. `execution/token_meter.py` — deterministic cost ledger
Parses Claude Code transcripts (`~/.claude/projects/<slug>/**/*.jsonl`) for real, cache-aware per-session cost. Answers "what do I typically spend?" + "what would Fable 5 cost?"
- Commands: `summary`, `sessions`, `session <id>`, `project-at --model fable-5`, `snapshot`. Flags `--since --all --project --json`.
- **Verified by a 3-agent workflow** (independent from-scratch recompute matched to the penny; dedup by requestId is load-bearing — drops 9,278 dup lines; without it cost inflates 2.85×).
- **Caught + fixed a P1:** flat glob missed nested subagent transcripts (~35% of spend). Now recursive.
- **True repo spend (May 28–Jul 6, 60 sessions): $3,825.62** (main $2,486 + subagents $1,339). Typical session median **$41.46**. All-Fable-5 reprice: **$6,777 (1.77×)**. Ledger persisted at `.agent/token-usage.jsonl` + `.agent/token-usage-summary.json`.

## Next session focus
1. **(Optional) Commit + PR** the CTM skill + `token_meter.py` + `ctm_verbatim_check.py`. Currently uncommitted on `main`; branch first.
2. **Run a full production Customer Truth Map** on a real audience — `/customer-truth-map BUILD` on **Jen FTHB** (has real source language) or the **Invisible Expert** ICP — live gather (cost-gated), not the smoke-test scale.

## Watch-outs
- Prose_classifier FLAGS the skill docs, but that's a structural false-positive for skill-doc type (the shipped kallaway skill flags identically — tables/em-dashes/markdown). Not a defect; do not gut the docs to satisfy it.
- Any paid gather (Apify/Perplexity) is cost-gated — surface projected cost, get explicit yes, never retry a denied call.
- Codex coexistence: never run Codex + Claude Code on this dir at once.

## Suggested skills (next session)
- **`/customer-truth-map`** (alias `/ctm`) — the front door for the production run (modes BUILD · APPLY · REFRESH).
- **`/resume customer-truth-map`** — pick this thread back up by name.
- **`commit-commands:commit-push-pr`** — if committing the two deliverables (branch off main first).
- **`/ctm-deepen`** — after a surface map, take it to identity-level depth via mcraney-deep-canvass + consumer-posture.
