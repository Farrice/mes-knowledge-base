# Source Ledger — marketing-studio-director

Wave 3 Lane 4 Batch 11 repair. This skill is a TOOL/SYSTEM skill (Higgsfield Marketing
Studio prompt director) — there is no person-expert transcript to ground against. Ground
truth = the skill's own in-repo files, which document the actual Higgsfield Marketing
Studio product interface. Confirmed absence of any extraction source (not assumed):

```
$ ls extractions/ | grep -i higgsfield   → no output
$ ls extractions/ | grep -i "marketing.studio"  → no output
```

No `extractions/` directory exists for this expert/tool. Every source below is a file
that already lived inside `skills/marketing-studio-director/` before this repair.

## Sources Consulted (file + size, `wc -c`)

| # | File | Size (bytes) | Label | Notes |
|---|------|--------------|-------|-------|
| 1 | `skills/marketing-studio-director/SKILL.md` | 20,405 | VERIFIED | Primary source; read in full. All quotes in genius.md and workflows/ are verbatim from this file. |
| 2 | `skills/marketing-studio-director/references/genius-patterns.md` | 1,808 | VERIFIED | Read in full (27 lines). Source for the 5 Genius Patterns migrated into genius.md. |
| 3 | `skills/marketing-studio-director/references/hidden-knowledge.md` | 546 | VERIFIED | Read in full (11 lines). Small file — confirmed non-empty and fully read, not truncated. Source for "reference drift" quote and the Hidden Knowledge section. |
| 4 | `skills/marketing-studio-director/references/prompts-v2/ugc-ad-prompt.md` | 13,359 | VERIFIED | Read in full. Frontmatter: `standard: structure-pure-v2`, `refactored: 2026-07-13`. Already carries Output Contract + Quality Gate. |
| 5 | `skills/marketing-studio-director/references/prompts-v2/tv-spot-ad-prompt.md` | 13,524 | VERIFIED | `grep`-confirmed: `refactored: 2026-07-13`, age-marker trigger-word list present verbatim, `## Output Contract` + `## Quality Gate` headings present. |
| 6 | `skills/marketing-studio-director/references/prompts-v2/hyper-motion-ad-prompt.md` | 13,583 | VERIFIED | Same `grep` confirmation as #5. |
| 7 | `skills/marketing-studio-director/references/prompts-v2/pro-virtual-try-on-prompt.md` | 13,184 | VERIFIED | Same `grep` confirmation as #5. |
| 8 | `skills/marketing-studio-director/references/prompts-v2/product-review-ad-prompt.md` | 13,083 | VERIFIED | Same `grep` confirmation as #5. |
| 9 | `skills/marketing-studio-director/references/prompts-v2/tutorial-ad-prompt.md` | 12,963 | VERIFIED | Same `grep` confirmation as #5. |
| 10 | `skills/marketing-studio-director/references/prompts-v2/ugc-virtual-try-on-prompt.md` | 13,304 | VERIFIED | Same `grep` confirmation as #5. |
| 11 | `skills/marketing-studio-director/references/prompts-v2/unboxing-ad-prompt.md` | 12,939 | VERIFIED | Same `grep` confirmation as #5. |
| 12 | `skills/marketing-studio-director/references/prompts-v2/wild-card-ad-prompt.md` | 13,189 | VERIFIED | Same `grep` confirmation as #5. |

## Claim-by-Claim

- **"9 Marketing Studio presets"** — VERIFIED. Counted directly from SKILL.md's Preset Router table (UGC, Tutorial, Unboxing, Hyper Motion, Product Review, TV Spot, Wild Card, UGC Virtual Try On, Pro Virtual Try On = 9 rows) and confirmed against the 9 files present in `references/prompts-v2/`.
- **"Never restyle or 'improve' the product"** — VERIFIED. Verbatim string search-confirmed inside SKILL.md's Engine Rules section.
- **"Trigger words to avoid: boy, girl, child, kid, young, teen, little"** — VERIFIED. `grep -c` confirmed the exact string present once in each of the 9 `prompts-v2/*.md` files (all 9 returned `1`), plus SKILL.md's Age-blind character rule.
- **"reference drift"** — VERIFIED. Verbatim term from `hidden-knowledge.md`'s Failure Mode section.
- **"refactored: 2026-07-13"** — VERIFIED. `grep` confirmed this exact frontmatter line present in all 9 `prompts-v2/*.md` files, not just `ugc-ad-prompt.md`.
- **Antislop banned-word list (40+ terms)** — VERIFIED. Counted directly from SKILL.md's Antislop section.
- **Higgsfield Marketing Studio generation link** (`https://higgsfield.ai/s/general-higgsfieldai-vKnfpx`) — UNCONFIRMED as a live/current URL. This repair does not call the URL or verify it resolves; it is reproduced only because it already exists verbatim in SKILL.md and the workflow files, and this repair does not alter model routing, cost references, or product links per the binding contract. No claim is made about the URL's current validity.
- **Any claim about who built or maintains Higgsfield Marketing Studio, or its non-documented internal model architecture** — UNCONFIRMED / not claimed anywhere in this repair. No such claim appears in genius.md or the workflow files; this line exists to make the absence explicit rather than silent.

## What Was NOT Done

No web search, no Higgsfield product documentation outside this repo, and no MCP tool call
to the live `Higgsfield` connector was used to ground this repair — everything above is
sourced from files that already existed in `skills/marketing-studio-director/` prior to
this repair pass. This is a deliberate scope limit (additive-first, never alter prompts,
model routing, or cost references), not an oversight.
