# ux-practice
Practice ux

## Before you push

Run `python3 scripts/check-content.py`. It fails on broken content (bad JSON, missing files, answer index out of range, duplicate options) and warns when the length of the options gives the answer away.

## Routes

- `#/` modules · `#/m/<id>` module · `#/a/<id>/learn/<n>` learn card · `#/a/<id>/test` quiz
- `#/review` missed-question bank · `#/review/run` run a review
- `#/m/<id>/review` module review quiz · `#/index` concept index
