---
thread: codex-parity
status: ready
resume_hint: Jam: felt verdict on take-a vs take-b, then re-run A/B under new AGENTS.md voice rule
unfinished: Jam verdict; A/B re-run; Farrice-only: Gemini credits + Copilot MCP re-auth
branch: main
pin: true
---

# Codex Parity — Live-Fire Hooks + Cross-Platform Harness Repair (CLI 0.144.3, A/B Proof)

## Purpose
- **Next session should do:** run the jam — Farrice's felt verdict on the two golden-brief takes — then re-run the A/B on Codex to confirm the voice-card gap closed; relay the two Farrice-only fixes below.
- **Not in scope:** re-verifying the hook layer (live-fire receipts exist), rebuilding the raw-intent bridge, anything against the Gemini CLI (dead platform, EOL'd 2026-06-18).

## Load First
- `_active/codex-parity-2026-07-13/proof/JUDGMENT.md` — the A/B scorecard + the one actionable gap (voice card), already patched
- `_active/codex-parity-2026-07-13/proof/take-a-claude-code.md` + `take-b-codex.md` — the jam material
- `docs/solutions/2026-07-13-codex-hooks-config-present-not-firing.md` — live-fire verification method; read before ANY "is X wired?" question
- `AGENTS.md` §"Hooks on Codex" + §"Voice layer" — the rewritten constitution sections the re-run tests
- `.agent/handoffs/2026-07-13-codex-parity.md` — full mission record (what shipped, do-NOTs)

## Current State
- **Objective:** Codex↔Claude Code output parity, operator-console visibility for both platforms.
- **What is already done:** CLI 0.133.0→0.144.3 (0.133 was a total outage vs gpt-5.6-sol); full hook chain live-fire verified on Codex (shell→`Bash` matcher; native file reads fire nothing); JCC SessionStart fixed (`hookEventName` required by Codex, patched in 3 copies); AGENTS.md/CODEX.md/GEMINI.md rewritten to verified reality + re-blessed; `raw_intent_run_packet.py` now compiles Mission Cards (goal spine + `.agent/missions.jsonl`, `platform: codex`); routing 'wiring' misfire fixed (27/27 golden); gemini_deep = depleted Google prepay credits (billing, not code); solution card saved.
- **What is uncertain or stale:** take-b was generated BEFORE the AGENTS.md voice-card rule — the re-run is the test; Codex memories DB error (`no such table: jobs`) unexplained but cosmetic; Copilot MCP token expired.
- **Latest proof/receipt:** live-fire probe output (all hooks Completed), `verify_control_intent.py` 27/27, `verify_raw_intent_run_packet.py` green, `verify_google_operator_core.py` PASS, both takes pass `prose_classifier.py`.

## Suggested Skills / Workflows
- `/resume codex-parity` — surfaces this thread with the full mission record
- `/jam` protocol (memory: project_jam-protocol.md) — two takes → gut verdict → taste ledger
- `/voice-ratchet` — bank the felt verdict silently in-session after the jam

## Exact Next Prompt
```text
/resume codex-parity — jam time: show me take-a and take-b side by side from _active/codex-parity-2026-07-13/proof/, take my gut verdict, bank it via voice-ratchet, then re-run the same golden brief on Codex (codex exec, read-only) and tell me if the voice-card rule in AGENTS.md closed the texture gap.
```

## Acceptance Criteria
- Farrice's verdict recorded against both takes (taste ledger entry)
- Fresh Codex take generated under the new AGENTS.md; side-by-side delta named (texture anchors present/absent)
- Verdict + delta noted on the codex-parity thread handoff

## Risk Notes
- Farrice-only, cannot be done by an agent: Gemini prepay credits top-up at ai.studio/projects (research floor is $0 Tavily meanwhile) · GitHub Copilot MCP re-auth on Codex (or remove the server)
- GOLDEN RULE: no live Codex session while Claude Code drives this tree — `codex exec` probes are fine, interactive Codex is not
- Never edit `.codex/hooks.json` directly (trust-hash invalidation silently kills all hooks); change target scripts instead
