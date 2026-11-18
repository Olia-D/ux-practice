---
name: "ux-research-advisor"
description: "Plan, critique and interpret UX research — method choice (usability vs concept test, walkthrough, mixed methods), task writing, rigor level, sample sizing, surveys, statistics, expert methods (heuristics, PURE, GOMS-KLM), cognitive biases, A/B critique, synthesis and strategic debriefs, ROI of UX, research ops and ethics, AI-assisted analysis guardrails, stakeholder interviews and incentive mapping, standard UX metrics (HEART, North Star, UMUX-Lite), and influencing stakeholders with evidence. Use whenever the user plans a study, questions a finding, is handed an A/B result, writes a survey, prepares a readout, needs to justify UX work in numbers, sets up or reads product analytics (Pendo tagging, funnels, dashboards, guides), or hits \"our users are different\"."
---

# UX Research Advisor

The tactical layer for research decisions: what to study, how hard, how to read the result
and how to get it acted on. Sources are listed at the end.

The unifying principle:
> Behavioral evidence beats self-report. When what users *say* and what users *do*
> conflict, behavior wins — every time.

Frame every recommendation as a **decision the team is making** and the **cost of being
wrong**, not as a methodology preference.

## Modes

- **PLAN** — pick the method and rigor for a decision; write tasks; set the evidence bar
- **CRITIQUE** — audit a study design, an A/B result, or a finding someone is citing
- **READOUT** — structure synthesis and strategic sessions; turn findings into ROI

---

## 1. Start from the decision: minimum rigor threshold

Three questions before any study:
1. **What if we're wrong?** Real-world impact of a wrong call. Button colour → cheap; core
   IA for millions → expensive.
2. **Can we reverse it?** Copy and placement are undoable; data models, navigation and
   onboarding that set permanent expectations are not. Irreversible → more rigor.
3. **How much uncertainty is acceptable?** "Need 95%" → full study, adequate sample.
   "Probably right from prior evidence" → quick checks, existing data.

Together these give the **least evidence needed for a responsible decision**. Agree it
with stakeholders *before* data exists — afterwards people move the goalposts.

**Sequence by cost:** paper before interactive, colleagues before recruited users,
competitors before building. **Test assumptions, not whole ideas:** name the
riskiest assumption and run a one-day simulation on it instead of a weeks-long test of the
whole idea. **Check existing evidence first** — past studies, analytics, support tickets,
sales notes. "We already know enough" is a legitimate research outcome.

Slow research is slow for operational reasons (recruiting, formatting, scoring), not
because rigor is slow. Fix the operations.

---

## 2. Choosing the method

| Question | Method | Not a substitute for |
|---|---|---|
| Can users complete a real task on a working interface? Where is the friction? | **Moderated usability test** — the default when you have users | concept tests, surveys |
| Which of several early directions resonates? (no interface yet) | **Concept test** — captures preference, not performance | usability testing before shipping |
| Will a new user know what to do at each step? (no users needed) | **Cognitive walkthrough** | usability testing or analytics |
| Which variant performs better on a metric? | **A/B test** — tells you *which*, never *why* | research on *why* |
| Behaviour *and* intent, or conflicting signals, or an expensive decision | **Mixed methods** (see §6) | two parallel studies in one deck |
| Why did the metric move? | Qual after quant (explanatory sequential) | guessing from the dashboard |

**Usability testing measures five things (Nielsen):** learnability, efficiency,
memorability, error recovery, satisfaction. Most studies only check task completion.

**Sample size follows the goal:** 5 users surface common usability problems; 50+ for
quantifying frequency or comparing groups. "Small sample = invalid" is a misunderstanding.

**Synthetic / AI users are not research.** LLMs predict plausible words, not behavior;
they mirror the persona you prompted. The value of research is **surprise** — confusion,
workarounds, embarrassment, a user believing a failed task worked — and a model never has
those moments. Use AI to speed analysis, tagging and first-draft prototypes; never to
replace watching a real user struggle.

---

## 3. Writing tasks

The task is the atomic unit of a usability test. Three rules:
1. **User goal, not UI action.** ❌ "Click Settings and find notification preferences"
   (tests instruction-following). ✅ "You're getting too many emails. Reduce them."
2. **Realistic scenario** with context, motivation and a way to judge success. ❌ "Find a
   product under $50." ✅ "Your friend's birthday is next week; they're into cooking; find a
   gift under $50 they'd like."
3. **No leading language.** Don't reuse interface words. If the button says "Filter", the
   task must not say "filter". Otherwise you test reading, not usability.

Add Hall's **deal-breaker task** — the one task that, if it fails, nothing else matters.
Start from realistic entry points (deep link, notification email), not the homepage.

---

## 4. Running a cognitive walkthrough

At every step, each reviewer answers **independently**: (1) will the user know what they
are trying to do? (2) will they see the control? (3) will they understand it does what they
need? (4) after acting, will they get feedback it worked?

Process: define a concrete goal ("compliance officer exports a quarterly report") → pick
realistic entry points → break into atomic steps → assign independent reviewers incl. one
naive outsider → compare; **mismatches are the finding**. A PM clicking through and
narrating is a demo, not a walkthrough. Rotate facilitators.

---

## 5. Biases to check in every study and every debrief

*About people:* implicit bias (older user's hesitation read as incompetence), attribution
error (blaming personality for circumstance), false consensus (your label logic = theirs).
*About ourselves:* confirmation bias (logging only supporting evidence), sunk cost
(resisting a fix because of effort spent), **"validate" language** — say *evaluate* or
*test*; aim to be proven wrong. **Evaluate options in parallel** — one idea alone
will always find its reasons.
*In the session:* social desirability ("I'd use this all the time"), self-report bias
("easy" after failing), framing ("others found this hard"), serial-position (first and last
items dominate).

Biases arrive in bundles — one dismissive team discussion can carry five. Keep a bias
checklist in the facilitator guide and the synthesis template.

---

## 6. A/B tests: what they can and cannot say

**Weak test:** vague idea, no user problem ("brighter button converts better"). **Strong
test:** specific hypothesis — the behavior to change, its cause, the exact design change
("users miss the primary action because it blends in; contrast + verb label should raise
completion").

**Match the claim to the test.** One element changed → claim about that element. Full
redesign → you compared two packages, not any single change. Several variables → multivariate
or staged rollout. A bigger button getting more clicks has four explanations, each with a
different fix.

**Before launch:** usability-check both variants; define guardrail metrics (support
contacts, downstream completion, accessibility); ground variants in research, not Figma.

**p < 0.05 means "unlikely to be chance"** — not that the variant caused it, that it will
hold broadly, or that you know why. Correlation → prediction → causation are three levels;
most tests reach the first. Netflix saw promising trial results fail at rollout; Booking.com
is wrong on ~9 of 10 predictions.

**Confounds to rule out:** novelty effect, concurrent changes (bug fix, performance,
another launch), selection effects (new onboarding "improves" retention by filtering out
confused users), segment bleed (one segment moved, you read the aggregate), returning-user
adaptation.

**Toward causal reasoning:** write a theory of change before the test; triangulate with
usability findings and analytics; look for natural experiments (phased rollouts, toggles);
report *likelihood*, not certainty — "likely contributed to", not "caused".

**Mixed methods done properly:** methods answer the *same* question and shape each other,
integration planned *before* collection. Four designs: exploratory sequential (qual → quant
to size it), explanatory sequential (quant → qual to explain it), concurrent triangulation,
embedded. Test: if one method alone would have reached the same result, it wasn't mixed.
Show conflicts explicitly; never average contradictory findings away.

---

## 7. Research as a service — where to show up

Not order-taking: use judgment about what to study, push back when a study won't answer
the real question, say when existing evidence is enough, stay close to the decision.

**During shaping** (before prototypes): what problem, who is affected, which decisions
are already made, where can direction still change; name the riskiest assumptions before
they harden into requirements. Work as a **product trio** — designer, PM, engineer
observing the same sessions; each spots different signals and handoffs lose them.

**Match method to risk:** high-risk → formal study; lower → lightweight sessions or expert
review; strong existing evidence → nothing new. **Stay through decisions:** pair during
design, make the prototype able to answer the real question, check post-launch whether it
helped. Frame findings around the project's choices: "must fix before release" vs "can wait".

---

## 8. Debriefs: two meetings, not one

**Synthesis session** (right after collection; researchers + 1–2 designers + a PM
comfortable with ambiguity): display evidence — quotes, clips, screenshots; look for
patterns across participants, not solutions. Close with **what we know / what we think /
what we need to verify**. Keep roadmap talk out. Torres's **interview snapshot**: a one-page
summary after *each* session (photo, memorable quote, opportunities) so synthesis is
continuous and searchable, not a batch at the end.

**Strategic session** (decision-makers): open with 3–5 evidence-backed insights, each as
**insight → implication → decision** ("users abandon at the address step" → "#1 conversion
blocker" → "fix the form or add autocomplete?"). Output: decisions with owners and timing.
If you're still finding surprises in the data, it's too early for this meeting.
Prioritise usability findings by **severity × frequency**.

---

## 9. Proving value: ROI and what stopped happening

**Five steps:** benchmark the problem (support hours, error rate, time on task,
conversion) → set measurable goals → quantify return (time saved, errors cut, revenue) and
investment (recruiting, hours, dev) → ROI = (benefit − cost) / cost → **lead with the
number**, then the story, then the assumptions.

Worked example: registration redesign cut support from 940 to 280 hours/semester; at
$26.44/h that's ~$17,450 saved against ~$10,000 cost → **74.5% ROI, $1.75 per $1**.
Conservative, single-metric; say so. Put it on slide 2, not slide 40.

**Good UX is invisible** (hedonic adaptation — every fix becomes the new baseline, and the
comparison point disappears for users *and* the team within about a week). Impact is far
easier to measure in the moment than to feel later, so document the *before* numbers
obsessively and track what stopped happening: tickets that vanished, errors that dropped,
training requests that ended, abandonment that fell. Without a baseline there is no proof.

**Measure task outcomes, not internal quality:** completion rate, time on task, error rate,
recovery, confidence — not component coverage or design-system compliance. Watch for the
**build trap**: counting launches as success.

---

## 10. When institutional knowledge fights research

NNG's foundational guidelines produce a usable design ~**90%** of the time. The burden of
proof is on whoever wants to deviate — and they need **behavioral data**, not tenure.

"Our users are different" claims that collapse under testing: "they've memorised our
icons", "technical users like jargon", "users don't scroll", "nobody's complained about
accessibility". The icon evidence: icon-only interfaces tested 11 times over 19 years at
five companies — when familiar icons were shuffled, experienced users were lost. They had
memorised positions, not meanings. If no one is ever confused in your sessions,
suspect the research, not the users.

Six ways it does damage: shuts research down early · flips the burden of proof ·
SME-minded interviewers lead participants · the same champion users become the panel ·
research becomes a confirmation ritual · researchers over-identify with users.

Companies say they value research; what they usually value is **confidence**. Unchecked,
that turns research into "go test this" or "get a quick quote for the deck". A senior IC
changes what the team is deciding, not just what gets tested: ask reframing questions,
think outcomes over artifacts, move fast enough to keep the seat, and frame research as
**de-risking investment**. System-driven orgs let research inform the roadmap; vibes-driven
orgs ask it to validate the roadmap afterwards.

---

## 11. Sample size, saturation and significance

**Qual: stop at saturation** — the point where new sessions stop changing what you know
(not everyone agreeing). Signs: the framework stops changing; "what surprised me?" answers
"not much" two or three times running. Give stakeholders a planning range and say upfront
you may stop early or extend: usability 5 per group then iterate · walkthrough/think-aloud
5–8 · field 4–10 · concept test 5–12 · interviews 6–15 · diary 10–20 · card sort 15–30.
Present ranges as risk management, never quotas.

**A/B sample size** comes from four inputs, not a habit: baseline rate · **MDE** (the
smallest improvement worth shipping — a product decision, so bring stakeholders in) ·
confidence · power. Halving the MDE roughly quadruples the sample, which is why one-point
lifts on low-traffic flows don't work. "We always test with 200" skips every input.

**Significance belongs to findings, not studies.** One survey can produce three significant
results and seven that aren't, from the same people — effect size, variability, sample and
the agreed confidence level decide each one. Set the threshold before the data. Significant
≠ large or important; report the difference, the uncertainty and the consequence together.

**Confidence intervals turn "trust me" into a range.** 5 of 5 completing a task is not
100% — the 95% interval is 48–100%. Use the **Wilson** interval for completion (it behaves
at 0% and 100%), a log-normal approach for time. Put error bars on the chart: "12%" and
"9–15%, some well above" lead to different decisions. ~90% is a realistic completion
benchmark for new users, not 100%.

**Time on task:** lead with the **median**, show the range and every individual time, and
explain the slow cases from what you observed. Never trim the outlier — it is usually the
failure path, and trimming it is the most important finding thrown away.

**Correlation is a signal, not a cause.** Say "is associated with", list the alternative
explanations (self-selection, third factor, reversed direction) *before* presenting the
pattern, and use it to design the next study.

**Check your tool's maths.** A 32-person ranking survey in MS Forms named a winner the raw
data didn't support — undocumented positional weighting. Different aggregation methods
legitimately pick different winners; use pairwise wins with a Borda tie-break (easy to
explain), state the method, and show the full rank distribution.

**Stats with an LLM: expert in the loop.** The calculation is deterministic; the choices
aren't. Pick the test from the question — two independent groups → two-sample t-test
(paired if the same people did both) · 3+ groups → ANOVA then follow-ups · categories ×
categories → chi-squared · rankings → pairwise methods, never averaged ranks · two numeric
measures → correlation/regression. You still check the data prep and interpret the result.

---

## 12. Surveys

**What they measure:** what people say, remember or want to believe — not behaviour. Report
**respondents, not users** ("75% of 28 respondents"). Don't validate ideas with them;
predicting your own future use is unreliable. Users rate failed tasks as easy.

**Three habits that make the data usable:**
1. **Pretest it like a usability test** — a few people thinking aloud, moderated if you can.
   A survey is a one-shot instrument; there is no redo after launch.
2. **Know the item type** — attributes (segment, don't stereotype; only if it changes a
   decision) · behaviours (analytics are usually better) · abilities · sentiments.
3. **Pair the ratings that matter with a "why"** — the score locates it, the comment acts on it.

**In-app pop-ups** are task-level measurement, not sentiment. Trigger on *attempts*, not
completions (completion-only triggers hear from survivors). Set a stop rule (~55 per
segment, cut off past 100), cooldowns, one survey per session, and compare only same
workflow / users / trigger. Write down purpose, segment, target and stop rule before launch.

**SUPR-Q** over a bare NPS or SUS: usability, credibility, loyalty and appearance in one
short validated questionnaire. A stable total can hide falling credibility, and a
usable-but-not-trusted result needs a different study than a trusted-but-hard-to-use one.
Label any derived SUS as *estimated*; take NPS from the recommend item, never by converting
the composite; don't compare product NPS with company marketing NPS.

**Picking a standard metric — what each is for:**

| Metric | Use when | Watch out |
|---|---|---|
| **HEART** (Happiness, Engagement, Adoption, Retention, Task success) | Setting goals → signals → metrics for one product area | Pick 2–3 dimensions, not all five |
| **North Star** | One leading metric the whole team moves | Shallow engagement shouldn't move it |
| **UMUX-Lite** | A 2-item usability score inside an in-app survey | Too short to diagnose; pair with a "why" |
| **TARS** | Feature adoption and satisfaction for one feature | Retention must plateau, not just exist |
| **Cohort retention** | Whether people keep coming back | Read the curve's shape, not one number |

Example targets ("top-task success above 80%") are only illustrative — set your own
baseline first and move it.

---

## 13. Interviews, expert methods and evidence management

**Interview questions** have two failure modes now: the old one (leading — "how much do you
love it?", example answers, double-barrelled) and the new one (**over-neutral** — flat,
context-free questions that read like an AI prompt and produce flat answers). Use five broad
questions by theme over ten narrow ones, funnel broad → specific, one question at a time, no
example answers, and an "if any" escape hatch. Neutrality is a tool, not the goal.

**Pick the heuristic lens, don't default to Nielsen's ten:** Norman's 7 (is it intuitive at
all) · Nielsen's 10 (general review, shared vocabulary) · Weinschenk & Barker's 20 (detail,
persuasion, emotion) · Tognazzini (complex interaction: defaults, anticipation, autonomy) ·
Gerhardt-Powals (data-heavy, high-stakes screens) · Covert (IA, findability, labelling).
One framework is a checklist; several are a toolkit. Naming the violation is the start —
say what it costs the user.

**PURE** turns expert review into a comparable score: define tasks → break into steps →
several experts rate each step independently (1 frictionless … 5 critical error) → sum and
track across versions. **GOMS-KLM** predicts error-free expert task time within 10–20%
without recruiting anyone — good for comparing two designs and prioritising efficiency
work, useless for learnability, errors or satisfaction.

**Quantifying qual without losing the story** (for decisions that drive real investment):
slice transcripts into single-claim evidence units → code against a codebook tied to
decisions → check rater agreement after calibration → weight by severity, segment and
evidence quality → report a range and what could change it. Counting mentions rewards noisy
minor issues and buries rare severe ones.

**5-star confidence on every finding** so stakeholders see at a glance how much to trust it:
★ one attitudinal finding · ★★ one behavioural/best-practice/factual, or two attitudinal ·
★★★ three or more including one behavioural · ★★★★ replicated · ★★★★★ validated repeatedly.
It is Bayesian habit made visible: start from priors (NN/g, MeasuringU), update per study,
communicate uncertainty as a level. Three stars says "solid, may need more validation"
without a statistics lecture.

**When is it a theme?** Before calling something a theme in affinity synthesis, check that
at least about **a third of participants** show it. Below that, report it as a signal with
its count. **Write each insight in four parts:** the learning · why it happens · the
consequence for the product · a confidence note.

**AI in analysis — guardrails before you trust the output:**
- **Match tool to stage:** chat for desk research, a shared workspace for studies with one
  method, scripted pipelines for repeatable analysis.
- **Participant data:** check the plan's training default, use business plans for
  participant data, and pseudonymise (faces and voices still identify). Limit folder access
  and review what the tool changed.
- **Build disconfirmation into every prompt**, plus a separate pass for edge cases and
  counter-evidence.
- **Define failure conditions:** "if the transcript doesn't support a code, return NULL and
  flag it" — so the model doesn't fill gaps.
- **A model change is an instrument change.** Keep a set of hand-coded transcripts as a
  regression set and re-run it after model updates. Record model and effort level in the
  methods section.
- **Calibrate on about five transcripts** against human coding before scaling up.

---

## 14. Plans, ops, ethics and honest artifacts

**A research plan is for alignment**, not to survive scrutiny: which decision it informs,
what success looks like, who does what. When a request arrives, ask first: *"What main
questions are you hoping to answer with this research?"* It moves the conversation from
method to goal and surfaces validation requests without accusing anyone. Then cascade:
where are we in the build, which decisions are still open, do we need to track this over
time, are we comparing against something existing.

**Research fails at the hand-offs**, not for lack of method or talent: recruit → schedule →
collect → synthesise → tell. Audit what gets re-typed, re-uploaded or re-explained, not the
tool count. Keep participant data where it lives rather than rebuilding a pool per study.
Same lesson for analytics: set the strategy before tagging, top tasks first — see §15.

**Ethics, borrowed from the APA code:** respect for rights and dignity (understandable,
voluntary, revocable consent) · competence · integrity (no overclaiming, no cherry-picking)
· professional responsibility · concern for welfare · and social responsibility. Store data
to a security standard and only as long as needed; strip rare details that identify someone
even after the name is gone. Don't run a study whose only purpose is to make a decided
product look validated.

**Honest artifacts:** a journey map built in a workshop without research lets a team invent
user emotions and leave feeling user-centred — and its polish makes guesses look like
findings. Prefer a **service blueprint** of real operations (frontstage, backstage, systems,
owners, hand-offs); it is checkable. Label assumptions as assumptions. Workshops are for
alignment — dot-voting ranks the group's opinions, not users' needs.

**No user access (B2B/enterprise)?** Still possible: task analysis and requirements,
shadowing people doing similar work, interviewing customer success and domain experts, job
postings to map roles and tasks, public forums and search trends, an internal lab of the
colleagues closest to customers. And the buyer is rarely the user — two experiences to
design. Access follows trust: small, low-risk first steps.

---

## 15. Product analytics (Pendo): set-up and reading the numbers

Use when rolling out or cleaning up Pendo (or any tag-based analytics), building funnels or
an exec dashboard, or when someone cites an event count as evidence.

**Never tag everything.** Auto-tagging tracks layout, not intent: in custom-built apps it
yields vague, inconsistent tags (div1, buttonX) that flow into funnels and dashboards and
look like tracking. Assume all tagging is manual. Inconsistent tags create fake findings —
one Submit button tagged three ways made one product show a 20% drop-off and another none.

**Rollout order**
1. **Align.** Executives: what user behaviour do you need to see; which metrics are reported
   across business units and which are missing? Product teams: where do users get stuck,
   how do they move through complex workflows, where does behaviour differ from expectation?
   ResearchOps turns the gap into **one shared tagging plan** (tracked actions, funnels,
   structure) so teams don't fragment the data.
2. **Top tasks.** List the ~20% of actions that make ~80% of use, add rare-but-critical ones
   (audit-log export), trim to **10–15** — merge similar, keep the representative one, favour
   different paths.
3. **Tag those tasks manually as Features.**
4. **Funnels** on known top tasks: start trigger → meaningful midpoints → completion trigger,
   **3–6 steps** (1–2 too thin, 7+ noisy; leave optional branches out).

   | Tag type | In funnels | Why |
   |---|---|---|
   | Feature | Use | Clear intent, precise timestamps |
   | Page | Mostly avoid | Fires passively, over-counts on refresh/idle. OK as a static confirmation exit, or the entry to a separate feature |
   | Track event | Sparingly | Accurate but costs dev time; back-end actions, custom components |
   | Guide | Never | System-triggered, can simulate interactions |

5. **Exec dashboard — pull, not push.** Completion rate by app and user type, drop-off
   points, time on task, adoption tied to specific interactions, funnel comparisons across
   teams/releases, workflow friction. Pair with one standard survey everywhere (SUS,
   SUPR-Q or NPS) to triangulate. Leaders' questions create product teams' interest.
6. **Guides, gradually.** Only after tags, funnels and a shared usage view exist. Each guide
   is a UX project (design, test, measure, tied to a user goal); interruptions very rare;
   a few good guides beat many overlapping ones (see `interaction-design-reviewer` on
   onboarding and in-app help).
7. **Paths and Journeys** last — exploration (detours, loops; cohorts over time) once the
   baseline is reliable. Funnels give benchmarks; Paths and Journeys give questions.

Don't wait for perfect coverage: start evaluative, with funnels on the top tasks you know.

**CRITIQUE checklist for an analytics claim** ("usage is low, so nobody needs it"):
- **Who can do it?** Is the denominator everyone logged in when only admins can act?
- **What fires the event?** A completed export, or a page view / button hover?
- **Is the tag consistent** across products and releases?
- **Is the window right?** Monthly or quarterly tasks look dead in a 30-day view.
- **Observation vs explanation:** "few exports last month" is behaviour; "users don't need
  reporting" is an unproven explanation. Pair with qual before deciding.

---

## 16. Stakeholders: interviews and incentives

**Interview stakeholders for raw material, not requirements.** Asking for requirements
directly gets you solutions. Script the interview around three areas: the **domain**, the
**audience**, and the **constraints** (technical, operational, political).

Questions that work:
- "Describe the purpose of this project in your own words."
- "What's the most important thing to get right?"
- "If you could ask users one question, what would it be?"
- "How will you judge whether this succeeded?"
- Question the labels: "Why do we call them power users?"
- Close with: "What did I miss?"

**Map incentives before pitching anything.** For yourself and each stakeholder, note what
motivates them, which decisions they own, and whether your goal aligns with theirs. Roles
have typical incentives: product — short-term lift; engineering — uptime and velocity;
marketing — brand health; support — fewer tickets. A pitch built on a metric the decider
doesn't care about fails however good the evidence is. If nothing aligns: ask what would
matter to them, find a stakeholder whose incentives do align, or shelve it for now.

```
STAKEHOLDER MAP
Name / role: [...]
Motivated by: [...]
Decisions they own: [...]
Aligned with our goal? yes / partly / no — because [...]
The metric they'll listen to: [...]
```

Pairs with §10: when "our users are different" comes up, the incentive map shows what the
person is protecting.

---

## Output formats

**PLAN**
```
Decision: [what the team is deciding]
Cost of being wrong / reversibility / acceptable uncertainty → Rigor: [quick check | lightweight | formal]
Existing evidence to check first: [...]
Method: [...] because [...]
Riskiest assumption to test first: [...]
Tasks (goal-based, scenario, no leading words): 1. 2. 3. (deal-breaker marked)
Sample + recruiting: [...]
Evidence bar agreed with stakeholders: [...]
Biases to guard: [...]
```

**CRITIQUE**
```
Claim being made: [...]
What the data can actually support: [...]
Gaps / confounds: [...]
What would make it trustworthy: [...]
How to communicate it honestly: [...]
```

**READOUT** — insight → implication → decision, three to five of them, number on slide 2,
assumptions stated, qual evidence beside the quant.

## Sources
Trevor Calabro, *UX Research in the Wild* (trevorcalabro.substack.com) — all 182 posts
(2023–2026) read and distilled into the reference book *UX in the Real World* and the UX Practice app, including
the *Pendo Rollout Playbook* (2025) · Erika Hall, *Just Enough Research* (2nd ed.) · Teresa
Torres, *Continuous Discovery Habits* · NN/g, Baymard, MeasuringU and Sauro findings cited
through Calabro · Dan Brown (EightShapes) on stakeholder interviews · Abby Covert on
incentive architecture · Brittany Hobbs on AI tools in research · Nikki Anderson on theme
thresholds and insight writing · HEART (Google), UMUX-Lite (Lewis et al.).

Figures here were checked against the original posts in Nov 2026. Where a post is dated —
AI model comparisons, Baymard's abandonment percentages, R/SPSS tooling — re-check before
quoting it.