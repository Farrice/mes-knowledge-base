# Workflow 09: Production Capacity Learning Loop

Use this when recurring production friction, asset reuse, or concurrency needs an evidence-led decision without importing another studio's scale.

This workflow learns from local stoppages and constraints. It does not prescribe crew counts, set counts, cycle times, or capital spending.

## Inputs

- planned production slate or next three candidate pieces;
- available environments, templates, graphics, equipment, people, and systems;
- current concurrency assumptions;
- recent wait, stop, rework, or substitution evidence;
- freshness and continuity notes;
- transformation contracts for the affected pieces;
- review owner and decision horizon.

## Diagnose before treatment

Choose the primary capacity failure:

- `BORROWED SCALE`: another studio's counts or speed are being copied without local evidence.
- `INVISIBLE BOTTLENECK`: work stops repeatedly but the constrained asset is not logged.
- `ASSET BLINDNESS`: reusable environments or production assets are unknown.
- `REUSE OVERREACH`: efficiency makes the content feel repeated or breaks story meaning.
- `CONCURRENCY FICTION`: the plan assumes owners or assets can serve simultaneous units when they cannot.
- `EXPANSION FIRST`: new capacity is proposed before reconfiguration, sequencing, or adaptation is tested.
- `VANITY EFFICIENCY`: throughput improves while recognition, shift, or trust deteriorates.

## Steps

1. **Map the asset topology.**
   - List environments, templates, graphics, equipment, people, and systems.
   - For each, record primary use, adaptable uses, transformation limits, and continuity constraints.

2. **State local concurrency assumptions.**
   - Name which units may overlap.
   - Name every shared owner or asset.
   - Mark assumptions as `OBSERVED`, `PLANNED`, or `UNKNOWN`.

3. **Build the bottleneck log.**
   - Record the stopped or delayed unit.
   - Name the constrained asset or decision.
   - Capture duration or consequence when known.
   - Distinguish a single inconvenience from a repeated capacity constraint.

4. **Choose the smallest evidence-supported response.**
   - `RESEQUENCE`
   - `ADAPT OR RECONFIGURE`
   - `SUBSTITUTE`
   - `DUPLICATE OR ADD CAPACITY`
   - `ACCEPT THE CONSTRAINT`
   - Escalate only when the prior option cannot preserve the story and mission.

5. **Run the freshness and meaning veto.**
   - Reject reuse that makes the story visibly stale, confuses geography, changes character meaning, or weakens the package payoff.
   - Record the exact transformation invariant at risk.

6. **Set a review cadence from the decision horizon.**
   - Use a cadence proportionate to the local slate and evidence.
   - The source's quarterly review is an example, not a default.

7. **Define the next evidence.**
   - Name the log entry, utilization observation, wait-time signal, or quality check that would confirm or reverse the decision.

## Output contract

Produce:

- asset-topology map;
- concurrency and shared-resource map;
- bottleneck log;
- response decision with rejected alternatives;
- freshness and transformation veto;
- review cadence;
- next-evidence plan.

Execution prompt: references/prompts-v2/production-capacity-learning-loop.md — honor its Output Contract.

## Output schema

```text
ASSET TOPOLOGY
[asset / primary use / adaptable uses / limits / continuity constraints]

CONCURRENCY MAP
[unit / timing / shared owner or asset / status]

BOTTLENECK LOG
[event / constrained asset / consequence / recurrence / evidence class]

CAPACITY DECISION
- Selected response:
- Why:
- Rejected alternatives:

FRESHNESS AND TRANSFORMATION VETO:
REVIEW CADENCE:
NEXT EVIDENCE:
```

## Adaptations

- **Solo creator:** assets include time blocks, locations, templates, proof sources, and editing capacity.
- **Small team:** map shared people as constraints without turning the packet into workforce planning.
- **Studio:** connect the log to existing production systems; do not invent a new software implementation.
- **Content queue:** use the topology to select feasible concepts, not to let convenience determine mission.

## Quality gate

- Are all numbers local observations or visibly labeled assumptions?
- Is the constrained asset named?
- Is recurrence distinguished from one-off inconvenience?
- Was the smallest viable response considered before expansion?
- Does reuse preserve story meaning and visible freshness?
- Is the review cadence tied to a decision horizon?
- Is the next evidence capable of reversing the decision?
- Are throughput and transformation quality kept separate?
