# Asset and Document Filing — Setup Receipt

Updated 2026-09-12. Task: 01a097c8-631e-7763-9ca7-9ae0e63735ba.

## Installed

- Start at `/Users/farricecain/Work/ASSET-FILING.md`; Work/START-HERE.md links to it.
- The readable current-document map is `/Users/farricecain/Work/30 Business/asset-filing-setup/CANON.md`.
- Helpers are installed in `/Users/farricecain/Work/50 Reference/Asset Filing/` and run during authorized tasks. No background sweep was installed.
- The global Codex instruction now loads the filing guide for task assets and documents. It requires current-authority lookup, version reconciliation, historical exclusion, and task-specific transfer verification.
- The saved default permissions profile is `asset-filing`, extending normal workspace permissions with exactly Work/20 Clients, Work/30 Business, Work/40 Creative, and Work/50 Reference/Asset Filing. Approval policy is unchanged and command network access remains restricted. Other configuration was compared and preserved.
- The four saved folder permissions passed read/write checks in a fresh Codex CLI sandbox with managed requirements included and no configuration overrides. This proves the saved profile, not adoption by an already-running desktop task.
- Personal browser downloads remain in Downloads. No original or unrelated download was moved, renamed, or deleted.

## Current and historical documents

Use one current anchor per purpose. File new revisions separately. Promote only from an explicit decision or authorized operational update. Re-read the authority revision before promotion; a stale parallel task must reconcile rather than overwrite it. Retiring an anchor preserves its bytes in 99-archive, leaves a redirect at the old path, updates the current link and indexes, and records the decision and successor. Parking leaves no current anchor and never revives an older offer as a fallback.

The actual guide is the live proof: revision 2 is current, revision 1 is preserved byte-for-byte in `99-archive/2026-09-12-r0002/`, the old path is a redirect, and ordinary retrieval excludes it. Current working authority is separate from human approval.

## Verification

- 9 asset-filing checks passed.
- 15 document-history checks passed, including stale parallel promotion refusal, history exclusion, original preservation, stable successor links, existing CANON preservation, and interrupted-transition detection.
- 6 native inventory checks passed, including parked/frontmatter and superseded/sidecar exclusion, invalid metadata handling, archive classification, and correct scanning inside a temporary worktree.
- The broader native artifact-router verifier passed after correcting a worktree-ancestor exclusion bug. Its generated global inventory and move plans were preserved in scratch and excluded from the deliverable.
- A real LinkedIn index rebuild using the repaired generator omitted an explicitly parked offer formerly listed as live. It also stopped advising that dates or undated filenames confer authority. The proof render stays in lane scratch because its HTML contains temporary worktree paths.

## Limits and remaining integration

The live Work helpers, guide, and global configuration are installed. The two shared repository generator repairs are preserved in `codex/asset-filing-setup`; their integration status is recorded in installation.json. After integration, regenerate the LinkedIn front door from the canonical checkout. Do not publish the temporary lane HTML as the permanent entry point.

The complete older-offer corpus has not been reconciled or bulk archived. Existing explicit parked/superseded status is honored by the repair; ambiguous business decisions still require recovery before reclassification. The index rebuild also reported 530 broken links in the pre-existing LinkedIn tree; that broader repair is outside this setup.

A real browser transfer remains UNVERIFIED. Browser Use rejected opening the harmless localhost test page because of administrator-enforced policy. No bypass was attempted. The test server was stopped; no browser download or upload occurred. This does not establish that other websites are blocked. Existing desktop tasks may retain their previous permission/instruction state.

## Recovery

Before-change global backups: `/Users/farricecain/.codex/backups/asset-filing-20260912T234101Z/` and `/Users/farricecain/.codex/backups/asset-filing-profile-20260912T235558Z/`. The profile migration changes representation of the same approved scope; it adds no further folders.

Before-upgrade local files: `/Users/farricecain/Work/50 Reference/Asset Filing/99-archive/20260912T234846Z/`.

Permission schema reference: https://learn.chatgpt.com/docs/config-file/config-reference (default_permissions, permissions.<name>.extends and filesystem).
