# Forms & Input Fields — Pattern Reference

## Why this matters
Forms are where users do real work — entering data, submitting decisions, configuring settings.
Every small friction point compounds. A form that looks clean but offloads cognitive work onto
the user will produce errors, abandonment, and support tickets. These principles reflect 40+
years of HCI research and are not up for aesthetic debate.

---

## Labels

Every input field must have a persistent, visible label placed **above** the field.

Labels must never disappear when the user clicks in. Once a user starts typing, the label
is the only thing that tells them what they're filling in. If it vanishes, the interface
has converted a recognition task into a memory task — and working memory fails under
distraction, fatigue, and interruption.

**Avoid:**
- Floating labels (label animates to top on focus) — creates the same memory problem,
  plus screen reader and browser autofill compatibility issues
- Placeholder-as-label — the worst pattern: disappears at the exact moment it's needed most,
  has low contrast by default, and many assistive technologies don't read it reliably

---

## Required Field Indicators

Mark every required field with an asterisk (*) **at the field label level**.

Do this even when every field in the form is required.

**Why the top-of-form "all fields required" approach fails:**
Users don't read forms top-to-bottom before starting. Eye-tracking research confirms attention
stays where the cursor is — one field at a time. Instructional text at the top gets skipped,
and even users who read it forget it by the time they reach the 4th or 5th field. When they
skip a required field, submission fails, and they have to hunt for what went wrong. That's
a preventable error caused by the design, not the user.

**The Type 1 vs Type 2 error frame** (useful for stakeholder conversations):
- Type 1 (over-signaling): asterisks on all required fields → small visual noise, low cost
- Type 2 (under-signaling): one line of text at the top → submission failure, forced backtracking, high cost

When someone argues asterisks create "visual clutter," reframe it: we're choosing which
failure mode is less harmful. A small, familiar symbol is a much cheaper error than a
blocked submission at the end of a completed form.

**Accessibility requirement:** A red asterisk alone is not sufficient. Pair it with
programmatic `required` state so screen readers announce it, and ensure it's visible
for users with color perception differences.

**When to use "(Optional)":**
Only add "(Optional)" to fields when a form has a mix of required and optional fields.
Mark the optional ones, not the required ones. This removes hesitation and prevents users
from treating optional fields as required.

---

## Placeholder Text

Almost never use placeholder text as instruction.

Static placeholder text disappears the moment the user starts typing. It has low contrast
by default (failing WCAG), and many assistive technologies skip it entirely.

**The one acceptable use:** Auto-formatting hints that appear *as the user types* (e.g.,
phone number grouping, date separators) are different from static instructional placeholders
and are genuinely helpful. These guide entry without vanishing before the user needs them.

---

## Help Text & System Feedback

- Explanatory text must be **visible at all times** — never hide it behind an "i" icon or
  tooltip when users need it to complete the field correctly
- System help text (requirements, format guidance, character limits) goes **below** the field
- Error messages appear at the **field level**, not only in a banner at the top of the form
- Field-level errors give users the exact location of the problem — top-only errors force a hunt

---

## Auto-formatting

Implement auto-formatting wherever possible: phone numbers, postal codes, dates, currency,
ID formats. This guides users during entry, reduces format errors, and makes validation
feel helpful rather than punishing.

---

## Quick Decisions

| Choice | Recommendation | Reason |
|--------|---------------|--------|
| Label inside field | Never | Disappears when needed most |
| Floating label | Avoid | Memory burden + a11y issues |
| Required asterisk on all required fields | Always | Just-in-time, prevents submission errors |
| "(Optional)" label | Only when mixed required/optional | Removes false assumptions |
| Placeholder as instruction | Never | Disappears, low contrast, a11y fails |
| Single "all fields required" at top | Insufficient alone | Users skip or forget it |
| Error message at top of form only | Insufficient | Forces users to hunt for the problem |
| Auto-formatting | Use where possible | Guides entry, reduces errors |
