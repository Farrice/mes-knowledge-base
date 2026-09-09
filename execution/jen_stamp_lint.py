#!/usr/bin/env python3
"""jen_stamp_lint.py: a voice line is a bank, never a stamp.

Fails a week's copy if the same sentence appears in more than one post of the week
(the 2026-09-02 scar: her verbatim close on 9 of 9 shipped posts). Warns when a
voice-bank line appears more than BANK_MAX times in the file.

  python3 execution/jen_stamp_lint.py <COPY.md | captions.txt> [--bank-max 1] [--min-words 6]
  python3 execution/jen_stamp_lint.py selftest

Post boundaries: markdown "### " headings (COPY-weeks format) or "=== " blocks (captions.txt).
Exit 0 = PASS, 1 = FAIL (a sentence repeats across posts), 2 = usage.
"""
import re
import sys

BANK = [
    "i'm here for you. that's my job. i do this to protect you and your best interest.",
    "everything works out exactly the way it's supposed to.",
    "just breathe. take a step back. let's sleep on it.",
    "we're gonna do this, this, and this, and we'll go from there.",
    "my dms are open",
    "or just say hi",
]

_POST_SPLIT = re.compile(r"^(?:### |=== )", re.M)
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")


def _norm(s: str) -> str:
    s = s.lower().replace("’", "'").replace("&#8217;", "'")
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[*_`>#|]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def split_posts(text: str):
    parts = _POST_SPLIT.split(text)
    posts = []
    for p in parts:
        body = p.strip()
        if not body:
            continue
        title = body.splitlines()[0].strip()[:70]
        posts.append((title, body))
    return posts if len(posts) > 1 else [("whole file", text)]


def sentences(body: str, min_words: int):
    out = set()
    for raw in _SENT_SPLIT.split(body):
        s = _norm(raw)
        if s.startswith(("#", "reply routing", "source:", "prices from", "message:", "> message")):
            continue
        if len(s.split()) >= min_words:
            out.add(s)
    return out


def lint(text: str, bank_max: int = 1, min_words: int = 6):
    posts = split_posts(text)
    seen = {}
    for title, body in posts:
        for s in sentences(body, min_words):
            seen.setdefault(s, []).append(title)
    repeats = {s: t for s, t in seen.items() if len(t) > 1}
    # a bank line counts once per POST (a slide and its caption are the same post), never per occurrence
    bank_hits = {b: sum(1 for _, body in posts if _norm(b) in _norm(body)) for b in BANK}
    warns = {b: n for b, n in bank_hits.items() if n > bank_max}
    return posts, repeats, warns


def selftest() -> int:
    good = "### a\nfirst post line one. send me the street.\n### b\nsecond post, different words. tell me the zip you keep coming back to.\n"
    bad = "### a\ni'm here for you. that's my job. i do this to protect you and your best interest.\n### b\nother words. i'm here for you. that's my job. i do this to protect you and your best interest.\n"
    _, r1, w1 = lint(good)
    _, r2, w2 = lint(bad)
    ok = (not r1 and not w1) and (r2 and w2)
    print("selftest:", "PASS" if ok else "FAIL", "| clean file repeats =", len(r1), "| stamped file repeats =", len(r2), "warns =", len(w2))
    return 0 if ok else 1


def main(argv) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    if argv[1] == "selftest":
        return selftest()
    bank_max = int(argv[argv.index("--bank-max") + 1]) if "--bank-max" in argv else 1
    min_words = int(argv[argv.index("--min-words") + 1]) if "--min-words" in argv else 6
    text = open(argv[1], encoding="utf-8").read()
    posts, repeats, warns = lint(text, bank_max, min_words)
    print(f"stamp-lint · {argv[1]} · {len(posts)} post(s)")
    for s, titles in sorted(repeats.items(), key=lambda kv: -len(kv[1])):
        print(f"  FAIL  {len(titles)}× across posts: \"{s[:90]}\"")
    for b, n in warns.items():
        print(f"  WARN  bank line used {n}× (max {bank_max}): \"{b[:70]}\"")
    if repeats:
        print(f"FAIL: {len(repeats)} sentence(s) repeat across posts. A voice line is a bank, never a stamp.")
        return 1
    print("PASS: no sentence repeats across posts" + (f" · {len(warns)} bank warning(s)" if warns else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
