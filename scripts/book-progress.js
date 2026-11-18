(function () {
  'use strict';
  // Reading progress for the book. Uses UXSync (../sync.js) when the book is opened from the
  // site, so progress syncs across devices; falls back to this browser's storage offline.
  var K = 'uxp-book-v1';
  var S = window.UXSync || {
    getBook: function () { try { var b = JSON.parse(localStorage.getItem(K)) || {}; b.read = b.read || {}; return b; } catch (e) { return { read: {} }; } },
    setBook: function (b) { try { localStorage.setItem(K, JSON.stringify(b)); } catch (e) {} },
    onChange: function () {}, onStatus: function () {}, state: function () { return { status: 'offline' }; }, connected: function () { return false; }
  };
  var inApp = document.documentElement.classList.contains('in-app');
  var arts = Array.prototype.slice.call(document.querySelectorAll('article.article')).filter(function (a) { return a.id && a.id !== 'archive-guide'; });
  if (!arts.length) return;
  var byId = {}; arts.forEach(function (a, i) { byId[a.id] = i; });
  function title(a) { var h = a.querySelector('h3'); return h ? h.textContent.trim() : a.id; }
  function isRead(b, id) { var r = b.read[id]; return !!(r && r.r); }
  var CHECK = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>';

  // End of every chapter: mark as read + next chapter
  arts.forEach(function (a, i) {
    var end = document.createElement('div'); end.className = 'ch-end';
    var nx = arts[i + 1];
    end.innerHTML = '<button type="button" class="ch-mark" aria-pressed="false"><span class="ch-box">' + CHECK + '</span><span class="ch-lbl">Mark as read</span></button>' +
      (nx ? '<a class="ch-next" href="#' + nx.id + '"><span>Next chapter</span><b>' + title(nx).replace(/[<>&]/g, '') + '</b></a>' : '');
    a.appendChild(end);
    end.querySelector('.ch-mark').addEventListener('click', function () {
      var b = S.getBook(), on = !isRead(b, a.id);
      b.read[a.id] = { r: on ? 1 : 0, t: Date.now(), m: 1 };
      S.setBook(b); paint();
    });
  });

  // Table of contents: progress line + a mark on read chapters
  var toc = document.getElementById('toc'), tocLine = null;
  if (toc) {
    tocLine = document.createElement('div'); tocLine.className = 'toc-progress';
    var h2 = toc.querySelector('h2'); (h2 || toc.firstChild).insertAdjacentElement('afterend', tocLine);
  }
  var rail = Array.prototype.slice.call(document.querySelectorAll('.rail a'));

  function partOf(a) { var el = a; while (el && !(el.classList && el.classList.contains('chapter-divider'))) el = el.previousElementSibling; return el ? el.id : ''; }
  var parts = {}; arts.forEach(function (a) { var p = partOf(a); (parts[p] = parts[p] || []).push(a.id); });

  function statusText() {
    var st = S.state();
    if (st.status === 'offline') return 'Saved in this browser.';
    if (!S.connected()) return 'Saved on this device only. <a href="../#/sync">Sync across devices</a>';
    if (st.status === 'error') return 'Sync paused. <a href="../#/sync">Fix</a>';
    return 'Synced across your devices. <a href="../#/sync">Settings</a>';
  }
  function paint() {
    var b = S.getBook(), n = 0;
    arts.forEach(function (a) {
      var r = isRead(b, a.id); if (r) n++;
      var btn = a.querySelector('.ch-mark');
      btn.setAttribute('aria-pressed', r ? 'true' : 'false');
      btn.querySelector('.ch-lbl').textContent = r ? 'Read' : 'Mark as read';
    });
    Array.prototype.forEach.call(document.querySelectorAll('.toc-entry'), function (e) {
      var id = (e.getAttribute('href') || '').slice(1);
      e.classList.toggle('is-read', isRead(b, id));
    });
    rail.forEach(function (l) {
      var id = (l.getAttribute('href') || '').slice(1), ids = parts[id];
      if (!ids) return;
      var c = l.querySelector('.rc'); if (!c) { c = document.createElement('span'); c.className = 'rc'; l.appendChild(c); }
      var k = ids.filter(function (x) { return isRead(b, x); }).length;
      c.textContent = k + '/' + ids.length; c.classList.toggle('all', k === ids.length);
    });
    if (tocLine) {
      tocLine.innerHTML = '<div class="tp-strip" aria-hidden="true">' + arts.map(function (a) { return '<i class="' + (isRead(b, a.id) ? 'd' : '') + '"></i>'; }).join('') + '</div>' +
        '<p><b>' + n + '</b> of ' + arts.length + ' chapters read. <span class="tp-sync">' + statusText() + '</span></p>';
    }
  }

  // Where am I? The chapter crossing a line 35% down the viewport.
  function current() {
    var y = window.innerHeight * 0.35, best = null;
    for (var i = 0; i < arts.length; i++) {
      var r = arts[i].getBoundingClientRect();
      if (r.top <= y && r.bottom > y) { best = { a: arts[i], f: Math.max(0, Math.min(1, (y - r.top) / r.height)) }; break; }
    }
    return best;
  }
  var dwell = {}, lastTick = Date.now(), saveT = null, lastSaved = '', pending = '';
  function tick() {
    var now = Date.now(), dt = Math.min(now - lastTick, 2000); lastTick = now;
    if (document.visibilityState !== 'visible') return;
    var c = current(); if (!c) return;
    dwell[c.a.id] = (dwell[c.a.id] || 0) + dt;
    var key = c.a.id + ':' + c.f.toFixed(2);
    if (key !== lastSaved && key !== pending) {
      pending = key;
      clearTimeout(saveT);
      saveT = setTimeout(function () {
        lastSaved = key;
        var b = S.getBook(); b.last = { id: c.a.id, f: +c.f.toFixed(3), t: Date.now() }; S.setBook(b);
      }, 1500);
    }
  }
  setInterval(tick, 1000);

  // Reaching the end of a chapter after spending real time in it marks it read.
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var a = en.target.parentNode, id = a.id, b = S.getBook(), r = b.read[id];
        if (r && (r.r || r.m)) return;            // already read, or unmarked by hand
        var need = Math.min(45000, Math.max(12000, a.textContent.length * 12)); // ~ quick-skim speed
        if ((dwell[id] || 0) < need) return;
        b.read[id] = { r: 1, t: Date.now() }; S.setBook(b); paint();
      });
    }, { threshold: 0.6 });
    arts.forEach(function (a) { io.observe(a.querySelector('.ch-end')); });
  }

  // Resume: #resume jumps to the saved position; otherwise offer it.
  function goLast(b) {
    var a = b.last && document.getElementById(b.last.id); if (!a) return false;
    var top = a.getBoundingClientRect().top + window.scrollY + (b.last.f || 0) * a.offsetHeight - window.innerHeight * 0.35;
    try { window.scrollTo({ top: Math.max(0, top), behavior: 'instant' }); } catch (e) { window.scrollTo(0, Math.max(0, top)); }
    return true;
  }
  function offerResume() {
    var b = S.getBook(); if (!b.last || !byId.hasOwnProperty(b.last.id)) return;
    var a = arts[byId[b.last.id]];
    var t = document.createElement('div'); t.className = 'resume'; t.setAttribute('role', 'status');
    t.innerHTML = '<span>Continue <b>' + title(a).replace(/[<>&]/g, '') + '</b></span><button type="button" class="r-go">Continue</button><button type="button" class="r-x" aria-label="Dismiss">×</button>';
    document.body.appendChild(t);
    function close() { if (t.parentNode) t.parentNode.removeChild(t); window.removeEventListener('scroll', onS); }
    var y0 = window.scrollY; function onS() { if (Math.abs(window.scrollY - y0) > window.innerHeight) close(); }
    window.addEventListener('scroll', onS, { passive: true });
    t.querySelector('.r-go').addEventListener('click', function () { goLast(S.getBook()); close(); });
    t.querySelector('.r-x').addEventListener('click', close);
  }
  function start() {
    if (location.hash === '#resume') {
      var b = S.getBook();
      try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
      requestAnimationFrame(function () { if (!goLast(b)) window.scrollTo(0, 0); });
    } else if (!location.hash) offerResume();
  }
  paint();
  S.onChange(function (w) { if (!w || w.book) paint(); });
  S.onStatus(function () { if (tocLine) { var s = tocLine.querySelector('.tp-sync'); if (s) s.innerHTML = statusText(); } });
  if (document.readyState === 'complete') start(); else window.addEventListener('load', start);
})();
