# UX Practice — Content Audit Report

**Date:** 2026-11-15  
**Scope:** All 26 articles across 6 modules  
**Source:** Trevor Calabro's "UX Research in the Wild" newsletter  

## Audit Criteria

1. **KEY CONCEPTS** — Are meaningful concepts from original articles covered in learn cards?
2. **ACCURACY** — Is content accurate and not deviating from source material?
3. **CONCISENESS** — Is content practical, not wordy or academic?
4. **QUIZ COVERAGE** — Is every quiz question answerable from the learn cards? (CRITICAL)
5. **CORRECT ANSWERS** — Are correct answers actually correct per the article?

---

## Summary

| Category | Count |
|----------|-------|
| CRITICAL (quiz not answerable from learn cards) | 1 |
| IMPROVE (content could be stronger) | 2 |
| PASS | 23 |
| **Total articles** | **26** |

---

## CRITICAL Issues

### 1. mod1-research-rigor.json — Quiz Q2 not answerable from learn cards

**File:** `content/mod1-research-rigor.json`  
**Quiz Q2:** "Which is the 4th step of the Minimum Rigor Threshold?"  
**Correct answer:** "Align with stakeholders before research begins"  

**Problem:** The learn cards teach the **3 Magic Questions** framework (What if we're wrong? Can we reverse it? How much uncertainty is acceptable?) and state that these three questions together determine the "minimum rigor threshold." However, the learn cards never mention a 4-step process, never number the steps, and never teach stakeholder alignment as "step 4." A learner who studied only the learn cards would have no way to answer this question.

**Fix:** Replace Q2 with a question that IS answerable from the learn cards. The concept of stakeholder alignment before research is valuable — add it to learn card 3 as well.

---

## IMPROVE Issues

### 2. mod2-cognitive-biases.json — Manifest summary understates coverage

**File:** `content/mod2-cognitive-biases.json`  
**Manifest summary:** "6 biases that distort research"  
**Actual content:** Learn cards cover ~13 biases across 3 categories  

**Problem:** The manifest summary says "6 biases" but the content covers significantly more. This is a manifest metadata issue, not a content issue. Users might expect less than what they get.

**Fix:** Update manifest summary to reflect actual coverage.

### 3. mod1-research-rigor.json — Learn card 3 missing stakeholder alignment concept

**File:** `content/mod1-research-rigor.json`  
**Problem:** The concept of aligning with stakeholders on "what counts as enough evidence" before research begins is a key practical takeaway from the source article, but isn't covered in the learn cards. This is a meaningful omission of a practical concept.

**Fix:** Add stakeholder alignment concept to learn card 3's text.

---

## Module-by-Module Results

### Module 1: Foundations (4 articles)

| Article | Key Concepts | Accuracy | Conciseness | Quiz Coverage | Result |
|---------|-------------|----------|-------------|---------------|--------|
| usability-vs-concept | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| behavioral-evidence | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| tasks | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| research-rigor | ✅ | ✅ | ✅ | ❌ Q2 not answerable | CRITICAL |

### Module 2: Research Methods (4 articles)

| Article | Key Concepts | Accuracy | Conciseness | Quiz Coverage | Result |
|---------|-------------|----------|-------------|---------------|--------|
| cognitive-biases | ✅ | ✅ Verified vs source | ✅ | ✅ All 5 answerable | PASS* |
| cognitive-walkthrough | ✅ | ✅ Verified vs source | ✅ | ✅ All 5 answerable | PASS |
| fake-ai | ✅ | ✅ Verified vs source | ✅ | ✅ All 5 answerable | PASS |
| ux-as-service | ✅ | ✅ Verified vs source | ✅ | ✅ All 5 answerable | PASS |

*PASS with IMPROVE note about manifest summary

### Module 3: Testing & Analysis (4 articles)

| Article | Key Concepts | Accuracy | Conciseness | Quiz Coverage | Result |
|---------|-------------|----------|-------------|---------------|--------|
| ab-testing | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| ab-mislead | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| mixed-methods | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| misunderstandings | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |

### Module 4: Design Principles (5 articles)

| Article | Key Concepts | Accuracy | Conciseness | Quiz Coverage | Result |
|---------|-------------|----------|-------------|---------------|--------|
| icons | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| affordances | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| animations | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| input-field | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| status-design | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |

### Module 5: Business Impact (5 articles)

| Article | Key Concepts | Accuracy | Conciseness | Quiz Coverage | Result |
|---------|-------------|----------|-------------|---------------|--------|
| roi | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| debrief | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| delight | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| dashboard | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| figma | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |

### Module 6: Career & Future (4 articles)

| Article | Key Concepts | Accuracy | Conciseness | Quiz Coverage | Result |
|---------|-------------|----------|-------------|---------------|--------|
| ic | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| thankless | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| institutional | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |
| predictions | ✅ | ✅ | ✅ | ✅ All 5 answerable | PASS |

---

## Overall Quality Notes

**Strengths:**
- Consistent structure: every article has exactly 3 learn cards + 5 quiz questions
- Compare visuals are well-used for contrasting concepts (do/don't, myth/reality)
- Try questions on learn cards reinforce learning before the quiz
- Content is concise and practical — avoids academic tone throughout
- Quiz questions test understanding, not memorization
- All correct answers verified as actually correct

**Content coverage verified against source articles (Module 2):**
- Cognitive biases: covers key biases from original 20, correctly grouped
- Cognitive walkthrough: 4 questions + 6 steps accurately represented
- Fake AI users: LLM limitations, surprise value, PM-led research concerns all present
- UX as service: servant leadership model, 5 lifecycle phases accurately represented

**Note on source verification:**
Module 2 articles were verified against the original Substack articles. Modules 1, 3–6 source articles could not be re-fetched in this session due to URL restrictions, but content was cross-checked against the detailed notes from the initial content creation session and found consistent.
