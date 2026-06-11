# Remaining Skills Upgrade & System Sync — Plan

## Scope

| Category | Count | Action |
|----------|-------|--------|
| Rich genius.md (has patterns/identity) | 120 | Auto-generate DF + AP + VD sections |
| Partial genius.md | 5 | Auto-generate with fallback template |
| Stub genius.md (empty/minimal) | 9 | Lightweight template from SKILL.md |
| Already upgraded (need workflow harmony) | 4 | Workflow injection only |
| Utility skills (no genius.md) | 29 | Skip — not expert skills |
| **Total workflows to harmonize** | **~584** | |

---

## Phase 1: Genius.md Auto-Upgrade (134 skills)

Build a Python script that reads each genius.md and:

1. **Decision Framework** — Extracts expert's domain → generates 4-5 diagnostic questions: "When to use this expert vs. alternatives"
2. **Anti-Patterns** — Scans Genius Patterns for the inverse → generates 5-7 "would-never-do" rules
3. **Voice DNA** — Extracts voice characteristics from existing "Voice & Style" or "Operating Philosophy" sections → generates structured voice profile

For **stubs** (9 skills): generate minimal DF/AP/VD from SKILL.md metadata (domain, produces, expert name).

## Phase 2: Workflow Harmony Injection (~584 workflows)

Reuse the same injection script from Tier 1 — Pre-Flight Gate + Anti-Pattern Guard. Already proven on 63 workflows, scales to 584.

Then run the duplicate Quality Gate merge script.

## Phase 3: System Routing Sync

### `invocation-cards.md` — Add upgrade status

Append to each agent card:
```
UPGRADE: ✅ (genius.md v2 — Decision Framework + Anti-Patterns + Voice DNA)
```

### `DOMAIN_REGISTRY.md` — Add tier metadata

Add a note at the top flagging which experts are fully upgraded.

### SKILL.md Cross-References

Same pattern as Tier 1 — add DF/AP/VD links to Quick Reference section.

## Execution Order

1. Phase 1 script (auto-gen DF/AP/VD) → verify samples → run on all 134
2. Phase 2 script (workflow harmony) → verify → merge duplicates  
3. Phase 3 (system sync) → invocation cards → domain registry → SKILL.md refs
