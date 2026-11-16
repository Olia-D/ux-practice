---
name: "ux-start"
description: "Entry point when Olha has a UX problem but hasn't named a method or skill, or when the task spans several steps (new feature, redesign, stakeholder pushback, launch review). Routes to the right specialist skill(s) and runs the standard flow. Trigger with \"where do I start\", \"what should I use\", \"which skill\", \"help me with this feature\", \"I need to design\", \"I'm stuck\", \"we're launching\", \"stakeholder says\", or any request that mixes research, design, copy, AI or data questions."
---

# UX Start — router and flows

This skill holds no patterns. It decides **which specialist skill(s) to load** and in
**what order**, then hands off. Always say in one line which skills you're loading and why,
so Olha learns the map.

## Step 1 — Classify the request

Ask (or infer) two things: **what is the deliverable** and **what decision is behind it**.

| Request looks like | Load | Then |
|---|---|---|
| "Is this screen / form / flow good?" — a mockup, Figma link, screenshot | `interaction-design-reviewer` (REVIEW) | + `data-visualization` if it has charts; + `ai-ux-patterns` if AI-powered |
| "Design X for me", "how should X work" | `interaction-design-reviewer` (CREATE or SUGGEST) | same add-ons |
| Chart, graph, dashboard, KPI, metric, report view | `data-visualization` | + `interaction-design-reviewer` for filters/controls around it |
| AI feature, agent, copilot, chat, "should the agent do this itself" | `ai-ux-patterns` (frameworks first) | + `interaction-design-reviewer` for the non-AI surface |
| "Should we test this", "how do I know", a finding or A/B result, readout, ROI, "our users are different" | `ux-research-advisor` | + `jtbd-research` if the question is *why users choose/switch* |
| Why users pick / drop / switch; positioning; churn | `jtbd-research` | + `ux-research-advisor` for the study plan |
| Button label, error, empty state, any product text | `interaction-design-reviewer` (forms/status) | (ux copy guidance lives there and in Microcopy / Everybody Writes in the project library) |
| Email, Slack, LinkedIn, CV text she sends as herself | `humanizer` | — |
| Framer component | `component-idea` | — |

If none fits, say so and answer with the project library (Hall, Torres, Yifrah, Handley,
Cialdini) rather than forcing a skill.

## Step 2 — Standard flows for multi-step requests

**New feature / redesign**
1. `ux-research-advisor` → what decision, cost of being wrong, riskiest assumption,
   existing evidence. Output: rigor level + what to test first.
2. `interaction-design-reviewer` CREATE / SUGGEST → spec or 2–3 options. Add
   `ai-ux-patterns` if AI is involved (set autonomy level and trust scaffold *before* UI),
   `data-visualization` if it shows numbers.
3. `interaction-design-reviewer` REVIEW → run the 5 stress tests on the chosen option.
4. `ux-research-advisor` → tasks for the usability test (goal-based, no leading words).

**Review something built**
1. `interaction-design-reviewer` REVIEW (+ `data-visualization` / `ai-ux-patterns` as above).
2. Priority stack → `ux-research-advisor` to decide which findings need user evidence
   before the team will act, and how to present them (insight → implication → decision).

**Stakeholder pushback / "our users are different" / "just copy competitor X"**
1. `ux-research-advisor` §10 (90/10 rule, burden of proof) and §6 if an A/B result is cited.
2. `interaction-design-reviewer` pushback-prep lines for the specific pattern.
3. `humanizer` if the answer goes out as a message from Olha.

**Launch / post-launch review**
1. `ux-research-advisor` §9 → baselines, what stopped happening, ROI frame.
2. `data-visualization` → how to show the before/after so the takeaway is right.
3. `humanizer` for the write-up.

**Dashboard or analytics page**
1. `data-visualization` Step 0 → what decision; monitor / diagnose / prove.
2. `data-visualization` §1–4 → charts, layout, colour.
3. `interaction-design-reviewer` → filters, status, empty states, controls.
4. `data-visualization` §5 → accessibility pass.

## Step 3 — Hand off cleanly

Load the first skill and follow *its* output format. When a flow has several stages,
finish one stage, show it, and ask whether to continue — Olha often wants to redirect
after step 1. Never summarise all stages in one shot unless she asks for the whole flow.

End every answer with one line: `Skills used: a, b` — so misrouting is visible and
fixable.