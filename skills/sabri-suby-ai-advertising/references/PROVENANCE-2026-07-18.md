# Provenance — sabri-suby-ai-advertising repair (Wave 3 Lane 4 Batch 14)

| Anchor / addition | Location in modified genius.md | Source file + location | Status |
|---|---|---|---|
| "Social Proof Deletion Protocol" anti-pattern | Anti-Patterns §, bullet 1 | `skills/sabri-suby-ai-advertising/references/hidden-knowledge.md` §7 | UNCONFIRMED (Suby attribution) |
| "Assemble, Don't Create" anti-pattern | Anti-Patterns §, bullet 2 | `skills/sabri-suby-ai-advertising/references/hidden-knowledge.md` §6 | UNCONFIRMED |
| "SaaS vs. Service Decision" anti-pattern | Anti-Patterns §, bullet 3 | `skills/sabri-suby-ai-advertising/references/hidden-knowledge.md` §2 | UNCONFIRMED |
| "Inverse Competition" anti-pattern | Anti-Patterns §, bullet 4 | `skills/sabri-suby-ai-advertising/genius.md` Pattern 1 (pre-existing) | UNCONFIRMED |
| Generic "Solution" Ad anti-pattern | Anti-Patterns §, bullet 5 | `skills/sabri-suby-ai-advertising/genius.md` Hall of Fame Anti-Exemplar (pre-existing) | UNCONFIRMED |
| "Defensive Permeability Calibration" anti-pattern | Anti-Patterns §, bullet 6 | `skills/sabri-suby-ai-advertising/genius.md` Evolution Log row, date 2026-04-09 (pre-existing) | Date/artifact VERIFIED; Suby-attribution UNCONFIRMED |
| "Small Batch Testing" anti-pattern | Anti-Patterns §, bullet 7 | `skills/sabri-suby-ai-advertising/genius.md` Pattern 15 (pre-existing) | UNCONFIRMED |
| Recognition-test line | "How to Use This Skill (Model Calibration)" § | New, written for this repair against the skill's existing Pattern 10 ("Doesn't Look Like An Ad") and the Ad Library / competitor-shopping motifs already present in genius.md | Original text, not a factual claim |
| 10 entity-floor "Cross-Reference" additions (Patterns 5,6,7,8,9,10,11,12; Hidden Knowledge #5,#7) | Inline, under each Pattern's Success Metric | All entities reused from elsewhere in the same `genius.md` (Pattern 1's "50+/<20" thresholds, Hidden Knowledge #1/#3 dollar figures, Hall of Fame Exemplar 1 and 2 quotes) — no new facts introduced | Same status as the section they cross-reference |

## Source-search log (see references/source-ledger.md for full detail)

1. `ls extractions/ | grep -i sabri` / `grep -i suby` → 0 hits (only unrelated `extractions/sabrina-ramonov`).
2. `find extractions -iname "*suby*" -o -iname "*sabri*"` → 0 hits.
3. Python `tarfile` scan of all `.tar.gz`/`.tar` archives repo-wide for member names matching "suby"/"sabri" → 0 hits.
4. Repo grep for "sabri suby" / "kingkong" / "sell like crazy" → hits only in other skills/agents/commands that reference this skill by name; no primary transcript found.
5. Checked `research_outputs/ai_authority_architect_agents/sabri_suby.md` (2,590 bytes) — off-topic (ghostwriter-fatigue market research, not Suby's own content) and already self-flagged `[MODELED]`/unsourced in its own 2026-06-02 grounding addendum. Not used.
6. Checked `agents/sabri-suby/AGENT.md` (79 lines) and `skills/sabri-suby-ai-advertising/SKILL.md.old` (109 lines) — both downstream restatements, no independent provenance.

No fabricated anchors: every UNCONFIRMED label above reflects an actual absence confirmed by the searches listed, not an unread gap.
