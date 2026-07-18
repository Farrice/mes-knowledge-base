# Source Ledger — monk-ai-offer-architecture

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 11). Ground-truth search performed
per envelope discipline before any UNCONFIRMED label was applied:

- `ls extractions/ | grep -i monk` → **no match** (193 extraction dirs total,
  none for Monk.Ai). Confirmed again with fragment searches (`monk`, `ai
  offer`, `offer pyramid`) — no hit.
- `find . -iname "*monk*"` (repo-wide, excluding `.git` and worktree
  mirrors) → only this skill's own files, its `agents/monk-ai/` persona
  shell, generated indexes (`SKILL_INDEX.md`, `DOMAIN_REGISTRY.md`,
  `.claude/commands/monk-ai*.md`), swarm-output logs that *invoke* this
  skill, and one downstream reference in `_active/parallax-icp-offer/` that
  cites the skill's framework, not an external Monk.Ai source.
- `find . -iname "*.tar*"` (repo-wide) checked for a possible archived
  extraction bundle — the only tarballs present are unrelated
  (`claude-export`, `shadcn-components`, Python venv artifacts). No Monk.Ai
  archive exists to open with `tarfile`.
- File-size check on every file in `skills/monk-ai-offer-architecture/`
  (`wc -c`, run before writing this ledger): all 59 files are non-empty,
  ranging 2,843–13,239 bytes. Nothing is a stub or 0-byte placeholder — the
  content is real and internally authored, not a broken/truncated
  extraction.

**Conclusion**: this skill has no `extractions/` source, no interview
transcript, no external verification that "Monk.Ai" is a real, named
practitioner. It reads as an in-house-authored AI-consulting offer-design
system (originally a 17-prompt pack — see `SKILL.md.old` — later refactored
into `structure-pure-v2` workflow files dated `2026-07-11`). That refactor
history is real and verifiable; the underlying "expert" identity and track
record are not.

## Claim-by-Claim

| Claim | Label | Basis |
|---|---|---|
| "Monk.Ai — $600K+ revenue track record" (`genius.md`, Expert Profile) | **UNCONFIRMED** | No extraction, no external source of any kind found. House framing only — flagged in `genius.md` Expert Profile and Model Calibration section. |
| "Pioneer of the 'Offer Pyramid' system" (`genius.md`, Expert Profile) | **UNCONFIRMED** | Same — no external corroboration. The Offer Pyramid concept is documented only inside this skill's own files. |
| The 7 numbered patterns (Offer Pyramid Logic, First Yes Psychology, Scope Creation, Trust Gradient, Downsell-as-Value, Compound Pipeline, Stakeholder Pre-Selling) | **LIKELY** | Not externally verified as *Monk.Ai's* patterns specifically, but internally consistent and directly grounded in verbatim language from this skill's own `references/prompts-v2/*.md` files (dated `refactored: 2026-07-11`) — see the "Grounding" lines added under Patterns 3–7 in `genius.md`, each with a file+line citation. Treat as a real, usable design system; do not attribute it to a named public figure in client-facing work. |
| Hall of Fame Exemplars ("AI Readiness Audit Funnel," "Pilot-to-Platform Ascension," the healthcare Anti-Exemplar) | **UNCONFIRMED as case studies** | These are illustrative composites (fictional company names, round dollar figures: $3,500 / $45,000 / $90,000 / $750,000 / $200,000 / $15,000) written to demonstrate the patterns, not documented real client engagements. No client names, dates, or outside corroboration exist anywhere in the repo. Safe to use as *teaching exemplars*; never present as verified case studies to a client. |
| The 5 anti-patterns added in this repair pass (`genius.md`, Anti-Patterns section) | **VERIFIED (as verbatim quotes from the skill's own reference files)** | Each quote checked character-for-character against its cited file+line: `buyer-type-qualifier.md:16`, `downsell-recovery-scripts.md:16`, `referral-trigger-system.md:39-40`, `stakeholder-presell-orchestrator.md:16`, plus the pre-existing Anti-Exemplar prose already in `genius.md`. VERIFIED means "matches the internal source file verbatim" — it does **not** mean these are externally attributed to a real person named Monk.Ai. |
| The four Grounding quotes added to Patterns 3–4–5–6–7 | **VERIFIED (verbatim, internal)** | Same standard — checked against `audit-implementation-bridge.md:16`, `value-anchor-pricing.md:16`, `downsell-recovery-scripts.md:16`, `pipeline-compound-architecture.md:35`, `stakeholder-presell-orchestrator.md:16`. |
| Evolution Log entry, 2026-04-09 (Decision Architecture Layer) | **VERIFIED (internal record)** | Pre-existing in `genius.md`; not touched this pass. Documents an in-system A/B result, not an external claim. |
| Workflow files' Output Schema / Quality Gate contracts | **VERIFIED (internal, pre-existing)** | Passing check before and after this repair; not modified. |

## What this means for downstream use

Nothing in this skill should be presented to a client as "Monk.Ai says" or
"per Monk.Ai's track record" without disclosing that the identity and
revenue claim are unconfirmed. The *system* (offer pyramid, trust-gradient
pricing, downsell-as-value-creation) is real, internally coherent, and
usable — it is just not traceable to a verified external practitioner.
