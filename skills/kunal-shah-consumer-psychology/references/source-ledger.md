# Source Ledger — kunal-shah-consumer-psychology

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 9). Ground truth = the raw transcript
embedded as an attachment inside the claude.ai export conversation that produced
this skill (2026-07-01 harvest). Located via `python3 -c "import tarfile..."`
content-scan of every `.md`/`.txt`/`.json` member of
`_archive/claude-export-2026-07-01.tar.gz` for "kunal" / "shah"+"cred" /
"delta-4" — filename search alone (`find`, `grep -l`) returns zero hits because
the source lives inside a conversation JSON/MD body, not a filename.

## Primary Sources (sizes = `wc -c` equivalent, from `tarfile` member.size)

| Source | Path (inside tarball) | Size | Role |
|---|---|---|---|
| **The Knowledge Project #141, "Core Human Motivations"** — full transcript (Merlin AI transcription of the YouTube episode, https://www.youtube.com/watch?v=nl1PIagzgUo), pasted as a claude.ai attachment | `claude-export/normalized/conversations/366b1ef4-cb21-4983-93d1-9492d0f0b835.md`, transcript body spans roughly char offset 2,000–131,169 (before the first `## assistant` turn) | 190,012 bytes (full conversation, transcript is the bulk of it) | PRIMARY — every genius.md pattern and every new anti-pattern anchor is a verbatim substring of this range, confirmed with a Python substring check this pass |
| Follow-up claude.ai session, same skill build, part 2 | `claude-export/normalized/conversations/004a47f6-905b-4e98-afe2-136dd0aae2b1.md` | 18,447 bytes | SECONDARY — MES-wrapper prompt-generation session (Crown Jewel Prompts), not raw Shah material; not used as a quote source |
| Original extraction working memory | `agents/kunal-shah/memory/context.md` | n/a | Confirms provenance note: "MES-wrapper framing and fabricated-precision stats from the export were discarded; all patterns lifted from Shah's own words" — the standard this ledger holds to |

A local extracted copy of the transcript conversation used for this repair pass is
saved at `.tmp/wave3-lane4-b9/kunal-shah-consumer-psychology/_src/src-366b.md`
(190,012 bytes, byte-identical extraction of the tarball member above).

## Claim-by-Claim Verification

### New this pass — Anti-Patterns section (genius.md)
All six quotes below were located as verbatim substrings (case-insensitive, raw
transcript is lowercase/unpunctuated ASR output) inside `_src/src-366b.md`,
char range 2,000–131,169, via direct Python string search.

| Anti-pattern anchor quote (as written in genius.md) | Status |
|---|---|
| "just by adding tech it doesn't become delta four... it has to improve the efficiency score of the desired behavior" | VERIFIED |
| "i see 90 of them fail all the time back to the analogy of building a dam where rivers don't exist" | VERIFIED |
| "netflix made the mistake of coming to india and say we'll charge you for it, nobody is going to pay that... because value of time is not a concept for us" | VERIFIED |
| "i've not seen people come out of that trap... envy is hyper local, it's like wifi, it works only in a local radius" | VERIFIED |
| "when you reduce the concentration of people with very high slope in the company... you become a big company" | VERIFIED |
| "i can't even risk one percent of my reputation, which makes them not propel in life" | VERIFIED |

### Pre-existing genius.md patterns — spot-checked this pass
| Claim | Status |
|---|---|
| "I see a lot of dam builders with no idea where rivers exist" | VERIFIED (transcript) |
| "Insight is the smallest unit of truth that is actionable..." | VERIFIED (transcript, opening lines) |
| "The fastest way to make somebody feel okay about what they're ashamed of is to make them feel proud about it" | VERIFIED (transcript, shame section) |
| "everything that we are proud of are the handles that we give to other humans to manipulate us" | VERIFIED (transcript) |
| "You cannot develop substance, net worth, wealth, experience unless you're constantly willing to risk your reputation" / 30-40% risk figure | VERIFIED (transcript, reputation section) |
| "standardized things are easier to disrupt than non-standardized things" / Hinduism-as-open-source-religion | VERIFIED (transcript, soulfulness section) |
| Sequoia US analyst-onboarding claim | VERIFIED as **Shah's own secondhand claim** ("i was told by sequoia in the us they've actually introduced this framework") — transcript confirms Shah said it; Sequoia's actual internal practice is not independently confirmable from this source, so treat the underlying fact as Shah-attributed, not fleet-verified |
| CRED "serving the most trustworthy customers to raise systemic trust" | LIKELY — not located as a verbatim substring in the transcript segment checked this pass; consistent with Shah's public CRED positioning but not re-confirmed here. Flagging rather than re-asserting, per this lane's false-absence discipline in reverse (no invented confirmation) |
| "hundreds of millions of users" fantasy framing (Value-of-Time pattern) | LIKELY — paraphrase of Shah's documented CRED thesis (top ~25 million customers), not a verbatim transcript string in this pass |
| "high-slope people identify each other within five minutes" | LIKELY — the three-hour-conversation test is transcript-verified; the five-minute recognition claim was not located as a verbatim string this pass |

No claim in this skill is UNCONFIRMED-and-anchored — items above marked LIKELY
carry no false verbatim-quote anchor; they read as paraphrase/inference in
genius.md, which is consistent with their unverified status.

## Repair Scope Note

This pass fixed `anti_patterns_sourced` and `source_ledger` only, per the
audit gap (`anti_patterns_sourced`, `source_ledger` — 2/6 failing). The
pre-existing 8 genius-pattern quotes above were spot-checked as a provenance
sanity pass, not re-derived; three secondary claims are labeled LIKELY rather
than silently left unlabeled.
