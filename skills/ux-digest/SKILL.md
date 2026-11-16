---
name: ux-digest
description: >
  Fetch and analyze the latest posts from Marina Krutchinsky's Substack, Nick Babich's YouTube
  channel, and Trevor Calabro's Substack, then deliver a structured weekly digest with summaries
  and key themes. Use this skill whenever the user asks to "check UX feeds", "what's new from
  Marina, Nick or Trevor", "get the UX digest", "run the weekly digest", "summarize recent UX
  posts/videos", or any request to catch up on these three creators' latest content. Also trigger
  if the user asks to analyze UX career, interaction design, or AI design content from these people.
---

# UX Digest Skill

This skill fetches the latest content from three UX creators and delivers a clean, insightful
weekly digest with summaries and recurring themes. Runs every Sunday and displays results in Cowork.

## Creators to Monitor

| Creator | Platform | URL |
|---------|----------|-----|
| Marina Krutchinsky | Substack (UX Mentor Diaries) | https://substack.com/@uxmentor/posts |
| Nick Babich | YouTube | https://www.youtube.com/@babichnick/videos |
| Trevor Calabro | Substack (UX Research in the Wild) | https://trevorcalabro.substack.com/archive |

---

## Step-by-Step Workflow

### 1. Fetch Marina's Latest Substack Posts

Navigate to https://substack.com/@uxmentor/posts using the browser.

- Scroll down to load at least 6–8 recent posts
- For each post, capture: **title**, **date**, **subtitle/teaser**
- Do NOT click into individual posts unless a teaser is missing — list view is enough
- Aim to capture posts from roughly the last 7 days (since last Sunday)

### 2. Fetch Nick's Latest YouTube Videos

Navigate to https://www.youtube.com/@babichnick/videos using the browser.

- The page defaults to "Latest" — keep it there
- Scroll to capture at least 8–10 recent videos
- For each video, capture: **title**, **view count**, **time since upload**
- Note which videos have significantly higher views — this signals resonance

### 3. Fetch Trevor's Latest Substack Posts

Navigate to https://trevorcalabro.substack.com/archive using the browser.

- Capture posts from roughly the last 7 days (since last Sunday)
- For each post, capture: **title**, **date**, **subtitle/teaser**
- Trevor publishes weekly — expect 1–2 new posts since the last digest
- His content focuses on evidence-based interaction design, HCI research, and UX practice

### 4. Produce the Digest

After collecting content from all three sources, display the digest directly in Cowork:

---

## UX Digest — Week of [Today's Date]

### 🗞️ Marina Krutchinsky — UX Mentor Diaries
*Substack | [X new posts this week]*

**This Week:**
For each post, write 1–2 sentences on what it's about and why it matters. Focus on the
insight or takeaway, not just restating the title.

**Recurring Themes:**
Identify 2–3 patterns across her recent posts. Be precise: not "she covers career topics"
but "she's focused on how designers frame research as financial risk to leadership."

**Most Practical Post:**
The one post most immediately actionable. One sentence on why.

---

### 🎬 Nick Babich — YouTube
*@babichnick | [X new videos this week]*

**This Week:**
For each video, write 1 sentence on what it covers. Note view count and flag any breakout
videos (significantly more views than the rest).

**Recurring Themes:**
Identify 2–3 content themes across recent videos.

**Most Watched:**
Highest-view video this week and why it likely resonated.

---

### 📖 Trevor Calabro — UX Research in the Wild
*Substack | [X new posts this week]*

**This Week:**
For each post, write 1–2 sentences on what it argues and what the practical takeaway is.
Trevor's posts are evidence-heavy — call out the specific research or principle he cites.

**Recurring Themes:**
Identify the pattern across his recent posts (he often circles back to the same underlying
argument from different angles — name it explicitly).

**Most Applicable to B2B SaaS:**
The post most relevant to product/dashboard/form design work. One sentence on why.

---

### 📊 Cross-Creator Patterns
This is the editorial highlight of the digest. Look for themes appearing across two or
more creators independently. When Marina, Nick, and Trevor all circle the same topic from
different angles, it signals something real is happening in the field. Name the convergence
explicitly and explain why it matters.

If there's no clear cross-creator pattern this week, say so honestly rather than inventing one.

---

## Tone & Style Notes

- Write for someone who follows all three creators but hasn't had time to read/watch everything
- Be specific — quote titles, name tools mentioned, reference actual frameworks
- Keep each post/video entry tight: 1–2 sentences max
- The Cross-Creator Patterns section is the editorial highlight — spend time on it
- If a creator hasn't posted since last Sunday, note that rather than padding with older content

---

## Known Context (pre-loaded to save browsing time)

As of April 2026. Always fetch fresh content — use this only as background.

**Marina Krutchinsky** (8.6K subscribers, #37 in Design on Substack):
- Publishes every Wednesday and Saturday
- Focus: how designers communicate with VPs and C-suite — making research feel like financial
  risk to ignore, not a "nice to have"
- Bundles practical Notion templates with posts (Cost-of-Inaction Builder, Strategic Ask Builder)
- Draws from her own experience as VP of UX Design at JPMorgan Chase

**Nick Babich** (@babichnick, 20.3K subscribers):
- Posts multiple times per week
- Dominant theme: Claude Code for UX/product designers — Claude Code + Figma, CLAUDE.md,
  Skills, Plan Mode, Ultraplan, design system documentation
- Broader: AI-powered design workflows (Gemini, NotebookLM, Vibe Design)
- Most-watched recent video: "Claude Skills 2.0: How to use Skill Creator" (~14K views)

**Trevor Calabro** (UX Research in the Wild, ~1.7K subscribers):
- Publishes weekly
- Focus: evidence-based interaction design and HCI research applied to real-world products
- Recent topics: form design, required field indicators, icon labeling, status design,
  split buttons, accessibility as usability, cognitive walkthroughs, UI animations
- Style: practitioner-grounded, cites 19+ years of field experience and actual usability data
- Particularly relevant to B2B SaaS and dashboard/form design work
