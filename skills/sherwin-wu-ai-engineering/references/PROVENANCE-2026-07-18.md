# PROVENANCE — sherwin-wu-ai-engineering repair (Wave 3 Lane 4 Batch 16)

Ground truth source: `extractions/sherwin-wu/transcript.txt` (92,292 bytes, single-line
cleaned ASR transcript of Sherwin Wu's Lenny's Podcast interview, ~17,768 words) and
`extractions/sherwin-wu/extraction-report.md` (17,875 bytes). Confirmed present with
`wc -c` before use (per envelope source-search discipline). No `_archive/claude-export`
scan needed — primary source was found directly under `extractions/`.

## Anti-Patterns (genius.md, new section)

All six quotes verified verbatim via `python3 -c "q in text"` against
`extractions/sherwin-wu/transcript.txt` (see command output in session; all six returned
`True`).

| Anchor (as written in genius.md) | Verbatim in transcript.txt | Context |
|---|---|---|
| "this team doesn't have that escape hatch" | Confirmed | Discussing OpenAI's internal 100%-Codex-written codebase experiment |
| "you want to make sure you're not letting the brooms go crazy here" | Confirmed | Sherwin invoking Sorcerer's Apprentice re: unsupervised agent fleets |
| "The models will eat your scaffolding for breakfast" | Confirmed | Sherwin's scaffolding-impermanence line (also already used in SKILL.md description) |
| "OpenAI API team has like been guilty of this" | Confirmed | Sherwin self-critiquing his own team's ad-hoc API design detours |
| "don't you know don't overly stress about this" | Confirmed | Sherwin's advice on AI-pace FOMO |
| "This is the worst the models will ever be" | Confirmed | Sherwin quoting OpenAI VP of Science Kevin Whale |

All six items sit on their own single-line list-item (no follow-on-line anchors), each
carrying its quote inline plus "(Lenny's Podcast interview; transcript:
extractions/sherwin-wu/transcript.txt)" as the source tag.

## Recognition Test (genius.md, "How to Use This Skill (Model Calibration)" section)

New section modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (read
before writing). Contains the literal phrase "would Sherwin recognize this as" —
written against Sherwin's actual documented patterns already present in genius.md:
platform-empirical numeric grounding ("95% of engineers use Codex," "70% more PRs" —
both drawn from extraction-report.md §Hidden Knowledge #1 and SKILL.md line 3), the
context-as-bottleneck diagnostic habit, and the wizard/apprentice oversight posture —
not invented texture.

## Untouched (already passing, out of repair scope)

- `verbatim_exemplars`, `source_ledger`, `named_entity_floor`, `workflow_contracts` —
  all PASS in the original audit; left unmodified per "repair only failing checks."
- Note: `source_ledger`'s PASS is a loose regex match on "[LIKELY ABSORBED]" inside
  `references/_legacy-prompts/05-scaffolding-obsolescence-audit.md` and
  `references/prompts/05-scaffolding-obsolescence-audit.md` (an ASCII diagram label, not
  a genuine VERIFIED/LIKELY/UNCONFIRMED source ledger). Flagged here for conductor
  awareness — not fixed because the check is not in the failing set and the envelope
  scopes repairs to failing checks only.
