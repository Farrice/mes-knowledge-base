# Signal Fidelity Companion Contract

Status: `SHADOW`. This is a cold advisory primitive, not a command, router, skill, agent, hook, score, schema requirement, or blocking gate.

## Purpose

Use this primitive selectively to reveal whether human-owned meaning survives a material AI transformation or handoff. It protects the recipient, intended change, source of conviction, must-survive details, promise, limit, proof state, and human owner without freezing the first idea or slowing clear work.

The target behavior is narrow:

> Compare what an unfamiliar recipient recovered with what the human owner meant, then expose material differences for review.

Signal Fidelity does not decide what is worth building, whether a claim is true, whether work has taste, whether a market will care, or whether trust has been earned.

## Source Boundary

The primary source is Lena Hall's talk, **The Signal Layer: What to Build When Anything Can Be Built**:

- YouTube: `https://www.youtube.com/watch?v=1KOdiGgMtpY`
- Evidence package: `extractions/video-context/1KOdiGgMtpY/`
- Build contract: `extractions/video-context/1KOdiGgMtpY/signal-fidelity-build-contract.md`

The source supplies the convergence-machine diagnosis, three distortion boundaries, promise-and-scope welding, thin-layer constraint, and recipient playback test. The structured Signal Contract and Antigravity owner mapping are implementation inferences, not Lena Hall's named framework.

## Relationship To Existing Owners

Signal Fidelity starts after existing intent work, not instead of it.

- Nate B. Jones Intent Engineering and the Co-Creative Launchpad clarify latent intent before execution.
- Skill System owns compact propagation across component boundaries.
- Agentic Engineering owns outcome ownership, review, explanation, and recovery.
- Proof and claim gates determine whether evidence and public claims are supportable.
- The human owner may revise the original intent deliberately.

This companion owns none of those decisions. Its only contribution is a post-transformation comparison surface.

## Eligibility

The current prototype has no automatic activation. A human or existing owner may choose to run it when at least one condition is present:

1. A source-derived idea crosses two or more transformations or handoffs.
2. Public, client-facing, money-adjacent, or consequential work could detach a promise from its limit or evidence.
3. Taste-bearing work introduces personal conviction, voice, or lived experience that the human owner may need to confirm.
4. Delegated work can satisfy the literal specification while losing the personally owned, unaverageable detail.
5. A cold recipient's interpretation materially determines whether the artifact works.

Skip tiny, mechanical, private, obvious, or single-step work. Never ask extra questions merely to populate this contract.

## Optional Signal Contract

The compact human-owned object is:

| Field | Meaning |
|---|---|
| `recipient` | The person or agent whose understanding matters. |
| `intended_change` | What should become different for that recipient. |
| `source_of_conviction` | Lived proximity, evidence, relationship context, or future-facing judgment behind the choice. |
| `promise` | What the work offers. |
| `limit` | What must not be implied, removed, or broadened. |
| `proof_state` | Current evidence state such as `VERIFIED`, `LIKELY`, `UNCONFIRMED`, `UNTESTED`, or `NO EVENT`. |
| `human_owner` | The person allowed to approve a deliberate change. |
| `source_path` | The exact evidence or intent source when available. |
| `must_survive` | A small list of named meanings plus observable markers and the surfaces where each should remain detectable. |

A useful checksum is:

> For **[recipient]**, create **[intended change]** because **[source of conviction]**, preserving **[must-survive detail]**, while never implying **[limit]**.

Do not require this packet on ordinary work. If existing Launchpad or handoff fields already contain the same information, reuse them rather than creating a duplicate form.

## Three Distortion Checks

### Source Distortion

Question: did the originator compress familiar context past legibility, or did AI fill an unstated gap with a common assumption?

Evidence may include a missing recipient, intended change, source of conviction, promise, limit, proof state, source, or human owner. Missing fields are an incomplete signal hypothesis, not proof that the operator lacks judgment.

### Handoff Distortion

Question: did the next contributor receive the task while losing why it matters, the personally owned detail, the decision boundary, or the open risk?

Evidence may include must-survive markers present in the contract but absent from the transformed artifact. A marker miss is a review cue, not semantic certainty.

### Machine Distortion

Question: did formatting, summarizing, optimizing, or remixing retain the attractive promise while dropping its limit, changing the proof state, or broadening the scope?

Proof-state changes require human review unless the packet records an owner-approved change. The evaluator never upgrades evidence.

## Recipient Playback

Give the transformed artifact to an unfamiliar recipient and ask them to describe:

1. who it is for;
2. what should change;
3. why the creator believes it;
4. what unusually important detail must remain;
5. what the promise does not include.

Compare that playback with the Signal Contract. The deterministic prototype can check supplied markers; it cannot establish semantic equivalence. A human owner decides whether the gap is material, acceptable, or a useful evolution.

## Deliberate Evolution

Fidelity does not mean preserving a weak first articulation forever.

- Record owner-approved changes by must-survive item id or field name.
- Preserve the reason for the change and the new limit.
- Treat approved changes as reviewable adaptations, not automatic distortion.
- Re-run playback when the recipient, promise, limit, or proof state materially changes.

## Owner Integrations

1. **Co-Creative Launchpad owns capture.** It may reuse existing center, edges, success, constraints, proof, and handoff fields to form a compact checksum.
2. **Skill System owns propagation.** It may pass the checksum, must-survive details, proof state, human owner, source path, and open risk across selected component handoffs.
3. **Agentic Engineering owns playback and review.** It may compare a cold recipient's supplied playback with the contract and return the delta to the outcome owner.

No integration transfers authority to this primitive.

## Context Policy

- **Hot only on a selected run:** checksum, promise plus limit, must-survive items, proof state, human owner, source path, and open risk.
- **On demand:** source evidence, approved-change rationale, and detailed playback.
- **Cold:** transcript, full history, adjacent expert systems, and previous artifacts.

Do not use a context dump as a substitute for a precise signal.

## Manual Prototype

The optional stdlib-only evaluator is:

```bash
python3 execution/signal_fidelity_shadow.py execution/fixtures/signal-fidelity-shadow/preserved.json --format plain
```

It reads one local packet, writes no state, makes no network or model call, and returns advisory evidence. Valid packets always exit successfully even when review is recommended. Invalid JSON or malformed packet structure may return a usage error because no evaluation occurred.

## SHADOW Rules

This companion may recommend or explain. It may not:

1. block, delay, reject, or mutate work;
2. add mandatory questions, fields, scores, or readiness thresholds;
3. auto-activate, route, log, publish, message, or write state;
4. create a command, skill, agent, router entry, hook, automation, plugin, or global mirror;
5. override factual, proof, privacy, safety, cost, destructive-action, or permission vetoes;
6. treat marker absence as confirmed semantic loss;
7. treat accurate playback as proof of truth, taste, trust, adoption, or commercial value;
8. prevent the human owner from approving a better evolved signal;
9. claim deployment success from files, fixtures, or verifier output.

## Promotion And Removal

Promotion requires three independent production receipts across different task types, blinded recipient comparison, zero false blocks on frozen safe controls, no added question burden for clear tasks, preserved creative range, explicit burden evidence, and Farrice's approval.

Keep it cold or remove it if existing owner fields produce the same behavior, warnings are mostly false positives, clear tasks become slower, creative adaptation narrows, or recipients show no material comprehension improvement.

Rollback is additive: remove the primitive, evaluator, fixtures, verifier, source package, and three owner pointers. There is no state or migration to undo.

## Proof State

Structural prototype: `SHADOW`.

Production behavior, recipient comprehension improvement, workflow burden, and trust effect: `UNTESTED`.
