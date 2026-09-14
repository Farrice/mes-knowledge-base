#!/bin/zsh
# PDF export only (headless Chrome, print variant). Run after build_deck.py.
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE="/Users/farricecain/Google Antigravity/.claude/worktrees/inbetweener-pitch-bible/deliverables/josh-banday-pitch-bible/lookbook"
"$CHROME" --headless=new --disable-gpu --virtual-time-budget=6000 --no-pdf-header-footer --print-to-pdf="$BASE/RECURRING_pitch_lookbook.pdf" "http://127.0.0.1:8799/RECURRING_pitch_lookbook_print.html" 2>/dev/null
ls -la "$BASE/RECURRING_pitch_lookbook.pdf" | cut -c1-100
