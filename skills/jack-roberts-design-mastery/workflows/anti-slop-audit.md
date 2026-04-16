# Anti-Slop Audit

> Score any AI-generated design against the 15-point Anti-Slop checklist — diagnose generic patterns and prescribe specific fixes.

## Context Required
- **Load First**: `genius.md` — Anti-Slop Architecture (Genius Pattern #3)

## Inputs
- **Required**: The design to audit (URL, screenshot, or HTML file)
- **Optional**: The DESIGN.md it was built against (for fidelity checking)
- **Optional**: The intended audience and purpose

## Workflow

### Step 1: First-Impression Scan (3 Seconds)
Open the design and answer within 3 seconds of viewing:
1. Does this look AI-generated? (Yes/No — gut reaction)
2. Have I seen this exact layout before? (Yes/No)
3. What is the ONE visual element that stands out? (If nothing — that's a fail)

### Step 2: The 15-Point Anti-Slop Checklist

Score each item 0 (fail) or 1 (pass):

**Color Slop (3 points)**
| # | Check | AI Default Pattern | What to Look For |
|---|-------|-------------------|------------------|
| 1 | **No default purple gradients** | `#7C3AED` → `#3B82F6` gradient | Colors should be brand-specific, not AI's favorite palette |
| 2 | **No generic blue CTA** | `#3B82F6` or `#2563EB` buttons | CTA color should be intentional, not default primary blue |
| 3 | **Palette has personality** | Safe, inoffensive color choices | At least one color choice surprises or delights |

**Typography Slop (3 points)**
| 4 | **Not Inter/default sans-serif** | Inter, system-ui, or Arial everywhere | Typography has character — specific fonts chosen for a reason |
| 5 | **Weight variation exists** | Everything at 400 or 600 weight | Light (300), regular (400), medium (500), bold (700) used purposefully |
| 6 | **Type scale is designed** | Random-feeling font sizes | Clear hierarchy: display → heading → body → caption with consistent proportions |

**Layout Slop (3 points)**
| 7 | **No three-column grid of rounded boxes** | Three equal cards with rounded corners | If using cards, they're asymmetric, staggered, or visually distinctive |
| 8 | **Hero isn't left-text/right-image** | 50/50 split with text left, illustration right | Hero section has a unique composition |
| 9 | **Sections don't all look the same** | Repeating white→gray→white pattern | Each section has distinct visual treatment |

**Detail Slop (3 points)**
| 10 | **Hover states exist** | Static, flat interactions | Interactive elements respond to hover with color, transform, or shadow changes |
| 11 | **Animations aren't generic** | No animations, or `fade-in` on everything | Entrance effects are varied, timed, and contextual |
| 12 | **Negative space is intentional** | Random amounts of padding | Whitespace creates rhythm and guides the eye |

**Soul Slop (3 points)**
| 13 | **There's a visual "signature"** | Nothing memorable about the design | One element that's uniquely THIS — not anyone else's design |
| 14 | **Imagery isn't stock-feeling** | Generic illustrations or photos | Images feel curated, styled, or generated to match the aesthetic |
| 15 | **The design has an opinion** | Safe, pleasing-to-everyone aesthetic | The design has made bold choices that not everyone would make |

### Step 3: Score & Grade

```
Total Score: ___/15

15/15  → ZERO SLOP    — This passes as human-designed professional work
13-14  → MINIMAL SLOP — Minor tells, mostly excellent  
10-12  → MODERATE SLOP — Noticeable AI patterns, needs targeted fixes
7-9    → HIGH SLOP    — Multiple generic patterns, significant rework needed
0-6    → FULL SLOP    — Start over with a proper DESIGN.md
```

### Step 4: Prescribe Fixes

For each failed check, provide a specific, actionable fix:

```markdown
## Anti-Slop Prescription

### Failed: [Check Name]
**Current**: [What the design has now]
**Problem**: [Why this reads as AI-generated]
**Fix**: [Exact change to make — specific colors, fonts, layout adjustments]
**Reference**: [Link to an example of this done well]
```

### Step 5: DESIGN.md Gap Analysis (if applicable)

If a DESIGN.md was provided:
1. Which DESIGN.md tokens were NOT used in the final output?
2. Which design decisions in the output have NO corresponding DESIGN.md token?
3. Where did the implementation drift from the specification?

Produce a `DESIGN.md Compliance Report`:
```
Tokens Used:     __/__ (percentage)
Drift Points:    [list of deviations]
Missing Tokens:  [tokens needed but not in DESIGN.md]
```

## Output
- Anti-Slop Scorecard (15-point with pass/fail per item)
- Grade (Zero Slop → Full Slop)
- Prescription Document (specific fixes for each failure)
- DESIGN.md Compliance Report (if applicable)
- Revised design (optional — apply the fixes automatically)
