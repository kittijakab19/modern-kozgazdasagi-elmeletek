# -*- coding: utf-8 -*-
"""Helyi előnézet: a Claude Artifact-formátumú oldalt (fej nélküli HTML)
teljes dokumentummá csomagolja, és kiszolgálja a http://localhost:8931 címen.
Minden újratöltésnél újraolvassa a fájlt, így a szerkesztések azonnal látszanak."""

import io, os
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "modern-kozgazdasagi-elmeletek.html")
PORT = int(os.environ.get("PORT", "8947"))

SHELL_HEAD = """<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  :root{color-scheme:light dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
  body{margin:0;font:14px system-ui,-apple-system,sans-serif;background:#fafaf9}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?")[0] not in ("/", "/index.html"):
            self.send_error(404, "Not found")
            return
        try:
            body = io.open(PAGE, encoding="utf-8").read()
        except OSError as err:
            self.send_error(500, "Nem olvashato: %s" % err)
            return
        html = SHELL_HEAD + body + "\n</body>\n</html>\n"
        data = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    print("Elonezet: http://localhost:%d" % PORT, flush=True)
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
