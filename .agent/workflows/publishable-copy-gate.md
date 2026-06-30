---
description: Thin publishable-copy gate for client-facing or revenue copy; routes through the existing high-taste wrapper, copy owner, claim-safety, anti-slop, and finalize checks
---

# /publishable-copy-gate

Use this when copy, scripts, hooks, ads, outreach, landing pages, or client-facing briefs must be ready to send, publish, or hand to production.

This is a gate, not a competing operating system. It does not own voice, strategy, or copywriting. It binds the existing owner workflow to the final checks that prevent generic, unsupported, or AI-shaped copy from shipping.

## Owner Rule

- Sales, ads, hooks, scripts, VSLs, or DR copy: owner is `/copy-engine` unless a narrower copy workflow is explicitly stronger.
- High-stakes client, recruiter, founder, or public copy: wrap the owner with `/high-taste-writing-os`.
- Failed revision or "we finally got the good version" language: add `/repeatability-spine` before rewriting.
- Claim-heavy or health/supplement copy: add `/accuracy-without-clickbait` or the strongest local claim-safety gate before finalizing.

## Gate

Before copy is considered publishable, verify:

- It reads as usable copy, not notes about the copy.
- The first 3 seconds create curiosity, private recognition, or tension.
- Each script row has a clear job: hook, mechanism, proof, reveal, objection, CTA, or production note.
- Claims are sourced, softened, labeled, or removed.
- No irrelevant internal notes, media-buyer notes to Codex, prompt residue, or recruiter-facing explanation appears inside the client artifact.
- No obvious AI tells: generic thesis language, repeated cadence, "not X, it's Y" crutch, vague stakes, unnecessary frameworks, or self-describing process.
- On-screen text is short enough to use in an actual ad.

## Required Receipt

End the run with:

```markdown
## Copy Gate Result
- Owner:
- Wrapper:
- Claims checked:
- AI-tell pass:
- Production-readiness pass:
- Open risks:
- Verdict: PASS / REVISE / BLOCK
```

## Verification

For written artifacts, run the strongest applicable local checks:

```bash
python3 execution/content_finish_gate.py check --file [artifact] --label publishable-copy
python3 execution/prose_classifier.py check [artifact]
python3 execution/grounding_guard.py [artifact] --task-type Content --strict
```

If the artifact is a DOCX or external deliverable, extract or mirror the text to a temporary review file before running prose and claim checks. Do not ship on a blocked claim or a failed AI-tell pass.
