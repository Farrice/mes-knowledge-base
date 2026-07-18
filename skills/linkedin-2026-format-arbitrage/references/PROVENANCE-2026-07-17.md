# Provenance — linkedin-2026-format-arbitrage repair

Anchor → source file + location, for every net-new claim added during this repair.
Pre-existing skill content (Hall of Fame Exemplars, Signature Moves, Quality Rubric,
Patterns 2/3/4/6/7 bodies) was NOT touched and is not re-anchored here.

| Anchor added in genius.md | Source file | Location |
|---|---|---|
| "$56,000 a month in just 30 days" / "150 million views" / "$23,000 in less than 90 days" (Pattern 1) | `_active/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/transcript.txt` | lines 27-38, ~00:00:26–00:00:41 |
| Video title/uploader/date "vidIQ, 'The NEW YouTube Strategy Dominating in 2026,' 2026-02-16" | `_active/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/metadata.json` | `upload_date: "20260216"`, `uploader: "vidIQ"` |
| "If you want to get *through* to people, first get *in front* of people" (Pattern 5) | `extractions/Jasmin_Alic_Extraction.md` | "Core Philosophy," Agent Configuration section |
| "4x more profile views daily" / 1+3 Comment Formula credited to Alic (Pattern 8) | `extractions/lara-acosta/2026-linkedin-playbook-extraction.md` | Pattern 7, "The 1+3 Comment Formula (Credited to Jasmin Alic)" |
| "Most people think a niche is just a topic" (Anti-Patterns #1) | `_active/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/transcript.txt` | lines 56-58, ~00:00:59 |
| "Anyone can copy a format, but very few can fill the formats with..." (Anti-Patterns #2) | same transcript.txt | lines 580-586, ~00:10:26–00:10:36 |
| "Big-channel bias" / "No experiment" failure modes (Anti-Patterns #3, #7) | `_active/codex-harvest-2026-06-11/extractions/tim-danilov/niche-bending-system/failure-modes.md` | table rows "Big-channel bias" and "No experiment" |
| "This defeats the typical viral LinkedIn slop" (Anti-Patterns #4) | `extractions/lara-acosta-content-system/transcript.txt` | Cameron/Lara dialogue, mid-transcript (image workflow discussion) |
| "Where people fail in the execution is that they'll try and copy a viral post but they won't copy it correctly. They won't emulate it." (Anti-Patterns #5) | `extractions/lara-acosta-content-system/transcript.txt` | same section, immediately preceding the "typical viral LinkedIn slop" line |
| "...generic AI fluff that Chad GPT writes" (Anti-Patterns #6) | `extractions/lara-acosta-content-system/transcript.txt` | closing section, "how do I remain authentic" exchange |
| LinkedIn 360Brew foundation model exists and does feed ranking (source-ledger, Platform claims) | External — arXiv:2501.16450 ("360Brew: A Decoder-only Foundation Model for Personalized Ranking and Recommendation") + LinkedIn engineering blog, confirmed via live search this session | Not a repo file — independently verified, not previously grounded in any local extraction |
| Recognition-test language ("would Danilov recognize this as theirs...") | Net-new, written this repair per envelope instruction | `genius.md` § How to Use This Skill (Model Calibration) |

## Verification method

- Every Tim Danilov quote/number was located with `grep -n` against the transcript file and
  the surrounding lines read to confirm context before use.
- The video's `metadata.json` was read directly to confirm upload date and uploader —
  not assumed from the extraction summary.
- The Jasmin Alic and Lara Acosta quotes were located with `grep`/`sed` against the
  raw transcript files (not just the extraction-report summaries) to confirm verbatim wording.
- The 360Brew claim was checked with a live web search this session (results: arXiv paper,
  LinkedIn engineering blog coverage, multiple independent third-party writeups) — labeled
  VERIFIED for the model's existence, LIKELY for the skill's specific interpretive framing.
- The "24.42% engagement rate" and "8-10 slides optimal" claims (pre-existing, Pattern 2)
  were searched for across `extractions/` and found nowhere — left in place (additive-only
  boundary) but flagged UNCONFIRMED in `references/source-ledger.md`, not silently passed.
