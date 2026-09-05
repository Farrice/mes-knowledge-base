# Sealed Artifact-Only Generator Packet

You are generating two evaluation artifacts from the shipped SooWei skill only. You are not judging them and may not inspect the reference corpus.

## Allowed Reads

For Candidate 1:

- `skills/soowei-consulting-leverage/SKILL.md`
- `skills/soowei-consulting-leverage/genius.md`
- `skills/soowei-consulting-leverage/workflows/two-pipeline-content-operations.md`
- `skills/soowei-consulting-leverage/references/prompts-v2/two-pipeline-content-operations.md`

For Candidate 2:

- `skills/soowei-consulting-leverage/SKILL.md`
- `skills/soowei-consulting-leverage/genius.md`
- `skills/soowei-consulting-leverage/workflows/trust-sequence-content-architecture.md`
- `skills/soowei-consulting-leverage/references/prompts-v2/trust-sequence-content-architecture.md`

## Forbidden Reads

- `extractions/soowei-consulting-leverage/reference-corpus/`
- all `extractions/soowei-goh-organic-content-acquisition-2026/` files
- source ledgers, transcripts, frames, prior generated candidates, behavior proofs, and this conversation
- any other expert, workflow, prompt, or web source

If a forbidden file is exposed, stop and mark the run contaminated.

## Candidate 1 — Content Operation

A founder-led consulting company publishes on YouTube and Instagram. The founder is the on-camera expert. Current team: founder, one strong long-form editor, one part-time short-form editor, and a general operations assistant. The founder still chooses topics, prepares studios, reviews raw footage, approves every edit, uploads posts, and reads analytics. Content is inconsistent; the editor is overloaded; the company cannot yet justify a large in-house department. Known constraints: local planning only, no hiring, publishing, connectors, paid tools, or invented performance data. Produce the exact contracted artifact for `two-pipeline-content-operations`.

Save to `extractions/soowei-consulting-leverage/blind-pass/generated/candidate-1-content-operation.md`.

## Candidate 2 — Trust and Proof

A young consultant has strong self-reported client results and a growing audience, but skeptical prospects question whether the results are typical, whether the consultant's age means luck, and whether client outcomes were promised too aggressively. Supplied proof consists only of an anonymized outcomes spreadsheet, refund-policy records, and permission to discuss the consultant's own mistakes—not client identities. No independent financial verification exists. Produce the exact contracted artifact for `trust-sequence-content-architecture`. Preserve claim limits and distinguish transparency from spectacle.

Save to `extractions/soowei-consulting-leverage/blind-pass/generated/candidate-2-trust-proof.md`.

## Generation Receipt

End each file with:

- exact files read;
- exact workflow and prompt used;
- forbidden reads: NONE or CONTAMINATED;
- external actions: NONE;
- self-assessment: omitted—the generator must not grade itself.
