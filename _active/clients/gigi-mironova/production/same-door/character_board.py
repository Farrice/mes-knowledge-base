#!/usr/bin/env python3
"""Render the visual character card for Same Door v4."""
import base64, pathlib
import tokens as T

HERE=pathlib.Path(__file__).parent
photo=(HERE.parent.parent/'brand'/'gigi-headshot.jpg').read_bytes()
portrait='data:image/jpeg;base64,'+base64.b64encode(photo).decode()

html=f'''<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="{T.FONTS}">
<style>{T.CSS}</style><div class="frame light">
<div class="pad">
  <div class="rule" style="border-bottom:1px solid {T.HAIRLINE}">
    <div class="caps" style="font-size:20px">GIGI MIRONOVA · VISUAL CHARACTER</div>
    <div class="caps" style="font-size:20px;color:{T.MUTED}">THE CALM CLOSER</div>
  </div>
  <div style="display:grid;grid-template-columns:390px 1fr;gap:44px;align-items:stretch">
    <div style="position:relative;height:505px;border-radius:220px 220px 24px 24px;overflow:hidden;background:{T.BAND}">
      <img src="{portrait}" style="width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.03)">
      <div style="position:absolute;inset:0;background:{T.BAND};mix-blend-mode:multiply;opacity:.22"></div>
      <div style="position:absolute;left:24px;bottom:24px" class="tag">16 years reading fine print</div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:space-between">
      <div class="h" style="font-size:74px;line-height:1.04">clear enough to trust.<br><span class="si">warm enough to call.</span></div>
      <div class="evidence" style="padding:28px 30px;font-size:27px;line-height:1.45;color:{T.MUTED}">
        precise, composed, protective. never clinical. never ornate. every visual move helps someone understand a consequential choice.
      </div>
      <div style="display:flex;gap:14px">
        {''.join(f'<div style="width:76px;height:76px;border-radius:50%;background:{c};border:1px solid {T.HAIRLINE}"></div>' for c in [T.PAPER,T.MIST,T.BAND,T.BRAND,T.ACCENT])}
      </div>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px">
    <div class="evidence" style="padding:26px"><div class="caps" style="font-size:17px;color:{T.ACCENT}">VOICE</div><div class="h" style="font-size:34px;line-height:1.16;margin-top:16px">plain English.<br>exact numbers.<br>no performance.</div></div>
    <div class="evidence" style="padding:26px"><div class="caps" style="font-size:17px;color:{T.ACCENT}">SIGNATURES</div><div style="font-size:25px;line-height:1.5;margin-top:16px;color:{T.MUTED}">evidence cards<br>document tabs<br>receipt rules<br>one clay marker</div></div>
    <div class="evidence" style="padding:26px"><div class="caps" style="font-size:17px;color:{T.ACCENT}">NEVER</div><div style="font-size:25px;line-height:1.5;margin-top:16px;color:{T.MUTED}">script type<br>generic luxury<br>decorative stock<br>unverified math</div></div>
  </div>
  <div class="foot"><div class="caps" style="font-size:18px;color:{T.MUTED}">HOUSESELLERS BLUE · HUMAN WARMTH · DOCUMENT-LITERATE</div><div class="caps" style="font-size:18px;color:{T.MUTED}">V4</div></div>
</div></div>'''
(HERE/'character-board.html').write_text(html)
print(HERE/'character-board.html')
