# Provenance — taki-moore-lifestyle-business repair

Ground truth: `extractions/lifestyle-business-experts/` (found directly via fragment search on "taki"/"moore" — no archive fallback needed). Full detail in `references/source-ledger.md`.

| Anchor used in genius.md | Source file | Location |
|---|---|---|
| "The real point of the guarantee is to guarantee the transaction, not the transformation." | `extractions/lifestyle-business-experts/transcript.txt` | offset ~10,547 (confirmed); also pre-existing in `skills/taki-moore-lifestyle-business/genius.md` GP-05 |
| "If I had 150,000 people watching one of my videos, there's no way in hell I'd run sales calls." | `extractions/lifestyle-business-experts/extraction-report.md` | L118 (HK-03); transcript.txt offset ~31,906 differs slightly ("...run ourselves") — labeled LIKELY in source-ledger, not VERIFIED |
| "the value they get is way more from their peers and seeing you coach in a group." | `extractions/lifestyle-business-experts/extraction-report.md` | L121 (HK-04) |
| "I'd rather them shitty first draft that we can tweak quickly... because they can give you a shitty first draft in an hour or they could spend 3 weeks in their head." | `extractions/lifestyle-business-experts/extraction-report.md` | L124 (HK-05); transcript.txt offset ~19,819 near-exact |
| "I feel like you think this is a sales call. No, this is a fit call. I don't care whether you join or not. Our only job right now is to work out, are we even a match?" | `extractions/lifestyle-business-experts/extraction-report.md` | L127 (HK-06); transcript.txt offset ~52,831 near-exact |
| "people are like, wait, I don't even know what questions you're asking and you're asking for money." | `extractions/lifestyle-business-experts/extraction-report.md` | L86 (GP-09); transcript.txt offset ~50,634 near-exact |
| "Pricing is chalk on a board. Most price objections are in the seller's head, not the buyer's." | `skills/taki-moore-lifestyle-business/genius.md` (pre-existing HK item 1) | fuller version at `extractions/lifestyle-business-experts/extraction-report.md` L111-112; transcript.txt offset ~6,415 (cappuccino/chalk imagery) |
| "would Taki Moore recognize this as him architecting a business around someone's actual week..." (recognition test) | Newly written for this repair | grounded in Core Philosophy ("Life-First Business Design") and Voice & Style sections already in `skills/taki-moore-lifestyle-business/genius.md` |
| "How to Use This Skill (Model Calibration)" section texture claims (iPads, spatial metaphors, swearing, "Team Brown Pants") | `skills/taki-moore-lifestyle-business/genius.md` Voice & Style section (pre-existing) + `extractions/lifestyle-business-experts/extraction-report.md` Methodology "Brown Pants Protocol" (L182) | cross-checked, not new invented detail |
| Output Schema headings (workflows 01-06) | Structural fix — renamed pre-existing `## Output` heading to `## Output Schema`; body content (each workflow's deliverable spec) untouched, already file-specific | `skills/taki-moore-lifestyle-business/workflows/*.md` |

Sizes confirmed via `wc -c` (not `wc -l` — transcript.txt is a single unbroken line and reads 0 under `wc -l`):
- `extractions/lifestyle-business-experts/transcript.txt` = 63,441 bytes
- `extractions/lifestyle-business-experts/extraction-report.md` = 19,346 bytes
