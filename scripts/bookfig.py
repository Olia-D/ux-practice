"""Figure helpers for book chapters: an SVG for wide screens plus an HTML fallback for phones.
Colours are the book's source palette; book.css recolours them for light and dark themes."""
from html import escape
import textwrap

F = "font-family=\"'Source Sans 3',system-ui,sans-serif\""
BG, INK, FAINT, LINE, OUT, SURF = '#fcfcfa', '#16191c', '#7c848c', '#e4e5e1', '#1f4e5a', '#f0f1ee'
INV = '#fdfdfb'  # text on an ink box; book CSS maps it to the page background so it flips with the theme


def e(s):
    return escape(s, quote=True)


def text(x, y, s, size=11, fill=INK, anchor='start', weight='400'):
    return '<text x="%s" y="%s" %s font-size="%s" fill="%s" text-anchor="%s" font-weight="%s">%s</text>' % (
        x, y, F, size, fill, anchor, weight, e(s))


def lines(x, y, s, width, size=10, fill=FAINT, anchor='start', weight='400', lh=14):
    out = []
    for i, ln in enumerate(textwrap.wrap(s, width)):
        out.append(text(x, y + i * lh, ln, size, fill, anchor, weight))
    return ''.join(out), len(textwrap.wrap(s, width))


def svg(w, h, title, body):
    return ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" role="img" aria-label="%s">'
            '<rect width="%d" height="%d" fill="%s"/>%s%s</svg>') % (
        w, h, w, h, e(title), w, h, BG, text(w / 2, 22, title, 11, FAINT, 'middle', '600'), body)


def figure(wide, narrow, caption):
    return ('\n  <figure class="illustration">\n    <div class="fig-wide">%s</div>%s\n'
            '    <figcaption>%s</figcaption>\n  </figure>\n') % (wide, narrow, caption)


def rows(title, items, caption, hi=None):
    """Label + description rows. hi = index of the row to mark in green."""
    h = 40 + 46 * len(items)
    b = ''
    for i, (lab, desc) in enumerate(items):
        y = 36 + 46 * i
        b += '<line x1="20" y1="%d" x2="640" y2="%d" stroke="%s"/>' % (y, y, LINE)
        b += '<rect x="20" y="%d" width="2" height="32" fill="%s"/>' % (y, OUT if (hi is None or hi == i) else LINE)
        b += text(40, y + 24, lab, 11, INK, 'start', '600')
        b += text(215, y + 24, desc, 10, FAINT)
    narrow = '<div class="fig-narrow"><p class="fig-title">%s</p><ul class="fn-layers">%s</ul></div>' % (
        e(title), ''.join('<li><strong>%s</strong><span>%s</span></li>' % (e(a), e(d)) for a, d in items))
    return figure(svg(660, h, title, b), narrow, caption)


def flow(title, steps, caption, loop=False):
    """Boxes left to right with arrows. steps = [(label, desc)]. loop draws a return arrow."""
    n = len(steps)
    gap = 26
    bw = (620 - gap * (n - 1)) / n
    wrapw = max(14, int(bw / 5.6))
    maxl = max(len(textwrap.wrap(d, wrapw)) for _, d in steps)
    bh = 44 + 14 * maxl
    h = 40 + bh + (46 if loop else 20)
    b = ''
    for i, (lab, desc) in enumerate(steps):
        x = 20 + i * (bw + gap)
        b += '<rect x="%.1f" y="40" width="%.1f" height="%d" rx="6" fill="%s" stroke="%s"/>' % (
            x, bw, bh, SURF if i else INK, LINE if i else INK)
        b += text(x + 12, 62, lab, 11, INV if i == 0 else INK, 'start', '600')
        t, _ = lines(x + 12, 80, desc, wrapw, 10, INV if i == 0 else FAINT)
        b += t
        if i < n - 1:
            ax = x + bw + 4
            b += '<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1.5"/>' % (ax, 40 + bh / 2, ax + gap - 10, 40 + bh / 2, INK)
            b += '<path d="M%.1f %.1f l-6 -4 v8 z" fill="%s"/>' % (ax + gap - 6, 40 + bh / 2, INK)
    if loop:
        y = 40 + bh + 22
        b += '<path d="M%.1f %d V%d H%.1f V%d" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="4 3"/>' % (
            20 + (n - 1) * (bw + gap) + bw / 2, 40 + bh + 4, y, 20 + bw / 2, 40 + bh + 8, OUT)
        b += '<path d="M%.1f %d l-4 7 h8 z" fill="%s"/>' % (20 + bw / 2, 40 + bh + 2, OUT)
        b += text(330, y + 16, loop, 10, OUT, 'middle', '600')
    narrow = '<div class="fig-narrow"><p class="fig-title">%s</p><ol class="fn-flow">%s</ol>%s</div>' % (
        e(title), ''.join('<li><strong>%s</strong><span>%s</span></li>' % (e(a), e(d)) for a, d in steps),
        ('<p class="fn-axis">↻ %s</p>' % e(loop)) if loop else '')
    return figure(svg(660, h, title, b), narrow, caption)


def compare(title, left, right, caption):
    """left/right = (label, [items]); left is the weaker practice."""
    n = max(len(left[1]), len(right[1]))
    h = 76 + 22 * n + 14
    b = '<line x1="20" y1="64" x2="320" y2="64" stroke="%s"/><line x1="340" y1="64" x2="640" y2="64" stroke="%s"/>' % (LINE, LINE)
    b += text(36, 54, left[0], 10, FAINT, 'start', '600') + text(356, 54, right[0], 10, OUT, 'start', '600')
    for i, it in enumerate(left[1]):
        b += text(36, 84 + 22 * i, '✕  ' + it, 11, INK)
    for i, it in enumerate(right[1]):
        b += text(356, 84 + 22 * i, '✓  ' + it, 11, INK)
    card = lambda cls, lab, items, mark: '<div class="fn-card %s"><p class="fn-label">%s</p><ul>%s</ul></div>' % (
        cls, e(lab), ''.join('<li><span aria-hidden="true">%s</span>%s</li>' % (mark, e(i)) for i in items))
    narrow = '<div class="fig-narrow"><p class="fig-title">%s</p>%s%s</div>' % (
        e(title), card('bad', left[0], left[1], '✕'), card('good', right[0], right[1], '✓'))
    return figure(svg(660, h, title, b), narrow, caption)


def matrix(title, xlab, ylab, quads, caption, hi=1):
    """quads in reading order: top-left, top-right, bottom-left, bottom-right; each (label, desc). hi = highlighted index."""
    b = ''
    x0, y0, w, hh = 70, 44, 270, 92
    for i, (lab, desc) in enumerate(quads):
        x = x0 + (i % 2) * (w + 10)
        y = y0 + (i // 2) * (hh + 10)
        on = i == hi
        b += '<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="%s" stroke="%s"/>' % (x, y, w, hh, INK if on else SURF, INK if on else LINE)
        b += text(x + 14, y + 26, lab, 12, INV if on else INK, 'start', '600')
        t, _ = lines(x + 14, y + 46, desc, 44, 10, INV if on else FAINT)
        b += t
    b += text(x0 + w + 5, y0 + 2 * hh + 10 + 26, xlab, 10, FAINT, 'middle', '600')
    b += '<text x="40" y="%d" %s font-size="10" fill="%s" text-anchor="middle" font-weight="600" transform="rotate(-90 40 %d)">%s</text>' % (
        y0 + hh + 5, F, FAINT, y0 + hh + 5, e(ylab))
    narrow = '<div class="fig-narrow"><p class="fig-title">%s</p><p class="fn-axis">%s · %s</p><div class="fn-matrix">%s</div></div>' % (
        e(title), e(ylab), e(xlab), ''.join('<div%s><strong>%s</strong><span>%s</span></div>' % (' class="hi"' if i == hi else '', e(a), e(d)) for i, (a, d) in enumerate(quads)))
    return figure(svg(660, y0 + 2 * hh + 10 + 40, title, b), narrow, caption)


def tree(title, root, opps, target_children, solutions, tests, caption):
    """Opportunity solution tree: root outcome; opps (3, middle is the target); target's children;
    solutions under the chosen child; tests under the first solution."""
    W = 660
    b = ''
    def box(x, y, w, h, lab, kind):
        fill, stroke, col = {'root': (INK, INK, INV), 'target': (BG, OUT, INK), 'n': (SURF, LINE, INK), 'test': (BG, LINE, FAINT)}[kind]
        s = '<rect x="%d" y="%d" width="%d" height="%d" rx="6" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, fill, stroke, 2 if kind == 'target' else 1)
        t, _ = lines(x + w / 2, y + 17, lab, int(w / 5.4), 10, col, 'middle', '600' if kind != 'test' else '400', 13)
        return s + t
    def link(x1, y1, x2, y2):
        return '<path d="M%d %d V%d H%d V%d" fill="none" stroke="%s"/>' % (x1, y1, (y1 + y2) // 2, x2, y2, FAINT)
    # rows: y positions
    b += box(230, 36, 200, 34, root, 'root')
    xs = [24, 237, 450]
    for i, o in enumerate(opps):
        b += link(330, 70, xs[i] + 93, 92)
        b += box(xs[i], 92, 186, 40, o, 'target' if i == 1 else 'n')
    cx = [150, 340]
    for i, c in enumerate(target_children):
        b += link(330, 132, cx[i] + 85, 154)
        b += box(cx[i], 154, 170, 40, c, 'target' if i == 0 else 'n')
    sx = [40, 240, 440]
    for i, s in enumerate(solutions):
        b += link(235, 194, sx[i] + 90, 216)
        b += box(sx[i], 216, 180, 34, s, 'n')
    tx = [20, 150]
    for i, t in enumerate(tests):
        b += link(130, 250, tx[i] + 60, 272)
        b += box(tx[i], 272, 120, 34, t, 'test')
    b += text(640, 292, 'Green = the target opportunity.', 9, FAINT, 'end')
    b += text(640, 305, 'Solutions grow only under it.', 9, FAINT, 'end')
    narrow = ('<div class="fig-narrow"><p class="fig-title">%s</p><ol class="fn-flow">'
              '<li><strong>Outcome</strong><span>%s</span></li>'
              '<li><strong>Opportunities</strong><span>%s (target: %s)</span></li>'
              '<li><strong>Sub-opportunities</strong><span>%s (target: %s)</span></li>'
              '<li><strong>Solutions</strong><span>%s</span></li>'
              '<li><strong>Assumption tests</strong><span>%s</span></li></ol></div>') % (
        e(title), e(root), e(' · '.join(opps)), e(opps[1]), e(' · '.join(target_children)), e(target_children[0]),
        e(' · '.join(solutions)), e(' · '.join(tests)))
    return figure(svg(W, 320, title, b), narrow, caption)
