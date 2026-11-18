#!/usr/bin/env python3
"""Apply the portfolio design to book/ux-in-the-real-world.html.
Idempotent: safe to run after every content change. Reads tokens.css and scripts/book.css,
embeds a Latin WOFF2 subset of Schibsted Grotesk so the book works offline as a single file."""
import re, base64, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
bookp = root / 'book' / 'ux-in-the-real-world.html'
s = bookp.read_text(encoding='utf-8')

tokens = (root / 'tokens.css').read_text(encoding='utf-8')
tokens = re.sub(r'@font-face\{.*?\}\s*', '', tokens, flags=re.S)
font = base64.b64encode((root / 'fonts' / 'schibsted-grotesk-latin-wght-normal.woff2').read_bytes()).decode()
face = ('@font-face{font-family:"Schibsted Grotesk";src:url(data:font/woff2;base64,%s) format("woff2");'
        'font-weight:400 900;font-style:normal;font-display:swap}\n' % font)
css = face + tokens + '\n' + (root / 'scripts' / 'book.css').read_text(encoding='utf-8')

# 1. replace the first <style> block, drop Google Fonts
a = s.index('<style>'); b = s.index('</style>', a) + len('</style>')
s = s[:a] + '<style>\n' + css + '\n</style>' + s[b:]
s = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', s)
s = re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>\s*', '', s)

# 1b. inline colours left over from the old palette
s = s.replace('color:#7c848c', 'color:var(--ink-faint)').replace('color:#1f4e5a', 'color:var(--ink)')

# 2. head: theme-colour + pre-paint theme
if 'uxp-theme' not in s:
    s = s.replace('<title>', '<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">\n'
                  '<meta name="theme-color" content="#141514" media="(prefers-color-scheme: dark)">\n'
                  '<script>try{var t=localStorage.getItem(\'uxp-theme\');if(t===\'dark\'||t===\'light\')document.documentElement.setAttribute(\'data-theme\',t)}catch(e){}</script>\n<title>', 1)

# 3. parts from the table of contents
parts = []
for m in re.finditer(r'<div class="toc-part">\s*<p class="toc-part-title">([^<]*)</p>(.*?)</div>', s, re.S):
    title, body = m.group(1), m.group(2)
    if not title.startswith('Part'): continue
    entries = re.findall(r'<a href="#[^"]*" class="toc-entry">.*?</a>', body, re.S)
    parts.append((title, [('toc-new' in e) for e in entries]))
n_new = sum(sum(p[1]) for p in parts); n_all = sum(len(p[1]) for p in parts)

# 4. cover strip: one mark per chapter, grouped by part
grp = ''.join('<span class="grp">' + ''.join('<i class="new"></i>' if n else '<i></i>' for n in flags) + '</span>' for _, flags in parts)
s = re.sub(r'<div class="corpus" aria-hidden="true">.*?</div>', '<div class="corpus" aria-hidden="true">' + grp + '</div>', s, count=1, flags=re.S)
s = re.sub(r'<p class="corpus-key">.*?</p>', '<p class="corpus-key">One mark per chapter, grouped by part. <b>%d of %d are new in this edition</b> (dark marks).</p>' % (n_new, n_all), s, count=1, flags=re.S)

# 5. ids on dividers
roman = {'Part I': 'part-i', 'Part II': 'part-ii', 'Part III': 'part-iii', 'Part IV': 'part-iv', 'Part V': 'part-v', 'Appendix': 'appendix'}
def add_id(m):
    label = m.group(2)
    return '<div class="chapter-divider%s" id="%s">\n  <p class="chapter-number">%s</p>' % (m.group(1), roman.get(label, 'x'), label)
s = re.sub(r'<div class="chapter-divider([^"]*)"(?: id="[^"]*")?>\s*<p class="chapter-number">([^<]*)</p>',
           lambda m: '<div class="chapter-divider%s" id="%s">\n  <p class="chapter-number">%s</p>' % (m.group(1), roman.get(m.group(2), 'x'), m.group(2)), s)

# 6. nav + rail
chev = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align:-2px"><path d="M15 18l-6-6 6-6"/></svg>'
nav = ('<nav class="nav-bar">\n'
       '  <span class="nav-left"><a class="nav-app" href="../#/">' + chev + ' UX Practice</a><a href="#toc">Contents</a><a href="#rules">Rules</a></span>\n'
       '  <span class="nav-title"><span class="mk" aria-hidden="true"><i></i><i></i><i></i></span>UX in the Real World</span>\n'
       '  <span class="nav-right"><a class="nav-ext" href="https://trevorcalabro.substack.com" target="_blank" rel="noopener">Original newsletter</a>\n'
       '  <button class="theme" id="themeBtn" type="button" aria-label="Switch colour theme">'
       '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
       '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg></button></span>\n'
       '  <span class="readbar" id="readbar" aria-hidden="true"></span>\n</nav>')
s = re.sub(r'<nav class="nav-bar">.*?</nav>', nav, s, count=1, flags=re.S)
s = re.sub(r'<aside class="rail".*?</aside>\s*', '', s, flags=re.S)
names = {'Part I': 'Interaction design', 'Part II': 'Research methods', 'Part III': 'Business impact', 'Part IV': 'Career and teams', 'Part V': 'Companion notes'}
rail = '<aside class="rail" aria-label="Contents"><p>Contents</p><ol>'
for (title, flags), key in zip(parts, ['part-i', 'part-ii', 'part-iii', 'part-iv', 'part-v']):
    lab = title.split(' — ')[0]
    rail += '<li><a href="#%s"><span class="rm"><i></i></span><span>%s. %s</span></a></li>' % (key, lab, names.get(lab, title))
rail += '<li><a href="#appendix"><span class="rm"><i></i></span><span>Archive guide</span></a></li>'
rail += '<li><a href="#rules"><span class="rm"><i></i></span><span>Rules to remember</span></a></li></ol></aside>\n'
s = s.replace('</nav>', '</nav>\n' + rail, 1)

# 7. behaviour
ui = '''<!--BOOKUI--><script>
(function(){
  var root=document.documentElement,b=document.getElementById('themeBtn');
  if(b)b.addEventListener('click',function(){var c=root.getAttribute('data-theme');if(!c)c=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';var n=c==='dark'?'light':'dark';root.setAttribute('data-theme',n);try{localStorage.setItem('uxp-theme',n)}catch(e){}});
  var bar=document.getElementById('readbar');
  var targets=['part-i','part-ii','part-iii','part-iv','part-v','appendix','rules'].map(function(i){return document.getElementById(i)});
  var links=Array.prototype.slice.call(document.querySelectorAll('.rail a'));
  function upd(){
    var h=document.documentElement,max=h.scrollHeight-h.clientHeight;
    if(bar)bar.style.width=(max>0?Math.min(1,Math.max(0,h.scrollTop/max))*100:0)+'%';
    var y=window.scrollY+140,cur=-1;
    targets.forEach(function(d,i){if(d&&d.getBoundingClientRect().top+window.scrollY<=y)cur=i});
    links.forEach(function(a,i){a.classList.toggle('cur',i===cur);a.classList.toggle('read',i<cur)});
  }
  addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();
})();
</script><!--/BOOKUI-->'''
s = re.sub(r'<!--BOOKUI-->.*?<!--/BOOKUI-->\s*', '', s, flags=re.S)
s = s.replace('</body>', ui + '\n</body>', 1)

bookp.write_text(s, encoding='utf-8')
print('book restyled: %d chapters in %d parts, %d new; %d bytes' % (n_all, len(parts), n_new, len(s)))
