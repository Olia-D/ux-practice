"""Helpers for authoring article content files. The correct option is listed first; the app shuffles."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN = os.path.join(ROOT, "content/manifest.json")

def cmp(l, li, r, ri):
    return {"type": "compare", "left": {"label": l, "items": li}, "right": {"label": r, "items": ri}}

def q(text, opts, explain):
    return {"type": "single", "q": text, "options": opts, "answer": 0, "explain": explain}

def write(aid, intro, cards, test, summary=None, title=None):
    """cards: [(card title, markdown text, visual|None, try-question)]"""
    man = json.load(open(MAN, encoding="utf-8"))
    entry = mod = None
    for m in man["modules"]:
        for a in m["articles"]:
            if a["id"] == aid: entry, mod = a, m
    assert entry, f"{aid} is not in the manifest"
    if summary: entry["summary"] = summary
    if title: entry["title"] = title
    path = os.path.join(ROOT, entry["file"])
    d = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    d.update({"id": aid, "module": mod["id"], "title": entry["title"], "icon": entry.get("icon", "📄"), "intro": intro,
              "topics": [{"id": "main", "title": entry["title"],
                          "learn": [dict({"title": t, "text": x, "try": tr}, **({"visual": v} if v else {})) for t, x, v, tr in cards],
                          "test": test}]})
    json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(man, open(MAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
