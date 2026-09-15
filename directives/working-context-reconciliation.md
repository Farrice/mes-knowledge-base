# Every-turn Working Context Reconciliation

Owner: `/system-audit`. Runtime: `execution/working_context.py`. Applies globally
to Codex sessions, across all domains and conversations without files. The
Claude adapter is tested but requires a separate native installation.
The user authorized this permanent loop on 2026-09-15. It extends existing
document-history, artifact filing and job ownership; it does not create a second
planner, infer a global preference from local feedback, or grant external actions.

## The invariant

At every user turn, integrate the new input into the whole accumulated intent
before the next dependent action. Preserve the desired outcome, audience,
constraints, accepted decisions and positive specimens. A small correction is
not a replacement objective. An explicit change of objective remains possible.
Synthesize one coherent working understanding; do not append each correction as
a new rule. User decisions outrank filenames, dates, search order and model scores.

## Runtime cycle — the session model executes it

1. The global `UserPromptSubmit` hook captures the exact turn and marks its
   session pending. The hook supplies the native session identity and revision.
   `PreToolUse`/`PostToolUse` surface missed reconciliation and source changes.
   `SessionStart`, `PreCompact` and `PostCompact` reload the same durable state.
2. Read the state using the exact runtime command in the hook. Restore the whole
   conversation intent and authoritative project context, not merely the latest
   sentence. New installations in existing tasks must recover their earlier
   intent from the actual task history before initializing; never claim earlier
   turns were captured by a hook that was not installed yet.
3. Before dependent production, commit one integrated snapshot, or acknowledge
   each pending turn with an explicit no-change effect for status/conversation.
   The assistant does this without asking the user to fill forms, run commands,
   confirm a clear correction, or invoke `/job`. No extra model/agent is needed.
4. After producing, update artifact paths and hashes, lifecycle states and next
   action. The actual saved state in external tools is distinct from a local
   candidate. Partial praise never means full artifact approval.
5. Verify before delivery. A missed receipt or drift requests one bounded
   same-turn recovery at Stop. A retry cannot loop forever; unresolved problems
   remain pending and must be reported honestly. Faults never become PASS.

Safe source reads and answering the user are allowed during reconciliation.
Never delay urgent help for bookkeeping. A new mid-turn message reopens the
pending state when delivered by the host; do not ignore steering just because
the earlier snapshot was valid. Host event coverage is measured, not assumed.

## Model-facing commands

Use the canonical runtime even when the current project is elsewhere:

```sh
python3 '/Users/farricecain/Google Antigravity/execution/working_context.py' read --session '<native-id>' --harness codex
python3 '/Users/farricecain/Google Antigravity/execution/working_context.py' commit --session '<native-id>' --harness codex --packet '<task-owned-request.json>'
python3 '/Users/farricecain/Google Antigravity/execution/working_context.py' verify --session '<native-id>' --harness codex
```

Global runtime state lives in `~/.codex/working-context/state.sqlite3`, with
SQLite transactions, per-session identities and immutable revisions. It is
runtime state, not a new global memory/knowledge library. Use normal tool
approval if its write is outside the sandbox; never bypass restrictions.
Keep a single reusable request file inside the owned task workspace, or pass
JSON on stdin with `--packet -`; do not create a numbered request per turn.

The commit request contains:

```json
{
  "expected_revision": 1,
  "resolutions": [
    {"turn": 1, "quote": "exact words from captured feedback", "effect": "How this affects the whole intent, or why no change is needed"}
  ],
  "snapshot": {
    "intent": "The entire intended outcome, preserved through ordinary refinements",
    "working_brief": "One synthesized brief incorporating cumulative decisions",
    "preserved": [
      {"id": "accepted-opening", "text": "Exact accepted part or decision", "scope": "component", "evidence": {"turn": 1, "quote": "exact words from captured feedback"}}
    ],
    "artifacts": [],
    "next_action": {"text": "The next authorized action", "targets": []}
  }
}
```

An artifact has `id`, absolute `path`, `purpose`, `role`, and `evidence`.
Roles are `candidate`, `reference`, `approved`, `rejected`, `superseded`,
`parked`, `archived`. A historical role also requires a short `reason`.
The runtime records actual SHA-256 for active files; supplying a hash checks it
against what the model inspected. One candidate/approved file per purpose.
Separate approved excerpts from a partly rejected source; do not load the whole
rejected draft just to preserve its opening. Put exact approved text in
`preserved` and retain the old file only as historical evidence.

Preserved scope is `component`, `artifact`, `task`, `project`, or `global`.
Global scope additionally requires `explicit_global: true` and actual user
evidence of that scope. Scope labels and quote matching establish a reviewable
claim; they do not prove correct semantic interpretation.

Every pending turn needs one resolution. Omit `snapshot` for a no-change turn;
on an uninitialized conversation also supply `no_change_reason`. Existing
preserved entries cannot silently disappear or change. New decisions that
change them use `overrides: {"<id>": {"turn": N, "quote": "..."}}`.
An objective replacement uses an `intent` override with
`kind: "objective-change"`. Restoring retired work and changing an approved
artifact likewise require an override from newly captured feedback.

Never auto-retry a stale `expected_revision` by changing the number. Reread and
reconcile the intervening turns first. Never cite a partial compliment as proof
of full approval. An uncertain interpretation stays uncertain in the brief.

## One current view; history stays cold

Set `write_root` to the explicit owning worktree/projectless task directory to
render a single `.working-context/<session-key>.md`. Integration main is rejected.
The view is regenerated, never prepended. Previous views and revisions remain
in the journal; hand edits produce drift. `render` rebuilds the derived view.
The runtime remains authoritative for freshness even if an old view is open.

This is a conversation view, not another project CANON. Existing project indexes
and `document_history.py` still own project document authority. When a document
is clearly superseded, use their reversible retirement and redirects within the
owned task, then update its runtime role and known active handoff pointers.
Do not archive code, sources or another task's files based on rejection of copy.
Do not choose authority by date, filename or whether a file was already loaded.

## Jobs, handoffs and ordinary retrieval

`job_board.py` includes the current session's validated context in dispatch and
handoff packets when `CODEX_THREAD_ID`/`CLAUDE_SESSION_ID` has captured state.
Pending or stale context is explicitly marked and cannot be advertised as
current. The job still owns its lanes and approval packets.

Use `handoff` to export a current packet; `verify --handoff <file>` checks exact
session/revision/content before reuse. Existing `/handoff` and `/fresh-pen` must
include this current packet, not a wall of rejected drafts. A recipient recovers
the explicit source session and starts its own record; no cross-task mutation.
Source hashes detect changed shared files. Project document-history revision
checks remain the concurrency protection for shared authoritative documents.

## Proof boundary

Native hook registration, execution receipts, protocol tests, semantic judgment
and user-rated output quality are different evidence. Do not call the whole
system reliable solely because tests pass. The loop cannot erase rejected ideas
already inside a context window; it controls subsequent inputs, makes authority
explicit and invokes the existing recovery path when repeated drift persists.
New user-owned tasks, extra agents, spending, publishing and external writes
retain their permission boundaries. Keep ordinary user-facing replies concise.
