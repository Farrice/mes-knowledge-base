# Preservation-First Mac Recovery Mission

**Started:** August 16, 2026
**Owner:** System Audit
**Status:** Baseline frozen; Drive hierarchy and connector round-trip verified; routing repaired; destructive actions awaiting exact approval
**Acceptance gate:** At least 150 GiB available on `/System/Volumes/Data`

## Current verdict

The Mac remains in an emergency-capacity state. The baseline Data-volume reading showed only 12,122,820 KiB available (about 11.56 GiB), while Downloads physically occupied 418,323,672 KiB (about 398.94 GiB). No cleanup, cloud move, eviction, or deletion of user material has occurred in this mission.

The final overnight reading showed 15,183,496 KiB available (14.48 GiB). That transient improvement is not credited as cleanup because no user files changed, and it still remains below the 15 GiB migration floor.

The authenticated Google Drive account is confirmed as Farrice Cain (`farrice.cain@gmail.com`). The approved archive hierarchy now exists in My Drive. A 1,372-byte baseline manifest completed an upload, metadata check, fresh download, and exact byte-for-byte comparison. Google Drive for desktop itself remains uninstalled because macOS requires an administrator password and interactive setup; the downloaded package passed Apple notarization and Gatekeeper before its temporary installer was removed.

The recovery mission now deterministically routes to System Audit instead of the unrelated ROI-driven offer workflow. Free-first offer research still routes to Deep Research OS when requested on its own. The preflight also understands that “no unapproved deletion or publishing” is a prohibition, not an action request; mixed positive/negative action clauses remain blocked correctly. Operator Core, Free-First Research, Autopilot runtime, and Codex/Claude parity suites pass.

The Downloads scan found no `.download`, `.crdownload`, `.part`, `.partial`, `.aria2`, `.opdownload`, or `.filepart` files. The single suspicious wrapper is a 2.556 GiB `Megapack Vol 1point2.rar.cpgz`; it is preserved in place and recorded as a non-canonical 30-day quarantine candidate rather than being assumed corrupt or safe to delete.

The archive inventory contains 327 ZIPs occupying 141.285 GiB, plus the 2.556 GiB `.cpgz`, for 143.841 GiB combined. A serial read-only pass completed at least 204 ZIPs: all 204 were SHA-256-readable and CRC-valid, with zero CRC failures and zero read errors. The three archives larger than 5 GiB also passed, but remain parked as oversize singletons. The scan stopped at a safe boundary without a persisted full per-file ledger, so no untested archive is eligible for migration and no claim is made about additional duplicate groups.

The Drive manifest folder contains 13 control files. Fresh raw downloads of `README.md` and the overnight status receipt matched their local bytes exactly at verification time.

## Separate system warnings

- **VERIFIED:** The local Notion mirror freshness check reports 115.83 hours stale against a 72-hour halt threshold.
- **UNCONFIRMED:** The finalizer's Notion regression probe could not resolve `api.notion.com` from this restricted execution context. That is not treated as evidence that Notion itself is down.
- No mirror refresh or Notion write was attempted. This warning is parked for a separate authenticated connector check because it does not justify expanding the storage mission into an external mutation.

## Locked safety rules

1. Exact targets must appear in an approved manifest before they move.
2. Moving an item to Trash and emptying that Trash batch are separate approvals.
3. iCloud `dataless` placeholders, active Git repositories, app databases, Photos, Notes, Apple media-analysis state, and confidential client material remain excluded.
4. Google Drive must use **Stream files**. Desktop, Documents, Downloads, Photos, and active repositories must not be mirrored or automatically backed up.
5. Each cloud batch must be uploaded, reach sync-idle with no error, be verified in the web interface, and pass a sampled re-download hash check before the local source can move to Trash.
6. Market research remains blocked until the live volume has at least 150 GiB available.
7. No post, message, schedule, or other external publication is authorized.

## Evidence state

- Baseline: `baseline-2026-08-16.json`
- Final overnight gate state: `overnight-status-2026-08-17.json`
- Exact-duplicate candidates: `deletion-manifest.json`
- Cloud-batch interface: `cloud-batch-manifest.template.json`
- Drive account, folder IDs, and desktop-client gate: `google-drive-control-plane.json`
- Verified connector round trip: `cloud-batch-000-connector-smoke.json`
- Worktree preservation and retirement decisions: `worktree-retirement-manifest.json`
- Operator routing and risk-parser repair: `operator-routing-repair-receipt.json`
- Ambiguous/incomplete-file control: `quarantine-manifest.json`
- Archive integrity scope and honest partial receipt: `archive-integrity-audit.json`
- Offer-research interface: `offer-hypothesis-registry.template.json`
- Active offer hypothesis registry: `offer-hypothesis-registry.json`
- Exact morning approvals and interactive setup: `morning-action-card.md`

## Stop conditions

Stop immediately on any hash mismatch, cloud error, wrong Google account, unexpected mirroring, incomplete upload, or free space below 15 GiB during a migration operation. Because the current baseline is already below 15 GiB, no cloud copy batch may begin until either the verified duplicate batch is emptied or another separately approved action raises the machine above that floor.

## Current decision surface

### LOCKED

- Preservation first.
- Recover 150 GiB before research.
- Google Drive for business archives; iCloud for personal and Apple-managed material.
- Keep both valid original design archives and extracted libraries in their separate cloud categories.

### PARKED

- Conditional archive/extracted pairs until integrity and completeness checks pass.
- Eight clean `.tmp` worktree lanes are remote-preserved and eligible for lifecycle retirement, pending exact approval; six worktrees outside `.tmp` remain protected.
- App-cache cleanup unless Downloads and cloud migration cannot reach the target.
- The Free-First offer research mission until the storage gate passes.
- Notion mirror refresh until a separately authorized, authenticated external check is run.

### NEXT ACTION

Open `morning-action-card.md`. It contains the exact, bounded approval language for the 11-path duplicate batch and the eight remote-preserved worktree lanes, plus the administrator-authenticated Google Drive setup checklist. Nothing outside those manifests is authorized.
