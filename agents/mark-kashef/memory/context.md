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

## Visual Blueprint Methodology Extraction (Mar 2026)
- Source: YouTube video on ASCII art wireframing for Claude Code visual planning.
- Core pattern: Insert visual wireframe checkpoint between human intent and AI execution. Iterate at wireframe layer (cheap) not code layer (expensive).
- New skill created: `mark-kashef-visual-design` with 5 workflows and 12 embedded prompt-capabilities.
- Workflows: ASCII Wireframe Generator, Visual Blueprint-to-Build Pipeline, Slide Deck Architect, Design System Visualizer, Visual Taste Gate.
- Slash commands: `/wireframe` (pre-flight), `/visual-blueprint` (full pipeline), `/sketch-to-build` (rapid execution).
- Stacks with: `banana-squad` (wireframed image gen), `oren-creative-direction` (CEV taste gates), `sean-kochel-design-first-build` (design-first artifacts).

## Wargame OS Extraction (Jul 2026)
- Source: YouTube nuwlyQXrADg ("Fable's last week" wargaming video, 13:58) + The Laundry List PDF (28pp) + shipped fable-wargame-kit (10 mission briefs, SUCCESS.md 8-point standard, LEDGER.md, /goal + /loop contracts).
- Core pattern: don't ask the frontier model for plans OR execution — make it WARGAME the mission on paper (Move / Expected observation / Fail + cause / Counter-move / Trigger, RECON NEEDED with exact settling checks, aborts, verification runs) so a cheaper executor runs it blind. "You pay for the genius once. You keep it forever."
- New skill: `mark-kashef-wargame-os` — 10 workflows (`/wargame-order`, `/wargame-run`, `/wargame-grade`, `/wargame-execute`, `/wargame-batch`, `/wargame-recon`, `/wargame-executor-fit`, `/wargame-brief`, `/wargame-mission`, `/wargame-client`).
- Layer relationship: wargaming is the planning layer ABOVE agent-orchestration — it produces the failure-map orchestration executes. Fan-out, tollbooths, files-are-truth reappear downstream.
- Key epistemics: the 2×2 unknowns box — "Your prompt only fills the first box. The wargame drags the other three into the light."
- Operational landmine learned: never ask a reasoning model to expose its thinking in output (can silently reroute the session) — request artifacts, findings, quotes, rewrites.
