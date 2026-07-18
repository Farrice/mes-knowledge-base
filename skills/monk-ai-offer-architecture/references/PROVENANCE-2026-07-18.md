# Provenance — monk-ai-offer-architecture repair (Wave 3 Lane 4 Batch 11)

Anchor → source file + location. All sources are internal to
`skills/monk-ai-offer-architecture/` (repo root:
`/Users/farricecain/Google Antigravity`) — no `extractions/` directory or
external source exists for "Monk.Ai" (see `references/source-ledger.md` for
the search trail).

| Anchor (in repaired `genius.md`) | Source file + line | Verbatim? |
|---|---|---|
| Pattern 3 Grounding — "a well-designed audit makes implementation feel inevitable, not optional" | `references/prompts-v2/audit-implementation-bridge.md:16` | Yes, character-checked |
| Pattern 4 Grounding — "Price is relative, and where you anchor determines how everything else is perceived" | `references/prompts-v2/value-anchor-pricing.md:16` | Yes |
| Pattern 5 Grounding — "Resistance to the primary offer doesn't mean resistance to working together — it means the trust-to-ask ratio is misaligned" | `references/prompts-v2/downsell-recovery-scripts.md:16` | Yes |
| Pattern 6 Grounding — "Every month starts at $0" | `references/prompts-v2/pipeline-compound-architecture.md:35` | Yes |
| Pattern 7 Grounding — "The final pitch should be a CONFIRMATION ceremony, not a persuasion event" | `references/prompts-v2/stakeholder-presell-orchestrator.md:16` | Yes |
| Anti-Pattern 1 — "The consultant, having no smaller offer, reduces the price by 20% but still requires a full commitment" | `genius.md`, pre-existing Anti-Exemplar section (this file, unedited) | Yes — already present before this repair pass |
| Anti-Pattern 2 — "Forcing the wrong offer on the wrong buyer type kills deals" | `references/prompts-v2/buyer-type-qualifier.md:16` | Yes |
| Anti-Pattern 3 — "Resistance to the primary offer doesn't mean resistance to working together — it means the trust-to-ask ratio is misaligned" | `references/prompts-v2/downsell-recovery-scripts.md:16` | Yes (same quote reused as both a Grounding line and an Anti-Pattern anchor — same file) |
| Anti-Pattern 4 — "Bad Moments (don't ask here): When they're frustrated" | `references/prompts-v2/referral-trigger-system.md:39-40` | Yes |
| Anti-Pattern 5 — "The final pitch should be a CONFIRMATION ceremony, not a persuasion event" | `references/prompts-v2/stakeholder-presell-orchestrator.md:16` | Yes (same quote as Pattern 7 Grounding) |
| `refactored: 2026-07-11` date used on every Anti-Pattern citation | Frontmatter of each `references/prompts-v2/*.md` file cited above | Yes — checked in each file's own YAML header |
| "$600K+ revenue track record" / "Pioneer of the Offer Pyramid system" | No source — UNCONFIRMED, labeled as such in both `genius.md` and `references/source-ledger.md` | N/A — explicitly not claimed as verified |

## Search performed before any UNCONFIRMED label was written

1. `ls extractions/ | grep -i monk` — 0 results (193 dirs scanned).
2. `find . -iname "*monk*" -not -path "./.git/*"` — repo-wide, no external
   source found; only this skill's own files and generated indexes/logs
   that reference it.
3. `find . -iname "*.tar*" -not -path "./.git/*"` — checked for an archived
   extraction bundle that might contain Monk.Ai source material; none
   exists (only unrelated tarballs: `claude-export`, `shadcn-components`,
   Python venv artifacts).
4. `wc -c` on every file under `skills/monk-ai-offer-architecture/` —
   confirmed no 0-byte or truncated files (59 files, 2,843–13,239 bytes
   each) before concluding the absence of a source is real, not a read
   failure.
