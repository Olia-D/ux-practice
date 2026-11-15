#!/usr/bin/env python3
"""Rebuild content/manifest.json so it covers every chapter of the book (99), in 11 modules."""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODULES = [
 ("foundations", "Foundations", "🧱", "What good UX is — and how you know",
  ["basics-problem","id-basics","best-practice-default","think-researcher","jakobs-law","millers-law","harmful-ideas","misunderstandings","stop-doing","analogies"]),
 ("interaction", "Interaction Design", "🖱️", "Icons, navigation, motion, effort",
  ["icons","affordances","animations","split-buttons","navigation","nav-guide","carousels","onboarding-help","interaction-cost","cognitive-load"]),
 ("controls", "Forms, Controls & Status", "🎛️", "What users type, pick, and wait for",
  ["input-field","status-design","style-guides","conversational-ux","checkout","c-confirm-undo","c-selection-controls","c-tables-bulk"]),
 ("accessibility", "Accessibility & Content", "♿", "Usability under real-world conditions",
  ["accessibility","accessibility-first","aria","content-structure","dark-patterns","dark-patterns-2026"]),
 ("running-studies", "Running Studies", "🔬", "Planning and running research that lands",
  ["tasks","usability-vs-concept","cognitive-walkthrough","research-rigor","research-plans","how-many-users","interview-questions","ethics","researchops","honest-artifacts","c-b2b-research"]),
 ("evidence", "Evidence & Bias", "🧠", "What counts as evidence, and what corrupts it",
  ["behavioral-evidence","cognitive-biases","fake-ai","institutional","five-star-confidence","quantifying-qual","mixed-methods","mixed-methods-advantage","mixed-methods-work"]),
 ("experiments", "Experiments & Statistics", "📐", "A/B tests, samples, and reading the numbers",
  ["ab-testing","ab-mislead","ab-strategies","ab-sample-size","stat-significance","confidence-intervals","correlation","stats-llms","tool-math","time-on-task","goms-klm","pure"]),
 ("metrics", "Surveys & Metrics", "📋", "Asking well, and measuring what matters",
  ["survey-myths","writing-surveys","in-app-surveys","supr-q","heuristic-frameworks"]),
 ("data-viz", "Data Visualization", "📊", "Charts and dashboards that lead to decisions",
  ["dashboard","chart-types","c-dataviz"]),
 ("business", "Business Impact", "💼", "Turning research into decisions and money",
  ["roi","debrief","figma","delight","pmf","c-tars","fuzzy-middle","service-failure","startup-principles"]),
 ("ai-ux", "AI UX", "🤖", "Designing and researching AI features",
  ["ai-chat-history","ai-cant-do","c-ai-frameworks","c-eu-ai-labels"]),
 ("career", "Career & Influence", "🧭", "Getting the work used, and growing",
  ["ic","thankless","predictions","career","career-craft","job-security","research-service","opt-in","critical-error","seven-patterns","leader-traps","c-three-books"]),
]

# book id -> (title, icon, one-line summary, substack slug or None for companions)
META = json.load(open(os.path.join(ROOT, "scripts/article-meta.json"), encoding="utf-8"))

old = json.load(open(os.path.join(ROOT, "content/manifest.json"), encoding="utf-8"))
olda = {a["id"]: a for m in old["modules"] for a in m["articles"]}
olda["research-service"] = olda.pop("ux-as-service")  # same article, book id

mods, seen = [], set()
for mid, name, icon, subtitle, ids in MODULES:
    arts = []
    for i, aid in enumerate(ids):
        assert aid not in seen, f"{aid} listed twice"
        seen.add(aid)
        meta = META[aid]
        a = olda.get(aid)
        if a:
            a = dict(a); a["id"] = aid
            a.setdefault("file", f"content/{aid}.json")
        else:
            a = {"id": aid, "title": meta["title"], "icon": meta["icon"],
                 "summary": meta["summary"], "file": f"content/{aid}.json"}
        if meta.get("source"): a["source"] = meta["source"]
        a["title"] = a.get("title") or meta["title"]
        arts.append(a)
    mods.append({"id": mid, "name": name, "icon": icon,
                 "week": f"Module {len(mods) + 1}", "subtitle": subtitle, "articles": arts})

missing = set(META) - seen
assert not missing, f"not placed in a module: {sorted(missing)}"
out = {"version": 1, "title": "UX Practice", "modules": mods}
json.dump(out, open(os.path.join(ROOT, "content/manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(mods)} modules, {len(seen)} articles")
for m in mods: print(f"  {m['id']:16} {len(m['articles']):2}  " + ", ".join(a["id"] for a in m["articles"] if not os.path.exists(os.path.join(ROOT, a['file']))))
