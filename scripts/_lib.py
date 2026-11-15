"""Helpers for writing article content files. Correct option is listed first; the app shuffles."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def cmp(l, li, r, ri): return {"type": "compare", "left": {"label": l, "items": li}, "right": {"label": r, "items": ri}}
def q(text, opts, explain): return {"type": "single", "q": text, "options": opts, "answer": 0, "explain": explain}
def write(file, summary, intro, cards, test, title=None):
    path = os.path.join(ROOT, "content", file); d = json.load(open(path, encoding="utf-8"))
    d["intro"] = intro
    if title: d["title"] = title
    d["topics"] = [{"id": "main", "title": d["title"], "learn": [dict({"title": t, "text": x, "try": tr}, **({"visual": v} if v else {})) for t, x, v, tr in cards], "test": test}]
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    mp = os.path.join(ROOT, "content/manifest.json"); m = json.load(open(mp, encoding="utf-8"))
    for mod in m["modules"]:
        for a in mod["articles"]:
            if a["id"] == d["id"]:
                a["summary"] = summary
                if title: a["title"] = title
    json.dump(m, open(mp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

