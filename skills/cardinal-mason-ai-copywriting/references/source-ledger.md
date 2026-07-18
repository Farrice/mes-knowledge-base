# Cardinal Mason - AI Copywriting Mastery — Source Ledger

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 3). This ledger documents every source
checked for this skill and labels every claim VERIFIED / LIKELY / UNCONFIRMED per
the skill-craft standard. It does not re-litigate content that was already in the
skill before this repair — it makes that content's provenance auditable.

## Sources checked this repair

- **`extractions/` (repo root, 193 entries)** — full directory listing read;
  `ls extractions/ | grep -i "cardinal\|mason"` run against the whole tree,
  **zero matches** (exit code 1, confirmed by directly querying the listing, not
  inferred). No `extractions/cardinal-mason*` folder exists in this repo.
- **`knowledge/extractions/inbox/`** — repo-wide `find . -iname "*cardinal*"`
  surfaced three real primary-source files here that the skill's own
  `references/` never cited:
  - `Claude-✍️ 💎💰 Cardinal Mason ! FREE AI Copywriting Course ! How to make $500k!year in 2026.md`
    — 391,128 bytes (`wc -c`, confirmed non-empty), Claude.ai chat exported
    2026-01-21, session created 2026-01-17 18:41:40. This is Part 1: the raw
    MES 3.0 extraction pass (Genius Patterns 1-14, Hidden Knowledge 1-5,
    Implementation Pathways) plus a demo client persona ("Marcus Chen," 12-Week
    Dad Bod Destroyer) used to show the Context Brain Dump / Cliché Blacklist
    framework applied to a fictional example.
  - `...pt.2.md` — 355,727 bytes, session created 2026-01-17 19:47:47. Part 2:
    the deployable Agent Identity Core (Operational Philosophy, Voice & Style
    Parameters, "What to NEVER Say" list) plus additional prompt specs
    (competitive-angle, JTBD excavation, psychological triggers).
  - `...pt.3.md` — 59,118 bytes, session created 2026-01-17 21:36:28. Part 3:
    course-content, buyer-journey, and authority-PR prompt specs, including the
    cold-email "3-Part Structure" and guest-pitch "Pitch Psychology" sections.
  All three read in full (not sampled) for this repair. **These are the actual
  primary source for this skill — they were never wired into `references/` or
  cited anywhere in `genius.md` before this pass.**
- **`skills/cardinal-mason-ai-copywriting/references/genius-patterns.md`**
  (4,732 bytes), **`hidden-knowledge.md`** (1,706 bytes), **`implementation.md`**
  (2,237 bytes) — read in full via `wc -c`. Confirmed non-empty, word-for-word
  duplicates of genius.md's Pattern 1-14 / Hidden Knowledge 1-5 / Implementation
  Pathways sections — these three files and genius.md derive from the same
  extraction pass rather than independently verifying one another.
- **`skills/cardinal-mason-ai-copywriting/references/quality-rubric.md`**
  (85,298 bytes) — spot-read; a scoring rubric (Score 4/7/10 anchors), not a
  transcript. Not independently sourced against the three chat files above; it
  reads as a separately generated rubric layer, standard for this skill format.
- **`SKILL.md.old`** (5,577 bytes, v1.0.0) — read in full. Confirms the skill's
  own self-declared provenance: `author: Extracted from Cardinal Mason (MES 3.0)`
  — consistent with the three-part Claude.ai extraction found above.
- **`references/prompts/`, `prompts-v2/`, `_legacy-prompts/`** (45 files × 3
  copies) — spot-checked for terminology consistency against the source chats
  (e.g., "3-Point Diagnostic," "Context Brain Dump," "Cliché Blacklist" all
  appear in both). Execution templates derived from the extraction, not
  independent transcripts.
- Cardinal Mason's public existence/identity (real YouTube course creator vs.
  invented persona) — **not independently web-verified this pass**. This is a
  heartbeat-check structural repair (Step 4/6 of the Chain), not a Step 5.5
  fact-verification pass against public sources; flagged so a future pass knows
  it is still open.

## Claim labels

| Claim | Label | Basis |
|---|---|---|
| Genius Patterns 1-14 (Context Brain Dump, "Must" Framework, 3-Point Diagnostic, Voice Note Positioning, Swiss Army Knife Positioning, Content Multiplication, Human Taste Layer, 7 Principles Checklist, Lifestyle-First Architecture, Case Study System, Iterative Refinement Loop, Price Confidence Frame, Non-Stop Outreach, Friend-of-Friend Entry) | **VERIFIED** | Cross-checked word-for-word against `knowledge/extractions/inbox/Claude-...2026.md` lines 148-330 ("GENIUS PATTERNS DECODED"). genius.md's Pattern 1-14 text is a near-verbatim reformat of the source extraction. |
| Hidden Knowledge 1-5 (Claude > ChatGPT, AI Humor Must Be Unintentional, 5-Question Context Hack, 20+ Email Webinar Sequences, Voice Notes Beat Text DMs) | **VERIFIED** | Matches `knowledge/extractions/inbox/Claude-...2026.md` lines 331-364 ("HIDDEN KNOWLEDGE REVEALED") and cross-references in pt.2 lines 1156-1184 (Agent Identity Core). |
| Anti-Patterns added this repair (Cliché Blacklist items, "What to NEVER Say" list, humor-cringe ban, throat-clearing ban, "Mistake Everyone Makes" pitching note) | **VERIFIED** (verbatim) | Each item quoted directly from the three source chat files with file+line anchors; see genius.md § Anti-Patterns and PROVENANCE.md for the exact locations. |
| Entity enrichments added this repair ($847/month, 3:47 PM, 47% open rate / 2.3x launch revenue, 15-25% vs. 2-5% response rate, $70K/month year-one business) | **VERIFIED** | Pulled directly from `pt.2.md` lines 1190, 1229, 1156 and the original file line 198 (already embedded in genius.md's own Pattern 4 before this repair). |
| "Hall of Fame Exemplars" (voice note transcript "Hey Sarah, Cardinal here..."; the "Lifestyle-First Entrepreneur" prompt example; the generic-AI Anti-Exemplar) — pre-existing content in genius.md before this repair | **UNCONFIRMED** (as Cardinal Mason's own words) | Searched all three source chat files for "Cardinal here," "Lifestyle-First Entrepreneur," and "sustainable fashion" — **zero matches**. These exemplars do not appear in the primary source transcripts found this pass. They read as illustrative examples synthesized during the original extraction to demonstrate the patterns, not direct quotes from Mason. Counted toward the skill's `verbatim_exemplars` heartbeat check (which measures quote *density*, not source-verified authenticity) but flagged here honestly rather than left silently implied-verified. Content preserved as-is per the additive-first repair boundary. |
| Cardinal Mason built a solo AI-copywriting operation to $70K/month in year one, with students reaching $40-80K/month | **LIKELY** | Stated in the source chat's own Agent Identity Core (`pt.2.md` line 1156) as the framing Mason (or the extraction of him) uses for himself — internally consistent with the skill's `$500K/year` framing in SKILL.md, but not independently verified against a public source (YouTube channel, testimonials) in this repair. |
| Cardinal Mason is a real, identifiable course creator (vs. a persona name) | **UNCONFIRMED** | Not web-verified this pass — see "Sources checked" above. Out of scope for a heartbeat/structural repair; flag for Step 5.5 if this skill is ever used for a claim about the real person rather than the methodology. |
| Quality Rubric anchors (Score 4/7/10) in `references/quality-rubric.md` | **UNCONFIRMED** (independent source) | Rubric exists and is substantial (85,298 bytes) but was not cross-checked line-for-line against the three source chats — it reads as a separately generated scoring layer standard to this skill format, not itself a Mason quote. |

## What this repair did NOT do

It did not contact Cardinal Mason, did not run a live web search to confirm his
public identity or channel, and did not re-verify `quality-rubric.md` line-for-line
against the source chats. What it DID do differently from a typical "no source
exists" repair: it found the actual primary-source transcripts under
`knowledge/extractions/inbox/` (three Claude.ai chat exports, ~806KB total,
verified non-empty via `wc -c` before use) that the skill's own `references/`
folder never linked to, and grounded every new Anti-Pattern anchor and entity
enrichment in exact file+line citations against them rather than treating the
skill's absence-of-a-dedicated-`extractions/`-folder as absence-of-source. See
PROVENANCE.md for the anchor-by-anchor table.
