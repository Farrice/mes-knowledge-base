---
description: "Deepen /library-ingest with a confidence-gated human-in-the-loop review lane — Kieran Flanagan's Recommended / Needs Review / Skipped triage: every proposed write is a typed card with a confidence badge and a target path, and the human only accepts, re-routes, or skips. Kills silent-write decay."
---

# Library Ingest Triage

Turn Simon's Extract→Atomize→Normalize ingest into a *reviewed* write. The model proposes; confidence thresholds route each proposal into a lane; the human adjudicates. Nothing is silently written, nothing is lost.

> The decay this fixes (Simon, verbatim): "the AI writes something slightly wrong, you save it back, and the next answer quietly builds on a mistake." Kieran's demo ("Cortex") solves it with a gated review lane, not blind trust.

## Pre-Flight Gate
- Load `genius.md` §Decision Framework #3-5 + §Ingest Triage.
- A KB + schema must exist (else `/library-kb-design`), and routing logic must be defined (else run `/library-ingest` step "routing logic" or the writing-logic recipe in `05-second-brain-substrate-install`). Kieran: "because it has routing logic, because in the files I tell it what to look for, and it then starts to understand where to update those different things."
- This wraps the WRITE step of `/library-ingest`; run standard chapter-map/Extract-Atomize-Normalize first to produce the atoms this triages.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md`. Load the KB's routing/writing-logic (the signals it looks for) so triage knows the valid target files and card types.

## Execution
1. **Ingest sweep**: run across connected sources — "all of those sources that you've connected, Slack, email, docs, everything" (Kieran) — and produce a proposed-write per detected item. Do NOT write yet.
2. **Type every proposal** against the routing logic. Each proposal is a TYPED card with a required metadata contract (never free text):
   - **Blocker** → owner · age · severity · next-action (verbatim demo card: "Create blocker — owner: VP Sales · age: 19d · severity: high · next: schedule async sign-off").
   - **Decision** → decision · reasoning · dependants · date.
   - **Experiment** → status · result · what-it-updates.
   - **Priority** → why-now · depends-on (named people) · suggested-action.
   Card also carries: **recommended action** (`Update existing file <path>` or `Create <type>`) with an explicit **typed-folder** target path. Decisions and blockers are FIRST-CLASS file types living in per-project typed folders (demo, verbatim): `ai-sdr/decisions/demo-ac...md`, `ai-sdr/blockers/randomisation-audit-sales-approval.md`. Routing target = `<project>/<type>/<slug>.md` — the type is a folder, not a tag.
3. **Score confidence per card** (0-100) and **gate into three lanes** (deterministic thresholds — the routing key, not decoration):
   - **Recommended** (≥85, clean single target): one-click accept. Demo badges: `HIGH · 92%`, `HIGH · 91%`.
   - **Needs Review** (55-84, or ambiguous target): human reads the target + diff before it writes.
   - **Skipped** (<55, or no clean target, or duplicate/conflict): logged to a Skipped ledger — surfaced, never lost; feeds the next health check.
4. **Present the lanes** with counts ("6 recommended · 8 gathering evidence · 3 need review"). Per card offer three controls only: **Accept** (write to target) · **Edit routing** (change type/target then write) · **Skip** (send to ledger).
5. **Write on adjudication**: accepted + re-routed cards write to their target files via the normal schema; skipped cards append to `skipped-ledger.md` with reason.
6. **Freshness pass**: mark each written source's freshness/last-seen so stale detection works later. Kieran: "This is how you keep it really current."
7. **Log**: changelog entry (counts by lane, by type) + a pickup note if the sweep was partial.

## Content Type Adaptations
| Source | Adaptation |
|---|---|
| Slack / comms | High dup rate → tighten Recommended threshold to ≥90; most chatter routes to Skipped |
| Docs / decision logs | Decision + Experiment cards dominate; capture reasoning, not just outcome (the Dalio move) |
| Meeting transcripts | Blocker + Decision cards; Confidence caps at Needs Review (unverified spoken claims) |
| Own notes (raw dump) | No connectors — triage the atoms `/library-ingest` already produced |
| Team/company KB | Add an owner field to every card; promotions route through `/library-brain-ladder`, not direct write |

## Output Requirements
The three lanes populated with typed cards (each: type, metadata contract filled, confidence %, recommended action + target path) + lane counts + written entries after adjudication + a Skipped ledger with reasons + freshness stamps + changelog entry. Deliver as a review sheet the user acts on, not a silent commit.

Execution prompt: references/prompts-v2/ingest-triage-review-lane.md — honor its Output Contract.

## Quality Gate
- Is EVERY card typed with its full metadata contract filled (blocker has owner/age/severity/next), not free text?
- Does confidence actually GATE the lane (deterministic thresholds), and does every card show its badge + target path?
- Are Skipped items logged with a reason (nothing silently dropped) and routed to the next health check?
- Did nothing write without accept/re-route? (Silent auto-write = fail — the decay `genius.md` §Anti-Patterns rejects.)
- §Rubric Ingest-trust ≥8 requires the live triage lane, not manual or blind ingest.

## Stacking
Wraps `/library-ingest` (the write gate on top of Extract→Atomize→Normalize). Feeds `/library-health-check` (Skipped ledger = raw-coverage input). In team/company KBs, promotions from a card route through `/library-brain-ladder` rather than writing straight to a higher tier.
