---
date: 2026-08-01
session: codex-end-session-control-plane
tier: operator-guide
status: enriched
---

# Codex End-Session Control Plane — What We Built 2026-08-01 and How to Use It

> `/end-session` now has a thin Codex-native coordinator while `.agent/workflows/end-session.md` remains the behavior authority. The coordinator binds a task to one exact handoff, organizes only explicitly owned artifacts, gates Git to a dedicated `codex/*` worktree, writes pointer-only global retrieval records, and tells the Codex app when to rename, pin, or archive the task.

## ⚡ If you only read 10 lines

- Create one handoff source whose H1 exactly matches `[Domain]: [Specific Object] - [Outcome]`.
- List the same core paths in the handoff and the closeout manifest.
- Run `python3 execution/codex_end_session.py run --manifest <json>`.
- The coordinator saves from the named source; it never guesses from the newest temp file.
- `handoff_store.py verify` must clear thread, title, body hash, branch, core paths, remaining priority, and Do-Not-Rebuild checks.
- `ready`, `blocked`, `active`, and `mid-build` tasks stay visible and pinned.
- `done` archives only after the handoff, spine, verifiers, and Git receipt are valid.
- Automatic Git is limited to manifest-owned paths on a dedicated `codex/*` worktree.
- `main`, secrets, unexpected deletions, unrelated dirt, divergence, and same-tree collisions hold Git.
- Global state under `~/.codex/end-session/` stores pointers and receipts, not duplicated project content.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/codex_end_session.py run --manifest <json> --dry-run` | Identity, lifecycle, organization, verifier, and Git-policy preview | Before the first real closeout in a workspace or after changing the manifest |
| `python3 execution/codex_end_session.py run --manifest <json>` | Verified handoff, shared closeout receipt, review queue, integration packet, and safe branch push | The task is ready to close or hand off |
| `python3 execution/handoff_store.py verify <thread> --source <path> --json` | Exact source-versus-stored semantic receipt | A resume artifact must be proven independently |
| `python3 execution/verify_codex_end_session.py` | Collision, lifecycle, organization, and Git matrix | After changing closeout behavior |
| `python3 execution/verify_system_control_plane.py --section end-session` | Scoped control-plane contract proof | The full system suite has unrelated baseline debt |
| `python3 execution/sync_operator_core_end_session.py --check` | Global/local wrapper alignment proof | After changing the canonical workflow or global front door |

## The mental model

### 1. A handoff is an identity record

Recency is not identity. A newer file may belong to another task and still be perfectly valid Markdown. The closeout therefore starts from an explicit path and checks semantic fields in addition to hashes. A matching checksum proves an unchanged copy; the thread, title, branch, paths, remaining priority, and Do-Not-Rebuild checks prove it is the right task.

### 2. The app and filesystem have separate owners

`codex_end_session.py` owns deterministic filesystem and Git work. The Codex app owns task rename, pin, and archive. The coordinator returns `task_actions`; the model applies those native actions only after reading the receipt. Python never pretends it renamed or archived a task.

### 3. Closeout does not grant broad Git authority

The manifest is the staging boundary. A file created during closeout is not automatically task-owned: only manifest paths and recognized closeout receipts qualify. Unexpected paths go to review. The branch may push itself; it may never integrate itself into `main`.

## Exact handoff identity

### What it is

`handoff_store.py save <source> --json` records source and stored checksums. `handoff_store.py verify <thread> --source <source> --json` reopens the canonical stored handoff and checks:

- requested thread and source thread
- source and stored H1 title
- normalized body checksum
- branch metadata
- resolvable core paths
- remaining priority
- Do-Not-Rebuild guidance

The Codex manifest adds one more boundary: its task title and core path set must equal the source handoff.

### When to reach for it

Use it whenever more than one task can write to a shared temp directory, when a closeout is resumed later, or when the wrong handoff would be worse than no handoff.

### When not to

For a conversational task with no artifacts, do not manufacture a handoff. For a focused transfer packet without whole-session housekeeping, use `/handoff` rather than `/end-session`.

### Worked example

The isolated verifier creates two handoffs, makes the unrelated one newer, and proves the exact Alex-style source still drives the spine. It also proves title, body, branch, and manifest-path mismatches fail before downstream work.

### Honest edges

`--from-temp` remains for compatibility. It now filters by thread and refuses unscoped ambiguity, but an explicit path remains the preferred route.

## Conservative organization and review

### What it is

`artifact_moves` is optional manifest data. A move runs only when both source and destination are task-owned, the source exists, the destination does not, and neither the handoff nor a core path is being moved. Loose root artifacts without an exact destination are not guessed into a folder; they are queued for review.

The global review receipt also captures unowned dirt, unexpected generated paths, Git blockers, and read-only self-heal findings. Codex self-heal uses `report --json --no-cache`, so a diagnostic scan does not silently alter the repository.

### When not to

Do not use closeout to reorganize a project wholesale. Broad filing, archive, deletion, and content rewrites remain separate reviewed work.

## Git and integration

### What it is

Automatic commit and push require all of the following:

- current branch starts with `codex/`
- checkout is a dedicated linked worktree
- no remote-behind divergence
- no detached HEAD
- no foreign active-tool or fresh session collision
- no secret-like path or added secret line
- no unexpected deletion
- no unrelated pre-existing dirt
- required component verifiers pass
- remote SHA equals the local commit after push

The integration packet records base, branch, commit, remote SHA, changed paths, verifier and spine checks, blockers, review queue, and the manual safe-merge route. There is no automatic `main` merge or push.

### Honest edges

Hook trust is absolute-path scoped. A newly created worktree may need separate desktop consent before the broad Google Operator Core hook-parity verifier passes. The coordinator does not edit `~/.codex/config.toml` or `.codex/hooks.json` to manufacture trust.

## Task lifecycle

The title is always proposed in the retrieval format. Unfinished statuses pin. A `done` status alone is insufficient to archive; the receipt must be valid and the real run must have completed. Dry-runs and failed or partial closeouts never archive.

## Composition options

| Option | Add it when | What it contributes |
|---|---|---|
| `/handoff` | Another task needs a focused continuation packet | Produces the source body; `/end-session` adds identity, housekeeping, lifecycle, and Git |
| `/system-audit` | Control-plane behavior is drifted or not firing | Owns diagnosis and repair of the lifecycle system |
| `/source-to-skill-system` | Closeout behavior must become reusable and connected | Enforces companion-layer and duplicate-system boundaries |
| `/repeatability-spine` | A closeout revision loses a previously good behavior | Adds preservation lock and regression replay |
