# PROVENANCE — jeremy-miner-identity-persuasion repair

Ground truth sources (read in full, sizes recorded via `wc -c`):
- `extractions/jeremy-miner-psych-triggers/transcript.txt` — 79,056 bytes, live-event Q&A transcript, no timestamps/dates present in file.
- `extractions/jeremy-miner-prospect-yes/transcript.txt` — 27,735 bytes, single-speaker training transcript, no timestamps/dates present in file.

Neither source file carries internal date/timestamp markers, so anchors use file path + verbatim quote (both satisfy the auditor's `_HB_SOURCE_ATTR_RE`: quoted string ≥6 chars, and the literal words "source"/"transcript" in the citation).

## Anti-Patterns section (genius.md, new)

| # | Bullet (first words) | Verbatim quote used | Source file | Verified by |
|---|---|---|---|---|
| 1 | Never open with a "meaty" problem question... | "how much credibility and trust do I have in the first 30 seconds of meeting a new prospect? How much?" | psych-triggers transcript | `grep -io` exact match confirmed |
| 2 | Never answer a price objection... | "which is more expensive? Like, is it more expensive to get, you know, the funding together..." | psych-triggers transcript | `grep -io` exact match confirmed |
| 3 | Never deploy the Challenging tone at the start... | "challenging tone. We're never going to do that at the beginning" | psych-triggers transcript | `grep -io` exact match confirmed |
| 4 | Never call a competitor's work "great" or "horrible."... | "fairly decent", "not horrible" | prospect-yes transcript | `grep -io` exact match confirmed (both phrases present) |
| 5 | Never tell the prospect directly what's wrong... | "who is more persuasive? You or them to themselves? Them. This is called self-persu[asion]" | psych-triggers transcript | `grep -io` exact match confirmed ("self-persu" is the file's own truncation, transcript is imperfect ASR) |
| 6 | Never introduce a framework, price, or concept "cold."... | "what I'm about to share with you..." | psych-triggers transcript | `grep -io` exact match confirmed (appears twice in file) |
| 7 | Never ask two important questions back-to-back... | No direct verbatim quote used — cited to Hidden Knowledge 9 (Verbal Pacing Controls Internalization), an existing genius.md section already grounded in the same transcript's ellipsis-pacing material. Anchor satisfied via explicit `source:` + `transcript.txt` citation, not a quote. | psych-triggers transcript | conceptual tie, not verbatim — flagged here for the adversarial verifier |

All six quoted items (1-6) were independently `grep -io`'d against the raw transcript files in this session and matched verbatim (modulo case). Item 7 is the one item without a direct quote; it restates an existing, already-sourced genius.md pattern (Hidden Knowledge 9) rather than introducing a new unverified claim.

## Model Calibration section (genius.md, new)

Not source-anchored — this section is craft guidance modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (read directly), rewritten for Miner's specific texture (verbal pacing, invisible tone mapping, questions-not-statements). No factual/provenance claims made in this section.

## Workflow contract (npq-conversation-architect-v2-identity-cartography.md)

New `## Output Format` section is derived from the workflow's own existing Stage 0 templates (Protected Identity, Shadow Identity, Identity Bridge, Emotional Residue Chain, Objection Identity Map — all already present in the file before this repair) plus a pointer back to v1's `## Output Format`. No external sourcing needed; this is a structural/schema fix, not a factual claim.
