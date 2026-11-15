# UX Practice — gap analysis and implementation plan

Date: 2026-11-15. State audited: 26 articles, 78 learn cards, 130 quiz questions + 78 quick checks. App renders without console errors on iPhone viewport; home, module, learn, quiz and result views all work.

## Findings

### 1. Quiz validity — correct answer is the longest option 88% of the time (184/208)
Options are shuffled at runtime, so position doesn't leak — but length does. A test-wise learner can score ~90% without reading the cards. Eight articles are 8/8. This is the most important fix: it undermines the "test" half of learn-then-test.

### 2. "Read original article" links are guessed slugs
Manifest uses `/p/animations`, `/p/ab-testing`, `/p/ic`; the real posts are `/p/most-ui-animations-shouldnt-exist`, `/p/ab-testing-and-the-two-party-trap`, `/p/why-i-stay-an-ic`. Most of the 26 links are probably 404s.

### 3. Coverage — 9 of Calabro's 35 articles are not in the app
Confirmed missing: *UX Job Security*, *UX Has a Basics Problem*, *The Rules of AI Chat History*, *Reframing Dark Patterns: 2026 Edition*, *The Problem With Split Buttons*. The remaining four are in the HTML reference book on the Mac (`ux-research-in-the-wild-book.html`).

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

### Phase 1 — Fix what's broken (½ day)
1. **De-bias answer length.** Script flags every question where the correct option is the longest; rewrite distractors to match length and specificity (plausible wrong answers, not short throwaways). Target: correct-is-longest ≤ 30%, no article above 50%. Re-run the content audit agent on rewritten questions.
2. ~~**Fix source links.**~~ Done 15 Nov — 21 of 26 slugs were wrong; now taken from the book. Resolve all 26 real slugs; verify each returns 200; update manifest.
3. **Add `scripts/check-content.py`** — JSON validity, id uniqueness, answer index in range, longest-option ratio, every manifest file exists, link check. Document "run before push" in README.
4. ~~Rename manifest title~~ (done); enable the Check button with inline prompt.

### Phase 2 — Retention mechanics, no gamification (1 day)
5. **Missed-question bank.** Persist missed question refs per article in `uxp-progress-v1`; clear a ref when answered right twice. Home shows "Review 7 missed questions" when non-empty.
6. **Module review quiz.** `#/m/<id>/review` — 10 questions drawn across the module's articles, weighted toward missed ones. Counts toward module completion label ("Reviewed").
7. **Concept index.** `#/index` — every learn-card title grouped by module, linking straight to the card. Replaces re-reading.

### Phase 3 — Bring the app up to the book (1–2 days)
8. The book (v2, Nov 2026) has 54 Calabro articles; the app has 26. Not yet in the app, in priority order: UX Has a Basics Problem, Stop Weaponizing Miller's Law, Primary Navigation Guide, Onboarding & In-App Help, Stop Throwing Away Time-on-Task Data, A/B Test Strategies, A/B Sample Sizing, Statistically Significant or Not, Mixed Methods at Work, Choosing the Right Chart Type, Dark Patterns 2026, The Rules of AI Chat History; then the older book articles the app skipped (split buttons, navigation, carousels, Jakob's Law, accessibility, career paths). Same format; verify against originals with the audit agent.

### Phase 4 — Two new modules from today's sources (2 days)
9. **Module 7 — Data Visualization** (5 articles): Choosing the chart (FT purposes) · Chart design rules (London: data-ink, labels, zero baseline) · Colour scales (Datawrapper) · Dashboards that lead to decisions (ACES + Calabro's three jobs) · Accessible charts (Fossheim, Chartability critical checks). Compare visuals carry most of the weight here.
10. **Module 8 — AI UX** (5 articles): How much should the agent do (Agentic L1–L5 + scoring) · Trust at the moment of reliance (T.R.U.S.T.) · Anatomy of a chat turn (C.O.N.V.E.R.S.E.) · Memory and chat history (Playground guide + Calabro) · Citations and failure disclosure. Source: aiuxplayground.com frameworks, with "breaks as" anti-patterns as the quiz material.
11. Update schedule text (8 modules, ~8 weeks), header count (26 → 40), unlock chain.


### Phase 4b — From saved LinkedIn posts (1½ days)
Reviewed all 85 saved posts (Nov 2026). ~50 are tool lists, Figma plugins, portfolio/interview tips or resource dumps — skipped. These carry rules the app and skills don't have:

| New article | Module | Source | Why |
|---|---|---|---|
| Confirm or Undo? | 4 Design Principles | Friedman, Confirm vs Undo decision tree | Severity × frequency rule; Undo by default, typed confirm for severe+rare; specific verbs ("Delete forever") not "Yes/Confirm" |
| Choosing the selection control | 4 | Goswami/Lyft decision tree | Radio = question, checkbox = statement; never pre-select; dropdown only for 5+; toggle only for instant effect |
| Tables and bulk operations | 4 | Sergushkin/Shestopalov tables; Friedman bulk import | B2B core: no row-hover actions, column show/hide, density modes; 5 import stages (pre-import → upload → map → repair → import) |
| Research without user access | 2 Running Studies | Friedman, B2B/enterprise research | What you can do when you can't recruit: task analysis, job postings, shadowing proxies, CS/domain experts; buyer ≠ user |
| Measuring feature impact (TARS) | 5 Business Impact | Raudaschl via Smashing | Target → Adoption → Retention → Satisfaction (CES); thresholds; deliberately excludes conversion — matches Calabro on attribution |
| AI labelling is now law | 8 AI UX | Friedman/Smashing on EU AI Act Art. 50 | In force since 2 Aug 2026 for anything EU users see: chatbots/agents disclose, deepfakes, unreviewed public-interest text; a sparkle ✨ is not a label; icon + plain text, persistent, accessible |

Folded into planned articles rather than new ones: Bach et al. dashboard tradeoffs (screenspace ↔ abstraction ↔ pages ↔ interaction; "you might not need a dashboard") → Module 7 dashboards; UX KPI targets → Module 5 ROI; design critique formats + Samsonov "design is taking too long" → Module 6.

### Phase 5 — Install and offline (2 hours)
12. `manifest.webmanifest` + minimal service worker (cache-first for app shell and `content/*.json`, network-first for manifest). Add-to-home-screen on the phone; works on the walk without signal.

### Not planned
- Streaks, points, badges, leaderboards — against the brief.
- Hall's surveys/personas/recruiting, Torres's opportunity solution trees — different scope; the skills cover them for daily work.
- Cross-device sync beyond copy/paste — would need a backend.

## Definition of done per phase
- Phase 1: `check-content.py` passes; all 26 links return 200; audit agent re-verifies rewritten questions.
- Phase 2: a missed question reappears in the bank and in the module review; index links land on the right card.
- Phase 3–4: audit agent confirms each new article against its source; no quiz question asks what the cards don't teach.
- Phase 5: app loads with network disabled after one visit.
