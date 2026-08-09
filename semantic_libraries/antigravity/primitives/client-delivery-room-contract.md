# Client Delivery Room Contract

## Purpose

Use this primitive when a client supplies an intake, files, links, and a live
decision that must become both a private working record and a polished,
share-safe client handoff.

The room is not a document reskin. It is a controlled transformation from
production truth to client clarity.

## V1 Scope

The first supported engagement is:

> The Angle Map + Message-Market-Fit Intelligence for one established
> supplement, functional-nutrition, recovery, or performance brand; one live
> occasion; one buyer; one message decision; one final decision-maker; and one
> deadline.

The client receives a decision room, evidence boundary, three campaign angles,
one lead-angle recommendation, and one bounded message-market-fit test. The
private working room retains the Customer Truth Dossier, Problem-Qualified
Segment reasoning, conflicts, unknowns, source inventory, and internal notes.

## Source Evidence

- Current user decision: Angle Map + message-market-fit; form, uploads, and
  kickoff; decision room, evidence, and action plan.
- `_active/linkedin/02-offer/ANGLE-MAP-ACTIVATION-PACKET.md`
- `_active/linkedin/02-offer/ANGLE-MAP-CONFIDENTIAL-INPUT-PROCEDURE.md`
- `skills/jordan-crawford-gtm-intelligence/`
- `execution/render_brief.py`
- `execution/brief_export.py`
- `execution/verify_brief_export.py`
- `_active/farrice-brand/premium-minimal/`

## Skill System Contract

| Field | V1 Contract |
|---|---|
| Objective | Turn one permissioned intake and source pack into a verified private working room and a separate Premium Minimal client ZIP without inventing missing evidence. |
| Components | `/client-delivery-room`, Jordan Crawford dossier/PQS/MMF workflows, Angle Map offer boundary, `render_brief.py`, `brief_export.py`, portable verifier, intake template, release gate. |
| Step order | initialize -> intake/uploads -> readiness check -> kickoff -> evidence ledger -> PQS -> three angles -> MMF charter -> private room -> editorial/privacy firewall -> client room -> verified ZIP -> learning return. |
| Inputs | Client identity, live occasion, one message decision, buyer, decision-maker, deadline, current message, approved evidence, claim boundaries, brand assets, handling permissions, source inventory. |
| Outputs | Private working room, client room, two ZIPs, release receipt, proof-state and unknown ledger. |
| Handoff summary | Pass evidence row IDs, decision, PQS status, three angle cards, lead recommendation, proof boundaries, permission state, and exact source paths. Do not pass the whole raw context to the client edition. |
| Composition rule | Client Delivery Room owns integration. Jordan owns upstream evidence and qualification. Angle Map owns scope. Premium Minimal owns presentation. The release gate owns outward safety. |
| Human checkpoint | A named person must approve evidence, privacy, prose, brand, links, and permission to share. Implementation approval does not substitute for per-client release approval. |
| Validation | Project check, client-language scan, portable bundle verifier on folders and ZIPs, unit tests, cold-start fixture, prose classifier, export-format guard. |
| Behavior-changing proof | The committed Angle Map founding fixture must build both rooms from a cold start, reject an intentional client leak, and verify both ZIPs. |
| Result surface | Offline branded HTML room plus ZIP; private Markdown/JSON/context remain available to the operator. |
| Context policy | Intake, source inventory, evidence ledger, and internal brief stay private. Client HTML receives only curated conclusions and public/approved citations. |
| Reuse hook | Use the same workflow for the next three Angle Map engagements. Generalize to other offers only after three delivery receipts reveal what actually repeats. |

## Agentic Engineering Packet

| Field | V1 Decision |
|---|---|
| Objective | One safe front door that builds and verifies both editions. |
| Source truth | Exact local contracts, project JSON, brief JSON, source inventory, generated manifests, and verifier output. |
| Context plan | Load the project manifest and selected evidence only; keep raw uploads cold and path-addressable. Never load every client file by default. |
| Work chunks | Contract and intake; validator; renderer/export bridge; fixture; regression tests; release receipt. |
| Review loop | Maximum two repair passes. Stop when unit tests, cold-start verification, privacy scan, prose check, export guard, and both ZIP verifiers pass. |
| Dependency gate | Standard library and existing repository modules only. No new package, hosted service, connector, or paid tool. |
| Structure pass | One owner script, one workflow, one primitive, one template, one thin command bridge. No duplicate renderer or brand tokens. |
| Use-now artifact | The Angle Map founding client room and verified ZIP. |
| Hardening proof | A clean build plus a deliberate leak fixture that is refused before export. |

## Intake Readiness

The working room may start only when these are literal, not placeholders:

1. One live occasion and deadline.
2. One message decision.
3. One named buyer and final decision-maker.
4. Current message or campaign material.
5. Approved evidence and claim boundaries, or an explicit `UNKNOWN`.
6. A source inventory with permission and visibility for every item.
7. A handling state of `NON_CONFIDENTIAL_DEMO`, `HUMAN_ONLY`, or
   `AI_ASSISTED_APPROVED`.

For real confidential work, the transfer channel, authorized access, working
location, NDA state, retention, deletion path, and AI permission must be
literal and tested. `HOLD` keeps the project at `HOLD`.

## Release Gate

The client ZIP is blocked unless all are true:

- editorial review `PASS`
- evidence review `PASS`
- privacy review `PASS`
- brand review `PASS`
- link review `PASS`
- permission to share `YES`
- reviewer name and timestamp present
- no placeholder, absolute path, file URI, repository path, internal framework
  name, or forbidden term appears in the client brief
- every local link and bundle hash verifies

The gate proves release hygiene. It does not prove the strategic conclusion,
customer demand, market fit, or business outcome.

## Required Private Room

- source coverage and permission state
- atomic evidence ledger: `FACT`, `QUOTE`, `CLAIM`, `INFERENCE`, `UNKNOWN`
- conflicts and counterexamples
- provisional Customer Truth Dossier
- Problem-Qualified Segment verdict
- three campaign-angle cards and lead recommendation
- message-market-fit test charter and counters
- unknowns and next research action
- release gate state

## Required Client Room

- executive decision
- what was reviewed
- what the evidence supports
- the problem-qualified buyer situation, with proof state visible
- three campaign angles
- one lead recommendation
- prioritized action plan
- one bounded message-market-fit test
- evidence and claim boundary
- next decision and revision instructions

## Stop Conditions

- Required source or permission is missing.
- Public traces are being promoted into customer truth.
- A provisional PQS is labeled qualified.
- The client prose exposes internal tools, paths, experts, prompts, branches, or
  working disagreements.
- A release review is `HOLD`, `FAIL`, missing, or unsigned.
- A folder or ZIP fails portability or hash verification.
- A real client transfer method remains untested.

## Proof States

Keep `VERIFIED`, `LIKELY`, `PROVISIONAL`, `UNKNOWN`, `UNTESTED`, `NO EVENT`,
and `NO PERMISSION` separate. A polished room cannot promote the underlying
evidence state.
