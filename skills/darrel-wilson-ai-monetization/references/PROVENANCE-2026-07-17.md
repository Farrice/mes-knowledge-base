# Provenance — Darrel Wilson AI Monetization repair pass

Anchor → source file + location. Every quote below was grep-verified verbatim
against the cited file during this repair (see commands in REPAIR-NOTES.md).

| Anchor (as used in genius.md) | Source file | Location |
|---|---|---|
| "Forget cold buying email lists. Forget cold blasting customers." | `extractions/darrel-wilson-ai-money/transcript.txt` | Single-paragraph transcript (no line breaks); appears ~180 words in, opening of Method 1 (lead generation) |
| "you're not selling a concept. You're showing a finished product." | `extractions/darrel-wilson-ai-money/transcript.txt` | Method 3 (selling AI websites), the Fitactory Nashville / "ugly website" example |
| "why don't you make a tool that people can actually use?" | `extractions/darrel-wilson-ai-money/transcript.txt` | Method 2 (affiliate tools), currency-exchange-site example |
| "instead of writing opinions like oh wise review you know my favorite exchange" | `extractions/darrel-wilson-ai-money/transcript.txt` | Method 2, immediately following the currency-exchange walkthrough |
| "Instead of selling your time, you can sell your systems." | `extractions/darrel-wilson-ai-money/transcript.txt` | Method 4 (selling AI workflows), opening line |
| "Any company offering a free and pro version, I typically try to avoid it... customers will just go directly to their websites or they'll buy the service after the cookies expire." | `extractions/darrel-wilson-affiliate-marketing/transcript.txt` | Affiliate-program-selection section, discussing marketplace vs. direct programs and freemium risk |
| "I have a Facebook group with over 15,000 members and guess what? No one buys... I have thousands of pins and I'm lucky to get one conversion a month." | `extractions/darrel-wilson-affiliate-marketing/transcript.txt` | Social-media-fatigue section, immediately after the Facebook/Pinterest discussion |

## Verification commands run this pass

```
grep -o "Forget cold.\{0,80\}" extractions/darrel-wilson-ai-money/transcript.txt
grep -o "you're not selling a concept.\{0,80\}" extractions/darrel-wilson-ai-money/transcript.txt
grep -o "why don.t you make a tool.\{0,80\}" extractions/darrel-wilson-ai-money/transcript.txt
grep -o "instead of writing opinions.\{0,100\}" extractions/darrel-wilson-ai-money/transcript.txt
grep -o "Instead of selling your time.\{0,60\}" extractions/darrel-wilson-ai-money/transcript.txt
grep -o "Any company offering a free and pro version.\{200\}" extractions/darrel-wilson-affiliate-marketing/transcript.txt
grep -o ".\{50\}No one buys\. my Pinterest.\{150\}" extractions/darrel-wilson-affiliate-marketing/transcript.txt
```

All seven returned exact matches — no UNCONFIRMED-labeled quote was used as an
anchor. The two items in the source-ledger marked UNCONFIRMED (exact video
publish date/URL) are explicitly excluded from any anchor — neither extraction
folder carries that metadata, confirmed by `ls -la` on both directories.

## Sizes checked (per envelope Rule 2 — verify absence, don't assert it)

```
extractions/darrel-wilson-ai-money/transcript.txt          14,562 bytes
extractions/darrel-wilson-affiliate-marketing/transcript.txt  21,929 bytes
extractions/darrel-wilson-affiliate-marketing/extraction-report.md  14,540 bytes
```

`_active/harness/codex-harvest-2026-06-11/extractions/` and the claude-export tarball
were not searched — the two files above already supplied ≥5 sourced
anti-patterns, so the gate did not require the deeper archival sweep. Noted
as scope, not as a false "nothing else exists" claim.
