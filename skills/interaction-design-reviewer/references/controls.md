# Icons, Navigation & Controls — Pattern Reference

## Icons

Every actionable icon must have a visible text label. No exceptions for navigation bars,
toolbars, action buttons, or primary task controls.

**Why icons alone fail:**
Users don't memorize icon meanings — they memorize icon locations. When the same icon moves
to a different position (a redesign, a responsive layout, a different screen), even experienced
users are lost. This has been tested repeatedly: even self-identified "power users" fail to
correctly match unlabeled icons to their functions when icons are shuffled.

Even so-called "universal" icons fall short. There are perhaps 7–8 truly universal icons,
and recognition still isn't 100% — meaning some percentage of users will always fail. Labels
eliminate that gap entirely at minimal visual cost.

**Tooltips are not a substitute:**
Tooltips require an extra interaction (hover), don't work on touchscreens, interrupt the
flow of navigation, and are invisible to screen reader users unless specifically implemented.
They're for supplementary tips, not primary identification.

**Common objections:**

| Objection | Response |
|-----------|----------|
| "Labels make it too busy" | Clarity over minimalism. An interface users can't operate isn't good design — it's aesthetic smoke and mirrors. |
| "Tooltips are good enough" | Tooltips fail on touch, require hover, and are not reliably exposed to assistive tech. |
| "Google/Figma/Notion doesn't label icons" | Those platforms have captive user bases who absorb bad UX through repeated forced exposure. Most products can't afford that margin. |
| "Users will learn over time" | Any interface that requires training to understand is already a failed design. |

**Icon + label pairing:**
When an icon and label appear together, both must communicate the same thing. A mismatched
icon and label (e.g., a download icon next to the label "Export to CSV" that actually opens
a modal) creates a signifier conflict that erodes trust. When in doubt, drop the icon —
the label alone is always sufficient.

---

## Affordances

The visual appearance of a UI element should communicate what the user can do with it —
without explanation, tooltip, or trial and error.

- Clickable things must look clickable. A button styled as plain text is an affordance failure.
- Input fields must look like areas where typing is possible (visible container, border, background differentiation).
- Tabs must look like tabs. Toggles must look like toggles. Sliders must look like sliders.

A useful test: show the element to someone unfamiliar with the product and ask what they'd do
with it. If 95%+ give the same correct answer, the affordance is strong. If responses vary,
the affordance is weak.

---

## Signifiers

Signifiers are the labels, icons, and cues that tell users what will happen when they interact
with a control — not just what the control is, but what it does.

- "Download Report" should download a report. Not open a form. Not redirect to a page.
- "Submit" should submit. "Save Draft" should save a draft.
- Button labels should describe outcomes, not internal feature names

A mismatch between signifier and outcome is a dark pattern. It breaks trust and increases
support burden as users report the product as "broken" or "confusing."

---

## Split Buttons

Avoid split buttons in almost all cases.

A split button combines a labeled primary action with a small dropdown arrow that reveals
related options. It looks efficient but consistently fails in usability testing: roughly 80%
of users click only the labeled side and never discover the dropdown. On mobile, the tiny
arrow target compounds fat-finger errors. For screen reader users, an unlabeled arrow in the
focus order is a blocker.

The root problem: split buttons violate the mental model that one button equals one action.
That model has been reinforced by decades of web interaction. Deviating from it costs
hesitation, mis-clicks, and loss of trust — especially in conversion flows.

**Alternatives:**
- Two separate buttons side by side (primary + secondary) when both actions are frequent
- Primary button + plain menu button when one action is rare
- Inline chips or visible option controls when the choice itself is the decision
- Step-in flow on mobile when space is constrained

**The one valid exception:** Repeat-use desktop software with power users, where the default
action covers the vast majority of use, both targets meet size requirements, and labels are
visible on both sides. Even then, never use for navigation.

---

## Jakob's Law — Correct Application

Jakob's Law states that users spend most of their time on other products, so they bring
existing mental models with them. Interfaces that match those models feel intuitive.
Interfaces that deviate from them create friction.

**Plain meaning: don't reinvent the wheel without a strong reason.**

**How it gets misused:**
1. Retroactive justification — finding one example of a novel pattern and claiming user familiarity
2. Platform copying — citing Google or Salesforce patterns without accounting for the fact that
   those platforms can force habituation through ubiquity that most products cannot

**How to apply it correctly:**
1. Describe the user's task in plain language (not the feature name)
2. Find 5+ examples from similar products serving similar users
3. Identify what genuinely repeats across those examples — that's what users have internalized

If a pattern appears in only 1–2 cherry-picked interfaces, it's a novel design that needs
validation testing — not a familiar convention protected by Jakob's Law.

---

## UI Animations

Most UI animations that trigger without user action shouldn't exist.

This isn't an argument against animation in general — some animations genuinely help
usability. The problem is auto-triggered motion: anything that moves, rotates, pulses,
or plays without the user explicitly causing it.

**Common offenders:**
- Auto-rotating carousels
- Autoplaying video (especially in hero sections or dashboards)
- Auto-pulsing or auto-prompting chatbots
- Scroll-triggered text reveals
- Animated GIFs used as icons or decorative elements
- Auto-blinking elements used to draw attention to new features
- Interrupt pop-ups with animated entrances

### Why auto-triggered animation harms usability

**Users miss content that moves.** NN/g's usability test on a Siemens website found a
user who looked directly at rotating promotional content multiple times and still reported
"there aren't any" promotions. The content moved before her brain could process and act
on it. This is banner blindness — content that behaves like an ad gets ignored like an ad.
Yale usability testing found that engagement dropped from 40% on the first carousel panel
to 18% on the second, and plummeted from there.

**Motion increases cognitive load.** Auto-triggered animations fall into the "extraneous
load" category from Cognitive Load Theory — effort introduced by the design that makes
the task harder than it needs to be. A study in the Journal of Consumer Research found
animated web interfaces reduced comprehension by 26% compared to static designs, due
to divided attention and increased task switching.

**Users describe it as annoying, not delightful.** Over 92% of users in a Bureau of
Internet Accessibility study described auto-animations as "annoying." Real delight comes
from a system that makes a difficult task quick and easy — not from motion for its own sake.

**It slows users down.** In an NN/g study on scroll-triggered animations, users had to
wait for text to animate into view. They assumed the system was slow. In enterprise
products where time is real money, artificial delays have real cost.

### The accessibility cost

Auto-triggered animation actively excludes users:
- **Cognitive/visual processing**: WCAG 2.2 (SC 2.2.2) requires any content that moves
  for more than 5 seconds to have a pause/stop control. Users with dyslexia or visual
  processing differences can't keep up with moving content.
- **Motor impairments**: If a carousel rotates before a user with limited dexterity can
  interact with it, they're excluded by design.
- **ADHD**: Auto-triggered motion hijacks focus and breaks concentration — especially
  harmful in complex enterprise workflows.
- **Vestibular disorders**: Parallax, zoom transitions, and auto-scrolling can cause
  dizziness and nausea. Studies indicate up to 35% of users with vestibular disorders
  struggle with heavy-motion interfaces.

### When animation actually helps

Good animations share these qualities:
- Triggered by an explicit user action (not automatic)
- Communicate something about system state that would otherwise be invisible
  (e.g. a download progress indicator, a file moving to a tray)
- Reinforce cause and effect — showing users the result of their action
- End quickly and cleanly — no loops, no lingering
- Respond within NN/g timing guidelines: interactive feedback within 100ms,
  hover-triggered content after 300–500ms delay

The blinking cursor in a text field is a good example — it only blinks after the user
has explicitly focused the field. Chrome's download animation is another — it shows
progress and then where the file went, answering a question the user has.

### Decision rule

Before adding any animation, ask:
- Does this respond to something the user did?
- Does it communicate something the user needs to know?
- Would the interaction still work without it?

If the answer to any of these is no — remove it.

**Rule of thumb: if it moves and it's not helping, take it out.**
