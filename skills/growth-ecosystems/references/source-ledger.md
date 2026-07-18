# Growth Ecosystems (Vincent Hu) — Source Ledger

Ground truth = `extractions/vincent-hu/` (3 transcripts + 1 extraction report) plus verbatim quotes already inside `skills/growth-ecosystems/genius.md`. File sizes confirmed via `wc -c` (2026-07-17, this repair pass):

| File | Size | What it is |
|---|---|---|
| `extractions/vincent-hu/transcript_1_500k_ecosystem.txt` | 64,793 bytes | "$500K Ecosystem Model" YouTube transcript |
| `extractions/vincent-hu/transcript_2_50k_consulting.txt` | 29,783 bytes | "$50K/mo Consulting Philosophy" YouTube transcript |
| `extractions/vincent-hu/transcript_3_100k_path.txt` | 42,934 bytes | "$0→$100K/mo in 18 Months" YouTube transcript |
| `extractions/vincent-hu/extraction-report.md` | 19,145 bytes | MES 3.0 synthesis of the three transcripts above |

All four files are non-empty, non-truncated, and were read in full for this repair pass.

## Claim-by-Claim

| Claim | Label | Basis |
|---|---|---|
| $0→$137K/month, 89% profit margin, 95% close rate, <5K followers, 18 months | VERIFIED | transcript_3: "95% close rate on over 20 calls," "less than 4,000 combined followers"; extraction-report.md header numbers match |
| Three-Yes Framework (Outcome / Method / You) | VERIFIED | transcript_1 direct explanation; extraction-report.md Genius Pattern 2 |
| 6-stage circular journey (stranger→viewer→follower→lead/prospect→client→case) | VERIFIED | transcript_2 names all six stages verbatim, in order |
| FOREST content structure (Foundation-Outcome-Resonance-Expertise-Social Proof-Trust) | VERIFIED | extraction-report.md Genius Pattern 4; structure consistent with how transcript_1 describes his own video architecture |
| Cardinal Rules (5: authenticity, simplicity, margin, dream clients, leverage) | VERIFIED | transcript_3 states all four/five directly ("truth over profit," "still \[__\] for reality," "dream clients only"); extraction-report.md Genius Pattern 7 |
| 15%/85% principle, incl. "Eugene Schwartz, *Breakthrough Advertising*" attribution | VERIFIED | transcript_3, verbatim: "this is called the 15% trap by Eugene Schwarz in Breakthrough of Advertising 1966" (his pronunciation transcribes as "Schwarz"; genius.md's spelling "Schwartz" is the standard spelling of the real author) |
| Hybrid Offer tiers — DIY / DWY $12.5K per 4 months / DFY $15K + 30% profit share | VERIFIED | transcript_3: "\$15,000 minimum setup with a 30% profit share"; "\$3,125 per month or 12.5K every four months" |
| Triage Setter model — 27 calls / 95% close vs. 80-call industry pattern | VERIFIED | transcript_3, verbatim: "I don't need 80 calls to only convert 20. I want 27 high quality leads" |
| Conviction video: $178K+ attributed revenue, 26/27 closes | LIKELY | Stated in extraction-report.md (Genius Pattern 4, Hidden Knowledge 4) as Vincent's "actual tracked result." The exact \$178K / 26-27 figure does not appear as a standalone verbatim string in the 3 transcripts on disk — it is carried from the original MES extraction pass, not independently re-confirmed against a transcript quote in this repair. Treated as LIKELY, not VERIFIED. |
| Client "Charlie," 40K/month jazz-piano coaching business | VERIFIED | transcript_2, verbatim: "Charlie, who I helped build a 40k per month jazz piano coaching business" |
| Vincent's initial conditions (28 Feb 2025): 2,200 IG followers, 40 YouTube subscribers | VERIFIED | transcript_3, verbatim: "my initial conditions around the 28th of Feb, 2025 were that my audience size was around 2,200 IG followers, 40 on YouTube" |
| Ad spend (<\$2,400) against a \$177K revenue month | VERIFIED | transcript_1, verbatim: "...100K in cash and 177K in revenue last July...less than 2.4,000 in ad spend" |
| Weekly rhythm — 4 call days, 1 content day, 1 systems day, 1 day off | VERIFIED | transcript_3, verbatim: "I have four days of calls, one day for content like today, and one day to optimize my structures in my business, and lastly, a day off" |
| "Fourth Yes" (Yes to Themselves) — 2026 evolution | UNCONFIRMED | genius.md's own "Patterns from claude.ai export — Vincent Hu conversations (2026-07-01)" section states its source is "five Vincent Hu videos." Only 3 transcripts exist in `extractions/vincent-hu/`. Cannot verify this claim against any file currently on disk. |
| 2003 online-consumer-trust study (400 shoppers) | UNCONFIRMED | Same section. Grep-verified: the strings "2003" and "400 shoppers" appear in **zero** of the 3 transcripts. No recoverable source. |
| Ravi Abuvala 36-day vs. 5-day sales-cycle example | UNCONFIRMED | Same section. Grep-verified: "Ravi" appears in **zero** of the 3 transcripts. No recoverable source. |
| Google's 7-hours / 11-touchpoints / 4-platforms rule | UNCONFIRMED | Same section, same gap. Not present in any available source file. |
| Client "Lisa," $99/mo → ~$888/mo reframed offer | UNCONFIRMED | Same section. "Lisa" appears in **zero** of the 3 transcripts. |

## Gap Note (read before trusting the "Patterns from claude.ai export" section of genius.md)

That section's own header claims a 5-video source set; only 3 of those transcripts are present in `extractions/vincent-hu/` (verified via directory listing — no other Vincent Hu source files exist anywhere else under `extractions/`). Five sub-claims within that section (Fourth Yes, the 2003 trust study, the Ravi Abuvala example, Google's 7-hours rule, and client Lisa) could not be located in any file under `extractions/` or elsewhere in the skill, verified by direct grep against all three transcripts (zero hits on every distinguishing term). Per the repair envelope's additive-first rule, this content was **not deleted** — it is flagged UNCONFIRMED here rather than presented as sourced. Everything else in `genius.md` and `SKILL.md` traces cleanly to the 3 transcripts + `extraction-report.md`.

## Sources NOT Consulted

No external web search or additional Vincent Hu material was pulled for this repair — scope was ground-truth repair against existing extraction files only, per the envelope.
