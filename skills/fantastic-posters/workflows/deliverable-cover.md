# Workflow: Client Deliverable Cover Frame

> **Use**: Strategy briefs, council reports, expert extraction packages, McKinsey-grade strategic dossiers
> **Default quality**: `high` ($0.17/image) — client-facing, premium signal required
> **Bound to**: `strategy_briefs/`, `councils/`, `extractions/`, `deliverables/` outputs

## Native-Fit Styles

| Style ID | When |
|---|---|
| `corporate-report` | McKinsey-grade strategic dossiers, business intelligence |
| `swiss-minimal-typo` | Frameworks, methodology breakdowns, IP packaging |
| `editorial-fashion` | Premium personality-led briefs (founder profiles, brand audits) |
| `minimal-tech-keynote` | Tech council reports, AI brain build deliverables |
| `tech-conf-darkmode` | Modern dark-themed briefs (memory architecture, agentic workflows) |
| `saul-bass-minimal` | Iconic, mark-driven covers (manifesto-style deliverables) |
| `art-deco` | Premium positioning briefs, luxury-brand work |

## Brief Construction (MUST include)

Every deliverable cover brief should contain:
1. **The deliverable's central thesis in one line** (NOT the title — the *idea*)
2. **The audience** (executives, founders, CMOs, etc.)
3. **The mood** (urgent / authoritative / contemplative / provocative)
4. **One concrete visual anchor** (a metaphor, an object, a geometric form)

Example:

> "Cover for strategic brief on AI memory architecture for solo founders. Audience: technical CEOs.
> Mood: authoritative, contemplative. Visual anchor: layered translucent planes intersecting at sharp angles,
> deep navy and warm gold accents, no people."

## Standard Run

```bash
# 1. Pre-flight (single high-quality cover)
python3 execution/fal_budget_guard.py check --quality=high --n=1

# 2. Generate
cd "/Users/farricecain/Google Antigravity/skills/fantastic-posters/" && \
  ./gen.sh "<brief above>" \
    --style=corporate-report \
    --quality=high \
    --size=portrait

# 3. Log
python3 execution/fal_budget_guard.py log --quality=high --n=1 --status=success --style=corporate-report
# Cost: $0.17
```

## When to Explore First (cheaper)

If you're unsure which style fits the brief, do a low-quality 3-variant pass first:

```bash
# $0.033 to find the right style
python3 execution/fal_budget_guard.py check --quality=low --n=3
./gen.sh "<brief>" --n=3 --quality=low
python3 execution/fal_budget_guard.py log --quality=low --n=3 --status=success

# Then $0.17 to render the winner at high quality
python3 execution/fal_budget_guard.py check --quality=high --n=1
./gen.sh "<same brief>" --style=<winner> --quality=high
python3 execution/fal_budget_guard.py log --quality=high --n=1 --status=success

# Total: $0.20 per deliverable cover
```

## Output Pipeline

1. Cover lands in `skills/fantastic-posters/out/`
2. Move to deliverable folder: `strategy_briefs/[brief-slug]/cover.png` (or `councils/`, `extractions/`, etc.)
3. If deliverable goes to Google Docs: insert as page 1 image (full-bleed)
4. If deliverable goes to PDF: use as cover page

## Cost Envelope

- **Standard cover (no exploration)**: $0.17
- **With exploration**: $0.20
- **Reasonable monthly cap for client work**: 5-10 covers = $1.00-$2.00

## Anti-Patterns

- ❌ Generic stock-art aesthetics (defeats the purpose — users have seen 1M of those)
- ❌ Putting the deliverable's literal title on the cover via prompt (typography is unreliable; use Canva post-gen)
- ❌ Recognizable real people in covers (likeness issues + GPT Image 2 will distort)
- ❌ Using `medium` for client-facing deliverables (the quality gap is visible at print/screen)
- ✅ Use the cover to signal the *category* of thinking, not summarize the content

## Output Schema

Each cover run produces one **Cover Generation Record** — the artifact a reviewer checks before the cover ships with a deliverable:

```markdown
## Cover — <deliverable slug>
- Style used: <style-id from Native-Fit Styles table> · Quality: high ($0.17) [+ exploration $0.033 × 3 if run]
- Brief (thesis · audience · mood · visual anchor): "<the four required lines>"
- Pre-flight: `fal_budget_guard.py check --quality=high --n=1` → <approved/denied>
- Output file: `skills/fantastic-posters/out/<file>.png` → moved to `<strategy_briefs|councils|extractions|deliverables>/<slug>/cover.png`
- Post-flight log: `fal_budget_guard.py log --quality=high --n=1 --status=success --style=<id>` ✓
- Total spend: $0.17 (or $0.20 with exploration)
```

Complete only when every field is filled and the log line shows `--status=success`.

## Quality Gate

- [ ] **Brief carries all four required elements** — thesis (not title), audience, mood, one concrete visual anchor. A brief missing any one produces a stock-art cover.
- [ ] **Style matches Native-Fit table intent** — not the auto-picker's first keyword hit; a deliberate pick for the deliverable's register.
- [ ] **`--quality=high` for anything client-facing** — `medium` is an anti-pattern here; the quality gap is visible at print/screen.
- [ ] **No literal deliverable title baked into the prompt** — GPT Image 2 typography is unreliable for a full title; add text in Canva post-gen.
- [ ] **No recognizable real person** — likeness risk + distortion risk both apply.
- [ ] **Pre-flight ran before generation, post-flight log ran after** — `fal_budget_guard.py check` → generate → `fal_budget_guard.py log`, in that order, every time.

**Pass criteria**: all checked. A cover that "looks premium" but skips the pre-flight/log pair or bakes in a literal title fails this gate regardless of how it renders.
