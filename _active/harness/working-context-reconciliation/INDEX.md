# Working Context Reconciliation

Current source: `execution/working_context.py`; contract:
`directives/working-context-reconciliation.md`.
Deployment: authorized for local main and global Codex on 2026-09-15. No push.
The deployment receipt records the receiving commit and native activation state.

## What this maintains

Every turn updates the whole accumulated objective, integrated brief, approved
parts, active references and next action. The session model interprets feedback;
SQLite records exact turn evidence and immutable revisions. A stale writer,
missed turn, lost preserved part, changed source, competing current artifact or
rejected next-action target cannot quietly become a current handoff.

One generated current view replaces the prior view. History stays recoverable.
Existing project CANON and document-history tools own physical filing and
retirement. This does not launch agents, create tasks, sweep other projects or
turn local feedback into a global rule.

## Integration and rollback

- Global Codex hooks: prompt, tools, resume, pre/post compaction and bounded Stop.
- Global instructions: thin pointer to the canonical contract.
- Job dispatch and handoff packets carry current state or a visible pending flag.
- Existing handoff/fresh-pen workflows export verified session state.
- Historical-read guard follows explicit lifecycle decisions, not dates/mtime.
- Installer: `execution/install_working_context.py`; defaults to dry run.
  `--apply` preserves receiving files in a dated global backup. `--rollback`
  consumes that receipt and refuses to overwrite later user edits.
- The Claude adapter is covered by protocol tests; Claude global installation
  is outside this Codex deployment.

## Evidence and its limits

`execution/tests/test_working_context*.py` cover transactional and adapter
behavior, concurrent prompt arrivals, stale renderers, no-artifact turns,
all-domain fixtures, failed handoffs, source changes and install/rollback.
The original 22-test offline prototype and real Jen failure fixture remain in
`06-system/`. They are historical proof, not native activation evidence.
The original design and its unmet live-quality gates are preserved in
`99-archive/2026-09-15-prototype-plan.md`.

Native registration, actual hook execution, a 10-turn live lifecycle replay,
and user-rated semantic quality are separate proof levels. The deployment
receipt must state which ran. Tests cannot guarantee perfect interpretation or
prevent every possible drift. No native compaction or user satisfaction result
is inferred from a synthetic payload.
