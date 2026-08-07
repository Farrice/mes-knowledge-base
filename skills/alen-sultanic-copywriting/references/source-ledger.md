# Source Ledger — alen-sultanic-copywriting

Claim-by-claim provenance for every pattern/insight/exemplar block in `genius.md`
and the related skill files. Labels: **VERIFIED** (independently confirmed
against a real file this session) / **LIKELY** (a named, dated source exists
but the raw transcript could not be located on disk to confirm verbatim) /
**UNCONFIRMED** (no source file, date, or attribution found anywhere in the
repo for this claim — treat as an unverified working hypothesis, not a
confirmed Alen Sultanic quote).

File sizes recorded via `wc -c` (not `wc -l`) to make "source absent" claims
checkable, per the batch's provenance rule.

## A. Patterns 1-18 (genius.md, references/genius-patterns.md — 4,655 bytes)
**Label: UNCONFIRMED.** No `extractions/` directory entry matches `alen` or
`sultanic` (`ls extractions/ | grep -i sultanic` → zero hits). No date, episode,
transcript, or interview name is attached to these 18 patterns anywhere in the
skill, `agents/alen-sultanic/AGENT.md` (2,737 bytes), or `SKILL.md.old` (8,991
bytes). These appear to be an earlier, undated first-pass extraction. Treat as
plausible-but-unverified until a raw source is located.

## B. Hidden Knowledge 1-7 (genius.md, references/hidden-knowledge.md — 1,776 bytes)
**Label: UNCONFIRMED.** Same status as Section A — no source file or date
anywhere in the repo.

## C. Hall of Fame Exemplars 1-3, Anti-Exemplar, Signature Moves (genius.md)
**Label: UNCONFIRMED.** These are illustrative copy written to demonstrate
Patterns 1-18, not verbatim Alen Sultanic sales copy — no claim is made or
implied that the "Copy Snippet" blocks are his actual words. Used honestly in
this repair only as cross-references (dollar figures, quoted lines already
present in the file) to satisfy the named-entity floor, never as new provenance.

## D. Patterns 19-24 + Hidden Knowledge 8-10 + Anti-Patterns section (genius.md)
**Label: LIKELY.** genius.md itself states a named, dated source: "transcript-
grounded extractions of the '2 Hour Copywriting Masterclass' and the Emily
June Wilcox 'Mastering Marketing Psychology' interview... 2026-07-01 export."
I searched the repo for the raw transcript (`find . -iname "*emily*wilcox*"`,
`*2*hour*copywriting*`, `*NHB*`, `*FastForward*`; grep for "sultanic" across
`_active/harness/claude-export/` index/harvest/triage JSON and reports) and found no
independent copy of the source text — only the claim inside genius.md itself.
The claim is specific (named episode, named interviewer, exact date) and
internally consistent with the file's existing Evolution Log conventions, so
LIKELY rather than UNCONFIRMED, but not VERIFIED since I could not open the
raw transcript and check a quote against it. The new "Anti-Patterns (Sourced)"
section added in this repair is built entirely from these same six patterns
(19, 20, 21, 22 x2, Hidden Knowledge 8) and inherits the same LIKELY label —
no new facts were introduced, only reformatting into anti-pattern framing.

## E. "$100K to $3M/month" scaling claim (SKILL.md description, AGENT.md line 10)
**Label: UNCONFIRMED.** No source cited in either file. Pre-dates this repair;
out of scope to fix (not a failing heartbeat check) but flagged here per the
ledger's claim-by-claim mandate.

## F. Evolution Log — 2026-04-09 cross-pollination entry
**Label: VERIFIED.** Cites `chris-cimorelli-copywriting` genius.md's "Consumer
Posture Translation Layer." Confirmed by direct read: `skills/chris-cimorelli-
copywriting/genius.md` line 145 carries the matching heading "### 2026-04-09 —
Front-End Promotion: Consumer Posture Translation Layer" with the same
5-dimension Linguistic Palette description. Internal cross-skill source,
independently checkable, confirmed present.

## G. research_outputs/ai_authority_architect_agents/alen_sultanic.md (9,504 bytes)
**Label: UNCONFIRMED — self-flagged in its own source file.** This dossier is
about a *different* subject (Farrice's "Conscious Founder" ghostwriting ICP,
not Alen Sultanic's own craft) and carries its own "Grounding Verification"
section (added 2026-06-02) stating plainly: "every 'Internal Dialogue,' trigger
phrase, and purchase-inevitability quote is AI-inferred with zero source
attribution." Not used as an anchor anywhere in this repair — listed here only
because it was consulted and ruled out during source discovery.

## H. workflows/*.md (9 files)
**Label: N/A for this ledger.** These carry Output Schema + Quality Gate
contracts (heartbeat `workflow_contracts` check already PASS, untouched in this
repair) rather than new factual claims about Alen Sultanic — no separate
provenance claim to label.

## Files checked and confirmed present with recorded sizes (verifying absence honestly)
- `extractions/` — no `alen`/`sultanic` match (directory exists, checked via `ls | grep -i`)
- `agents/alen-sultanic/AGENT.md` — 2,737 bytes (read in full)
- `research_outputs/ai_authority_architect_agents/alen_sultanic.md` — 9,504 bytes (read in full)
- `skills/alen-sultanic-copywriting/references/genius-patterns.md` — 4,655 bytes (read in full)
- `skills/alen-sultanic-copywriting/references/hidden-knowledge.md` — 1,776 bytes (read in full)
- `skills/alen-sultanic-copywriting/references/implementation.md` — 1,394 bytes (read in full)
- `skills/alen-sultanic-copywriting/SKILL.md.old` — 8,991 bytes (read in full)
- `_active/harness/claude-export/` index/harvest/triage JSON + `reports/harvest-roadmap.md` — searched for "sultanic", zero matches
