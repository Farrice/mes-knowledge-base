# Golden-Brief A/B — Harness Parity Judgment (2026-07-13)

**Brief (identical both sides):** 120-160-word LinkedIn post, Farrice's voice, on today's real operator lesson: config presence is not proof — a hook means nothing until you watch it fire live.

**Takes:** `take-a-claude-code.md` (CC, VOICE-CARD.md loaded) · `take-b-codex.md` (Codex 0.144.3, gpt-5.6-sol, AGENTS.md only — no voice card pointer fired)

## Harness-parity scorecard (the point of this A/B)

| Dimension | Claude Code | Codex 0.144.3 | Verdict |
|---|---|---|---|
| Hooks fired during run | full chain | SessionStart + UserPromptSubmit×3 (no tool calls → no tool hooks, correct) | **PARITY** |
| Constitution loaded | CLAUDE.md + memory | AGENTS.md auto-injected (seen in session transcript) | **PARITY** |
| Voice layer reached the model | VOICE-CARD.md loaded per binding | NOT loaded — AGENTS.md has no voice-card load rule for Farrice-named content | **GAP (fixable)** |
| Prose gate | prose_classifier PASS | prose_classifier PASS | **PARITY** |
| Brief compliance | 120 words, scene-open | ~170 words, over cap, twin-sentence ending (banned move) | CC ahead |
| Cost | in-session | 103,576 tokens for one post (AGENTS.md + skills context) | note for batching |

## Felt-verdict material (Farrice's jam, not mine)

- **A** anchors in his actual texture: 18 years coaching, the squat/bar image, specific-list close.
- **B** is clean operator prose with two structural tells (the "That is the operator trap" naming move; the twin-sentence ending "The screen finally caught the command. / That was when the automation became real.") and no personal anchor — voice-card absence shows exactly where expected.

## The one actionable gap

Codex parity for Farrice-voiced content needs ONE line in AGENTS.md: anything in Farrice's own voice → read `_active/farrice-brand/voice/VOICE-CARD.md` first (mirror of the CLAUDE.md `farrice_voice_alignment` binding). Applied 2026-07-13 — see AGENTS.md "Voice layer" note.

## Bottom line

Harness parity: **real** — gates, constitutions, and prose floor hold on both platforms after today's repairs. Output parity: CC leads on voice fidelity only where Codex's constitution was missing the voice-card pointer, now added. Re-run this A/B after the next AGENTS.md re-bless to confirm the gap closed.
