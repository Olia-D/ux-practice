# Test Cases

These define the behaviors this skill should reliably produce. Use them to verify the
skill is working correctly after install or updates.

---

### Test 1 — Required field indicator (REVIEW)
**Prompt:** "We mark only optional fields with '(Optional)' and leave required fields unmarked. Is that okay for a self-serve setup form?"

Expected: flags the approach as a usability risk → explains why field-level indicators are
needed (attention stays at field level, top instructions are skipped/forgotten) → cites
Type 1 vs Type 2 error tradeoff → recommends asterisks on all required fields → notes
accessibility requirement → frames cost in business terms.

---

### Test 2 — Form design from scratch (CREATE)
**Prompt:** "Design a required field indicator system for a self-serve B2B onboarding form. Users set this up once, without training."

Expected: structured spec (not just bullets) → asterisk on all required fields →
discourages top-of-form-only instruction → "(Optional)" guidance for mixed forms →
accessibility note → stakeholder pushback response for the "visual clutter" objection.

---

### Test 3 — Icon label pushback (SUGGEST)
**Prompt:** "Our PM wants unlabeled icons in the left nav. He says it looks cleaner. What are my options?"

Expected: 2+ distinct options → explains why unlabeled icons fail (location memorization,
not meaning) → addresses "looks cleaner" with business framing → clear recommendation for
B2B SaaS nav → does not validate the PM's preference uncritically.

---

### Test 4 — Dashboard info architecture (REVIEW)
**Prompt:** "We're putting key performance metrics behind three tabs because it looks less cluttered. Users need to compare numbers across them."

Expected: flags tabs as a memory burden problem → explains comparison requires co-presence →
offers concrete alternatives (summary row, side-by-side, expandable) → frames cost around
the three dashboard jobs: monitor, diagnose, prove ROI.

---

### Test 5 — Post-action status design (REVIEW + CREATE)
**Prompt:** "After a customer activates an automated email campaign, we just show 'Active' as the status. Is that enough?"

Expected: flags "Active" as insufficient for a B2B self-serve context → explains the six
questions users carry after an action → identifies what's missing (evidence of activity,
next step, whether any action is needed) → offers a concrete improved status label →
references the difference between communicating state vs. communicating meaning.

---

### Test 6 — UI animations (REVIEW)
**Prompt:** "We want to add an auto-rotating carousel to the dashboard homepage to highlight key metrics. Good idea?"

Expected: flags auto-rotation as a usability and accessibility risk → explains banner
blindness and the Yale/NN/g carousel engagement data → notes cognitive load cost →
recommends static or user-triggered alternatives → does not validate the idea.

---

### Test 7 — Permission-limited action (REVIEW)
**Prompt:** "Viewers can't publish, so we disable the Publish button for them. Fine?"

Expected: asks whether viewers ever need to know publishing exists → if yes, keeps it
disabled **with a visible reason** and how to get access → if never, hides it and designs
when it appears → notes legibility and focusability for screen readers → does not leave a
silent disabled button.

---

### Test 8 — Running a critique (CREATE)
**Prompt:** "Our design critiques turn into opinion fights. How should I run them?"

Expected: separates the meeting types (critique, design review, quality review, shareout)
→ recommends 4–6 people with rotating roles → gives the timed 30-minute agenda with silent
written feedback before discussion → sets the discussion order → keeps feedback as
questions, optional for the designer, in a critique.
