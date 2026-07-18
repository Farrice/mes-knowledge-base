# Source Ledger — nate-b-jones-ai-taste-mastery

Repair pass: Wave 3 Lane 4 Batch 11. All sizes verified with `wc -c` on 2026-07-18.
All quotes below were re-read verbatim from the cited file/line before being marked
VERIFIED — none were assumed.

## Source files consulted

| File | Bytes (`wc -c`) | Internal date | Topic |
|---|---|---|---|
| `extractions/nate-b-jones/karpathy-loop-mes-extraction.md` | 25,368 | 2026-04-20 (in-file `**Date**` field) | "The Karpathy Loop — Auto-Research to Auto-Agent" (YouTube, April 2026). Auto-improvement loops. **Not** about taste. |
| `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | 16,368 | no in-file date field; file mtime 2026-03-11 | "4 AI Labs Built the Same System Without Talking to Each Other" (YouTube). Multi-agent orchestration. **Not** about taste. |
| `extractions/nate-b-jones/turbokvant-context-engineering-extraction.md` | 19,104 | no in-file date field; file mtime 2026-04-12 | "TurboQuant: Google's Breakthrough..." (YouTube). Memory/context engineering. **Not** about taste. |
| `extractions/nate-b-jones/transcript.txt` | 30,609 | n/a (raw transcript) | Raw transcript, same source as the Karpathy Loop extraction. Grepped for "taste" — 0 hits. |

## Verified absence of a dedicated taste source

Per the batch rule that an "absent source" claim is itself a provenance claim requiring
verification: ran `grep -n -i "taste" extractions/nate-b-jones/transcript.txt` (0 hits)
and the same across all 4 files in the directory (3 hits total, all incidental):

- `smoothing-jagged-frontier-extraction.md:110` — "...become a sniff-checker, a
  tastemaker, and an agent infrastructure builder..." (passing word choice, not a
  taste framework).
- `smoothing-jagged-frontier-extraction.md:164` — "Oren's Taste Mastery" — a
  cross-reference to a **different** skill (`oren-taste-*`), not this expert.
- `turbokvant-context-engineering-extraction.md:12` — lists "taste" as an existing
  sibling skill-domain at extraction time, not source content.

**Conclusion**: no file in `extractions/nate-b-jones/` is an extraction of a Nate B.
Jones video specifically about taste, judgment, or quality gatekeeping as a named
framework. The gap is real, not unread.

## Claim-by-claim ledger

| Claim / section | Label | Basis |
|---|---|---|
| Patterns 1–5 (Taste Activation Formula, Differential Calibration Protocol, 100x Value Multiplication, Oracle Interpretation Framework, Flexible Tool User Identity) | UNCONFIRMED | No matching language in any of the 4 source files. |
| Hidden Knowledge 1–7 (Binary Trust Trap, Embodiment Advantage, Intelligence Stack Reordering, Compost Pile Metaphor, Taste Domain Fluidity, Hollowness Detector, Work Primitive Leveraging) | UNCONFIRMED | No source match. "Compost" appears in the corpus only as an unrelated prompt filename (`compost-pile-synthesizer.md`), not a Jones quote. |
| The Taste Stack (Levels 1–4) | UNCONFIRMED | No source match. |
| Hall of Fame Exemplars (Sector X/Y market analysis, SaaS pitch, marketing-manager anti-exemplar) | UNCONFIRMED — explicitly illustrative | Constructed demonstration scenarios (fictional entities); not transcript-attributed. Flagged in genius.md with an explicit banner this pass. |
| "People who tell you the Karpathy loop eliminates the need for human judgment are flat wrong. It actually concentrates the need for human judgment." | VERIFIED | `karpathy-loop-mes-extraction.md:164` |
| "Most teams that I talk to... measuring activity instead of outcome..." | VERIFIED | `karpathy-loop-mes-extraction.md:158` |
| "The meta agent gets lazy... inserts rubric-specific prompting so the task agent can game the metrics." | VERIFIED | `karpathy-loop-mes-extraction.md:247` |
| "Business process automation, workflow automation, operational systems. It's a matter of when, not if." | VERIFIED | `karpathy-loop-mes-extraction.md:212` |
| "You can start building the infrastructure that makes it possible... These investments pay off regardless of whether you ever run the full autoimprovement loop." | VERIFIED | `karpathy-loop-mes-extraction.md:191` |
| "I don't think autoimproving agents are optional in H2 of 2026..." | VERIFIED | `karpathy-loop-mes-extraction.md:251` |
| "I cannot promise you that you can continue your current habits." | VERIFIED | `smoothing-jagged-frontier-extraction.md:110` |
| "Everything at work is moving to meta-skills." | VERIFIED | `smoothing-jagged-frontier-extraction.md:107` |
| "bring a product strategy to 3-4 experienced product leaders and their assessments will be 'remarkably consistent.'" | VERIFIED | `smoothing-jagged-frontier-extraction.md:104` |
| "Score-only logging (no traces = no interpretability = random mutations)"; "Customer-facing system as first target (failure ≠ cheap)" | LIKELY | These are the extraction document's own structured DO-NOT list (`karpathy-loop-mes-extraction.md:432-445`) — the MES 3.0 extractor's synthesis of Nate's stated failure modes, not his verbatim words. Source-grounded, not verbatim — hence LIKELY not VERIFIED. |
| Applying the above auto-improvement/harness quotes to ground this skill's "taste mastery" thesis | LIKELY | Editorial bridge, made explicit this pass: same expert, adjacent domain, identical throughline (judgment concentrates, doesn't disappear, under AI acceleration). Not a substitute for a dedicated taste-specific source — see Gap below. |

## Gap named (for REPAIR-NOTES.md)

No file under `extractions/nate-b-jones/` is a dedicated taste/judgment-mastery
extraction. `turbokvant-context-engineering-extraction.md:12` lists "taste" as an
existing sibling skill-domain at the time of its own extraction, implying a
taste-specific source once existed or was scoped — it is not present in this repo
today. Recommended fix (out of scope for this repair pass): source a dedicated Nate
B. Jones taste/quality-gatekeeping video and re-extract with MES 3.0, or formally
relabel Patterns 1–5 / Hidden Knowledge / Taste Stack as a synthesized framework
rather than an attributed extraction.
