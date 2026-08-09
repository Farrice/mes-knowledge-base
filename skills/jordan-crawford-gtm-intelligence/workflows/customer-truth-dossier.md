---
name: "Customer Truth Dossier"
produces: "Provenance-safe dossier separating actions, verbatim voice, CRM claims, inference, conflicts, and unknowns"
expert: "Jordan Crawford — Evidence-First GTM Intelligence"
load_context: "genius.md"
tier: 1
---

# Customer Truth Dossier

## Pre-Flight Gate

Require at least one real source or route to `zero-data-discovery`. Confirm permission to use private records. Read `genius.md` and `references/research-tool-contract.md`. Never merge contradictory rows into a synthetic average.

## Skill Acquisition

Load `references/genius-patterns.md` cards 2, 14, and 15 plus the source ledger. Use the trust default `ACTION > QUOTE > CLAIM`; overturn it only with a specific receipt.

## Input Required

- Customer/product actions with source and date
- Verbatim calls, emails, tickets, reviews, or interviews
- CRM/operator claims
- Product and commercial context
- Privacy, retention, and output constraints

## Execution

1. Inventory sources; record coverage, date, owner, reliability limits, direct/indirect type, and permission state. For external research, partition private context and attach a Research Receipt.
2. Normalize atomic evidence rows as `FACT`, `QUOTE`, `CLAIM`, `INFERENCE`, or `UNKNOWN`.
3. Link rows to problem, trigger, failed alternative, consequence, desired outcome, and buying context without forcing every field.
4. Preserve conflicts and edge cases in a dissent ledger.
5. Rank recurring problem clusters by behavioral evidence first, voice second, operator claim third. Apply the three-source customer-pattern floor; otherwise label the cluster `MODELED` or `PROVISIONAL`.
6. Write a provisional dossier narrative that cites row IDs; keep it separate from the evidence table.
7. Name missing evidence and the smallest next research action.

## Content Type Adaptations

| Context | Adaptation |
|---|---|
| B2B SaaS | Product events, calls, support, renewal/churn, CRM |
| Service business | Calls, proposals, delivery notes, objections, referrals |
| Consumer | Purchase/repeat/return behavior, reviews, support, usage |
| Single prospect | Prospect dossier; do not generalize to a market |

## Output Requirements

Dossier with source inventory, atomic evidence table, problem clusters, conflict ledger, provisional interpretation, unknowns, and next research action. Use `references/prompts-v2/customer-truth-dossier.md`.

## Quality Gate

- Every material statement traces to row IDs.
- Quotes remain verbatim; inference never appears as fact.
- At least one dissent/edge-case section exists, even if `NONE FOUND` with coverage stated.
- Private data handling and permission state are explicit.
- External research has a receipt; failed/blocked retrieval is `NO RESEARCH EVENT`.
- Every recurring customer pattern meets the source floor or is visibly provisional.
- Output does not claim market fit or demand.
