# Solution Card — Briefing Room cards across worktrees

**Problem:** A visual brief rendered in an isolated worktree appeared in that
worktree's generated Briefing Room, but the card was rewritten to an absolute
path under the main checkout. Clicking it opened a 404 because the live server
was correctly jailed to main while the brief still existed only in the lane.

**Root cause:** The Room encoded checkout-specific `file://` card addresses and
relied on JavaScript to strip the current root. That made a generated index
fragile when an artifact moved between worktrees or someone normalized its
paths before the brief itself was integrated. Generation checked context-pack
paths but did not prove the card target.

**Repair:** `execution/brief_library.py` now emits two addresses from the same
known file: a Room-relative address for static use and a repo-relative address
for the ROOT-jailed `/repo/` live route. Generation verifies every card, `md`,
`ctx`, and supersession target before replacing the index. The read-only
`python3 execution/brief_library.py verify` command checks an existing Room.

Context packs use the same portability rule. Their repo-relative `path` is the
canonical identity; `abs` remains only as a render-time compatibility hint.
The librarian resolves `path` from the active checkout first and canonical main
second, which preserves main-only untracked media without making a disposable
worktree path authoritative. `verify` fails when neither root contains the
referenced file.

**Operating rule:** A lane-local brief is previewable from that lane. It becomes
part of the main live Room only after its full brief directory is integrated.
Never hand-edit a generated index to point at a different checkout.

**Proof:** Regenerate the Room, run `brief_library.py verify`, then tamper one
in-memory `data-repo-path`; the verifier must report the missing card and live
target. For end-to-end proof, serve the lane locally and require HTTP 200 for
both `/room` and the card's `/repo/deliverables/research-briefs/...` route.
`execution/verify_briefing_room_portability.py` preserves the cross-worktree
resolution order as a deterministic regression test.
