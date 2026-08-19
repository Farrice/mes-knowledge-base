# Briefing Room Link Receipt

Verified August 19, 2026 in the isolated repair lane.

## Root cause repaired

- The four offer briefs were brought forward from the parked offer branch onto the latest committed workspace line.
- Briefs were re-rendered from their canonical source JSON; the Room was regenerated with 51 active cards.
- Card links now carry portable static paths plus explicit repo-relative live routes.
- HTTP protocol alone no longer activates Pulse routing. The Room requires a successful `/ping` handshake whose `root` matches the checkout that generated it.
- `/ping` now returns `root` and `commit`; a server on the requested port is no longer silently reused when it belongs to another checkout.

## Required cards

| Card | Room presence | HTML | Markdown | Context |
|---|---:|---:|---:|---:|
| `work-recovery-command-board` | PASS | 200 | 200 | 200 |
| `market-proof-dossier` | PASS | 200 | 200 | 200 |
| `offer-launch-kit` | PASS | 200 | 200 | 200 |
| `demo-test-receipt` | PASS | 200 | 200 | 200 |

The landing page route also returned 200.

## Click behavior

- Real Pulse server: Room handshake reported `live=true`; the Offer Launch Kit card navigated to `/repo/deliverables/research-briefs/offer-launch-kit/offer-launch-kit-brief.html` and loaded the correct brief title.
- Generic HTTP preview: handshake reported `live=false`; the same card retained its relative `offer-launch-kit/offer-launch-kit-brief.html` route and loaded successfully.
- This negative control proves the card no longer rewrites itself to a `/repo/` route that the current server cannot answer.

## Security and failure controls

- `GET /repo/.env` → 403.
- traversal-shaped request → denied or normalized to 404.
- unknown route → 404.
- retired offer-worktree path `.tmp/codex-worktrees/zero-momentum-offer` is absent from the inspected Room, offer briefs, context packs, and landing page.
- Pulse preview browser tab loaded with zero unexpected console errors after favicon handling was added.

This receipt verifies local navigation. It does not claim that the isolated branch has been merged into the dirty main tree.
