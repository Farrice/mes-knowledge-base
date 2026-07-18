# Source Ledger — tyler-denk-audience-monetization

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 17). Every anchored claim
added to `genius.md` in this pass labeled VERIFIED / LIKELY /
UNCONFIRMED against what was actually found on disk. Pre-existing
skill content (genius patterns, hidden knowledge, exemplars,
signature moves, rubric) is unchanged and carried over from the prior
extraction pass — its claims are re-labeled here for auditability, not
rewritten.

## Search performed (per envelope rule: absence verified, not assumed)

- `ls extractions/ | grep -i denk` → 1 hit: `extractions/tyler-denk/`
  (directory).
- `find extractions -iname "*denk*"` → same directory, 2 files inside.
- `ls extractions/ | grep -i beehiiv` → 0 results (no separate
  Beehiiv-branded extraction folder; all source material lives under
  `extractions/tyler-denk/`).
- No `_archive/claude-export-2026-07-01.tar.gz` scan was needed —
  primary source material was found directly under `extractions/`
  before falling back to the archive.

## Files consulted (real, on-disk, sized with `wc -c`)

| File | Size (wc -c) | What it is |
|---|---|---|
| `extractions/tyler-denk/transcript.txt` | 73,539 bytes | Full interview transcript ("Anatomy of a Dream"-style podcast, host Matt interviewing Tyler Denk, CEO of Beehiiv, re: Big Desk Energy newsletter growth + Beehiiv platform strategy). Read in full for this repair. |
| `extractions/tyler-denk/extraction-report.md` | 7,440 bytes | Prior MES 3.0 extraction summary — genius patterns, hidden knowledge, methodology (BDE Growth Engine), crown-jewel prompts. Source of the genius.md pattern language that predates this repair. |
| `skills/tyler-denk-audience-monetization/genius.md` (pre-repair) | baseline | Original genius file — Genius Patterns, Hidden Knowledge, Hall of Fame Exemplars, Signature Moves, Quality Rubric. All content preserved; this repair is additive (Model Calibration, Anti-Patterns, Verbatim Exemplars sections). |
| `skills/tyler-denk-audience-monetization/SKILL.md` | baseline | Workflow index + execution-prompt pointers; unchanged by this repair. |
| `skills/tyler-denk-audience-monetization/references/prompts-v2/*.md` (4 files) | baseline | Structure-pure v2 execution prompts (B2B Sponsor Profiler, BDE Tease-Drop-Trap, Founder Intimacy Automator, Zero-Cost Referral Architect); unchanged. |

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| Tyler Denk is CEO of Beehiiv; grew Big Desk Energy to ~120,000 subscribers in ~2 years | VERIFIED | Stated directly by Denk in transcript: "About 120 today" (subscriber count); "it was just about exactly two years ago. So, January of 2024 was the first issue." |
| Series B pitch deck offered as tier-1 referral reward, deck raised $33M | VERIFIED | Verbatim in transcript: "by sharing a single your link with just a single person, you receive the unedited series B deck that we use to raise $33 million." |
| Costa Rica mastermind: $10,000/person, 7-8 people, $70,000 revenue, ~50-60% margin | VERIFIED | Verbatim in transcript: "It's $10,000 per person. We host about 7 to eight people... it's $70,000 in revenue"; margin stated separately: "it's probably 50 60% revenue profit margins on these events." |
| Post-subscribe survey completion: ~30-40k of 120k subs submitted | VERIFIED | Verbatim: "I think of my 120,000 subs about 30 to 40,000 of them have submitted the survey." (Note: a later line claims "87 to 90% completion rate" for a different survey context — the two figures are not reconciled in the source; both are Denk's own statements, flagged here rather than silently picking one.) |
| VA sends LinkedIn/X connection requests + newsletter DM to every new Beehiiv signup | VERIFIED | Verbatim: "I have a VA that sends a LinkedIn request, which I've maxed out now, but an X request to follow every single new user on the platform... I also have them send a note to sign up to my newsletter." |
| Anti-pattern: swag-first referral rewards create logistical/margin drag | VERIFIED | Verbatim Denk quote in transcript, referral-program segment (see genius.md Anti-Patterns, item 1). |
| Anti-pattern: Boost was over-engineered for growth-manager-style users | VERIFIED | Verbatim Denk quote, Boost-cons segment (see genius.md Anti-Patterns, item 2). |
| Anti-pattern: no single silver-bullet channel, only compounding tactics | VERIFIED | Verbatim Denk quote, growth-tactics segment (see genius.md Anti-Patterns, item 3). |
| Anti-pattern: pricing sponsorships off hypothesis instead of survey data | VERIFIED | Verbatim Denk quote, monetization segment (see genius.md Anti-Patterns, item 4). |
| Anti-pattern: aggregator/recap content is most exposed to AI summarization | VERIFIED | Verbatim Denk quote, AI-in-the-inbox segment (see genius.md Anti-Patterns, item 5). |
| Anti-pattern: assuming only high-volume consumer brands are worth chasing for sponsorship | VERIFIED | Verbatim Denk quote, HubSpot-vs-Spotify segment (see genius.md Anti-Patterns, item 6). |
| HubSpot-style B2B SaaS sponsors only need one conversion to justify spend, vs. consumer brands needing volume | VERIFIED | Paraphrased accurately from transcript's HubSpot/Spotify math discussion; not a single clean verbatim line (transcript has a transcription artifact — "crazy rorowaz," likely a garbled "ROI" — around the exact HubSpot dollar figure, so the number is treated as LIKELY rather than re-quoted verbatim). |
| "One-of-One Narrative Moat," "Compounding Growth Stack," "Zero-Cost Referral Lever," "Post-Subscribe Intelligence Capture" pattern names | LIKELY | These are the prior extraction pass's synthesized pattern *names* (not Denk's own vocabulary — he never uses these exact terms on the podcast). The underlying behaviors they describe are VERIFIED against the transcript; the naming/framing is analyst synthesis, consistent with `extraction-report.md`. |
| "Subscriber Value Staging Architecture" (4-stage engagement model) | UNCONFIRMED | Not present in the transcript in this form. Denk discusses engagement-based targeting informally (survey completion, open rates) but never articulates a 4-stage Warming/Engaged/Invested/Champion model. This appears to be prior-pass synthesis beyond the source material — flagged, not removed (pre-existing content, additive-first boundary applies), but should not be treated as a direct Denk quote or framework. |
| "Automated Authenticity" as Denk's own named paradox | LIKELY | The behavior (VA-scaled personal outreach) is VERIFIED verbatim; the specific label "Automated Authenticity Paradox" is prior-pass analyst naming, not Denk's own phrase. |
| Workflow files carry Output Schema + Quality Gate | VERIFIED | Confirmed by `execution/skill_auditor.py` heartbeat check (workflow_contracts: PASS both before and after this repair — untouched). |

## What this repair did NOT do

- Did not invent a Tyler Denk quote, date, or figure to make the
  anti-pattern/exemplar checks pass artificially — every quoted string
  in the new Anti-Patterns and Verbatim Exemplars sections was checked
  as an exact, contiguous, on-disk substring of
  `extractions/tyler-denk/transcript.txt` before being written.
- Did not resolve the survey-completion-rate discrepancy (30-40k vs.
  87-90%) in the source by picking one number — both are genuine Denk
  statements in different parts of the same interview, addressing
  different survey contexts; flagged above rather than silently
  averaged or cherry-picked.
- Did not remove or rewrite the pre-existing "Subscriber Value Staging
  Architecture" pattern (UNCONFIRMED) — out of scope for a heartbeat
  repair (additive-first, minimal-touch); flagged here for a future
  pass or Farrice review rather than deleted unilaterally.
