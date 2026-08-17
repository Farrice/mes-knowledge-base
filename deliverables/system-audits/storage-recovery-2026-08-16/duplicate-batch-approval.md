# Exact-Duplicate Batch 001 — Approval Sheet

**Decision requested:** Approve or reject moving the 11 paths below to Trash.
**Recorded candidate footprint:** 12,022,009,856 allocated bytes (11.196 GiB). Final reclaim is accepted only from the live volume reading after this exact Trash batch is emptied.
**Current mutation state:** Nothing listed here has been moved or deleted.

Every removal candidate is byte-identical to the retained file shown beside it. Files were verified with SHA-256. Directory trees were verified using a sorted per-file SHA-256 manifest and `diff -qr` with a zero exit status. Full hashes, byte counts, and rollback paths are recorded in `deletion-manifest.json`.

| # | Move to Trash | Retain | Allocated GiB |
|---:|---|---|---:|
| 1 | `~/Downloads/02_Design_Assets/Style Bender For Photoshop.zip` | `~/Downloads/02_Design_Assets/Templates/Style Bender Template For Photoshop-1696955105011/Style Bender For Photoshop.zip` | 2.832 |
| 2 | `~/Downloads/02_Design_Assets/9592d114-2a17-4ebc-8d80-17c7a87043ab.zip` | `~/Downloads/02_Design_Assets/Kalypso - Instagram Carousel Package (V2).zip` | 1.753 |
| 3 | `~/Downloads/Claude (1).dmg` | `~/Downloads/Claude (3).dmg` | 0.328 |
| 4 | `~/Downloads/Claude (2).dmg` | `~/Downloads/Claude (3).dmg` | 0.326 |
| 5 | `…/Style Bender For Photoshop 2/Style 1.psd` | `…/Style Bender For Photoshop/Style 1.psd` | 1.150 |
| 6 | `…/Style Bender For Photoshop 2/Style 2.psd` | `…/Style Bender For Photoshop/Style 2.psd` | 1.955 |
| 7 | `…/Style Bender For Photoshop 2/Style 3.psd` | `…/Style Bender For Photoshop/Style 3.psd` | 1.702 |
| 8 | `…/Mockups/Modelled-Oversized-T-Shirt-Mockup-By-Studio-Innate-2.1-o42fxj (1)` | Same directory name without ` (1)` | 0.588 |
| 9 | `…/Mockups/closeup-texture-tshirt-mockup-with-color-changeable (1)` | Same directory name without ` (1)` | 0.207 |
| 10 | `…/Mockups/editable-mockup-realist-printed-catton (1)` | Same directory name without ` (1)` | 0.189 |
| 11 | `…/Mockups/editable-extreme-closeup-mockup-screen-printing-looks (1)` | Same directory name without ` (1)` | 0.165 |

## Explicit protection control

`~/Downloads/02_Design_Assets/Hoodie V.2 (1)` will **not** move. It contains nine files versus eight in the unnumbered folder, including the unique 172,314,827-byte file `MyBPM Template-Hoodie Vol2 Back Mockup Irhasalfahad.psd` with SHA-256 `109458219e9b7464a219db4be87bacf2ffd91dbee3421b3be1a298e9363533ea`.

## What approval authorizes

Approval authorizes only moving these 11 exact paths into a mission-specific recoverable Trash batch. It does not authorize emptying Trash, removing any other duplicate, deleting an archive/extracted pair, deleting a worktree, or touching an iCloud placeholder.

After the move, the retained copies will be re-hashed and this manifest will be updated. Emptying only this batch will then require a second explicit approval.
