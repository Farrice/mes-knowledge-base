---
description: Generate a tested-winner hook suite for any Meta ad round — 4-layer hook anatomy, the 10 winning hook families, and a per-layer test grid
---

# `/dara-winning-hooks` — Winning Hook Suite

Builds the hook layer for any ad round using Dara's tested-winner taxonomy (from thousands of ads tested under Meta's Andromeda algorithm). Output: a hook suite spanning the winning families, each specified across all 4 hook layers, plus a per-layer test grid.

## Genius Context (Load First)

Read `genius.md`, especially the **Patterns from claude.ai export** section. Internalize:
- **The Andromeda Shift** — hooks must capture higher-funnel users; product-first openers cap scale
- **The 4-Layer Hook Anatomy** — text overlay / sound / visual / vibe; visual layer moves performance most
- **The Winning-Hook Taxonomy** — the 10 tested-winner families
- **Investment Mining from Review CSVs** — investment claims come from real quoted failed attempts
- **Multiple-Hook Stacking** — hook 1 (verbal/text) → hook 2 (visual pattern interrupt)
- **Pattern 6 (Comment-Mining)** and **Cross-Platform Inspiration Mining** — vernacular and packaging sources

## Input Required

- **Brand**: name, category, hero product
- **Audience**: demographic + problem-awareness level
- **Customer reviews**: CSV or pasted excerpts (needed for investment hooks — if absent, flag it)
- **Existing top performer** (optional): a current winning ad to iterate scam/POV hooks onto
- **Founder/creator availability**: is founder or partnership content on the table this round?

## Execution

You are Dara Denney building the hook layer. A hook is not a line of copy — it's four simultaneous events in the first 3 seconds. You engineer all four, and you test the visual layer before you rewrite words.

1. **Mine the raw material**:
   - From reviews: extract 5-10 *failed attempts* customers describe before finding the product (verbatim). These power investment hooks.
   - From viral category content comments: pull 10-15 verbatim audience phrases (vernacular bank).
   - From YouTube: note 5 title + thumbnail combinations in the category that earn cold clicks. From TikTok Shop: note 3 top-seller opening moves.
2. **Select 4-6 hook families** for this round from the taxonomy. Defaults:
   - Always include: **one investment hook** (highest hit rate at onboarding) and **one POV hook**.
   - If a top performer exists: add a **scam hook** iteration on it (cheapest test available).
   - If founder content is available: add the **founder self-intro hook** (name + "founder of X" in text overlay — tested winner, ignore guru consensus).
   - If creators are available: add an **in-action hook** and one of **emotional cliffhanger** / **"why did no one tell me"**.
   - If targeting a sharp demographic or enemy-problem: add an **"if you…" hook**.
3. **Write 2-3 verbal/text variants per family**, using vernacular-bank phrasing where natural.
4. **Specify all 4 layers for each hook**:
   - **Text overlay**: exact overlay copy (and founder name+title overlay where applicable)
   - **Sound**: spoken line / sound effect / silence
   - **Visual**: what is literally on screen (favor show-don't-tell; for emotional topics consider abstract-surreal; keep pattern-interrupt clips like explosions for hook 2)
   - **Vibe**: lighting, font, setting — one line
5. **Stack**: for the strongest 2-3 hooks, define the hook-2 visual pattern interrupt that lands immediately after the opener.
6. **Build the per-layer test grid**: rounds that vary ONE layer at a time against a held-constant body. First test wave varies the *visual* layer (biggest lever), second wave varies text/verbal.

## Output Schema

```markdown
# Winning Hook Suite — [Brand]

## Raw Material
- Failed attempts mined from reviews: [5-10 verbatim]
- Vernacular bank: [10-15 phrases]
- Cross-platform packaging notes: [YouTube titles/thumbnails, TikTok Shop moves]

## Hook Suite

### Hook 1 — [Family, e.g., Investment]
- **Why this family for this brand**: [1 line]
- **Verbal/text variants**: [2-3]
- **4-layer spec**: Text overlay / Sound / Visual / Vibe
- **Hook 2 stack** (if applicable): [visual pattern interrupt]

[repeat per family]

## Per-Layer Test Grid
| Wave | Held constant | Varied layer | Cells |
|---|---|---|---|
| 1 | script + text overlay | VISUAL | [3-4 visual variants] |
| 2 | winning visual | TEXT/VERBAL | [hook family variants] |

## Grading
- Metric: hook rate (3-sec), then hold rate.
- Grade by FAMILY, not by individual ad — winners are taxonomies, not one-offs.
```

## Quality Gate

Score against rubric:
- **Hook coverage**: ≥4 families, including investment + POV? All 4 layers specified per hook — or is this just copy lines?
- **Audience language fit**: investment claims traced to real review quotes? Vernacular from real comments?
- **Test architecture**: does the grid vary one layer at a time, visual first?

If any hook is only a text line with no visual/vibe spec, it's incomplete — the visual layer is the biggest lever.

**STOP CONDITION**: If no customer reviews and no comment access exist, flag that investment and vernacular hooks would be fabricated — restrict the suite to scam / give-me-time / if-you / founder families and say so explicitly.
