# Codex Parity Runbook — 2026-07-06 Frontier Session

> Execute this in a **Codex** session on this repo to verify and complete parity with the 2026-07-06 Claude Code frontier session (branch `feat/harness-frontier-loops`, ~37 commits, 6 missions). Almost everything shipped is platform-neutral (repo workflows, execution scripts, launchd jobs, shared hooks). This runbook verifies the Codex surface and closes the few gaps that are Codex-specific.
> **GOLDEN RULE FIRST**: confirm no Claude Code session is driving this repo (`git status` clean of surprise churn; the `active_tool_lock` hook will warn if another driver stamped recently).

## What shipped (inventory — all in-repo, already available to Codex)

| Layer | What's new | Codex entry point |
|---|---|---|
| Front doors | `/go` (anti-bottleneck staging), `/create` (universal content conductor) | `.agent/workflows/go.md`, `.agent/workflows/create.md` via SLASH_COMMANDS.md |
| Doctrine | `directives/peak-operation.md` — operating shape, routing table, drift signals, invariants | Load when orchestrating (AGENTS.md points to it) |
| Router learning | always-rank + feedback loop (`routing-intelligence.json`), nightly weights (`.agent/skill-weights.json`), report card (`.agent/router-report-card.md`), hybrid embeddings behind `SKILL_ROUTER_EMBED=1` | `execution/skill_router_hook.py` + `find_skill.py` — fired by `.codex/hooks.json` skill-router |
| Safety hooks | `active_tool_lock` (GOLDEN RULE guard), `guard_stranded_deliverables` | wired in `.codex/hooks.json` via `codex_hook_runner.py` TARGETS (Wave 1b) |
| Memory | `thought_bank.py` deterministic capture (+ `/dump` delegation, nightly backstop), memory facade semantic on `.venv` python | `execution/thought_bank.py`; codex_hook_runner already prefers `.venv/bin/python` |
| Compliance | `skills/claim-safe-health-marketing/` (`/claim-safe`), `claim_risk_scan.py` auto-fires in `chain_runner.py finalize` Step 2.6 | shared — finalize path is platform-neutral |
| Outer loop | COS daily brief Outer Loop section, `revenue_tracker.py checkin` interactive | shared launchd + CLI |
| Evolution | Phase 3 lifted, regression suite repaired (declared-domain matching), `finalize --auto` | shared |
| Notion | `create_knowledge_vault_entry` rich bodies; 250/250 backfilled | shared (`notion_api.py`) |
| Constitutions | single-source blocks `directives/constitution-core/` + `platform_compiler.py compile --check/--write` (daily observe check) | shared; AGENTS.md carries BEGIN/END markers |
| Spend | Fal guard deterministic recording + STATE STALE warning | shared scripts |

## Verification checklist (run each, expect PASS)

```bash
.venv/bin/python3 execution/verify_codex_claude_parity.py            # expects 8 Codex hook commands — PASS
.venv/bin/python3 execution/verify_memory_stack.py                   # venv + genai + facade smoke
echo '{}' | .venv/bin/python3 .codex/tools/codex_hook_runner.py active-tool-lock   # exit 0
echo '{}' | .venv/bin/python3 .codex/tools/codex_hook_runner.py guard-stranded     # exit 0
echo '{"prompt":"write landing page copy for a fitness coach","session_id":"codex-parity"}' | .venv/bin/python3 execution/skill_router_hook.py   # suggestion JSON emits
.venv/bin/python3 execution/claim_risk_scan.py scan <(echo "reverses type 2 diabetes in 30 days") # DISEASE_CLAIM
.venv/bin/python3 execution/thought_bank.py stats                    # runs clean
.venv/bin/python3 execution/platform_compiler.py compile --check     # in-sync (after baseline re-bless)
grep -n "「/go」\|/go\b" SLASH_COMMANDS.md | head -2                  # /go registered
```

## Codex-specific gaps to close (the actual work)

1. **Session-ledger stop parity**: confirm `.codex/hooks.json` fires `session-ledger stop` (Operator Lesson 3-prompt nudge added there today). If the stop event isn't wired on Codex, add it following the existing hooks.json entry shape.
2. **Recall on Codex**: `.codex/config.toml` lists a recall MCP server — verify it's authenticated on the Codex side (Claude side was re-authed 2026-07-06; auth does NOT transfer). `/create` Stage 2 degrades to perplexity+research.py if recall is down, but fix it if possible.
3. **`~/.codex/skills/` staleness**: AGENTS.md already says repo skills win. Do NOT re-port; if any Codex-side skill port shadows `/go`, `/create`, or `/claim-safe`, delete the stale port.
4. **CODEX.md refresh**: add the same front-doors + doctrine pointer block that AGENTS.md gained on 2026-07-06 (grep AGENTS.md for "Front doors (2026-07-06)") anywhere CODEX.md describes command surfaces.
5. **Known cleanup (either platform)**: `.agent/workflows/analyze-intent.md` contains misfiled SEO-audit content, not intent analysis — rename it to what it is (e.g. `seo-keyword-audit.md`) and regenerate registries (`sync_registries.py`).

## Report format
Return a parity table: check → PASS/FAIL/FIXED, plus anything Codex-specific you repaired. Commit surgical fixes with clear messages. Do not restructure anything that passes — this session's rule was: extend, never rebuild.
