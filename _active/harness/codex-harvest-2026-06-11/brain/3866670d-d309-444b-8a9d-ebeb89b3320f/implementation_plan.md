# Session Workspace System — Per-Conversation Folder Organization

Every `/session-kickoff` will auto-create a structured, dated folder for the conversation. All assets produced during that session get routed to this folder. You'll have an always-current master index to find anything by date, domain, or keyword.

## The Problem

Assets scatter across `brain/`, `deliverables/`, `_active/`, `swarm_outputs/`, and `.tmp/` with no connection to the conversation that produced them. Finding a LinkedIn strategy doc from Tuesday means hunting through unlabeled sidebar entries and hoping you remember the folder name.

## Proposed Changes

---

### New: `sessions/` Directory (The Master Workspace)

A new top-level `sessions/` directory becomes the single source of truth for per-conversation work.

**Folder naming convention**: `YYYY-MM-DD_HH-MM_domain--label`

Examples:
```
sessions/
├── SESSION_INDEX.md                    ← Master registry of all sessions
├── 2026-03-30_20-31_system--session-workspace/
│   ├── _manifest.md                    ← What was produced, auto-updated
│   ├── assets/                         ← Images, PDFs, generated files
│   ├── drafts/                         ← Work-in-progress content
│   ├── deliverables/                   ← Final outputs ready to use
│   └── research/                       ← Research notes, swarm outputs
├── 2026-03-30_17-05_strategy--workspace-reorg/
│   ├── _manifest.md
│   ├── assets/
│   ├── drafts/
│   ├── deliverables/
│   └── research/
└── 2026-03-29_23-33_linkedin--artifact-retrieval/
    └── ...
```

**Why this naming**:
- **Date-first** → Natural chronological sort in Finder/file manager
- **Time** → Multiple sessions on the same day get unique folders
- **Domain tag** → Visual clustering (`linkedin--*`, `extraction--*`, `system--*`)
- **Label** → Human-readable at a glance

---

### New: `SESSION_INDEX.md` (Master Registry)

A running table at `sessions/SESSION_INDEX.md` that auto-updates every kickoff:

```markdown
# Session Index

| Date | Time | Domain | Label | Folder | Status |
|------|------|--------|-------|--------|--------|
| 2026-03-30 | 20:31 | System | Session Workspace Build | [link] | 🟢 Active |
| 2026-03-30 | 17:05 | Strategy | Workspace Reorg | [link] | ✅ Complete |
```

Fields: date, time, domain, label, folder path link, status (🟢 Active / ✅ Complete / 📦 Archived).

---

### New: `_manifest.md` (Per-Session Asset Tracker)

Each session folder gets a `_manifest.md` that tracks what was produced:

```markdown
# Session: System — Session Workspace Build
**Date**: 2026-03-30 20:31 PST
**Conversation ID**: 3866670d-d309-444b-8a9d-ebeb89b3320f

## Assets Produced
| # | Type | Filename | Description |
|---|------|----------|-------------|
| 1 | Script | session_workspace.py | Folder creation engine |
| 2 | Workflow | session-kickoff.md | Updated workflow |

## Key Decisions
- [Auto-populated with session notes]

## Related Sessions
- [Links to related session folders]
```

---

### [NEW] [session_workspace.py](file:///Users/farricecain/Google%20Antigravity/execution/session_workspace.py)

Python script that handles all folder operations. Called by the session-kickoff workflow.

**Commands**:
```bash
# Create a new session workspace
python execution/session_workspace.py create "System" "Session Workspace Build"

# List recent sessions
python execution/session_workspace.py list --last 10

# Search sessions by keyword
python execution/session_workspace.py search "linkedin"

# Archive old sessions (consolidate into monthly bundles)
python execution/session_workspace.py archive --before 2026-03-01

# Log an asset to the current session's manifest
python execution/session_workspace.py log-asset "/path/to/file" --type "Deliverable" --desc "Final strategy doc"
```

**`create` output** (what the workflow reads):
```
SESSION_PATH=/Users/farricecain/Google Antigravity/sessions/2026-03-30_20-31_system--session-workspace
```

The script:
1. Creates the dated folder with subfolders (`assets/`, `drafts/`, `deliverables/`, `research/`)
2. Generates the `_manifest.md` template
3. Appends entry to `SESSION_INDEX.md`
4. Prints the path for the workflow to capture

---

### [MODIFY] [session-kickoff.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/session-kickoff.md)

Add a new **Step 1.5: Create Session Workspace** between the label step and the task detection step:

```markdown
## Step 1.5: Create Session Workspace

// turbo
After generating the conversation label, create the session's working directory:

\```bash
python execution/session_workspace.py create "[Domain]" "[Label]"
\```

Capture the output path. All assets produced during this session should be
saved to the appropriate subfolder:
- `assets/` — images, PDFs, generated media
- `drafts/` — work-in-progress content, rough versions
- `deliverables/` — final outputs ready to use or share
- `research/` — research notes, swarm outputs, analysis

Add the workspace path to the kickoff block:
**Session Workspace**: `sessions/YYYY-MM-DD_HH-MM_domain--label/`
```

Also update the kickoff block template in Step 3 to include the workspace path.

---

### [MODIFY] [end-session.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/end-session.md)

Add a step to finalize the session workspace:

```markdown
### 1.5: Finalize Session Workspace
Update the session's `_manifest.md` with all assets produced.
Mark the session as ✅ Complete in `SESSION_INDEX.md`.
Move any deliverables that were written elsewhere into the session's
`deliverables/` subfolder (or symlink them).
```

---

## Consolidation Strategy (Future-Proof)

When folders accumulate, run:
```bash
python execution/session_workspace.py archive --before 2026-03-01
```

This will:
1. Create `sessions/_archive/2026-02/` monthly bundles
2. Move completed sessions into the monthly folder
3. Preserve the `SESSION_INDEX.md` entries (marked 📦 Archived with updated path)
4. Keep any session marked 🟢 Active in place

Manual consolidation: You can always merge related session folders (e.g., three LinkedIn sessions → one `linkedin-launch-campaign/` folder) and update the index.

---

## Verification Plan

### Automated Test
```bash
# Dry-run test — creates a session workspace and verifies structure
python execution/session_workspace.py create "Test" "Verification Run"
# Expected: folder created at sessions/YYYY-MM-DD_HH-MM_test--verification-run/
# Expected: _manifest.md exists with correct template
# Expected: SESSION_INDEX.md has new entry
# Then clean up:
rm -rf "sessions/$(ls sessions | grep test--verification-run)"
```

### Manual Verification
1. Run `/session-kickoff` in a new conversation
2. Verify the kickoff block includes a `Session Workspace` path
3. Check the folder exists in Finder at `Google Antigravity/sessions/`
4. Confirm `SESSION_INDEX.md` has the new entry
5. Produce a deliverable, verify it can be saved to the session folder
