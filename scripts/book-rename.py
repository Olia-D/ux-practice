"""One-off: rename the book to 'UX in the Real World' and present it as multi-source."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
def edit(rel, pairs):
    p = root / rel; s = p.read_text()
    for old, new in pairs:
        assert s.count(old) >= 1, (rel, old[:60])
        s = s.replace(old, new)
    p.write_text(s)

AUTHORS = 'Erika Hall, Teresa Torres, Vitaly Friedman, Dan Brown, Abby Covert, Jeremy Bird, Brittany Hobbs, WebAIM, Adrian Raudaschl, Bach et al., the Financial Times, dataschool, Chartability, AI UX Playground and EU guidance'
CSS = '#who .who-lede{font-size:1.1875rem;color:var(--ink);margin-bottom:2rem}\n#who h3.who-name{font-weight:600;font-size:1.25rem;letter-spacing:-.02em;margin:0 0 .75rem;padding-top:1.25rem;border-top:1px solid var(--line)}\n'
edit('book/ux-in-the-real-world.html', [
  ('<title>UX Research in the Wild — The Book</title>', '<title>UX in the Real World</title>'),
  ('</span>UX Research in the Wild</span>', '</span>UX in the Real World</span>'),
  ('<a class="nav-ext" href="https://trevorcalabro.substack.com" target="_blank" rel="noopener">Original newsletter</a>', '<a class="nav-ext" href="#who">Sources</a>'),
  ('Evidence-based UX research and interaction design, distilled from Trevor Calabro’s writing.', 'Evidence-based UX research and interaction design, compiled from practitioners who test their claims.'),
  ('<p class="section-label">Who wrote the original articles</p>\n  <h2>Trevor Calabro</h2>',
   '<p class="section-label">Sources</p>\n  <h2>Where the chapters come from</h2>\n  <p class="who-lede">91 chapters are distilled from Trevor Calabro’s newsletter <em>UX Research in the Wild</em>. 13 companion notes draw on ' + AUTHORS + ', credited on each page.</p>\n  <h3 class="who-name">Main source: Trevor Calabro</h3>'),
  ('<p>Compiled from <a href="https://trevorcalabro.substack.com" target="_blank">trevorcalabro.substack.com</a> — UX Research in the Wild by Trevor Calabro</p>',
   '<p><strong>UX in the Real World</strong> — a personal reference edition compiled from several authors.</p>\n  <p style="margin-top:12px">Main source: <a href="https://trevorcalabro.substack.com" target="_blank" rel="noopener">UX Research in the Wild</a> by Trevor Calabro.</p>'),
  ('#who .section-label{margin-bottom:.4rem}\n', '#who .section-label{margin-bottom:.4rem}\n' + CSS),
  ('<p class="cover-meta">All 182 posts from <a href="https://trevorcalabro.substack.com">trevorcalabro.substack.com</a> (2023–2026) were read for this edition.<br>\n    91 chapters from Calabro, 13 companion notes from other sources, and an archive guide to everything left out.</p>', '<p class="cover-meta">104 chapters: 91 distilled from Trevor Calabro’s newsletter (all 182 posts, 2023–2026, were read) and 13 companion notes from other authors, plus an archive guide to everything left out. <a href="#who">See all sources</a>.</p>'),
])
edit('scripts/book.css', [('#who .section-label{margin-bottom:.4rem}\n', '#who .section-label{margin-bottom:.4rem}\n' + CSS)])
