# Token Optimization: Slash Command Trimming + Genius.md Refactoring

## Goal

Reduce per-message and per-expert token consumption without losing any knowledge, expertise, depth, or system capability. Zero quality downgrade.

---

## Phase 1: Slash Command Description Trimming

### Problem
Every message loads all 399 workflow descriptions from YAML frontmatter. Current total: **6,666 words ≈ 8,888 tokens per message**.

### Solution
Build a Python script (`execution/trim_descriptions.py`) that:
1. Reads each `.agent/workflows/*.md` file
2. Extracts the current `description:` from YAML frontmatter
3. Trims it to **8 words max** — a tight imperative phrase
4. Writes the trimmed description back
5. Saves a full backup (`description_backup.json`) with every original description preserved

### Trimming Rules
- Keep the **verb + core action + target** (e.g., "Build a complete brand foundation" → "Build brand foundation with Nike methodology")
- Strip attribution clauses ("using X's framework", "Diandra Escobar's methodology fully operationalized")
- Strip elaboration ("with hook variants, body copy, and CTA")
- Strip platform lists ("YouTube, LinkedIn, Instagram, articles...")
- Preserve the ONE thing that makes the workflow unique

### Quality Safeguard
- **Full backup**: Every original description stored in `execution/description_backup.json`
- **Rollback script**: Can restore all originals with one command
- **Routing test**: After trimming, verify routing still works by spot-checking 20 workflows — does the trimmed description still clearly indicate what the command does?

### Expected Savings
- Before: ~8,888 tokens/message
- After: ~3,200 tokens/message (8 words × 399 workflows ÷ 0.75 words/token)
- **Savings: ~5,600 tokens per message** (63% reduction in workflow index cost)

---

## Phase 2: Genius.md Size Refactoring

### Problem
27 genius.md files exceed 50KB (range: 53KB–149KB). A Tier 2 load of the largest expert costs ~37,000 tokens just for genius.md.

### Solution — NOT Implemented This Session

> [!IMPORTANT]
> Genius.md refactoring is **deferred**. Here's why:

1. **Risk/reward**: Each genius.md is a hand-crafted expert codification. Splitting them risks breaking the narrative coherence that makes them effective. This requires per-file creative judgment, not batch processing.
2. **Impact is per-expert, not per-message**: Unlike descriptions (which cost tokens on every message), genius.md only costs tokens when that specific expert is loaded at Tier 2+.
3. **Behavioral mitigation exists**: Using Tier 1 (SKILL.md only) instead of Tier 2 for routine tasks already avoids the genius.md cost entirely.
4. **Recommendation**: Schedule this as a dedicated session where we audit each of the 27 oversized files individually, deciding what's core vs. reference material. Not a batch script — a quality-controlled editorial pass.

### The 27 Files That Would Be Candidates (for future reference)

| File | Size | Expert |
|------|------|--------|
| nicolas-cole-niche-positioning/genius.md | 149KB | Nicolas Cole |
| nba-betting-edge/genius.md | 128KB | NBA Betting |
| luke-iha-copy-blocks/genius.md | 127KB | Luke Iha |
| dan-wang-literary-analysis/genius.md | 126KB | Dan Wang |
| tommy-clark-linkedin-growth/genius.md | 123KB | Tommy Clark |
| dr-kriukow-humanization/genius.md | 122KB | Dr. Kriukow |
| jeremy-miner-identity-persuasion/genius.md | 112KB | Jeremy Miner |
| fresh-voice-system/genius.md | 110KB | Fresh Voice |
| shan-hanif-audience-monetization/genius.md | 109KB | Shan Hanif |
| seth-godin-ideavirus/genius.md | 108KB | Seth Godin |
| + 17 more (53–104KB each) | | |

---

## Execution Plan (This Session)

### Step 1: Build the trimming script
#### [NEW] [trim_descriptions.py](file:///Users/farricecain/Google%20Antigravity/execution/trim_descriptions.py)
- Reads all workflow files
- Backs up all original descriptions
- Applies 8-word-max trimming using intelligent compression
- Writes trimmed descriptions back to files
- Outputs a before/after comparison report

### Step 2: Review + execute
- Run script in dry-run mode first (report only, no writes)
- Review the before/after report for quality
- Execute with writes
- Spot-check 20 workflows for routing clarity

### Step 3: Verify + commit
- Confirm all 399 workflows still have valid YAML frontmatter
- Run file count verification
- Commit and push

---

## Verification Plan

### Pre-Flight
- [ ] Backup all original descriptions to JSON
- [ ] Dry-run produces clean before/after report

### Post-Trim
- [ ] All 399 files still parse valid YAML
- [ ] Spot-check: 20 random workflows have clear, routing-sufficient descriptions
- [ ] No workflow lost its description entirely
- [ ] Backup file exists and is complete

### Quality Gate
**If any trimmed description is ambiguous about what the workflow does**, the original is restored for that specific file. We optimize for clarity, not minimum word count.
