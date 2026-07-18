# Source Ledger — mark-kashef-claude-claw

Repair pass: Wave 3 Lane 4 Batch 10. Ground truth = files under `extractions/`
matching this expert, verified by direct file read + `wc -c` (sizes below),
plus content already inside the skill files before this repair.

## Files consulted (all read in full this pass)

| File | Size (wc -c) | Role |
|---|---|---|
| `extractions/mark-kashef-claude-claw/extraction-report.md` | 14,288 bytes | PRIMARY source for this skill. Contains "Content Assessment" header claiming its own upstream source was "YouTube video transcript, ~16 min, 3,091 words" — but no raw transcript file for this specific video exists on disk. This report is itself the only artifact; it is a synthesized extraction, not a verbatim transcript. |
| `extractions/mark-kashef/extraction-report.md` | 6,254 bytes | SECONDARY source, different video ("7 Agent Team Use Cases"). Used only for the "Team Invocation" / "create an agent team" claim already present in genius.md's Signature Moves and Hall of Fame before this repair. |
| `extractions/mark-kashef/transcript.txt` | 27,910 bytes | Raw verbatim transcript for the SECONDARY source above. Read in full this pass. Confirms the "spawn agents" vs. "create an agent team" distinction verbatim (see VERIFIED row below). |

No 0-byte or missing files were found for either extraction folder — both `extraction-report.md` files and the one `transcript.txt` are populated and were read in full before any claim below was labeled.

## Claim-by-claim labels

| Claim / anchor | Label | Basis |
|---|---|---|
| Genius Patterns 1–8 (Derivative Detector, Bridge-Not-Brain, Subprocess-as-Architecture, Cost-Zero Infrastructure Bias, Wizard Builder, Memory Decay Architecture, 4-Minute-Mile Reframe, Platform-Agnostic Bridge Design) | LIKELY | Verbatim text matches `extractions/mark-kashef-claude-claw/extraction-report.md` "Genius Patterns" section. No raw transcript exists for this video to cross-check the report's own paraphrasing against Kashef's literal words, so these are LIKELY (confirmed against the extraction report, not against source audio/transcript). |
| Hidden Knowledge 1–6 (Dual-Entry Tax, Subprocess > API Call, Memory Dedup > Memory Size, Computer-Must-Be-On Constraint, Self-Building System Prompt, Session ID Persistence) | LIKELY | Same basis as above — verbatim match to the extraction report's "Hidden Knowledge" section; no raw transcript to verify against. |
| 8-Stage Bridge Pipeline + 3-Layer Memory table + latency figures ("<5 seconds for text, 30-40 seconds for video interpretation") | LIKELY | Present verbatim in `extraction-report.md`, "Methodology" and "Applied Intelligence" sections. Not independently verifiable without the source video. |
| Implementation Pathway ("24-Hour Quickstart" / "7-Day Sprint" / "30-Day Integration") | LIKELY | Present verbatim in `extraction-report.md`, "Implementation Pathway" section. |
| "Team Invocation" claim — saying "spawn agents" produces siloed sub-agents, only "create an agent team"/"spawn an agent team" produces communicating agents | **VERIFIED** | Cross-checked against the raw verbatim transcript `extractions/mark-kashef/transcript.txt`: "The most important magic words you always need to say is create an agent team or spawn an agent team. If you just say spawn agents, it could get confused between sub agents, which are very different in the way they work versus agent teams." This is the one claim in this skill with a raw-transcript-level verification, and it comes from a *different* Kashef video/extraction than the Claude Claw source material — flagged as cross-domain corroboration in the Anti-Patterns section, not native to this skill's own source. |
| "3 to 5 agents is the sweet spot" (referenced in Signature Moves / Quality Rubric) | LIKELY | Present in `extractions/mark-kashef/extraction-report.md` Hidden Knowledge ("The Sweet Spot") and also stated in the raw transcript ("the rule of thumb, by the way, from anthropic is three to five agents is the sweet spot") — VERIFIED at the transcript level for the *other* video, but only LIKELY as applied to Claude Claw itself since it is imported cross-domain, not stated in the Claude Claw source. |
| Hall of Fame Exemplars 1 & 2 ("Custom Claude Code CLI Self-Builder", "Cross-Platform AI Assistant Bridge") | **UNCONFIRMED (constructed)** | Searched both extraction reports in full — neither scenario appears anywhere in the source material. These are illustrative compositions built from the Genius Patterns by a prior enrichment pass, not reported episodes. Flagged inline in genius.md above the Hall of Fame section so this is never mistaken for sourced case history. |
| Anti-Exemplar "Monolithic Cloud Bot" (narrative framing) | **UNCONFIRMED (constructed)**, but its factual anchor ("SQLite over Supabase") is LIKELY | The narrative itself is not in either extraction report. The specific infrastructure-bias fact it illustrates — "SQLite over Supabase. Local file system over cloud storage." — is verbatim in `extraction-report.md`, Genius Pattern 4, and is cited inline where used. |
| Signature Moves section | **UNCONFIRMED (constructed)** | Not found verbatim in either extraction report; restates Genius Patterns 1–3, 5–6 and the cross-domain Team Invocation claim in a different format. No new factual claims beyond what's labeled above. |
| Expert-Specific Quality Rubric | **UNCONFIRMED (derived, not a factual claim)** | A scoring rubric synthesized from the Genius Patterns and their stated Success Metrics — not a claim about what Kashef said, so VERIFIED/LIKELY/UNCONFIRMED provenance labeling doesn't strictly apply; labeled UNCONFIRMED here to be conservative and to flag it as a derived artifact rather than sourced content. |

## Repair-pass additions (this batch)

The following inline anchors were added to previously zero-entity sections
(Subprocess-as-Architecture, Wizard Builder Pattern, Memory Decay
Architecture, Platform-Agnostic Bridge Design, Hidden Knowledge 5, and the
Anti-Exemplar) and to the new "Anti-Patterns (Sourced)" section. Every added
quote was grep-verified against `extraction-report.md` verbatim before being
placed in genius.md — none were invented or reconstructed from memory.
