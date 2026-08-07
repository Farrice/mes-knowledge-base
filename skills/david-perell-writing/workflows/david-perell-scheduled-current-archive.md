---
name: david-perell-scheduled-current-archive
produces: evidence-bounded Scheduled Archive Calendar with HOLD rows and evergreen fallbacks
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: An archive and sourced future-event packet need supported preparation windows without queue mutation.
---

# Scheduled-Current Archive

## Pre-Flight Gate

Read `genius.md` and `references/cross-domain-patterns.md`. Require an archive inventory, sourced future-event packet, workflow 08 `SCHEDULE` receipts, supplied lead times, planning horizon, current date, capacity, and expiry assumptions. Missing sources, dates, future windows, or receipts stay as HOLD rows. Do not research events, complete dates from memory, or mutate a queue.

## Input Required

1. Archive inventory with stable IDs, theses, evidence, and modules.
2. Future-event packet with sources, dates, windows, uncertainty, and expiry.
3. Workflow 08 `SCHEDULE` receipts for proposed pairings.
4. Preparation lead times, planning horizon, current date, and capacity.
5. Audience and brand territory.

## Procedure

### 1. Normalize the Archive

Record each idea's invariant core, evidence readiness, format, and whether a module has its own claim, evidence, context, and return path.

### 2. Normalize Events

Record identity, source, date, release window, expiry, and confidence. A passed window becomes `EXPIRED CURRENT`; a canceled event becomes `NO EVENT` when supplied evidence supports that state.

### 3. Join Only Supported Pairings

Require a `SCHEDULE` receipt and a substantive connection, not keyword overlap or celebrity proximity. Missing receipts become `NEEDS WORKFLOW 08`.

### 4. Back-Plan

Calculate preparation start, draft-ready date, review date, release window, and expiry from supplied dates and lead times.

### 5. Surface Collisions

Show capacity, brand, and window conflicts. Recommend a decision but do not silently reprioritize.

### 6. Preserve Fallbacks and Ownership

Every scheduled row retains an evergreen fallback. Kieran receives proposed queue actions only after human selection; this workflow makes no persistent scheduling change.

## Output Schema

```text
## Scheduled Archive Calendar
Planning horizon:
Current date:
State: READY | PARTIAL | HOLD

| Archive ID | Module | Invariant core | Event/source/date | Schedule receipt | Supported connection | Prep start | Review date | Release window | Expiry | Status | Evergreen fallback |

Allowed row states: SCHEDULED | HOLD | NEEDS WORKFLOW 08 | EXPIRED CURRENT | NO EVENT

## Capacity and Collision Report
| Window | Collision | Consequence | Recommended decision |

## Unsupported or Invalid Mappings
| Archive ID | Event | Failure reason | Required evidence |

## Unmatched Archive Opportunities
[archive items retained without forced mapping]

## Proposed Kieran Handoff
| Selected row | Proposed queue action | Human approval required |

## No-Mutation Receipt
- Queue changed: NO
- Publication scheduled: NO
```

## Quality Gate

- [ ] Every date comes from a supplied packet and every pairing has a workflow 08 receipt.
- [ ] Each module can stand alone without becoming a contextless excerpt.
- [ ] Back-planning clears the release window.
- [ ] Weak connections remain HOLD instead of receiving a forced wrapper.
- [ ] Every scheduled row has an expiry and evergreen fallback.
- [ ] No queue, calendar, publication, reach, conversion, or revenue claim was created.

Execution prompt: references/prompts-v2/david-perell-scheduled-current-archive.md — honor its Output Contract.
