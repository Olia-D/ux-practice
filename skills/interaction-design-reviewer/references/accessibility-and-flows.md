# Accessibility, Flows & Dashboard Design — Pattern Reference

## Accessibility as a Usability Standard

Accessibility is not a compliance checklist or a separate audit step. It's a real-world
usability standard — a stress test that reveals whether an interface was designed for
actual use or for idealized conditions.

When a design fails for a user with a disability, it's almost always exposing a weakness
that degrades the experience for all users under less-than-perfect conditions: distraction,
time pressure, device switching, fatigue, interruption.

**The 4 stress tests map directly to accessibility:**
- Memory burden → cognitive accessibility, working memory load
- Hidden information → screen reader access, keyboard navigation
- Cross-context inconsistency → assistive tech, device switching, responsive behavior
- Precision dependency → motor accessibility, mobile touch targets

**Order of operations:**
1. Make it accessible first
2. Make it usable within those constraints
3. Make it aesthetically polished within those constraints

Visual polish that compromises interaction clarity is the wrong priority order. Aesthetic
decisions cannot be made before usability decisions are resolved.

---

## Cognitive Walkthrough — Quick Method

Use a cognitive walkthrough to evaluate a flow (not just a single screen) before usability
testing. It's a cheap, structured method for catching obvious friction early — and it's more
reliable than a team demo because it forces reviewers to ask the right questions instead of
narrating from inside their own knowledge.

**The 4 questions to ask at each step:**
1. Will the user know what they are trying to do at this step?
2. Will they see the control or option that lets them do it?
3. Will they understand that this control does what they need?
4. After acting, will they receive feedback confirming it worked?

Document each step as Yes / No / Maybe with a brief note. Any No or Maybe is a finding.

**How to run it without bias:**
- Have reviewers answer the 4 questions independently before comparing — groupthink fills
  in gaps that real users would stumble over
- Start from realistic entry points (deep links, notification emails, alerts) — not the
  clean homepage that nobody actually uses as a starting point
- If a reviewer catches themselves narrating "and then the user would know to..." — stop.
  That narration is covering a discoverability gap, not resolving it.

A cognitive walkthrough done wrong — as a guided demo where someone explains what everything
does — is worse than not doing one at all, because it produces false confidence.

---

## Dashboard Design

Dashboards for B2B SaaS products have a specific usability challenge: users arrive with a
goal (understand performance, diagnose a problem, prove ROI) and need to get to an answer
quickly, often without any training.

**Comparison requires co-presence, not memory:**
When users need to compare values — metrics over time, before/after, segment A vs segment B —
those values must be visible simultaneously. Putting comparable data behind separate tabs
forces users to memorize one value while navigating to the next. This fails even for
highly motivated users under time pressure.

Use tabs only when information is genuinely mutually exclusive and comparison is not the goal.

**Progressive disclosure in dashboards:**
Not everything needs to be visible all the time, but the hierarchy must be learnable:
- Surface the most important signal first (the answer to "is this working?")
- Make drill-down feel predictable — users should be able to guess where more detail lives
- Don't hide actionable information behind hover states or icon-only controls

**Self-serve assumption:**
If customers use the dashboard without training or onboarding support, the design must do
all the explanatory work. Empty states, metric labels, status indicators, and contextual
help text are not optional polish — they are core functionality for self-serve products.

**Dashboard-specific anti-patterns:**
- Key metrics behind tabs when comparison is needed → forces memory-based comparison
- Hover-only tooltips as the only explanation for what a metric means → fails on mobile,
  fails for screen readers, fails under time pressure
- Icon-only action buttons in data tables → users can't tell what will happen on click
- Status indicators that rely on color alone → fails for color-blind users and in
  low-contrast environments

---

## Voyado-Specific Lenses

When designing or reviewing for Voyado products (Ratings & Reviews, Onsite Messenger Flows,
dashboards):

**Self-serve assumption applies everywhere.** Voyado's customers configure and monitor
products without Voyado team support in the room. Every piece of context that a trained
user would have in their head must be explicit in the interface.

**Setup flows are high-stakes and infrequent.** Users may configure a Messenger Flow or
set up a Reviews widget once, then not return for months. Design for the user who has
forgotten everything since last time — not for the user who uses it daily.

**Dashboard views serve three distinct jobs:**
1. Monitor: is everything working? (surface status clearly, no hunting)
2. Diagnose: why did this happen? (allow drill-down without losing the top-level view)
3. Prove ROI: show this number to my manager (make key metrics exportable and shareable)

Design for all three jobs, and don't let the "monitor" view hide the information needed
for "diagnose" and "prove ROI."
