#!/usr/bin/env python3
"""Download the grid thumbnails (640px) captured live from instagram.com/_jiing on 2026-09-01.
Farrice authorized pulling 3-5 of Jen's public photos as placeholders. Signed CDN URLs expire; re-capture if they 403."""
import pathlib, subprocess, urllib.request

OUT = pathlib.Path(__file__).parent / "img" / "jen"
OUT.mkdir(parents=True, exist_ok=True)
H = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
     "Referer": "https://www.instagram.com/"}
URLS = {
    "jen-2025-04-30-intro.jpg": "https://scontent-lax3-2.cdninstagram.com/v/t51.75761-15/491430517_18498913351051480_156378405833671408_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=111&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=dvNHIRE7_KYQ7kNvwE_QQPY&_nc_oc=Adqt0-O6YDZ6-VlWNDQ6geQftpMxrTR1GNR6aXDMsbaATnCDRn_KD1BZVCIFCx71dmI&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQIalsPme_yh6IjGznDMzJmHBwG9CfGwx_0n4-4M4C6tJg&oe=6A9CFEDF",
    "jen-2026-05-20-video.jpg": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/703546406_18585879442051480_3814983744004334036_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=111&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=FHPNZWVKlM8Q7kNvwHhfRqT&_nc_oc=AdorWsxlQ2WaIa_A_M-tOsJjfEOn3_sx1Z2yPf4-aBKQa0g5TZIvFLCNqqT2oAlr3IE&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQLG5igqrb2Ka52fjBWNPbD9VhmrHYH0NOlMZSscdtHTiQ&oe=6A9CFF10",
    "jen-2026-08-27-photo.jpg": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/787638703_18617786764051480_4422702518110843608_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=104&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=ksx09xvg6gsQ7kNvwHSj623&_nc_oc=Adrnrt8M_125bF9Mizqkd3SL5BOssCnie8J_Xc8Napbd8mthHQDgOKNDdqfkn0iSMkw&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQKB_BvCcDa9S5O0qZCvZtNvUKUiJNcrBxG0xji_1I6XmA&oe=6A9D05D2",
    "jen-2026-08-25-video.jpg": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/786390895_18617193457051480_8958080058217958495_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=106&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=Mi_S5O89F9sQ7kNvwFEOxCv&_nc_oc=Adpp87yNFHoEOShTcQ1ib_GSD3oJNqZm6BO1069ackjVRrHiAwpNeMnIbpUVW8vQjqE&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQJZZx7qSl0Fr6HdCurWhLpr8dr0IR80n3w6WUWfWsm0Gg&oe=6A9CFE9A",
    "jen-2026-08-19-video.jpg": "https://scontent-lax3-1.cdninstagram.com/v/t51.82787-15/779865274_18615178582051480_1297208092627968638_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=102&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=xCb14MyNAeIQ7kNvwEWklJg&_nc_oc=AdqZtvZvXGdUsjXZR79Uk1qbHbu3BnHdc1GerlObEJ4_MNge3iCta7lvQVm9xd6shWQ&_nc_zt=23&_nc_ht=scontent-lax3-1.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQJuLf1X4ZWNfhUGLvTzeL5G3jW-H8n3BeO8xhABjkAY8g&oe=6A9D2631",
    "jen-2026-08-14-video.jpg": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-15/775603211_18613038274051480_3593743548873871722_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=105&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=g1F498S9JnkQ7kNvwEWTa5w&_nc_oc=AdpaNUgMX1Bf_FZw35DYPj6bJ539JsjK7A6Tmpaib09KJzPansqQ0cxrF6dNgCUGx2M&_nc_zt=23&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQJlxy-BzIq7eY1-uJazE37C2dqkPoAJBmnIRZ3nM_vBPQ&oe=6A9D15AF",
    "jen-2026-08-10-video.jpg": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-15/773430015_18611644402051480_9217054052637236912_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=106&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=zndnbJvMPuYQ7kNvwFL5A4k&_nc_oc=Ado5AQQtERcvNNKWTkFEZJ5K6hiB_2X-NJ-dqfHXRf0koigGSuaAv5d-OuNacISIhbs&_nc_zt=23&_nc_ht=scontent-lax3-2.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQKpJTWJCY-aopsbBztoISIG7Jcg_862cFozhnFC7dYFVQ&oe=6A9D231A",
    "jen-2026-07-30-video.jpg": "https://scontent-lax7-1.cdninstagram.com/v/t51.82787-15/760997892_18607957819051480_4438488219979421159_n.jpg?stp=dst-jpg_e35_s640x640_tt6&_nc_cat=101&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=1He7vutFVCYQ7kNvwECzCdg&_nc_oc=AdrvyMm6fBOsi72BrBO3Oz-6yO1YhXAVnl9XcrgBomxlw1P8dUhbRQROY5Iht1Ola6M&_nc_zt=23&_nc_ht=scontent-lax7-1.cdninstagram.com&_nc_gid=GZhOWsYevQfZBi3irk7q5g&_nc_ss=79689&oh=00_AQJRXaOIBKYPXojDg5uizxFrJ34DGa8lVmXg_lC2Rc9Kfw&oe=6A9D19DA",
}
for name, u in URLS.items():
    try:
        data = urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=30).read()
        (OUT / name).write_bytes(data)
        print("ok", name, len(data) // 1024, "KB")
    except Exception as e:
        print("FAIL", name, str(e)[:60])
for f in sorted(OUT.glob("*.jpg")):
    if f.stat().st_size > 70 * 1024:
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "55", str(f), "--out", str(f)], check=True, capture_output=True)
    print(f"{f.name}: {f.stat().st_size // 1024} KB")
