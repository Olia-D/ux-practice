---
name: "ai-ux-patterns"
description: "Design and review AI product interfaces — decide autonomy level and trust scaffold first (Agentic UX, T.R.U.S.T., C.O.N.V.E.R.S.E. frameworks), then apply patterns from Shape of AI, AI UX Patterns and AI UX Playground: prompting, tuning, human-in-the-loop, trust signals, memory, citations, agentic commerce. Use whenever the user is designing, speccing, or critiquing any AI-powered feature (chatbots, copilots, generative tools, agents, voice assistants, AI shopping) even if they don't say \"AI UX\" — e.g. \"how should the loading state work for this generation\", \"what happens when the agent wants to send an email\", \"how much should the agent do on its own\". Trigger with \"AI feature\", \"AI UX\", \"agent\", \"autonomy\", \"streaming response\", \"hallucination disclosure\", \"memory controls\", \"citations UI\", \"agent interface\", \"thread history\", \"chat history\", \"AI label\", \"EU AI Act\", \"AI disclosure\", \"where should the AI go\", \"AI side panel\", \"voice AI\", \"voice assistant\"."
---

# AI UX Patterns

A pattern library for designing and reviewing AI-powered product interfaces, combining three
public pattern libraries with decision frameworks and anti-patterns (credits under Sources).
Use this alongside general interaction
design principles — it fills the gaps that traditional HCI pattern libraries don't cover:
prompting, model behavior, human oversight of AI actions, and trust in generated content.

**Decide before you pick patterns.** The frameworks below settle *how much* autonomy and
*how much* trust scaffolding a feature needs. The pattern catalog then tells you *what* to
build. Skipping the decision step is how teams ship a confident agent with no undo.

Trigger this when a request involves an AI feature specifically — chat interfaces, copilots,
generative tools, agents, or any UI where the system is producing content or taking actions
on the user's behalf. For non-AI interface work (forms, dashboards, standard controls), use
general interaction design review instead.

## How to use

**REVIEW mode** — when auditing an existing AI feature: walk through the categories below
and check which patterns are present, missing, or misapplied. Flag gaps the same way as a
standard design review — issue, why it fails, alternative, evidence.

**CREATE mode** — when designing a new AI feature: use the categories as a checklist in
rough sequence (Wayfinders → Input modalities → Prompt actions → Tuners → Session & thread
management → Governors → Trust builders → Identifiers) to make sure onboarding, control,
and trust are all addressed, not just the core generation loop.

## Frameworks — decide first

### A. Agentic UX: how much authority should the agent have?

Autonomy is a product decision, not a model capability. **Grant the lowest level that
delivers the outcome.** When signals conflict, choose the lower level or split the workflow
so low-risk steps run and high-impact steps stay under review.

| Level | Agent / human | Must build | Breaks as |
|---|---|---|---|
| **L1 Suggest** | advises / you act | explain why, offer alternatives, free dismissal | one pushy recommendation; a suggestion that looks like a done action |
| **L2 Draft** | starts / you finish | mark as draft, everything editable, side effects blocked until publish | draft that auto-sends or edits durable records |
| **L3 Confirm** | proposes / you approve | preview exact impact, edit/deny/cancel, re-ask if plan changes | approval without impact preview; silent re-planning after "yes" |
| **L4 Bounded** | acts within your limits | hard limits (budget, scope, stop rules), escalate when unsure, one-click interrupt + rollback | soft limits the agent can ignore; exceptions that fail silently |
| **L5 Monitor** | runs / you watch | always-on status, anomaly alerts to a named owner, safe shutdown + re-authorisation | always-on agent with no visible status or owner |

**Score each action** on five factors to pick the level: impact (how bad if wrong),
reversibility (can it be undone), reliability (how proven at this task), sensitivity
(context), detection (will anyone catch a bad outcome). Reversibility and detectability set
the ceiling — hard-to-undo or hard-to-spot actions get lower autonomy even if the agent is
reliable. Wrong *actions* cost more than wrong *answers*.

*Pre-ship checks:* lowest level that still works? visible who decides/acts/monitors? side
effects blocked until the level allows? re-ask on plan change? one-click interrupt/deny?
hard limits real, not preferences? status unmistakable when autonomy rises? recovery after a
bad autonomous action?

### B. T.R.U.S.T.: how much evidence and control does this output need?

Trust is calibrated, not maximised — overtrust accepts wrong output, undertrust ignores
useful output. **Scaffold the moment of reliance.**

- **Truthful expectations** — label the AI's role (draft / recommendation / assisted result), describe capability in task terms, state what it does *not* do, disclose model or mode changes. *Breaks as:* vague "AI-powered", limits revealed only after someone acts on bad output.
- **Reasons & provenance** — claim-level citations with excerpt, "why this?" for recommendations, assumptions surfaced, freshness/coverage/conflict labels. Four depths: glance → inspect → investigate → audit. *Breaks as:* source list disconnected from claims.
- **Uncertainty & limits** — plain-language labels for estimated/conflicting evidence, alternatives when ambiguous, ranges over false precision, verification prompt before consequential use. *Breaks as:* an unexplained "78% confidence".
- **Safeguards & control** — the control ladder: inspect → adjust → correct → reject → override → escalate → revoke. Non-AI path, fine-grained feedback (inaccurate / stale / unsafe / misunderstood), undo + version history, visible human handoff. *Breaks as:* accept-only flows, buried handoff, no undo on durable changes.
- **Track record & repair** — output history, version/freshness status, outage disclosure, correction receipts, incident explanations. *Breaks as:* silent degradation, no confirmation after feedback.

| Situation | Minimum scaffold |
|---|---|
| Low-stakes creative draft | AI label, editability, simple feedback |
| Factual answer / research summary | claim-level citations, freshness, limitation note |
| Recommendation affecting a decision | reasons, criteria, assumptions, alternatives, rejection path |
| Prediction / forecast | uncertainty range, input basis, scenario comparison |
| High-impact decision support | evidence record, human review, override, escalation, audit |
| Autonomous or external action | all of the above + Agentic UX level |

### C. C.O.N.V.E.R.S.E.: is this chat turn complete?

For conversational products. Design the composer before the prompt — what users can
attach, select, constrain and revise sets the signal the model receives.

**C**ontext (can they see and change what the AI knows this turn?) · **O**nboarding (does a
first-timer know what to ask?) · **N**atural expression (intent in their own words/media, no
prompt engineering) · **V**isibility (waiting, streaming, failure states clear; stop control) ·
**E**vidence (can they judge what supports a claim?) · **R**efinement (fix one part without
restarting — regenerate is not the only fix) · **S**tructure (table/checklist/artifact when
the job needs it, not fluent prose) · **E**rror recovery (wrong, partial, failed → clear path).
*Prototype the hard moments:* vague prompt, large file, conflicting context, interrupted
stream, wrong answer, long thread.

### D. Agentic commerce (retail-relevant)

When an agent can search, choose and pay for a shopper: walk the purchase in order, one
decision per stage — discover (match reasons, editable constraints) → decide (fit check
blocks a bad buy) → authorise (one-charge approval showing merchant, items, reason; spending
limits with cap/merchants/expiry; single-use virtual card) → check out (seller named before
payment, totals visible) → track (activity log, one card per purchase) → return (agent-filed
claims the shopper approves first) → watch (price alerts stop at notification; watch-then-buy
rules show target, merchant, cap) → revoke (list of spending agents, a stop that blocks the
next charge). *Breaks as:* a charge showing amount but not the original ask; a price-drop
alert that buys on its own; a wallet removable only by deleting the account.

---

### E. Placement: where should the AI sit?

Decide placement from the user's primary task, not from what competitors ship.

| Placement | Use when | Avoid when |
|---|---|---|
| **Floating widget** | Bounded, reactive help on any page | The AI is the main job |
| **Inline overlay** | Small edits right inside the content | Long, multi-step work |
| **Right panel, on demand** | Expert help while deep in another task | Novices — they often miss it |
| **Left panel, co-creator** | Chat drives a live output beside it | Screen space is already tight |
| **Centre stage** | Prompting *is* the main job | AI is a helper to another task |
| **Infinite canvas** | Visual ideation, many parallel options | Linear, form-like tasks |
| **Grid / spreadsheet** | One query fills many cells or rows | Single answers |

A feature with no visible AI surface at all (it just acts in the workflow) still needs
the governors and trust builders below — invisible doesn't mean unaccountable.

---

## Table of contents

Jump straight to the relevant category instead of reading top to bottom:

- [1. Wayfinders](#1-wayfinders--helping-users-start-and-compose-well) — starting and composing a good prompt
- [2. Input & output modalities](#2-input--output-modalities) — text, image, voice in and out
- [3. Prompt actions](#3-prompt-actions--what-users-can-direct-the-ai-to-do) — the verbs available mid-flow
- [4. Tuners](#4-tuners--refining-what-the-ai-has-to-work-with) — controlling the inputs that shape output
- [5. Session & thread management](#5-session--thread-management) — navigating and resuming history
- [6. Governors](#6-governors--keeping-the-human-in-the-loop) — human oversight of AI actions
- [7. Result display](#7-result-display) — how generated results are presented
- [8. Trust builders](#8-trust-builders--signaling-that-output-is-safe-to-rely-on) — signaling reliability
- [9. Identifiers](#9-identifiers--giving-the-ai-a-distinct-recognizable-identity) — the AI's visual/brand identity

---

## 1. Wayfinders — helping users start and compose well

Solve the "blank canvas" problem, and help users write a prompt good enough to get a useful
result on the first try.

- **Initial CTA** — a large, open-ended input that invites the first interaction.
- **Suggestions** — example prompts shown near the input to seed ideas.
- **Templates** — structured, fillable starting points (by the user or pre-filled by the AI).
- **Structured prompt** — scaffold the input into explicit required fields rather than one
  open text box, when the task needs specific details to succeed.
- **Paginated prompt** — break a structured prompt into steps/pages to keep each one focused,
  for longer or more complex setup flows.
- **Cloze passage** — present prompt variables as fill-in-the-blank slots inside a natural
  sentence, rather than a form — useful for narrow, well-defined tasks.
- **Randomize** — a low-effort way to get a first result and learn the system by example.
- **Example gallery** — sample generations/prompts shown to educate and inspire.
- **Nudges** — contextual prompts pointing users toward an AI capability they haven't tried.
- **Inline help** — subtle, contextual help presented alongside the input itself, lighter
  weight than a full onboarding flow.
- **Prompt quality feedback** — a live indicator of how complete/detailed the current prompt
  is, so users learn to write better prompts instead of guessing why a result was weak.
- **Prompt details** — surfacing what's actually being sent to the model (system prompt,
  context, attachments) so users understand what's shaping the response.
- **Follow-up** — the AI asks a clarifying question when the initial prompt is ambiguous,
  instead of guessing and producing a low-quality result.

*Design risk if skipped:* users stare at an empty input and bounce, or write vague prompts,
get a bad first result, and blame the product rather than realizing the prompt was the issue.

## 2. Input & output modalities

What form the user's input — and the AI's answer — takes, beyond typed text.

- **Raw text input** — the default: direct typed prompting.
- **Image input** — an image attached alongside a supporting text prompt.
- **Voice input** — spoken input as a more natural alternative to typing.

*Design risk if skipped:* forcing every input through text excludes tasks (and users) that
are a much better fit for a different modality — describing a photo in words is much
higher-effort than just attaching it.

**Voice in and out — rules that typed chat doesn't need:**
- **Confirm key values back** (dates, names, amounts) in the next turn — listeners can't
  scroll back. Confirm high-risk actions explicitly, simple ones implicitly.
- **Switch channel for anything people would write down** — send it by text or email.
- **Voice can't carry tables or code.** Plan the hand-off to a screen.
- **Push-to-talk** for noisy places or long prompts; **voice activity detection** for hands-free.
- **Signal the state** — listening, thinking, speaking — and make turn-taking unmistakable.
- **Be brief, say what it can do with examples,** accept follow-ups and pronouns, never
  blame the user for a misheard request.
- **Full-screen voice mode hides the thread** — keep an inline option and a transcript.
- **Never imply it's human.** Outbound calls identify themselves and earn permission first.
  Keep the persona steady, including when delivering bad news.
- **Meeting bots:** decide active / passive / invisible, whether notes auto-share or wait for
  approval, and mark AI-written text with links back to the transcript moment.
- **Audio consent:** voice consent with scope and deletion; transcripts and playback speed
  for accessibility.

## 3. Prompt actions — what users can direct the AI to do

The verbs available once a user is already in a flow with content on the page.

- **Open input** — free-text conversational prompting.
- **Inline action** — invoke AI contextually on content already on the page (select text → act).
- **Auto-fill** — extend one prompt across multiple fields/inputs at once.
- **Chained action** — sequence multiple AI steps as one user-facing action.
- **Editing assistance** — AI helps revise the user's own prompt before it's submitted,
  distinct from a full prompt enhancer that rewrites it automatically.
- **Restructure / Transform** — use existing content as a starting point, or change its
  modality (text → image, doc → slides, etc.).
- **Expand / Summary / Synthesis** — lengthen, distill, or reorganize content.
- **Regenerate (full)** — re-run the same prompt for a completely new attempt.
- **Partial regeneration / Inpainting** — target a specific region or section of a result to
  regenerate, rather than the whole thing.
- **Describe** — break a result down into the tokens/parameters that produced it.
- **Madlibs** — repeat a generative task at scale while holding format constant.

*Design risk if skipped:* every correction requires a full new prompt from scratch — users
regenerate whole results to fix one small part, which is slow and erodes trust in precision.

## 4. Tuners — refining what the AI has to work with

Give users control over the inputs that shape the output, not just the output itself.

- **Attachments / Reference material** — give the AI a concrete reference (file, image, doc)
  to anchor and scope its response.
- **Connectors** — let the AI pull in external data/context (calendar, CRM, docs).
- **Filters** — constrain inputs or outputs by source, type, or modality.
- **Parameters** — explicit constraints attached to a prompt (length, tone, format).
- **Configurable controls** — a highly abstracted, UI-driven way to compose a prompt through
  settings rather than free text, for users who shouldn't need to write prompts at all.
- **Modes** — swap the underlying persona/constraints for a specific context of use.
- **Model management / Model selection** — let users choose which underlying model handles
  their prompt.
- **Generation tokens** — an explicit, visible compute/length budget the user can spend on
  a generation — more concrete than a generic cost estimate.
- **Preset / saved styles / Prompt templates** — reusable style or prompt presets, either
  provided by the product or defined and saved by the user.
- **Voice and tone** — consistent alignment of output to a defined brand or personal voice.
- **Prompt enhancer** — the system automatically rewrites/improves a user's raw prompt before
  running it.
- **Tool switching in composer** — change search / reasoning / image / effort mode without
  losing the draft; show model and effort *before* send when cost or quality varies.
- **Context chip management** — files, @mentions, connectors shown as dismissible chips so
  the user sees what the next turn will use. Hidden context causes surprise; too many chips
  cause clutter.
- **Slash commands** — structured intents reachable from the input, lighter than a settings maze.

*Design risk if skipped:* users get generic output and have no lever to make it theirs —
they either accept mediocre results or abandon the tool for one with more control.

## 5. Session & thread management

How users navigate and return to their history of AI interactions — often overlooked because
it's information architecture rather than a moment inside a single generation.

- **Thread options** — let users choose whether a new prompt continues the current thread
  (with context) or starts fresh (without it).
- **Thread history** — a browsable record of past threads/sessions the user can return to.

**Three-layer model.** A transcript is a record,
not a history. Design three connected layers, each with its own job:

1. **Task history** — one thread per distinct goal (a self-contained request with a finish
   point); refinements stay inside it; users can rename threads in their own words. When a
   real shift is detected, *suggest* a new task in user terms ("so each request's progress
   stays separate"), never in terms of tokens, and let them decline. Long-running work gets
   its own background instance listed by state: needs clarification · in progress · ready
   for review · completed · failed.
2. **Interaction history** — separate events from results. The instruction and the final
   output matter most; tool activity matters when it fails. Mark milestones at real changes
   of direction, collapse old exchanges into items that name their content ("Completed
   analysis with 4 flagged changes", not "Updated response"), keep warnings and open
   questions visible, and show which files/data/earlier tasks informed the response.
3. **Output workspace** — anything long, editable, versioned, exported or reused lives in a
   persistent panel beside the conversation, current version obvious, earlier ones comparable.

*Test it* with a pre-populated history: return to a task from days ago; find the final output
after several revisions; say which sources informed an answer; start an unrelated task without
contaminating the current one; find the task waiting for review; explain what context the
system is using now.

*Design risk if skipped:* users lose valuable past work, can't resume an interrupted task,
or unintentionally carry irrelevant context into a new, unrelated prompt.

## 6. Governors — keeping the human in the loop

The most important category for anything AI-agentic: control, visibility, and reversibility
before/while/after the AI acts.

- **Action plan** — show the steps the AI will take *before* executing, for approval.
- **AI agent initial command** — for agents specifically, a clear, explicit starting
  instruction/scope the agent is bound to, stated up front rather than inferred.
- **Sample response** — confirm intent on complex/ambiguous prompts before committing compute.
- **Cost estimates** — surface compute/time/dollar cost before a user commits to an action.
- **Draft mode** — cheap, fast iterations before a final, expensive generation.
- **Controls** — pause or adjust a request mid-stream rather than only before/after.
- **Stream of thought** — expose the AI's reasoning, tool calls, and intermediate decisions.
- **Shared vision** — live visibility into AI actions happening in a shared canvas/workspace.
- **Branches** — support non-linear iteration while keeping a visible path back to origin.
- **Result variations / options** — show multiple candidate results side by side, with
  relevant actions attached to each, rather than one result at a time.
- **References** — show and let users manage what sources the AI is drawing on.
- **Citations** — inline attribution tying claims in the output to their sources.
- **Verification / Agent action review & confirm** — require explicit user confirmation
  before an AI action takes effect, especially for anything destructive or hard to reverse;
  for agents, this means reviewing the agent's understanding before it proceeds.
- **Memory** — let users see and control what the AI remembers about them across sessions.
  Keep *declared* instructions and *learned* memories on separate surfaces; every item
  viewable, editable, deletable; **pause** (stop learning, keep profile) distinct from
  **reset**. Style presets are not memory. Edit/delete rate is the trust signal.
- **Granular consent** — per-capability permissions with scope, expiry, revoke and drift
  notice, not one app-level toggle.
- **Autonomy budgets / hard budget ceilings** — time- or action-bounded unattended runs with
  enforceable spend caps; running meters (tokens, cost, quota) visible during execution.
- **Per-action autonomy / Suggest–Confirm–Execute** — autonomy scoped per capability; three
  modes the user can set per action type.
- **Checkpoints & restore** — named snapshots with one-click rollback before an agent run.
- **Interrupt & resume** — stop mid-response with a single gesture and continue with context
  intact; lost prompts after failure are a defect.
- **Smart diff** — highlight exactly what the model changed so review is a diff, not a reread.
- **Sandbox preview / blast-radius view** — show what a proposed action will touch before it runs.
- **Role card: "Trusted for / Will not do"** — state the agent's remit in two short lists
  where the user sets it up. "Will not do" is the part people read.
- **Stop & take over** — a persistent control to halt and continue manually from the same state.
- **Intervention inbox** — one place listing everything waiting for human approval across
  agents, instead of approvals scattered through threads.
- **Forget what you learned** — let users remove a learned preference or reset personalisation.

*Design risk if skipped:* users can't tell what the AI is about to do, can't stop it
mid-action, and can't undo it after — the exact conditions that make AI features feel
unsafe to rely on for anything consequential. This risk compounds for agents, where actions
may have real-world side effects outside the product itself.

## 7. Result display

How generated results are presented — easy to default to "a block of text" when the content
warrants a more structured view.

- **Result rendered preview** — a live, rendered preview of generated content (code, image,
  document) instead of raw output, so users evaluate the actual artifact, not its source form.
- **Timeline display** — present results chronologically when time/sequence is the relevant
  structure (e.g. a generated project plan or history).
- **Object-oriented display** — present results grouped by their object/category to expose
  hierarchical structure, when a flat list would bury relationships between results.
- **Skeleton loader + processing-time estimate** — show the shape of what's coming and an
  expected wait; a spinner alone is a vague state.
- **Variation grid** — side-by-side candidates to pick from, with actions attached to each.
- **Response refinement chips** — "more concise", "more formal", "retry this part" on the
  result, so correction is cheaper than a new prompt.

*Design risk if skipped:* users have to mentally render or reorganize AI output themselves,
which is exactly the kind of work the AI was supposed to remove.

## 8. Trust builders — signaling that output is safe to rely on

- **Disclosure** — clearly mark AI-generated or AI-guided content as such, not blended in
  silently with human-authored content. In the EU this is now law, not a nicety — see
  *Legal floor* below.
- **Caveat** — proactively surface known model shortcomings or risk areas (not just a
  generic disclaimer buried in terms of service).
- **Footprints** — let users trace a result back through the steps that produced it.
- **Consent** — only use a person's data/likeness/content with their knowledge and permission.
- **Data ownership** — give users control over how their data is stored and reused by the model.
- **Incognito mode** — allow AI interaction that doesn't get added to persistent memory.
- **Watermark** — machine- and human-readable marking on AI-generated content.
- **Failure disclosure** — say plainly when the system can't answer or a tool failed, instead
  of a confident guess; pair with a repair path.
- **Confidence indicators** — only with what the number means and what to do next; never as a
  substitute for sources.
- **Wrong-source feedback** — a specific "this source is wrong/irrelevant" control, not a bare
  thumbs-down. Citation depth: inline chip → claim preview with excerpt → full source list.
  Chips that open nothing are decoration.
- **Capabilities & limits before use** — say what it can't do before the first prompt, not
  after the first failure.
- **Counterfactual explanation** — "you'd have been approved if X were Y": explain a decision
  by what would have changed it.
- **Decision testing** — let people try different inputs and see how the outcome changes.
- **Consent-usage timeline** — show when and how the data someone consented to was used.

*Design risk if skipped:* users can't distinguish AI output from human output, can't tell
when to double-check a claim, and have no way to audit how a result was produced — all of
which erode trust faster in AI features than in traditional software, because the failure
modes (confident wrong answers) are less visible than a broken button.

### Legal floor: EU AI Act Article 50 (in force since 2 August 2026)

Applies whenever AI output reaches people in the EU, whatever the risk class. Fines up to
€15M or 3% of global turnover. Practical detail: Commission guidelines on transparency
(20 July 2026) and the Code of Practice on marking and labelling AI-generated content.

| Obligation | Who | UX consequence |
|---|---|---|
| Tell people they're interacting with AI, unless obvious from context | Provider | Chatbots and agents identify as AI at the start of the interaction — in text, not only an avatar or sparkle |
| Mark synthetic audio/image/video/text in a machine-readable, detectable format | Provider (deployer shares) | Watermark/metadata must survive download and sharing. **Grace period:** generative systems already on the market before 2 Aug 2026 have until **2 Dec 2026** |
| Disclose deepfakes (realistic content of real people, places, events) | Deployer | Visible label on the asset itself |
| Disclose AI-generated text published on matters of public interest, unless human-reviewed with a named responsible editor | Deployer | Product claims touching health, finance, safety, environment count. A skim isn't review |
| Inform people exposed to emotion recognition or biometric categorisation | Deployer | Notice before or at exposure, plus GDPR basis |

**Usually exempt:** spellcheck/grammar/translation/cropping-level assistance, clearly
non-realistic imagery, substantively human-edited text with a named editor.
**Counts as generation:** summaries, composites, substantive rewrites, adding/removing
elements in photos.

**What a compliant label looks like:** visible, persistent, accessible plain text (plus the
EU icon — variants: AI · fully AI-generated · partially AI-modified). **Non-compliant:** a
faint icon alone, a footer note, a label that flashes and disappears, a sparkle with no text.
Carbon's AI label (inline label → icon → explainability panel) is a production-ready model.

Disclosure is the floor, not the trust work: provenance, citations and visible context
(sections 5 and 8) are what make output checkable. In reviews, flag a missing or
non-compliant disclosure as a **compliance** issue, separate from UX severity. Not legal
advice — confirm scope with legal for B2B-only or non-EU products.

## 9. Identifiers — giving the AI a distinct, recognizable identity

- **Avatar** — a visual identifier for the AI itself.
- **Color** — a consistent visual cue marking AI-powered surfaces or content.
- **Iconography** — a consistent icon vocabulary for AI-powered actions.
- **Name** — how the AI is referred to across the product and customer experience.
- **Personality** — the characteristics that make the AI's voice distinct and on-brand.

*Design risk if skipped:* AI features feel bolted-on rather than native to the product,
and users can't build a consistent mental model of what the AI is or does across surfaces.

---

## Evaluating AI features — what not to delegate to AI

- **No synthetic users** for evaluation. They sound human and confirm what you believe; they
  can't get confused, invent a workaround or surprise you. Test AI features with real people.
- **Write the research questions yourself** — neutral-prompt habits strip the context a good
  question needs.
- **Don't trust AI-run interaction models** — correcting ChatGPT's GOMS-KLM analysis took
  about 6× longer than doing it by hand.
- **Choose the statistics yourself** — running code isn't choosing a test; accuracy rose from
  about a third to 90%+ only with expert prompts.
- **Interpret against the decision** — a significant result says groups differ, not which or
  whether it matters.

Hand evaluation planning to `ux-research-advisor`.

## Output format for reviews

```
Category: [Wayfinders / Input modalities / Prompt actions / Tuners / Session & thread
           management / Governors / Result display / Trust builders / Identifiers]
Pattern: [Name]
Status: [Present / Missing / Misapplied]
Why it matters here: [Tied to the specific AI feature and what users need from it]
Recommendation: [Specific, implementable]
```

Open every review by stating the **Agentic UX level** the feature is operating at (and
whether it should), and the **T.R.U.S.T. scaffold** its situation requires. Then list
pattern findings. For each issue name the "breaks as" failure in concrete terms (what the
user sees go wrong), not just the missing pattern.

End with a short priority list — governors and trust builders first for anything agentic
or consequential; wayfinders and input modalities first for anything new-user-facing.

**Invest / skip rules from the guides** (use when the question is "should we build this
at all?"):
- *Composer chrome:* add when modes change retrieval or spend, attachments/voice are common
  first intents, or a wrong model choice is expensive. Keep minimal when it's plain chat or
  extra controls hurt mobile send rate.
- *Memory:* invest when users return across sessions for the same long-running work and
  every stored item can be shown/edited/deleted. Stay light for one-off sessions, shared
  devices or regulated data.
- *Citations:* invest when answers are web/tool-grounded or users act on numbers, policies,
  medical/financial claims. Skip when the task is purely generative — faking sources is worse
  than none.
- *Onboarding:* activate in context when AI lives inside existing work; use a short wizard
  only for answers that change the first output; no paywall before a first real success.
  Define one first-success moment and measure time to it.

## Sources

Placement patterns and voice patterns: Sharang Sharma (UX Collective, 2026); Voice
Principles (Ben Sauer); IBM conversational persona guidance. Governor and trust additions:
IF Data Patterns catalogue; Dustin Kirk, Agentic UX Patterns. Chat-history layers and the
"what AI can't do" list: Trevor Calabro, *UX Research in the
Wild* (The Rules of AI Chat History, Jun 2026; 5 Things AI Still Can't Do for UX Research,
Oct 2026). Legal floor: Regulation (EU) 2024/1689 Art. 50; Commission transparency
guidelines (20 Jul 2026); AI Omnibus grace period for marking (to 2 Dec 2026).

Pattern taxonomy combines [The Shape of AI](https://www.shapeof.ai) by Emily Campbell
(CC-BY-NC-SA) and [AI UX Patterns](https://www.aiuxpatterns.com) by Luke Bennis. Frameworks
(Agentic UX, T.R.U.S.T., C.O.N.V.E.R.S.E., Agentic shopping), anti-patterns and the
invest/skip guides come from [AI UX Playground](https://aiuxplayground.com) (Bestfolios) —
see its teardowns for how ChatGPT, Claude, Perplexity, Gemini, Notion AI, Lovable and Manus
actually ship these. All three are actively growing — check periodically.