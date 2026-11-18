# Design Systems — Pattern Reference

A design system is patterns, the shared language that names them, and the practices that
keep them alive. Review a system for adoption and decay, not only for component quality.

## What's in a system

| Part | Contents |
|---|---|
| Functional patterns | The parts people use: buttons, fields, tables, navigation |
| Perceptual patterns | How it feels everywhere: type, colour, spacing, motion, voice |
| Shared language | One name per pattern, the same in design files, code and conversation |
| Principles and guidance | Why and when to use each pattern, for designers, writers, PMs and engineers |

**From parts to pages:** atoms (inputs, buttons) → molecules (a search form) → organisms (a
header) → templates (layouts and content structure) → pages (real content). Test patterns on
pages with real and extreme content: one item and a thousand, short and very long names.

## Keeping it alive

- **Make it official:** a funded product with people and time. Start with a small pilot and
  show value before asking for a mandate.
- **Governance process:** how to request, change, approve, document, ship and retire a
  pattern, and who owns each step.
- **Retire with notice** and a recommended replacement.
- **Communicate change** where teams already work: change log, roadmap, office hours.
- **Keep design and code in sync**; a library that drifts from production loses trust.
- **Make it approachable:** a clear front page saying what it's for and how to use it.
- The biggest threat is neglect, not bad components.

## Team models

| Model | How it works | Risk |
|---|---|---|
| Solitary | One product team's library offered to others | Its own needs come first; others fork |
| Centralised | A dedicated system team builds and distributes | Drifts from product needs while proving its value |
| Federated | Designers from several teams decide together | Slow; decisions get lost without a scribe |

Whatever the model, someone writes decisions down and announces them.

## Style guides document behaviour

Visual values belong in tokens. The guide's job is states and behaviour: focus-visible,
pressed, selected and their combinations, loading, error, warning, success, disabled and
read-only. Undocumented behaviour becomes a build-time guess.

## Review questions

1. Is there a named owner and a written process for changing a pattern?
2. Do design and code use the same names?
3. Are states and behaviour documented, or only default and hover?
4. When did a pattern last get retired, and how were teams told?

Sources: Alla Kholmatova, *Design Systems* · Brad Frost, *Atomic Design* (chapters 2 and 5) ·
Nathan Curtis, "Team models for scaling a design system".
