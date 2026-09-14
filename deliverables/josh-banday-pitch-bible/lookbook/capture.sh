#!/bin/zsh
# Headless-Chrome captures for the design gauntlet + PDF export. Literal paths on purpose.
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE="/Users/farricecain/Google Antigravity/.claude/worktrees/inbetweener-pitch-bible/deliverables/josh-banday-pitch-bible/lookbook"
G="$BASE/gauntlet/recurring-lookbook/round-1"
URL="http://127.0.0.1:8799/RECURRING_pitch_lookbook.html"
PURL="http://127.0.0.1:8799/RECURRING_pitch_lookbook_print.html"
mkdir -p "$G"
COMMON=(--headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 --force-device-scale-factor=1)
"$CHROME" "${COMMON[@]}" --window-size=1440,900  --screenshot="$G/desktop.png" "$URL" 2>/dev/null
"$CHROME" "${COMMON[@]}" --window-size=768,1024  --screenshot="$G/tablet.png"  "$URL" 2>/dev/null
# mobile.png comes from Playwright with true mobile emulation (headless desktop Chrome at 375 lays out wider and clips)
# long captures of the print variant (reveals forced, hero fixed height) for mid-page evidence
"$CHROME" "${COMMON[@]}" --window-size=1440,9000 --screenshot="$G/desktop-long.png" "$PURL" 2>/dev/null
"$CHROME" "${COMMON[@]}" --window-size=375,12000 --screenshot="$G/mobile-long.png"  "$PURL" 2>/dev/null
# PDF beside the HTML
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=6000 --no-pdf-header-footer --print-to-pdf="$BASE/RECURRING_pitch_lookbook.pdf" "$PURL" 2>/dev/null
ls -la "$G" "$BASE/RECURRING_pitch_lookbook.pdf" | cut -c1-120
