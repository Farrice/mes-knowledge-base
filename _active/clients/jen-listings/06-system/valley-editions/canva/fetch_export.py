#!/usr/bin/env python3
"""Download the Canva export PNGs of Jen · The Valley · Tarzana Edition 01 (design DAHUEKxS7Ig) into canva/edition-01/."""
import pathlib, urllib.request

OUT = pathlib.Path(__file__).parent / "edition-01"
OUT.mkdir(exist_ok=True)
URLS = [
    "https://export-download.canva.com/xS7Ig/DAHUEKxS7Ig/-1/0/0001-2970638602026487557.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T215401Z&X-Amz-Expires=74541&X-Amz-Signature=9823c7ea1114303f2759044f288b9aaed1100657fa3258e693b8084cc6cef104&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Wed%2C%2002%20Sep%202026%2018%3A36%3A22%20GMT",
    "https://export-download.canva.com/xS7Ig/DAHUEKxS7Ig/-1/0/0002-2970638602026487557.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260901T232312Z&X-Amz-Expires=68510&X-Amz-Signature=6b5796f902248c562c0ce78d7a7561e900e9c8a2ac9df71d9009bdd6efdff524&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Wed%2C%2002%20Sep%202026%2018%3A25%3A02%20GMT",
    "https://export-download.canva.com/xS7Ig/DAHUEKxS7Ig/-1/0/0003-2970638602026487557.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T161607Z&X-Amz-Expires=9312&X-Amz-Signature=7521205d8a3f7de33df436160932866236e4a731fd1d99f8f5ff4c1b3360f589&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Wed%2C%2002%20Sep%202026%2018%3A51%3A19%20GMT",
    "https://export-download.canva.com/xS7Ig/DAHUEKxS7Ig/-1/0/0004-2970638602026487557.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T065559Z&X-Amz-Expires=40900&X-Amz-Signature=e2bec9c5a8b852f7fecdb77aaceb6dd62abbeee14f1e02f439d85f1b938d2903&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Wed%2C%2002%20Sep%202026%2018%3A17%3A39%20GMT",
    "https://export-download.canva.com/xS7Ig/DAHUEKxS7Ig/-1/0/0005-2970638602026487557.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUH5AO7UJ26%2F20260902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260902T034547Z&X-Amz-Expires=54460&X-Amz-Signature=47f689a0fc22b70a9f829f2c8d62e2a3aa59287963d9053286052c22146802ce&X-Amz-SignedHeaders=host%3Bx-amz-expected-bucket-owner&response-expires=Wed%2C%2002%20Sep%202026%2018%3A53%3A27%20GMT",
]
NAMES = ["01-cover", "02-laidrey", "03-listing", "04-what-869k-buys", "05-send-me-the-street"]
for url, name in zip(URLS, NAMES):
    p = OUT / f"{name}.png"
    urllib.request.urlretrieve(url, p)
    print(f"{p.name} {p.stat().st_size // 1024} KB")
