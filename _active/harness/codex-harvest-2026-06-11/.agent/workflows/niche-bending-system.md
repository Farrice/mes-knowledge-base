---
description: Turn any credible expertise, domain, or niche into differentiated content angles using niche bending, empty-square mapping, borrowed fluency, visual language transfer, and production-ready validation
---

# /niche-bending-system - Niche Bending Command OS

Create a practical Niche Bending Pack from a user's expertise, market, platform, and desired outcome. This is an orchestrator over the existing Tim Danilov niche-bending skill, not a duplicate expert skill.

## Source Grounding

Read first:

1. `extractions/tim-danilov/niche-bending-system/source-map.md`
2. `extractions/tim-danilov/niche-bending-system/command-contract.md`
3. `extractions/tim-danilov/niche-bending-system/operating-mechanics.md`
4. `skills/tim-danilov-niche-bending/SKILL.md`
5. `skills/tim-danilov-niche-bending/genius.md`

Use the source map for evidence anchors. Do not load the full transcript unless the user asks for timestamp-level support or the output needs source-detail proof.

## Runtime Inputs

Required:

- Core expertise or niche
- Target audience or market
- Primary platform
- Desired outcome: growth, authority, lead generation, offer differentiation, or content series

Optional:

- Current content, format rut, or examples
- Competitors or benchmark creators
- Scout markets or borrowed format sources
- Existing proof, constraints, offers, or production capacity

If required inputs are missing and cannot be inferred, ask only for the missing execution-critical fields.

## Component Order

### Phase 1: Input Gate And Expertise Constraint

Lock:

- user's credible expertise payload
- target market or audience
- primary platform
- desired outcome

Reject bends the user cannot fill with real expertise. This is the anti-gimmick gate.

Output:

- expertise lock
- market lock
- platform lock
- outcome lock
- constraints and assumptions

### Phase 2: Demand And Format Staleness Scan

Load only if needed:

1. `skills/tim-danilov-niche-bending/workflows/blue-ocean-market-identification.md`

Identify:

- market demand signal
- dominant stale formats
- adjacent markets worth including in the grid
- current format consensus

If live research is unavailable or not approved, use supplied competitors, user context, and clearly labeled assumptions.

Output:

- demand/staleness table
- target and adjacent market rows for the grid

### Phase 3: Outlier Format Scout

Load only if needed:

1. `skills/tim-danilov-niche-bending/workflows/viral-format-engineering.md`

Find or infer candidate source formats:

- prefer smaller-channel or smaller-account outliers when research is available
- separate subject matter from format skeleton
- identify title architecture, hook mechanic, narrative arc, visual language, and pacing

If the user does not provide scout examples and live research is not approved, use a bounded starter set of proven formats and label it as a starter scout, not current market proof.

Output:

- outlier format table
- 5 to 12 candidate format columns for the grid

### Phase 4: Empty Square Grid

Build a compact market-format grid:

- rows: target market plus adjacent markets
- columns: proven candidate formats
- marks: occupied, emerging, empty, incompatible

Prioritize cells by:

- expertise fit
- format proof
- market demand
- blue-ocean potential
- platform fit

Output:

- empty square grid
- top ranked opportunities

### Phase 5: Borrowed Fluency And Visual Language

Use:

1. `extractions/tim-danilov/niche-bending-system/quality-gates.md`
2. `skills/tim-danilov-niche-bending/workflows/high-conversion-content-design.md` when drafting production specs

For the top opportunities, map:

- source-format vocabulary
- expertise translations
- cultural shorthand and metaphors
- thumbnail or first-frame logic
- layout, motion, pacing, props, or interface cues

Output:

- borrowed fluency map
- visual language notes

### Phase 6: Three Production-Ready Bends

Produce three concepts. Each must include:

- bend equation: `[Target Market] + [Borrowed Format]`
- title
- hook
- format skeleton
- expertise payload
- borrowed fluency
- visual language
- platform adaptation
- validation verdict

Output:

- three production-ready bends
- first experiment and success metric

## Output Schema

```markdown
# Niche Bending Pack: [Expertise / Market]

## Routing Trace
- Source:
- Components:
- Assumptions:
- Evidence limits:

## Expertise Constraint
| Field | Lock |

## Market And Format Diagnosis
| Market | Demand Signal | Stale Format | Opportunity |

## Outlier Format Scout
| Source Market | Format | Proof Signal | Portable Skeleton |

## Empty Square Grid
| Market / Format | Format 1 | Format 2 | Format 3 |

## Borrowed Fluency Map
| Source Term Or Trope | Expertise Translation | Use |

## Visual Language Notes
| Format Signal | How It Shows Up |

## Three Production-Ready Bends
### 1. [Bend Name]
- Bend:
- Title:
- Hook:
- Skeleton:
- Expertise payload:
- Borrowed fluency:
- Visual language:
- Platform adaptation:
- Verdict:

## Validation Verdict
- Best first bet:
- Fix before production:
- Reject:

## First Experiment
- Make:
- Measure:
- Double down if:
- Archive if:
```

## Quality Gate

Before final output, check:

- expertise constraint passes,
- every recommended bend has a real payload,
- format and market are separated,
- empty squares are not treated as demand proof unless the format and market are independently proven,
- borrowed fluency is structural, not decorative,
- visual language is specific enough to brief a designer or producer,
- the first experiment is clear enough to make immediately.

## Verification

For system edits, run:

```bash
python3 execution/sync_registries.py
python3 execution/validate_skill.py tim-danilov-niche-bending
python3 execution/validate_skill.py source-command-niche-bending-system
python3 execution/command_menu.py search "take any domain expertise and find differentiated niche bending angles"
python3 execution/workflow_router.py search "take any domain expertise and find differentiated niche bending angles"
python3 execution/routing_governor.py evaluate "take any domain expertise and find differentiated niche bending angles"
python3 execution/context_retriever.py search "take any domain expertise and find differentiated niche bending angles" --top 8
python3 execution/codex_live_surface_audit.py --strict
```
