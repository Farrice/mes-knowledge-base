# Outlier radar auto-refresh — PREPARED, NOT ARMED (Compass: no automation self-activates)

Farrice's explicit yes required before loading. When he says go, run:

```bash
cat > ~/Library/LaunchAgents/com.antigravity.outlier-radar-refresh.plist <<'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.antigravity.outlier-radar-refresh</string>
  <key>ProgramArguments</key><array>
    <string>/Users/farricecain/Google Antigravity/.venv/bin/python3</string>
    <string>/Users/farricecain/Google Antigravity/execution/outlier_radar.py</string>
    <string>refresh</string><string>--niche</string><string>farrice-parallax</string>
  </array>
  <key>WorkingDirectory</key><string>/Users/farricecain/Google Antigravity</string>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>6</integer><key>Minute</key><integer>40</integer></dict>
  <key>StandardOutPath</key><string>/Users/farricecain/Google Antigravity/.agent/outlier-radar/launchd.log</string>
  <key>StandardErrorPath</key><string>/Users/farricecain/Google Antigravity/.agent/outlier-radar/launchd.log</string>
</dict></plist>
PLIST
launchctl load ~/Library/LaunchAgents/com.antigravity.outlier-radar-refresh.plist
```

Daily 06:40 (before the 07:00-ish content window), main-tree paths (post-merge), $0, receipts to `.agent/outlier-radar/receipts/`. Homebase already shows pack age. Add more niches = duplicate the three args. Disarm = `launchctl unload` + delete the plist.
