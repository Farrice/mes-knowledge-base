# Artifact Comprehension v0.2 — Human Gate

Status: **HUMAN GATE PENDING**

This tests only substantial artifact presentation. It does not test or alter
ordinary replies, closeouts, Clear Depth, or the global three-prompt system.

For each example, choose `X`, `Y`, or `TIE`, then answer four questions:
faster to understand, depth preserved, easier to act, and whether the
representation earned its place.

## AHG-001 — Strategy

**Prompt:** Show the chosen offer direction, tradeoffs, and immediate action.

### Variant X

The recommended direction is to keep one proof-led offer as the primary owner
while testing different message angles within that offer. This is preferable
to running three simultaneous offers because it reduces proof risk and keeps
the work closer to revenue. More preparation should not be the priority because
it does not produce buyer evidence. The next action is to run one buyer-facing
test, although the demand assumption remains untested and should not be
described as validated.

### Variant Y

#### Verdict

Keep one proof-led offer as the owner. Test message angles inside it rather
than opening another offer lane.

| Route | Revenue proximity | Proof risk | Decision |
|---|---:|---:|---|
| One owner, bounded angles | High | Low | Choose |
| Three simultaneous offers | Low | High | Park |
| More preparation | Low | Medium | Stop |

**Next action:** Run one buyer-facing test. Demand remains untested.

## AHG-002 — Research

**Prompt:** Summarize the demand evidence without overstating buyer validation.

### Variant X

#### What changes

Category interest is supported; willingness to pay for this exact offer remains
untested.

| Claim | Support | Confidence | Implication |
|---|---|---|---|
| Buyers discuss the problem | Interview set | Verified | Continue |
| They will buy this package | No payment event | Untested | Run a paid test |

**Caveat:** Attention is not purchase behavior.

### Variant Y

The current evidence suggests that buyers discuss the problem, based on the
interview set, so there is enough support to continue exploring the category.
However, there is no payment event demonstrating that buyers will purchase this
specific package. That means category attention should not be treated as
willingness to pay. The practical implication is to continue only through a
paid test, with the buyer-response assumption clearly labeled as untested.

## AHG-003 — Implementation

**Prompt:** Show how to build and validate the pilot while preserving the stop
boundary.

### Variant X

The pilot should first preserve the successful global behavior and then build
artifact-only fixtures. After the fixtures exist, negative controls should be
run before collecting human artifact ratings. Only after those stages should
there be an explicit promotion decision. The process must stop before merge,
hook changes, or global activation, and each stage should retain its verifier
and rollback note.

### Variant Y

#### End state

Workspace proof, stopped before promotion.

1. Freeze the successful global behavior.
2. Build artifact-only fixtures.
3. Run negative controls.
4. Collect human artifact ratings.

**Flow:** Fixtures → sabotage proof → human gate → explicit promotion decision

**Stop:** Before merge, hooks, or global activation.

## Rating Sheet

| Example | Preferred X/Y/TIE | Faster? | Depth preserved? | Easier to act? | Representation earned? | Why? |
|---|---|---|---|---|---|---|
| AHG-001 |  |  |  |  |  |  |
| AHG-002 |  |  |  |  |  |  |
| AHG-003 |  |  |  |  |  |  |
