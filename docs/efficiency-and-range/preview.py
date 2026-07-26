#!/usr/bin/env python3
"""Turn the locally-built Jekyll page into a self-contained preview.

Everything the live site loads over the network — the just-the-docs stylesheets
and the two Google fonts — is inlined, so the preview is byte-for-byte the same
rendering without any external requests (which an Artifact's CSP would block).
"""
import base64, re, urllib.request, pathlib

SITE = pathlib.Path(__file__).resolve().parents[2] / '_site'
OUT = pathlib.Path(__file__).resolve().parent / 'preview.html'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')

html = (SITE / 'efficiency-and-range.html').read_text()

# ---- 1. Fonts: only if the page actually links a webfont. The paper layout
# uses system faces, so this normally does nothing; a just-the-docs page would
# pull in head_custom's two Google families. ----
font_css = ''
webfont = re.search(r'<link[^>]+href="(https://fonts\.googleapis\.com/[^"]+)"', html)
if webfont:
    req = urllib.request.Request(webfont.group(1).replace('&amp;', '&'), headers={'User-Agent': UA})
    src = urllib.request.urlopen(req, timeout=30).read().decode()
    kept = []
    for b in re.findall(r'@font-face\s*\{[^}]*\}', src):
        ur = re.search(r'unicode-range:\s*([^;]+);', b)
        if ur and 'U+0000-00FF' not in ur.group(1):
            continue                              # latin subset only
        url = re.search(r'url\((https://[^)]+\.woff2)\)', b)
        if not url:
            continue
        data = urllib.request.urlopen(
            urllib.request.Request(url.group(1), headers={'User-Agent': UA}), timeout=30).read()
        uri = 'data:font/woff2;base64,' + base64.b64encode(data).decode()
        kept.append(b.replace(url.group(1), uri))
    font_css = '\n'.join(kept)
    print(f'fonts inlined: {len(kept)}  ({sum(len(k) for k in kept)//1024} KB base64)')
else:
    print('fonts inlined: 0 (page uses system faces)')

# ---- 2. The site's own stylesheets, in link order ----
css = []
for href in re.findall(r'<link rel="stylesheet" href="([^"]+)"', html):
    p = SITE / href.replace('/ioniq-app/', '')
    if p.exists():
        css.append(f'/* ==== {p.name} ==== */\n' + p.read_text())
        print(f'inlined stylesheet: {p.name} ({p.stat().st_size//1024} KB)')

# ---- 3. head_custom's inline <style> blocks (site typography + sidebar tweaks) ----
head = html.split('</head>')[0]
for s in re.findall(r'<style[^>]*>(.*?)</style>', head, re.S):
    css.append('/* ==== head_custom ==== */\n' + s)

# ---- 4. Body, minus the scripts the preview can't run ----
body = html.split('<body>', 1)[1].rsplit('</body>', 1)[0]
body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.S)
# Site-internal links would 404 outside the site; in-page anchors still work.
body = re.sub(r'href="/ioniq-app/[^"#]*"', 'href="#"', body)
body = re.sub(r'<link[^>]*>', '', body)

page = (
    '<title>How Range and Efficiency Are Calculated — support site preview</title>\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<style>\n' + font_css + '\n' + '\n'.join(css) + '\n</style>\n'
    + body
)
OUT.write_text(page)
print(f'wrote {OUT} ({len(page)//1024} KB)')
