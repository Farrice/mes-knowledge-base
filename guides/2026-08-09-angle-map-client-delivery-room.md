---
date: 2026-08-09
session: angle-map-client-delivery-room
tier: operator-guide
status: enriched
---

# Client: Angle Map Delivery Room - V1 Sealed and Parked — What We Built 2026-08-09 and How to Use It

> This session turned the portable Briefing Room into a governed client-delivery system for The Angle Map plus Message-Market-Fit Intelligence. It now has a guarded intake, an evidence ledger, separate private and client rooms, a human release gate, portable ZIP verification, and a founding proof fixture. Start with `.agent/workflows/client-delivery-room.md`; the behavior contract lives in `semantic_libraries/antigravity/primitives/client-delivery-room-contract.md`; the complete non-confidential example lives under `deliverables/client-rooms/angle-map-message-market-fit-v1/`.

## ⚡ If you only read 10 lines

- The operating rule is **private truth first, client edition second**.
- Start a new engagement with `client_delivery_room.py init`; new projects begin on HOLD.
- Complete intake and handling permissions before loading confidential material.
- Inventory every source as FACT, QUOTE, CLAIM, INFERENCE, or UNKNOWN, with CLIENT_SAFE or INTERNAL_ONLY visibility.
- Build the private working room before trying to produce a client deliverable.
- The working room holds the Customer Truth Dossier, Problem-Qualified Segment, three angles, one message-market-fit test, conflicts, and unknowns.
- The client room is derived from reviewed evidence; it is not the private room with a few paragraphs deleted.
- Client export requires editorial, evidence, privacy, brand, and link PASS plus explicit permission to share.
- `verify` checks hashes, local links, and portable paths; the client build also rejects internal terminology and absolute local paths.
- V1 proves fulfillment reliability, not demand. Keep expansion parked until three real client deliveries expose recurring friction.

## Command table

| Command | What it produces | Reach for it when |
|---|---|---|
| `python3 execution/client_delivery_room.py init --project-dir <path> --client "<name>"` | A guarded project scaffold with intake, evidence inventory, release gate, and two brief shells | A new Angle Map client engagement begins |
| `python3 execution/client_delivery_room.py check <project-dir>` | Working-room readiness with exact unresolved fields | You want to know whether analysis can begin safely |
| `python3 execution/client_delivery_room.py check <project-dir> --release` | Client-export readiness | The client copy has been reviewed and permission may be complete |
| `python3 execution/client_delivery_room.py build <project-dir> --output <new-dir> --working-only` | Verified private folder and ZIP | Strategy work is ready but the client release gate is not |
| `python3 execution/client_delivery_room.py build <project-dir> --output <new-dir>` | Verified private and client folders plus both ZIPs and a release receipt | All release reviews and permission fields pass |
| `python3 execution/client_delivery_room.py verify <release-dir>` | Re-verification against the signed release receipt | Before handoff or after moving a release |
| `python3 execution/verify_client_delivery_room.py` | Cold-start proof plus deliberate leak rejection | After changing the workflow or exporter |
| `python3 execution/verify_brief_export.py <bundle-or-zip>` | Portable manifest, hash, link, and path verification | Before sending any portable room |
| `python3 execution/worktree_lane.py merge --lane codex/portable-brief-export` | Guarded integration into main, or a safe parked result | The current main writer has finished and main is clean |

## The mental model

### One truth record, two audiences

The private room is the canonical reasoning surface. It can contain incomplete evidence, contradictions, internal terminology, provisional segment logic, and the real reason one angle outranks another. The client room is a decision surface derived from that record after review. This prevents two common failures: cleaning the private file until it is no longer useful, or manually copying the work into a second document that quietly drifts.

### Readiness and proof are separate

Passing the builder means the delivery mechanics are reliable. It does not mean the market wants the offer or that the message has achieved fit. The founding fixture records The Angle Map honestly: the offer and local sources exist, but customer exposure, held attention, sales, and collected revenue remain NO EVENT. That distinction must survive every future client room.

### Release is a human decision with machine enforcement

The system can detect missing fields, bad paths, broken links, stale hashes, placeholders, and internal-language leaks. It cannot decide whether a strategic interpretation is tasteful, whether a client has approved a claim, or whether permission was genuinely granted. Those remain named human reviews. The machine makes the decision explicit and prevents an unreviewed artifact from masquerading as final.

## Capability 1: Guarded intake and source inventory

### What it is

`init` creates one project container with `intake.json`, `source-inventory.json`, `release-gate.json`, two brief JSON shells, and a human-readable intake form. Confidential projects start on HOLD. The source inventory forces evidence type, visibility, permission, location, and limitation states before the work can be treated as grounded.

### When to reach for it

Use it when a client has a live messaging decision, a real deadline, permitted source material, and a named decision maker. It is especially useful when uploads include mixed truth quality: research, founder claims, customer language, internal hypotheses, and assets that should not all appear in the client edition.

### When NOT to

Do not use the full workflow for a casual copy edit or a single headline with no research requirement. Use the ordinary content/copy route and its normal evidence checks. Do not place confidential files into the project until the handling fields are complete.

### Worked example

The founding project at `deliverables/client-rooms/angle-map-message-market-fit-v1/` uses NON_CONFIDENTIAL_DEMO mode. Its evidence ledger preserves the difference between verified offer facts, local strategic material, inferences, and unknown demand. That allows the system to prove delivery behavior without pretending a live client approved anything.

### Honest edges

The confidential handling path has not been exercised with a real client. Transfer channel, access list, NDA, retention, deletion, reuse, and AI permission are therefore a hard activation checklist, not ceremonial metadata.

## Capability 2: Private Customer Truth and Angle Map room

### What it is

The private brief holds source coverage, Customer Truth Dossier, Problem-Qualified Segment, three angles, one message-market-fit test, and the unknown/release boundary. The required heading signals ensure these components cannot silently disappear during drafting.

### When to reach for it

Build this once the intake and source inventory pass. Use `--working-only` when strategic work is useful but outward prose, permissions, or final review are unfinished.

### When NOT to

Do not wait for perfect evidence before building the private room. Unknowns belong there. The cheaper alternative is to label an inference or unknown correctly, not to stall or fill the gap with plausible fiction.

### Honest edges

The builder validates structure and evidence state, not whether the strategic judgment is brilliant. Jordan Crawford's workflow remains the reasoning layer; Farrice's verdict remains the taste and business gate.

## Capability 3: Share-safe client decision room

### What it is

The outward edition uses the same Premium Minimal visual system as the main Briefing Room while removing private context. The release scan blocks placeholders, absolute local paths, repository language, and internal terms such as Antigravity, God Agent, Codex, Claude Code, worktree, and PRIVATE_CONTEXT.

### When to reach for it

Produce it after the client-facing recommendation, evidence boundary, and test plan have been reviewed. The final ZIP is the thing to send; the private ZIP is never a client handoff.

### When NOT to

Do not export because the room looks polished. If any release review is HOLD, keep the private edition and stop. Visual readiness is not permission.

### Worked example

The sealed release under `/Users/farricecain/.codex/visualizations/2026/08/09/019fe785-b6d0-7863-8011-29f18a392714/Angle-Map-Client-Delivery-Room-V1-Sealed-2026-08-09/` contains the final client room, private room, both ZIPs, and `release-receipt.json`. A deliberate internal-note injection was rejected in the cold-start proof.

### Honest edges

This is an offline portable deliverable, not a hosted client portal. Hosting, white-label automation, connectors, and live collaboration are intentionally parked until usage proves the need.

## Capability 4: Portable verification and signed release

### What it is

Every export contains a manifest of packaged files and hashes. Verification confirms that local links resolve, portable context paths stay inside the bundle, ZIP contents match the manifest, and the final ZIP hash matches the release receipt. Private curated roots now receive the same provenance handling as share roots without being mislabeled as repository paths.

### When to reach for it

Run verification after moving a folder, before attaching a ZIP, and after any exporter or template change. Use the cold-start verifier after code changes because it proves both the happy path and a blocked leak.

### When NOT to

Do not substitute checksum success for editorial review. Hashes prove the artifact did not change; they do not prove the recommendation is right.

### Honest edges

The broad Operator Core verifier reported a lane-specific hook-parity warning, and the optional Notion regression check was unavailable in the restricted network. Neither affects offline bundle integrity. Keep those as separate system work unless Farrice explicitly opens that scope.

## Composition options

| Stack with | When it earns its cost | What it contributes |
|---|---|---|
| `jordan-crawford-gtm-intelligence` | The message or target is genuinely uncertain | Customer Truth Dossier, PQS, and evidence-first message test logic |
| `/briefs` | The output must be reusable or client-facing | Premium Minimal visual rendering and portable delivery |
| `source-to-skill-system` | Repeated client use reveals a real architectural gap | Controlled workflow evolution without creating a duplicate mega-skill |
| `/end-session` | The engagement crosses sessions or worktrees | Exact, verified handoff identity and a retrieval-safe continuation |

## Parked state and resumption

The implementation is committed on `codex/portable-brief-export` at `f0ea0a90e91adc5a2bdfe9bf576078cb24e2ffbf`. The guarded merge parked because another session owns a dirty main tree. Do not force it. When main becomes clean, run the exact lane merge command in the table. Expansion stays parked; the next genuine product-learning event is the first authorized client delivery, not another architecture pass.
