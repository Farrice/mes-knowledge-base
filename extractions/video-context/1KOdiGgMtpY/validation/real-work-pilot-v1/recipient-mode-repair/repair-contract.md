# Signal Fidelity Recipient-Mode Repair Contract

Status: `FROZEN BEFORE REPAIR`

## Objective

Repair one presentation defect exposed by Farrice's blinded result: explicit
Signal Fidelity structure helped consequential strategy and AI-agent execution,
but native language was preferred for public content, human handoff, and burden.

## Authorized Change

Add one optional `recipient_mode` distinction to the existing SHADOW evaluator
and the same three owner pointers:

| Mode | Delivery surface |
|---|---|
| `strategy` | Explicit decision boundaries on a selected consequential decision. |
| `ai_agent` | Explicit execution capsule. |
| `human` | Native conversational artifact; Signal Fidelity stays in a cold sidecar. |
| `public_content` | Native content-owner artifact; Signal Fidelity is owner-only audit. |

Every mode remains advisory, non-blocking, non-authoring, local, reversible,
and manually selected. No mode may ask a required question or rewrite an
artifact.

## Frozen Replay

1. Strategy positive control: treatment hash
   `6175b00b95fe5c0a969781def0e24bd25e8195aa1012618e7692ce71ab07d0cb`.
2. Content failed case: preserve baseline hash
   `05d3e2e6f120c8ecc39251d86b32306f0ae6124fe5d68999f61964e5706aa3b8`.
3. Human handoff: preserve baseline hash
   `9b5d222c8fd59743e2f653b4725e9029456c0f94ebc6a35f3ef1280be78844b3`.
4. AI-agent handoff: preserve treatment hash
   `fb090d91fd3616a7894e0252c2a2315ef737c50d8b802400a822a70d70da7df3`.
5. Replay creative/manual and sparse-not-selected restraint controls.

## Pass Conditions

- The four selected visible artifacts match the frozen hashes exactly.
- Strategy and AI-agent modes expose explicit capsules.
- Human and public-content modes expose no capsule into the native artifact.
- All modes report `composition_authority: false`, `can_block: false`, and
  `enforcement: false`.
- No required questions, artifact mutations, proof upgrades, false blocks, or
  new hot surfaces appear.
- Existing Signal Fidelity verifier and recipient-mode replay both pass.

## Stop And Rollback

Stop after one implementation pass and the frozen replay. Failure parks the
branch with the defect named. Success leaves the branch unmerged for production
receipts; it does not authorize promotion, automatic activation, a command,
route, hook, skill, agent, global mirror, or enforcement. Rollback is deletion
of this repair commit because no state or migration is created.
