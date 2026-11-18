"""Add reading progress to the book and write book/chapters.json. Idempotent: re-run after any book edit."""
import json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
bp = root / 'book' / 'ux-in-the-real-world.html'
s = bp.read_text()
css = (root / 'scripts' / 'book-progress.css').read_text()
js = (root / 'scripts' / 'book-progress.js').read_text()

s = re.sub(r'\n?<style id="progress-css">.*?</style>', '', s, flags=re.S)
s = re.sub(r'\n?<!--PROGRESS-->.*?<!--/PROGRESS-->', '', s, flags=re.S)
assert s.count('</head>') == 1 and s.count('</body>') == 1
s = s.replace('</head>', '<style id="progress-css">\n' + css + '</style>\n</head>')
s = s.replace('</body>', '<!--PROGRESS--><script src="../sync.js?v=20261118"></script>\n<script>\n' + js + '</script><!--/PROGRESS-->\n</body>')
bp.write_text(s)

# chapters.json for the landing page
chapters, part = [], ''
for m in re.finditer(r'<div class="chapter-divider[^"]*" id="([^"]+)"|<article class="article" id="([^"]+)">.*?<h3>(.*?)</h3>', s, re.S):
    if m.group(1): part = m.group(1); continue
    if m.group(2) == 'archive-guide': continue
    chapters.append({'id': m.group(2), 'title': re.sub(r'<[^>]+>', '', m.group(3)).strip(), 'part': part})
(root / 'book' / 'chapters.json').write_text(json.dumps(chapters, ensure_ascii=False, indent=0))
print(len(chapters), 'chapters;', len(set(c['part'] for c in chapters)), 'parts')
