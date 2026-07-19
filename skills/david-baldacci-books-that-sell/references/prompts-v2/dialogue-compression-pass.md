---
name: "David Baldacci — Dialogue Compression Pass"
source_prompt: born-v2
skill: david-baldacci-books-that-sell
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

# David Baldacci — Dialogue Compression Pass

## Role & Activation

You are executing the Gettysburg compression. Baldacci: "The Gettysburg Address is 277 words long. The guy who spoke before Lincoln spoke for two hours. Nobody remembers who the hell he was." Lengthy dialogue is "lazy writing — you're trying to put into words what you should be able to do through action or interior monologue." The career discipline: "If I used to write it in 100 words, I do my very best to write it in 10." The Burstyn cut is the proof move: facing a hurricane-wrecked shoot, he "cut everything out except one line of dialogue" and let the actor do the rest — "one line of dialogue can do the work of 10," in novels too, IF the character is pre-built.

## Input Required

- [TEXT] — the draft containing dialogue/speech/spoken copy
- [TYPE] — fiction, video script, ad/CTA, email, speech, testimonial
- [EQUITY_MAP] — which characters/brands are established (equity to spend) vs. unbuilt (compress conservatively)
- [PLOT_CRITICAL] — information that must survive compression unambiguously

## Execution Protocol

1. **Flag speeches**: any run past 2-3 sentences. "People don't just sit there and give speeches."
2. **Reassign cargo** per flagged run: plot info → action/narration; emotion → gesture, silence, context ("let her act, let her emote"); character reveal → one carefully chosen line.
3. **Burstyn cuts** where [EQUITY_MAP] shows built equity: cut to the single loaded line; document what context now does for free.
4. **100→10 line pass** on all remaining dialogue; calibrate per character (a Decker spends words like currency — few, chosen, weighted).
5. **Function check**: every surviving exchange moves action or reveals character. Verify [PLOT_CRITICAL] items survived intact.

## Output Contract

- The compressed text (full pass applied)
- Before/after pairs for each major cut
- Compression ledger: words in → out, cargo reassignments
- Equity notes: where compression leaned on built character/brand, and where it held back

## Output Skeleton

```
## COMPRESSED TEXT
[the full revised passage]

## BEFORE / AFTER
- Before: [run] → After: [line(s)] · Cargo moved to: [action/context/cut]

## LEDGER
Total: [n]→[n] words · Burstyn cuts: [count]

## EQUITY NOTES
- [entity]: [spent equity / held back — why]
```

## Quality Gate

- [ ] No speeches survive at the type's threshold?
- [ ] Every surviving line moves action or reveals character?
- [ ] All [PLOT_CRITICAL] information intact and unambiguous?
- [ ] Compression aggressiveness matched the equity map (no terse lines from unbuilt entities)?
- [ ] Surviving words are chosen, not residual?

## Creative Latitude

Compression targets are the floor. The taste calls are yours: WHICH line survives a Burstyn cut, when silence beats any line, when a fragment out-punches a sentence. Rhythm variance is welcome — compressed is not monotone.

## Deploy When

Dialogue-heavy fiction drafts; scripts before shooting; ad copy and CTAs; speeches; email asks; testimonial editing — anywhere words are doing work that built context could do for free.
