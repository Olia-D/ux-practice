---
name: "ux-writing"
description: "Write and review product copy — button labels, error messages, empty states, form labels and help text, notifications, onboarding, status labels, confirmation dialogs and AI responses — using evidence-based content rules. Use whenever the user asks what a button or message should say, wants copy reviewed or tightened, names a feature, sets product voice and tone, or decides between 'your' and 'my'. Trigger with \"copy\", \"microcopy\", \"UX writing\", \"label\", \"button text\", \"error message\", \"empty state\", \"tooltip\", \"onboarding copy\", \"voice and tone\", \"naming\", \"terminology\", \"your or my\"."
---

# UX Writing

Words are interface. Most "usability problems" in a review are copy problems: a button
that doesn't say what it does, an error that blames, a status that means four things.

The unifying principle:
> Copy is judged by what the reader does next, not by how it sounds. If a line doesn't
> help someone decide or act, cut it.

Frame findings as **what the reader does wrong because of the words** and what that costs
(errors, support tickets, abandonment) — not as style preferences.

## Modes

- **WRITE** — draft copy for a screen, flow or component, with variants where the choice matters
- **REVIEW** — audit existing copy line by line: issue → why it fails → rewrite
- **SYSTEM** — set vocabulary, voice and tone, and naming rules for a product

---

## 1. Four standards for every line

| Standard | Test |
|---|---|
| **Purposeful** | Does it help the reader decide or act? If not, cut it. |
| **Concise** | Could it lose a third of its words and keep its meaning? |
| **Conversational** | Would a helpful colleague say it out loud like this? |
| **Clear** | Could someone new to the product act on it without asking anyone? |

Front-load the words that matter: people scan the first two words of a line.
Sentence case everywhere. No exclamation marks in errors. Numbers as digits.

---

## 2. Words first

Write the copy before the visuals; it exposes missing decisions early.
- **Start with onboarding and the most frequent error message.** Those two set the voice
  for everything else.
- **Organise copy by task, not by persona or screen.** List the questions a user has at
  each step, in priority order, and make sure each one is answered.
- **Use shared product vocabulary** — Log in, Save, Delete — not invented synonyms.
- **One word per concept, on every screen.** If it's "workspace" in settings, it's not
  "account" in billing. Keep a glossary.
- **Naming is hard and renaming after adoption is close to impossible.** Test names with
  users before they ship.
- **Give real durations** ("about 9 minutes"), not "a few moments".
- **Avoid the word "content"** and other words that mean nothing to the reader.
- **Read it aloud, then reread it tomorrow.**

---

## 3. "Your" or "my"? — who else is in the room

Ask who is speaking:
- **Nobody needs to be named** → no pronoun ("Settings", "Drafts"). This is the default.
- **The product is talking to the user** → "your" ("Your recommendations", "Your plan
  renews on 3 May"). Use for system-initiated content, onboarding, errors.
- **The user is talking to the product** → "my" ("Save my draft", "My list"). Use for
  things the user made or owns, privacy and personal settings.

Never mix both in one product for the same kind of thing, and never present the system's
decisions as the user's own ("My recommendations" is wrong — the user didn't make them).

---

## 4. Patterns

**Buttons and links**
- Verb + object, naming the outcome: *Save changes*, *Send invite*, *Delete campaign*.
  Never "Submit", "OK", "Yes" or "Confirm" alone.
- Keep the verb through the flow: the button says *Publish*, the toast says *Published*.
- Destructive actions name what is lost: *Delete forever*, not *Continue*.
- Links describe their destination; never "Click here" or "Learn more" alone.

**Error messages** — what happened, why (if useful), and how to fix it, in that order.
- **Validation:** next to the field, specific: "Enter a date after today", not "Invalid date".
- **System:** say it's on our side and what still works: "We couldn't save your changes.
  Your draft is safe — try again in a minute."
- **Blocking:** what's blocked, why, and the way out.
- **Permission:** who can do it and how to get access: "Only admins can publish. Ask an
  admin, or request access."
- Never blame ("You entered…"), never apologise more than once, never show error codes
  without a human sentence.
- Keep the user's input. Never clear a form because of one error.

**Empty states** — say what will appear here and give one way to start: "No campaigns yet.
Create one to start sending." For a filtered empty state, say what's filtered and offer to
clear it. For "everything done", say so plainly.

**Forms**
- Labels above fields, as nouns ("Company name"), never placeholders as labels.
- Help text before the field, for anything people get wrong: format, why it's asked.
- Mark optional fields, not required ones, when most fields are required.
- Ask only what you'll use; explain sensitive asks ("We use your phone number only for
  sign-in codes").

**Status labels** — answer "what's happening right now and do I need to do anything?"
"Pending" means four things; "Waiting for approval from your admin" means one.
Add time when it's predictable: "Usually done within 1 business day".

**Confirmation dialogs** — the title asks the specific question ("Delete 3 campaigns?"),
the body states the consequence ("Their reports will be deleted too. You can't undo
this."), the buttons name the outcomes (*Delete campaigns* / *Keep*).

**Notifications** — one per event that the reader can act on; lead with the change, not
the product name; link straight to the thing.

**Onboarding** — show the first useful action, not a tour of features. One idea per step.
Let people skip, and let them find it again later.

**AI responses** — say what it did and what it used ("Based on your last 3 campaigns…");
state limits plainly; never imply it's a person; label AI-written text.

---

## 5. Content design: start from a user need

Before writing, decide whether words are the answer. Content design means meeting a need in
the best way: a sentence in the interface, a page, or removing a page.

- **Write the need:** *As a* [role tied to the task, never "a user"], *I need to* [a task
  verb: apply, pay, change, claim], *so that* [why it matters]. "Understand" or "be aware
  of" only when the *so that* shows the task it serves.
- **No solution in the need.** "I need to use the calculator" justifies a tool; "I need to
  know how much I could get" is the need.
- **Acceptance criteria:** what must be true for the need to be met. Record need, criteria,
  evidence and owner, so content can be checked and retired.
- **Plan before writing:** how much, what format, where it lives, and whether it already
  exists. Then write, then maintain or archive.
- **Audit structure before rewriting a section:** list pages with hierarchy IDs (2.4.1),
  flag orphans and files, and compare menu labels with page titles.
- Settle style debates with evidence where it exists (the open *Readability Guidelines*).

## 6. Voice and tone

**Voice stays the same; tone moves with the reader's state.**

| Reader's state | Tone |
|---|---|
| Succeeding, routine | Brief, neutral — get out of the way |
| Learning, first use | Encouraging, explanatory |
| Stuck or confused | Calm, specific, one next step |
| Something went wrong / lost work | Serious, direct, responsible — no jokes |
| Anxious (money, data, security) | Precise, reassuring with facts, not adjectives |

Write the voice as a short list of **is / isn't / why**, with an example of each — e.g. "is
direct, isn't curt — because our users are busy, not beginners".

---

## 7. Review checklist

- [ ] Every button names its outcome; no "Submit", "OK", "Yes"
- [ ] The same action has the same verb from button to confirmation to toast
- [ ] Every error says what happened and how to fix it, next to the problem
- [ ] No line blames the user; no stacked apologies
- [ ] Empty states give one way to start
- [ ] Statuses say what's happening and whether action is needed
- [ ] One term per concept across the flow
- [ ] Pronouns follow the "who's in the room" rule
- [ ] Copy works without the visuals (read it as a list)
- [ ] Copy survives 30% longer translations and very long or short values

## Review output format

```
Line: "[current copy]"  — where it appears
Issue: [what the reader does wrong because of it]
Rewrite: "[new copy]"
Why: [behaviour + cost, one line]
```
End with the 3 rewrites that matter most.

**Related skills:** the control or status the copy sits in → `interaction-design-reviewer`.
AI-specific disclosure and trust copy → `ai-ux-patterns`. Testing whether copy works →
`ux-research-advisor`.

## Sources

Nick DiLallo, *Writing for billions*, and Vitaly Friedman (*Words First*; *Your vs My*,
2025, with Diana MacDonald's "who else is in the room" test) · Jane Ruffino, Microcopy
Canvas · Kinneret Yifrah, *Microcopy: The Complete Guide* · Torrey Podmajersky, *Strategic
Writing for UX* · the open-source content-designer UX-writing standards (purposeful,
concise, conversational, clear) · Trevor Calabro, *UX Research in the Wild* (labels,
status and error findings) · GOV.UK content design guidance (user needs, acceptance
criteria) · Content Design London, *Readability Guidelines* · Lisa Maria Marquis, *Everyday
Information Architecture* (structural audits).
