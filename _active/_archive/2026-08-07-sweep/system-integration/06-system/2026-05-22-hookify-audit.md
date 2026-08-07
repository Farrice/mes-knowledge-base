# Hookify Wiring Audit — 2026-05-22

> **Triggered by**: 2026-05-21 best-practices research synthesis Integration B. Stream 2 finding flagged `.claude/hookify.*.local.md` files as potentially "documentation-only" and recommended wiring them into `.claude/settings.local.json` as active hook bindings.
>
> **Verdict**: The synthesis brief's premise was incorrect. **The hookify plugin is fully installed and wired**. The 11 `.md` files are runtime configuration, not docs. No settings.local.json edits required. Recommendation: leave as-is.

---

## What I Verified

### 1. Hookify plugin IS installed

Location: `/Users/farricecain/.claude/plugins/cache/claude-plugins-official/hookify/`

```
hookify/
├── README.md
├── agents/
├── commands/      (help, list, configure, hookify)
├── core/
├── hooks/
│   ├── hooks.json
│   ├── pretooluse.py
│   ├── posttooluse.py
│   ├── stop.py
│   └── userpromptsubmit.py
├── matchers/
├── skills/        (writing-rules)
└── utils/
```

### 2. Hookify IS wired to all 4 Claude Code native hook events

`hooks/hooks.json` (the plugin's own manifest) binds:

| Claude Code Event | Hookify Handler |
|---|---|
| `PreToolUse`       | `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/pretooluse.py` (timeout 10s) |
| `PostToolUse`      | `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/posttooluse.py` (timeout 10s) |
| `Stop`             | `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/stop.py` (timeout 10s) |
| `UserPromptSubmit` | `python3 ${CLAUDE_PLUGIN_ROOT}/hooks/userpromptsubmit.py` (timeout 10s) |

At each event, the corresponding handler reads `.claude/hookify.*.local.md` files, parses the YAML frontmatter (`event`, `action`, `conditions`), and fires rules whose conditions match the current invocation context.

### 3. The 11 `.claude/hookify.*.local.md` files ARE active runtime config

Not documentation. They are the hookify plugin's rule format (see `commands/hookify.md` for the spec). Each file is one rule. Current inventory:

| File | Event | Action | Purpose |
|---|---|---|---|
| `hookify.anchor-named-discipline.local.md`   | (varies) | warn  | Anchor naming discipline |
| `hookify.autopilot-ledger.local.md`          | (varies) | warn  | Autopilot ledger emission |
| `hookify.fal-budget.local.md`                | PreToolUse | block? | Fal API budget gate |
| `hookify.freshness-tax.local.md`             | (varies) | warn  | Freshness tax on stale content |
| `hookify.intent-pipeline.local.md`           | Stop | warn  | Intent scoring reminder |
| `hookify.notion-api-guard.local.md`          | PreToolUse | warn  | Notion API version guard |
| `hookify.performance-log.local.md`           | (varies) | warn  | Performance log reminder |
| `hookify.perplexity-budget.local.md`         | PreToolUse | warn  | Perplexity budget gate |
| `hookify.quality-gate.local.md`              | Stop | warn  | Quality gate reminder |
| `hookify.routing-coverage.local.md`          | Stop | warn  | Routing enforcer skipped warning |
| `hookify.session-state-reminder.local.md`    | (varies) | warn  | Session state reminder |

### 4. settings.local.json has NO `hooks` block

```bash
jq '.hooks' .claude/settings.local.json
# null
```

This is **correct and intentional** — the hookify plugin's `hooks/hooks.json` provides the binding layer. settings.local.json doesn't need to duplicate it.

---

## Why the Synthesis Brief Got This Wrong

The brief's Stream 2 inferred docs-only status from a file listing. The actual contract (hookify plugin reads `.claude/hookify.*.local.md` at runtime via its own bundled `hooks.json`) was invisible until I traced into the plugin cache. The synthesis recommendation to "wire" these in settings.local.json would have created **duplicate hook bindings** — both the plugin AND settings.local.json firing on the same events, racing each other.

---

## The Real Distinction: `warn` vs Command Execution

The existing hookify rules use `action: warn` — they surface a textual nag into the conversation when their conditions match. **They do not execute shell commands.**

The synthesis brief's recommendation was something different: command-execution hooks that actually run `routing_enforcer.py check`, `chain_runner.py finalize`, `recall_logger.py log` deterministically. Those would need to be added as direct `PreToolUse` / `Stop` / `UserPromptSubmit` entries in settings.local.json **in addition to** the existing hookify-plugin binding.

### Should we add command-execution hooks?

**Arguments FOR** (the synthesis brief's view):
- Closes AI-Memory-Dependent-Observability for routing (per `feedback_ai-memory-dependent-observability.md`)
- Deterministic — no model-dependence
- Same mechanism as the `recall_logger` backstop shipped in commit `a35ae51a`

**Arguments AGAINST** (counter-read #2 from synthesis brief itself):
- "Every PreToolUse hook is a shell command that can fail and block legitimate work"
- Cursor deliberately avoids this layer
- Current `chain_runner.py finalize()` ALREADY provides deterministic post-hoc backstop for routing (per CLAUDE.md: "chain_runner.py finalize() also runs a post-hoc check when --workflow is supplied")
- Risk: a buggy hook command blocks every Bash/Edit/Read call until removed — high-blast-radius

**Decision**: Defer. The current state is correct:
1. Hookify warning hooks fire automatically at PreToolUse / Stop / UserPromptSubmit
2. `chain_runner.finalize()` provides deterministic post-hoc check for routing
3. `chain_runner.finalize()` auto-fires `recall_logger` for Recall observability (per commit `a35ae51a`)
4. Adding command-execution hooks would be redundant for routing/recall AND introduces brittleness risk

If a NEW class of failure surfaces that warnings + `finalize()` don't catch, revisit. Until then, the hookify-plugin warning layer + `finalize()` backstop is the right balance.

---

## What If We Wanted to Add Command-Execution Hooks Anyway?

For completeness — if a future session decides the brittleness trade is worth it, the wire-up looks like this:

```jsonc
// .claude/settings.local.json
{
  "permissions": { ... },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 execution/routing_enforcer.py check --request \"${USER_PROMPT}\" --workflow \"${CHOSEN_WORKFLOW}\" --quiet --source pretooluse",
            "timeout": 5
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 execution/recall_logger.py report --days 1 --quiet",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

**Three critical caveats if this is ever shipped**:

1. **PreToolUse blast radius**: a hook that fails or hangs blocks the parent tool call. Test exhaustively in a throwaway branch before merging.
2. **Variable substitution**: Claude Code's PreToolUse hook payload doesn't include the original user request as a clean `${USER_PROMPT}` env var. You'd need to read `.agent/session-state.md` or pipe the payload JSON through `jq`. Verify the actual contract in the Claude Code docs first.
3. **Don't shell out to `chain_runner.finalize` from Stop**: it's a multi-step interactive process. Keep that one as the model-invoked finalize that already exists.

---

## Action Items

1. **None for this session** — close Integration B with this audit note.
2. **Add to `feedback_ai-memory-dependent-observability.md`'s 30-day review** (target 2026-06-02): if any new observability failures surface, revisit whether command-execution hooks would have caught them.
3. **Update the synthesis brief** if it gets re-circulated: Stream 2 finding about hookify-as-docs was incorrect.

---

## Cross-References

- Synthesis brief: `_active/_archive/2026-08-07-sweep/system-integration/02-research/2026-05-21-best-practices-research-synthesis.md` (Stream 2, Integration B)
- Hookify plugin docs: `~/.claude/plugins/cache/claude-plugins-official/hookify/562a27feec2c/`
- AI-Memory-Dependent-Observability precedent: commit `a35ae51a` (Recall logger backstop)
- chain_runner.finalize() post-hoc routing check: `execution/chain_runner.py` (referenced in CLAUDE.md Mandatory Workflow Routing section)
- Feedback memory: `feedback_ai-memory-dependent-observability.md`
