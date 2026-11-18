# ux-practice
Practice ux

## Downloads

Two separate things live next to the app. Each can be used without the other.

### The book — *UX in the Real World*, reference edition (104 chapters)
Single self-contained HTML file; opens offline in any browser.
- [Download the zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/ux-in-the-real-world-book.zip) · or the file itself: [`book/ux-in-the-real-world.html`](book/ux-in-the-real-world.html) (use "Download raw file")

### The skills — UX design toolkit for Claude
Seven skills, each in `skills/<name>/` and as an upload-ready zip (SKILL.md at the zip root).

| Skill | Download |
|---|---|
| ux-start (router) | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-ux-start.zip) |
| ux-research-advisor | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-ux-research-advisor.zip) |
| interaction-design-reviewer | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-interaction-design-reviewer.zip) |
| ai-ux-patterns | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-ai-ux-patterns.zip) |
| data-visualization | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-data-visualization.zip) |
| jtbd-research | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-jtbd-research.zip) |
| ux-writing | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/skill-ux-writing.zip) |
| **All seven** | [zip](https://github.com/Olia-D/ux-practice/raw/main/downloads/ux-skills-all.zip) |

**How to install and use them:** [`skills/HOW-TO-USE.md`](skills/HOW-TO-USE.md). In short, upload one zip per skill under Settings → Skills on claude.ai, or copy the folders into `~/.claude/skills/` for Claude Code, then just ask.

## Design

Monochrome with one accent: green marks outcomes only (done, correct, passed). Type is Schibsted Grotesk (OFL, in `fonts/`). Colours, radii and type live in `tokens.css`, shared by the app and the book. The book inlines the tokens and an embedded Latin font subset, so it still works as a single offline file. After editing `scripts/book.css` or the book content, run `python3 scripts/book-restyle.py`.

## Before you push

Rebuild the zips with `scripts/build-downloads.sh` after changing a skill or the book. Run `python3 scripts/check-content.py`. It fails on broken content (bad JSON, missing files, answer index out of range, duplicate options) and warns when the length of the options gives the answer away.

## Routes

- `#/` modules · `#/m/<id>` module · `#/a/<id>/learn/<n>` learn card · `#/a/<id>/test` quiz
- `#/review` missed-question bank · `#/review/run` run a review
- `#/m/<id>/review` module review quiz · `#/index` concept index
- `#/library` book and skills: read or download · `#/library/skill/<id>` read a skill · `#/library/guide` how to use the skills
