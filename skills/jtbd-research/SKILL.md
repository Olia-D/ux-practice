---
name: "jtbd-research"
description: "Frame user research around Jobs to Be Done (JTBD) — statement templates, forces-of-progress interview probes, and competitive comparison matrices. Make sure to use this skill whenever Olha is trying to understand user motivation, positioning, or why users chose/dropped a product, even if she doesn't say \"JTBD\" explicitly — e.g. \"why do people actually use this over the alternative\" or \"help me write up why users churned.\" Trigger with \"jobs to be done\", \"JTBD\", \"job story\", \"why did users switch/adopt/drop this\", or positioning and competitive research questions."
---

# Jobs to Be Done (JTBD)

Use this skill when the goal is understanding *why* users adopt, switch to, or drop a
product — not evaluating a specific screen or flow (for that, use interaction/design
critique skills instead). JTBD reframes research around the progress a user is trying to
make in their life or work, rather than around product features or demographics.

Good triggers: positioning work, competitive analysis, "why did we win/lose this user",
onboarding drop-off, feature prioritization, or any point where research needs to explain
motivation rather than usability.

**Core concept:** customers don't buy products for their features — they "hire" a product
to get a job done, and "fire" it for a better solution just as quickly. The classic
example: people don't want a drill, they want a hole in the wall (or more precisely, the
shelf that hole enables).

## JTBD statement template

```
When [situation/context], I want to [motivation/action], so I can [expected outcome].
```

Keep it free of product/feature names — a good JTBD statement should still make sense if
the product didn't exist yet.

## Forces of progress

Four forces act on every switching decision. Useful as interview probes and as a lens for
synthesizing "why now" moments in transcripts:

| Force | Question it answers | Example probe |
|-------|---------------------|----------------|
| Push | What's wrong with the current situation? | "What made the old way stop working?" |
| Pull | What's attractive about the new solution? | "What did you expect this to do for you?" |
| Anxiety | What's holding them back from switching? | "What almost stopped you from trying this?" |
| Habit | What keeps them attached to the old way? | "What do you miss about how you used to do it?" |

A switch happens when push + pull outweigh anxiety + habit. If adoption is stalling, check
which side of that equation is winning.

## Comparison matrix (for competitive/positioning research)

A compact way to synthesize how a product and its alternatives serve the same underlying
job. Fill this in from interview data, not assumptions:

| | Research questions | [Your product] | [Alternative 1] | [Alternative 2] |
|---|---|---|---|---|
| **Use case** | How do you do [task]? Show me. Walk me through it. | | | |
| **Alternatives** | What would you use instead if this didn't exist? What else did you consider? | | | |
| **Progress** | What are the limitations of your current solution? What challenges do you have when using it? | | | |
| **Value proposition** | What's the main benefit you get from this? Why would you choose it over alternatives? | | | |

## Job Stories (alternative format, good for feature scoping)

```
When [situation], I want to [motivation], so I can [expected outcome].
```

Same shape as the statement template, but written to sit directly next to a feature spec —
useful when handing requirements to engineering, since it keeps the "why" attached to the
"what."

## Workflow

1. **Clarify the question**: Is this about why users adopted/switched (comparison matrix),
   or what a specific segment is trying to accomplish (statement template + forces)?
2. **Interview with force-based probes** (see table above) rather than feature questions.
3. **Synthesize** raw quotes into JTBD statements — one per distinct job, not per participant.
4. **Validate statements are product-agnostic** — if removing the product name breaks the
   statement, it's still a feature request in disguise, not a job.
5. **Output** a statement set for positioning/roadmap discussions, or a comparison matrix
   for competitive research.

## Deliverables

- JTBD statement set (one per distinct job uncovered)
- Forces-of-progress breakdown per statement (what pushed, pulled, caused anxiety, kept habit)
- Comparison matrix against named alternatives
- Job Stories, when handing off to engineering alongside a feature spec

