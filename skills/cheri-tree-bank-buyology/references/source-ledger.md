# Source Ledger — Cheri Tree B.A.N.K. Buyology

Claim-by-claim provenance for this skill. Written during the Wave 3 Lane 4 repair pass
(2026-07-17) after confirming no primary source exists in the repo — see verification
note below.

## Primary source status

- **UNCONFIRMED**: The original primary source — *Why They Buy* by Cheri Tree (PDF) —
  is referenced in `references/source-notes.md` ("Source: *Why They Buy* by Cheri Tree,
  PDF supplied by Farrice Cain") but the PDF/transcript itself is **not present anywhere
  in this repository**. Verified by direct search: `find . -iname "*why they buy*"` and
  `find . -iname "*.pdf"` filtered for buy/bank/tree returned zero hits (checked
  2026-07-17). `extractions/` (top-level) has no `cheri`/`bank`/`buyology`-matching
  entry either (`ls extractions/ | grep -i cheri` → empty, 193 total entries scanned).
  Therefore **no sentence in this skill can be confirmed as Cheri Tree's own verbatim
  wording** — everything below is either (a) a real, checkable quote from this skill's
  own already-existing reference files (which are themselves AI-synthesized field
  notes, not the book), or (b) synthesized methodology built from those field notes.

## Verified-to-exist files (not verified against the original book)

| File | Git-add date | Status |
|---|---|---|
| `_active/harness/codex-harvest-2026-06-11/extractions/cheri-tree-bank-buyology/architecture.md` | 2026-06-11 | VERIFIED to exist, 771 bytes, read in full |
| `_active/harness/codex-harvest-2026-06-11/extractions/cheri-tree-bank-buyology/vision.md` | 2026-06-11 | VERIFIED to exist, 997 bytes, read in full |
| `references/source-notes.md` | 2026-07-02 | VERIFIED to exist, read in full |
| `references/bank-code-field-guide.md` | 2026-07-02 | VERIFIED to exist, read in full |
| `references/genius-patterns.md` | 2026-07-02 | VERIFIED to exist, read in full |
| `references/hidden-knowledge.md` | 2026-07-02 | VERIFIED to exist, read in full |
| `references/bank-deployment-map.md` | 2026-07-02 | VERIFIED to exist (not directly quoted in this repair) |

All dates confirmed via `git log --diff-filter=A --date=short`.

## Claim inventory (genius.md additions from this repair)

| Claim / quote used in genius.md | Label | Source |
|---|---|---|
| "the four B.A.N.K. types: Blueprint, Action, Nurturing, Knowledge" | VERIFIED (verbatim in-repo) | `references/source-notes.md` line 9 |
| "A person's full code is an ordered stack, not a single label." | VERIFIED (verbatim in-repo) | `references/bank-code-field-guide.md`, "Code Order" section |
| "If code insights stay in the seller's head, they disappear. If code is stored and routed, the whole business can send better messages." | VERIFIED (verbatim in-repo) | `references/hidden-knowledge.md`, "CRM Is Where B.A.N.K. Becomes Compounding" |
| "A pitch delivered before code diagnosis is a guess." | VERIFIED (verbatim in-repo) | `references/genius-patterns.md`, Pattern 1 |
| "The method should help the right buyer understand the right offer. It should not pressure a poor-fit buyer into a bad decision." | VERIFIED (verbatim in-repo) | `references/genius-patterns.md`, Pattern 10 |
| Blueprint/Action/Nurturing/Knowledge "Avoid" list quotes | VERIFIED (verbatim in-repo) | `references/bank-code-field-guide.md`, per-code sections |
| "Use only short calibration excerpts if needed. Most outputs should be transformed methodology, original business assets, and operational prompts." | VERIFIED (verbatim in-repo) | `references/source-notes.md` line 17 |
| Whether any of the above phrases match Cheri Tree's own book wording | UNCONFIRMED | No PDF/transcript in repo to check against |
| The B.A.N.K. framework's overall structure (4 codes, motive/values/clues/likes/avoid/triggers taxonomy) attributed to Cheri Tree | LIKELY | Consistent across `source-notes.md`, `architecture.md`, `vision.md`, and public knowledge of the *Why They Buy* framework's public description, but not independently re-verified against the book itself in this pass |

## What this ledger does NOT claim

This ledger does not assert that any quoted sentence above is Cheri Tree's original
prose. It asserts only that the quoted sentence exists verbatim in this skill's own
reference files, which is the honest, checkable claim available given the primary
source's absence from the repo.
