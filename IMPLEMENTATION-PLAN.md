# UX Practice — gap analysis and implementation plan

Date: 2026-11-15. State audited: 26 articles, 78 learn cards, 130 quiz questions + 78 quick checks. App renders without console errors on iPhone viewport; home, module, learn, quiz and result views all work.

## Findings

### 1. Quiz validity — correct answer is the longest option 88% of the time (184/208)
Options are shuffled at runtime, so position doesn't leak — but length does. A test-wise learner can score ~90% without reading the cards. Eight articles are 8/8. This is the most important fix: it undermines the "test" half of learn-then-test.

### 2. "Read original article" links are guessed slugs
Manifest uses `/p/animations`, `/p/ab-testing`, `/p/ic`; the real posts are `/p/most-ui-animations-shouldnt-exist`, `/p/ab-testing-and-the-two-party-trap`, `/p/why-i-stay-an-ic`. Most of the 26 links are probably 404s.

### 3. Coverage — 9 of Calabro's 35 articles are not in the app
Confirmed missing: *UX Job Security*, *UX Has a Basics Problem*, *The Rules of AI Chat History*, *Reframing Dark Patterns: 2026 Edition*, *The Problem With Split Buttons*. The remaining four are in the HTML reference book on the Mac (`ux-in-the-real-world-book.html`).

### 4. Knowledge gathered today that the app doesn't carry
- **Data visualization** — FT Visual Vocabulary, London data design guidelines, Datawrapper colour rules, dataschool ACES, Chartability. Only one article (*Why Your Data Dashboard Stinks*) touches this.
- **AI UX** — Agentic UX autonomy levels, T.R.U.S.T., C.O.N.V.E.R.S.E., plus Calabro's own *Rules of AI Chat History*. Nothing in the app.
- Hall and Torres are already folded in where they fit. Their out-of-scope topics (surveys, personas, OSTs) stay out by design.

### 5. Promised features that don't exist
- The schedule text promises a "mixed quiz at end of each module". There is none.
- Missed questions live only in `sessionStorage` for the current attempt — there is no cross-article "review what you missed" bank, which is the single most effective retention mechanic that isn't gamification.
- No concept index: once an article is done there is no fast way to re-find "the 4 walkthrough questions" without re-reading cards.

### 6. Small things
- No web-app manifest or service worker → not installable, no offline. The whole app is ~200 KB of static files; offline is cheap.
- Quick-check "Check" button is disabled with no explanation until an option is picked (the skills flag exactly this pattern). Keep it enabled and show "Pick an answer" on click instead.
- `content/manifest.json` title is "UX Lärbasen" (template leftover, unused by the app, but English-only rule).
- No automated content check; the audit was manual.

## Plan

### Phase 1 — Fix what's broken — done 15 Nov, with two follow-ups
1. ~~**De-bias answer length.**~~ Correct-is-the-longest went from 88% to 16% (target ≤ 30%), and no article is above 50%. Follow-up: the correct option is now the *second*-longest in 54% of questions. A weaker cue, but it should be spread evenly; `check-content.py` warns about it.
2. ~~**Fix source links.**~~ 21 of 26 slugs were wrong; now taken from the book. (Not yet re-verified by HTTP status.)
3. ~~**Add `scripts/check-content.py`.**~~ JSON validity, id uniqueness, answer index in range, duplicate options, missing explanations, answer-length bias and length-rank spread. Run before every push.
4. ~~Rename manifest title; keep the Check button enabled with an inline “Pick an answer first.”~~

### Phase 1b — Content accuracy — done 15 Nov
Checking the book against Calabro's posts showed that some original chapters, and the app cards built from them, had drifted from the source. Example: *UX Research Starts with Tasks* taught a three-step task-writing framework that isn't in the post, which is about building a Top Task List.

- **Rebuilt from the posts (cards + questions):** tasks, usability-vs-concept, cognitive-walkthrough, fake-ai, cognitive-biases, ab-testing, dashboard, debrief, delight, figma. Generators are in `scripts/rewrite_batch1.py` and `rewrite_batch2.py`.
- **Checked against the posts and rewritten (4):** predictions (listed two predictions Calabro never made), behavioral-evidence (invented three cognitive mechanisms; the post gives three organisational reasons and a behaviour/perception/sentiment framework), ic (invented an "IC ceiling" section), thankless (invented the term "absence metrics").
- **Checked and patched (3):** institutional cited icon testing "across seven organizations"; icons misstated why Google gets away with unlabeled icons; mixed-methods claimed a five-criteria self-check.
- **Checked and correct (9):** research-rigor, research-service, ab-mislead, misunderstandings, affordances, animations, input-field, status-design, roi. Verified down to the figures — Yale's 40%/18% carousel data, the 2013 NN/g Siemens test, 100ms feedback, 7–8 ubiquitous icons, the 7 input-field elements and Type 1/Type 2 reframe, five meanings of "Pending", the university ROI example, the Three Magic Questions, MeasuringU's nine participants, Baymard's 300–500ms hover delay and the search/navigation split.
- The same four corrections were applied to the book (`fixes.py`).

### Phase 3+4 — Full book coverage — done 15 Nov
The app now carries **all 99 chapters of the book** (was 26), restructured into 12 modules:

| Module | Articles | Module | Articles |
|---|---|---|---|
| Foundations | 10 | Experiments & Statistics | 12 |
| Interaction Design | 10 | Surveys & Metrics | 5 |
| Forms, Controls & Status | 8 | Data Visualization | 3 |
| Accessibility & Content | 6 | Business Impact | 9 |
| Running Studies | 11 | AI UX | 4 |
| Evidence & Bias | 9 | Career & Influence | 12 |

Each new article has 3 learn cards with a quick check and a 5-question quiz, written from Calabro's posts via the book (792 questions in total). Generators live in `scripts/b_*.py`; `scripts/restructure.py` rebuilds the manifest from `scripts/article-meta.json`.

Companion articles (Friedman, Raudaschl, FT, AI UX Playground, Hall/Torres) have no single original post, so they carry a `sourceNote` instead of a `source` URL, and the app renders it as text.

**Answer-length bias after the expansion:** the correct option is the longest in 21% of questions (target ≤ 30%); by length rank it is 1st in 26%, 2nd in 40%, 3rd in 15%, 4th in 18%. Rank 1 is now at chance level. Rank 2 at 40% is the remaining weak cue and is worth evening out.

### Phase 2 — Retention mechanics — done 15 Nov
5. **Missed-question bank.** A wrong answer stores `articleId#questionIndex` in `uxp-progress-v1.missed`; the reference is dropped after **two** correct answers (one isn't enough to show it stuck). The home screen shows "Review missed questions · N waiting", and `#/review` lists them grouped by article with `#/review/run` drawing up to 12.
6. **Module review quiz.** `#/m/<id>/review` — 10 questions across the module, weighted toward the ones you have missed, with the source article named above each question. Marks the module "Reviewed" and records the last score. A card at the bottom of every module page starts it.
7. **Concept index.** `#/index` — all 297 learn-card titles grouped by module, each linking to its card, with a live filter.

Correct answers in any session (article quiz, module review or review run) count toward retiring a reference, so the bank drains through normal use.

### Phase 5 — Install and offline (2 hours)
12. `manifest.webmanifest` + minimal service worker (cache-first for app shell and `content/*.json`, network-first for manifest). Add-to-home-screen on the phone; works on the walk without signal.

### Not planned
- Streaks, points, badges, leaderboards — against the brief.
- Hall's surveys/personas/recruiting, Torres's opportunity solution trees — different scope; the skills cover them for daily work.
- Cross-device sync beyond copy/paste — would need a backend.

## Definition of done per phase
- Phase 1: `check-content.py` passes with no errors (done); all 26 links return 200 (open); Phase 1b's 16 articles verified against the posts (open).
- Phase 2: verified — a failed question enters the bank, survives one correct answer, and leaves on the second; module review runs for all 12 modules; all 297 index links resolve.
- Phase 3–4: structure done and all 99 render; an independent check of each new article against its source post is still outstanding.
- Phase 5: app loads with network disabled after one visit.
