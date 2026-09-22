# -*- coding: utf-8 -*-
"""index.html előállítása a forrásoldalból.

A forrás (modern-kozgazdasagi-elmeletek.html) Claude Artifact formátumú:
nincs benne <!doctype>, <html>, <head>, <body> — azokat a közzétevő teszi hozzá.
Ez a script ugyanazt a keretet adja hozzá a statikus (GitHub Pages) változathoz,
plusz a noindex jelzést, hogy a keresők ne indexeljék.

Használat:  python3 build.py
"""

import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "modern-kozgazdasagi-elmeletek.html")
OUT = os.path.join(HERE, "index.html")

SHELL_HEAD = """<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<style>
  :root{color-scheme:light dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
  body{margin:0;font:14px system-ui,-apple-system,sans-serif;background:#F1F0F7}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>
"""


def build():
    body = io.open(SRC, encoding="utf-8").read()
    html = SHELL_HEAD + body + "\n</body>\n</html>\n"
    io.open(OUT, "w", encoding="utf-8").write(html)
    return len(html)


if __name__ == "__main__":
    print("index.html kesz: %d byte" % build())
