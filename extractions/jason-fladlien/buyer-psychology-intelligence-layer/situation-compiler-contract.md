# Sales Psychology Situation Compiler

**Status:** cold development compiler
**Runtime authority:** unchanged
**Executable:** `execution/jason_buyer_psychology_situation_compiler.py`

## Purpose

The compiler converts an explicit Buyer Reality Ledger into one bounded psychology decision receipt. It does not infer a person's psychology from free text and it does not write the final copy, offer, sales response, or onboarding experience.

Its job is to enforce the operating sequence:

> reality -> truth and safety -> earliest material decision -> one mechanism -> countercondition -> smallest intervention -> native owner -> receipt

## Input Contract

The compiler accepts a JSON object with:

| Field | Requirement |
|---|---|
| `case_id` | Unique fixture or receipt identifier. |
| `artifact_class` | Audience-facing class or a declared abstention class such as `technical-specification` or `evidence-ledger`. |
| `receiver_outcome` | The explicit human outcome: understand, remember, evaluate, choose, adopt, act, continue, or none. |
| `material_decision` | Boolean stating whether a material decision can change. |
| `persuasion_permitted` | Required strict boolean; `true` is explicit authorization to evaluate the bounded layer and `false` prevents intervention. An explicit qualified handoff or do-not-advance route may still return first because neither performs persuasion. Omission and strings such as `"false"` are malformed and fail closed. |
| `risk_domain` | Required closed enum: `STANDARD` or `HIGH_STAKES`. `HIGH_STAKES` prevents a psychology intervention even when permission is true. |
| `buyer_evidence` | `OBSERVED`, `SUPPORTED`, or `UNKNOWN`. |
| `requires_buyer_interpretation` | Strict boolean stating whether the proposed diagnosis depends on a buyer belief, feeling, identity, motive, or behavior interpretation. |
| `truth_gaps` | Explicit unresolved gaps such as `missing-proof`, `broken-offer`, `unclear-terms`, or `delivery-failure`. |
| `unsafe_requests` | Any requested manipulation, concealment, diagnosis, fabricated proof, false scarcity, pressure, or permission violation. |
| `observed_friction_codes` | Observable registry signals, never inferred personality labels. |
| `support_friction_code` | Optional separate weak link at a different journey stage. |
| `native_owner` | The function owner for the specific artifact or interaction when it differs from the card default. |
| `preservation_locks` | One or more unique, nonblank facts, terms, proof states, options, voice constraints, or permission boundaries the intervention must preserve. |

The caller, not the compiler, is responsible for grounding the ledger in actual facts, buyer language, behavior, terms, proof, constraints, and unknowns.

`persuasion_permitted`, `risk_domain`, `requires_buyer_interpretation`, `truth_gaps`, `unsafe_requests`, and `observed_friction_codes` are required even when their value is `false` or an empty list. Omission is malformed input; absence may not silently mean permission or no risk.

## Truth-First Precedence

The compiler evaluates these boundaries before selecting a card:

1. **Unsafe request:** return `REJECT_UNSAFE`.
2. **Explicit do-not-advance condition:** return `DO_NOT_ADVANCE`.
3. **Explicit qualified handoff:** return `HAND_OFF` without performing persuasion.
4. **Neutral, mechanical, evidence-led, high-stakes, or permission-excluded work:** return `ABSTAIN`.
5. **No material human decision:** return `ABSTAIN`.
6. **Unsupported claim or missing proof:** return `GET_PROOF`.
7. **Broken offer, poor fit, or undefined delivery capacity:** return `FIX_OFFER`.
8. **Unclear or hidden terms or disclosure:** return `CLARIFY_TERMS`.
9. **Actual performance or delivery failure:** return `IMPROVE_DELIVERY`.
10. **Buyer interpretation without buyer evidence:** return `GET_BUYER_EVIDENCE`.
11. **No registered observed friction:** return `ABSTAIN`.
12. **Eligible friction:** select the earliest material registered journey stage.

This precedence prevents Evidence from laundering a false claim, Value from disguising a weak offer, Choice from hiding terms, Action from pressuring poor fit, or Experience from reframing delivery failure.

## Selection Contract

- Exactly one primary card is permitted for `INTERVENE`.
- At most one support card is permitted.
- A support card must own a different decision and journey stage.
- Only the selected card, optional support card, and their source slices may load.
- The compiler returns a change brief to the native owner; `compilerAuthoredFinal` must remain `false`.
- Buyer evidence is trimmed and normalized only within the closed `OBSERVED`, `SUPPORTED`, or `UNKNOWN` enum; any other value is malformed input and fails closed.
- Artifact class, receiver outcome, truth-gap codes, and friction codes are trimmed and case-normalized before closed-boundary checks, so whitespace or casing cannot bypass abstention or repair.
- Truth gaps use a closed enum. An unrecognized explicit gap is malformed and fails closed; it cannot be ignored while psychology proceeds.
- Permission, interpretation, and handoff flags accept booleans only; truthy strings do not grant authority.
- Preservation locks must be unique nonblank strings. Empty, blank, or duplicate locks return no intervention.
- Each decision has an explicit native-owner allowlist. An arbitrary expert, Jason, or the compiler itself cannot be injected as the execution owner; an invalid owner returns `HAND_OFF`.
- A support card must also admit the primary card's selected owner. Cross-owner support is rejected and left to the proper route rather than smuggled into the primary receipt.
- Every registry default owner must itself be allowed; omitting an override therefore preserves the card's declared handoff rather than silently failing.
- The five candidate cards are selectable only with `--development`.
- Outside development mode, a candidate signal returns `HAND_OFF` and does not activate the candidate.

The deterministic order is not a claim that human decisions always occur linearly. It is a safe tie-breaker for a structured ledger containing several observed frictions. The native owner may reject the selection after running its countercondition.

## Output Receipt

Every output includes:

- mode and promotion eligibility;
- runtime mode and market-event state;
- decision route, primary card, and optional support;
- native owner and `compilerAuthoredFinal: false`;
- loaded cards and source slices;
- smallest intervention and risk veto;
- countercondition state and preservation status;
- current evidence and outcome class; and
- remaining proof gap.

Development outputs are `STRUCTURALLY_VALIDATED` and `CRAFT_PREFERENCE_ONLY`. They cannot be upgraded to human preference, behavior, sold, collected, retained, conversion, or causality without the separately qualified event.

## Invocation

```bash
python3 execution/jason_buyer_psychology_situation_compiler.py \
  --input path/to/buyer-reality-ledger.json \
  --pretty
```

Use `--development` only for the tunable development corpus. It does not admit candidates into runtime.

## Context Policy

Hot context remains the existing SHADOW pointer only. This compiler, the registry, candidates, research, and fixtures stay cold. A run loads the registry mechanically and reports only the selected card paths. It never loads the 38-workflow Jason package, all 33 prompts-v2, all source transcripts, or a broad expert stack.

Non-development execution is bound to the canonical registry path and its frozen SHA-256 trust anchor. A custom registry is rejected outside explicit development mode; inside development it is labeled `DEVELOPMENT_UNTRUSTED_REGISTRY` and cannot claim runtime authority. Registry statuses are a closed enum (`SHADOW`, `CANDIDATE`), and countercondition evidence must be a nonblank string rather than a stringified object.

## Failure and Rollback

Fail closed if the ledger is malformed, the buyer-evidence enum is invalid, preservation locks are blank or duplicated, the native owner is not allowed for the selected decision, activation codes collide, truth or safety precedence is bypassed, more than one support appears, the compiler authors final craft, an unselected card loads, a candidate activates outside development, or any evidence class is inflated.

Rollback is local and reversible: remove the compiler and its development artifacts. Existing SHADOW owner pointers and eight-decision behavior remain unchanged.
