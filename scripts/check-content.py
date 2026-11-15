#!/usr/bin/env python3
"""Content checks for UX Practice. Run before every push:  python3 scripts/check-content.py
Fails on broken structure; warns on answer-length bias (correct option is the single longest)."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_BIAS_ARTICLE, MAX_BIAS_TOTAL = 0.50, 0.30
errors, warnings = [], []

def questions(article):
    for t in article.get("topics", []):
        for c in t.get("learn", []):
            if "try" in c: yield "check", c["try"]
        for q in t.get("test", []): yield "test", q

manifest = json.load(open(os.path.join(ROOT, "content/manifest.json"), encoding="utf-8"))
seen, tot, tot_long = set(), 0, 0
ranks = {}
for m in manifest["modules"]:
    for a in m["articles"]:
        path = os.path.join(ROOT, a["file"])
        if a["id"] in seen: errors.append(f"duplicate article id {a['id']}")
        seen.add(a["id"])
        if not a.get("source", "").startswith("https://") and not a.get("sourceNote"):
            errors.append(f"{a['id']}: needs a source URL or a sourceNote")
        if not os.path.exists(path): errors.append(f"{a['id']}: missing file {a['file']}"); continue
        try: art = json.load(open(path, encoding="utf-8"))
        except Exception as e: errors.append(f"{a['file']}: invalid JSON ({e})"); continue
        if art.get("id") != a["id"]: errors.append(f"{a['file']}: id {art.get('id')!r} != manifest {a['id']!r}")
        n = long = 0
        for kind, q in questions(art):
            where = f"{a['id']} [{kind}] {q.get('q', '')[:50]!r}"
            opts, ans = q.get("options", []), q.get("answer")
            if len(opts) < 3: errors.append(f"{where}: fewer than 3 options")
            if not isinstance(ans, int) or not 0 <= ans < len(opts): errors.append(f"{where}: answer index out of range"); continue
            if len(set(opts)) != len(opts): errors.append(f"{where}: duplicate options")
            if not q.get("explain"): errors.append(f"{where}: no explanation")
            lens = [len(o) for o in opts]; n += 1
            r = sorted(lens, reverse=True).index(lens[ans]) + 1; ranks[r] = ranks.get(r, 0) + 1
            if lens[ans] == max(lens) and lens.count(max(lens)) == 1: long += 1
            if max(lens) > 2.2 * max(1, min(lens)) and lens[ans] in (max(lens), min(lens)):
                warnings.append(f"{where}: correct option is the length outlier ({lens[ans]} vs {sorted(lens)})")
        tot += n; tot_long += long
        if n == 0: errors.append(f"{a['id']}: no questions")
        elif long / n > MAX_BIAS_ARTICLE: warnings.append(f"{a['id']}: correct answer is the longest option in {long}/{n} questions")

share = tot_long / max(1, tot)
print(f"{len(seen)} articles, {tot} questions. Correct answer is the longest option in {tot_long} ({share:.0%}; target ≤ {MAX_BIAS_TOTAL:.0%}).")
print("Length rank of the correct option (1 = longest): " + ", ".join(f"{k}: {v} ({v / tot:.0%})" for k, v in sorted(ranks.items())))
for k, v in sorted(ranks.items()):
    if v / tot > 0.45: warnings.append(f"correct option is the #{k} longest in {v / tot:.0%} of questions; aim for an even spread")
for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
if share > MAX_BIAS_TOTAL: print("WARN  overall answer-length bias above target")
sys.exit(1 if errors else 0)
