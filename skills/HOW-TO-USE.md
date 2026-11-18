# How to use the UX skills

Once installed, the skills need no setup. Claude reads each skill's short description and loads the full skill when your request matches it. You ask normally, and the right one kicks in.

## Install

- **claude.ai (web, desktop, mobile):** go to Settings → Skills → upload. Download one zip per skill from the app's **Library** screen or the [downloads folder](https://github.com/Olia-D/ux-practice/tree/main/downloads), and upload each zip separately. The skills then work in every chat, project and Claude Code session on that account.
- **Claude Code:** copy the skill folders into `~/.claude/skills/` (for every project) or `<repo>/.claude/skills/` (for one project). They load when the next session starts.

## Three ways to use them

1. **Just ask.** For example, "Review this checkout form", "Is 8 users enough for this test?" or "How should the agent confirm before sending an email?" These load `interaction-design-reviewer`, `ux-research-advisor` and `ai-ux-patterns` without you naming them.
2. **Start with `ux-start` when you're not sure.** For example, "Where do I start with the new segmentation feature?" or "The PM says users don't need onboarding." It picks the right skill or skills and runs a set sequence of steps (new feature, design review, stakeholder pushback, launch review, dashboard).
3. **Name one to force it.** Type `/ux-research-advisor` or "use interaction-design-reviewer". This helps when a request is borderline and you want a specific lens.

## What each one is for

| Skill | Reach for it when… |
|---|---|
| `ux-start` | The problem is vague, or it mixes research, design and copy |
| `interaction-design-reviewer` | You're working on forms, controls, navigation, statuses, tables, accessibility audits, destructive actions, or running a design critique |
| `ux-writing` | You need a button label, error, empty state, status or any product text, or you're setting voice and naming rules |
| `ai-ux-patterns` | You're designing any AI feature: how much the agent does on its own, where it sits in the UI, voice, how trust and citations work, chat history, the EU AI Act labelling rules |
| `ux-research-advisor` | You're planning a study, judging an A/B result, writing a survey, using AI in analysis, interviewing stakeholders, picking a metric, preparing a readout, arguing ROI, or setting up or reading Pendo analytics |
| `data-visualization` | You're choosing a chart, reviewing a dashboard or designing KPI views |
| `product-discovery` | You're deciding what to build next: setting an outcome, running weekly interviews, mapping an opportunity tree, testing assumptions, or questioning a roadmap |
| `jtbd-research` | You need to know why users adopt, switch or churn |

## Make routing reliable

- **Turn off overlapping skills.** Generic design skills (for example `design-critique`, `user-research` and `accessibility-review` from the Design plugin) have descriptions that overlap with these. When two skills overlap, the generic one sometimes fires instead. Turn them off in Settings → Skills. `ux-copy` overlaps with `ux-writing`, so keep only one of them.
- **Add the routing note to your projects.** Pasting [`PROJECT-INSTRUCTIONS.md`](PROJECT-INSTRUCTIONS.md) into a project's custom instructions (claude.ai) or `CLAUDE.md` (Claude Code) makes skill selection more reliable in that project.

## Keep the skills current

These folders are snapshots. If a skill changes in your account, download the new version and replace the folder. Then rebuild its zip so that `SKILL.md` sits at the root of the zip:

```
cd skills/<name> && zip -r ../../downloads/skill-<name>.zip .
```
