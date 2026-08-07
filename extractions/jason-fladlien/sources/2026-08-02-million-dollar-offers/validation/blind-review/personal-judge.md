# Blind Judge Receipt — Personal Fixture

## Verdict

**Winner: Cobalt — narrow but clear.**  
**Result: PASS.**

Cobalt makes materially better package and risk decisions without materially regressing the approved spine. Orchid is more minimal and slightly stricter with evidence, but leaves two consequential gaps unresolved.

## Material Decision Deltas

| Decision | Orchid | Cobalt | Edge |
|---|---|---|---|
| Sprint activation | Explicitly starts the 21-day clock only after artifacts and network list arrive | Requires inputs before build work, but is less explicit about the clock trigger | Orchid |
| Audit outcome | Leaves the paid audit's output unspecified | Adds a bounded, documented sprint fit/no-fit decision within the existing 90 minutes | Cobalt, material |
| First tangible win | Sequences approval before messaging and planning | Makes that approval a dated milestone inside the sprint | Cobalt, material |
| Guarantee ambiguity | Parks undefined terms while bounding the refinement-week scope | Holds public use until eligibility and “qualified conversation” are defined, without inventing either | Cobalt, material |
| Cross-burden handling | Clean, low-change solution, but limited treatment of rigidity or buyer pressure | Explicitly weighs deadline pressure, rigidity, administration, and privacy, then accepts or holds accordingly | Cobalt |
| Price and proof | Holds price and preserves market unknowns | Same, with a slightly more operational testing boundary | Near tie |

Cobalt's strongest better decision is the guarantee go-live hold: it converts a known contractual ambiguity into an owner action while keeping the definitions unknown. The fit/no-fit audit endpoint is also a meaningful package improvement that remains bounded by the existing audit duration.

## Worse Decisions or Unnecessary Changes

### Orchid

- “The audit is not credited against the sprint” closes an unsupported payment-term question. The fixture establishes separate paid rungs, but not whether an audit credit is allowed.
- It parks the guarantee definitions but does not decide whether the ambiguous guarantee can be used publicly.
- It leaves the paid audit without a stated buyer-facing output.

### Cobalt

- The fit/no-fit endpoint is useful, but the packet does not supply decision criteria; implemented carelessly, it could become an arbitrary new promise.
- It treats missing first-win timing as established friction despite having no direct buyer-response evidence. The absence is factual; the magnitude of buyer friction is inferred.
- A dated approval milestone can create artificial pressure, though Cobalt identifies and bounds that burden.

These are contained risks, not material regressions: Cobalt leaves duration, prices, sprint outcome, client rep gates, guarantee remedy, and proof claims unchanged.

## Scores

| Candidate | Decision quality | Evidence respect | Operational usefulness |
|---|---:|---:|---:|
| Orchid | 8.4/10 | 9.4/10 | 8.6/10 |
| Cobalt | 9.0/10 | 9.1/10 | 9.3/10 |

**PASS — Cobalt makes at least one materially better offer decision without a material regression.**

## Isolation and Mapping Boundary

- Judge task: `/root/blind_personal_judge`.
- Context fork: `none`.
- Allowed reads: frozen fixture plus anonymized Orchid and Cobalt candidates only.
- Mapping was withheld from the judge: Orchid = baseline; Cobalt = enhanced.
- Exact model identifier and a platform-level file-read transcript were not exposed.
- This receipt proves a blinded fixture judgment, not live buyer response or market performance.
