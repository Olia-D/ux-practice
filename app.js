/* UX Practice – learn-then-test app for the book UX in the Real World.
   Static SPA. Content in content/*.json. */
(function () {
  'use strict';

  var KEY = 'uxp-progress-v1';
  var app = document.getElementById('app');
  var summaryEl = document.getElementById('rank');
  var manifest = null;
  var cache = {};
  var progress = loadProgress();
  var session = null;

  // ---------- storage ----------
  var S = window.UXSync;
  function loadProgress() {
    if (S) return S.getApp();
    try { var p = JSON.parse(localStorage.getItem(KEY)); return (p && typeof p === 'object' && !Array.isArray(p)) ? p : {}; } catch (e) { return {}; }
  }
  function saveProgress() {
    if (S) S.setApp(progress);
    else try { localStorage.setItem(KEY, JSON.stringify(progress)); } catch (e) {}
    renderSummary();
  }
  function rec(id) { progress.items = progress.items || {}; return progress.items[id] = progress.items[id] || {}; }

  // ---------- missed-question bank ----------
  // progress.missed = { "<articleId>#<questionIndex>": rightInARow }
  // A reference is dropped once it has been answered correctly twice.
  function missedBank() { progress.missed = progress.missed || {}; return progress.missed; }
  function missedKey(aid, qi) { return aid + '#' + qi; }
  function noteMissed(aid, qi) { missedBank()[missedKey(aid, qi)] = 0; }
  function noteCorrect(aid, qi) {
    var b = missedBank(), k = missedKey(aid, qi);
    if (!(k in b)) return;
    b[k] += 1;
    if (b[k] >= 2) delete b[k];
  }
  function missedRefs(filterIds) {
    var b = missedBank(), out = [];
    Object.keys(b).forEach(function (k) {
      var p = k.split('#'), aid = p[0], qi = parseInt(p[1], 10);
      if (filterIds && filterIds.indexOf(aid) < 0) return;
      out.push({ aid: aid, qi: qi, streak: b[k] });
    });
    return out;
  }
  function pruneMissed() {
    if (!manifest) return;
    var live = {};
    manifest.modules.forEach(function (m) { m.articles.forEach(function (x) { live[x.id] = true; }); });
    var b = missedBank(), changed = false;
    Object.keys(b).forEach(function (k) { if (!live[k.split('#')[0]]) { delete b[k]; changed = true; } });
    if (changed) saveProgress();
  }

  // ---------- header summary ----------
  function renderSummary() {
    if (!summaryEl) return;
    if (!manifest) { summaryEl.textContent = ''; return; }
    var items = progress.items || {}, done = 0, total = 0;
    manifest.modules.forEach(function (mod) {
      mod.articles.forEach(function (a) {
        total++;
        var r = items[a.id + '/test'];
        if (r && r.best != null) done++;
      });
    });
    if (total === 0) { summaryEl.textContent = ''; return; }
    summaryEl.innerHTML = '<b>' + done + '</b> of ' + total + ' done';
  }

  // ---------- icons ----------
  function svg(path, extra) { return '<svg class="ico' + (extra ? ' ' + extra : '') + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + path + '</svg>'; }
  var ICON = {
    back: svg('<path d="M15 18l-6-6 6-6"/>'),
    chev: svg('<path d="M9 18l6-6-6-6"/>'),
    check: svg('<path d="M20 6L9 17l-5-5"/>', 'ok'),
    x: svg('<path d="M18 6L6 18M6 6l12 12"/>'),
    out: svg('<path d="M7 17L17 7M8 7h9v9"/>')
  };
  function setupTheme() {
    var b = document.getElementById('theme'); if (!b) return;
    b.addEventListener('click', function () {
      var root = document.documentElement, cur = root.getAttribute('data-theme');
      if (!cur) cur = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      var next = cur === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('uxp-theme', next); } catch (e) {}
    });
  }

  // ---------- text helpers ----------
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fmt(s) {
    var h = esc(s);
    h = h.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
    h = h.replace(/→/g, '<span style="color:var(--mute)">→</span>');
    h = h.replace(/❌/g, '<span style="color:var(--ink-faint)">✗</span>');
    h = h.replace(/✅/g, '<span style="color:var(--out-text)">✓</span>');
    return h.replace(/\n/g, '<br>');
  }

  // ---------- visuals ----------
  function visual(v) {
    if (!v) return '';
    if (v.type === 'compare') {
      return '<div class="vis"><div class="compare-grid">' +
        '<div class="compare-box left"><div class="compare-label">' + esc(v.left.label) + '</div><ul class="compare-items">' +
        v.left.items.map(function (i) { return '<li>' + esc(i) + '</li>'; }).join('') + '</ul></div>' +
        '<div class="compare-box right"><div class="compare-label">' + esc(v.right.label) + '</div><ul class="compare-items">' +
        v.right.items.map(function (i) { return '<li>' + esc(i) + '</li>'; }).join('') + '</ul></div>' +
        '</div></div>';
    }
    return '';
  }

  // ---------- question rendering ----------
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  function renderQuestion(q, box, onDone) {
    var order = shuffle(q.options.map(function (_, i) { return i; }));
    var name = 'q' + Math.random().toString(36).slice(2, 8);
    var html = '<div class="qrow"><div class="q">' + fmt(q.q) + '</div></div>' + visual(q.visual);
    html += '<div class="opts" role="radiogroup" aria-label="Answer options">';
    order.forEach(function (oi) {
      html += '<label class="opt" data-i="' + oi + '"><input type="radio" name="' + name + '" value="' + oi + '"><span class="otext">' + fmt(q.options[oi]) + '</span><span class="mark2"></span></label>';
    });
    html += '</div>';
    if (q.hint) html += '<details class="note hint"><summary>Hint</summary>' + fmt(q.hint) + '</details>';
    html += '<div class="fbwrap" aria-live="polite"></div><div class="row end"><button class="btn check" type="button">Check</button></div>';
    box.innerHTML = html;

    box.classList.add('guard');
    setTimeout(function () { box.classList.remove('guard'); }, 400);

    var checkBtn = box.querySelector('.check'), fbw = box.querySelector('.fbwrap'), answered = false;
    function current() { var c = box.querySelector('input:checked'); return c ? +c.value : -1; }
    function refresh() {
      if (answered) return;
      if (current() >= 0 && fbw.querySelector('.need')) fbw.innerHTML = '';
      Array.prototype.forEach.call(box.querySelectorAll('.opt'), function (l) { l.classList.toggle('sel', l.querySelector('input').checked); });
    }
    box.addEventListener('change', refresh);
    checkBtn.addEventListener('click', function () {
      if (answered) return;
      var c = current(), ok = c === q.answer;
      if (c < 0) { fbw.innerHTML = '<div class="fb need">Pick an answer first.</div>'; return; }
      answered = true;
      Array.prototype.forEach.call(box.querySelectorAll('input'), function (i) { i.disabled = true; });
      Array.prototype.forEach.call(box.querySelectorAll('.opt'), function (l) {
        var i = +l.getAttribute('data-i'), isRight = i === q.answer, picked = l.querySelector('input').checked, mk = l.querySelector('.mark2');
        if (isRight && picked) { l.classList.add('right'); mk.innerHTML = ICON.check + 'Correct'; }
        else if (isRight) { l.classList.add('right'); mk.innerHTML = ICON.check + 'Correct answer'; }
        else if (picked) { l.classList.add('wrong'); mk.innerHTML = ICON.x + 'Your answer'; }
      });
      var msg;
      if (ok) msg = '<span class="head">Right.</span>' + (q.explain ? fmt(q.explain) : '');
      else msg = '<span class="head">Not quite.</span>The answer is <b>' + fmt(q.options[q.answer]) + '</b>' + (q.explain ? '<br>' + fmt(q.explain) : '');
      fbw.innerHTML = '<div class="fb ' + (ok ? 'ok' : 'no') + ' pop">' + msg + '</div>';
      checkBtn.remove();
      onDone(ok, fbw);
    });
  }

  // ---------- data loading ----------
  function getJSON(url) { return fetch(url, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(url); return r.json(); }); }
  function loadManifest() { return manifest ? Promise.resolve(manifest) : getJSON('content/manifest.json').then(function (m) { manifest = m; return m; }); }
  function loadArticle(file) {
    if (cache[file]) return Promise.resolve(cache[file]);
    return getJSON(file).then(function (d) { cache[file] = d; return d; });
  }

  // ---------- views ----------
  function scoreLabel(best, total) {
    if (best == null) return '<span class="note">Not done yet</span>';
    return '<span class="note">' + best + '/' + total + ' correct</span>';
  }
  function setView(html) { app.innerHTML = html; window.scrollTo(0, 0); try { app.focus({ preventScroll: true }); } catch (e) {} }

  function moduleProgress(mod) {
    var items = progress.items || {}, done = 0, total = 0;
    mod.articles.forEach(function (a) {
      total++;
      var r = items[a.id + '/test'];
      if (r && r.best != null) done++;
    });
    return { done: done, total: total, pct: total ? Math.round(100 * done / total) : 0 };
  }

  // The strip: one mark per article. Grey = not started, dark grey = learned, green = done.
  function stripFor(mod) {
    var items = progress.items || {};
    return '<div class="strip" aria-hidden="true">' + mod.articles.map(function (a) {
      var l = items[a.id + '/learn'] || {}, t = items[a.id + '/test'] || {};
      var done = l.done && t.best != null;
      return '<i class="' + (done ? 'd' : (l.done || t.best != null) ? 'l' : '') + '"></i>';
    }).join('') + '</div>';
  }

  // ---------- HOME VIEW ----------
  function viewHome() {
    loadManifest().then(function (m) {
      renderSummary();
      pruneMissed();
      var totalDone = 0, totalAll = 0;
      var nArt = 0; m.modules.forEach(function (x) { nArt += x.articles.length; });
      var html = '<a class="crumb" href="#/">' + ICON.back + 'Home</a><h1 class="statement">Learn the ideas. <span>Then test yourself.</span></h1>';
      html += '<p class="sub">Key concepts from the book UX in the Real World: Trevor Calabro\'s research writing plus companion notes from other authors.</p>';
      html += '<p class="pace">Suggested pace: one article a day, four days a week. Read the cards, then take the quiz. ' + nArt + ' articles across ' + m.modules.length + ' modules.</p>';

      m.modules.forEach(function (mod, mi) {
        var p = moduleProgress(mod);
        totalDone += p.done; totalAll += p.total;
        var unlocked = mi === 0 || moduleProgress(m.modules[mi - 1]).pct >= 50;

        html += '<a class="mod-card' + (unlocked ? '' : ' locked') + '" href="' + (unlocked ? '#/m/' + mod.id : '#/') + '"' + (unlocked ? '' : ' aria-disabled="true"') + '>' +
          '<div class="mod-head"><div class="mod-info">' +
          '<div class="mod-week">' + esc(mod.week) + '</div>' +
          '<div class="mod-title">' + esc(mod.name) + '</div>' +
          '<div class="mod-sub">' + esc(mod.subtitle) + '</div>' +
          '</div><div class="mod-count' + (p.done === p.total && p.total ? ' done' : '') + '">' + p.done + '<small>/' + p.total + '</small></div></div>' +
          stripFor(mod) +
          (unlocked ? '' : '<div class="note" style="margin-top:8px">Finish half of ' + esc(m.modules[mi - 1].name) + ' first</div>') +
          '</a>';
      });

      var nMissed = missedRefs().length;
      html += '<div class="tools home-tools"><a class="toolrow" href="#/review"><span><b>Review missed questions</b>'
           + (nMissed ? '<span class="note"> · ' + nMissed + ' waiting</span>' : '<span class="note"> · nothing yet</span>')
           + '</span><span class="chev">' + ICON.chev + '</span></a>'
           + '<a class="toolrow" href="#/index"><span><b>Concept index</b><span class="note"> · every learn card</span></span><span class="chev">' + ICON.chev + '</span></a>'
           + '</div>';
      if (totalAll) {
        var totalPct = Math.round(100 * totalDone / totalAll);
        html += '<div class="overall"><span class="muted">Overall, ' + totalDone + ' of ' + totalAll + ' articles done</span><span class="big num' + (totalPct === 100 ? ' done' : '') + '">' + totalPct + '%</span></div>';
      }

      html += syncLine();
      setView(html);
    }).catch(showError);
  }

  // ---------- LANDING ----------
  var BOOK = 'book/ux-in-the-real-world.html';
  var chapters = null;
  function loadChapters() {
    return chapters ? Promise.resolve(chapters) : getJSON('book/chapters.json').then(function (c) { chapters = c; return c; });
  }
  function bookState() { return S ? S.getBook() : { read: {} }; }
  function isRead(b, id) { var r = b.read[id]; return !!(r && r.r); }

  function timeAgo(ms) {
    if (!ms) return '';
    var s = Math.round((Date.now() - ms) / 1000);
    if (s < 45) return 'just now';
    var m = Math.round(s / 60); if (m < 60) return m + ' min ago';
    var h = Math.round(m / 60); if (h < 24) return h + ' h ago';
    var d = Math.round(h / 24); return d === 1 ? 'yesterday' : d + ' days ago';
  }
  function syncLine() {
    var st = S ? S.state() : { status: 'local' };
    var dot = '<span class="sdot ' + st.status + '" aria-hidden="true"></span>';
    if (st.status === 'local') return '<p class="syncline">' + dot + '<span>Progress is saved on this device only.</span> <a href="#/sync">Sync across devices</a></p>';
    if (st.status === 'error') return '<p class="syncline">' + dot + '<span>Sync paused: ' + esc(st.error) + '</span> <a href="#/sync">Fix</a></p>';
    if (st.status === 'syncing') return '<p class="syncline">' + dot + '<span>Syncing…</span> <a href="#/sync">Sync settings</a></p>';
    return '<p class="syncline">' + dot + '<span>Synced across your devices' + (st.at ? ', ' + timeAgo(st.at) : '') + '.</span> <a href="#/sync">Sync settings</a></p>';
  }

  // Next practice step: the first unfinished article in an unlocked module.
  function nextPractice(m) {
    var items = progress.items || {}, found = null;
    m.modules.forEach(function (mod, mi) {
      if (found) return;
      var unlocked = mi === 0 || moduleProgress(m.modules[mi - 1]).pct >= 50;
      if (!unlocked) return;
      mod.articles.forEach(function (a) {
        if (found || !a.file) return;
        var l = items[a.id + '/learn'] || {}, t = items[a.id + '/test'] || {};
        if (!l.done) found = { a: a, href: '#/a/' + a.id + '/learn/0', verb: 'Learn' };
        else if (t.best == null) found = { a: a, href: '#/a/' + a.id + '/test', verb: 'Quiz' };
      });
    });
    return found;
  }

  function viewLanding() {
    Promise.all([loadManifest(), loadChapters().catch(function () { return []; }), loadLibrary().catch(function () { return { skills: [] }; })]).then(function (r) {
      var m = r[0], ch = r[1], L = r[2], b = bookState();
      renderSummary();
      var nRead = ch.filter(function (c) { return isRead(b, c.id); }).length;
      var last = b.last && ch.filter(function (c) { return c.id === b.last.id; })[0];

      var html = '<section class="hero"><h1 class="statement">Evidence-based UX.<br><span>Read it, practise it, use it at work.</span></h1>' +
        '<p class="sub">A reference book, a learn-then-test practice app and a set of Claude skills, all built from the same research.</p></section>';

      // Book
      var bstrip = '<div class="strip grouped" aria-hidden="true">', part = null;
      ch.forEach(function (c) {
        if (c.part !== part) { if (part !== null) bstrip += '</span>'; bstrip += '<span class="grp">'; part = c.part; }
        bstrip += '<i class="' + (isRead(b, c.id) ? 'd' : last && c.id === last.id ? 'cur' : '') + '"></i>';
      });
      bstrip += (part !== null ? '</span>' : '') + '</div>';
      html += '<section class="door" aria-labelledby="d-book">' +
        '<div class="door-head"><div><p class="door-kind">Book</p><h2 id="d-book">UX in the Real World</h2></div>' +
        '<p class="door-count num"><b' + (nRead && nRead === ch.length ? ' class="done"' : '') + '>' + nRead + '</b><small>/' + ch.length + ' read</small></p></div>' +
        '<p class="door-sub">' + ch.length + ' chapters on interaction design, research methods, business impact and the UX career, with figures and a rules cheat sheet.</p>' +
        bstrip +
        '<div class="row door-actions">' +
        (last ? '<a class="btn" href="' + BOOK + '#resume">Continue reading</a>' : '<a class="btn" href="' + BOOK + '#part-i">Start reading</a>') +
        '<a class="btn secondary" href="' + BOOK + '#toc">Contents</a></div>' +
        (last ? '<p class="note door-where">You were in <b>' + esc(last.title) + '</b>' + (b.last.t ? ', ' + timeAgo(b.last.t) : '') + '.</p>' : '') +
        '</section>';

      // Practice
      var nArt = 0, nDone = 0;
      var pstrip = '<div class="strip grouped" aria-hidden="true">';
      m.modules.forEach(function (mod) {
        var p = moduleProgress(mod); nArt += p.total; nDone += p.done;
        pstrip += '<span class="grp">' + stripFor(mod).replace(/^<div class="strip" aria-hidden="true">|<\/div>$/g, '') + '</span>';
      });
      pstrip += '</div>';
      var nx = nextPractice(m), nMissed = missedRefs().length;
      html += '<section class="door" aria-labelledby="d-practice">' +
        '<div class="door-head"><div><p class="door-kind">Practice</p><h2 id="d-practice">Learn, then test yourself</h2></div>' +
        '<p class="door-count num"><b' + (nDone && nDone === nArt ? ' class="done"' : '') + '>' + nDone + '</b><small>/' + nArt + ' done</small></p></div>' +
        '<p class="door-sub">' + nArt + ' short articles in ' + m.modules.length + ' modules. Read a few cards, then answer 5 questions. About 10 minutes each.</p>' +
        pstrip +
        '<div class="row door-actions">' +
        (nx ? '<a class="btn" href="' + nx.href + '">' + (nDone || (progress.items && Object.keys(progress.items).length) ? 'Continue' : 'Start') + ': ' + esc(nx.a.title) + '</a>' : '') +
        '<a class="btn secondary" href="#/practice">All modules</a></div>' +
        '<p class="note door-where"><a href="#/review">Review missed questions</a>' + (nMissed ? ' (' + nMissed + ')' : '') + ' · <a href="#/index">Concept index</a></p>' +
        '</section>';

      // Skills
      html += '<section class="door" aria-labelledby="d-skills">' +
        '<div class="door-head"><div><p class="door-kind">Claude skills</p><h2 id="d-skills">Use the rules at work</h2></div>' +
        '<p class="door-count num"><b>' + L.skills.length + '</b><small> skills</small></p></div>' +
        '<p class="door-sub">The book’s rules packaged for Claude: design reviews, research planning, UX writing, AI features, charts and Jobs to Be Done.</p>' +
        '<ul class="skill-list">' + L.skills.map(function (s) {
          return '<li><a href="#/library/skill/' + esc(s.id) + '"><b>' + esc(s.title) + '</b><span>' + esc(s.blurb) + '</span></a></li>';
        }).join('') + '</ul>' +
        '<div class="row door-actions"><a class="btn secondary" href="#/library">All skills and downloads</a></div>' +
        '</section>';

      html += syncLine();
      setView(html);
    }).catch(showError);
  }

  // ---------- SYNC ----------
  function viewSync() {
    var st = S ? S.state() : { status: 'local' }, on = S && S.connected();
    var html = '<a class="crumb" href="#/">' + ICON.back + 'Home</a>' +
      '<h1>Sync progress</h1>' +
      '<p class="sub">Your reading and practice progress is saved in this browser. Connect a private GitHub gist and it stays the same on your laptop, phone and any other device.</p>';
    if (on) {
      html += '<div class="panel sync-panel"><p class="sync-state"><span class="sdot ' + st.status + '" aria-hidden="true"></span>' +
        (st.status === 'error' ? 'Sync paused' : st.status === 'syncing' ? 'Syncing…' : 'Connected') + '</p>' +
        '<p class="note">' + (st.status === 'error' ? esc(st.error) : st.at ? 'Last synced ' + timeAgo(st.at) + '. ' : '') +
        'Progress syncs on its own when you finish a chapter or a quiz, and when you come back to the page.</p>' +
        '<div class="row lib-actions"><button class="btn small" type="button" id="sync-now">Sync now</button>' +
        '<button class="btn small secondary" type="button" id="sync-off">Disconnect this device</button></div></div>' +
        '<h2>Add another device</h2><p>Open this page on the other device and paste the same token. Keep the token in your password manager so it’s easy to find.</p>';
    } else {
      html += '<ol class="steps">' +
        '<li><h3>Create a token on GitHub</h3><p>The link opens GitHub with only the <b>gist</b> permission ticked. Choose an expiry, press <b>Generate token</b> at the bottom, and copy the token.</p>' +
        '<a class="btn small secondary" href="' + (S ? S.tokenUrl : '#') + '" target="_blank" rel="noopener">Create token on GitHub ' + ICON.out + '</a></li>' +
        '<li><h3>Paste it here</h3><form id="sync-form" class="sync-form" autocomplete="off"><label for="tok" class="sr">GitHub token</label>' +
        '<input id="tok" class="idxfilter" type="password" placeholder="ghp_…" spellcheck="false" autocapitalize="off" required>' +
        '<button class="btn" type="submit">Connect</button></form><div class="fbwrap" aria-live="polite"></div></li>' +
        '<li><h3>Do the same on your other devices</h3><p>Use the same token everywhere. Save it in your password manager so it’s easy to paste on your phone.</p></li></ol>';
    }
    html += '<p class="note">The token is stored only in this browser and can only read and write your gists. Progress lives in a secret gist named <code>' + (S ? S.fileName : '') + '</code> in your GitHub account; secret gists are unlisted, not encrypted, so the file holds nothing but chapter and quiz progress.</p>';
    html += '<details class="backup-section"><summary class="note">Backup without GitHub</summary>' +
      '<p class="note">Copy your practice progress as text and paste it on another device, or start over.</p>' +
      '<div class="row" style="gap:8px;margin:8px 0"><button class="btn small secondary" id="export-btn">Copy progress</button>' +
      '<button class="btn small secondary" id="import-btn">Paste progress</button>' +
      '<button class="btn small secondary" id="reset-btn">Reset practice progress</button></div></details>';
    setView(html);
    bindBackup();
    var f = document.getElementById('sync-form');
    if (f) f.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = f.querySelector('button'), fb = f.parentNode.querySelector('.fbwrap');
      btn.disabled = true; btn.textContent = 'Connecting…'; fb.innerHTML = '';
      S.connect(document.getElementById('tok').value).then(function () {
        progress = loadProgress(); viewSync();
      }, function (err) {
        btn.disabled = false; btn.textContent = 'Connect';
        fb.innerHTML = '<div class="fb no"><span class="head">Couldn’t connect.</span>' + esc(err.message) + '</div>';
      });
    });
    var sn = document.getElementById('sync-now');
    if (sn) sn.addEventListener('click', function () { sn.disabled = true; sn.textContent = 'Syncing…'; S.syncNow().then(function () { progress = loadProgress(); viewSync(); }, function () { viewSync(); }); });
    var so = document.getElementById('sync-off');
    if (so) so.addEventListener('click', function () {
      if (confirm('Disconnect this device? Progress stays on this device and in your gist; it just stops syncing here.')) { S.disconnect(); viewSync(); }
    });
  }

  // ---------- MODULE VIEW ----------
  function viewModule(mid) {
    loadManifest().then(function (m) {
      var mod = m.modules.filter(function (x) { return x.id === mid; })[0];
      if (!mod) return viewHome();
      var mp = moduleProgress(mod);
      var html = '<a class="crumb" href="#/practice">' + ICON.back + 'All modules</a>';
      html += '<h1>' + esc(mod.name) + '</h1>';
      html += '<p class="sub">' + esc(mod.subtitle) + '</p>';
      html += stripFor(mod) + '<p class="note" style="margin:8px 0 var(--phi-2)">' + mp.done + ' of ' + mp.total + ' articles done</p>';

      mod.articles.forEach(function (a, i) {
        var r = (progress.items || {})[a.id + '/test'] || {};
        var learned = (progress.items || {})[a.id + '/learn'] || {};
        var hasContent = !!a.file;
        var quizDone = r.best != null;

        var articleDone = learned.done && quizDone;
        var artPct = articleDone ? 100 : (learned.done ? 50 : 0);
        html += '<div class="art">' +
          '<div class="art-n num">' + (i + 1) + '</div><div>' +
          '<h3>' + esc(a.title) + (articleDone ? ICON.check + '<span class="sr">Done</span>' : '') + '</h3>' +
          '<p class="art-sum">' + esc(a.summary) + '</p>' +
          (hasContent ? '<div class="art-actions">' +
            '<a class="btn small' + (learned.done ? ' secondary' : '') + '" href="#/a/' + a.id + '/learn/0">' + (learned.done ? 'Review cards' : 'Start learning') + '</a>' +
            '<a class="btn small secondary" href="#/a/' + a.id + '/test">' + (quizDone ? 'Retake quiz' : 'Quiz') + '</a>' +
            '<span class="score">' + (quizDone ? r.best + ' of ' + (a.q || 5) + ' correct' : (a.q || 5) + ' questions') + '</span>' +
          '</div>' : '<p class="note" style="margin-top:8px">Content coming soon</p>') +
          (a.source ? '<div class="source"><a href="' + esc(a.source) + '" target="_blank" rel="noopener">Read the original article ' + ICON.out + '</a></div>'
                    : a.sourceNote ? '<div class="source">Source: ' + esc(a.sourceNote) + '</div>' : '') +
          '</div></div>';
      });
      var mr = (progress.items || {})['module/' + mod.id] || {};
      var mMissed = missedRefs(mod.articles.map(function (x) { return x.id; })).length;
      html += '<div class="modreview"><div class="row between"><h3 style="margin:0">Module review</h3>' +
        (mr.reviewed ? '<span class="pill">Reviewed</span>' : '') + '</div>' +
        '<p class="muted" style="margin:4px 0 0">10 questions drawn across this module' +
        (mMissed ? ', weighted toward the ' + mMissed + ' you have missed' : '') + '.' +
        (mr.last != null ? ' Last time: ' + mr.last + '/' + mr.of + '.' : '') + '</p>' +
        '<div class="row end" style="margin-top:10px"><a class="btn' + (mr.reviewed ? ' secondary' : '') + '" href="#/m/' + mod.id + '/review">' +
        (mr.reviewed ? 'Review again' : 'Start review') + '</a></div></div>';
      setView(html);
    }).catch(showError);
  }

  // ---------- LEARN VIEW ----------
  function viewLearn(aid, idx) {
    loadManifest().then(function (m) {
      var art = null, file = null, modId = null;
      m.modules.forEach(function (mod) { mod.articles.forEach(function (a) { if (a.id === aid) { art = a; file = a.file; modId = mod.id; } }); });
      if (!art || !file) return showError(new Error('Article not found'));
      return loadArticle(file).then(function (d) {
        var t = d.topics[0];
        if (!t) return showError(new Error('No content'));
        idx = Math.max(0, Math.min(idx, t.learn.length - 1));
        var c = t.learn[idx], last = idx === t.learn.length - 1;
        var dots = '<div class="strip cards" role="img" aria-label="Card ' + (idx + 1) + ' of ' + t.learn.length + '">' + t.learn.map(function (_, i) { return '<i class="' + (i <= idx ? 'on' : '') + '"></i>'; }).join('') + '</div>';

        var html = '<a class="crumb" href="#/m/' + (modId || d.module) + '">' + ICON.back + esc(art.title) + '</a>' +
          dots + '<p class="note num" style="margin:8px 0 0">Card ' + (idx + 1) + ' of ' + t.learn.length + '</p>' +
          '<div class="learn-card pop"><h2>' + fmt(c.title) + '</h2>' +
          '<div class="learn-text">' + fmt(c.text) + '</div>' +
          visual(c.visual) +
          (c.try ? '<div class="try-wrap"><h4>Quick check</h4><div class="trybox"></div></div>' : '') +
          '</div>' +
          '<div class="row between">' +
          (idx > 0 ? '<a class="btn secondary small" href="#/a/' + aid + '/learn/' + (idx - 1) + '">Back</a>' : '<span></span>') +
          (last ? '<a class="btn" href="#/a/' + aid + '/test">Take the quiz</a>' : '<a class="btn" href="#/a/' + aid + '/learn/' + (idx + 1) + '">Next</a>') +
          '</div>';
        setView(html);

        if (c.try) {
          var tb = app.querySelector('.trybox');
          var runTry = function () {
            renderQuestion(c.try, tb, function (ok, fbw) {
              if (ok) return;
              var r = document.createElement('div'); r.className = 'row end';
              r.innerHTML = '<button class="btn secondary small" type="button">Try again</button>';
              fbw.parentNode.appendChild(r);
              r.querySelector('button').addEventListener('click', runTry);
            });
          };
          runTry();
        }
        if (last) { var r = rec(aid + '/learn'); if (!r.done) { r.done = true; r.updated = new Date().toISOString(); saveProgress(); } }
      });
    }).catch(showError);
  }

  // ---------- QUIZ ----------
  var SKEY = 'uxp-session-v1';
  function saveSession() {
    try { sessionStorage.setItem(SKEY, JSON.stringify({ aid: session.aid, idxs: session.idxs, pos: session.pos, right: session.right, missed: session.missed, retry: session.retry })); } catch (e) {}
  }
  function clearSession() { try { sessionStorage.removeItem(SKEY); } catch (e) {} }
  function readSession(aid) {
    try { var s = JSON.parse(sessionStorage.getItem(SKEY)); if (s && s.aid === aid && !s.retry && s.pos <= s.idxs.length) return s; } catch (e) {}
    return null;
  }

  function startQuiz(aid, onlyIdx) {
    loadManifest().then(function (m) {
      var art = null, file = null, modId = null;
      m.modules.forEach(function (mod) { mod.articles.forEach(function (a) { if (a.id === aid) { art = a; file = a.file; modId = mod.id; } }); });
      if (!art || !file) return showError(new Error('Article not found'));
      return loadArticle(file).then(function (d) {
        var t = d.topics[0];
        if (!t || !t.test) return showError(new Error('No quiz'));
        var all = t.test;
        var saved = onlyIdx ? null : readSession(aid);
        var idxs = onlyIdx || all.map(function (_, i) { return i; });
        if (!onlyIdx && !saved) idxs = shuffle(idxs);
        session = { aid: aid, modId: modId, art: art, all: all, idxs: idxs, pos: 0, right: 0, missed: [], retry: !!onlyIdx };
        if (saved && saved.idxs.every(function (i) { return i < all.length; })) {
          session.idxs = saved.idxs; session.pos = saved.pos; session.right = saved.right; session.missed = saved.missed;
        }
        renderQuizStep();
      });
    }).catch(showError);
  }

  // A mixed session draws questions from several articles.
  // items: [{aid, qi, q, title}]; label shows in the crumb.
  function startMixed(items, label, backHash) {
    if (!items.length) { location.hash = backHash || '#/'; return; }
    session = {
      aid: null, modId: null, mixed: true, label: label, back: backHash || '#/',
      art: { title: label }, all: items.map(function (x) { return x.q; }),
      srcIds: items.map(function (x) { return x.aid; }),
      srcQis: items.map(function (x) { return x.qi; }),
      idxs: items.map(function (_, i) { return i; }), pos: 0, right: 0, missed: [], retry: false
    };
    renderQuizStep();
  }

  // Collect quiz questions for a set of article ids, in manifest order.
  function collectQuestions(ids) {
    return loadManifest().then(function (m) {
      var arts = [];
      m.modules.forEach(function (mod) { mod.articles.forEach(function (a) { if (ids.indexOf(a.id) >= 0) arts.push(a); }); });
      return Promise.all(arts.map(function (a) {
        return loadArticle(a.file).then(function (d) { return { a: a, d: d }; }, function () { return null; });
      })).then(function (rows) {
        var out = {};
        rows.forEach(function (r) {
          if (!r) return;
          var t = r.d.topics && r.d.topics[0];
          if (t && t.test) out[r.a.id] = { title: r.a.title, test: t.test };
        });
        return out;
      });
    });
  }

  function renderQuizStep() {
    var s = session, n = s.idxs.length;
    if (s.pos >= n) return renderQuizEnd();
    saveSession();
    var q = s.all[s.idxs[s.pos]];
    var back = s.mixed ? s.back : '#/m/' + s.modId;
    var srcLine = s.mixed && s.srcTitles ? '<p class="note" style="margin:0 0 4px">From <b>' + esc(s.srcTitles[s.pos]) + '</b></p>' : '';
    var html = '<div class="row between"><a class="crumb cancel" href="' + back + '">' + ICON.back + 'Stop</a><span class="note">' + (s.retry ? 'Retry · ' : '') + esc(s.art.title) + '</span></div>' +
      '<div class="progress strip cards" role="img" aria-label="Question ' + (s.pos + 1) + ' of ' + n + '">' + s.idxs.map(function (_, i) { return '<i class="' + (i <= s.pos ? 'on' : '') + '"></i>'; }).join('') + '</div>' +
      '<p class="note num" style="margin:8px 0 4px">Question ' + (s.pos + 1) + ' of ' + n + '</p>' + srcLine +
      '<div class="qbox pop"></div>';
    setView(html);
    renderQuestion(q, app.querySelector('.qbox'), function (ok, fbw) {
      var qi = s.idxs[s.pos];
      // In a mixed session idxs are positions in the picked list, so the bank
      // key has to come from the question's own article and index.
      var bankId = s.mixed ? s.srcIds[s.pos] : s.aid;
      var bankQi = s.mixed ? s.srcQis[s.pos] : qi;
      if (ok) { s.right++; noteCorrect(bankId, bankQi); }
      else { s.missed.push(qi); noteMissed(bankId, bankQi); }
      saveProgress();
      s.pos++; saveSession();
      var b = document.createElement('div'); b.className = 'row end';
      b.innerHTML = '<button class="btn nextq" type="button">' + (s.pos < n ? 'Next' : 'See results') + '</button>';
      fbw.parentNode.appendChild(b);
      var nb = b.querySelector('button'), used = false;
      nb.addEventListener('click', function () { if (used) return; used = true; renderQuizStep(); });
      try { nb.focus({ preventScroll: true }); } catch (e) {}
      try { b.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); } catch (e) {}
    });
  }

  function renderQuizEnd() {
    var s = session, n = s.idxs.length;
    clearSession();
    var ratio = s.right / n;
    if (s.mixed) return renderMixedEnd(s, n, ratio);
    var key = s.aid + '/test', r = rec(key);
    try { history.replaceState(null, '', '#/m/' + s.modId); } catch (e) {}
    if (!s.retry) { r.best = Math.max(r.best || 0, s.right); r.last = s.right; }
    r.updated = new Date().toISOString();
    saveProgress();
    var msg = s.right === n ? 'All correct.' : ratio >= 0.7 ? 'Solid. You got the key ideas.' : 'Worth another pass — the learn cards will help.';
    var m = s.missed.length;
    var retryLabel = m === 1 ? 'Retry missed question' : 'Retry ' + m + ' missed';
    var learnBtn = m ? '<a class="btn' + (ratio < 0.5 ? '' : ' secondary') + ' wide" href="#/a/' + s.aid + '/learn/0">Review learn cards</a>' : '';
    var retryBtn = m ? '<button class="btn' + (ratio < 0.5 ? ' secondary' : '') + ' wide retry" type="button">' + retryLabel + '</button>' : '';
    var html = '<div class="result pop"><p class="score num' + (ratio >= 0.7 ? ' pass' : '') + '">' + s.right + '<small> of ' + n + '</small></p>' +
      '<p class="msg">' + msg + '</p></div>' +
      '<div class="stack">' + (ratio < 0.5 ? learnBtn + retryBtn : retryBtn + learnBtn) +
      '<a class="btn secondary wide" href="#/m/' + s.modId + '">Back to module</a></div>';
    setView(html);
    var rb = app.querySelector('.retry');
    if (rb) rb.addEventListener('click', function () { startQuiz(s.aid, s.missed.slice()); });
  }

  function renderMixedEnd(s, n, ratio) {
    if (s.modId) { var mr = rec('module/' + s.modId); mr.reviewed = true; mr.last = s.right; mr.of = n; mr.updated = new Date().toISOString(); }
    saveProgress();
    var left = missedRefs().length;
    var msg = s.right === n ? 'All correct.' : ratio >= 0.7 ? 'Solid. You got the key ideas.' : 'Worth another pass — the learn cards will help.';
    var html = '<div class="result pop"><p class="score num' + (ratio >= 0.7 ? ' pass' : '') + '">' + s.right + '<small> of ' + n + '</small></p>' +
      '<p class="msg">' + msg + '</p>' +
      '<p class="note">' + (left ? left + ' question' + (left === 1 ? '' : 's') + ' still in your review list.' : 'Your review list is empty.') + '</p></div>' +
      '<div class="stack">' + (left ? '<a class="btn wide" href="#/review">Review missed questions</a>' : '') +
      '<a class="btn secondary wide" href="' + s.back + '">Back</a></div>';
    setView(html);
  }

  // ---------- REVIEW: the missed-question bank ----------
  function reviewItems() {
    var refs = missedRefs();
    if (!refs.length) return Promise.resolve([]);
    var ids = refs.map(function (r) { return r.aid; }).filter(function (v, i, arr) { return arr.indexOf(v) === i; });
    return collectQuestions(ids).then(function (byId) {
      var items = [];
      refs.forEach(function (r) {
        var row = byId[r.aid];
        if (row && row.test[r.qi]) items.push({ aid: r.aid, qi: r.qi, q: row.test[r.qi], title: row.title });
      });
      return items;
    });
  }

  function runReview() {
    reviewItems().then(function (items) {
      if (!items.length) { location.hash = '#/review'; return; }
      var pick = shuffle(items).slice(0, 12);
      startMixed(pick, 'Review', '#/review');
      session.srcTitles = pick.map(function (x) { return x.title; });
      renderQuizStep();
    }).catch(showError);
  }

  function viewReview() {
    reviewItems().then(function (items) {
      if (!items.length) {
        return setView('<a class="crumb" href="#/practice">' + ICON.back + 'All modules</a>' +
          '<h1>Nothing to review</h1>' +
          '<p class="sub">Questions you get wrong land here. They leave once you answer them right twice.</p>');
      }
      var byArticle = {};
      items.forEach(function (x) { byArticle[x.title] = (byArticle[x.title] || 0) + 1; });
      var list = Object.keys(byArticle).sort().map(function (t) {
        return '<li>' + esc(t) + ' <span class="note">\u00b7 ' + byArticle[t] + '</span></li>';
      }).join('');
      setView('<a class="crumb" href="#/practice">' + ICON.back + 'All modules</a>' +
        '<h1>Review</h1>' +
        '<p class="sub">' + items.length + ' question' + (items.length === 1 ? '' : 's') + ' you have missed. Each one leaves this list after two correct answers.</p>' +
        '<ul class="review-list">' + list + '</ul>' +
        '<div class="row" style="margin-top:var(--phi-2)"><a class="btn" href="#/review/run">Start review</a></div>');
    }).catch(showError);
  }

  // ---------- MODULE REVIEW QUIZ ----------
  function viewModuleReview(modId) {
    loadManifest().then(function (m) {
      var mod = null;
      m.modules.forEach(function (x) { if (x.id === modId) mod = x; });
      if (!mod) return showError(new Error('Module not found'));
      var ids = mod.articles.map(function (a) { return a.id; });
      return collectQuestions(ids).then(function (byId) {
        var missedSet = {};
        missedRefs(ids).forEach(function (r) { missedSet[r.aid + '#' + r.qi] = true; });
        var pool = [], weighted = [];
        ids.forEach(function (aid) {
          var row = byId[aid];
          if (!row) return;
          row.test.forEach(function (q, qi) {
            var item = { aid: aid, qi: qi, q: q, title: row.title };
            (missedSet[aid + '#' + qi] ? weighted : pool).push(item);
          });
        });
        var pick = shuffle(weighted).slice(0, 10);
        pick = pick.concat(shuffle(pool).slice(0, Math.max(0, 10 - pick.length)));
        pick = shuffle(pick);
        if (!pick.length) return showError(new Error('No questions in this module'));
        startMixed(pick, mod.name + ' review', '#/m/' + modId);
        session.modId = modId;
        session.srcTitles = pick.map(function (x) { return x.title; });
        renderQuizStep();
      });
    }).catch(showError);
  }

  // ---------- CONCEPT INDEX ----------
  function viewIndex() {
    loadManifest().then(function (m) {
      var all = [];
      m.modules.forEach(function (mod) { mod.articles.forEach(function (a) { all.push({ mod: mod, a: a }); }); });
      return Promise.all(all.map(function (row) {
        return loadArticle(row.a.file).then(function (d) { return { row: row, d: d }; }, function () { return null; });
      })).then(function (rows) {
        var html = '<a class="crumb" href="#/practice">' + ICON.back + 'All modules</a>' +
          '<h1>Concept index</h1>' +
          '<p class="sub">Every learn card in the app. Tap one to open it.</p>' +
          '<input class="idxfilter" type="search" placeholder="Filter concepts" aria-label="Filter concepts">' +
          '<div class="idxresults">';
        var curMod = null;
        rows.forEach(function (r) {
          if (!r) return;
          var t = r.d.topics && r.d.topics[0];
          if (!t) return;
          if (curMod !== r.row.mod.id) {
            if (curMod !== null) html += '</div>';
            curMod = r.row.mod.id;
            html += '<div class="card idxmod"><p class="idxmodname">' + esc(r.row.mod.name) + '</p>';
          }
          t.learn.forEach(function (c, i) {
            html += '<a class="idxrow" href="#/a/' + r.row.a.id + '/learn/' + i + '">' +
              '<span class="idxcard">' + esc(c.title) + '</span>' +
              '<span class="idxart">' + esc(r.row.a.title) + '</span></a>';
          });
        });
        html += curMod !== null ? '</div></div>' : '</div>';
        setView(html);
        var f = app.querySelector('.idxfilter');
        if (f) f.addEventListener('input', function () {
          var q = this.value.trim().toLowerCase();
          Array.prototype.forEach.call(app.querySelectorAll('.idxrow'), function (el) {
            el.style.display = !q || el.textContent.toLowerCase().indexOf(q) >= 0 ? '' : 'none';
          });
          Array.prototype.forEach.call(app.querySelectorAll('.idxmod'), function (el) {
            var any = el.querySelector('.idxrow:not([style*="none"])');
            el.style.display = any ? '' : 'none';
          });
        });
      });
    }).catch(showError);
  }

  // ---------- LIBRARY (book + skills) ----------
  var libCache = null;
  function loadLibrary() {
    if (libCache) return Promise.resolve(libCache);
    return fetch('skills/index.json').then(function (r) { if (!r.ok) throw new Error('Could not load the library'); return r.json(); })
      .then(function (d) { libCache = d; return d; });
  }
  function dlBtn(href, label, cls) {
    var name = href.split('/').pop();
    return '<a class="btn small ' + (cls || '') + '" href="' + esc(href) + '" download="' + esc(name) + '">' + label + '</a>';
  }
  function viewLibrary() {
    loadLibrary().then(function (L) {
      var b = L.book;
      var html = '<a class="crumb" href="#/">' + ICON.back + 'Home</a>' +
        '<h1>Claude skills</h1><p class="sub">' + L.skills.length + ' skills that bring the book’s rules into your work with Claude. Read each one here, or download it and add it to Claude.</p>' +
        '<div class="row lib-actions">' + dlBtn(L.all, 'Download all skills') + '<a class="btn small secondary" href="#/library/guide">How to install them</a></div>';
      L.skills.forEach(function (s) {
        html += '<div class="card lib-item"><h3>' + esc(s.title) + '</h3><p class="note">' + esc(s.blurb) + '</p>' +
          '<div class="row lib-actions"><a class="btn small" href="#/library/skill/' + esc(s.id) + '">Read</a>' +
          dlBtn('downloads/skill-' + s.id + '.zip', 'Download zip', 'secondary') + '</div></div>';
      });
      html += '<p class="note">Upload one zip per skill on claude.ai under Settings → Skills. For Claude Code, unzip into <code>~/.claude/skills/&lt;name&gt;/</code>.</p>';
      html += '<div class="card lib-item"><p class="lib-kicker">The book as a file</p><h3>' + esc(b.title) + '</h3><p class="note">' + esc(b.blurb) + '</p>' +
        '<div class="row lib-actions">' + dlBtn(b.download, 'Download HTML', 'secondary') + dlBtn(b.zip, 'Download zip', 'ghost') + '</div></div>';
      setView(html);
    }).catch(showError);
  }
  function viewDoc(path, back, backLabel, extra) {
    fetch(path).then(function (r) { if (!r.ok) throw new Error('Could not load ' + path); return r.text(); }).then(function (md) {
      var html = '<a class="crumb" href="' + back + '">' + ICON.back + esc(backLabel) + '</a>' + (extra || '') +
        '<article class="md">' + (mdBase = path, renderMd(md)) + '</article>' +
        '<a class="crumb" href="' + back + '">' + ICON.back + esc(backLabel) + '</a>';
      setView(html);
    }).catch(showError);
  }
  function viewSkill(id, ref) {
    loadLibrary().then(function (L) {
      var s = L.skills.filter(function (x) { return x.id === id; })[0];
      if (!s) { location.hash = '#/library'; return; }
      if (ref) {
        if ((s.refs || []).indexOf(ref) < 0) { location.hash = '#/library/skill/' + id; return; }
        return viewDoc('skills/' + id + '/references/' + ref + '.md', '#/library/skill/' + id, s.title);
      }
      var bar = '<div class="card lib-item"><h2 class="lib-title">' + esc(s.title) + '</h2><p class="note">' + esc(s.blurb) + '</p>' +
        '<div class="row lib-actions">' + dlBtn('downloads/skill-' + id + '.zip', 'Download zip') +
        dlBtn('skills/' + id + '/SKILL.md', 'Download SKILL.md', 'secondary') + '</div>';
      if (s.refs && s.refs.length) {
        bar += '<p class="note lib-refs">Reference files: ' + s.refs.map(function (r) {
          return '<a href="#/library/skill/' + id + '/' + r + '">' + esc(r.replace(/-/g, ' ')) + '</a>';
        }).join(' · ') + '</p>';
      }
      bar += '</div>';
      viewDoc('skills/' + id + '/SKILL.md', '#/library', 'All skills', bar);
    }).catch(showError);
  }

  // Small Markdown renderer for skill files: frontmatter, headings, lists, tables, code, quotes, inline marks.
  var mdBase = '';
  function resolveRel(base, rel) {
    var parts = base.split('/').slice(0, -1);
    rel.split('/').forEach(function (seg) { if (seg === '..') parts.pop(); else if (seg && seg !== '.') parts.push(seg); });
    return parts.join('/');
  }
  function mdInline(s) {
    var codes = [];
    var h = esc(s).replace(/`([^`]+)`/g, function (_, c) { codes.push(c); return '\u0000' + (codes.length - 1) + '\u0000'; });
    h = h.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, function (_, txt, url) {
      var safe = /^(https?:|#|mailto:)/.test(url) ? url : (/^[\w.\/-]+$/.test(url) ? resolveRel(mdBase, url) : '#');
      var ext = /^https?:/.test(url) ? ' target="_blank" rel="noopener"' : '';
      return '<a href="' + safe + '"' + ext + '>' + txt + '</a>';
    });
    h = h.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/(^|[\s(])\*([^*\s][^*]*?)\*(?=[\s.,;:)!?]|$)/g, '$1<i>$2</i>');
    return h.replace(/\u0000(\d+)\u0000/g, function (_, i) { return '<code>' + codes[+i] + '</code>'; });
  }
  function renderMd(md) {
    var lines = md.replace(/\r/g, '').split('\n'), out = [], i = 0, meta = '';
    if (lines[0] === '---') {
      var j = lines.indexOf('---', 1);
      if (j > 0) {
        lines.slice(1, j).forEach(function (l) {
          var m = l.match(/^description:\s*"?(.*?)"?$/);
          if (m) meta = m[1].replace(/\\"/g, '"');
        });
        lines = lines.slice(j + 1);
      }
    }
    if (meta) out.push('<p class="md-desc">' + mdInline(meta) + '</p>');
    var para = [];
    function flush() { if (para.length) { out.push('<p>' + mdInline(para.join(' ')) + '</p>'); para = []; } }
    while (i < lines.length) {
      var l = lines[i], m;
      if (/^```/.test(l)) {
        flush(); var buf = []; i++;
        while (i < lines.length && !/^```/.test(lines[i])) buf.push(lines[i++]);
        i++; out.push('<pre><code>' + esc(buf.join('\n')) + '</code></pre>'); continue;
      }
      if ((m = l.match(/^(#{1,4})\s+(.*)/))) { flush(); var n = Math.min(m[1].length + 1, 5); out.push('<h' + n + '>' + mdInline(m[2]) + '</h' + n + '>'); i++; continue; }
      if (/^\s*\|/.test(l)) {
        flush(); var rows = [];
        while (i < lines.length && /^\s*\|/.test(lines[i])) rows.push(lines[i++]);
        var cells = function (r) { return r.trim().replace(/^\||\|$/g, '').split('|').map(function (c) { return c.trim(); }); };
        var t = '<div class="md-table"><table>';
        rows.forEach(function (r, ri) {
          if (/^\s*\|?\s*:?-{2,}/.test(r)) return;
          var tag = ri === 0 ? 'th' : 'td';
          t += '<tr>' + cells(r).map(function (c) { return '<' + tag + '>' + mdInline(c) + '</' + tag + '>'; }).join('') + '</tr>';
        });
        out.push(t + '</table></div>'); continue;
      }
      if (/^\s*([-*]|\d+\.)\s+/.test(l)) {
        flush(); var ordered = /^\s*\d+\./.test(l), items = [];
        while (i < lines.length && (/^\s*([-*]|\d+\.)\s+/.test(lines[i]) || (/^\s{2,}\S/.test(lines[i]) && items.length))) {
          var ln = lines[i++];
          if (/^\s*([-*]|\d+\.)\s+/.test(ln)) items.push(ln.replace(/^\s*([-*]|\d+\.)\s+/, ''));
          else items[items.length - 1] += ' ' + ln.trim();
        }
        var tg = ordered ? 'ol' : 'ul';
        out.push('<' + tg + '>' + items.map(function (x) { return '<li>' + mdInline(x) + '</li>'; }).join('') + '</' + tg + '>'); continue;
      }
      if (/^>\s?/.test(l)) {
        flush(); var q = [];
        while (i < lines.length && /^>\s?/.test(lines[i])) q.push(lines[i++].replace(/^>\s?/, ''));
        out.push('<blockquote>' + mdInline(q.join(' ')) + '</blockquote>'); continue;
      }
      if (/^\s*(-{3,}|\*{3,})\s*$/.test(l)) { flush(); out.push('<hr>'); i++; continue; }
      if (!l.trim()) { flush(); i++; continue; }
      para.push(l.trim()); i++;
    }
    flush();
    return out.join('\n');
  }

  // ---------- backup ----------
  function bindBackup() {
    var exp = document.getElementById('export-btn');
    var imp = document.getElementById('import-btn');
    var rst = document.getElementById('reset-btn');
    if (exp) exp.addEventListener('click', function () {
      var data = JSON.stringify(progress);
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(data).then(function () { exp.textContent = 'Copied!'; setTimeout(function () { exp.textContent = 'Copy progress'; }, 2000); });
      } else {
        prompt('Copy this:', data);
      }
    });
    if (imp) imp.addEventListener('click', function () {
      var raw = prompt('Paste your progress data:');
      if (!raw) return;
      try {
        var d = JSON.parse(raw);
        if (d && typeof d === 'object') { progress = d; saveProgress(); route(); }
      } catch (e) { alert('Could not read that data. Make sure you pasted the full text.'); }
    });
    if (rst) rst.addEventListener('click', function () {
      if (confirm('Reset all practice progress? This also clears it on your synced devices and cannot be undone.')) {
        progress = { resetAt: new Date().toISOString() }; saveProgress(); route();
      }
    });
  }

  // ---------- error ----------
  function showError(e) {
    setView('<div class="card empty"><p><b>Something went wrong.</b></p><p class="muted">' + esc(e && e.message || '') + '</p><a class="btn" href="#/">Home</a></div>');
  }

  // ---------- router ----------
  function route() {
    var h = location.hash.replace(/^#\/?/, '').split('/');
    if (h[0] === 'review') return h[1] === 'run' ? runReview() : viewReview();
    if (h[0] === 'index') return viewIndex();
    if (h[0] === 'practice') return viewHome();
    if (h[0] === 'sync') return viewSync();
    if (h[0] === 'library') {
      if (h[1] === 'guide') return loadLibrary().then(function (L) { viewDoc(L.guide, '#/library', 'All skills'); }).catch(showError);
      if (h[1] === 'skill' && h[2]) return viewSkill(h[2], h[3]);
      return viewLibrary();
    }
    if (h[0] === 'm' && h[1]) {
      if (h[2] === 'review') return viewModuleReview(h[1]);
      return viewModule(h[1]);
    }
    if (h[0] === 'a' && h[1]) {
      if (h[2] === 'learn') return viewLearn(h[1], parseInt(h[3] || '0', 10) || 0);
      if (h[2] === 'test') return startQuiz(h[1]);
    }
    return viewLanding();
  }
  function markNav() {
    var h = location.hash.replace(/^#\/?/, '').split('/')[0];
    var cur = h === 'library' ? 'skills' : (h === 'm' || h === 'a' || h === 'practice' || h === 'review' || h === 'index') ? 'practice' : '';
    Array.prototype.forEach.call(document.querySelectorAll('.topnav a'), function (a) {
      if (a.getAttribute('data-nav') === cur) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
  }

  document.addEventListener('click', function (e) {
    var l = e.target.closest && e.target.closest('a[href^="#"]');
    if (!l) return;
    if (l.classList.contains('cancel')) clearSession();
    // If the hash is already the same, hashchange won't fire — route manually
    if (l.getAttribute('href') === location.hash) {
      e.preventDefault();
      route();
    }
  });

  window.addEventListener('hashchange', function () { markNav(); route(); });
  // Progress merged in from another device or another tab: refresh overview pages, never a running quiz.
  if (S) {
    S.onChange(function () {
      progress = loadProgress(); renderSummary();
      var h = location.hash.replace(/^#\/?/, '').split('/')[0];
      if (!session && (h === '' || h === 'practice' || h === 'm')) route();
    });
    S.onStatus(function () {
      var el = app.querySelector('.syncline');
      if (el) { var t = document.createElement('div'); t.innerHTML = syncLine(); el.parentNode.replaceChild(t.firstChild, el); }
    });
  }
  markNav();
  setupTheme();
  renderSummary();
  route();
})();
