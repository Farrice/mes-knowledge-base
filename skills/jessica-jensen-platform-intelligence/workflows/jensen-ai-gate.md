# /jensen-ai-gate — AI Content Authenticity Gate

## Purpose
Pre-publish audit ensuring AI-augmented content passes LinkedIn's detection signals and maintains unmistakable human voice. The "could AI have written this for 50 other people" test.

## When to Use
- Before publishing any AI-assisted LinkedIn content
- When content "sounds right but feels off"
- When engagement rates drop despite consistent quality (possible AI detection)
- As a mandatory gate for ghostwriting and agency content production

## Inputs
- `[DRAFT]` — The content draft to audit
- `[AUTHOR_VOICE]` — Reference voice samples or voice profile of the intended author
- `[AI_USAGE]` — How AI was used in creation (ideation / drafting / editing / none)

## Steps

### Step 1 — The 50-Person Test
Apply Jensen's core test (Genius Pattern 10): "Could AI have written this identically for 50 other people?"

Score each dimension:
| Dimension | Generic (1-3) | Somewhat Unique (4-6) | Unmistakably One Person (7-10) |
|-----------|--------------|----------------------|-------------------------------|
| **Opening line** | Template opener | Topic-specific but replaceable | Only THIS person would start this way |
| **Perspective** | Consensus view | Informed take | Contrarian, experienced, or surprising angle |
| **Anecdotes** | None / generic | Category-specific | Named person, date, place, or detail |
| **Voice markers** | Professional tone | Some personality | Verbal tics, humor style, word choices |
| **Conclusion** | Generic CTA | Relevant takeaway | Leaves the reader changed |

**Total score < 25**: Block publication. Rewrite required.
**Total score 25-35**: Revise flagged dimensions.
**Total score 36-50**: Cleared for publication.

### Step 2 — AI Language Pattern Scan
Flag these specific AI-content markers that LinkedIn may detect:

**Structural Tells**
- [ ] Perfect parallel construction in lists (AI loves symmetry)
- [ ] Overly balanced "on one hand / on the other hand" framing
- [ ] Three-point structures with identical sentence lengths
- [ ] Conclusions that perfectly summarize all points made

**Vocabulary Tells**
- [ ] "Landscape" / "Navigate" / "Leverage" / "Robust" / "Tapestry"
- [ ] "In today's fast-paced world" or similar throat-clearing
- [ ] "It's not just about X, it's about Y" (AI's favorite construction)
- [ ] Passive voice dominance

**Personality Tells**
- [ ] No humor, self-deprecation, or emotional vulnerability
- [ ] No specific numbers, dates, or named references
- [ ] No cultural references, slang, or colloquialisms
- [ ] No "wrong" grammar that real humans use intentionally

### Step 3 — Human Voice Injection Protocol
For any flagged content, apply Jensen's authenticity injection sequence:

1. **Add a specific story**: Replace one generic point with a real anecdote (named people, actual dates, specific outcomes)
2. **Break a rule**: Intentionally use a sentence fragment. Start with "And." End with "Right?"
3. **Insert personality**: Add one moment of humor, vulnerability, or unexpected opinion
4. **Create asymmetry**: Vary sentence lengths dramatically (3 words. Then twenty-seven.)
5. **Apply the flamingo test**: Where's the unexpected, personality-driven moment? (Genius Pattern 5)

### Step 4 — Final Authenticity Verdict

```
## AI Authenticity Gate — Verdict

### 50-Person Test Score: [X/50]
### AI Pattern Flags: [X items flagged]
### Voice Fidelity: [Match to author voice profile: HIGH/MEDIUM/LOW]

### Verdict: [PASS / REVISE / BLOCK]

### If REVISE — Priority Fixes:
1. [Specific fix with example rewrite]
2. [Specific fix with example rewrite]
3. [Specific fix with example rewrite]

### Authenticity Anchors Present:
- [✓/✗] Specific anecdote with named details
- [✓/✗] Personality-driven moment (humor/vulnerability/surprise)
- [✓/✗] Asymmetric sentence structure
- [✓/✗] Voice markers matching author profile
- [✓/✗] At least one "only THIS person would write this" element
```

## Output Format
Pass/Revise/Block verdict with specific fixes and example rewrites for flagged content.

## Quality Gate
- [ ] 50-Person Test scored across all 5 dimensions
- [ ] AI language patterns scanned (structural + vocabulary + personality)
- [ ] Human voice injection applied to any REVISE/BLOCK content
- [ ] Final verdict includes specific rewrite examples, not just flags
- [ ] Author voice profile referenced (not generic "add personality")
