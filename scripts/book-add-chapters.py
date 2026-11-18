#!/usr/bin/env python3
"""Add companion notes 101-104 and the extensions to the book. Idempotent."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
p = root / 'book' / 'ux-research-in-the-wild.html'
s = p.read_text(encoding='utf-8')
if 'id="c-legacy-ux"' in s:
    print('chapters already present'); raise SystemExit

def ul(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def steps(items): return '<ol class="step-list">' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'
def table(head, rows):
    h = ''.join('<th>%s</th>' % c for c in head)
    r = ''.join('<tr><th scope="row">%s</th>%s</tr>' % (row[0], ''.join('<td>%s</td>' % c for c in row[1:])) for row in rows)
    return '<div class="ct-wrap"><table class="compare-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, r)
def callout(label, text): return '<div class="callout"><p class="callout-label">%s</p><p>%s</p></div>' % (label, text)

def article(id_, title, sub, date, source, summary, body, remember):
    return '''
<!-- %s -->
<article class="article" id="%s">
  <div class="article-meta">
    <span class="article-tag companion">Companion</span>
    <span class="article-date">%s</span>
    <span class="article-source">%s</span>
  </div>
  <h3>%s</h3>
  <p class="article-subtitle">%s</p>
  <div class="summary-box">
    <strong>Summary</strong>
    %s
  </div>
  %s
  <div class="remember-box"><span>Remember</span>%s</div>
</article>
''' % (id_, id_, date, source, title, sub, summary, body, remember)

LI = 'https://www.linkedin.com/pulse/'
legacy = article('c-legacy-ux', 'Modernizing Legacy UX', 'Why feature parity is the trap', '2026',
  '<a href="%show-modernize-legacy-ux-without-breaking-everything-vitaly-friedman-msh1f/" target="_blank">Vitaly Friedman, “How to modernize legacy UX” ↗</a>' % LI.replace('pulse/','pulse/').replace('%s','') if False else '<a href="https://www.linkedin.com/pulse/how-modernize-legacy-ux-without-breaking-everything-vitaly-friedman-msh1f/" target="_blank">Vitaly Friedman, “How to modernize legacy UX” ↗</a>',
  'A legacy product is one that succeeded and no longer fits. Modernize when keeping it costs more than it returns, and aim at what should exist now, not at a copy of what exists. Start with a working group of legacy users and migrate one key workflow at a time.',
  '<p>Legacy software is not bad software. It is software that was right for its time and has drifted away from what people need now. The risk in replacing it is rarely the technology. It is rebuilding the old product in a new skin.</p>'
  '<h4>Why modernizations go wrong</h4>' +
  ul(['<strong>Late-found dependencies.</strong> Old systems hold rules nobody wrote down. They surface in the last month.',
      '<strong>The feature-parity trap.</strong> “It must do everything the old one did” rebuilds every past compromise.',
      '<strong>Innovation theatre.</strong> A new look and a launch event, with the same workflows underneath.',
      '<strong>A feature factory.</strong> The team ships a long list and never checks that any of it helps.',
      '<strong>Worn-down people.</strong> Multi-year projects burn out the team that knows the old system.',
      '<strong>Delivered too late.</strong> After several years the team ships what was needed one to three years ago.']) +
  '<p>Behind most of these sit unknown unknowns: things nobody knows they don’t know until the migration starts.</p>'
  '<h4>Modernize the product, not the interface</h4>'
  '<p>Ask “what should exist now?” before “what do we have to carry over?”. Start with a working group of people who use the legacy product every day. They know which parts are load-bearing and which are habit.</p>'
  '<h4>Five ways to migrate</h4>' +
  table(['Strategy', 'How it works', 'Main risk'], [
    ['Big bang', 'Everyone switches on one day.', 'All the surprises arrive at once, with no way back.'],
    ['Incremental', 'Replace the product piece by piece.', 'Two interfaces live side by side for a long time.'],
    ['Parallel', 'Old and new both run. People opt into the new one as a public beta.', 'Double the support and maintenance work.'],
    ['Incremental and parallel', 'Power users move first, once the new version matches the old on day one.', 'Power users are the hardest group to satisfy.'],
    ['Upgrade the old UI, then beta the new', 'Improve the legacy interface in place while a new one runs as a public beta.', 'Effort split across two builds.']]) +
  '<p>Whichever you pick, migrate <strong>slice by slice, by key workflow</strong>, not feature by feature. A slice a user can finish end to end teaches you more than a feature that is only part of a task. Pilot each slice with a small group first; early wins build the trust the later slices need.</p>' +
  callout('A number to leave out', 'Articles on this topic often repeat that 65–79% of modernizations fail. The source article gives no reference for the figure, so don’t quote it in a business case.') +
  callout('Calabro link', 'The build trap — counting what shipped instead of what changed for users — is the same failure at project scale. See <a href="#figma">Users Don’t Care About Your Figma File</a>. For measuring whether the new version works, see <a href="#c-tars">Measuring Feature Impact (TARS)</a>.'),
  'Modernize the product, not the screen. Parity is not a goal.')

stake = article('c-stakeholders', 'Interviewing Stakeholders and Mapping Incentives', 'Get raw material, then pitch to what each person is rewarded for', '2026',
  '<a href="https://medium.com/eightshapes-llc/the-delicate-art-of-interviewing-stakeholders-d6496443cbec" target="_blank">Dan Brown, EightShapes ↗</a> · <a href="https://abbycovert.com/writing/incentive-architecture/" target="_blank">Abby Covert, Incentive architecture ↗</a>',
  'A stakeholder interview gathers raw material, not requirements. Script it around the domain, the audience and the constraints. Then map what each person is rewarded for before you pitch anything, because evidence on a metric the decision-maker doesn’t care about doesn’t move them.',
  '<p>Research findings reach a decision only through people. Two habits make that path shorter: interviewing stakeholders well at the start, and knowing what each of them is rewarded for when you present.</p>'
  '<h4>The interview</h4>'
  '<p>Don’t ask stakeholders for requirements. You will get solutions, and they will be the first thing the stakeholder thought of. Ask for the raw material: what the project is for, who it serves and what limits it. Cover three areas:</p>' +
  ul(['<strong>Domain:</strong> what the business or product area is and what it is trying to do.',
      '<strong>Audience:</strong> who the stakeholder thinks the users are, and how they know.',
      '<strong>Constraints:</strong> technical, operational and political. The political ones decide more than people admit.']) +
  '<p>Questions that work:</p>' +
  ul(['“Describe the purpose of this project in your own words.”',
      '“What is the most important thing to get right?”',
      '“If you could ask users one question, what would it be?”',
      '“How will you judge whether this succeeded?”',
      'Question the labels. “Why do we call them power users?”',
      'Close with “What did I miss?”']) +
  '<h4>The incentive map</h4>'
  '<p>For yourself and for each stakeholder, write down what they are motivated by, which decisions they own, and whether their incentives line up with yours. People in different roles are usually rewarded for different things:</p>' +
  table(['Role', 'Typical incentive'], [
    ['Product', 'Short-term lift in a headline metric'],
    ['Engineering', 'Uptime and delivery speed'],
    ['Marketing', 'Brand health and campaign results'],
    ['Support', 'Fewer tickets']]) +
  '<p>Pitch on a measure the decider is rewarded for. A usability finding framed as “support tickets down” can reach a support lead who would not move for “better learnability”. If nothing lines up, you have three honest options: ask what would matter to them, find a stakeholder whose incentives do align, or shelve the idea for now.</p>' +
  callout('Calabro link', 'This is the working method behind <a href="#opt-in">The Opt-In Approach</a> and <a href="#seven-patterns">Seven Patterns That Derail Product Teams</a>. When the pushback is “our users are different”, the incentive map shows what the person is protecting; see <a href="#think-researcher">Think Like a Researcher</a>.'),
  'Interview for raw material. Pitch on what each person is rewarded for.')

crit = article('c-critiques', 'Running Design Critiques', 'Four kinds of meeting, and a 30-minute agenda that works', '2026',
  '<a href="https://uxdesign.cc/improving-design-critiques-0e4d075ead2f" target="_blank">Jeremy Bird, “Improving design critiques” ↗</a> · <a href="https://www.doc.cc/articles/form-factor-trap" target="_blank">Samsonov, “The form factor trap” ↗</a>',
  'Critiques turn into opinion fights when nobody agreed what kind of meeting it was. Name the type first. Then run a timed slot with silent written feedback before any discussion, so the loudest voice doesn’t set the room.',
  '<p>“Can you take a look?” can mean four different things. Each has different people in the room and a different rule for what happens to the feedback.</p>' +
  table(['Meeting', 'Purpose', 'What happens to feedback'], [
    ['Critique', 'Improve the craft of work in progress. Designers only.', 'Asked as questions, not instructions. The designer decides what to use.'],
    ['Design review', 'Check the work against goals and constraints. Cross-functional.', 'Each point is implemented or answered with a reason.'],
    ['Quality review', 'Keep patterns and components consistent. Led by a design lead.', 'Directive: fix it to match the system.'],
    ['Shareout', 'Show progress and business value.', 'None. It is one-way.']]) +
  '<h4>Set it up</h4>' +
  ul(['Four to six people. More and the quiet ones stop contributing.',
      'Rotate the roles: captain, facilitator, presenter, critics and note-taker.',
      'Sessions of 60–90 minutes in 30-minute slots. The presenter sends the topic 24–48 hours ahead, with the stage of the work and the feedback they want.']) +
  '<h4>The 30-minute slot</h4>' +
  table(['Minutes', 'Step'], [
    ['2', 'Background: the problem, the user, the constraint'],
    ['3', 'Walkthrough of the work'],
    ['2', 'Clarifying questions only. No opinions yet.'],
    ['7–10', '<strong>Silent written feedback</strong>'],
    ['10–13', 'Conversation'],
    ['3', 'Wrap-up: the presenter says what they will do next']]) +
  '<p>Silent writing is the step that matters most. It collects everyone’s view before one person anchors the room. In the conversation, hear from people in other disciplines first, then designers, then leads, so seniority doesn’t end the discussion early.</p>'
  '<h4>Questions that improve the work</h4>' +
  ul(['What is the main benefit for the user, and does this deliver it?',
      'What other ways would deliver the same benefit?',
      'Which decision are you least sure about?',
      'What happens when it goes wrong: empty, error, slow, no permission?']) +
  callout('The form factor trap', 'A polished mockup can hide decisions nobody has made. Match the fidelity of the work to how settled the idea is, and agree the user benefit before comparing features. If the team can’t name the benefit, that is a finding.') +
  callout('Calabro link', 'Findings that survive a critique are easier to present. See <a href="#debrief">Debriefs Reframed</a> for turning feedback into decisions.'),
  'Name the meeting type. Write first, talk second.')

hid = article('c-hidden-disabled', 'Hidden, Disabled or Read-Only?', 'A decision tree for limiting what people can do', '2026',
  '<a href="https://www.linkedin.com/pulse/decision-trees-ui-components-vitaly-friedman-chgae/" target="_blank">Vitaly Friedman, “Decision trees for UI components” ↗</a>',
  'Ask whether the feature should be limited at all. If this user can never use it, hide it. If a field is system-made or edited elsewhere, make it read-only and say where to edit. If it exists but can’t be used right now, disable it and say why.',
  '<p>Teams reach for a greyed-out control by habit. Hidden, disabled and read-only mean three different things to the person looking at the screen, and the choice is a product decision, not a styling one.</p>' +
  steps(['<strong>Should it be limited at all?</strong> A feature that is irrelevant, not allowed for this role or currently unavailable is a different problem in each case.',
         '<strong>Can this user never interact with it?</strong> Hide it. Still decide when it appears, how, and to whom, so the product doesn’t read as inconsistent between roles.',
         '<strong>Is it a value the system makes, or one edited elsewhere?</strong> Make it read-only. Add a hint where the value can be changed.',
         '<strong>Does it exist, but can’t be used right now?</strong> Disable it, and always explain why and what unlocks it: a missing permission, a missing prerequisite, a temporary state.']) +
  table(['State', 'Use when', 'Must include'], [
    ['Hidden', 'The user can never use it', 'A plan for when it does appear'],
    ['Read-only', 'The value is generated or edited elsewhere', 'A hint saying where to change it'],
    ['Disabled', 'It exists, but not for this user now', 'The reason, and what unlocks it']]) +
  '<h4>Accessibility</h4>'
  '<p>WCAG 2.2 AA doesn’t require contrast on disabled controls. People still need to read them. Keep the text legible and, ideally, focusable so a screen reader announces the reason. A disabled control that can’t take focus is invisible to keyboard users.</p>'
  '<h4>Don’t hide by default</h4>'
  '<p>Never hide buttons or filters just because they have no effect right now. People expect them to stay where they were. A button that vanishes teaches users to doubt the interface; a disabled one with a reason teaches them how it works.</p>' +
  callout('Related', 'Permission-based hiding turns into a status problem fast; see <a href="#status-design">Fixing Bad Status Design</a>. For the logic of picking the control itself, see <a href="#c-selection-controls">Choosing the Selection Control</a>.'),
  'Hide what is never theirs. Disable with a reason.')

new_chapters = legacy + stake + crit + hid
s = s.replace('\n<!-- Archive guide -->', new_chapters + '\n<!-- Archive guide -->', 1)

# TOC entries 101-104
toc = ''
for i, (id_, title, sub) in enumerate([
    ('c-legacy-ux', 'Modernizing Legacy UX', 'Why feature parity is the trap'),
    ('c-stakeholders', 'Interviewing Stakeholders and Mapping Incentives', 'Raw material first, then pitch to incentives'),
    ('c-critiques', 'Running Design Critiques', 'Four meeting types and a timed agenda'),
    ('c-hidden-disabled', 'Hidden, Disabled or Read-Only?', 'A decision tree for limiting what people can do')], start=101):
    toc += '    <a href="#%s" class="toc-entry"><span class="toc-entry-title">%s <span class="toc-new">New</span> <span class="toc-entry-sub">— %s</span></span><span class="toc-num">%d</span></a>\n' % (id_, title, sub, i)
m = re.search(r'(<a href="#c-ai-frameworks" class="toc-entry">.*?</a>\n)', s, re.S)
s = s[:m.end()] + toc + s[m.end():]

# Rules list
rules = ''.join('<li><a href="#%s">%s</a> <span class="rules-src">%s</span></li>' % (i, r, t) for i, r, t in [
    ('c-legacy-ux', 'Modernize the product, not the screen. Parity is not a goal.', 'Modernizing Legacy UX'),
    ('c-stakeholders', 'Interview for raw material. Pitch on what each person is rewarded for.', 'Interviewing Stakeholders and Mapping Incentives'),
    ('c-critiques', 'Name the meeting type. Write first, talk second.', 'Running Design Critiques'),
    ('c-hidden-disabled', 'Hide what is never theirs. Disable with a reason.', 'Hidden, Disabled or Read-Only?')])
anchor = '<span class="rules-src">Deciding How Much the AI Should Do</span></li>'
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + rules)

# counts
s = s.replace('91 chapters from Calabro, 9 companion notes from other sources', '91 chapters from Calabro, 13 companion notes from other sources')
s = s.replace('Part V adds 9 companion notes from other sources', 'Part V adds 13 companion notes from other sources')
s = s.replace('Erika Hall, Teresa Torres, Vitaly Friedman, Adrian Raudaschl,', 'Erika Hall, Teresa Torres, Vitaly Friedman, Dan Brown, Abby Covert, Jeremy Bird, Brittany Hobbs, WebAIM, Adrian Raudaschl,')

# extensions: a callout before the last remember-box (or end) of the target article
def extend(aid, html):
    global s
    a = s.index('id="%s"' % aid); e = s.index('</article>', a)
    seg = s[a:e]
    k = seg.rfind('<div class="remember-box">')
    pos = a + (k if k >= 0 else len(seg))
    s = s[:pos] + html + '\n  ' + s[pos:]

extend('ai-cant-do', '<h4>Guardrails when you do use AI for analysis <span class="toc-new">New</span></h4>' + ul([
    '<strong>Build disconfirmation into every prompt,</strong> and run a separate pass for edge cases and counter-evidence.',
    '<strong>Define what failure looks like.</strong> “If the transcript doesn’t support a code, return NULL and flag it” stops the model filling gaps.',
    '<strong>Pseudonymise participant data.</strong> Faces and voices still identify people. Check your plan’s data and training defaults at the source before you upload anything.',
    '<strong>Calibrate on about five transcripts</strong> against human coding before you scale up.']) + '<p class="note">Source: Brittany Hobbs, “A UX researcher’s guide to Claude tools” (Product Impact Pod).</p>')
extend('stats-llms', callout('A model change is an instrument change', 'Keep a few hand-coded transcripts as a regression set. Re-run them whenever the model changes, and record the model and the effort setting in your methods section. A result you can’t reproduce is an anecdote. <span class="note">(Brittany Hobbs, Product Impact Pod)</span>'))
extend('c-tables-bulk', '<h4>Added in this edition</h4>' + ul([
    '<strong>Tables have four jobs:</strong> find records, compare them, view or edit one row, and act on several. Design each on purpose.',
    '<strong>Screen readers:</strong> a caption is the table’s accessible name, header cells are announced with every data cell, and non-interactive cells should not take focus. The test: can a screen-reader user get what a sighted user gets at a glance?',
    '<strong>Toolbar commands need an enablement rule</strong> for zero, one and many selected rows.',
    '<strong>Bulk import:</strong> accept the file as it is, remember column mappings between sessions, suggest the nearest valid value, allow a partial import with a downloadable error report, and let people choose overwrite or skip for duplicates.',
    '<strong>The 5–20 item gap:</strong> too many for one form and too few for a spreadsheet. Extend the single form into a batch builder with one review step and one approval.']) + '<p class="note">Sources: Léonie Watson (tink.uk), Smashing Magazine, Flatfile, RazorpayX.</p>')
extend('c-dataviz', '<h4>Added in this edition</h4>' + ul([
    '<strong>Is a dashboard the right answer?</strong> Fewer than one in ten US adults aged 16–65 reach proficient numeracy, and single values are read far more easily than relationships or trends. For most users, an insight placed where the decision happens beats a chart to decode.',
    '<strong>Four trade-offs:</strong> screen space, number of pages, level of abstraction and amount of interaction. Reducing one stresses the others.',
    '<strong>Meta-information is part of the design:</strong> data source, description, last update, refresh cadence, disclaimers and annotations for events that explain a spike.',
    '<strong>Operational or analytical?</strong> Set defaults by role. Design the dashboard last, after the questions are known.']) + '<p class="note">Sources: Wagner, Zide and Zimmers; Bach et al., Dashboard Design Patterns (IEEE VIS 2023); Taras Bakusevych.</p>')
extend('status-design', '<h4>Degraded experiences <span class="toc-new">New</span></h4><p>Status design also covers the day a dependency fails. Decide in advance what the page does when an optional service is slow or down:</p>' + ul([
    'The page still renders. One failing panel never blanks the screen.',
    'Primary tasks stay available.',
    'Say what is missing, in place: “Recommendations are unavailable right now. Everything else works.”',
    'Never show stale numbers as current. Label the time of the last update.',
    'Recover without a reload.']) + '<p class="note">Source: Vitaly Friedman, decision trees for UI components.</p>')
extend('accessibility', '<h4>Where to spend the effort <span class="toc-new">New</span></h4>' + ul([
    'In the WebAIM screen reader survey (#9, 2021), about 68% of respondents navigate a long page by headings first. Landmarks are the first choice for about 3%.',
    'About 90% use a screen reader on a phone, so test on mobile as well as desktop.',
    'Run an audit in five layers: automated, keyboard, screen reader, visual and a full task flow.']) + '<p class="note">The survey is from 2021; check for a newer edition before quoting the figures.</p>')

p.write_text(s, encoding='utf-8')
print('added 4 chapters, 6 extensions')
