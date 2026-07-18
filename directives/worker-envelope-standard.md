# Worker Envelope Standard — the contract every fleet worker runs under

**Born 2026-07-18 (Wave 4, Frontier Elevation)** from the jw-engine envelope propagated
through Wave 3's repair fleets — 325 skills repaired under it (Lanes 1-4), every rule
below paid for by a caught failure. This is the STANDARD; per-mission envelopes copy it
and add mission specifics, never subtract rules. Companion failure catalog:
`docs/solutions/2026-07-17-repair-fleet-poc-three-failure-shapes.md` · runbook:
`directives/fleet-conductor-doctrine.md`.

## The six clauses every envelope MUST carry

1. **Objective, scoped.** Repair/produce ONLY what the audit/spec names. Preserve
   everything that passes. Additive-first: never delete or rewrite passing content —
   cleanup candidates are PROPOSALS to the conductor (Farrice standing rule 2026-07-17).
2. **Quarantine writes.** Exact absolute output dir, stated twice ("this exact repo
   path — not your scratchpad"). Deliver full modified copies mirroring the target
   layout. NEVER write inside the protected tree (shape 2: path drift; a sentinel +
   write-guard hook backs this physically when the target is `skills/`).
3. **Git read-only.** `status/diff/log/show` allowed; add/commit/merge/push/checkout/
   restore are CONDUCTOR-ONLY. Ignore SessionStart divergence alarms — they address the
   conductor (shape 4: workers slicing main's history).
4. **Provenance or UNCONFIRMED — the one unforgivable failure is invented provenance.**
   Every anchor cites file + location in PROVENANCE.md. A quote you cannot find gets
   UNCONFIRMED, never an anchor. **THREE-LOCATION RULE** (2026-07-18, fired both
   directions the same day): an absence claim ("no source exists") must name searches of
   ALL THREE source locations — root `extractions/`, the claude-export archive tarball
   (python tarfile per-member CONTENT scan — filenames are UUIDs), and
   `_active/codex-harvest-2026-06-11/extractions/` — fewer searched = the claim is
   unverified. "Scan not needed" is itself an absence claim. Search name FRAGMENTS
   without apostrophes/punctuation; record sizes with `wc -c` (never `wc -l`).
5. **Deliverable paths, not self-report.** End by reporting the file count, the output
   dir, and proof the protected tree is untouched (`git status --porcelain <target>`
   must be empty). The return message is a ROUTING HINT; the conductor's gate decides
   (shape 5: hollow delivery — paperwork without payload never merges).
6. **Adversarial audit notice.** State that a verifier will open cited files, check
   quotes byte-exact, AND spot-check UNCONFIRMED/absence claims (lazy-UNCONFIRMED =
   false absence). Workers who know negatives get audited stop guessing.

## Per-stage model tier (advisory — Farrice's token discipline made deterministic)

| Stage kind | Tier | Rationale |
|---|---|---|
| judgment (verdicts, merges, violation fixes, calibration) | highest available (Fable → Opus) | Conductor Ladder; never Sonnet |
| execution (repairs, ports, builds, research reads) | inherit session model (Sonnet default) | volume work; envelope + gate carry the quality |
| mechanical (renames, audits, staging, sed/copy) | cheapest (Haiku/scripts) | deterministic where possible — push into Python, not prompts |

Never pin Opus (opus-fallback-policy): degrade a tier rather than stall.

## Envelope lifecycle

- Canonical current envelope lives with the batch (`.tmp/<mission>/ENVELOPE.md`); new
  batches `sed` the prior one — rules ratchet forward, never relax.
- A rule earns its place by naming the failure it prevents (date + incident). A rule
  that can't name one is a candidate for the conductor to cut — workers never cut.
- Dispatch prompt = 3-6 sentences: envelope path, assignment ID, audit/spec file, exact
  output dir, mission-specific cautions (sibling skills, domain risks like fake study
  citations), and the ≤120-word return format.
