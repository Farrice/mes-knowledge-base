# Working Context Reconciliation

**State: implementation plan with an offline protocol prototype. Global activation is NOT INSTALLED.**

## Outcome

Farrice can iterate naturally, every turn, without becoming the file manager or
repeating the whole brief. The session maintains a coherent understanding of
the entire objective, incorporates new feedback at the right scope, preserves
accepted parts, and retires rejected direction from normal working context.
This is ongoing task stewardship, not a periodic cleanup job.

**Universal scope:** this governs collaboration itself: coding, strategy,
research, business decisions, planning, creative production, personal work and
open-ended thinking, including turns that create no file. Jen is the first
failure fixture, not a content-only activation condition. Artifact filing is
one output of the loop; maintaining coherent intent is its primary job.

The invariant is global; decisions retain their proper local scope. A rejected
metaphor must not become a ban for every future task. A coding correction must
not silently rewrite product goals. A new research source can change a finding
without erasing the question. A time constraint can alter the plan without
discarding the intended outcome. Evolving intent must be integrated as a whole,
not merely frozen or overwritten by the newest sentence.

The source of authority is the whole accumulated user intent and its explicit
revisions. The latest sentence is a change to interpret within that intent;
it is not a replacement objective unless the user actually changes the objective.
Earlier wording is not frozen against later clarification either.

## Decision

Extend the existing document-history, filing, hook, and handoff systems with
one reconciliation protocol. Use the model already working with Farrice for
semantic judgment. Use deterministic code for receipt coverage, task identity,
version checks, approved-part preservation, pointer freshness, and history
exclusion. Do not create another autonomous writer, library, or slash command.

| Approach | User effort and cost | Judgment / maintenance | Decision |
|---|---|---|---|
| Operate the existing librarian and filing commands alone | No new provider; still depends on remembering task-time reconciliation | Existing tools are useful, but their wiring does not cover every turn | Reuse as components; insufficient alone |
| Small local adapter around existing owners | Existing session inference; small local checks; no new subscription or autonomous model calls | Exact integration with decisions, files and jobs; requires lifecycle tests and maintenance | Recommended |
| Separate finished organizer or agent product | Another integration and potentially another subscription; authority would still need to be supplied | File organization alone cannot establish approval or repair session interpretation | No external product needed for this demonstrated failure |

## Evidence and recovered machinery

1. The inspected Jen `CAROUSEL-CURRENT.md` prepended new CURRENT blocks while retaining older
   instructions, including a v03 next action and an abandoned consultation
   direction. Her active task has six recorded compactions, but that does not
   prove compaction caused the writing failures. The direction error predates
   this task's recovery merges.
   During this audit the owning Jen task reconciled it and preserved the old
   file at `99-archive/reconciliation-20260914-231237/CAROUSEL-CURRENT.md`.
   Our regression now uses that exact archived failure and separately scans
   live state; it does not falsely report the repaired file as still broken.
2. `execution/job_board.py::portable_text` exports job status, packets, trace
   and the card. It does not reconcile creative authority across those inputs.
3. `execution/hooks/artifact_placement_hook.py` handles Write/Edit/NotebookEdit,
   not the shell/Python writes that produced the stacked Jen state. The Codex
   artifact-placement matcher also omits `exec_command` and `apply_patch`.
4. `execution/hooks/superseded_read_guard.py` handles Read, while its date rule
   can recommend undated siblings sorted by modification time. This is weaker
   than the newer decision-led filing contract. Widening a matcher alone does
   not make arbitrary shell reads/writes observable.
5. `directives/artifact-placement.md` still calls undated names living truth and
   says absorption is never automated. `Work/ASSET-FILING.md` instead gives
   explicit decisions precedence and documents transactional retirement. The
   instruction conflict must be reconciled as part of the repair.
6. The existing document-history helper already provides revision checks,
   project locking, preserved bytes, redirects, history exclusion and a pending
   transaction journal. Reuse these mechanisms; do not add a competing CANON.
7. `/knowledge-librarian` is a read-only discovery pulse, not an automatic
   artifact manager. `/fresh-pen` preserves decisions at transfer, but does not
   maintain each intermediate creative state. The July 31 Angle Map recovery
   documented the same stale-index/rejected-draft failure and fixed it locally.

## Every-turn operating cycle

This cycle applies on **every user turn of an active iterative task**, including
short approvals, corrections, reversals, status questions and mid-run steering.
It does not rely on negative sentiment, a revision count, a timer, a compaction,
or Farrice invoking a command. Pure conversation can receive a no-change
disposition without creating a content project or a new brief.

Every-turn coverage is a lifecycle property, not a domain router or keyword
match. New input also matters while a tool is running: reconcile it before the
next dependent action. Track the actual native event coverage of each host;
never report support for an application that does not expose the needed events.

1. **Receive.** A native prompt hook records the exact user turn identity and
   marks its bound task state pending. No regex decides approval or deletion.
   Never bind by the newest folder, newest handoff, title alone or guessed job.
2. **Reconcile meaning before production.** The current model rereads the
   coherent working brief, accepted specimens and new feedback. It classifies
   the update as clarification, component revision, approval, rejection,
   exploration, objective replacement, or no creative change. It synthesizes
   the whole direction again; it does not append the latest sentence as a new
   rule. Multiple pending user turns must all be accounted for.
3. **Commit the state change.** Validate exact task/purpose identity, feedback
   evidence, expected revision, preserved components and active next action.
   Replace the managed current view atomically. Historical snapshots stay cold.
   An unchanged creative state still acknowledges the turn, without making a
   new creative file. Save one current record and one journal per scope.
4. **Produce from that state.** The native craft owner receives the current
   objective, complete positive references, exact approved parts, one candidate
   per purpose, and concise exclusion reasons. Source research remains available
   for its evidenced use even when a draft that used it was rejected.
5. **Reconcile the result.** Check actual artifact hashes, task-local current
   pointers, existing job handoff and actual saved external-tool state. A local
   preview and the Canva-saved version are distinct facts. A classifier PASS is
   never an approval. Completion must not leave a stale next action active.
6. **Verify coverage.** At turn end the loop compares captured turns with
   reconciled receipts and consumer hashes. A missing reconciliation triggers
   a bounded recovery in the same session. Failed recovery produces a concrete
   fault and keeps stale state unusable; it never logs a false healthy receipt.

Before each subsequent production write, check that no new feedback arrived
after reconciliation. Mid-turn messages reopen the pending state. Safe source
reads and answering the user remain possible during recovery.

## What the current view contains

- The entire intended outcome: audience, purpose, desired effect, constraints,
  and the user-defined quality bar, synthesized into one readable brief.
- Exact approved components and their source/decision references. Preserve
  partial approvals at component level; do not approve a whole draft by proxy.
- Current candidate and exploratory alternatives, with explicit purposes.
  Exploration is allowed; alternatives are not all competing primaries.
- Material accepted/rejected decisions and short reasons, not a wall of bans.
- Decision scope: this component, artifact, task, project, or explicit global
  preference. Never promote a local correction into a global instruction by
  inference. Store intent even when the task has no artifact yet.
- Unresolved uncertainty, next useful action, and actual save/review state.
- An internal revision and covered-turn cursor; these are not user forms.

The full conversation, complete failed drafts, historical snapshots, logs and
receipts are retrieved only for a specific question. The loop cannot erase
already-loaded text from a model context; it can control subsequent inputs,
make authority explicit, and prepare an existing fresh-pen transfer when
repeated drift persists. A fresh context needs a correct packet, not the full
discard pile. Starting a new user-owned task remains a separate user decision.

## Keep / retire / delete

Retirement is about active authority, not whether a file has intrinsic value.
Keep useful research, preserve exact approved parts, and record why a candidate
failed. Use the existing document-history helper to archive clearly superseded
working copies with preserved hashes and short redirects. Do not promote an
older candidate just because the latest was rejected. Deliberate restoration
requires a new decision and retains its original provenance.

Never delete code, workflows, programs, original sources or another task's work
because a creative draft was rejected. Removing an implementation requires a
separate dependency/ownership audit. A scoped task archive is not a disk sweep.

## Integration map and build order

| Stage | Existing owner to extend | Acceptance evidence |
|---|---|---|
| 1. Formal state protocol and Jen replay | This offline prototype; existing document-history tests | Pending turn coverage, partial approval, intent preservation, stale action and wrong-task tests; failure reproduced from real Jen file |
| 2. Durable transactions and current-view rendering | `_active/harness/asset-filing-setup/06-system/document_history.py` and its installed Work counterpart | Real locking/concurrent writes, crash recovery, idempotency, archive hashes, old-link redirects; no two authority stores |
| 3. Turn lifecycle adapter | `execution/tool_event.py`, shared hooks and native global hook registrations | Prompt, mid-turn input, shell/Python writes, apply_patch, ordinary reads, resume and supported compaction lifecycle tested on real hosts |
| 4. Consumer integration | `job_board.py` briefs/checkpoints, `/fresh-pen`, `/handoff`, existing retrieval and project entry points | All consumers resolve the same revision; stale handoff rejected and refreshed; historical files stay available only on explicit retrieval |
| 5. Global activation and measurement | Thin global Codex and Claude instructions/hooks pointing to the canonical implementation | Preserve existing hooks and trust settings; verify actual hook firing in a new and resumed task on each supported host |

Reconcile the obsolete date/filename authority wording and its read guard in
stage 2; preserve newer decision-led index behavior already installed. Do not
rewrite all constitutions or archive the project tree as part of this change.
The existing job manager stays the job owner; this is its context maintenance
function, not a second planner or competing manager.

For a projectless task, use its own task workspace and explicit task binding.
For a repository, use the owning worktree and explicit artifact scope. Only
integration helpers may update main. Several tasks may share a project while
having different artifact purposes. Same-purpose concurrent changes require
revision-aware reconciliation, not last-writer-wins. Global hooks must never
fall back to writing a guessed canonical project when ownership is absent.

## Gates before claiming permanent activation

**Mechanical proof:** the supplied prototype tests validate transition and
packet properties only. They do not run native hooks or interpret language.

**Semantic proof:** replay full, real sequences from Jen and Angle Map. Present
the session model with original intent, full positive reference and cumulative
feedback; inspect its proposed interpretation against the recorded verdicts.
Include delayed feedback, two interleaved artifacts, partial approval, reversal,
exploration, and status-only turns. Do not grade by banned-word absence or
accept the model's self-score as proof. No paid or headless seat is assumed.

Also require non-content fixtures: a code fix that preserves the feature goal;
a strategy refinement that preserves its commercial outcome; a contradictory
research finding that retains provenance; a shorter plan that retains the
deadline and obligations; and a conversation with evolving intent but no files.
Cross-domain tests and a projectless live probe are required before a universal
collaboration claim. Passing only the Jen case is insufficient.

**Live proof:** demonstrate prompt capture and reconciliation on every turn of
at least a 10-turn controlled session, with one resume and a separately observed
compaction where supported. Run it in Codex and Claude if both are activated.
That is coverage for the tested run, not a universal reliability percentage.
Unsupported native events must be named; a saved config is not firing proof.

**Failure proof:** an omitted acknowledgment, missing source, wrong task,
stale writer, appended CURRENT block, or rejected-target next action must yield
a specific recovery condition. No infinite stop-hook loop. If the host cannot
support bounded same-turn recovery safely, keep that host staged and report
the exact limitation rather than claiming the global mechanism is complete.

**Creative proof:** accepted parts survive and subsequent work responds to the
whole brief. Farrice's verdict remains the quality authority. Neither checksum
success nor hook coverage promises great writing or that drift can never recur.

## Goal and engineering packet

- Target: continuous working-context reconciliation across supported Codex and
  Claude tasks, with the initial proof scoped to this owned worktree.
- Scope now: decision protocol, forensic fixture, executable tests and reviewable
  integration plan. Global runtime activation, live Jen changes, destructive
  cleanup, new tasks and extra model seats are not performed by this prototype.
- Source truth: the exact files in the evidence and integration sections;
  live Jen task `01a0a1e0-dcd8-7683-aa4f-31d2fe5096b0`; its recorded user turns;
  current user's every-turn and whole-intent requirements.
- Context plan: current brief and positive examples stay active; history is
  retrieved for evidence only; no full rejected-draft library in writer packets.
- Permitted side effect: local prototype and proof files in this initiative.
  The user's request authorizes preparing a global repair; no further permission
  is needed merely to plan or test it. Existing tool approval/trust and task
  ownership boundaries still apply to actual deployment.
- Evaluator: protocol tests plus real-file stack scan and a manually mapped
  Jen replay. Semantic interpretation is supplied, not autonomously proven.
- Stop for this proof: tests pass, failure fixture is detected, approved opening
  survives, rejected middle is excluded and no rejected-next-action is exported.
- Iteration cap: two repair passes per failing mechanism before revisiting the
  design. No open-ended autonomous rewrite loop.
- No-regression: prototype imports only Python standard library, changes no
  runtime files, does not touch live Jen work, hooks, main or global settings.
- Wake-up check: run `python3 -m unittest discover -s
  _active/harness/working-context-reconciliation/06-system -p 'test_*.py'` and
  read `06-system/proof.json`; next implementation slice is stage 2.
- Rollback: discard this isolated prototype. Future production transactions
  preserve original bytes and prior revisions; installer backups and rollback
  restore only owned additions without removing other hooks.

## Current proof and limits

Read [the machine receipt](06-system/proof.json). The protocol's semantic inputs
are manually constructed from user feedback; exact-quote validation proves
provenance, not correctness of interpretation. Native every-turn hook firing,
durable transactions, global installation, compaction continuation and actual
creative improvement remain NOT RUN by this prototype.

There is separate, real observational outcome evidence: after the owning Jen
task's reconciliation, Farrice wrote at 23:15:21 local time on September 14,
2026, "omg this is it so much better 9/10 thank you thank you!" He still wanted
small edits. Earlier, he deliberately selected v09 as a useful baseline after
rejecting it; that reversal is also recorded. The protocol must permit such
re-selection without converting it into full approval. This naturally occurring
improvement supports the repair hypothesis but does not isolate file retirement
from the fresh composition, clarified feedback and other concurrent changes.
It is not proof that this undeployed prototype caused the improvement.

This plan does not require Farrice to change modes, invoke `/job`, fill a form,
manage files or approve each housekeeping operation. It does require the build
to earn its activation claim through the gates above.
