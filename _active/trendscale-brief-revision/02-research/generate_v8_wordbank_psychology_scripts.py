from __future__ import annotations

import copy
import re
import zipfile
from pathlib import Path

from generate_v6_conversion_hooks import JCKED as JCKED_V6
from generate_v6_conversion_hooks import PURAVITA as PURAVITA_V6
from generate_v6_conversion_hooks import ROOT, build_docx, docx_to_markdown


RAW_INTENT = (
    "Hooks still sound generic and scientific, stating facts rather than "
    "appealing to human psychology and copywriting. Use the research word "
    "banks and customer avatar language."
)


def sentence_lengths(text: str) -> list[int]:
    parts = [p.strip() for p in re.split(r"[.!?]+", text) if p.strip()]
    return [len(re.findall(r"\b[\w'<%+]+\b", p)) for p in parts]


def control_script(brief: dict) -> str:
    rows = brief["script_rows"]
    return " ".join([rows[0][2], *[row[2] for row in rows[3:]]])


def build_briefs() -> list[dict]:
    jcked = copy.deepcopy(JCKED_V6)
    jcked.update(
        {
            "filename": "TrendScale_JCKED_Production_Brief_v8.docx",
            "client_filename": "TrendScale_JCKED_Production_Brief_FINAL.docx",
            "production_note": (
                "Recommended control is Hook 1. The script column is exact "
                "spoken voiceover. This pass restores the original buyer "
                "psychology: half-used bottle, week-three quit, self-blame, "
                "same gym, different biology, and the 500mg versus 4,000mg "
                "label comparison. PDP facts used: Liquid L-Carnitine 4000MG, "
                "4,000mg serving, 15mL tablespoon direction, liquid delivery, "
                "current flavor variants, and $59.95 single-bottle pricing."
            ),
            "hypothesis": (
                "The locked-vault concept works when the viewer first recognizes "
                "the old failed test. The strongest cold opener starts with the "
                "moment he quit, blamed himself, and never checked whether the "
                "dose made the test unfair."
            ),
            "overall_direction": (
                "Use one hook, then continue through the body rows in order. The "
                "ad should feel like a quiet re-reading of the bottle he already "
                "gave up on: same gym, same diet, different biology."
            ),
            "note": (
                "Structure-function language only. Final edit must match the live "
                "PDP and label. Competitor/dose contrast should stay conditional: "
                "if the old label says 500mg, the test changed. Avoid hard "
                "fat-loss promises, disease claims, personal-attribute callouts, "
                "before-after framing, and uncleared competitor claims. Source "
                "anchors: JCKED PDP, original TrendScale source brief, NIH ODS "
                "Carnitine Health Professional Fact Sheet, and Linus Pauling "
                "Institute L-Carnitine."
            ),
            "script_rows": [
                [
                    "Bathroom cabinet. Half-used L-carnitine bottle. Thumb turns the old label toward camera.",
                    "Hook 1",
                    "He tried L-carnitine once. Quit at week three. The bottle got blamed. The dose never went on trial.",
                    "WEEK THREE WASN'T THE TEST",
                ],
                [
                    "Gym bag, food scale, old bottle. Cut fast, no body-shot transformation.",
                    "Hook 2",
                    "Same gym. Same diet. Different biology. That half-used bottle never explained the door.",
                    "SAME GYM. DIFFERENT BIOLOGY.",
                ],
                [
                    "Closed amber vault. Old bottle in foreground, JCKED still hidden.",
                    "Hook 3",
                    "The ingredient may not have failed him. The key may have been too small.",
                    "THE KEY WAS TOO SMALL",
                ],
                [
                    "Old supplement shelf. Quick flashes of familiar promise language, then silence.",
                    "Avatar wound",
                    "He has seen the promises. Faster fat loss. More energy. Fewer crashes. His thumb already knows that ad.",
                    "HE'S SEEN THAT AD",
                ],
                [
                    "Cinematic vault inside a cell. Fuel sits behind the closed door.",
                    "Mechanism",
                    "The better question is access. Stored fuel has to reach mitochondria before the body can use it.",
                    "THE QUESTION IS ACCESS",
                ],
                [
                    "Amber key reaches the gate. Keep it metaphorical and editorial.",
                    "Vault turn",
                    "That is the locked vault: door, key, fuel. L-carnitine is part of the transport step.",
                    "DOOR. KEY. FUEL.",
                ],
                [
                    "Two label cards. Left card says old label. Right card shows JCKED 4,000mg / 15mL.",
                    "Dose contrast",
                    "If the old label says 500mg, the test changed. JCKED gives 4,000mg in 15mL.",
                    "500MG VS 4,000MG",
                ],
                [
                    "Real JCKED bottle on a counter. No urgency graphics. Hold the label.",
                    "Product reveal",
                    "That is the click: a fairer test before another bottle gets blamed.",
                    "A FAIRER TEST",
                ],
                [
                    "Bottle hold. CTA appears after the last word lands.",
                    "CTA",
                    "Open the product page. Read the serving. Then compare it to the bottle still sitting in the cabinet.",
                    "READ THE SERVING",
                ],
            ],
        }
    )

    puravita = copy.deepcopy(PURAVITA_V6)
    puravita.update(
        {
            "filename": "TrendScale_Puravita_Production_Brief_v8.docx",
            "client_filename": "TrendScale_Puravita_Production_Brief_FINAL.docx",
            "production_note": (
                "Recommended control is Hook 1. The script column is exact spoken "
                "voiceover. This pass restores the original buyer psychology: "
                "phone at 5%, normal bloodwork, still feeling off, wife asks if "
                "he is okay, no answer, and the form-list click. PDP facts used: "
                "Puravita Magnesium Complex Capsules, current buy 1 / buy 2 get "
                "1 / buy 3 get 2 bundle options, visible serum-magnesium FAQ "
                "language, and 'Powered By 12 Active Magnesium Forms' product-page copy."
            ),
            "hypothesis": (
                "The battery concept works when it names the private gap before "
                "it explains magnesium. The strongest opener is the invisible "
                "warning-light moment: normal bloodwork ended the conversation, "
                "but it did not answer the question he is actually living with."
            ),
            "overall_direction": (
                "Use one hook, then continue through the body rows in order. The "
                "ad should feel like it is naming what he has been living without "
                "language for, then giving him one clean reason to inspect the label."
            ),
            "note": (
                "Use label/PDP-approved structure-function claims only. Final edit "
                "must match the live PDP and label. Keep the avatar inside a third-"
                "person narrative rather than diagnosing the viewer. Avoid depletion "
                "certainty, sleep cures, fatigue claims as a promised outcome, disease "
                "language, named-influencer dependency, and diagnosis framing. Source "
                "anchors: Puravita PDP, original TrendScale source brief, and NIH ODS "
                "Magnesium Health Professional Fact Sheet."
            ),
            "script_rows": [
                [
                    "Phone at 5% on a nightstand. Morning light. Hand reaches in, face never shown.",
                    "Hook 1",
                    "Your phone tells you when it is at 5 percent. Your body lets you call it stress.",
                    "NO BATTERY ICON",
                ],
                [
                    "Lab panel slides in. The word normal lands, then the kitchen goes quiet.",
                    "Hook 2",
                    "The bloodwork came back normal. He still did not feel like himself.",
                    "NORMAL, STILL OFF",
                ],
                [
                    "Search bar starts with magnesium, then deletes it and types why do I feel off.",
                    "Hook 3",
                    "He types why do I feel off before he ever thinks magnesium.",
                    "SEARCHING FOR AN ANSWER",
                ],
                [
                    "Coffee on counter. Gym shoes by the door. Wife's hand briefly touches his shoulder.",
                    "Avatar wound",
                    "He slept. He trained. He got the normal report. His wife asked if he was okay, and he had no answer.",
                    "NO ANSWER",
                ],
                [
                    "Phone battery graphic fades into a soft body-map glow.",
                    "Metaphor turn",
                    "A phone gives him a warning light. His body gives him clues he keeps explaining away.",
                    "A WARNING LIGHT",
                ],
                [
                    "Serum window card: small bright line in blood, larger glow in bone and soft tissue.",
                    "Proof",
                    "Serum shows less than 1 percent of total magnesium. Normal can be a narrow window.",
                    "NORMAL CAN BE NARROW",
                ],
                [
                    "Body-map icons for energy, nerve, and muscle. Keep it editorial.",
                    "Mechanism",
                    "Magnesium supports hundreds of enzyme systems, including energy, nerve, and muscle function.",
                    "HUNDREDS OF SYSTEMS",
                ],
                [
                    "Clean form-board reveal. Twelve cards settle around the real bottle.",
                    "Product reveal",
                    "Puravita puts 12 active magnesium forms in one capsule formula. Now the form list is the story.",
                    "12 ACTIVE FORMS",
                ],
                [
                    "Bottle and form list. CTA appears after the voice lands.",
                    "CTA",
                    "Open the product page. Read the forms. Then compare it to the simpler bottle he was about to buy.",
                    "READ THE FORMS",
                ],
            ],
        }
    )
    return [jcked, puravita]


def source_language_ledger() -> str:
    return """# TrendScale v8 Source Language Ledger

## Preservation Lock
- Keep: the original concepts, live PDP URLs, template structure, exact script-table format, and bounded supplement claims.
- Change: hooks must start from buyer psychology and source language before teaching mechanism.
- Do not disturb: JCKED dose/label comparison, Puravita serum-window proof, and editor-ready visual specificity.
- Risk: overcorrecting into unsupported claims, Meta personal-attribute framing, or broad competitor accusations.
- Gate: script rows must read as recordable paid-social voiceover and pass content_finish_gate, prose_classifier, grounding_guard, and DOCX residue checks.

## JCKED Word Bank Recovered
- half-used L-carnitine bottle in his cabinet
- quit at week three
- same diet, same gym, different biology
- wrong assumption
- stored fuel he cannot access
- locked vault, door, key, fuel
- no key, no access
- the man he remembers being
- 500mg versus 4,000mg as a conditional label comparison

## Puravita Word Bank Recovered
- phone tells you when it is at 5 percent, your body does not
- bloodwork came back normal, he still feels off
- he is not looking for magnesium, he is looking for an answer
- his wife asks if he is okay and he has no answer
- naming what he has been living without language for
- no warning light
- serum sees less than 1 percent
- 12 active magnesium forms

## v7 Failure
- Hooks were clean but too abstract.
- Mechanism arrived before buyer recognition.
- Source vocabulary was compressed into notes instead of carried into spoken script.
- The copy gate caught AI tells but did not score psychological pull.

## v8 Repair
- Adds an Avatar Wound row before mechanism for both products.
- Uses original phrase families inside the voiceover.
- Restores JCKED's dose contrast as conditional label comparison.
- Restores Puravita's bloodwork/wife/no-answer pressure without diagnosing the viewer.
"""


def quality_snapshot(briefs: list[dict]) -> str:
    lines = ["# TrendScale v8 Psychology-Led Script Quality Snapshot", ""]
    for brief in briefs:
        script_texts = [row[2] for row in brief["script_rows"]]
        lengths = [length for text in script_texts for length in sentence_lengths(text)]
        control_word_count = len(re.findall(r"\b\w+\b", control_script(brief)))
        lines.extend(
            [
                f"## {brief['client']}",
                f"- Script rows: {len(script_texts)}",
                f"- Control voiceover length: {control_word_count} words",
                f"- Average sentence length: {round(sum(lengths) / len(lengths), 1)} words",
                f"- Longest sentence: {max(lengths)} words",
                "- Recommended control hook: Hook 1",
                "- Hook basis: buyer psychology and recovered source word bank before mechanism.",
                "",
            ]
        )
    lines.extend(
        [
            "## Copy Gate Standard",
            "- Hooks create private recognition or curiosity before facts.",
            "- Mechanism appears only after an avatar wound or metaphor turn.",
            "- PDP facts stay shootable and label-adjacent.",
            "- No internal process notes appear in the client-facing DOCX files.",
            "",
        ]
    )
    return "\n".join(lines)


def red_team_receipt() -> str:
    return """# TrendScale v8 Red-Team Receipt

## Failure addressed
- v7 passed generic copy gates but still felt too scientific.
- The hook language stated facts before creating buyer recognition.
- The source word banks lived in the research, not in the spoken ad.

## Route proof
- Primary failure class: creative revision degradation.
- System failure also confirmed: the first preflight misrouted the critique to a story workflow.
- Repair route: system-audit patch for the trigger language, then high-taste wrapper over copy-engine for the creative repair.

## Claim ledger
| Claim | Status | Source | Script decision |
|---|---|---|---|
| JCKED PDP references Liquid L-Carnitine 4000MG, 4,000mg, and 15mL. | VERIFIED | JCKED PDP / Shopify endpoint | Kept as label proof. |
| L-carnitine participates in fatty-acid transport into mitochondria. | VERIFIED | NIH ODS Carnitine; Linus Pauling Institute | Kept as transport-step mechanism. |
| 500mg versus 4,000mg dose contrast appeared in original source strategy. | SOURCE BRIEF | Original TrendScale source packet | Kept as conditional label comparison only. |
| Puravita PDP references 12 active magnesium forms. | VERIFIED | Puravita rendered PDP text | Kept as product reveal. |
| Serum magnesium is less than 1% of total body magnesium. | VERIFIED | NIH ODS Magnesium | Kept as narrow-window proof. |
| Magnesium supports hundreds of enzyme systems, including energy, nerve, and muscle function. | VERIFIED | NIH ODS Magnesium | Kept as broad structure-function mechanism. |

## Copy red-team
- Hooks begin with human pressure, not a mechanism lecture.
- Avatar language from the source packet appears inside the spoken script.
- No hard fat-loss promise.
- No sleep cure claim.
- No disease claim.
- No direct diagnosis of the viewer.
- No broad universal competitor accusation.
- No internal process notes in client-facing briefs.

## Verdict
PASS for recruiter/founder review after normal brand label and compliance review.
"""


def recruiter_note() -> str:
    return """Hi [Recruiter Name],

Thanks again for the direction. I made a final script-focused pass on both TrendScale briefs.

This version keeps the original concepts the client liked, restores more of the source language and avatar psychology, and rewrites the scripts so the hook earns attention before the mechanism appears. I also kept the live PDP context and bounded the supplement claims for review.

Attachment order:
1. TrendScale_JCKED_Production_Brief_FINAL.docx
2. TrendScale_Puravita_Production_Brief_FINAL.docx

Best,
Farrice
"""


def write_outputs(paths: list[Path], briefs: list[dict]) -> None:
    extract = ["# TrendScale Production Briefs v8 Psychology-Led Text Extract", ""]
    for path in paths:
        extract.append(docx_to_markdown(path))
        extract.append("")
    (ROOT / "TrendScale_Production_Briefs_v8_Text_Extract.md").write_text(
        "\n".join(extract),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v8_Source_Language_Ledger.md").write_text(
        source_language_ledger(),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v8_Script_Quality_Snapshot.md").write_text(
        quality_snapshot(briefs),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v8_RedTeam_Receipt.md").write_text(
        red_team_receipt(),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v8_Recruiter_Revision_Note.md").write_text(
        recruiter_note(),
        encoding="utf-8",
    )

    package = ROOT / "TrendScale_v8_Psychology_Led_Send_Package.zip"
    package_items = [
        ROOT / "TrendScale_JCKED_Production_Brief_FINAL.docx",
        ROOT / "TrendScale_Puravita_Production_Brief_FINAL.docx",
        ROOT / "TrendScale_v8_Recruiter_Revision_Note.md",
    ]
    with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
        for item in package_items:
            archive.write(item, item.name)


def main() -> None:
    briefs = build_briefs()
    paths = [build_docx(brief) for brief in briefs]
    write_outputs(paths, briefs)
    for path in paths:
        print(path)
    print(ROOT / "TrendScale_Production_Briefs_v8_Text_Extract.md")
    print(ROOT / "TrendScale_v8_Source_Language_Ledger.md")
    print(ROOT / "TrendScale_v8_Script_Quality_Snapshot.md")
    print(ROOT / "TrendScale_v8_RedTeam_Receipt.md")
    print(ROOT / "TrendScale_v8_Recruiter_Revision_Note.md")
    print(ROOT / "TrendScale_v8_Psychology_Led_Send_Package.zip")


if __name__ == "__main__":
    main()
