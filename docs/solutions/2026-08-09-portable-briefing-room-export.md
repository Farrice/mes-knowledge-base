# Solution Card — Portable Briefing Room export

**Problem:** Briefing Room artifacts were portable across Git worktrees after
the card repair, but they still assumed the recipient had the Antigravity
repository. A copied HTML file could retain absolute context links, and a copied
context pack could name files that were not present beside it.

**Decision:** Keep repository portability and external portability as separate
contracts. Repository cards use repo-relative identities. An external export is
a newly derived, self-contained bundle with bundle-relative identities,
explicit provenance, and a declared audience.

**Implementation:** `execution/brief_export.py` exports selected slugs. Private
mode includes rewritten HTML, Markdown, provenance JSON, rewritten context
packs, deduplicated safe source files, an offline index, README, SHA-256
manifest, omissions ledger, portable verifier, and optional ZIP. Share mode
uses the existing share-safe renderer and exports presentation HTML only.

**Safety:** The exporter never copies `.git`, credential-shaped files, key
material, or external absolute files. Hidden repository paths require an
explicit flag, but hard-denied material remains blocked. File and total-context
limits omit oversized sources with reasons. Existing destinations are never
overwritten.

**Proof:** `execution/verify_brief_export.py` validates a folder or ZIP without
repo imports. It checks schema, manifest coverage, bytes, SHA-256 hashes,
zip-slip safety, local HTML links, absolute-path leakage, and private context
resolution. The three-brief Jordan/GTM fixture passed as a folder, as a ZIP,
and with the copied `verify.py`; its index, all three brief pages, a context
pack, and a copied evidence source each returned HTTP 200 from a temporary
server outside the repository. Share mode passed independently with no context,
Markdown, or provenance files.

**Operating rule:** Use private mode for Farrice-owned working libraries and
share mode for outward review. A share export still needs a human prose review;
mechanical stripping is not editorial approval.
