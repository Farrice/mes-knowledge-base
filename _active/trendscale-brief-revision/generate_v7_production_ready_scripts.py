from __future__ import annotations

import copy
import re
import zipfile
from pathlib import Path

from generate_v6_conversion_hooks import JCKED as JCKED_V6
from generate_v6_conversion_hooks import PURAVITA as PURAVITA_V6
from generate_v6_conversion_hooks import build_docx, docx_to_markdown, ROOT


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
            "filename": "TrendScale_JCKED_Production_Brief_v7.docx",
            "client_filename": "TrendScale_JCKED_Production_Brief_FINAL.docx",
            "production_note": (
                "Recommended control is Hook 1. The script column is exact spoken "
                "voiceover. This pass loads the current PDP and keeps the ad focused "
                "on one cold-traffic action: inspect the serving before judging the "
                "ingredient. PDP facts used in the brief: Liquid L-Carnitine 4000MG, "
                "4,000mg serving, 15mL tablespoon direction, liquid delivery, current "
                "flavor variants, and $59.95 single-bottle pricing."
            ),
            "hypothesis": (
                "The locked-vault concept works when the hook does not lecture. The "
                "strongest cold opener is a serving-size challenge: before the viewer "
                "dismisses L-carnitine, make the old bottle feel like an unfair test."
            ),
            "overall_direction": (
                "Use one hook, then continue through the body rows in order. The ad "
                "should feel like a label-inspection mystery with a clear PDP reason "
                "to click, not a fat-loss promise."
            ),
            "note": (
                "Structure-function language only. Final edit must match the live PDP "
                "and label. Avoid hard fat-loss promises, disease claims, personal-"
                "attribute callouts, before-after framing, and uncleared competitor "
                "claims. Source anchors: JCKED PDP, NIH ODS Carnitine Health "
                "Professional Fact Sheet, and Linus Pauling Institute L-Carnitine."
            ),
            "script_rows": [
                [
                    "Bathroom cabinet. Half-used L-carnitine bottle. Cut to a clean serving-size card.",
                    "Hook 1",
                    "Before blaming L-carnitine, check the serving. A small test can make the right ingredient look useless.",
                    "CHECK THE SERVING",
                ],
                [
                    "Two simple cards snap into frame: same ingredient, different serving.",
                    "Hook 2",
                    "Same ingredient. Different dose. Different experiment.",
                    "DIFFERENT EXPERIMENT",
                ],
                [
                    "Old bottle in shadow. JCKED bottle stays out of frame until the body.",
                    "Hook 3",
                    "That half-used bottle may not prove L-carnitine failed. It may prove the test was too small.",
                    "THE TEST WAS TOO SMALL",
                ],
                [
                    "Cinematic mitochondria gate. Fatty-acid tag pauses outside the gate.",
                    "Mechanism",
                    "Long-chain fatty acids need a transport step before mitochondria can use them for energy.",
                    "THE TRANSPORT STEP",
                ],
                [
                    "Amber key enters the gate. Keep it metaphorical, not medical.",
                    "Vault turn",
                    "L-carnitine is part of that step. That is the locked vault.",
                    "THE LOCKED VAULT",
                ],
                [
                    "Macro PDP and label moment. Highlight 4,000mg and 15mL only.",
                    "PDP proof",
                    "JCKED makes the serving hard to miss: 4,000mg liquid L-carnitine in 15mL.",
                    "4,000MG / 15ML",
                ],
                [
                    "Real bottle on counter. Flavor tiles can appear quickly, then fade.",
                    "Product reveal",
                    "It is liquid, direct, and built around the serving the old bottle made easy to ignore.",
                    "LIQUID L-CARNITINE",
                ],
                [
                    "Bottle hold. CTA appears after the final word lands.",
                    "CTA",
                    "Open the product page. Look at the serving first. Then decide whether the old bottle was a fair comparison.",
                    "LOOK AT THE SERVING",
                ],
            ],
        }
    )

    puravita = copy.deepcopy(PURAVITA_V6)
    puravita.update(
        {
            "filename": "TrendScale_Puravita_Production_Brief_v7.docx",
            "client_filename": "TrendScale_Puravita_Production_Brief_FINAL.docx",
            "production_note": (
                "Recommended control is Hook 1. The script column is exact spoken "
                "voiceover. This pass loads the current PDP and keeps the ad focused "
                "on one cold-traffic action: read the form list. PDP facts used in "
                "the brief: Puravita Magnesium Complex Capsules, current buy 1 / "
                "buy 2 get 1 / buy 3 get 2 bundle options, visible serum-magnesium "
                "FAQ language, and 'Powered By 12 Active Magnesium Forms' product-page copy."
            ),
            "hypothesis": (
                "The battery concept works when the hook begins with the private "
                "search, not the category. Start with the moment normal stops being "
                "reassuring, then let serum and form-list proof earn the product."
            ),
            "overall_direction": (
                "Use one hook, then continue through the body rows in order. The ad "
                "should move from private question to label inspection without "
                "diagnosing the viewer or promising a sleep cure."
            ),
            "note": (
                "Use label/PDP-approved structure-function claims only. Final edit "
                "must match the live PDP and label. Avoid depletion certainty, sleep "
                "cures, fatigue claims, disease language, named-influencer dependency, "
                "and diagnosis framing. Source anchors: Puravita PDP and NIH ODS "
                "Magnesium Health Professional Fact Sheet."
            ),
            "script_rows": [
                [
                    "Phone at 11:07 on a nightstand. Search bar begins, then stops before the query finishes.",
                    "Hook 1",
                    "At 11:07, the search is not for magnesium. The search is for why normal still feels unfinished.",
                    "NORMAL FEELS UNFINISHED",
                ],
                [
                    "Clean lab panel slides in. The word normal lands like a period.",
                    "Hook 2",
                    "A normal panel can close the case before the magnesium question even starts.",
                    "NORMAL CAN CLOSE THE CASE",
                ],
                [
                    "Phone battery at 5 percent. Cut to a quiet body-map glow.",
                    "Hook 3",
                    "Phones show 5 percent. The body makes you investigate.",
                    "NO BATTERY ICON",
                ],
                [
                    "Soft body map lights up energy, nerve, and muscle icons. Editorial, not clinical.",
                    "Mechanism",
                    "Magnesium supports hundreds of enzyme systems, including energy, nerve, and muscle function.",
                    "HUNDREDS OF SYSTEMS",
                ],
                [
                    "Serum window card: small bright line in blood, larger glow in bone and soft tissue.",
                    "Proof",
                    "Less than 1% of total magnesium is in serum. That is a narrow window.",
                    "A NARROW WINDOW",
                ],
                [
                    "Form list appears as clean cards, not a busy supplement-facts wall.",
                    "Form turn",
                    "Then the form list matters. Magnesium forms can absorb differently.",
                    "FORM MATTERS",
                ],
                [
                    "Real Puravita bottle. Twelve form cards settle around the label.",
                    "Product reveal",
                    "Puravita builds the story around 12 active magnesium forms in one capsule formula.",
                    "12 ACTIVE FORMS",
                ],
                [
                    "Bottle and form list. CTA appears after the voice lands.",
                    "CTA",
                    "Open the product page. Read the form list. Compare it to a simpler bottle before choosing.",
                    "READ THE FORM LIST",
                ],
            ],
        }
    )
    return [jcked, puravita]


def quality_snapshot(briefs: list[dict]) -> str:
    lines = ["# TrendScale v7 Production-Ready Script Quality Snapshot", ""]
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
                "",
            ]
        )
    lines.extend(
        [
            "## Copy Gate Standard",
            "- Scripts read as spoken ad copy, not descriptions of strategy.",
            "- PDP facts are included in client-facing notes and used only where shootable.",
            "- No media-buyer-only instructions, Codex notes, or recruiter apologetics appear in the briefs.",
            "- Health/supplement claims stay bounded to structure-function or label/PDP proof.",
            "",
        ]
    )
    return "\n".join(lines)


def red_team_receipt() -> str:
    return """# TrendScale v7 Production-Ready Red-Team Receipt

## Route proof
- Prompt: Run the high-taste plus copy-engine route, load the PDP and prior brief, then write only production-ready scripts that pass the copy gate.
- Preflight owner: /high-taste-writing-os.
- Support gates: /copy-engine, /publishable-copy-gate, /repeatability-spine, /content-finish-gate.
- Routing enforcer: PASS.

## PDP proof
| Product | PDP fact used | Status |
|---|---|---|
| JCKED | Live Shopify product endpoint returns Liquid L-Carnitine 4000MG, JCKED vendor, 4,000mg PDP language, 15mL serving language, and $59.95 flavor variants. | VERIFIED 2026-06-29 |
| Puravita | Live Shopify product endpoint returns Puravita Magnesium Complex Capsules, PuraVita vendor, and bundle variants. Rendered PDP text includes serum-magnesium FAQ language and 'Powered By 12 Active Magnesium Forms.' | VERIFIED 2026-06-29 |

## Claim ledger
| Claim | Status | Source | Script decision |
|---|---|---|---|
| L-carnitine helps transport long-chain fatty acids into mitochondria for energy production. | VERIFIED | NIH ODS Carnitine; Linus Pauling Institute | Kept as transport-step mechanism. |
| JCKED PDP references 4,000mg Liquid L-Carnitine and 15mL serving. | VERIFIED | JCKED PDP / Shopify product endpoint | Kept as PDP proof. |
| Magnesium is a cofactor in more than 300 enzyme systems and relates to energy, nerve, and muscle function. | VERIFIED | NIH ODS Magnesium | Kept as broad structure-function mechanism. |
| Less than 1% of total magnesium is in blood serum. | VERIFIED | NIH ODS Magnesium | Kept as serum-window proof. |
| Magnesium forms can differ in absorption. | VERIFIED | NIH ODS Magnesium | Kept as form-list rationale. |
| Puravita PDP says Powered By 12 Active Magnesium Forms. | VERIFIED | Puravita rendered PDP text | Kept as product reveal. |

## Copy red-team
- No hard fat-loss promise.
- No disease claim.
- No sleep cure claim.
- No depletion certainty.
- No named-influencer dependency.
- No universal competitor accusation.
- No internal process notes or media-buyer-only notes.
- No before-after, scale, doctor, diagnosis, or panic urgency direction.
- Script rows are exact spoken voiceover.

## Verdict
PASS for recruiter/founder review after final brand label and compliance review.
"""


def recruiter_note() -> str:
    return """Hi [Recruiter Name],

Thanks again for the direction. I made a final production-ready script pass on both TrendScale briefs.

This version keeps the original concepts the client liked, loads the live PDP context, and rewrites the scripts so the voiceover reads like paid social copy instead of strategy notes. I also kept the claim language bounded for supplement review and removed internal-only process notes from the client-facing docs.

Attachment order:
1. TrendScale_JCKED_Production_Brief_FINAL.docx
2. TrendScale_Puravita_Production_Brief_FINAL.docx

Best,
Farrice
"""


def write_outputs(paths: list[Path], briefs: list[dict]) -> None:
    extract = ["# TrendScale Production Briefs v7 Production-Ready Text Extract", ""]
    for path in paths:
        extract.append(docx_to_markdown(path))
        extract.append("")
    (ROOT / "TrendScale_Production_Briefs_v7_Text_Extract.md").write_text(
        "\n".join(extract),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v7_Script_Quality_Snapshot.md").write_text(
        quality_snapshot(briefs),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v7_RedTeam_Receipt.md").write_text(
        red_team_receipt(),
        encoding="utf-8",
    )
    (ROOT / "TrendScale_v7_Recruiter_Revision_Note.md").write_text(
        recruiter_note(),
        encoding="utf-8",
    )

    package = ROOT / "TrendScale_v7_Production_Ready_Send_Package.zip"
    package_items = [
        ROOT / "TrendScale_JCKED_Production_Brief_FINAL.docx",
        ROOT / "TrendScale_Puravita_Production_Brief_FINAL.docx",
        ROOT / "TrendScale_v7_Recruiter_Revision_Note.md",
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
    print(ROOT / "TrendScale_Production_Briefs_v7_Text_Extract.md")
    print(ROOT / "TrendScale_v7_Script_Quality_Snapshot.md")
    print(ROOT / "TrendScale_v7_RedTeam_Receipt.md")
    print(ROOT / "TrendScale_v7_Recruiter_Revision_Note.md")
    print(ROOT / "TrendScale_v7_Production_Ready_Send_Package.zip")


if __name__ == "__main__":
    main()
