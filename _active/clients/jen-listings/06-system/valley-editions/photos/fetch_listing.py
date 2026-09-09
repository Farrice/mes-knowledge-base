#!/usr/bin/env python3
"""Pull the four listing photos Farrice pasted (public Facebook CDN URLs, his wife's page) into photos/jen/."""
import pathlib, urllib.request

DST = pathlib.Path(__file__).parent / "jen"
URLS = {
    "listing-01-exterior.jpg": "https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/725579004_1691298188726821_17819560062972785_n.jpg?stp=dst-jpg_tt6&cstp=mx2048x1534&ctp=p960x960&_nc_cat=108&ccb=1-7&_nc_sid=f727a1&_nc_ohc=ado2M6vSQJcQ7kNvwECGrgE&_nc_oc=AdoaiYasTzSANxxogZ8f1z2W1uKKFq8XG3qzd2VqaITRgKsCZHu9kFwGHI27qviy7Z0&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=KPCFVYtDwYaAK9Cp_X_pqg&_nc_ss=7b2a8&oh=00_AQICtxhBylEkUOf9wOepGplo7U3XJrimRxNOzyKWClMs8A&oe=6A9E2A40",
    "listing-02-living.jpg": "https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/726373291_1691298452060128_5366326627951358947_n.jpg?stp=dst-jpg_tt6&cstp=mx1600x1066&ctp=p960x960&_nc_cat=102&ccb=1-7&_nc_sid=f727a1&_nc_ohc=18O6FfDdtFEQ7kNvwEAXL67&_nc_oc=Adp6BWr1jcYeZqQLj6zRDmIPr74-SAXKr7CDjrayNJjVBSszdE6inge8-SYsOzGldsc&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=KPCFVYtDwYaAK9Cp_X_pqg&_nc_ss=7b2a8&oh=00_AQLfsABjMQr9scpuqb_Jjb-WHR-Vthy1_nkgViYjJ4ADMQ&oe=6A9E2E4A",
    "listing-03-pool.jpg": "https://scontent-lax7-1.xx.fbcdn.net/v/t39.30808-6/725361621_1691298392060134_626933435010784549_n.jpg?stp=dst-jpg_tt6&cstp=mx2048x1390&ctp=p960x960&_nc_cat=105&ccb=1-7&_nc_sid=f727a1&_nc_ohc=0zg0B515t0EQ7kNvwH3VTEW&_nc_oc=AdqYxFtMyhB4hPE-o8CZsrYcCvQTxZaFJmnyyHkr9tK2C1qXF6JSjLCGGZ_-dblziYU&_nc_zt=23&_nc_ht=scontent-lax7-1.xx&_nc_gid=KPCFVYtDwYaAK9Cp_X_pqg&_nc_ss=7b2a8&oh=00_AQKE38w3Xc4hkOzPkXNnp9udmknPqzo6D3ZAzw2ic66nDw&oe=6A9E1762",
    "listing-04-kitchen.jpg": "https://scontent-lax3-1.xx.fbcdn.net/v/t39.30808-6/725436260_1691298438726796_5694748828193421562_n.jpg?stp=dst-jpg_tt6&cstp=mx1600x1066&ctp=p960x960&_nc_cat=110&ccb=1-7&_nc_sid=f727a1&_nc_ohc=KNhMPXyun0EQ7kNvwGZaBAv&_nc_oc=AdqkczzonkDOLH7zmIK1_sGM8y7ZG1sbRnG_UcBpEUVJk--Yil7ftVd4qLOCwEYXLq0&_nc_zt=23&_nc_ht=scontent-lax3-1.xx&_nc_gid=KPCFVYtDwYaAK9Cp_X_pqg&_nc_ss=7b2a8&oh=00_AQLqxga8-pH95Jg-PRQBk7m_OTWztwVRm_SKu8SNDdJ_nw&oe=6A9E3261",
}
for name, url in URLS.items():
    p = DST / name
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r, open(p, "wb") as f:
        f.write(r.read())
    print(f"{name} {p.stat().st_size // 1024} KB")
