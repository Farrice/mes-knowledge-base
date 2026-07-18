# Source Ledger — vince-nijhof-dtc-operator-system

Every claim/quote used in `genius.md` (and the anti-pattern anchors added in this repair
pass) traced to source, claim-by-claim.

## Primary Source

- **`extractions/vince-nijhof/transcript.txt`** — 113-minute studio interview transcript,
  127,784 bytes (`wc -c`), 24,646 words per the existing genius.md header. VERIFIED
  present on disk, VERIFIED read in full for this repair pass. No date-of-recording
  metadata is present in the transcript file itself; the only calendar reference inside
  the transcript is a passing remark ("real e-commerce in 2026... you are the epitome of
  ecommerce in 2026"), which is conversational color, not a publish date — LABELED
  UNCONFIRMED as a publish/recording date.

## Claim-by-Claim (anti-pattern anchors added 2026-07-18 repair pass)

| # | Claim / anti-pattern | Label | Source |
|---|---|---|---|
| 1 | "There is so much free value out there on the internet that your customers are telling you through support tickets, trust pilot forms, Amazon reviews, competitor reviews, even like emails." | VERIFIED | `extractions/vince-nijhof/transcript.txt` — exact substring match confirmed via grep |
| 2 | "we started to apply emotional marketing and with emotional marketing I mean indeed what you say there is a human on the other side of the screen they have emotions" | VERIFIED | same file — exact substring match confirmed |
| 3 | "We really launch everything as a oneshot killing. We want to make sure that if we shoot, we shoot, right?" | VERIFIED | same file — exact substring match confirmed |
| 4 | "get flow, inventory, supply chain setup. Those three is the first thing you look at put it well and not necessarily look at it too much again." | VERIFIED | same file — exact substring match confirmed |
| 5 | "train the model and you want to go to an extent that you want him to make them think like you." | VERIFIED | same file — exact substring match confirmed |
| 6 | "Talking with creators can be really exhausting." / "our our strategist doesn't talk to creators." | VERIFIED | same file — both exact substring matches confirmed |
| 7 | "people don't purchase until they see your product or ad 13 times." | VERIFIED | same file — exact substring match confirmed. Note: the speaker himself flags this as "a madeup number" in the next sentence — the quote is verbatim but the underlying statistic is the speaker's own acknowledged fabrication, not a research citation. Anti-pattern anchor stands (it documents what he *said*); do not reuse "13 times" as a factual claim in downstream content without the same caveat. |
| 8 | "sometimes you just whatever just throw it out there Meta will figure it out" | VERIFIED | same file — exact substring match confirmed |
| 9 | "Anthropic foundation courses" / executive-assistant certificate story (genius.md Pattern 11 / Hidden Knowledge 5) | LIKELY | Transcript spells the company "Entropic" (ASR mis-transcription pattern consistent with "Anthropic" mis-heard) — content (foundation courses, certificate, executive assistant, pay-raise tie) matches Anthropic's public Claude/AI-fluency course structure. Treated as Anthropic per existing genius.md; flagged here as LIKELY rather than VERIFIED because the transcript's own spelling is not literally "Anthropic." |
| 10 | "$10K bet" launch gate ("Would I bet $10K of my own money this beats current top performer?") | UNCONFIRMED as verbatim | Not found as an exact substring in `extractions/vince-nijhof/transcript.txt` (searched "bet $10", "bet 10" — no hits). This is a paraphrase/compression of the speaker's stated launch discipline (oneshot-kill philosophy, confirmed at #3 above), not a direct quote. Existing genius.md presents it in prose without quotation marks (correct); this ledger entry exists so no future pass mistakes it for a sourced verbatim line. |
| 11 | "launch 1000 ads, Meta will figure it out" (genius.md Pattern 3, quoted) and "earn the launch slot" gate (genius.md Pattern 3, quoted) | UNCONFIRMED as verbatim | Neither "launch 1000 ads", "1000 video ads", nor "earn the launch slot" is found as an exact substring in the transcript (searched all three — no hits). Only the fragment "Meta will figure it out" is verbatim (see claim #8). These two phrases are pre-existing quoted text in genius.md (not added in this repair pass, out of scope for the two failing checks assigned) that read as verbatim Vince quotes but are the skill author's own framing/compression. Flagged here rather than silently fixed — additive-first, minimal-touch scope; see REPAIR-NOTES.md gap note. |

## Pre-Existing Reference File

- **`references/data-bank-source-mining.md`** — operational playbook derived from the
  transcript's data-bank patterns (Genius Pattern 1, Hidden Knowledge 1). Matched the
  heartbeat auditor's `source_ledger` check on filename alone (contains "source"); this
  file (`source-ledger.md`) is the claim-level ledger the check's spirit calls for and is
  additive to, not a replacement for, that file.

## Method Note (per envelope source-search discipline)

`ls extractions/ | grep -i nijhof` and `grep -i vince` both returned exactly one hit:
`extractions/vince-nijhof/` (one directory, one file, `transcript.txt`). File size
confirmed with `wc -c` (127,784 bytes) — not `wc -l`, per the envelope's warning that
single-line files read as 0 lines. No second source file exists under `extractions/`.
The `_archive/claude-export-2026-07-01.tar.gz` archive scan (per envelope's fallback
protocol) was not required because a matching extraction was found on the first search —
recorded here so the absence-of-search is not mistaken for an absence-of-source claim.
