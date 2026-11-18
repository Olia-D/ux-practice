---
name: "interaction-design-reviewer"
description: "Design, generate, and review UI designs, forms, controls and interaction patterns using evidence-based HCI research. Use whenever the user asks to review a design, create a form, pick a control, audit a flow, suggest alternatives, or get feedback on any interface decision — including \"does this follow best practices\", \"is this good UX\", \"how should I design X\", \"what are my options\". Covers forms, selection controls, icons, navigation, status design, accessibility, ARIA, animations, destructive actions, tables, hidden vs disabled states, design critiques, dark patterns, visual hierarchy, spacing, type, colour, touch targets, design systems and Jakob's Law. For charts and dashboards, data-visualization takes over."
---

# Interaction Design Skill

A skill for both **creating** new interaction designs and **reviewing** existing ones, grounded
in evidence-based HCI research. Works in three modes:

- **CREATE** — generate design specs, form structures, pattern options from scratch
- **REVIEW** — audit existing designs with structured critique + concrete alternatives
- **SUGGEST** — generate 2–4 distinct options when the right approach is unclear

The unifying principle behind every recommendation:
> A clean-looking interface is not the same as a usable one. Many designs appear polished
> because they offload cognitive work onto the user.

Always frame output in terms of **user behavior** and **business cost** — not "best practices."

---

## Reference Files

Load the relevant file(s) before responding based on what the request is about:

| Topic | File |
|-------|------|
| Forms, input fields, labels, required indicators, placeholders, help text | `references/forms.md` |
| Icons, navigation, affordances, signifiers, split buttons, animations, Jakob's Law | `references/controls.md` |
| Accessibility, accessibility audits, cognitive walkthroughs, flows | `references/accessibility-and-flows.md` |
| Status labels, post-action feedback, spinners, toasts, system state communication, degraded experiences | `references/status-design.md` |
| Running a design critique, review or shareout; giving and structuring feedback | `references/critique-sessions.md` |
| Visual hierarchy, spacing, type scale, line length, colour roles, contrast | `references/visual-design.md` |
| Mobile and touch: grips, tap accuracy by zone, target spacing, tab bars | `references/touch-and-mobile.md` |
| Design systems: pattern types, atomic levels, governance, team models, documenting states | `references/design-systems.md` |

**Related skills:** charts, dashboards and analytics views → `data-visualization`. Study
design, A/B critique, debriefs and ROI → `ux-research-advisor`. AI-powered features →
`ai-ux-patterns`. Load the related skill when the request crosses into its territory.

Load only what's relevant. For mixed requests (e.g. a form with icon-only actions), load multiple.

---

## Mode 1: CREATE

When asked to design or generate something from scratch:

**Step 1 — Clarify context** (ask or infer):
- What is the user's task? (e.g. "configure a flow", "submit a review", "filter a report")
- Who is the user — first-time, infrequent, or power user?
- Platform: desktop SaaS, mobile, or hybrid?
- What's the cost of a user error? Low stakes or high stakes?
- Any design system or component constraints?

**Step 2 — Generate a design spec** using this structure:

```
## [Component or Pattern Name]

Purpose: [What task this serves and why this pattern was chosen]

Structure:
[Each element in order — label, control, indicator, help text, feedback state]

Key decisions:
- [Decision]: [Reason grounded in user behavior, not aesthetics]

What to avoid:
- [Anti-pattern]: [The failure mode it causes for real users]

Stakeholder pushback prep:
- If someone says "[likely objection]" → [evidence-based response]
```

**Step 3 — Offer variants when there are real trade-offs:**

```
Option A — [Name]: [Description + when to use]
Option B — [Name]: [Description + when to use]
Recommendation: [Which one and why, given the stated context]
```

---

## Mode 2: REVIEW

**Step 1 — Understand context** (ask or infer):
- What is the user trying to accomplish? (task, not feature name)
- Who is the user and how often do they use this?
- Platform?
- What breaks if the user makes an error?

**Step 2 — Apply the 5 real-world stress tests** at each key interaction point:
1. **Memory burden**: must the user remember instructions or prior content to succeed?
2. **Hidden information**: is important content behind tabs, tooltips, hover, or accordions?
3. **Cross-context consistency**: does this behave differently on mobile vs desktop, or keyboard vs mouse?
4. **Precision dependency**: does success require hovering precisely or decoding visual minimalism?
5. **Build trap**: is the team measuring feature output (shipped it!) instead of user outcome (task completion, error reduction)? A polished Figma file is not evidence that users can complete the task.

A yes to any of these is a real-world friction point — flag it regardless of how it looks in a static mockup.

**Step 3 — Load the relevant reference file(s)** and check the design against specific pattern rules.

**Step 4 — Output findings** using this format:

```
❌ ISSUE: [Label]
What's happening: [The specific design choice]
Why it fails: [What real users do — behavior, not theory]
Business cost: [Abandonment / errors / support tickets / trust]
Alternative: [Specific, implementable fix]
Evidence: [Principle or research source]

✅ STRONG: [Label]
Why it works: [Brief explanation tied to user behavior]
```

Always include at least one concrete alternative for every issue — never criticism alone.

**Step 5 — End with a Priority Stack:**
The 3 highest-impact fixes, ranked, each with the alternative already named.

---

## Mode 3: SUGGEST

When asked "what are my options" or "how should I approach this":

Generate 2–4 genuinely distinct approaches (not just tone variations), each with:

```
Option A — [Name]
What: [One sentence description]
Best for: [Context where this works well]
Risk: [What could go wrong or needs validation]

Recommendation for your context: [Option X], because [reason tied to user type and task].
```

---

## Output Principles

These apply across all three modes:

- **Business framing first.** Every recommendation should be expressible as a completion rate,
  error rate reduction, or support cost — not just a UX principle.

- **Explain the why.** Don't just say what to do. Explain why real users behave in the way
  that makes this the right decision. The reasoning is what makes recommendations stick.

- **Concrete over vague.** "Add a label" is less useful than "Add a persistent label above
  the field that reads 'Campaign name' and stays visible while the user types."

- **Pushback prep.** For any recommendation likely to face aesthetic-driven pushback, include
  a ready-made response framed in behavior and cost — not design principle.

- **Never say "validate."** Framing research as "validating the design" primes for confirmation
  bias. Say "evaluate" or "test." Aim to be proven wrong.

- **Cheap tests first.** Sequence by cost: paper prototypes before interactive ones, colleagues
  before recruited users, competitor audits before building your own. Each cheaper round
  eliminates issues the expensive round doesn't need to find.

- **Test assumptions, not whole ideas.** Identify the riskiest assumption and test that
  specifically. A 10-person simulation test on one assumption takes a day; a full prototype
  test takes weeks.

- **Evaluate in parallel.** Never test a single option in isolation — confirmation bias
  guarantees you'll find reasons to love it. Always compare at least two alternatives.

---

## Pattern Index

A complete map of every pattern in this skill — what it is, when it's a risk, and where
to find the full detail. Use this as a quick reference when designing or reviewing.

---

### 🗂 Forms & Input Fields → `references/forms.md`

**Persistent above-field label**
Every input field needs a visible label placed above it that never disappears. Once a user
starts typing, the label is the only thing telling them what they're filling in. Remove it
and you've converted a recognition task into a memory task.
*Risk: users lose track of what a field is for mid-entry, especially under distraction or
on longer forms. Error rates rise, particularly in infrequently-used setup flows.*

**Floating label (avoid)**
The label starts inside the field and animates to the top on focus. Looks slicker than
placeholder-as-label but causes the same memory burden, plus screen reader and browser
autofill compatibility issues.
*Risk: screen reader announcements are unreliable; autofill often injects values without
triggering the animation, making filled fields look unfilled.*

**Placeholder-as-label (avoid)**
Using placeholder text inside the field as a substitute for a real label. The label
disappears the moment the user starts typing — exactly when they need it most. Placeholder
text also has low contrast by default (WCAG fail) and many assistive technologies skip it.
*Risk: highest-risk label pattern. Causes errors, abandonment, and accessibility failures
across the board.*

**Required field asterisk (*) on all required fields**
Mark every required field at the label level with an asterisk, even when every field in
the form is required. Eye-tracking research confirms users' attention stays at the field
level — one field at a time. A top-of-form "all fields required" instruction gets skipped
or forgotten by field 4 or 5.
*Risk of omitting: submission errors at the end of a completed form. Users have to backtrack
and hunt for what they missed — a preventable failure caused by the design, not the user.*

**"(Optional)" indicator**
Only add "(Optional)" to fields when a form contains a mix of required and optional fields.
Mark the optional fields, not the required ones. This removes hesitation and prevents users
from treating skippable questions as blockers.
*Risk of misuse: adding "(Optional)" to all fields, or using it inconsistently, creates
confusion about which fields are truly required.*

**Top-of-form "all fields required" text (insufficient alone)**
A single line of instructional text at the top of a form is not enough. Users skip it,
and even those who read it forget it before they reach the relevant fields. It can be
included as a supporting signal, but never as the only required indicator.
*Risk: creates a false sense that status has been communicated when it hasn't. Submission
errors feel unexpected and unfair to the user.*

**Placeholder text as instruction (avoid)**
Static placeholder text inside a field disappears on input, has low default contrast, and
is frequently skipped by assistive technologies. The one acceptable use is auto-formatting
hints that appear dynamically as the user types (e.g. phone number grouping).
*Risk: instructions vanish at the moment the user needs them. Common cause of format errors
and support tickets on forms with specific input requirements.*

**Visible, always-on help text**
Explanatory text that helps users complete a field correctly must be visible at all times —
never hidden behind an "i" icon or tooltip. System help text (format requirements, character
limits, warnings) goes below the field. Error messages appear at field level, not just in
a banner at the top of the form.
*Risk of hiding: users miss critical guidance, submit incorrectly, and hit preventable
error states. Top-only error banners force users to hunt for the problem.*

**Auto-formatting**
Implement auto-formatting wherever possible: phone numbers, dates, postal codes, currency,
ID formats. Guides entry in real time and makes validation feel helpful rather than punishing.
*Risk of omitting: format errors increase. Users submit data in the wrong format and receive
error messages that feel arbitrary rather than helpful.*

---

### 🎛 Icons, Controls & Navigation → `references/controls.md`

**Icon labeling (always required)**
Every actionable icon must have a visible text label — no exceptions for navigation bars,
toolbars, action buttons, or primary task controls. Users memorise icon *locations*, not
icon *meanings*. When icons move (redesign, new screen, responsive layout), even experienced
users are lost. There are only ~7–8 truly universal icons and none have 100% recognition.
*Risk: users can't find features after any layout change. Tooltips are not a substitute —
they fail on touch, require hover, and aren't reliably exposed to assistive tech.*

**Icon + label consistency**
When an icon and label appear together, both must tell the same story. A download icon
next to "Export to CSV" that actually opens a modal is a signifier conflict — it breaks
trust and generates support tickets.
*Risk: users learn not to trust the interface. Trust, once broken, is hard to recover.*

**Affordances (things should look like what they are)**
The visual appearance of any UI element should communicate what the user can do with it
without explanation or trial and error. Clickable elements must look clickable. Input
fields must look typeable. Tabs must look like tabs. If 95%+ of unfamiliar users can't
identify an element's purpose at a glance, the affordance is weak.
*Risk: users don't interact with elements they can't identify, or interact with the wrong
ones. Hidden functionality stays hidden.*

**Signifiers (labels should say what will happen)**
Button labels and action cues must describe the outcome, not the internal feature name.
"Download Report" should download a report. "Submit" should submit. A mismatch between
what a label promises and what actually happens is a dark pattern — it destroys trust
and generates confusion.
*Risk: users feel deceived. Even minor signifier mismatches ("Learn More" that opens a
paywall) erode confidence in the entire interface.*

**Split buttons (avoid)**
A split button combines a labeled primary action with a small dropdown arrow revealing
more options. Roughly 80% of users click only the labeled side and never find the dropdown.
The tiny arrow target causes fat-finger errors on mobile. Screen readers often can't access
the unlabeled arrow at all.
*Risk: hidden functionality goes unused. Users mis-click and trigger unintended actions.
Especially dangerous in flows with destructive or irreversible actions.*

**Auto-triggered animations (avoid)**
Any animation that plays without a user action — rotating carousels, autoplaying video,
scroll-triggered text reveals, pulsing chatbots, blinking attention-grabbers — harms
usability and accessibility. Over 92% of users describe them as annoying. Content that
moves gets ignored (banner blindness). Animated interfaces reduce comprehension by 26%
compared to static designs. WCAG 2.2 SC 2.2.2 requires a pause/stop control for moving
content lasting more than 5 seconds.
*Risk: users miss content entirely. Cognitive load increases. Users with vestibular
disorders, ADHD, dyslexia, or motor impairments are actively excluded.*

**When animation is acceptable**
Animations triggered by explicit user actions that communicate system state changes are
genuinely helpful. Examples: a progress indicator during a compute-heavy task, a file
icon animating to show where a download went, a cursor blinking after a field is focused.
These must end quickly and cleanly, and respond within NN/g timing guidelines (interactive
feedback within 100ms; hover content after 300–500ms).
*Risk of over-animating: even well-intentioned user-triggered animations slow users down
if they are too long, looping, or elaborate.*

**Jakob's Law (apply correctly)**
Users bring mental models from other products. Interfaces that match familiar patterns feel
intuitive. The law is frequently misused as retroactive justification — teams find one
example of a novel pattern online and claim user familiarity. The correct application
requires 5+ examples from similar products serving similar users.
*Risk of misuse: novel designs get shipped as "established patterns." Teams copy Google or
Salesforce without accounting for those platforms' ability to force habituation through
ubiquity — an advantage most products don't have.*

---

### ♿ Accessibility & Flows → `references/accessibility-and-flows.md`

**Accessibility as a usability standard**
Accessibility is not a compliance checklist or a separate audit. It's a stress test for
whether an interface works under real-world conditions. When a design fails for a user
with a disability, it almost always reveals a weakness that affects all users under less
ideal conditions: distraction, fatigue, time pressure, device switching.
*Risk of treating it as a checklist: accessibility problems are caught late, are expensive
to fix, and often signal deeper usability failures that affect the whole user base.*

**The 4 real-world stress tests**
Four questions to run against any key interaction point: (1) does the user need to remember
something to succeed? (2) is important content hidden behind a click, hover, or accordion?
(3) does this behave differently on mobile vs desktop, or keyboard vs mouse? (4) does
success require precision or decoding subtle cues? A yes to any of these is a friction point.
*Risk: designs that only work under perfect conditions — full attention, desktop mouse,
trained users — fail in the real world where conditions are never perfect.*

**Priority order: accessible → usable → polished**
Visual polish decisions cannot come before usability decisions. The correct order is:
make it accessible, then make it usable within those constraints, then make it aesthetically
polished within those constraints.
*Risk of inverting: aesthetics-first design trades interaction clarity for visual elegance.
Users pay the price in confusion, errors, and exclusion.*

**Cognitive walkthrough**
A structured method for evaluating a flow step-by-step before usability testing. Four
questions per step: will the user know what to do, see the right control, understand it,
and receive feedback after acting? Done correctly — with independent reviewers starting
from realistic entry points — it's one of the most cost-effective ways to catch obvious
friction early.
*Risk of skipping: friction that would be obvious to a new user gets shipped, because
everyone who reviewed it already knew how it worked. Risk of doing it badly: a guided
demo where someone explains everything produces false confidence.*

**Dashboards and charts → `data-visualization` skill**
Two rules stay here because they are interaction rules, not chart rules: comparisons need
**co-presence** (values compared must be visible at once — tabs and toggles turn
recognition into recall), and a dashboard serves **three jobs** (monitor, diagnose, prove
ROI) that need different design decisions. Everything else — chart choice, axes, colour,
layout, ACES, dataviz accessibility — lives in `data-visualization`. Load it for any
request involving a chart, KPI, metric or analytics view.

**Usability quality components**
A usability review should check against all five components: learnability (can a new user
figure it out?), efficiency (can a trained user do it fast?), memorability (can a returning
user re-learn quickly?), error recovery (can the user recover from mistakes?), and
satisfaction (is the experience pleasant?). Most reviews only check task completion —
that covers learnability and misses the other four.
*Risk: a design that's learnable but inefficient ships and frustrates power users. A design
that's efficient but unrecoverable ships and punishes mistakes.*

**Product trio for discovery**
Designer, PM, and engineer should observe the same user sessions together — each role spots
different signals from the same interview. The designer notices interaction friction, the PM
notices business-model misalignment, the engineer notices technical feasibility gaps. Handing
off research insights between roles loses the signal that comes from direct observation.
*Risk of solo discovery: the team builds on filtered summaries instead of direct evidence.
Critical context gets lost in translation between roles.*

**Self-serve assumption**
In products used without training or onboarding support, every piece of context that a
trained user holds in their head must be explicit in the interface. Empty states, metric
labels, status indicators, and help text are core functionality — not optional polish.
*Risk: self-serve users can't complete setup flows, misinterpret metrics, or can't tell
whether the product is working. Every gap becomes a support ticket.*

---

### 📡 System Feedback & Status → `references/status-design.md`

**Status labels must answer 6 questions**
After any significant action, users carry six questions: did it work? what's happening
now? do I need to do anything? can I leave? who owns the next step? how long will this
take? Good status design answers these explicitly. Bad status design forces users to infer.
*Risk: users refresh repeatedly, submit twice, ping colleagues, or build parallel
spreadsheets. Over time, workarounds become the actual workflow.*

**Vague status labels (avoid)**
Labels like "Pending", "Processing", "In Progress", and "Submitted" are technically
accurate but practically useless — each can describe multiple completely different system
states. "Pending" might mean waiting for a person, a sync, a nightly process, or a
broken state nobody has noticed.
*Risk: users can't tell if the system is working normally or stuck. Trust erodes.
"Pending legal approval" is always better than "Pending."*

**Spinners as the only feedback (insufficient)**
Spinners are acceptable for waits of 2–3 seconds. For anything longer, more complex,
or indeterminate, a spinner gives the appearance of feedback without any explanation of
what's happening, how long it will take, or what to do if it stalls.
*Risk: users assume the system is broken. Especially damaging in enterprise workflows
where users don't know if they should wait, refresh, or start over.*

**Toasts as the only confirmation (insufficient)**
Toasts confirm the thinnest version of success and then disappear — right when users
need orientation most. Temporary UI elements are also frequently missed entirely.
In B2B workflows the action that just occurred is often the start of a longer process,
not the end.
*Risk: users don't know if their action succeeded, what happens next, or whether they
need to do anything else. In multi-step workflows, this generates follow-up confusion
and duplicate submissions.*

**Status must be legible across time**
Users should be able to return to a workflow later and immediately understand where things
stand. A disappearing toast is not persistent status. "Last saved at 2:14 PM" in a stable
visible location is. A vague badge with no history is not. A status label with a timestamp
and brief change history is.
*Risk: users who return to a workflow after an interruption or the next day can't re-orient
without support.*

**Ownership and next steps must be explicit**
"In Review" is less useful than "In Review — assigned to [team]." When the user is done
and can safely move on, that should be stated explicitly. When another person or system
owns the next step, name them.
*Risk: users follow up too early, create duplicate requests, or stay on a screen they
could have left, wasting time and creating noise for the teams they're chasing.*

**The power-user fallacy**
When users adapt to bad status communication through repetition, it can look like expertise.
"Our users know how this works" usually describes people who have learned to compensate for
a system that never explained itself properly. That is not good design — it's offloaded
explanatory work.
*Risk: teams mistake user adaptation for product quality. Real problems go unfixed because
they're invisible to anyone who has already internalised the workaround.*

---

### ☑️ Selection Controls — the logic, not the taste

Choosing a control is a **logic question**. A mismatch between the control and what the
system does is an error, not a preference — and teams that re-debate it ship contradictions
developers spot immediately.

| Control | Use when |
|---|---|
| **Checkbox** | Independent options, zero/one/many. A single checkbox is one yes/no; the label is a statement. |
| **Radio** | Exactly one of two or more mutually exclusive options; the label is a question. |
| **Toggle** | A binary setting that takes effect **immediately**. If it needs a Save button, it isn't a toggle. |
| **Segmented** | 2–5 short options, single select, changing a setting or view of the same content. **Not tabs**: never use it for navigation or filtering. |
| **Dropdown** | Single choice from a long list (5+). Below that, show the options. |
| **Chips** | Short multi-select, usually filters. Not radio buttons in disguise. |

**Never pre-select.** In testing, pre-filled options are consistently overlooked and
submitted unchanged — that's an answer the user never gave. Sort options most to least
common, offer a way out ("None of the above"), and use ~40×40px targets.
*Red flags: a parent toggle over child checkboxes (nobody can say what it shows when one is
ticked), exclusive options as checkboxes, a legally required item shown as a disabled
toggle — offering a choice the user doesn't have. Say it in plain text instead.*

---

### 🧭 Navigation — information scent and the activation rules

Users forage: they follow clues that predict where their goal lives. **Information scent**
dies through compromise, not sabotage — a label rewritten for a marketing push, a category
renamed after the org chart.

*Weak scent:* vague labels ("Explore", "Solutions", "Resources") · icons without text ·
overlapping categories ("Help Center", "Support Articles" and "FAQs" together) · branded
language that isn't user vocabulary · IA that mirrors the org chart.
*Diagnose with:* tree tests and card sorts · 5-second tests · click tracking · quotes like
"I wouldn't have clicked that".

**Primary navigation rules (spec-ready, hand to engineering):**
- Activation is **click, tap, Enter or Space — never hover**. Hover is visual only: it can't
  open, close or dismiss anything, change ARIA state, or affect tab order. Moving the
  pointer away does **not** close an open menu.
- Every item is **either a link or a menu button, never both**. If a parent has its own
  page, put an "Overview" link inside the menu.
- Dismissal: re-activate the trigger, click outside, or Esc — with focus returning to it.
- Targets ≥ **24×24px**, spaced. Focus visible and clearly distinct from hover.
- Native HTML before ARIA: a landmark, real links and buttons, `aria-expanded` on triggers.
  Don't put `role="menu"` on site navigation — that's an application menu keyboard model.
*Risk: hover-driven menus and split rows are the two causes behind most navigation failures.*

---

### ↩️ Destructive Actions — confirm or undo

Choose by **severity × frequency**:
- Frequent + low impact → **Undo by default**
- Rare + low impact → one click, no interruption
- Frequent + severe → Undo, plus a warning
- Rare + severe → confirmation; **typed** when the stakes are high

Most actions are reversible, so Undo is the default and confirmation has to earn the
interruption. Genuinely irreversible: deleting linked items, removing data from other
people's accounts, disconnecting devices, leaving without saving. **If you can't make it
undoable, delay it** (e.g. 15 minutes before a permanent delete runs).

Label the **outcome**, never "Yes"/"Confirm": *Delete forever*, *Leave*, *Unsubscribe*,
*Stay*. No double negatives ("Cancel cancellation?"). Put Undo in a **persistent button**,
not only a toast that fades. Destructive actions never sit beside save or confirm, styled
alike, where muscle memory lands.

---

### 📑 Tables & Bulk Operations — the B2B work most products get wrong

Start from tasks: which filters, sorts, search, editing modes and permissions are needed.
Let users build their own filter set and show/hide/reorder columns when comparison matters.
Offer compact and comfortable **density modes**. Test with very long and very short values
and pseudo-localisation. Check how a screen reader moves through the table.

**Avoid hover-only row actions** — they cause errors and rage clicks, don't exist on touch,
and keyboard users can't reach them predictably. Use visible buttons on each row.

**Bulk import succeeds or fails in its repair step:** pre-import (template, example,
guardrails) → upload (drag, keyboard, paste) → map (match columns, check values) → **repair
(show only the error rows, dedupe)** → import (summary, tag the new records). Most products
dismiss a file as "invalid"; the value is helping users fix it in place.

**Tables have four jobs** — find records, compare, view/edit/add a single row, act on
records. Design each one on purpose. Right-align numbers and dates, left-align text; pin the
key column; set minimum widths per content type; show full precision on the active cell.

**Screen readers:** a `<caption>` is the table's accessible name; header cells (`th`) are
announced with every data cell; **don't make non-interactive cells focusable**. Editable
grids follow the ARIA grid pattern. Test: can a screen-reader user get what a sighted user
gets at a glance?

**Bulk:** define an **enablement rule per toolbar command** by selection count (0, 1, many).
Accept the file as it is rather than forcing a template first, **remember column mappings**
across sessions, suggest the nearest valid value for unmatched ones, allow a **partial
import** with a downloadable error report, and let people choose overwrite or skip for
duplicates. **The 5–20 item gap:** too many for one form, too few to justify a CSV — extend
the single form into a batch builder with one review step and one approval.

---

### 🙈 Hidden, Disabled or Read-Only — decide, don't default

Ask first **whether the feature should be limited at all**. Then:
- **Hide** when this user can **never** interact with it (irrelevant to the role, not part
  of their plan). Still design when, how and to whom it appears.
- **Read-only** mainly for fields whose value is **system-generated or edited elsewhere** —
  add a hint saying where it can be changed.
- **Disabled** when the user should know it **exists but can't use it now** (permissions,
  a missing prerequisite, a temporary state). **Always say why** and what unlocks it.

WCAG 2.2 AA doesn't require contrast on disabled controls, but people still need to read
them: keep the text legible and, ideally, focusable so screen readers announce the reason.
**Never hide buttons or filters by default** — people expect them to stay where they were.
*Risk: a disabled button with no reason reads as a bug and becomes a support ticket; a
hidden feature in a role-based product means nobody can tell a missing permission from a
missing feature.*

---

### 🪣 Effort — interaction cost and cognitive load

**Interaction cost** is total effort: physical (clicks, scrolls, typing) + mental (reading,
deciding, remembering) + recovery (errors, undo, backtracking), **multiplied by how often
the task is done**. A small cost in a once-a-year task is noise; the same cost in a task
done 40 times a day is a productivity problem. Unnecessary interactions are the worst kind
because users repeat them every time. Find it with task analysis and timing, observation in
context, and system data (drop-off, error logs, undo frequency, repeat attempts). Treat it
as a design input, not a post-launch metric.

**Cognitive load has three kinds** — "reduce cognitive load" is too blunt:
- **Intrinsic** — the task's own complexity. Can't remove it; **chunk** it.
- **Extraneous** — effort the design added: clutter, poor layout, jargon. **Remove it.**
- **Germane** — effort that builds a useful mental model. **Support it** with consistent patterns.
When you need numbers, **NASA-TLX** measures perceived workload on six dimensions.

**Miller's Law is about memory, not menus.** Miller studied recall of information that was
no longer visible; an open menu is a recognition task, so 7±2 says nothing about item count.
Labels and grouping decide success. Don't swap 7 for 4 either. Real working-memory demands
(a code carried between screens, values compared across pages) are flaws to remove.

---

### 💡 Help, Copy and Conversation

**Help belongs at the moment of the decision, inside the workflow.** Just-in-time, not
up-front; only ask for what the system genuinely needs now; make the next action explicit
(minimum text needed to be obvious, which is not the same as minimum text); adapt to role
and permissions; prevent first, then recover. *Patterns decades of data say don't work:
product tours before any task, forced optional setup, a "?" icon or tooltip holding
essential instructions, the floating help bubble.* Tools like Pendo make all four trivial to
add, which is exactly why they accumulate.

**"Conversational UX" is not a chatty tone.** It is interaction mechanics: **turn-taking**
(respond to what the user just did) · **context** (fit where they are) · **repair** (help
them recover) · **shared meaning** (their words, not system names). An auto-starting tour, a
"friendly" upsell modal and "Something went wrong" break all four — friendly wording can
disguise interruption, shaming and upsell. *Paper test:* print the words, have one colleague
play the system saying only what's printed, another play a user with a real goal. If the
system can only interrupt or repeat itself, it's a monologue.

**Content beyond readability:** a readability score says text is easy to read, not easy to
use. Structure (headings, chunks, links), IA matched to how users look for things (card
sorts and tree tests, not the org chart), and voice and tone sit above it.

---

### 📖 Style Guides — document behaviour, not looks

A typical guide shows default, hover and disabled, then leaves the rest to "dev will figure
it out". A button actually needs **focus-visible** and **pressed**, **selected** plus its
combinations (people switch between mouse and keyboard mid-task), **loading**, and **error /
warning / success / confirmation**. Pressed is the state skipped most often — and it's the
user's immediate proof that something happened. Focus-visible must be distinct from hover.
Visual values belong in tokens; **the guide's job is states and behaviour**.
*Risk: undocumented behaviour becomes a developer's decision at build time, without UX
context — surfacing later as bugs, accessibility failures and components that behave
differently in each part of the product.*

---

### 🔊 ARIA — four layers that matter

Rule one: **don't use ARIA if semantic HTML does the job.** When you do need it:
- **Anchor navigation** — `aria-current` ("where am I?"), one per set: page, step or location
- **Clarify meaning** — `aria-labelledby` / `aria-describedby`, reusing visible text
- **Reveal state** — `aria-expanded` on the toggle itself, optional `aria-controls`
- **Signal change** — `role="status"` (polite) or `role="alert"` (urgent)

Live regions must exist in the DOM **before** the update and must not be `display:none`;
marking everything assertive overwhelms people. For form errors set `aria-invalid` and link
the message with `aria-describedby`. In a financial-dashboard study every screen-reader
participant hit what one called "an invisible wall": missing `aria-current` sounds like "am
I on step two or three?"; a missing `aria-expanded` makes people assume the control is broken.

---

### 🕸 Dark Patterns — a principle beats a taxonomy

Naming patterns ("Roach Motel", "Confirmshaming") helped once, then became a loophole:
teams argue "that isn't *technically* Confirmshaming" instead of confronting intent. The
principle underneath: **every dark pattern removes the user's ability to act freely.**
Three questions — *can they stop? can they undo? can they refuse?* Any "no" is already
veering into manipulation.

Still everywhere in 2026, each failing a basic heuristic: **consent asymmetry** (Accept All
big, Reject buried) · **fake urgency** (a timer that resets on refresh) · **false scarcity**
· **pre-selected opt-ins** · **misleading labels** ("View pricing" → a sign-up form) ·
**forms that punish errors** (wiping input, blocking paste).

Pre-selection has no exceptions: a pre-checked opt-in is a dark pattern even
when the team believes users benefit — nobody should have to undo a choice they never made.
And **conversion isn't consent**: a 94% acceptance rate tells you what happened under those
conditions, not what people would have chosen freely. Accessibility is the canary: these
patterns break first, and hardest, for disabled users.

---

## Test Cases

Eight test cases covering the most common patterns are in `references/test-cases.md`.
Run them after install or updates to verify the skill is behaving correctly.

---

## Sources

The rules in this skill draw on: Trevor Calabro, *UX Research in the Wild*; Erika Hall, *Just
Enough Research*; Teresa Torres, *Continuous Discovery Habits*; Jakob Nielsen's usability
quality components; Vitaly Friedman (hidden/disabled/read-only, decision trees, degraded
experiences); Léonie Watson on accessible tables; Smashing Magazine and Flatfile on complex
tables and imports; WebAIM Screen Reader User Survey #9; Jeremy Bird on design critiques;
*Refactoring UI*; Matthew Butterick, *Practical Typography*; WCAG 2.2; Steven Hoober on touch
and grips; Alla Kholmatova, *Design Systems*; Brad Frost, *Atomic Design*; Nathan Curtis on
design-system team models.
