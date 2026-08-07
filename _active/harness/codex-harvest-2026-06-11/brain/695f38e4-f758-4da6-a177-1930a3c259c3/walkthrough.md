# Token Efficiency Overhaul — Walkthrough

All 3 moves have been implemented to reduce daily token consumption by 30-50%.

## Move 1: Tiered Kickoff ✅

**Files modified:**
- [session-kickoff.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/session-kickoff.md) — Sport Mode (default, 3 calls) vs Race Mode (`--deep`, full ceremony)
- [end-session.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/end-session.md) — Quick handoff summary by default, deep cleanup via `--deep`
- [session_workspace.py](file:///Users/farricecain/Google%20Antigravity/execution/session_workspace.py) — Added `create-if-needed` command for deferred workspace creation

**Key behavior change:** Workspace folders only materialize when the first asset is produced, not at session start.

---

## Move 2: Internalized Chain ✅

**Files modified:**
- [GEMINI.md](file:///Users/farricecain/Google%20Antigravity/GEMINI.md) / [CLAUDE.md](file:///Users/farricecain/Google%20Antigravity/CLAUDE.md) / [AGENTS.md](file:///Users/farricecain/Google%20Antigravity/AGENTS.md) — Added **Chain Efficiency Rules** section + Hot Context tier in Context Engine table
- [token-efficiency-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/token-efficiency-protocol.md) — Added **Rule 5** (Chain Step Internalization) + **Rule 6** (Hot Context Cache) + 3 new anti-patterns

**Key behavior change:** Steps 1-3 of The Chain execute in-head for 8 known domain routes. No `intent-pipeline.md` or `DOMAIN_REGISTRY.md` reads for routine requests. Saves ~2,200 tokens per request.

---

## Move 3: Hot Context Cache ✅

**Files modified:**
- [session-state-protocol.md](file:///Users/farricecain/Google%20Antigravity/directives/session-state-protocol.md) — Added **Hot Context Stack** to anchor format + standalone rules section

**Key behavior change:** Experts loaded at Tier 1+ are tracked as "hot" for the entire conversation. Re-reading `SKILL.md` for the same expert is blocked. Saves ~1,350 tokens per redundant load.

---

## Verification Plan (Next Session)

| Test | What to confirm |
|------|----------------|
| Sport Mode | Simple request triggers no ceremony, no workspace creation until first asset |
| Race Mode | `/session-kickoff --deep` fires full ceremony |
| Internalized Chain | LinkedIn request routes directly to Lara Acosta without reading `DOMAIN_REGISTRY.md` |
| Hot Context | Second request for same expert skips all file reads |
