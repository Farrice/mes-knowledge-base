# Design Iteration Loop

> The structured micro-polish process that takes an 80% draft to 100% — Jack Roberts' Step 4 methodology for refinement without starting over.

## Context Required
- **Load First**: `genius.md` — Iterative Micro-Polish signature move
- **Required**: An existing design draft (website, presentation, graphic) to refine

## Inputs
- **Required**: The design file/URL to iterate on
- **Required**: The DESIGN.md it was built against
- **Optional**: Specific feedback from the user ("I don't like X")
- **Optional**: Quality scores from `/anti-slop-audit`

## Workflow

### Round 1: Structural Assessment (Does the skeleton work?)

Evaluate the overall structure before touching any details:

1. **Information hierarchy check:**
   - What's the first thing the eye sees? Is that correct?
   - Can someone understand the purpose within 3 seconds?
   - Does the visual flow match the intended reading order?

2. **Section balance:**
   - Are any sections too dense or too sparse?
   - Is there consistent vertical rhythm between sections?
   - Does the footer feel intentional or like an afterthought?

3. **Responsive reality:**
   - Check 375px (mobile), 768px (tablet), 1440px (desktop)
   - Does anything break, overflow, or stack awkwardly?
   - Is mobile layout designed, or just desktop-stacked?

**Structural fixes only.** Don't touch colors, fonts, or details yet.

### Round 2: Design System Compliance (Does it match the DESIGN.md?)

Compare every element against the DESIGN.md specification:

```
□ All colors use DESIGN.md tokens (no rogue hex values)
□ All font sizes follow the type scale
□ All spacing follows the spacing system
□ Button styles match specification
□ Card/container styles match specification
□ Hover states match specification
□ Animation timing matches specification
□ Logo placement matches specification
```

Fix any compliance drift. The DESIGN.md is the law.

### Round 3: Micro-Polish Pass (The details that make it premium)

Go element-by-element through the design:

**Typography polish:**
- Check line lengths (45-75 characters optimal for body)
- Verify letter-spacing on headings (display text often needs tracking)
- Ensure no orphan words (single words on their own lines)
- Validate font loading (no FOUT — flash of unstyled text)

**Color polish:**
- Check contrast ratios (WCAG AA minimum: 4.5:1 for text)
- Verify gradients are smooth (no banding)
- Ensure hover states have visible color change
- Validate dark/light backgrounds have proper text contrast

**Spacing polish:**
- Check padding consistency within same-type components
- Verify margins between sections are consistent
- Ensure nothing touches viewport edges on mobile
- Validate icon-to-text alignment (vertical center)

**Image polish:**
- Check all images are sharp (not stretched or pixelated)
- Verify alt text exists for accessibility
- Ensure lazy-loading is working
- Validate aspect ratios are consistent within same component types

### Round 4: Animation & Interaction Polish

- Smooth all transitions (no janky or stuttering animations)
- Verify scroll-triggered animations fire at the right scroll position
- Check that hover effects feel responsive (< 100ms perceived delay)
- Ensure no animation plays on page load before content is visible
- Test keyboard navigation (Tab, Enter, Escape)

### Round 5: The "Would I Pay For This?" Test

Final pass from the user's perspective:

1. **Screenshot it.** Look at the screenshot as a static image. Is it beautiful?
2. **Show it to someone.** Would they guess this was AI-generated?
3. **Compare to references.** Put it next to the original references from the design philosophy. Does it belong in that league?
4. **The magazine test.** Could this appear in a design publication?

If any answer is "no" — identify the specific element causing doubt and fix it.

5. **Sub-agent factcheck.** If the design contains any data, stats, claims, or research:
   - Spin up sub-agents to verify every factual claim independently
   - Replace anything unverifiable with confirmed data
   - Source: *"I want you to spin up sub agents and fact check that research"* — this is non-negotiable for client-facing work

### Iteration Protocol

After each round, document changes:

```markdown
## Iteration Log

### Round [#]: [Focus Area]
**Changes made:**
1. [Specific change + why]
2. [Specific change + why]
3. [Specific change + why]

**Remaining issues:**
- [Issue that needs next round]

**Quality improvement:** [Score before → after]
```

**When to stop iterating:**
- Anti-Slop Score: ≥ 13/15
- User says: "This is it"
- Diminishing returns: Changes are micro-adjustments < 1% visual impact
- Maximum: 5 iteration rounds (if not done by Round 5, re-evaluate the DESIGN.md)

## Output
- Refined design at production quality
- Iteration log documenting all changes and decisions
- Final Anti-Slop score
- Sign-off confirmation

## Output Schema
```
Iteration Loop Result: [design name]
├── Iteration Log            (one "### Round [#]: [Focus Area]" block per round actually run — Changes made / Remaining issues / Quality improvement)
├── Rounds Completed: __/5   (which of the 5 named rounds ran: Structural / DESIGN.md Compliance / Micro-Polish / Animation / "Would I Pay For This?")
├── Final Anti-Slop Score: __/15
├── Refined design            (the production-quality artifact itself)
└── Sign-off confirmation     (stop condition met: score ≥13, user said "this is it", diminishing returns, or Round 5 reached)
```

## Quality Gate
- Stop condition is one of the four named in "When to stop iterating" — never stop mid-round without hitting one explicitly.
- Round 2 (Design System Compliance) checklist fully checked off — no rogue hex values, no off-scale font sizes, before Round 3 polish begins. Rounds run in order; skipping Round 2 to jump to polish is a failed gate.
- If the design contains any data, stat, or claim, Round 5's sub-agent factcheck runs before sign-off — per the workflow's own "non-negotiable for client-facing work" language.
- Iteration Log has a "Quality improvement: [Score before → after]" entry for every round that ran — a round with no logged before/after is not counted as complete.
- If Round 5 is reached without hitting 13+/15, the DESIGN.md itself is re-evaluated (per the Maximum rule) rather than continuing to iterate the same broken foundation.
