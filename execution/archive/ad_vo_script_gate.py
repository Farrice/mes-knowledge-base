#!/usr/bin/env python3
"""Gate paid-ad voiceover rows so notes cannot masquerade as spoken copy.

The TrendScale briefs have two different surfaces:

- brief fields: strategy, proof, editing direction, and claim guardrails
- VO rows: exact narrator copy that a HeyGen speaker could record as-is

This gate reads only ``Script:`` lines from a VO-only extract. It intentionally
does not scan the whole DOCX/text extract, because strategy language belongs in
the brief and must not be confused with the spoken script.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['/-][A-Za-z0-9]+)*|<1%")

RATIONALE_PATTERNS = [
    r"\bthis pass\b",
    r"\brecommended control\b",
    r"\bthe script column\b",
    r"\bvoiceover\b",
    r"\bthis ad\b",
    r"\bad should\b",
    r"\bshould feel\b",
    r"\bmetaphor works\b",
    r"\breason to click\b",
    r"\bthat is the click\b",
    r"\bform list is the story\b",
    r"\bnow the form list\b",
    r"\bstrategy\b",
    r"\bstrategic\b",
    r"\bbrief\b",
    r"\bclient\b",
    r"\brecruiter\b",
    r"\bmedia buyer\b",
    r"\bpdp\b",
    r"\bclaim guardrail\b",
    r"\bsource anchor\b",
    r"\bsource anchors\b",
    r"\bproduction note\b",
    r"\bediting note\b",
    r"\bviewer should\b",
    r"\bthe hook\b",
]

NON_SPOKEN_PATTERNS = [
    r"\bvisual\b",
    r"\bshot\b",
    r"\bb-roll\b",
    r"\bcaption\b",
    r"\btext overlay\b",
    r"\bon-screen\b",
    r"\brow\b",
    r"\bsection\b",
    r"\beditor\b",
    r"\bmust match\b",
    r"\bavoid\b",
    r"\bkeep\b",
    r"\buse one hook\b",
    r"\buse label\b",
]

STAGE_LABEL_PATTERNS = [
    r"\bhook\s+[123]\b",
    r"\bavatar wound\b",
    r"\bmechanism\b",
    r"\bproduct reveal\b",
    r"\bdose contrast\b",
    r"\bserum proof\b",
]

HOOK_MECHANISM_PATTERNS = [
    r"\bmitochondria\b",
    r"\bcpt-?1\b",
    r"\benzyme systems?\b",
    r"\bserum\b",
    r"\babsorb\b",
    r"\babsorption\b",
    r"\bbioavailability\b",
    r"\blong-chain fatty acids?\b",
    r"\btransport step\b",
    r"\bsupplement forms?\b",
]

GENERIC_HOOK_STARTS = (
    "l-carnitine",
    "magnesium supports",
    "stored fuel",
    "serum shows",
    "jcked puts",
    "puravita puts",
    "puravita gives",
)

WOUND_SECTIONS = ("avatar", "wound", "recognition", "private pressure", "buyer wound")
MECHANISM_SECTIONS = ("mechanism", "proof", "dose", "serum", "transport", "product reveal")


@dataclass(frozen=True)
class Row:
    product: str
    section: str
    script: str
    line_no: int


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def parse_rows(text: str) -> list[Row]:
    rows: list[Row] = []
    product = ""
    section = ""
    for line_no, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if line.startswith("Product:"):
            product = line.split(":", 1)[1].strip()
            section = ""
            continue
        if line.startswith("Section:"):
            section = line.split(":", 1)[1].strip()
            continue
        if line.startswith("Script:"):
            script = line.split(":", 1)[1].strip()
            rows.append(Row(product=product, section=section, script=script, line_no=line_no))
    return rows


def grouped(rows: list[Row]) -> dict[str, list[Row]]:
    products: dict[str, list[Row]] = {}
    for row in rows:
        key = row.product or "Unknown product"
        products.setdefault(key, []).append(row)
    return products


def match_any(patterns: list[str], text: str) -> str:
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return pattern
    return ""


def section_has(section: str, needles: tuple[str, ...]) -> bool:
    lowered = section.lower()
    return any(needle in lowered for needle in needles)


def evaluate(rows: list[Row]) -> list[str]:
    failures: list[str] = []
    if not rows:
        return ["No Script: rows found. Gate expects a VO-only extract."]

    for product, product_rows in grouped(rows).items():
        hooks = [row for row in product_rows if row.section.lower().startswith("hook")]
        if len(hooks) < 3:
            failures.append(f"{product}: expected at least 3 hook rows, found {len(hooks)}")
        if len(product_rows) < 7:
            failures.append(f"{product}: expected at least 7 VO rows, found {len(product_rows)}")

        first_wound = next((i for i, row in enumerate(product_rows) if section_has(row.section, WOUND_SECTIONS)), None)
        first_mechanism = next((i for i, row in enumerate(product_rows) if section_has(row.section, MECHANISM_SECTIONS)), None)
        if first_wound is None:
            failures.append(f"{product}: missing avatar-wound or recognition row before mechanism.")
        elif first_mechanism is not None and first_wound > first_mechanism:
            failures.append(f"{product}: mechanism/proof appears before avatar wound.")

    for row in rows:
        text = row.script.strip()
        lowered = text.lower()
        count = len(words(text))
        max_words = 18 if row.section.lower().startswith("hook") else 24

        if not text:
            failures.append(f"line {row.line_no}: empty Script row.")
        if " - " in text or " -- " in text or "—" in text:
            failures.append(f"line {row.line_no}: dashy spoken copy; tighten or split the line.")
        if count > max_words:
            failures.append(
                f"line {row.line_no}: {count} words in {row.section or 'row'} script "
                f"(max {max_words})."
            )

        rationale = match_any(RATIONALE_PATTERNS, lowered)
        if rationale:
            failures.append(f"line {row.line_no}: rationale/process phrase in spoken script: {rationale}")

        non_spoken = match_any(NON_SPOKEN_PATTERNS, lowered)
        if non_spoken:
            failures.append(f"line {row.line_no}: production direction leaked into Script: {non_spoken}")

        stage_label = match_any(STAGE_LABEL_PATTERNS, lowered)
        if stage_label:
            failures.append(f"line {row.line_no}: stage label leaked into spoken script: {stage_label}")

        if row.section.lower().startswith("hook"):
            mechanism = match_any(HOOK_MECHANISM_PATTERNS, lowered)
            if mechanism:
                failures.append(f"line {row.line_no}: mechanism-first hook term: {mechanism}")
            if lowered.startswith(GENERIC_HOOK_STARTS):
                failures.append(f"line {row.line_no}: generic mechanism/product-first hook opener.")

        if re.search(r"\b(there are|here are)\s+\d+\s+(reasons|ways|things)\b", lowered):
            failures.append(f"line {row.line_no}: listicle phrasing in spoken ad copy.")
        if re.search(r"\b(the (reason|point|idea) is)\b", lowered):
            failures.append(f"line {row.line_no}: explanatory setup reads like notes, not VO.")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(prog="ad_vo_script_gate.py")
    sub = parser.add_subparsers(dest="cmd", required=True)
    check = sub.add_parser("check")
    check.add_argument("--file", required=True)
    check.add_argument("--label", default="")
    check.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    path = Path(args.file)
    text = path.read_text(encoding="utf-8", errors="ignore")
    rows = parse_rows(text)
    failures = evaluate(rows)
    label = args.label or path.name
    if failures:
        print(f"AD VO SCRIPT GATE - FAIL - {label}")
        for failure in failures:
            print(f"- {failure}")
        return 2

    if not args.quiet:
        products = grouped(rows)
        row_count = len(rows)
        product_bits = ", ".join(f"{product}: {len(product_rows)} rows" for product, product_rows in products.items())
        print(f"AD VO SCRIPT GATE - CLEAN - {label}")
        print(f"- Script rows checked: {row_count}")
        print(f"- Products: {product_bits}")
        print("- Scope: Script lines only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
