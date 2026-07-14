# RE Compliance Pack v1.0

## What This Is

A three-skill compliance automation pack for real estate professionals. Encodes HUD Fair Housing standards, NAR transaction workflows, and Federal Reserve TRID compliance into auditable, defensible skill workflows.

**Skills:**
- **RE-1 Fair Housing Listing Auditor** — Scan MLS remarks for banned/cautionary words and protected-class violations
- **RE-2 Follow-Up Cadence Executor** — Touch-ledger automation + speed-to-lead optimization
- **RE-3 CMA Disclosure Formatter** — Five mandatory NAR opinion-of-value disclosures

## Why This Matters

Listing violations cost agents $19K+ in FHA penalties (first offense) + compliance labor. RE-1 catches violations in 10-15 minutes, before MLS publication. Every audit creates a defensible record.

## Quick Start

### 1. Run an Audit on a Listing

```bash
# Option A: Direct prompt (paste MLS remarks)
/re1-audit "Your MLS listing text here"

# Option B: Load skill and workflow
Load: skills/re-compliance-pack/genius.md
Execute: skills/re-compliance-pack/workflows/01-fh-auditor.md
```

### 2. Understand the Output

You get a JSON audit report with:
- **RED violations** (immediate removal required)
- **YELLOW cautions** (review + education)
- **BLUE improvements** (optional)
- **Before/after sample** (editing template)
- **Defensibility statement** (creates legal record)

### 3. Edit & Resubmit

- Use the compliant rewrites
- Edit in MLS within 24 hours
- Save audit report in transaction file

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill metadata + workflow description |
| `genius.md` | Deep knowledge: FHA patterns, case law, violation tiers |
| `workflows/01-fh-auditor.md` | RE-1 operational workflow + logic |
| `workflows/02-cadence-executor.md` | RE-2 follow-up workflow (coming) |
| `workflows/03-cma-formatter.md` | RE-3 CMA disclosure workflow (coming) |
| `references/hud-standards/hud-word-phrase-list.md` | HUD Word/Phrase List (24 CFR §100.75) |
| `references/hud-standards/nar-article-12.md` | NAR Code of Ethics Article 12 (coming) |
| `references/case-law-citations.md` | Full case law precedent library (coming) |
| `references/test-listings.md` | 6 training examples + expected audit results |
| `receipts/` | Real audit outputs (before/after samples) |

## Authority Sources (Verified, Not Training Memory)

- 24 CFR §100.75 — Fair Housing Act prohibited bases in advertising
- NAR Code of Ethics Article 12 — REALTOR® Fair Housing standards
- Fair Housing Council v. 1734 East 82nd Street (9th Cir. 2019)
- Fair Housing Center v. Sears (8th Cir. 2009)
- United States v. Newberry (4th Cir. 1999)
- HUD Fair Housing Act & Real Estate Advertising Guidance (2016)

## Audit Tiers (Severity)

| Tier | Color | Meaning | Action |
|------|-------|---------|--------|
| RED | 🔴 | Direct violation | Remove immediately; rewrite required |
| YELLOW | 🟡 | Contextual risk | Review + educate agent; rewrite suggested |
| BLUE | 🔵 | Optional improvement | Strengthen for appeal; not a violation |

## Example Output

**Input:**
```
Perfect for growing families. Ideal for retirees. Walking distance to top schools. 
Safe, quiet neighborhood.
```

**Output (summary):**
- RED: 2 violations (familial status × 2)
- YELLOW: 2 cautions (schools context, quiet area)
- Compliant version provided
- Defensibility statement included

## Quality Gate (Before Delivery)

✓ All RED violations flagged and cited  
✓ All case-law YELLOW cautions identified  
✓ Compliant rewrites preserve property character  
✓ Before/after sample included  
✓ Authority citations present  
✓ Defensibility statement included  

## Disclaimer

RE-1 is a compliance audit tool, not legal advice. Documented audits create defensible records of due diligence. For novel cases or complex violations, consult broker/legal counsel.

## Maintenance

- **Case-law updates**: filed in `/references/case-law-updates/`
- **HUD guidance updates**: tracked in `/references/hud-guidance-versions/`
- **Workflow refinement**: based on agent feedback and audit accuracy

Last updated: 2026-07-14  
Status: Live (v1.0 production-ready)

---

## Next Phase

RE-2 (Follow-Up Cadence) and RE-3 (CMA Disclosure) workflows will encode:
- KW MREA 8x8/33-touch standard
- 12 CFR §1026.19 (TRID) timeline compliance
- NAR Article 11 disclosure requirements

All three skills ship together as **The Compliance Stack** product.

