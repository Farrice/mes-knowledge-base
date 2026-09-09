# Operating Codex, Claude Code, and Cowork

This is the operating contract for using all three surfaces without creating a second Antigravity system.

> **Current decision (2026-08-11):** Codex is Farrice's primary working surface. Google Antigravity remains the sole canonical system. Claude Code and Cowork remain supported secondary surfaces. "Primary" describes where Farrice starts work; it does not demote Claude's technical authority or create a Codex fork.

## The model

There is one system and several ways into it:

- **Canonical system:** `/Users/farricecain/Google Antigravity`
- **Default Codex write lane:** `/Users/farricecain/Google-Antigravity-Codex-Operator-Core`
- **Codex primary surface:** day-to-day thinking, execution, verification, documents, and local workspace work
- **Claude Code secondary surface:** available for Claude-specific execution, review, or workflows when it is the better fit
- **Cowork secondary surface:** global, versioned plugins used on demand; it is not a second workspace or source of truth

The default Codex lane is an operational worktree, not another canonical repo. Its branch can contain reviewed work while dirty `main` remains untouched.

## Authority

Platform constitutions are peers:

- Claude Code reads `CLAUDE.md`.
- Codex reads `AGENTS.md` and the expanded `CODEX.md` contract.
- Gemini reads `GEMINI.md` when used.

No platform constitution outranks another merely because Codex is the preferred user surface. Shared generated blocks and platform lint preserve the common contract; platform-specific sections describe genuine runtime differences.

Google Antigravity owns the workflows, skills, routing rules, verifiers, and learning records. Global Codex files stay thin: they point into Google Antigravity and select a safe write lane. Do not copy the full harness, create another router, or maintain a second skill tree under `~/.codex`.

## Where to start

### Codex, the default

Start ordinary work in Codex. The global Antigravity bridge resolves the canonical system and chooses the safe write boundary:

```bash
python3 ~/.codex/tools/antigravity_global.py status
python3 ~/.codex/tools/antigravity_global.py route "<request>"
python3 ~/.codex/tools/antigravity_global.py preflight "<request>"
python3 ~/.codex/tools/antigravity_global.py write-check
```

When canonical `main` is dirty, `write-check` must select `/Users/farricecain/Google-Antigravity-Codex-Operator-Core`. Read canonical state as needed, but make approved mutations in that lane.

### Claude Code

Claude Code remains fully supported. The first writer may own the main tree. Every additional session uses its own worktree lane and bootstraps it with `execution/worktree_lane.py bootstrap`. Do not make a second writer share an active tree.

### Cowork

Cowork plugins remain installed globally, versioned, and available on demand. Use the narrowest relevant plugin for the current task. A plugin being installed proves package availability, not connector authentication or task-level output quality.

## One writer per tree

The safety rule is no longer "only one tool can be open." It is:

> **The first writer owns a tree. Every additional writing session gets its own lane.**

- Never let Codex and Claude Code write to the same checkout concurrently.
- Do not clean, stash, reset, or absorb another session's dirty work.
- Bootstrap every added lane so hooks, environment links, memory access, MCP configuration, and budget controls are available.
- Integrate through clean commits and the lane merge process. Conflicts park the lane; never force them.
- The dedicated Codex operator lane stays available even when it is ahead of `main`. It is not merged automatically while canonical `main` is dirty.

### End-session lane hygiene

Use the existing `/end-session` workflow as the primary Codex closeout; do not
create a second cleanup command. It classifies the lane before cleanup:

- **Persistent operator lane:** `codex/antigravity-operator-core` is a reusable
  workbench. Verify the exact handoff, commit only task-owned paths locally, and
  keep the lane available.
- **Temporary task lane:** closeout must return an exact merge-or-park action.
  Keep the task pinned until that action is approved and resolved; conflicts
  park visibly instead of being forced.
- **Git and global boundaries:** local commit is the default. Branch push,
  updates to `main`, and writes under `~/.codex/end-session/` require explicit
  approval for that run.

A clean session therefore means every change is committed or explicitly held,
every continuation has an exact named handoff, and every temporary lane is
merged or visibly parked. It does not mean deleting the permanent Codex lane.

## Capability policy

Shared Antigravity capability counts only when the workflow, adapter, activation path, and verifier are present. File presence alone is not proof of useful behavior.

Use these acceptance labels:

- `SHARED_AND_PROVEN`: both relevant surfaces have current structural or live proof.
- `CODEX_ADVANTAGE`: Codex has a verified surface-specific capability or lower-friction route.
- `CLAUDE_COWORK_ADVANTAGE`: Claude Code or Cowork has a verified surface-specific capability.
- `ADAPTER_NEEDED`: canonical behavior exists but one surface lacks a safe bridge.
- `BLOCKED`: a known dependency or permission boundary prevents use.
- `UNMEASURED`: installed or structurally available, but not tested on a real task or authenticated connector.

Qualitative claims such as "same caliber or better" remain `UNMEASURED` until production tasks provide receipts. The first ten substantive Codex-primary tasks are the evaluation set; do not promote more harness changes merely because installation checks pass.

## Imported adapter policy

An imported `source-command-*` adapter may enter the Codex lane only when it is mechanically thin and points to tracked canonical behavior:

1. The directory contains only expected adapter files.
2. Frontmatter name matches the directory.
3. Its command target exists in the captured tracked tree.
4. It contains no independent business logic, executable payload, secret, or asset.
5. It is a recognized generated thin wrapper or an explicitly verifier-declared hot control.
6. Its source fingerprint is unchanged before and after transfer.

Everything else is `PARKED_IMPORT`: preserved where found, not deleted, not silently promoted, and not treated as capability loss. Current projects, deliverables, runtime state, counters, untracked workflows, Claude commands, and local configuration do not ride along with adapter imports.

## Subagents and orchestration

Codex subagents are available, but real subagent use requires Farrice's explicit authorization for that run. The main Codex task owns integration and file edits by default. Read-only diagnostic or validation subagents may be proposed when they would materially help; they are not silently spawned.

Claude Code and Cowork may have different orchestration or plugin strengths. Those differences are recorded in the capability matrix rather than flattened into false parity.

## Cross-surface continuity

Continuity travels through canonical artifacts and exact named handoffs:

- Save or resume the exact named handoff.
- Verify it with `python3 execution/handoff_store.py verify`.
- Prefer explicit source paths with `handoff_store.py save --from <path>`.
- Never use shared-temp newest-file discovery for cross-surface transfer. `--from-temp` can select a sibling session's file and is not an identity-safe handoff.
- Include the branch or lane, exact artifact paths, open decisions, proof state, and next action.

Do not ask either surface to reconstruct context from "the newest file" or an unspecified conversation.

## Hooks and global trust

Codex hooks are trusted per exact hook definition and path. The lane's `.codex/hooks.json` must be represented by path-scoped state in `~/.codex/config.toml`, and trust must be proven through live safe-command and dangerous-command dry-run probes. Configuration text by itself is not proof.

If the lane hook file changes:

1. Run the operator-core verifier first.
2. Back up `~/.codex/config.toml`.
3. Update only the exact path-scoped hook-state entries for the lane.
4. Preserve every unrelated global setting and plugin entry.
5. Repeat the live probes.

Global configuration mutation remains approval-gated.

## What each surface is for

| Need | Default surface | Reason |
|---|---|---|
| Messy problem shaping, local execution, verification, documents, code, or system work | Codex | Primary surface with the dedicated safe write lane and global dispatcher |
| Claude-specific model judgment, Claude-native workflows, or a deliberate second implementation/review | Claude Code | Supported peer surface with the same canonical Antigravity source |
| A packaged Cowork specialty or connector-backed business workflow | Cowork | Versioned plugins available on demand |
| Multiple surfaces at once | Separate lanes | Parallel access is safe only with one writer per tree |

Choose by outcome, not by loyalty. Codex is the default; Claude Code and Cowork remain valid tools when they offer a concrete advantage.

## Verification set

After meaningful harness changes, verify:

```bash
python3 execution/verify_google_operator_core.py
python3 execution/verify_codex_authority.py
python3 execution/verify_autopilot_runtime_preflight.py
python3 execution/verify_skill_system_contract.py
python3 execution/verify_subagent_approval_language.py
python3 execution/platform_compiler.py lint --json
python3 execution/verify_codex_claude_parity.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```

For global access:

```bash
python3 ~/.codex/tools/antigravity_global.py verify
python3 ~/.codex/tools/antigravity_global.py write-check
codex plugin list
```

## The short version

1. Start in Codex.
2. Keep Google Antigravity canonical.
3. Write in the dedicated Codex lane when `main` is dirty.
4. Keep Claude Code and Cowork available for concrete advantages.
5. Never place two writers in one tree.
6. Transfer work through exact named artifacts and handoffs.
7. Treat installation as structural proof; use real tasks to prove caliber.
