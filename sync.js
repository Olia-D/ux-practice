/* UXSync — progress storage for the UX Practice app and the book.
   Everything is saved in this browser. Optionally, a private (secret) GitHub gist keeps
   progress the same on every device: each sync pulls the gist, merges, and writes back.
   Loaded by index.html and by book/ux-in-the-real-world.html (same origin, same storage). */
(function (w) {
  'use strict';
  var K_APP = 'uxp-progress-v1', K_BOOK = 'uxp-book-v1', K_SYNC = 'uxp-sync-v1';
  var FILE = 'ux-practice-progress.json', API = 'https://api.github.com';
  var TOKEN_URL = 'https://github.com/settings/tokens/new?scopes=gist&description=UX%20Practice%20progress%20sync';

  function get(k) { try { var v = JSON.parse(localStorage.getItem(k)); return v && typeof v === 'object' && !Array.isArray(v) ? v : null; } catch (e) { return null; } }
  function put(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function del(k) { try { localStorage.removeItem(k); } catch (e) {} }
  function ts(x) { var n = Date.parse(x); return isNaN(n) ? 0 : n; }
  function clone(o) { return o == null ? o : JSON.parse(JSON.stringify(o)); }

  // ---------- merge ----------
  // App progress: keep the best score, keep "learned" if either device learned it,
  // otherwise take the newer record. The missed-question list comes from the newer snapshot.
  function mergeApp(a, b) {
    a = a || {}; b = b || {};
    var an = ts(a.savedAt), bn = ts(b.savedAt), base = clone(an >= bn ? a : b) || {};
    var ai = a.items || {}, bi = b.items || {}, items = {};
    Object.keys(ai).concat(Object.keys(bi)).forEach(function (k) {
      if (k in items) return;
      var x = ai[k], y = bi[k];
      if (!x || !y) { items[k] = clone(x || y); return; }
      var r = clone(ts(x.updated) >= ts(y.updated) ? x : y);
      if (/\/test$/.test(k) && (x.best != null || y.best != null)) r.best = Math.max(x.best || 0, y.best || 0);
      if (/\/learn$/.test(k)) r.done = !!(x.done || y.done);
      items[k] = r;
    });
    var reset = Math.max(ts(a.resetAt), ts(b.resetAt));
    if (reset) {
      base.resetAt = new Date(reset).toISOString();
      Object.keys(items).forEach(function (k) { if (ts(items[k] && items[k].updated) <= reset) delete items[k]; });
    }
    base.items = items;
    base.missed = clone((an >= bn ? a.missed : b.missed) || {});
    if (an || bn) base.savedAt = new Date(Math.max(an, bn)).toISOString();
    return base;
  }
  // Book progress: read = { chapterId: { r: 1|0, t: ms, m: 1 if set by hand } }, newest wins
  // per chapter, so marking a chapter unread on one device carries over. last = newest position.
  function mergeBook(a, b) {
    a = a || {}; b = b || {};
    var ar = a.read || {}, br = b.read || {}, read = {};
    Object.keys(ar).concat(Object.keys(br)).forEach(function (k) {
      var x = ar[k], y = br[k];
      read[k] = clone(!x ? y : !y ? x : (x.t || 0) >= (y.t || 0) ? x : y);
    });
    var la = a.last, lb = b.last, last = !la ? lb : !lb ? la : (la.t || 0) >= (lb.t || 0) ? la : lb;
    return { read: read, last: clone(last) || null };
  }

  // ---------- local state ----------
  var changeFns = [], statusFns = [], state = { status: 'local', at: 0, error: '' };
  function cfg() { return get(K_SYNC) || {}; }
  function connected() { return !!cfg().token; }
  function setStatus(s, err) {
    state.status = s; state.error = err || '';
    if (s === 'ok') { state.at = Date.now(); var c = cfg(); c.at = state.at; put(K_SYNC, c); }
    statusFns.forEach(function (fn) { try { fn(state); } catch (e) {} });
  }
  function changedRemotely(what) { changeFns.forEach(function (fn) { try { fn(what); } catch (e) {} }); }

  function getApp() { return get(K_APP) || {}; }
  function setApp(p) { p.savedAt = new Date().toISOString(); put(K_APP, p); dirty(); }
  function getBook() { var b = get(K_BOOK) || {}; b.read = b.read || {}; return b; }
  function setBook(b) { put(K_BOOK, b); dirty(); }

  // ---------- GitHub gist ----------
  function api(path, opt) {
    opt = opt || {};
    var h = { 'Accept': 'application/vnd.github+json', 'Authorization': 'Bearer ' + cfg().token };
    if (opt.body) h['Content-Type'] = 'application/json';
    opt.headers = h; opt.cache = 'no-store';
    return fetch(API + path, opt).then(function (r) {
      if (r.status === 401 || r.status === 403) { var e = new Error(r.status === 401 ? 'GitHub did not accept the token. Check it was copied in full and has not expired.' : 'GitHub refused the request. Make sure the token has the gist permission.'); e.auth = true; throw e; }
      if (!r.ok) throw new Error('GitHub answered ' + r.status + '. Try again in a minute.');
      return r.json();
    });
  }
  function snapshot() { return { v: 1, app: getApp(), book: getBook(), savedAt: new Date().toISOString() }; }
  function findGist(page) {
    page = page || 1;
    return api('/gists?per_page=100&page=' + page).then(function (list) {
      for (var i = 0; i < list.length; i++) if (list[i].files && list[i].files[FILE]) return list[i].id;
      if (list.length === 100 && page < 5) return findGist(page + 1);
      return null;
    });
  }
  function ensureGist() {
    var c = cfg();
    if (c.gist) return Promise.resolve(c.gist);
    return findGist().then(function (id) {
      if (id) return id;
      var files = {}; files[FILE] = { content: JSON.stringify(snapshot(), null, 1) };
      return api('/gists', { method: 'POST', body: JSON.stringify({ description: 'UX Practice progress (book and practice app)', public: false, files: files }) })
        .then(function (g) { return g.id; });
    }).then(function (id) { var c2 = cfg(); c2.gist = id; put(K_SYNC, c2); return id; });
  }

  var inflight = null, again = false, isDirty = false, timer = null;
  function dirty() {
    isDirty = true;
    if (!connected()) return;
    clearTimeout(timer); timer = setTimeout(sync, 2500);
  }
  function sync(opts) {
    if (!connected()) { setStatus('local'); return Promise.resolve(false); }
    if (inflight) { again = true; return inflight; }
    var keep = !!(opts && opts.keepalive);
    setStatus('syncing');
    inflight = ensureGist().then(function (id) {
      return api('/gists/' + id).then(function (g) {
        var f = g.files && g.files[FILE], remote = {};
        try { remote = f && f.content ? JSON.parse(f.content) : {}; } catch (e) { remote = {}; }
        var la = getApp(), lb = getBook();
        var app = mergeApp(la, remote.app), book = mergeBook(lb, remote.book);
        var appChanged = JSON.stringify(app) !== JSON.stringify(la), bookChanged = JSON.stringify(book) !== JSON.stringify(mergeBook(lb, {}));
        put(K_APP, app); put(K_BOOK, book);
        if (appChanged || bookChanged) changedRemotely({ app: appChanged, book: bookChanged });
        var out = { v: 1, app: app, book: book, savedAt: new Date().toISOString() };
        var same = remote.app && JSON.stringify(mergeApp(remote.app, {})) === JSON.stringify(mergeApp(app, {})) && JSON.stringify(mergeBook(remote.book, {})) === JSON.stringify(book);
        isDirty = false;
        if (same) return true;
        var files = {}; files[FILE] = { content: JSON.stringify(out, null, 1) };
        return api('/gists/' + id, { method: 'PATCH', body: JSON.stringify({ files: files }), keepalive: keep }).then(function () { return true; });
      }, function (e) {
        // The gist was deleted on GitHub: forget it and create a new one next time.
        if (/ 404\./.test(e.message)) { var c = cfg(); delete c.gist; put(K_SYNC, c); }
        throw e;
      });
    }).then(function () {
      setStatus('ok');
    }, function (e) {
      setStatus('error', e.message || 'Sync failed.');
      if (e.auth) throw e;
    }).then(function () {
      inflight = null;
      if (again) { again = false; return sync(); }
      return true;
    }, function (e) { inflight = null; throw e; });
    return inflight;
  }
  function connect(token) {
    token = String(token || '').trim();
    if (!/^(ghp_|github_pat_|gho_)?[A-Za-z0-9_]{20,}$/.test(token)) return Promise.reject(new Error('That doesn’t look like a GitHub token. It usually starts with ghp_.'));
    put(K_SYNC, { token: token });
    return sync().then(function () { return true; }, function (e) { del(K_SYNC); setStatus('local'); throw e; });
  }
  function disconnect() { del(K_SYNC); setStatus('local'); }

  // Pull when the page comes back into view; push what's pending when it goes away.
  var lastPull = 0;
  function maybePull() { if (connected() && Date.now() - lastPull > 20000) { lastPull = Date.now(); sync().catch(function () {}); } }
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'visible') maybePull();
    else if (isDirty && connected()) { clearTimeout(timer); sync({ keepalive: true }).catch(function () {}); }
  });
  // Another tab on this device (the book or the app) saved progress.
  w.addEventListener('storage', function (e) {
    if (e.key === K_APP) changedRemotely({ app: true });
    if (e.key === K_BOOK) changedRemotely({ book: true });
  });

  w.UXSync = {
    getApp: getApp, setApp: setApp, getBook: getBook, setBook: setBook,
    mergeApp: mergeApp, mergeBook: mergeBook,
    connect: connect, disconnect: disconnect, connected: connected,
    syncNow: function () { lastPull = Date.now(); return sync(); },
    state: function () { var c = cfg(); return { status: connected() ? (state.status === 'local' ? 'idle' : state.status) : 'local', at: state.at || c.at || 0, error: state.error }; },
    onChange: function (fn) { changeFns.push(fn); },
    onStatus: function (fn) { statusFns.push(fn); },
    tokenUrl: TOKEN_URL, fileName: FILE
  };
  if (connected()) { lastPull = Date.now(); setTimeout(function () { sync().catch(function () {}); }, 300); }
})(window);
