# No Claude Code Subagents

**The rule:** Never propose, create, or invoke project-level Claude Code subagents under `.claude/agents/`. Route work through the existing system instead: an expert persona in `agents/<expert>/` (220 personas, loaded as Tier 2 context) + the matching skill in `skills/<name>/` + a workflow in `.agent/workflows/`. See `directives/agent-loading-protocol.md` for the Tier 0-3 loading sequence.

`.claude/agents/` is closed. Do not add new files there. `.claude/agents/_archived/` holds prior subagent definitions for historical reference only — their presence is not an invitation to revive or extend them.

## Why

Farrice binding feedback, 2026-05-25 (memory record: `feedback_no-claude-code-subagents.md`). On 2026-04-28 a roster of 12 "virtuoso-tier" Claude Code subagents (deep-research, fact-verifier, prose-doctor, expert-extractor, icp-deep-canvasser, synthesis-engine, adversarial-reviewer, content-finalizer, master-copywriter, brand-system-builder, competitive-intel, swarm-orchestrator) was added to the system. After extensive use across the Coach Cooz pivot and other client work, they:

1. Produced subpar output compared to the actual expert personas + skills they were meant to shortcut.
2. Polluted routing — Claude defaulted to a generic subagent instead of the correct expert chain (e.g., Lara Acosta for LinkedIn, Luke Iha for DR copy).
3. Added latency and time tax with no quality return.

Removed 2026-05-02. The system was excellent at the pre-2026-04-28 baseline; the subagent layer was a regression, not an upgrade.

## How to apply

- For research: `/deep-research-gemini` (primary) or `/research-topic` / `/research-sprint`, not a `deep-research` subagent.
- For fact verification: `verify` / `grounding-pass` skills, or Chain Step 5.5 directly.
- For prose / AI-tell scrubbing: `prose-check`, `slop-check`, `anti-slop-audit`, `voice-audit`, `word-audit`.
- For copy: load the relevant expert persona + matching skill (Lara Acosta for LinkedIn, Luke Iha for DR, Nicolas Cole for ghostwriting), not a `master-copywriter` subagent.
- For brand systems: Oren John or Grace Andrews + `/brand-arena`, `/caleb-brand-build`, `/grace-city-blueprint`, `/design-md-synthesize`.
- For competitive intel: `/competitor-intel` or `/spy-market` + Playwright per browser-automation routing.
- For ICP work: `/icp-deep-dive`, `/mcraney-deep-canvass`, `/consumer-posture-profile`, `/belief-first-audience-intelligence`.
- For swarms: `/swarm`, `/parallel-swarm`, `/strike`, `/campaign`, `/jcc-deploy`, `/research-swarm` — not a `swarm-orchestrator` subagent.
- For finalize: `python3 execution/chain_runner.py finalize ...` directly per CLAUDE.md Step 6.
- For extractions: `/extract`, `/parallel-extract`, `/extract-forge`.
- For synthesis: `/reflect`, `knowledge_compiler` synthesis pass, or expert-persona reflection — not a `synthesis-engine` subagent.

If a task seems to need a subagent, the right answer is almost always: load an expert persona, route to a skill, invoke an existing workflow.
