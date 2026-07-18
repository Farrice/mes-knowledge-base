# Damon Cart NLP — Source Ledger

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 3). This ledger exists because no raw
source file for this skill could be located anywhere in the repository — see
"Provenance status" below before trusting any claim in `genius.md` or `SKILL.md`
at face value.

## Provenance status (verify-absence, not assert-absence)

- `SKILL.md` frontmatter states `source: claude.ai export 2026-07-01`. Checked for
  a matching file: `ls extractions/ | grep -iE "damon|cart"` → 0 of 193 extraction
  directories matched. `find . -iname "*damon*"` (repo-wide, excluding the stale
  `.claude/worktrees/w3-lane3-repair-execution/` mirror, which is an untouched
  duplicate of the same `skills/` tree, not a separate source) → only this skill's
  own `skills/damon-cart-nlp/`, `agents/damon-cart/`, and `.claude/commands/`
  scaffolding. No claude.ai export, transcript, or raw interview file exists in
  this repo. Checked 2026-07-17.
- File sizes actually read in full for this repair (via `wc -c`, not `wc -l`,
  per the fleet's provenance rule): `SKILL.md` 4,593 bytes; `genius.md` 13,695
  bytes; `workflows/01-dissolve-resistance.md` 4,827 bytes;
  `workflows/02-transform-self-concept.md` 5,279 bytes;
  `workflows/03-persuade-through-their-map.md` 5,902 bytes;
  `references/prompts-v2/dissolve-resistance-cycle.md` 8,812 bytes;
  `references/prompts-v2/persuasion-through-their-map.md` 9,930 bytes;
  `references/prompts-v2/self-concept-transformation.md` 8,556 bytes. None are
  empty or truncated — this is not a case of a lost/corrupted source file, it is
  a case of the source never having been checked into the repo.
- Given the absence, this ledger separates: (a) claims that ARE the skill's own
  verbatim text (traceable to file+line, and therefore internally consistent even
  if the ultimate origin is unconfirmed), and (b) claims about the real Damon Cart
  that were independently checked against the live web on 2026-07-17.

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| Damon Cart is a real NLP trainer/teacher | VERIFIED | Active YouTube channel `youtube.com/c/DamonCart` / `youtube.com/damoncart`; multiple third-party-hosted interview videos and podcast episodes found independently (2026-07-17 web search). |
| Cart trained with / interviewed Steve Andreas ("direct student" framing) | LIKELY | Multiple independently-hosted videos confirm a real collaborative relationship: "Candid Interview With NLP Master Steve Andreas & Damon Cart" (YouTube), "Second Interview of Steve Andreas by Damon Cart" (`andreasnlp.com/articles/second-interview-of-steve-andreas-by-damon-cart/`), "Rare Interview With NLP Legends Steve & Connirae Andreas & Damon Cart." These establish mentorship/close collaboration; SKILL.md's specific phrase "direct student of Steve Andreas" is plausible but not verbatim-confirmed in what was checked, hence LIKELY not VERIFIED. |
| Cart is "one of the largest NLP channels on YouTube" | UNCONFIRMED | No subscriber-count or ranking data was checked (would require a live YouTube API/page pull, out of scope for this repair pass); the channel's existence is VERIFIED, its relative size is not. |
| Cart is Co-Founder / lead curriculum developer at SelfConcept.com | LIKELY | Stated in third-party-indexed bio/blog copy surfaced independently (`lifemasterygym.com` blog content, `themindsetandselfmasteryshow.com` interview page); not cross-checked against SelfConcept.com's own about page directly, hence LIKELY not VERIFIED. |
| Cart hosts a podcast covering NLP + self-concept, with a Jason Fladlien episode | VERIFIED | Buzzsprout/Apple Podcasts listings independently indexed: "NLP Sales Secrets To Make Your First $1 Million in 2025 — The Self-Concept Podcast #24" and "Sales Masterclass: NLP Techniques You Can Use Instantly," both crediting Damon Cart's show; a Fladlien-focused blog post on `lifemasterygym.com` ("Influence & Persuasion Skills From World Record Holder Jason Fladlien") corroborates the connection. |
| Cart personally struggled with depression before finding NLP | LIKELY | Third-party-indexed bio copy states Cart "suffered from depression running his own life insurance business as a State Farm agent" before discovering NLP. This is thematically consistent with — but not verbatim identical to — the in-skill claim "Cart's own depressions: one NLP session versus a year of psychotherapy" (genius.md, Insight: NLP Is Content-Free). The specific "one session vs. a year of psychotherapy" comparison was not independently found and is UNCONFIRMED on its own. |
| The Japanese Soldier Reframe, Reverse Values Elicitation, Vision Integration Cycle, Four-Level Self-Concept Architecture, Anti-Affirmation Principle, Grounded Change / Anti-Euphoria Rule, Wholeness Over Parts, Enter the Model of Reality, Utilization, Doubt Insertion (all `genius.md` pattern names and their **Execute**/**Success Metric** text) | UNCONFIRMED (verbatim to skill file, not to an external recording) | Confirmed present, word-for-word, in `skills/damon-cart-nlp/genius.md` by direct read (13,695 bytes, full file). No underlying transcript/export exists in this repo to check these against Cart's actual spoken material — see Provenance status above. Treat these as the skill's working model of Cart, not as directly-cited quotations from a recording. |
| "Euphoria means you did something wrong." | UNCONFIRMED | Verbatim in `genius.md` (Pattern: Grounded Change). Reads as a plausible direct quote given Cart's documented anti-hype stance across the third-party-indexed material, but no recording/transcript was locatable to confirm the exact wording. |
| "It's not survival of the fittest — it's survival of the familiar. People would rather die than change." (attributed to Bandler) | UNCONFIRMED | Verbatim in `genius.md` (Insight: Survival of the Familiar), attributed to Richard Bandler via Cart. This is a widely-circulated paraphrase in NLP circles; the exact wording and its direct attribution to Cart's own delivery could not be confirmed against a primary recording in this repair pass. |
| "90% of what makes a good coach is helping somebody organize their thoughts, feelings, and states..." | UNCONFIRMED | Verbatim in `genius.md` (Insight: Selling Is Coaching). No matching primary source located. |
| The "<5% to 28% close rate" webinar-structure result cited under "Enter the Model of Reality" | UNCONFIRMED | No case study, testimonial page, or transcript containing this specific statistic was located. Flagged here explicitly so it is never upgraded to VERIFIED without a real citation. |
| Workflow 03's co-attribution to Jason Fladlien ("the system from his sales training with Jason Fladlien") | LIKELY | Supported by the independently-confirmed podcast collaboration above (Cart hosting Fladlien on two documented episodes); the specific claim that workflow 03's *techniques* originate in a joint "sales training" (as opposed to podcast conversation) was not independently confirmed. |

## How to extend this ledger

If a future pass locates the actual claude.ai export or a primary Damon Cart
recording, re-run this table claim-by-claim against it before upgrading any
UNCONFIRMED label — do not upgrade on inference alone.
