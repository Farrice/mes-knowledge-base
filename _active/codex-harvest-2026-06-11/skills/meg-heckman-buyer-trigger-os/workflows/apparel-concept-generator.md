---
description: Generate identity-led T-shirt, hoodie, mug, poster, or POD concepts from a niche using buyer recognition, social currency, and familiar/twist mechanics.
---

# Apparel Concept Generator

## Input

- Niche or community.
- Buyer subculture language.
- Product type and print constraints.
- IP constraints.
- Desired tone: deadpan, heartfelt, weird, premium, funny, insider, giftable, etc.

## Steps

1. Load `references/source-ledger.md` and `references/genius-patterns.md`.
2. Name the source timestamp anchors used.
3. If the request includes `--research`, current trends, buyer insights, social listening, or purchase intent research, run `workflows/research-backed-trigger-run.md` first.
4. Use evidence IDs or source URLs for current buyer language, trends, marketplace signals, or community claims.
5. Define the exact buyer, not the broad market.
6. Separate `Source Mechanics`, `Live Evidence Used`, and `Domain Extrapolation`.
7. List 5 private recognition moments the buyer would feel. Mark them as sourced or hypothesis.
8. Convert each moment into a self-statement.
9. Pair each self-statement with a familiar/twist structure.
10. Draft concepts that pass thumbnail-speed recognition.
11. Add social currency: the reaction, gift, share, or public moment.
12. Check printability and originality.
13. Score and choose the top 3 concepts.

## Output

| Concept | Buyer Moment | Shirt/Product Text | Identity Signal | Familiar/Twist Pair | Social Currency Moment | Print Notes | Risk | Verdict |
|---|---|---|---|---|---|---|---|---|

## Guardrails

- Avoid broad labels like "dog mom," "EDM fan," or "dance nerd" unless a specific lived scene sharpens them.
- Avoid protected logos, lyrics, event marks, team names, and copied meme formats.
- Do not overbuild visuals before the recognition mechanic works.
- Do not claim a concept is trend-backed, social-listening-backed, or buyer-language-backed without an evidence ID or source URL.
- If research status is `DEGRADED`, label concepts as research-informed hypotheses.
- If research status is `FAILED`, produce the evidence gap and do not invent concept directions from current-world claims.
