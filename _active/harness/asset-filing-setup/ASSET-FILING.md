# Find and File Assets

Start at **[Farrice Work](/Users/farricecain/Work)**. Your personal browser downloads continue going to **Downloads**. Codex files only assets identified as belonging to the task it is carrying out.

## Find something quickly

- Existing projects retain their established homes. Start from the project's INDEX.md, handoff, or Work shortcut before creating anything new.
- [Clients](/Users/farricecain/Work/20%20Clients), [Business](/Users/farricecain/Work/30%20Business), and [Creative](/Users/farricecain/Work/40%20Creative) hold new local projects that do not already have a canonical home.
- **INDEX.md** describes the project. **ASSET-INDEX.md** lists the assets, versions, review status, and clickable file links.
- Look in **04-deliverables** for approved work. A file's newest version is not necessarily approved.
- Ask Codex: “Find the approved kitchen-pan clip for 5200 Armida and verify the file still matches its record.” It should check the established project index first, then use the filing helper for Work projects.

## One home, readable names

Project folders use descriptive lowercase words separated by hyphens: `jen-santulan-5200-armida`. Project titles remain readable: **Jen Santulan — 5200 Armida**. Website projects should use the same recognizable project title where the tool supports it; keep the website's project URL in the project index.

Files use **project-description-v01-status.ext**. Example: `5200-armida-exterior-camera-rise-v02-review.mp4`. Include a meaningful format when needed: `vertical-1080x1920`. Examples illustrate names, not existing or approved assets.

Use `source`, `draft`, `review`, `approved`, or `export`. An export is a format derivative, not an approval. Increase versions for changed content; never overwrite an earlier version. Record actual approval before marking a file approved. Avoid generic download names, unexplained abbreviations, `new`, and `final-final`.

Living guides stay undated. Date historical receipts as `YYYY-MM-DD-description.md`. Record a downloaded file's original name and origin even when its working copy gets a readable name.

| Folder within the project | What belongs there |
|---|---|
| `01-source` | Source material, with provenance |
| `03-working-drafts` | Editable work in progress |
| `05-assets` | Images, clips, and other assets awaiting review |
| `04-deliverables` | Explicitly approved outputs |
| `90-exports` | Derivatives prepared for another tool or destination |
| `06-system` | Asset register and operational receipts |

Reuse the existing artifact-router hierarchy. Add `02-research` or `99-archive` only when useful. Do not impose a new hierarchy on an established project.

## Current documents and historical material

Before drafting, recommending an offer, or continuing a system build, resolve the active project and its current anchor. The order is: latest explicit user decision, the decision-backed living CANON/index, current supporting documents, then historical records only when requested. A conflicting or stale index is evidence to reconcile, not permission to disregard the latest decision.

**Modification time, an undated filename, a canonical label, and search rank never establish authority.** Dated records can contain valuable decisions, but they do not automatically become the working document. Memory and old task summaries are retrieval leads; verify them against current project decisions before using them as anchors.

| State | Default use |
|---|---|
| Current | The one operational anchor for a named purpose, such as offer, project brief, or system specification |
| Draft / review | Candidate or supporting work; never silently replaces a current anchor |
| Parked | Deliberately paused; do not recommend, activate, or resume without a new user decision |
| Superseded | Replaced by a named successor; follow the successor |
| Archived / retired | History only; excluded from normal retrieval and recommendations |

Current authority and approval are separate: a current working draft is not automatically a client-approved deliverable. Multiple purposes can each have one current document; several competing offers cannot all become the default offer merely because they exist.

### Required reconciliation step during filing and before task completion

1. At the start, read the project's existing CANON/index, parked decisions, and current document. Record the authority revision used to start work.
2. File a revision as a new version. Keep the current anchor until there is an explicit replacement decision or clear authorization to update that operational document.
3. Before promoting the revision, re-read current state. If another task has changed the anchor, reconcile the two revisions first. Never automatically change the expected revision just to make an older task's write succeed.
4. When a replacement is authorized, move the old working copy into `99-archive/YYYY-MM-DD-rNNNN/`, preserving its bytes, prior path, decision, and successor. Leave a short historical redirect at the old path so old links do not reopen stale content. Update CANON, the stable current link, the asset index, and any known active handoff pointers together. Do not change unrelated inbound references by a broad text replacement.
5. Parking a direction removes its current anchor. It does not select an older offer as a fallback. Restore history only through an explicit decision and a new versioned working copy.
6. Verify the current link resolves, the current file matches its recorded checksum, the archived file is preserved, and ordinary retrieval excludes historical versions. Record unresolved conflicting decisions rather than declaring everything current.

This task authorizes routine, reversible retirement of clearly superseded versions during the work. Age alone is never enough to archive. Existing ambiguous offer documents and other people's active work require decision recovery before changes. No bulk historical cleanup or deletion is implied.

### Document-history helper

For Work projects managed by this helper, CANON.md is the readable current map, `00-start-here/<purpose>.md` is a stable link, and `06-system/document-state.json` records revisions and decision history. The existing asset register remains the asset inventory; this small document-state record adds only current authority and retirement. Existing human-owned CANON files are preserved and must be reconciled explicitly before adoption. Repository projects can use the helper only from their owning worktree; ordinary reads can use their native CANON and index.

```sh
python3 '/Users/farricecain/Work/50 Reference/Asset Filing/document_history.py' current --project-home '/path/to/project'
python3 '/Users/farricecain/Work/50 Reference/Asset Filing/document_history.py' promote --project-home '/path/to/project' --key offer --path '03-working-drafts/project-offer-v02-review.md' --decision 'Exact replacement decision and its source' --expect-revision 1
python3 '/Users/farricecain/Work/50 Reference/Asset Filing/document_history.py' retire --project-home '/path/to/project' --key offer --state parked --decision 'Exact parking decision and its source' --expect-revision 2
```

The revision check and per-project lock prevent stale concurrent promotions. Interrupted transitions leave a journal and block anchor use until reconciled. Normal asset search excludes parked, superseded, and archived entries; explicit historical work adds `--include-history`. Raw repository searches should exclude `99-archive`, `_archive`, and other known archive directories unless historical recovery is requested. A legacy index may still mix old and current material: verify status rather than trusting a “Live now” heading.

## What Codex does during an authorized task

1. Resolve the project home and current document authority from task context, explicit decisions, and existing indexes. An uncertain destination stays unresolved; do not guess or create a duplicate project.
2. Use an explicit download result/path. With concurrent tasks, the newest file in Downloads is not proof of ownership. Confirm the source, filename, and download completion.
3. Copy that task's file into its proper project folder. Keep the original. Never sweep, move, or rename unrelated Downloads files.
4. Give the working copy a readable versioned name, verify its bytes, and update the project's asset index and provenance record.
5. When reusing an asset, check its project, status, format, existence, and recorded checksum. Do not automatically choose the newest file across projects.
6. Upload only the assets and destination authorized by the current task, using available connector or computer controls. Verify completion in the receiving tool. Record the destination URL and the exact asset version in the project handoff or transfer receipt. Private files need specific data/destination authorization. Uploading is separate from publishing, outreach, or spending approval.
7. Complete the document reconciliation step above, then report the final project location and any blocked transfer. Continue other authorized work where possible.

This is a task-time default, not a background watcher or a promise of unrestricted computer control. Browser, OS, connector, and managed approval restrictions still apply. Never work around a tool security denial. Ordinary file-picker handling is attempted through permitted tools.

## Filing helper for local Work projects

Codex runs this; Farrice does not need to run commands.

```sh
python3 '/Users/farricecain/Work/50 Reference/Asset Filing/asset_filing.py' init --category client --project 'Client Name - Project Name'
python3 '/Users/farricecain/Work/50 Reference/Asset Filing/asset_filing.py' file '/path/to/completed-download.mp4' --project-home '/Users/farricecain/Work/20 Clients/client-name-project-name' --asset 'kitchen-pan' --status review
python3 '/Users/farricecain/Work/50 Reference/Asset Filing/asset_filing.py' find 'kitchen-pan' --status approved --verify
```

The helper copies, assigns versions without overwriting, records original names/paths and optional source URLs, checks SHA-256, and writes ASSET-INDEX.md plus `06-system/asset-register.jsonl`. Repeating the same import returns the existing identical copy. Approved status requires `--approval-note` identifying the actual approval. Search reports missing or changed files instead of treating them as valid.

The helper is limited to physical Work client/business/creative project folders. Existing Antigravity projects retain their native `execution/artifact_router.py` and `execution/asset_index.py`, project indexes, and Git worktree rules. Work shortcuts are entry points, never duplicate stores or permission to write into the integration checkout.

## Access and proof

Chrome's “Ask where to save each file before downloading” is off, reported by Farrice. The default download destination remains Downloads. Explicit Save As actions or site-specific dialogs may still appear.

Farrice approved and the setup saved narrowly scoped Codex writable roots for Work client/business/creative folders and this filing-support folder. It preserves the existing approval policy and network restrictions. A saved configuration is not proof that an already-running task adopted it. See [SETUP-RECEIPT.md](/Users/farricecain/Work/50%20Reference/Asset%20Filing/SETUP-RECEIPT.md) for actual installation and test results.

No background cleanup, global Downloads redirection, bulk migration, website upload, or publication is part of this setup.
