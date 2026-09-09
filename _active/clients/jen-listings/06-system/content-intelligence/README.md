# Jen Content Intelligence Bank

This system turns Jen's own Instagram history into a source-linked content and
story bank. It is deliberately split into a private evidence archive and a
redacted client-facing layer.

## The operating line

**Brand promise:** The whole move feels handled.

**Content proof:** You will always know what happens next.

This is not a public content franchise yet. It is the standard used to identify
and organize evidence already present in Jen's work.

## Privacy boundary

- Private archive: raw Monid responses, usernames, captions, the single comment
  canary receipt, media,
  cursors, checksums, quote receipts, cost receipts, and failure records.
- Curated bank: source-linked stories with handles, exact addresses, and client
  identifiers removed unless written permission is documented.
- Instagram remains read-only. The system does not edit, delete, message, or
  publish.

## Evidence states

- `REVIEW_REQUIRED`: the archive threshold appears met, but human evidence and
  stability review are still pending.
- `EMERGING`: repeated evidence exists, but it is not yet a validated pillar.
- `NO_EVENT`: no attributable DM, consultation, signed client, closing, or
  collected revenue has been recorded.
- Engagement metrics are attention signals, not lead or revenue proof.

## Expert composition

| Owner | Owns | Does not own |
|---|---|---|
| Kallaway | archive classification, topic and pillar evidence, format portfolio, hook architecture, testing logic | invented niches or final story prose |
| Jun Yuh | bounded story moments, source-truth packets, continuity chains, scripts and captions after review | strategy selection or unsupported outcomes |
| Alyssa | bounded real-estate platform and lead-path check | Jen's voice or story truth |
| Jen | voice, privacy, proof, fair-housing, and final publishing approval | extraction mechanics |

The handoff is sequential: Kallaway validates the content job and format; Jun
writes from the source boundary; Alyssa checks the lead path; Jen is the final
authority. No general-purpose writing council touches every asset.

## Checkpoints

1. Inventory: reconcile the live profile count, media types, and Highlights.
2. Archive: preserve accessible source media and itemize unavailable material.
3. Story Bank: rank 200 sourced moments, deep-process 50, derive evidence-backed
   pillar candidates, and produce the privacy and retrieval queues. The audience
   language bank remains coverage-labeled because comments were waived.
4. Publishing pack: begins only after Story Bank review.

## Budget and recovery

- Total Monid project ceiling: **$10.00**.
- Comment extraction was waived by the operator after one $0.003 canary; no
  further comment or reply spend is permitted for this baseline archive.
- Each paid phase writes a quote receipt before requests begin.
- Each individual request writes a pending receipt before the API call and an
  immutable raw page plus checksum after completion.
- If a call is interrupted after billing, the runner stops. It can recover the
  completed Monid run by ID without paying for the same page again.

## Operator commands

Run from the Google Antigravity repository root. The private archive defaults to
`.tmp/jen-content-intelligence` and is not part of the shared client tree.

```text
python3 execution/jen_content_archive.py inventory --max-cost 0.50
python3 execution/jen_content_archive.py highlights
python3 execution/jen_content_archive.py waive-comments
python3 execution/jen_content_archive.py media --top 200
python3 execution/jen_content_archive.py build-bank
python3 execution/jen_content_archive.py drive-export
python3 execution/jen_content_archive.py status
```

`build-bank --provisional` exists only for local QA. A provisional bank must
never be presented as a complete archive.
