#!/usr/bin/env python3
"""Check or align End-session Operator Core wrappers with source truth."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "end-session.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-end-session" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_END_SESSION = Path.home() / ".codex" / "skills" / "end-session" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-end-session" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Google Antigravity/.agent/workflows/end-session.md"

COMMON_REQUIREMENTS = (
    "whole-session closeout",
    "retrieval handoff",
    "closeout intelligence capture",
    "3 Next Prompts",
    "Operator Lesson",
    "Next-time prompt",
    "Subagent worth it?",
    "Reuse hook",
    "session_closeout_intelligence.py run --source end-session",
    "conversation_index.py stats",
    "handoff_store.py verify",
    "codex_end_session.py run --manifest",
    "[Domain]: [Specific Object] - [Outcome]",
    "archive only",
    "dedicated `codex/*` worktree",
    "Never auto-commit, auto-merge, or auto-push `main`",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
    "close ready",
    "close done",
    "bulk closeout audit",
    "Bare `ready` and `done`",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for End-session behavior",
        "whole-session closeout",
        "not `/handoff`",
        "not `/steering-compass`",
        "3 Next Prompts",
        "Operator Lesson",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        "handoff_store.py verify",
        "codex_end_session.py run --manifest",
        "[Domain]: [Specific Object] - [Outcome]",
        "archive only",
        "dedicated `codex/*` worktree",
        "Never auto-commit, auto-merge, or auto-push `main`",
        "Optional cleanup must be reviewed",
        "Real Codex subagents require explicit authorization",
        "close ready",
        "close done",
        "bulk closeout audit",
        "Bare `ready` and `done`",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/end-session.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global End-Session Closeout",
    ),
    GLOBAL_END_SESSION: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
        "Insightful Momentum/frontier standard",
        "legacy thin prompt shell",
        "contextual_next_prompts.py",
        "Output/Capability Move",
        "Operator Insight",
        "Hidden Gap/Opportunity",
        "Capability Revealed",
        "Recommended task title",
        "Expected outcome",
        "Quality bar",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/end-session/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "conversation_index.py update <current-conversation-id>",
    "manual closeout only",
    "skip closeout intelligence",
    "generic handoff only",
    "spawn real Codex subagents by default",
    "push without confirmation",
    "plan-first approval checkpoint",
)

GLOBAL_AGENTS_BLOCK = f"""## Global End-Session Closeout

Use the global `end-session` skill at `/Users/farricecain/.codex/skills/end-session/SKILL.md`
when the user invokes `/end-session`, `source-command-end-session`, `end session`,
`wrap this session`, `session closeout`, `close ready`, `close done`, or asks to finish the current thread
with whole-session closeout, retrieval handoff, and closeout intelligence capture.

The canonical Antigravity End-session workflow is `{CANONICAL_PATH}`. Global
End-session wrappers are thin compatibility wrappers with no competing behavior
contract.

Default behavior: native task naming with `[Domain]: [Specific Object] - [Outcome]`
-> exact named handoff save and `handoff_store.py verify` -> Codex coordination via
`codex_end_session.py run --manifest` -> `3 Next Prompts` -> `Operator Lesson`
-> closeout intelligence via
`session_closeout_intelligence.py run --source end-session` ->
`conversation_index.py stats` -> artifact organization checks when relevant.
Meaningful closeouts also retain `Next-time prompt`, `Subagent worth it?`, and
`Reuse hook` so the next task can restart from an explicit continuation surface.
Treat `/handoff` as a focused transfer packet and `/steering-compass` as
standalone next-prompt coaching. Pin unfinished tasks and archive only a verified
`done` closeout. Automatic Git synchronization is limited to manifest-owned
paths in a dedicated `codex/*` worktree. Never auto-commit, auto-merge, or
auto-push `main`. Optional cleanup needs review; never broadly delete or perform
destructive cleanup without explicit approval.
Real Codex subagents require explicit authorization.

Guarded shorthand is global but thin: `close ready` requests a verified `ready`
closeout and never archives; `close done` requests proof and archives only when
the coordinator receipt sets `task_actions.archive` true; `bulk closeout audit`
is read-only and dispatches nothing. Bare `ready` and `done` are status words,
never commands. Google Antigravity remains the behavior source of truth.
"""

GLOBAL_END_SESSION_TEXT = f"""---
name: end-session
description: Global thin compatibility wrapper for Antigravity End-session closeout. Triggers on /end-session, end session, close ready, close done, and bulk closeout audit; delegates safety behavior to the canonical project workflow.
---

# End-session

## Project Source Of Truth

The canonical End-session behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps `/end-session`,
`end session`, `close ready`, `close done`, `bulk closeout audit`, and closeout
language discoverable anywhere in Codex, but it must
not maintain a competing behavior contract. When the Antigravity project
workflow is available or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current End-session contract:

- `/end-session` owns whole-session closeout, retrieval handoff, and closeout intelligence capture
- it is not focused `/handoff` transfer and not standalone `/steering-compass` next-prompt coaching
- meaningful closeouts include `3 Next Prompts`
- meaningful closeouts include `Operator Lesson`
- include `Next-time prompt`
- include `Subagent worth it?`
- include `Reuse hook`
- use `session_closeout_intelligence.py run --source end-session`
- use `conversation_index.py stats` before any rebuild
- save from an exact named source and require `handoff_store.py verify <thread> --source <path> --json`
- coordinate Codex closeout through `codex_end_session.py run --manifest <json>`
- use `[Domain]: [Specific Object] - [Outcome]`; rename every meaningful task, pin unfinished work, and archive only verified `done`
- allow automatic commit and push only for manifest-owned paths in a dedicated `codex/*` worktree
- Never auto-commit, auto-merge, or auto-push `main`
- optional cleanup needs review and no publish, push, broad deletion, or destructive cleanup without explicit approval
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract

## Guarded Global Shorthand

- `close ready` runs the canonical closeout with requested status `ready`; it never archives or merges main.
- `close done` is a verification request, not a declaration. Archive only when the coordinator receipt sets `task_actions.archive` true; otherwise fail closed to `ready`, `blocked`, or `mid-build`.
- `bulk closeout audit` builds the task-to-lane map read-only and dispatches nothing.
- Bare `ready` and `done` remain ordinary status words, never commands.

When the project helper is available, use
`python3 execution/bulk_closeout_control.py interpret "<phrase>"` before acting.

## Output Contract

Produce a concise session closeout: visible `Recommended task title`, session name, slug, searchable keywords,
completed work, remaining priority, essential context paths, hot experts or
workflows, `3 Next Prompts`, and an `Operator Lesson`. Run or request the
project workflow's local closeout intelligence steps when operating inside the
Antigravity workspace. For native Codex closeout, read the coordinator receipt
before applying title, pin, or archive task actions.

Meaningful closeouts must preserve the Insightful Momentum/frontier standard,
not the legacy thin prompt shell. When the workspace renderer exists, run
`execution/contextual_next_prompts.py` and retain its Recommended task title, Output/Capability Move,
Operator Insight, Hidden Gap/Opportunity, Capability Revealed, prompt, expected
outcome, quality bar, skip condition, and suggested workflow fields.
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-end-session
description: Global compatibility alias for /end-session; follows the Antigravity closeout source of truth.
---

# source-command-end-session

This is a compatibility alias for the global End-session wrapper. When invoked,
load and follow:

`/Users/farricecain/.codex/skills/end-session/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current End-session contract: whole-session closeout, retrieval handoff,
closeout intelligence capture, `3 Next Prompts`, `Operator Lesson`,
`Next-time prompt`, `Subagent worth it?`, `Reuse hook`,
`session_closeout_intelligence.py run --source end-session`,
`conversation_index.py stats`, `handoff_store.py verify`,
`codex_end_session.py run --manifest`, `[Domain]: [Specific Object] - [Outcome]`,
archive only after verified `done`, automatic Git only in a dedicated `codex/*`
worktree, Never auto-commit, auto-merge, or auto-push `main`, real Codex subagents require explicit
authorization, and no competing behavior contract.

Preserve the guarded shorthand: `close ready` never archives; `close done`
requires coordinator and integration proof; `bulk closeout audit` is read-only;
Bare `ready` and `done` are never commands.

Route focused transfer packets to `/handoff` and standalone next-prompt coaching
to `/steering-compass`; keep whole-session closeout on `/end-session`.
"""

LOCAL_ALIGNMENT_BLOCK = """## Operator Core Alignment

This project wrapper follows `.agent/workflows/end-session.md` as the canonical behavior source. It must stay a thin compatibility wrapper and preserve:

- whole-session closeout, retrieval handoff, and closeout intelligence capture
- clear separation from focused `/handoff` transfer packets and standalone `/steering-compass` next-prompt coaching
- `3 Next Prompts`
- `Operator Lesson`
- `Next-time prompt`
- `Subagent worth it?`
- `Reuse hook`
- `session_closeout_intelligence.py run --source end-session`
- `conversation_index.py stats`
- exact named handoff save plus `handoff_store.py verify <thread> --source <path> --json`
- Codex coordination through `codex_end_session.py run --manifest <json>`
- `[Domain]: [Specific Object] - [Outcome]`, rename every meaningful task, pin unfinished work, and archive only verified `done`
- automatic commit and push only in a dedicated `codex/*` worktree
- Never auto-commit, auto-merge, or auto-push `main`
- real Codex subagents require explicit authorization
- no competing behavior contract
- `close ready` never archives or merges main
- `close done` requires integration proof and a coordinator archive receipt
- `bulk closeout audit` is read-only and dispatches nothing
- Bare `ready` and `done` are status words, never commands
"""

WORKFLOW_ALIGNMENT_BLOCK = """## Operator Core Alignment

This workflow is the canonical source of truth for End-session behavior. Global
and local End-session wrappers must stay thin compatibility wrappers that point
back here, not competing behavior contracts.

Preserve these invariants:

- `/end-session` owns whole-session closeout, retrieval handoff, and closeout intelligence capture.
- It is not `/handoff` for a focused transfer packet and not `/steering-compass` for standalone next-prompt coaching.
- Meaningful closeouts include session naming metadata, a concise handoff, `3 Next Prompts`, and an `Operator Lesson`.
- Closeout intelligence runs through `python3 execution/session_closeout_intelligence.py run --source end-session`.
- Conversation indexing uses the safe `python3 execution/conversation_index.py stats` check before any rebuild.
- Codex closeout saves an exact named source, requires `handoff_store.py verify`, and runs `python3 execution/codex_end_session.py run --manifest <json>`.
- Codex titles use `[Domain]: [Specific Object] - [Outcome]`; unfinished tasks stay pinned and archive only follows a verified `done` receipt.
- Automatic Git synchronization is limited to manifest-owned paths in a dedicated `codex/*` worktree. Never auto-commit, auto-merge, or auto-push `main`.
- Optional cleanup must be reviewed; never publish, push, broadly delete, or perform destructive cleanup without explicit approval.
- Real Codex subagents require explicit authorization.
- `close ready` never archives or merges main; `close done` requires integration
  proof and a coordinator archive receipt; `bulk closeout audit` is read-only;
  Bare `ready` and `done` are status words, never commands.
"""


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def ensure_block(text: str, block: str, anchor: str) -> str:
    heading = block.splitlines()[0]
    if heading in text:
        return text
    if anchor not in text:
        return text.rstrip() + "\n\n" + block.rstrip() + "\n"
    return text.replace(anchor, block.rstrip() + "\n\n" + anchor, 1)


def align_workflow(text: str) -> str:
    return ensure_block(text, WORKFLOW_ALIGNMENT_BLOCK, "## Usage")


def align_local_wrapper(text: str) -> str:
    if "## Operator Core Alignment" in text:
        return re.sub(
            r"## Operator Core Alignment\n.*?(?=\n## Command Template)",
            LOCAL_ALIGNMENT_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    return ensure_block(text, LOCAL_ALIGNMENT_BLOCK, "## Command Template")


def align_global_agents(text: str) -> str:
    if "## Global End-Session Closeout" in text:
        return re.sub(
            r"## Global End-Session Closeout\n.*?(?=\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    return ensure_block(text, GLOBAL_AGENTS_BLOCK, "## Native Codex Artifact Default")


def apply_alignment() -> list[str]:
    changed: list[str] = []

    original_workflow = read(PROJECT_WORKFLOW)
    updated_workflow = align_workflow(original_workflow)
    if updated_workflow != original_workflow:
        write(PROJECT_WORKFLOW, updated_workflow)
        changed.append(str(PROJECT_WORKFLOW.relative_to(ROOT)))

    original_local = read(LOCAL_WRAPPER)
    updated_local = align_local_wrapper(original_local)
    if updated_local != original_local:
        write(LOCAL_WRAPPER, updated_local)
        changed.append(str(LOCAL_WRAPPER.relative_to(ROOT)))

    original_agents = read(GLOBAL_AGENTS)
    updated_agents = align_global_agents(original_agents)
    if updated_agents != original_agents:
        write(GLOBAL_AGENTS, updated_agents)
        changed.append(str(GLOBAL_AGENTS))

    if not GLOBAL_END_SESSION.exists() or read(GLOBAL_END_SESSION) != GLOBAL_END_SESSION_TEXT.rstrip() + "\n":
        write(GLOBAL_END_SESSION, GLOBAL_END_SESSION_TEXT)
        changed.append(str(GLOBAL_END_SESSION))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-end-session", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global end-session", GLOBAL_END_SESSION),
        ("global source-command-end-session", GLOBAL_WRAPPER),
    ):
        if not path.exists():
            failures.append(f"{label} missing: {path}")
            continue
        text = read(path)
        normalized = normalize(text)
        for snippet in PATH_REQUIREMENTS[path]:
            if normalize(snippet) not in normalized:
                failures.append(f"{label} missing: {snippet}")
        for snippet in FORBIDDEN:
            if snippet.lower() in text.lower():
                failures.append(f"{label} contains stale End-session contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align End-session Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global/local End-session surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("END-SESSION OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("END-SESSION OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("END-SESSION OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
