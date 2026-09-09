---
description: Convert resolved real-estate casework into permission-safe Instagram proof stories that compound trust and create attributable qualified conversations
---

# /enrico-proof-story — Transaction → Proof Story → Qualified Conversation

Use this workflow when an agent has real client work, transaction decisions, or a resolved listing outcome that prospects normally cannot see. The job is not to make an ordinary transaction sound dramatic. The job is to expose the agent's useful judgment with inspectable proof, without inventing facts or compromising a client or live deal.

Enrico owns Instagram strategy and format fit. Marie Lee's 2026 interview supplies the additive transaction-story mechanics. Shaan Puri supplies narrative dosage only. The social-content pipeline owns production after approval. The agent, client, brokerage, and applicable law own privacy and permission.

## Usage

```text
/enrico-proof-story mine --agent "[name]" --market "[market]"
/enrico-proof-story build --case "[case receipt path]" --goal "[qualified audience action]"
/enrico-proof-story adapt --case "[case receipt path]" --formats "reel,carousel,caption"
/enrico-proof-story audit --asset "[draft path]"
```

## Required context

1. `skills/enrico-incarnati-instagram-realestate/genius.md`
2. `skills/enrico-incarnati-instagram-realestate/references/marie-lee-transaction-story-mechanics.md`
3. `skills/enrico-incarnati-instagram-realestate/references/prompts-v2/transaction-to-proof-story-pack.md`
4. `skills/shaan-puri-storytelling/references/story-deployment-map.md` for dosage
5. For Jen: `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md` and the current Jen architecture

Do not load a generic virality or copy stack before the case passes truth, permission, and proof review.

## Phase 1 — Case Receipt

One resolved case becomes one receipt. Unknown fields stay unknown.

```yaml
case_receipt:
  id: ""
  agent: ""
  market: ""
  status: "resolved | active | disputed | incomplete"
  intended_person: ""
  client_situation: ""
  stakes: ""
  obstacle: ""
  agent_diagnosis: ""
  decisions_and_actions: []
  turning_point: ""
  result: ""
  result_date: ""
  proof_objects: []
  sources: []
  client_permission: "yes | no | pending | not_required"
  brokerage_review: "pass | pending | not_required"
  disclosure_risks: []
  protected_details: []
  safe_after: ""
  claim_status: "VERIFIED | SOURCE_REPORTED | UNCONFIRMED"
```

Return `HOLD / PROOF NEEDED` when the result, chronology, permission, or central decision cannot be supported. An active or disputed matter cannot become a public victory story. It may become a non-identifying process lesson only if the disclosure owner approves it.

## Phase 2 — Competence Moment

Select the smallest moment that reveals why the result was not automatic:

- a diagnosis that changed the plan,
- a contract or negotiation detail that protected the client,
- a positioning decision that changed buyer response,
- a constraint the agent designed around,
- or a recovery after the first plan failed.

Reject generic claims such as “worked hard,” “marketed aggressively,” or “went above and beyond.” Replace them with an observable decision plus a proof object.

## Phase 3 — Narrative Dosage

Choose exactly one:

- `FULL STORY`: a real want, obstacle, change, result, and supported turn exist.
- `STORY FRAGMENT`: one useful moment is supported, but a full arc would require invention or unnecessary disclosure.
- `NO STORY`: evidence is missing, the case is active or sensitive, or a direct explainer is the more truthful form.

No story is a valid output. Route it to proof capture, a direct process explanation, or a future-safe date.

## Phase 4 — Format Router

Choose the lightest format that can carry the evidence and that the agent can produce credibly.

| Format | Use when | Native proof | Failure mode |
|---|---|---|---|
| Competence-moment Reel | One decisive moment can be told aloud in under 60 seconds | Document detail, screenshot, or resolved outcome | Overacting or generic advice |
| Single image + narrative caption | The agent writes better than they perform | Face/property image plus fact-traced caption | Dense chronology with no turn |
| Proof carousel | The case needs comparison, sequence, and multiple receipts | Before/after copy, staging, showing, offer, or timing evidence | Decorative slides with no proof |
| Bounded live-stakes series + recap | A real, time-bound challenge can be discussed safely while underway | Dated updates, field footage, recap after resolution | Exposing negotiation, client data, or an uncertain outcome |
| Direct explainer | Story dosage is `NO STORY`, but the decision teaches | Source document or process diagram | Narrative theater |

Do not let an algorithm anecdote choose the format. Agent strength, evidence density, audience need, and production capacity decide; first-party performance later refines the portfolio.

## Phase 5 — Story Spine

Build in this order, then compress for the chosen format:

1. **Specific hook:** before/after, time, or constraint; no unsupported superlative.
2. **Situation:** who needed what, with protected details removed.
3. **Obstacle:** what made the default path fail.
4. **Diagnosis:** what the agent noticed that changed the plan.
5. **Actions:** the few decisions that caused movement.
6. **Receipts:** visual or documentary proof attached to the relevant beat.
7. **Result:** verified outcome and any material caveat.
8. **Relevance:** the decision principle a similar prospect can use.

For carousels, use one idea per slide and a repeated visual anchor when that reduces production burden. For video, use a concise context line on screen and let the agent's natural delivery carry the scene. Energy can be raised for clarity; persona cannot be fabricated.

## Phase 6 — Conversion Lane

Choose one, not both:

### Trust-compounding lane

Use for evergreen proof. No forced keyword. End with a low-pressure relevance bridge or no CTA. Measure later story mentions and identifiable conversations.

### Demand-capture lane

Use only when a current property, guide, or specific next step exists and someone owns the response. State what the person receives and ask one routing question before advice or a pitch.

Map both lanes through:

```text
story exposure → identifiable two-way conversation → CRM source note → appointment → signed representation/listing → closed transaction
```

Likes, comments, reach, saves, and profile visits are attention evidence—not leads.

## Phase 7 — Production Handoff

Hand the approved packet to `00-social-content` with:

- the selected format and slide/beat plan,
- real proof objects and screenshot paths,
- the agent's voice constraints,
- prohibited details,
- claim labels,
- CTA lane and response owner,
- and an explicit ban on AI-generated transaction evidence.

Real screenshots, property media, documents, and field footage outrank synthetic visuals. Redact before production, not after publishing.

## Output contract

1. Case Receipt
2. Truth, permission, and privacy verdict
3. Competence Moment
4. Narrative dosage
5. Format decision with rejected alternatives
6. Proof Story Packet
7. Production handoff
8. Conversation and CRM attribution path
9. Attention and pipeline measurement rows
10. Evidence limits and next proof gate

## Quality Gate

- Is every material fact sourced and correctly labeled?
- Is the case resolved enough for the claimed result?
- Does the competence moment expose a concrete decision instead of effort fog?
- Does narrative dosage prevent unsupported drama?
- Does the format fit evidence density and the agent's real production strength?
- Is each result claim paired with proof or explicitly held?
- Are privacy, permission, brokerage, access, financial, negotiation, and fair-housing risks cleared?
- Does a demand-capture CTA promise something real and name a response owner?
- Are attention events excluded from the definition of a lead?
- Is performance `UNTESTED` until first-party publication and pipeline evidence exist?

## Stop conditions

Stop and name the safe continuation when the central claim cannot be verified; the matter is active, disputed, or confidential; permission is pending; the story depends on protected-class steering; proof would expose private client, access, financial, or negotiation details; the CTA has no human response owner; or the agent asks AI to manufacture a case.

Publishing, client contact, CRM writes, automation activation, and external distribution require separate authorization.

**Execution prompt:** `skills/enrico-incarnati-instagram-realestate/references/prompts-v2/transaction-to-proof-story-pack.md`
