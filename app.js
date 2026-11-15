/* UX Practice – learn-then-test app for UX Research in the Wild.
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
  function loadProgress() {
    try { var p = JSON.parse(localStorage.getItem(KEY)); return (p && typeof p === 'object' && !Array.isArray(p)) ? p : {}; } catch (e) { return {}; }
  }
  function saveProgress() {
    try { localStorage.setItem(KEY, JSON.stringify(progress)); } catch (e) {}
    renderSummary();
  }
  function rec(id) { progress.items = progress.items || {}; return progress.items[id] = progress.items[id] || {}; }

  // ---------- header summary ----------
  function renderSummary() {
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
    summaryEl.innerHTML = '<b>' + done + '/' + total + '</b> articles done';
  }

  // ---------- text helpers ----------
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function fmt(s) {
    var h = esc(s);
    h = h.replace(/\*\*(.+?)\*\*/g, '<b>$1</b>');
    h = h.replace(/→/g, '<span style="color:var(--accent)">→</span>');
    h = h.replace(/❌/g, '<span style="color:var(--warm)">✗</span>');
    h = h.replace(/✅/g, '<span style="color:var(--ok)">✓</span>');
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
      html += '<label class="opt" data-i="' + oi + '"><input type="radio" name="' + name + '" value="' + oi + '"><span class="otext">' + fmt(q.options[oi]) + '</span><span class="mark" aria-hidden="true"></span></label>';
    });
    html += '</div>';
    if (q.hint) html += '<details class="note hint"><summary>Hint</summary>' + fmt(q.hint) + '</details>';
    html += '<div class="fbwrap" aria-live="polite"></div><div class="row end"><button class="btn check" type="button" disabled>Check</button></div>';
    box.innerHTML = html;

    box.classList.add('guard');
    setTimeout(function () { box.classList.remove('guard'); }, 400);

    var checkBtn = box.querySelector('.check'), fbw = box.querySelector('.fbwrap'), answered = false;
    function current() { var c = box.querySelector('input:checked'); return c ? +c.value : -1; }
    function refresh() {
      if (answered) return;
      checkBtn.disabled = current() < 0;
      Array.prototype.forEach.call(box.querySelectorAll('.opt'), function (l) { l.classList.toggle('sel', l.querySelector('input').checked); });
    }
    box.addEventListener('change', refresh);
    checkBtn.addEventListener('click', function () {
      if (answered) return;
      var c = current(), ok = c === q.answer;
      answered = true;
      Array.prototype.forEach.call(box.querySelectorAll('input'), function (i) { i.disabled = true; });
      Array.prototype.forEach.call(box.querySelectorAll('.opt'), function (l) {
        var i = +l.getAttribute('data-i'), isRight = i === q.answer, picked = l.querySelector('input').checked, mk = l.querySelector('.mark');
        if (isRight && picked) { l.classList.add('right'); mk.textContent = '✓'; }
        else if (isRight) { l.classList.add('right'); mk.textContent = '✓ Correct'; }
        else if (picked) { l.classList.add('wrong'); mk.textContent = '✗'; }
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

  // ---------- HOME VIEW ----------
  function viewHome() {
    loadManifest().then(function (m) {
      renderSummary();
      var totalDone = 0, totalAll = 0;
      var html = '<h1>UX Practice</h1>';
      html += '<p class="sub">Key concepts from Trevor Calabro\'s UX Research in the Wild. Learn the ideas, then test yourself.</p>';
      html += '<div class="schedule-hint"><b>Suggested pace:</b> 1 article per day, 4 days a week. Read the cards, take the quiz. About 6 weeks total.</div>';

      m.modules.forEach(function (mod, mi) {
        var p = moduleProgress(mod);
        totalDone += p.done; totalAll += p.total;
        var unlocked = mi === 0 || moduleProgress(m.modules[mi - 1]).pct >= 50;

        html += '<a class="card tile mod-card' + (unlocked ? '' : ' locked') + '" href="' + (unlocked ? '#/m/' + mod.id : '#/') + '">' +
          '<div class="mod-head"><div class="mod-icon">' + mod.icon + '</div><div class="mod-info">' +
          '<div class="mod-week">' + esc(mod.week) + '</div>' +
          '<div class="mod-title">' + esc(mod.name) + '</div>' +
          '<div class="mod-sub">' + esc(mod.subtitle) + '</div>' +
          '</div></div>' +
          '<div class="mod-progress"><div class="mod-bar"><i style="width:' + p.pct + '%"></i></div><span class="mod-pct">' + p.done + '/' + p.total + '</span></div>' +
          (unlocked ? '' : '<div class="note" style="margin-top:6px">Finish half of ' + esc(m.modules[mi - 1].name) + ' first</div>') +
          '</a>';
      });

      if (totalAll) {
        var totalPct = Math.round(100 * totalDone / totalAll);
        html += '<div class="card" style="text-align:center"><p class="muted">Overall: ' + totalDone + ' of ' + totalAll + ' articles done</p><div class="mod-progress"><div class="mod-bar"><i style="width:' + totalPct + '%"></i></div><span class="mod-pct">' + totalPct + '%</span></div></div>';
      }

      // progress backup
      html += '<details class="backup-section"><summary class="note">Progress backup</summary>' +
        '<p class="note">Your progress saves in this browser automatically. Use backup to move it to another device or keep a copy.</p>' +
        '<div class="row" style="gap:8px;margin:8px 0"><button class="btn small secondary" id="export-btn">Copy progress</button>' +
        '<button class="btn small secondary" id="import-btn">Paste progress</button>' +
        '<button class="btn small secondary" id="reset-btn" style="color:var(--warm)">Reset</button></div>' +
        '</details>';

      setView(html);
      bindBackup();
    }).catch(showError);
  }

  // ---------- MODULE VIEW ----------
  function viewModule(mid) {
    loadManifest().then(function (m) {
      var mod = m.modules.filter(function (x) { return x.id === mid; })[0];
      if (!mod) return viewHome();
      var mp = moduleProgress(mod);
      var html = '<a class="crumb" href="#/">← All modules</a>';
      html += '<h1>' + esc(mod.name) + '</h1>';
      html += '<p class="sub">' + esc(mod.subtitle) + '</p>';
      html += '<div class="mod-progress" style="margin-bottom:12px"><div class="mod-bar"><i style="width:' + mp.pct + '%"></i></div><span class="mod-pct">' + mp.done + '/' + mp.total + ' done</span></div>';

      mod.articles.forEach(function (a, i) {
        var r = (progress.items || {})[a.id + '/test'] || {};
        var learned = (progress.items || {})[a.id + '/learn'] || {};
        var hasContent = !!a.file;
        var quizDone = r.best != null;

        var articleDone = learned.done && quizDone;
        var artPct = articleDone ? 100 : (learned.done ? 50 : 0);
        html += '<div class="card' + (articleDone ? ' done' : '') + '">' +
          '<div class="row between"><h3>' + (articleDone ? '✓ ' : '') + esc(a.title) + '</h3><span class="pill">' + (i + 1) + '</span></div>' +
          '<div class="art-progress"><i style="width:' + artPct + '%"></i></div>' +
          '<p class="muted" style="margin:4px 0 0">' + esc(a.summary) + '</p>' +
          (hasContent ? '<ul class="steps">' +
            '<li class="step"><span class="lbl">Learn' + (learned.done ? ' <span class="note">· done</span>' : '') + '</span>' +
              '<a class="btn small' + (learned.done ? ' secondary' : '') + '" href="#/a/' + a.id + '/learn/0">' + (learned.done ? 'Review' : 'Start') + '</a></li>' +
            '<li class="step"><span class="lbl">Quiz · 5 questions<br>' + scoreLabel(r.best, 5) + '</span>' +
              '<a class="btn small' + (quizDone ? ' secondary' : '') + '" href="#/a/' + a.id + '/test">' + (quizDone ? 'Retake' : 'Start') + '</a></li>' +
          '</ul>' : '<p class="note" style="margin-top:8px">Content coming soon</p>') +
          '<div class="source"><a href="' + esc(a.source) + '" target="_blank">Read original article ↗</a></div>' +
          '</div>';
      });
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
        var dots = '<div class="dots" aria-label="Card ' + (idx + 1) + ' of ' + t.learn.length + '">' + t.learn.map(function (_, i) { return '<i class="' + (i <= idx ? 'on' : '') + '"></i>'; }).join('') + '</div>';

        var html = '<a class="crumb" href="#/m/' + (modId || d.module) + '">← ' + esc(art.title) + '</a>' +
          '<p class="note" style="margin:0">Card ' + (idx + 1) + ' of ' + t.learn.length + '</p>' + dots +
          '<div class="learn-card pop"><h2>' + fmt(c.title) + '</h2>' +
          '<div class="learn-text">' + fmt(c.text) + '</div>' +
          visual(c.visual) +
          (c.try ? '<div class="try-wrap"><h4>Quick check</h4><div class="trybox"></div></div>' : '') +
          '</div>' +
          '<div class="row between">' +
          (idx > 0 ? '<a class="btn secondary small" href="#/a/' + aid + '/learn/' + (idx - 1) + '">← Back</a>' : '<span></span>') +
          (last ? '<a class="btn" href="#/a/' + aid + '/test">Take the quiz →</a>' : '<a class="btn" href="#/a/' + aid + '/learn/' + (idx + 1) + '">Next →</a>') +
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
        if (last) { var r = rec(aid + '/learn'); if (!r.done) { r.done = true; saveProgress(); } }
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

  function renderQuizStep() {
    var s = session, n = s.idxs.length;
    if (s.pos >= n) return renderQuizEnd();
    saveSession();
    var q = s.all[s.idxs[s.pos]];
    var html = '<div class="row between"><a class="crumb cancel" href="#/m/' + s.modId + '">← Stop</a><span class="note">' + (s.retry ? 'Retry · ' : '') + esc(s.art.title) + '</span></div>' +
      '<div class="progress" aria-hidden="true"><i style="width:' + Math.round(100 * s.pos / n) + '%"></i></div>' +
      '<p class="note" style="margin:0 0 4px">' + (s.pos + 1) + ' of ' + n + '</p>' +
      '<div class="card qbox pop"></div>';
    setView(html);
    renderQuestion(q, app.querySelector('.qbox'), function (ok, fbw) {
      if (ok) s.right++; else s.missed.push(s.idxs[s.pos]);
      s.pos++; saveSession();
      var b = document.createElement('div'); b.className = 'row end';
      b.innerHTML = '<button class="btn nextq" type="button">' + (s.pos < n ? 'Next →' : 'See results →') + '</button>';
      fbw.parentNode.appendChild(b);
      var nb = b.querySelector('button'), used = false;
      nb.addEventListener('click', function () { if (used) return; used = true; renderQuizStep(); });
      try { nb.focus({ preventScroll: true }); } catch (e) {}
      try { b.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); } catch (e) {}
    });
  }

  function renderQuizEnd() {
    var s = session, n = s.idxs.length, key = s.aid + '/test', r = rec(key);
    clearSession();
    try { history.replaceState(null, '', '#/m/' + s.modId); } catch (e) {}
    var ratio = s.right / n;
    if (!s.retry) { r.best = Math.max(r.best || 0, s.right); r.last = s.right; }
    r.updated = new Date().toISOString();
    saveProgress();
    var msg = s.right === n ? 'All correct.' : ratio >= 0.7 ? 'Solid. You got the key ideas.' : 'Worth another pass — the learn cards will help.';
    var m = s.missed.length;
    var retryLabel = m === 1 ? 'Retry missed question' : 'Retry ' + m + ' missed';
    var learnBtn = m ? '<a class="btn' + (ratio < 0.5 ? '' : ' secondary') + ' wide" href="#/a/' + s.aid + '/learn/0">Review learn cards</a>' : '';
    var retryBtn = m ? '<button class="btn' + (ratio < 0.5 ? ' secondary' : '') + ' wide retry" type="button">' + retryLabel + '</button>' : '';
    var html = '<div class="card result pop"><p class="score">' + s.right + ' / ' + n + '</p>' +
      '<p style="font-size:17px">' + msg + '</p></div>' +
      '<div class="stack">' + (ratio < 0.5 ? learnBtn + retryBtn : retryBtn + learnBtn) +
      '<a class="btn secondary wide" href="#/m/' + s.modId + '">Back to module</a></div>';
    setView(html);
    var rb = app.querySelector('.retry');
    if (rb) rb.addEventListener('click', function () { startQuiz(s.aid, s.missed.slice()); });
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
        if (d && typeof d === 'object') { progress = d; saveProgress(); viewHome(); }
      } catch (e) { alert('Could not read that data. Make sure you pasted the full text.'); }
    });
    if (rst) rst.addEventListener('click', function () {
      if (confirm('Reset all progress? This cannot be undone.')) {
        progress = {}; saveProgress(); viewHome();
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
    if (h[0] === 'm' && h[1]) return viewModule(h[1]);
    if (h[0] === 'a' && h[1]) {
      if (h[2] === 'learn') return viewLearn(h[1], parseInt(h[3] || '0', 10) || 0);
      if (h[2] === 'test') return startQuiz(h[1]);
    }
    return viewHome();
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

  window.addEventListener('hashchange', route);
  renderSummary();
  route();
})();
