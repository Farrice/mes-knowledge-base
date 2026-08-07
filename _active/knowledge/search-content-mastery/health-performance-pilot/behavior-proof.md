# Behavior Proof — Generic Promise to Inspectable Answer Asset

## Test

The same approved `SearchBrief` evaluated two local artifacts:

- **Before:** `before-answer-fixture.md` — a constructed generic baseline, not live copy.
- **After:** `improved-answer-asset.md` — the source-backed Claim Receipt answer.

Both were scored with the same deterministic evaluator and no expert or operator override.

## Result

| Asset | Original/final score | Proof state | Receipt |
|---|---:|---|---|
| Before fixture | 2.3 / 10 | `PREDICTED` | `project-pack/scores/score-d60c1847a550.json` |
| Improved answer | 9.1 / 10 | `PREDICTED` | `project-pack/scores/score-29653ecf671a.json` |
| Delta | **+6.8** | readiness change only | same brief and evaluator |

## Extracted mechanic applied

The portfolio mechanic was not “add more keywords.” The decision changed from a generic promise of trust and AI-search visibility to an inspectable answer with:

- one target query and audience;
- a direct answer;
- a five-field Claim Receipt;
- a worked example distinguishing composition fact from outcome implication;
- source receipts and limitations;
- qualified-review ownership;
- an explicit CTA and falsifier;
- separate readiness and outcome language.

## Changed decision

**Before:** the content would be rejected because it contains no source receipt, information gain, measurement hypothesis, or safe route from claim to reviewer.

**After:** the content is ready for internal claim/source/taste review. It is **not** ready for publication, and the score does not promote it to ranked, cited, trafficked, converted, or sold.

## Remaining proof gap

- No dated human comprehension review has occurred.
- No real client claim, product, or page has been tested.
- No publication, indexation, ranking, citation, traffic, conversion, or collected-revenue event exists.
- The prototype's willingness-to-pay remains `UNTESTED`.

## Evaluator regression repaired

The first run exposed a rubric defect: “does not guarantee” was being counted as guarantee language. The evaluator now ignores sentence-local disclaimers while still flagging asserted guarantees. A later prose pass removed mechanical parallelism without changing the 9.1 readiness score. The latest receipts above are the acceptance pair; earlier receipts remain in the append-only project pack as diagnostic history.
