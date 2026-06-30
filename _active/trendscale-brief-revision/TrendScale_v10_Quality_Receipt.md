# TrendScale v10 Quality Receipt

## Source Lock
- Clean rescue packet: `_active/trendscale-brief-revision/TrendScale_Clean_Rescue_Packet.md`
- JCKED storyboard: `/Users/farricecain/Downloads/farrice-trendscale-complete/04_Source_Markdown/JCKED-Storyboard.md`
- Puravita storyboard: `/Users/farricecain/Downloads/farrice-trendscale-complete/04_Source_Markdown/Puravita-Storyboard.md`
- JCKED source deck pages: concept, avatar, script
- Puravita source deck pages: concept, avatar, script
- Template: `/Users/farricecain/Downloads/TrendScale_Master_Brief_Template (1).docx`

## Template Lock
- Preserved 28 document paragraphs.
- Preserved 1 script table.
- Preserved columns: Visual / editing notes, Section, Script, On-screen text.

## Writing Lock
- Script cells are spoken paid-ad VO only.
- Production direction is held in Visual / editing notes and brief fields.
- Claim guardrails are held in Note fields.
- JCKED preserves The Locked Vault.
- Puravita preserves The Battery You Can't See.

## PDP And Label Notes
- JCKED PDP URL used: https://jcked.com/products/liquid-l-carnitine-4000mg-of1
- PuraVita PDP URL used: https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex
- Current PDP facts are treated as product-page facts, with final label art and Supplement Facts verification required before external send.

## Gate Results
- VO-only gate: PASS. `ad_vo_script_gate.py` checked 16 Script rows across JCKED and Puravita.
- Content finish gate: PASS on spoken-copy-only gate file. Em-dashes: 0. No reveal pattern, no triple anaphora, no cheap close.
- Prose classifier: PASS. Spoken copy scored CLEAN with AI score 0/10.
- Grounding guard strict mode: PASS on spoken copy and receipt.
- DOCX structure check: PASS. Each DOCX preserves 28 document paragraphs and 1 script table with 4 columns.
- Residue scan: PASS. No em dash, internal-process language, blocked failure phrases, or strategy language inside Script cells.
- Export format guard: PASS. DOCX output is allowed because the client template was explicitly requested.
- Chain finalize: PASS. Composite 8.67/10, status Keep, anchored to the clean rescue packet and automated gates.
- External regression lookup: non-blocking warning because Notion network access was unavailable. Notion logging was skipped.

## Final Deliverables
- `TrendScale_JCKED_Production_Brief_v10.docx`
- `TrendScale_Puravita_Production_Brief_v10.docx`
- `TrendScale_v10_VO_Only_Extract.md`
- `TrendScale_v10_Quality_Receipt.md`
