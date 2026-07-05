---
thread: ad-script
status: ready
resume_hint: Send JCKED + Puravita v2 .docx to recruiter; 3 open decisions in private note
branch: main
pin: true
---

# TrendScale Creative Strategist Trial — Script Rework v2 (JCKED + Puravita)

**Thread:** ad-script · **Status:** ready to send (3 small user-decisions open) · **Resume:** `/resume ad-script`

## What this session was
Reworked Farrice's two TrendScale trial ad scripts (JCKED Liquid L-Carnitine "Locked Vault" + Puravita Magnesium "Battery You Can't See") into the client's official Brief Template v1.3 `.docx`, then elevated to published-grade over several passes: fixed pricing/alignment, killed AI tells, added the founder hire-unlock triad, removed the internal Notes section, and rewrote both bodies to flow as one cohesive cold-traffic script (the metaphor now carries the mechanism).

## Where everything lives
`projects/trendscale-trial/rework-v2/`
- **SEND:** `TrendScale_JCKED_Brief_v2.docx` + `TrendScale_Puravita_Brief_v2.docx`
- **Message to recruiter:** `COVER-NOTE.md`
- **Readable full copy (plain text):** `MASTER-COPY.md`
- **KEEP FOR FARRICE, do not send:** `PRIVATE-STRATEGIST-NOTES.md` (sources, A/B logic, founder-call talking points, the 3 open decisions in §8)
- Generator (rebuild docx): `scratchpad/trendscale/build_briefs.py` → run from `skills/docx/`. Note: pandoc/LibreOffice not installed; use `textutil -convert txt` for QA.

## Verified state
Zero em-dashes, no Notes section, no behind-the-curtain leakage, XML well-formed. Reviewers: prose-doctor (bodies CLEAN) + adversarial founder (hire YES, fund YES, published-grade; Puravita body judged stronger than its hooks).

## Open decisions (only Farrice can close — private note §8)
1. **Puravita CTA guarantee** — get Puravita's refund terms; mirror JCKED's 365-day line onto its CTA.
2. **Huberman/Attia named-person call** — keep named (higher-converting) or ship the name-free fallback (ready).
3. **Source cards** — leave sources in the private note (clean brief) or add a one-line citation under each proof card.

## Next action
Send the two `.docx` + cover note to the recruiter (WhatsApp 778-322-4478). Log outcome to `revenue_tracker.py` when the client responds.
