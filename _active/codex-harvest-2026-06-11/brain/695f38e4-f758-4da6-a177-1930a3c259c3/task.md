# Token Efficiency Overhaul — Three Moves

## Move 1: Tiered Kickoff (Sport Mode / Race Mode)
- [x] Write implementation plan
- [x] Rewrite `session-kickoff.md` with two modes
- [x] Rewrite `end-session.md` with ambient logging
- [x] Update `session_workspace.py` with `create-if-needed`

## Move 2: Internalize the Chain's Lightweight Steps
- [x] Write implementation plan
- [x] Add Chain Efficiency Rules to `GEMINI.md`/`CLAUDE.md`/`AGENTS.md`
- [x] Add Hot Context tier to Context Engine table
- [x] Mirror changes to all 3 system files
- [x] Add Rule 5 + Rule 6 to `token-efficiency-protocol.md`

## Move 3: Hot Context Cache
- [x] Write implementation plan
- [x] Add Hot Context Stack section to `session-state-protocol.md`
- [x] Add Hot Context Stack to anchor format template

## Verification (Next Session)
- [ ] Dry-run Sport Mode kickoff (simple request, no ceremony)
- [ ] Confirm Chain skips file reads for known-domain routing
- [ ] Confirm Hot Context prevents redundant expert loads
