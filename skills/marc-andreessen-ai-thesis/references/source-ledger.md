# Source Ledger — marc-andreessen-ai-thesis

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 10). Every claim in `genius.md`
labeled VERIFIED (located verbatim or near-verbatim by direct file search),
LIKELY (consistent with the source but not a located exact phrase — a
reasonable synthesis by the original extraction), or UNCONFIRMED (could not
be located in any available source after full-text search; flagged, not
deleted, per additive-first repair scope).

## Sources Consulted

| File | Size | Role |
|---|---|---|
| `extractions/marc-andreessen/transcript.txt` | 137,689 bytes (`wc -c`) | PRIMARY — Lenny Rachitsky interview transcript, ~26,000 words. Ground truth for this skill (SKILL.md line 11 names this interview explicitly). |
| `extractions/marc-andreessen/extraction-report.md` | 25,822 bytes | SECONDARY — the mastery-extraction write-up genius.md was built from; used to cross-check framework names and structure. |
| `extractions/marc-andreessen-ben-horowitz/transcript.txt` | 55,427 bytes | NOT CONSULTED for this skill — different expert pairing, different topic (new-media/podcasting strategy, not AI economic thesis). Excluded to avoid cross-contaminating this skill's provenance; already verbatim-verified for `a16z-new-media` / `new-media-ghostwriting` per dispatch note. |

## Genius Patterns (1-9) — VERIFIED against transcript.txt

| # | Pattern | Status | Note |
|---|---|---|---|
| 1 | Philosopher's Stone Reframe | VERIFIED | "philosopher stone" located at transcript offset ~543 ("AI is the philosopher stone... transfers the most common thing in the world which is sand converted into the most rare thing in the world which is thought"). |
| 2 | Productivity Growth Master Variable | VERIFIED | Productivity-growth-as-single-variable framing runs throughout the opening third of the transcript; consistent with extraction-report.md §2. |
| 3 | Task Replacement vs. Job Replacement Diagnostic | VERIFIED | Exact phrase located: "Everybody wants to talk about job loss but really what you want to look at is task loss. The job persists longer than the individual tasks." |
| 4 | Non-Fungible Professional Architecture (T-Shaped) | VERIFIED (T-shaped) / LIKELY ("non-fungible" label, "E-Shaped") | "T-Shaped strategy" located verbatim. "Non-fungible" and "E-Shaped" are not found as exact strings in the transcript — they read as the extraction's synthesis label for the T-shaped content, not a direct quote. Treat the *behavior* as VERIFIED, the *naming* as LIKELY. |
| 5 | 3-Layer Company Redefinition Framework | LIKELY | Product/jobs/company framing is consistent with the interview's company-building discussion; the specific "3-layer" structuring is extraction synthesis rather than a verbatim Andreessen phrase. |
| 6 | Determinate Optimist Filter | VERIFIED | "Silicon Valley is characterized by... too much what he calls indeterminate optimism" and "what the world needs more is determinate optimists which are people who are like no the world is going to be better because I'm going to do this specific thing" located verbatim. Nuance: Andreessen separately places himself, as a VC, on the *indeterminate* side ("I would put myself firmly on the side of the indeterminate optimist... founders need to be determinate optimists") — the filter applies to founders/strategies, not to portfolio-level VC posture. Corrected during this repair after an initial misreading; see PROVENANCE.md. |
| 7 | Barbell Information Diet | VERIFIED | "I have like a almost a perfect barbell strategy... I read X and I read old books... everything in the middle I'm always like much more skeptical about" located verbatim. |
| 8 | Human Premium Thesis | VERIFIED | Opening lines of transcript: "in the face of declining population growth... the remaining human workers are going to be at a premium, not at a discount." |
| 9 | Superpowered Individual Model | VERIFIED | "superpowered individual" located verbatim ("how do I become that superpowered individual"). |

## Hidden Knowledge (1-7)

| # | Insight | Status | Note |
|---|---|---|---|
| 1 | AI-Driven Deflation Is the Hidden Wealth Mechanism | VERIFIED | "price deflation and then as a consequence of price deflation everything that people are buying today gets a lot cheaper... a gigantic increase in wealth" located verbatim. |
| 2 | One-Person Billion-Dollar Company | VERIFIED | "this whole idea of a one-person billion-dollar company" located verbatim. |
| 3 | Moat Skepticism as Investment Discipline | VERIFIED | Full moat discussion located ("is there a moat uh on AI models" ... "within a year of GPT3 coming out, there were... open source GP3s... available for free"). |
| 4 | The Prosaic AGI Reframe | VERIFIED | "the prosaic uh definition of AGI and then there's like the... cosmic definition" located verbatim. |
| 5 | Education's Real Output Is Curiosity, Not Credentials | UNCONFIRMED | "curiosity" does not appear anywhere in `transcript.txt` (full-text search, 0 matches). This item's framing is not sourced to the available transcript; likely an interpretive add from a portion of the interview not captured, or extrapolation. Flagged for skill-owner review. |
| 6 | Hardware/Wetware Limitation | UNCONFIRMED | "wetware" and "40,000 years" do not appear in `transcript.txt`. Not located in the available source. Flagged, not deleted. |
| 7 | AI Capability Skepticism Is the New Flat Earth | UNCONFIRMED | "flat earth," "illiterate," and "learn to read" do not appear in `transcript.txt`. Not located. See inline provenance note added directly under this item in `genius.md`. |

## New Anti-Patterns Section (added this repair) — all VERIFIED verbatim

1. "One-dimensional... AI just kind of sweeps sweeps the world and changes everything... kind of the wrong frame" — VERIFIED, `transcript.txt`.
2. "Everybody wants to talk about job loss but really what you want to look at is task loss" — VERIFIED, `transcript.txt`.
3. "too much what he calls indeterminate optimism" / "what the world needs more is determinate optimists which are people who are like no the world is going to be better because I'm going to do this specific thing" — VERIFIED, `transcript.txt`.
4. "everything in the middle I'm always like much more skeptical about" — VERIFIED, `transcript.txt`.
5. "within a year of GPT3 coming out, there were... open source GP3s running on a fraction of the hardware... available for free" — VERIFIED, `transcript.txt`.
6. "If we didn't have AI, we'd be in a panic right now... in the face of declining population growth" — VERIFIED, `transcript.txt` (opening lines).

## Honest Gaps

Three pre-existing Hidden Knowledge items (5, 6, 7) could not be verified against
the available transcript despite full-text search for their key terms
("curiosity," "wetware," "40,000 years," "flat earth," "illiterate," "learn to
read" — all zero matches). These are labeled UNCONFIRMED above and flagged
inline in `genius.md` (item 7 only, as the most specific/quotable claim);
items 5 and 6 are flagged here rather than inline to stay within additive,
minimal-touch scope. Recommend the skill owner either locate a
missing/longer cut of the interview containing this material or downgrade
these three items from "Hidden Knowledge" (implies extracted from source) to
clearly-labeled synthesis/inference.
