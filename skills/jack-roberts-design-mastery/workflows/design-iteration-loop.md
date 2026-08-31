# Design Iteration Loop

> The structured micro-polish process that takes an 80% draft to 100% — Jack Roberts' Step 4 methodology for refinement without starting over.

Use this lightweight categorical pass when screenshots or a named reference bar are unavailable. For renderable, taste-bearing work with a reference, use `design-gauntlet.md`; it adds baseline preservation, viewport evidence, comparative judgment, regression recovery, and a two-repair cap.

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

**Structural fixes only.** Don't touch colors, fonts, or details yet. Record the baseline before editing.

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

Fix accidental compliance drift. In Precision Polish mode the DESIGN.md is source truth. If the user explicitly wants Theme-Respect Elevate or Creative Unleash, proposed token or system changes must be named and preference-locked rather than silently treated as polish.

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

5. **Factual veto.** If the design contains data, stats, claims, or research, route them through the workspace's deterministic or source-grounded verification path. Replace unsupported claims or label them honestly. Real subagents may support an explicitly authorized research run, but are never an automatic requirement.

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
- The named reference bar and deterministic checks pass with visible evidence
- User says: "This is it"
- Plateau or regression: a new candidate does not visibly beat the prior best
- Maximum: two repair cycles after the five categorical assessment passes; then preserve the best version and re-evaluate the DESIGN.md or reference

## Output
- Refined design at production quality
- Iteration log documenting all changes and decisions
- Final Blind Bar verdict, with supporting evidence
- Sign-off confirmation

## Output Schema
```
Iteration Loop Result: [design name]
├── Iteration Log            (one "### Round [#]: [Focus Area]" block per round actually run — Changes made / Remaining issues / Quality improvement)
├── Rounds Completed: __/5   (which of the 5 named rounds ran: Structural / DESIGN.md Compliance / Micro-Polish / Animation / "Would I Pay For This?")
├── Final Blind Bar Verdict: [PASS/PARTIAL/FAIL + evidence]
├── Refined design            (the production-quality artifact itself)
└── Sign-off confirmation     (stop condition met: score ≥13, user said "this is it", diminishing returns, or Round 5 reached)
```

## Quality Gate
- Stop condition is one of the named conditions in "When to stop iterating" — never stop without naming it explicitly.
- Round 2 (Design System Compliance) checklist fully checked off — no rogue hex values, no off-scale font sizes, before Round 3 polish begins. Rounds run in order; skipping Round 2 to jump to polish is a failed gate.
- If the design contains any data, stat, or claim, the factual-veto path runs before sign-off and names its evidence status.
- Iteration Log records a visible or deterministic before/after delta for every repair; a self-awarded score is not proof.
- If two repair cycles do not beat the prior best, restore that best version and re-evaluate the DESIGN.md or reference rather than continuing an open-ended loop.
