---
name: "product-discovery"
description: "Run continuous product discovery: set a product outcome, keep weekly story-based customer interviews going, map opportunities in an opportunity solution tree, choose a target, compare solutions and test the riskiest assumptions. Use whenever the user plans discovery, writes an interview guide or snapshot, builds or critiques an opportunity tree, maps assumptions, picks an experiment, turns a feature request into an outcome, or reviews a roadmap for output bias, even if they don't say discovery. Trigger with \"discovery\", \"continuous discovery\", \"CPD\", \"opportunity solution tree\", \"OST\", \"assumption mapping\", \"assumption test\", \"outcome vs output\", \"product trio\", \"interview snapshot\", \"build trap\", \"what should we build next\"."
---

# Product Discovery

Discovery is how a team decides what to build with evidence that keeps arriving, not with
one study before a big decision. The unifying principle:

> Start from an outcome, collect real customer stories every week, choose one opportunity,
> compare several solutions, and test the belief that would sink the idea before building it.

Frame advice as **what the team would get wrong without it** (building the wrong thing,
arguing from opinion, shipping outputs nobody uses) and what that costs.

## Modes

- **PLAN** — set up discovery: outcome, trio, weekly cadence, recruiting, first interviews
- **MAP** — turn interview stories into an opportunity solution tree and choose a target
- **TEST** — list assumptions, place them on importance × evidence, choose and design tests
- **REVIEW** — critique a roadmap, feature request, tree or test plan for output bias and gaps

---

## 1. Outcome first

| Metric | Example | Use in discovery |
|---|---|---|
| Business outcome | Revenue, retention, cost to serve | Too far from one team. Use it to choose product outcomes |
| **Product outcome** | Customer behaviour or sentiment in the product (teams that invite a colleague in week one) | **The goal.** The team can move it and many solutions could |
| Traction metric | Use of one feature | Only for optimising that feature; it narrows solutions to one |

- Outputs (features shipped, dates met) are evidence of effort, not value.
- Strategy cascade: strategic intent (1–2 years) → product initiatives (customer problems) →
  options (solutions as bets). Leaders set the why; teams own the how.
- **Feature request → outcome:** ask which outcome it should move and what you'd see if it
  worked. No answer means it's an output looking for a reason.
- Check four risks before building: **value** (will they choose it), **usability** (can
  they use it), **feasibility** (can we build it), **viability** (does it work for the
  business, including legal and ethics).

## 2. The weekly habit

- A customer touchpoint **at least every week**, by the **product trio** (product manager,
  designer, engineer) together, so they share one view of the evidence.
- **Automate recruiting** (in-product invite, onboarding line, standing ask to customer
  success) so the next interview is always booked.
- **One-page snapshot within the hour** of each interview; share it.
- Refresh the tree **every 3–4 interviews**.
- Where to start: feature factory → story-map one planned feature and list its assumptions;
  new to trios/OKRs → one bright spot where the trio interviews together; sliding back under
  pressure → share snapshots and the tree after every interview.

## 3. Story-based interviews

- Ask for one specific, recent story: **"Tell me about the last time you…"** Never "would
  you…?" — predictions are guesses.
- **Dig it out:** set the scene (when, where, what before) → keep them in the moment ("what
  happened next?") → bring generalisations back ("I usually…" → "and last time?") → don't
  stop at a short answer.
- **Bad data:** compliments ("that's cool") → ask what they do today; generalisations and
  future promises ("I always…", "I'd definitely buy") → ask for the last time; feature
  requests → ask why and what they do now. The need underneath is the opportunity.
- **Demand tests:** real interest costs something — time (trial, next meeting), reputation
  (an introduction), money (pre-order). Compliments with no next step = little learned.
- Swap questions: "how much would you pay?" → "what did this cost you last month?";
  "is this a good idea?" → "how do you handle this today?"; "do you have this problem?" →
  "what else have you tried?"
- The interviewer's classic mistakes: selling instead of listening, speculating instead of
  observing.

**Snapshot template**
```
Who: [quick facts that matter for the outcome]
Memorable quote: "..."
The story: [moments in order — trigger → what they tried → where it hurt → how it ended]
Opportunities heard: [needs / pain points / desires, in their words]
Insights and surprises: [...]
Follow-ups: [...]
```

## 4. Opportunity solution tree

```
Outcome
├── Opportunity (need, pain point or desire, in the customer's words)
│   ├── Sub-opportunity  ← target
│   │   ├── Solution A ── assumption tests
│   │   ├── Solution B
│   │   └── Solution C
│   └── Sub-opportunity
└── Opportunity
```
- **Disguised-solution test:** if it can be addressed only one way, it's a solution. Ask
  "why?" to find the opportunity underneath ("calendar export" → "see my schedule outside
  the app").
- A child is part of its parent ("what are other reasons why…?"); siblings are distinct and
  can be addressed separately; similar needs with different constraints share a parent.
- Opportunities come from story interviews. Tickets, sales calls and analytics suggest what
  to ask about; they are not opportunities on their own.
- **Choose a target** on size (how many, how often), market position, strategic fit and
  customer importance/satisfaction. **Leave effort out** — feasibility is tested later.
  Compare one row at a time, top down. It's a two-way door. No scoring formulas.
- Brainstorm **only for the target**; compare **about three** solutions.
- Before the first tree: an outcome, a working theory of the customer, 3–4 story
  interviews. Messy after 6–8 interviews → check interviewing and synthesis. New tree only
  when the outcome changes direction, not when its number changes.
- Mistakes: invented opportunities, solutions as opportunities, brainstorming across the
  whole tree, chasing the latest ticket, several outcomes at once, one company-wide tree.

## 5. Assumptions and tests

- **Find them:** story-map the solution as if it existed — each customer step, and under it
  what must be true (20–30 minutes). Write each as "We believe that…".
- **Five types:** desirability · usability · feasibility · viability · ethics.
- **Prioritise on importance × evidence:** test **important + no evidence** first. Evidence
  means something observed, not the loudest opinion.

| Strength | Evidence of | Examples |
|---|---|---|
| Weaker | What people say | Interviews, surveys, comprehension questions |
| Stronger | What people do | Prototype tests, fake doors, Wizard of Oz, A/B tests |
| Strongest | What people give up | Effortful sign-ups, pre-orders, paid pilots |

- Start cheap and weak; move to stronger tests as the signal improves. Several tests can
  check one assumption.
- Change one variable at a time. Define who you test with. **Write the pass line before
  the test.** A badly built A/B test is weak evidence; a well-run interview can be strong.

**Test card**
```
Assumption: We believe that [...]   Type: [desirability | usability | feasibility | viability | ethics]
Test: [method] with [who, how many]
Measure: [what we observe]
Pass line (set before running): [...]
Cost / time: [...]   Evidence strength: [say | do | give up]
If it fails: [drop the idea | change the solution | pick another opportunity]
```

## 6. Strategy check (REVIEW mode)

A strategy has a **diagnosis** (the critical challenge), a **guiding policy** (an approach
that rules options out) and **coherent actions** (steps that reinforce each other). Flag:
fluff, no named challenge, goals posing as strategy ("20% growth"), sprawling or unreachable
objectives. Ask of any roadmap: what is the diagnosis, what does the policy rule out, do the
actions reinforce each other, which outcome shows it's working and when do we look?

---

## Output formats

**PLAN**
```
Outcome: [product outcome + how measured]   Business outcome it serves: [...]
Trio: [roles]   Cadence: [weekly touchpoint, day]
Recruiting: [automated channel + screener]
First 4 interviews: [who, story prompt]
Snapshot owner + where snapshots are shared: [...]
```

**MAP** — the tree as an indented outline, the target marked, and one line per target
factor (size, market, strategy, importance) with the evidence behind it.

**TEST** — assumption list grouped by type, the 2x2 placement, then a test card for each
assumption in the important/no-evidence corner.

**REVIEW**
```
What's being proposed: [...]
Output or outcome? [...]
Missing: [outcome | stories | target choice | alternatives | assumption tests | pass lines]
Riskiest unstated assumption: [...]
Next smallest step: [...]
```

**Related skills:** writing the study plan, sample sizes and synthesis → `ux-research-advisor`.
Why users switch and job statements → `jtbd-research` (job statements make good
opportunities). Designing and reviewing the chosen solution → `interaction-design-reviewer`.
AI features → `ai-ux-patterns`. Measuring impact after launch → `ux-research-advisor` §9.

## Sources
Teresa Torres, *Continuous Discovery Habits* (2021) and Product Talk (opportunity solution
trees, prioritising and mapping opportunities, getting started with discovery) · Marty
Cagan, SVPG, "Product risk taxonomies" · Melissa Perri, *Escaping the Build Trap* · Richard
Rumelt, "The perils of bad strategy" (McKinsey Quarterly, 2011) · Giff Constable, *Talking
to Humans* (free) · Rob Fitzpatrick, *The Mom Test* · Strategyzer, assumptions mapping and
strong experiments · *The Real Startup Book* (free, Creative Commons). Compiled in the
reference book *UX in the Real World*, Part VI.
