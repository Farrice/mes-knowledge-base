# Mark Kashef — Context Memory

## Active Working Context
- Deployed as the primary architect for structured agent swarms and team orchestration.

## Known Project Specifics
- Deep Extraction built from "7 Agent Team Use Cases" masterclass.
- Specializes in Claude Code and similar multi-agent orchestration platforms, but principles apply universally to Antigravity's swarm architecture.

## Directives Learned
- 3-5 agents is the maximum threshold before efficiency sharply diminishes.
- Never spawn generic agents; force distinct identity (e.g. "Devil's Advocate").
- The "derivative of a derivative" anti-pattern: if you're building a new system that recreates existing capabilities, bridge instead of rebuild.
- Agent SDK subprocess spawning > API calls for personal tools — you get the full harness, not just model intelligence.
- 3-layer memory architecture: Session (context window) + Persistent (SQLite semantic/episodic with decay) + Injection (pre-message search + dedup).

## Claude Claw Extraction (Feb 2026)
- Source: YouTube video on Agent SDK bridge architecture for personal AI assistants.
- Core pattern: Thin Telegram bridge → Agent SDK subprocess → existing Claude Code instance with all skills/MCPs.
- New skill created: `mark-kashef-claude-claw` with 3 prompts (bridge-architect, memory-system-designer, wizard-builder).
- Applied to: Mobile access layer architecture for Antigravity (jarvis-bot decommissioned 2026-03-02).
