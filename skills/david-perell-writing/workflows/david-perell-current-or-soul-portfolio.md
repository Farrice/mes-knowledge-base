---
name: david-perell-current-or-soul-portfolio
produces: mission-locked Portfolio Boundary with project classes and stop rules
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: Attention opportunities may be funding, blending with, or displacing the creator's stated soul work.
---

# Current-or-Soul Portfolio

## Pre-Flight Gate

Read `genius.md` and the Current Riding as a Means pattern. Require a project inventory, desired reputation, explicitly named soul work, current opportunities, capacity, commercial constraints, non-negotiables, and review date. Missing mission boundaries return `HOLD`; do not infer what should matter. Missing current source, date, or expiry remains `UNCONFIRMED`. Use numbers only when the user supplies them.

## Input Required

1. Project and commitment inventory.
2. Desired reputation and named soul work.
3. Current opportunities with evidence and expiry.
4. Available capacity and commercial constraints.
5. Creator-supplied non-negotiables.
6. Optional user-supplied numeric allocation.
7. Review date.

## Procedure

### 1. Create the Soul Lock

Freeze deeper work, desired reputation, non-negotiables, and identity distortions the creator rejects before considering current opportunities.

### 2. Normalize the Portfolio

Record purpose, effort, deadline, dependencies, commercial role, current evidence, and opportunity cost for each project.

### 3. Classify Every Project

- `SOUL`: worth doing independent of current attention.
- `CURRENT-FUNDED`: tactical work with an explicit resource-transfer contract into soul work.
- `BOTH`: advances soul work and fits a real current without distortion.
- `HOLD`: missing evidence, mission conflict, unsupported current, or unavailable capacity.

### 4. Test the Bargain

For current-funded work, name the exact resource it is supposed to buy—money, time, distribution, access, or learning—the evidence that transfer occurs, and what prevents indefinite expansion.

### 5. Apply Capacity

Validate user-supplied numbers when present. Otherwise return qualitative priority and conflicts without fabricated percentages, hours, or ratios.

### 6. Set Stop Rules

Define expiry, time ceiling, mission-drift trigger, failed resource-transfer trigger, and review point. Prepare downstream actions but do not schedule, publish, mutate a queue, or promise results.

## Output Schema

```text
## Current-or-Soul Portfolio Boundary
Status: READY | PARTIAL | HOLD
Allocation mode: USER-SUPPLIED NUMERIC | QUALITATIVE ONLY
Effect state: UNTESTED EFFECT unless direct evidence exists

## Soul Lock
- Named soul work:
- Desired reputation:
- Non-negotiables:
- Identity-distortion vetoes:

## Portfolio Classification
| Project | SOUL / CURRENT-FUNDED / BOTH / HOLD | Evidence | Soul contribution | Current evidence/expiry | Capacity cost | Distortion risk | Rationale |

## Current-Funded Transfer Contracts
| Project | Resource expected | Transfer into soul work | Evidence state | Stop rule |

## Capacity Boundary
- Supplied capacity:
- User-supplied allocation, if any:
- Conflicts:
- Qualitative priority order:

## Portfolio Stop Rules
| Trigger | Project affected | Required response |

## HOLD Ledger
| Project | Missing evidence or conflict | Required decision |

## Review
- Next review date:
- Evidence to collect:
- Downstream action requiring approval:
```

## Quality Gate

- [ ] Soul work and non-negotiables were fixed before tactic selection.
- [ ] Every project receives one of the four allowed classifications.
- [ ] CURRENT-FUNDED rows contain a resource-transfer contract and stop rule.
- [ ] No percentage, hour, ratio, reach, revenue, or freedom claim was invented.
- [ ] High attention cannot redefine the creator's soul work.
- [ ] No queue, calendar, publication, budget, or external system changed.

Execution prompt: references/prompts-v2/david-perell-current-or-soul-portfolio.md — honor its Output Contract.
