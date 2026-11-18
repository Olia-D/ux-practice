#!/usr/bin/env python3
"""Add the product-craft chapters (Part VI, chapters 111-120) after the discovery chapters. Idempotent.
Run after book-add-part6.py; re-run book-progress.py afterwards."""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from bookfig import rows, flow, compare, matrix, scale

root = pathlib.Path(__file__).resolve().parent.parent
p = root / 'book' / 'ux-in-the-real-world.html'
s = p.read_text(encoding='utf-8')
if 'id="p-hierarchy"' in s:
    print('craft chapters already present'); raise SystemExit
assert 'id="d-strategy"' in s, 'run book-add-part6.py first'

def ul(items): return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
def steps(items): return '<ol class="step-list">' + ''.join('<li>%s</li>' % i for i in items) + '</ol>'
def table(head, rws):
    h = ''.join('<th>%s</th>' % c for c in head)
    r = ''.join('<tr><th scope="row">%s</th>%s</tr>' % (row[0], ''.join('<td>%s</td>' % c for c in row[1:])) for row in rws)
    return '<div class="ct-wrap"><table class="compare-table"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, r)
def callout(label, text): return '<div class="callout"><p class="callout-label">%s</p><p>%s</p></div>' % (label, text)
def link(url, label): return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)
def see(*ids): return '<p class="note">See also: %s.</p>' % ', '.join('<a href="#%s">%s</a>' % (i, t) for i, t in ids)
def sources(*items): return '<p class="note">Sources: %s.</p>' % ' · '.join(items)

def article(id_, title, sub, source, summary, body, remember):
    return '''
<!-- %s -->
<article class="article" id="%s">
  <div class="article-meta">
    <span class="article-tag companion">Craft</span>
    <span class="article-date">2026</span>
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
''' % (id_, id_, source, title, sub, summary, body, remember)

RUI = 'https://cdn.jsdelivr.net/npm/claude-code-skills@0.5.0/data/skills/ux-ui-design-system/references/refactoring-ui.md'
SRC = {
  'rui': link(RUI, 'Adam Wathan and Steve Schoger, <em>Refactoring UI</em> (digest)'),
  'butt': link('https://practicaltypography.com/summary-of-key-rules.html', 'Matthew Butterick, <em>Practical Typography</em> (free)'),
  'wcag11': link('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2, 1.4.11 Non-text Contrast'),
  'wcag1': link('https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html', 'WCAG 2.2, 1.4.1 Use of Color'),
  'khol': link('https://shop.smashingmagazine.com/printed-books/design-systems/', 'Alla Kholmatova, <em>Design Systems</em> (2017)'),
  'atom2': link('https://atomicdesign.bradfrost.com/chapter-2/', 'Brad Frost, <em>Atomic Design</em>, ch. 2 (free)'),
  'atom5': link('https://atomicdesign.bradfrost.com/chapter-5/', 'Brad Frost, <em>Atomic Design</em>, ch. 5 (free)'),
  'eight': link('https://eightshapes.com/articles/team-models-for-scaling-a-design-system', 'Nathan Curtis, “Team models for scaling a design system”'),
  'covert': link('https://abbycovert.com/make-sense/', 'Abby Covert, <em>How to Make Sense of Any Mess</em> (free)'),
  'marquis': link('https://alistapart.com/article/everyday-information-architecture-excerpt/', 'Lisa Maria Marquis, <em>Everyday Information Architecture</em> (excerpt)'),
  'nncs': link('https://www.nngroup.com/articles/card-sorting-definition/', 'NN/g, “Card sorting”'),
  'nnct': link('https://nngroup.com/articles/card-sorting-tree-testing-differences', 'NN/g, “Card sorting vs tree testing”'),
  'nntt': link('https://nngroup.com/articles/interpreting-tree-test-results/', 'NN/g, “Interpreting tree test results”'),
  'gcd': link('https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design', 'GOV.UK, “Understand content design”'),
  'gun': link('https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/', 'GOV.UK, “Identify user needs”'),
  'rg': link('https://contentdesign.london/case-studies/readability-guidelines', 'Content Design London, <em>Readability Guidelines</em>'),
  'hoob1': link('https://uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php', 'Steven Hoober, “How do users really hold mobile devices?”'),
  'hoob2': link('https://uxmatters.com/mt/archives/2013/11/design-for-fingers-and-thumbs-instead-of-touch.php', 'Steven Hoober, “Design for fingers and thumbs”'),
  'houde': link('https://creativetech.mat.ucsb.edu/readings/Prototypes_prototype.pdf', 'Stephanie Houde and Charles Hill, “What do prototypes prototype?” (1997)'),
  'gv': link('https://gv.com/sprint', 'GV, “The Design Sprint”'),
  'rsb': link('https://kromatic.com/real-startup-book/4-evaluative-product-experiments/', '<em>The Real Startup Book</em> (free)'),
  'figma': link('https://www.figma.com/reports/guide-to-handoff/', 'Figma, “Guide to handoff”'),
  'game': link('https://www.oreilly.com/library/view/gamestorming-2-0/9781098148072/ch10.html', 'Dave Gray and Sunni Brown, <em>Gamestorming 2.0</em> (2025), ch. 10'),
  'dsk': link('https://medium.com/google-design/expanding-the-design-sprint-methodology-with-an-open-source-toolkit-ac9147e36f48', 'Google, open-source Design Sprint Kit'),
}
CH = []

# 7 Visual hierarchy -----------------------------------------------------------
CH.append(article('p-hierarchy', 'Visual Hierarchy and Spacing', 'Decide what matters before you decide how it looks', link(RUI, 'Refactoring UI ↗'),
  'Every screen has three levels of emphasis: one primary thing, supporting content, and quiet metadata. Build the levels with weight and colour before size. Space from a fixed scale, start with too much, and use the squint test to check that groups read as groups.',
  '<p>When everything is bold, nothing is. Most cluttered screens don’t have too much content; they have too many things asking to be looked at first.</p>'
  '<h4>Three levels of emphasis</h4>' +
  table(['Level', 'What it holds', 'How to show it'], [
    ['Primary', 'The main action or information. One per view.', 'Darkest colour, heaviest weight, filled button'],
    ['Secondary', 'Supporting information people read', 'Regular weight, body colour, outlined or subtle button'],
    ['Tertiary', 'Metadata, hints, timestamps', 'Lighter grey, smaller or lighter weight, text-only button']]) +
  ul(['<strong>Weight and colour before size.</strong> A label in lighter grey steps back without shrinking until it’s hard to read.',
      '<strong>Visual emphasis and HTML structure are separate decisions.</strong> An <code>h2</code> doesn’t have to be big; a key number doesn’t have to be a heading.',
      '<strong>One filled primary button per view.</strong> Secondary actions are outlined or subtle, tertiary actions are text.']) +
  scale('A spacing scale', [4, 8, 12, 16, 24, 32, 48, 64, 96], 'Pick from the scale instead of nudging by eye. Gaps between values grow as the values grow, so choices stay distinct.', note='Base unit 4 or 8 px. Form defaults: 4 input→help, 8 label→input, 24 between groups') +
  '<h4>Space on purpose</h4>' +
  ul(['<strong>Start with too much whitespace,</strong> then remove it until it feels right. Adding space to a cramped layout rarely works.',
      '<strong>Squint test:</strong> blur your eyes. Related items should merge into one shape and separate groups should stay apart.',
      '<strong>Match density to the job.</strong> Dashboards and data tables can be dense; onboarding and marketing pages need room.',
      '<strong>Space between groups must be larger than space inside them.</strong> Otherwise the label sits as close to the wrong field as to its own.']) +
  callout('Borders last', 'Before adding a border, try a background change, a little more space or a shadow. Borders add lines to scan; spacing groups things without adding anything.') +
  see(('id-basics', 'Reframing Interaction Design Basics'), ('p-type', 'Type That Reads'), ('p-colour', 'Colour With a Job')) +
  sources(SRC['rui']),
  'One primary thing per view. Group by spacing before you reach for a border.'))

# 8 Type -------------------------------------------------------------------------
CH.append(article('p-type', 'Type That Reads', 'Size, line spacing and line length do most of the work', link('https://practicaltypography.com/summary-of-key-rules.html', 'Practical Typography ↗'),
  'Body text decides how a page reads, because there is more of it than anything else. On screen, set body text at 15–25 px, line spacing at 120–145% of the size, and lines of 45–90 characters. Use few sizes and weights, and keep emphasis rare.',
  '<p>Headlines get the attention in design reviews, but readers spend their time in body text. Four choices shape it: size, line spacing, line length and the font.</p>' +
  rows('Four numbers for body text', [
    ('Size', '15–25 px on screen; product UI body rarely below 16 px'),
    ('Line spacing', '120–145% of the size; headings tighter, about 1.2'),
    ('Line length', '45–90 characters a line, spaces included'),
    ('Paragraph space', 'Space between paragraphs or a first-line indent, never both')],
    'Wrong line length is the most common fault on wide screens: the eye loses its place on the way back to the next line.') +
  '<h4>A small, deliberate scale</h4>' +
  ul(['<strong>Use a type scale,</strong> for example 12, 14, 16, 18, 20, 24, 30, 36, 48 px, and two or three sizes per component.',
      '<strong>Weights with a job:</strong> regular for body, medium for labels, semibold for buttons and subheadings, bold for headings. Skip very thin weights in UI.',
      '<strong>Tighten large headings slightly</strong> and add 5–12% letter spacing to all-caps text.',
      '<strong>Bold or italic, sparingly and not together.</strong> Underline only links.',
      '<strong>All caps only for less than a line,</strong> and centred text sparingly.']) +
  '<h4>Small things readers notice</h4>' +
  ul(['Curly quotes and real apostrophes, not straight ones.', 'One space between sentences.', 'A proper dash, not two hyphens.', 'Kerning always on.']) +
  callout('In product UI', 'Reading rules come from long text. Interface text is scanned: front-load the words that matter and keep labels short. The reading rules still hold for help pages, empty states and anything longer than two lines.') +
  see(('p-hierarchy', 'Visual Hierarchy and Spacing'), ('content-structure', 'Content Beyond Readability')) +
  sources(SRC['butt'], SRC['rui']),
  '45 to 90 characters a line, 120 to 145% line spacing, and one emphasis at a time.'))

# 9 Colour -------------------------------------------------------------------------
CH.append(article('p-colour', 'Colour With a Job', 'Neutrals for content, colour for meaning', link(RUI, 'Refactoring UI, WCAG ↗'),
  'Most of an interface should be neutral. Keep saturated colour for actions, links and status, so colour carries meaning when it appears. Build scales, not single swatches, and never let colour be the only signal: text needs 4.5:1 contrast, and controls and meaningful graphics need 3:1.',
  '<p>A palette is not five brand colours. It’s a set of scales with roles, so that every colour on the screen answers the question “what does this mean?”.</p>' +
  rows('Colour roles', [
    ('Neutrals', '9 or more greys for text, borders and backgrounds; tinted slightly warm or cool'),
    ('Primary', '5–7 shades of one colour for actions, links and selection'),
    ('Status', 'Success, warning, error, info, always paired with text or an icon'),
    ('Accent', 'Optional; used rarely, so it stays noticeable')],
    'Saturated colour on everything turns into noise. On a mostly neutral screen, one colour is enough to show what to do next.', hi=1) +
  '<h4>Contrast and colour blindness</h4>' +
  table(['What', 'Minimum', 'Rule'], [
    ['Body text', '4.5:1', 'WCAG 1.4.3'],
    ['Controls and their states, meaningful graphics', '3:1 against what’s next to them', 'WCAG 1.4.11'],
    ['Information shown by colour', 'Never colour alone: add text, a shape or an icon', 'WCAG 1.4.1'],
    ['Links inside text', 'Underline, or 3:1 against the surrounding text', 'WCAG 1.4.1']]) +
  ul(['<strong>A red border alone doesn’t mark an error.</strong> Add a message and an icon.',
      '<strong>Green for valid, red for invalid still needs another cue.</strong>',
      '<strong>Check charts in greyscale.</strong> If series can’t be told apart, add labels or patterns.']) +
  callout('Greys with character', 'Pure grey looks dead next to colour. Tint greys slightly towards the brand hue, and make secondary text a grey from the scale rather than a lower opacity, which shifts on coloured backgrounds.') +
  see(('accessibility-first', 'Accessibility First, Not Last'), ('chart-types', 'Choosing the Right Chart Type'), ('p-hierarchy', 'Visual Hierarchy and Spacing')) +
  sources(SRC['rui'], SRC['wcag11'], SRC['wcag1']),
  'Neutral by default. Colour means something, and never says it alone.'))

# 10 Design systems ---------------------------------------------------------------
CH.append(article('p-systems', 'Design Systems That Last', 'Patterns, a shared language, and a team that owns them', link('https://atomicdesign.bradfrost.com/chapter-5/', 'Kholmatova, Frost, Curtis ↗'),
  'A design system is the patterns, the shared language that names them, and the practices that keep them alive. Build from small parts up to real pages, run it as a funded product with a governance process, and pick a team model that fits your organisation. Neglect kills more systems than bad components.',
  '<p>A component library is a part of a design system, not the whole thing. The system also includes the principles behind the patterns, the names people use for them, and the rules for changing them.</p>'
  '<h4>Two kinds of pattern</h4>' +
  table(['Pattern', 'What it is', 'Examples'], [
    ['Functional', 'The parts people use to do things', 'Buttons, form fields, tables, navigation, cards'],
    ['Perceptual', 'How the product feels across all of them', 'Type, colour, spacing, motion, tone of voice']]) +
  '<p>Name both. A <strong>shared language</strong> (the same word for the same pattern in design files, code and conversation) is what lets a team use patterns consistently.</p>' +
  flow('From parts to pages', [
      ('Atoms', 'Labels, inputs, buttons.'),
      ('Molecules', 'Small groups: label, input and button as a search form.'),
      ('Organisms', 'Sections: a header with logo, navigation, search.'),
      ('Templates', 'Layouts that set content structure.'),
      ('Pages', 'Templates with real content, to stress-test.')],
    'Real content on pages finds the weak spots: a cart with one item and with ten, a name with three letters and with forty.') +
  '<h4>Keep it alive</h4>' +
  ul(['<strong>Make it official:</strong> a funded product with time, budget and people, not a side project. Start with a small pilot and show value first.',
      '<strong>Write a governance process:</strong> how to request, change, approve and retire a pattern, who documents it, and how it ships.',
      '<strong>Retire patterns with notice</strong> and a recommended replacement.',
      '<strong>Tell people what changed,</strong> where they already work: change logs, a roadmap, office hours.',
      '<strong>Keep design and code in sync.</strong> A library that drifts from production stops being trusted.',
      '<strong>Make it useful beyond developers:</strong> writers, product managers and designers need voice, principles and usage guidance too.']) +
  '<h4>Choose a team model</h4>' +
  table(['Model', 'How it works', 'Watch out for'], [
    ['Solitary', 'One product team’s library, offered to others', 'Its own team’s needs always come first; others fork it.'],
    ['Centralised', 'A dedicated team builds and distributes the system', 'Can drift from product needs while trying to prove its value.'],
    ['Federated', 'Designers from several teams decide together', 'Slow, and decisions get lost without someone writing them down.']]) +
  callout('Whatever the model', 'Assign someone to write decisions down and announce them. Without documentation the living style guide goes stale, and the system becomes folklore.') +
  see(('style-guides', 'Why Your UI Style Guide Sucks'), ('p-handoff', 'Handoff Is a Conversation')) +
  sources(SRC['khol'], SRC['atom2'], SRC['atom5'], SRC['eight']),
  'A system is patterns, names and an owner. Without the owner it decays.'))

# 11 IA --------------------------------------------------------------------------
CH.append(article('p-ia', 'Information Architecture Without Jargon', 'Audit what exists, sort with users, then test the tree', link('https://nngroup.com/articles/interpreting-tree-test-results/', 'Covert, Marquis, NN/g ↗'),
  'Information architecture is how the parts are arranged so the whole makes sense. Start by auditing how the structure really works today. Use an open card sort to learn how people group things, decide the structure yourself, then tree-test it. Median tree-test success across studies is about 62%; critical tasks should pass 90%.',
  '<p>IA is not the sitemap diagram. It is every decision about what things are called and where they live, and it shows up as findability: can people get to what they came for?</p>' +
  flow('An IA project, in order', [
      ('Audit', 'Map how the structure really works today.'),
      ('Card sort', 'Learn how people group and name things.'),
      ('Decide', 'Choose the structure; users don’t design it for you.'),
      ('Tree test', 'Check people can find things in it.')],
    'Card sorting generates ideas; tree testing evaluates a structure. Run them in this order.', loop='Fix labels, test again') +
  '<h4>Audit first</h4>' +
  ul(['Walk the navigation level by level and record every page with an ID that shows its place: <code>2.4.1</code> is the first page under the fourth under the second. The home page is <code>0.0</code>.',
      'Use <code>x</code> for repeating content, such as a news archive, instead of listing every item.',
      'Flag the odd ones: pages reachable only from inside content, files, external links, and pages whose place is unclear.',
      '<strong>Compare menu labels with page titles.</strong> Frequent mismatches point to inconsistent publishing or a broken back end.']) +
  '<h4>Card sorting</h4>' +
  table(['Choice', 'Use'], [
    ['Open sort', 'People create and name their own groups. The default: it shows their mental model.'],
    ['Closed sort', 'People sort into your categories. A tree test usually evaluates categories better.'],
    ['Hybrid', 'Some fixed categories. Avoid unless you’re sure of one or two; fixed groups bias the rest.'],
    ['Participants', 'At least 15 for qualitative insight, 30–50 for quantitative results.'],
    ['Cards', 'About 30–50. More and people tire and dump the rest in “Miscellaneous”.']]) +
  '<p>Card sorts ignore context and capture only one level. Treat group names as hints, not final labels.</p>'
  '<h4>Tree testing</h4>' +
  table(['Metric', 'What it tells you'], [
    ['Success', 'Reached a correct place. Below 40% poor, 61–80% good, above 90% excellent.'],
    ['Directness', 'Got there without backtracking. Confident wrong turns are the worst failures.'],
    ['First click', 'Where people expected it. A wrong first click usually leads to failure.'],
    ['Destination', 'Where they ended up. Spread across siblings means overlapping labels.']]) +
  ul(['<strong>Benchmarks:</strong> across 98 studies the median task success was 62%. Your own past results are the better yardstick.',
      '<strong>Critical and revenue tasks:</strong> aim above 90%.',
      '<strong>Comparing two trees:</strong> about 50 participants per tree, each person testing only one.',
      '<strong>Real-world success can be higher</strong> than in a tree test, which removes search and visual cues.']) +
  callout('Plain language is the method', 'Most IA problems are naming problems: two labels that mean the same, or one label that means different things to different teams. Agree the words before the boxes.') +
  see(('navigation', 'Why Your Navigation Stinks'), ('nav-guide', 'Primary Navigation Interaction Guide'), ('p-content-design', 'Content Design Starts With a User Need')) +
  sources(SRC['covert'], SRC['marquis'], SRC['nncs'], SRC['nnct'], SRC['nntt']),
  'Audit, sort, decide, test. Card sorts give ideas; tree tests give answers.'))

# 12 Content design -----------------------------------------------------------------
CH.append(article('p-content-design', 'Content Design Starts With a User Need', 'Who, what, why, and how you’ll know it’s met', link('https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/', 'GOV.UK ↗'),
  'Content design means meeting a user need in the best way possible, which isn’t always more words. Write every need as who, what and why, with a task verb and no solution in it. Add acceptance criteria, decide the format and place, then write, then keep it current.',
  '<p>Content design starts before writing. The question is not “how do I word this page?” but “what does someone need to do, and what is the best way to help?”. Sometimes the answer is a sentence in the interface, sometimes a page, sometimes removing a page.</p>' +
  rows('Anatomy of a user need', [
    ('As a…', 'Who, by their relationship to the task: “as a carer”, not “as a user”'),
    ('I need to…', 'A task: apply, pay, claim, change. “Understand” only if it serves a task'),
    ('So that…', 'Why it matters to them, without naming a solution'),
    ('Acceptance criteria', 'What must be true for the need to be met')],
    'Example: as a carer, I need to get financial help, so that I can keep looking after the person I care for.') +
  '<h4>Rules for a valid need</h4>' +
  ul(['<strong>Never start with “as a user”.</strong> Name the role that makes the need specific; different needs get different groups.',
      '<strong>Use task verbs.</strong> “Be aware of” is valid only when the “so that” shows a task it serves.',
      '<strong>No solution in the need.</strong> “I need to use the benefits calculator” justifies a tool; it doesn’t describe a need.',
      '<strong>Write acceptance criteria:</strong> for the carer, understand the allowance, check eligibility, apply, know the amount.',
      '<strong>Record each need</strong> with its criteria, evidence and owner, so content can be checked and retired.']) +
  '<h4>From need to content</h4>' +
  steps(['<strong>Identify the need,</strong> with evidence: search terms, support contacts, research.',
         '<strong>Plan:</strong> how much to say, in what format, where it belongs, and whether it already exists somewhere.',
         '<strong>Write clearly:</strong> plain words, front-loaded, accessible formatting.',
         '<strong>Maintain:</strong> keep it current, or archive it when the need is gone.']) +
  callout('Evidence over opinion', 'Style arguments go faster with evidence. The open <em>Readability Guidelines</em> collect usability evidence for style questions such as capitals, abbreviations, links and hyphens.') +
  see(('content-structure', 'Content Beyond Readability'), ('p-ia', 'Information Architecture Without Jargon'), ('style-guides', 'Why Your UI Style Guide Sucks')) +
  sources(SRC['gcd'], SRC['gun'], SRC['rg']),
  'Start from who needs to do what, and why. Then decide whether it needs words at all.'))

# 13 Thumbs -----------------------------------------------------------------------
CH.append(article('p-thumbs', 'Designing for Thumbs', 'How people really hold and tap their phones', link('https://uxmatters.com/mt/archives/2013/11/design-for-fingers-and-thumbs-instead-of-touch.php', 'Steven Hoober, UXmatters ↗'),
  'In 1,333 observations, 49% of people touching their phone used one hand, 36% cradled it and 15% used two hands, and they changed grip often. People tap the centre most accurately and the top and bottom edges least. Space targets about 7 mm apart in the centre and 10–12 mm at the top and bottom.',
  '<p>“Everyone uses their thumb” became a design rule faster than the evidence supported. Field observation shows a mix of grips that change every few seconds, and accuracy that depends more on where on the screen than on which hand.</p>' +
  rows('How people held their phones (780 people touching the screen)', [
    ('One hand', '49%: right thumb 67%, left thumb 33%'),
    ('Cradled', '36%: one hand holds, the other taps (thumb 72%, finger 28%)'),
    ('Two hands', '15%: nine in ten of them in portrait')],
    'Grips change constantly, so “reach zones” aren’t fixed. The author later withdrew his early thumb-reach drawings; plan for accuracy instead.', hi=0) +
  '<h4>Accuracy by screen zone</h4>' +
  table(['Zone', 'Accuracy', 'Space targets'], [
    ['Centre', 'Highest; people tap here most confidently', 'About 7 mm apart, centre to centre'],
    ['Left and right edges', 'Slightly lower, same for both hands', 'Prefer full-width list rows to small icons and checkboxes'],
    ['Top and bottom edges', 'Lowest: slower, less accurate, less confident', '10–12 mm between selectable items']]) +
  ul(['<strong>Why the edges miss:</strong> a tap counts on release, and at low thumb angles the touch drifts off the target.',
      '<strong>Don’t put risky or rare actions at the hard edges</strong> just because one-handed use is common; don’t ignore the third of people who cradle or use two hands either.',
      '<strong>Keep tappable items away from tab bars,</strong> or separate them with space or non-tappable labels.',
      '<strong>Leave room below the last list item</strong> so people can scroll it up to a comfortable spot.',
      '<strong>Check smaller screens:</strong> a bar that fits five icons on one phone may fit four on another.',
      '<strong>Test on a real device,</strong> held in every likely grip, and check what fingers cover.']) +
  callout('Visible size is not touch size', 'Separate the visible target, the touch target and the space around it. Misses come from crowding, so the fix is often spacing, not bigger buttons.') +
  see(('checkout', '11 Checkout Essentials'), ('input-field', 'The Anatomy of an Input Field')) +
  sources(SRC['hoob1'], SRC['hoob2']),
  'Design for the centre and the edges differently. Space targets more at the top and bottom.'))

# 14 Prototypes -----------------------------------------------------------------------
CH.append(article('p-prototypes', 'Prototypes Sized to the Question', 'Decide what the prototype is for before how polished it is', link('https://creativetech.mat.ucsb.edu/readings/Prototypes_prototype.pdf', 'Houde and Hill ↗'),
  'Describe a prototype by what it tests, not by its tool or polish. A prototype can explore its role in someone’s life, its look and feel, or how it would be built. Build the one that answers your most important open question most cheaply, say what it doesn’t answer, and build several.',
  '<p>“Low fidelity or high fidelity?” is the wrong first question. A rough paper flow can answer a role question perfectly, and a polished mockup can hide that nobody knows how it would work.</p>' +
  rows('What a prototype can test', [
    ('Role', 'What it does in someone’s life or work. Storyboards, scenarios, a faked service'),
    ('Look and feel', 'What it is like to see, hear and use. Visual mockups, motion studies'),
    ('Implementation', 'Whether and how it can work. Technical spikes, data and performance tests'),
    ('Integration', 'All three together, closest to the real thing; built last')],
    'Most early prototypes should sit firmly in one corner. Integration prototypes are slow and come after focused ones have answered their questions.', hi=0) +
  '<h4>Choose and use</h4>' +
  ul(['<strong>Start from the open question.</strong> Build the cheapest thing that answers it.',
      '<strong>Fidelity isn’t completeness.</strong> Detail and polish don’t show how settled a design is.',
      '<strong>Build several,</strong> with different tools for different questions, and throw them away.',
      '<strong>Know your audience.</strong> A customer test, an engineering review and a leadership pitch need different prototypes.',
      '<strong>Say what it doesn’t answer.</strong> Prototypes never explain their own purpose.']) +
  '<h4>Prototype types for testing ideas</h4>' +
  table(['Type', 'Good for'], [
    ['Paper or sketch', 'Flow and role questions, in minutes'],
    ['Clickable', 'Navigation and comprehension tests'],
    ['Realistic façade', 'Customer tests of a whole idea in a few days: only the surface people see is built'],
    ['Single-feature product', 'Whether people use one capability for real'],
    ['Wizard of Oz', 'A service that looks automated while a person does the work behind it']]) +
  callout('Match fidelity to what you ask', 'Testing comprehension with a beautiful mockup invites comments on colour. Testing a full idea with a sketch invites guessing. The question sets the fidelity.') +
  see(('figma', 'Users Don’t Care About Your Figma File'), ('d-assumptions', 'Assumption Mapping and Testing'), ('p-workshops', 'Workshops That Close')) +
  sources(SRC['houde'], SRC['gv'], SRC['rsb']),
  'Name the question first. Then build the cheapest prototype that answers it.'))

# 15 Handoff --------------------------------------------------------------------------
CH.append(article('p-handoff', 'Handoff Is a Conversation', 'Engineers in early, a shared definition of done', link('https://www.figma.com/reports/guide-to-handoff/', 'Figma report ↗'),
  'Handoff fails when it’s treated as a baton pass. Bring engineers in before designs settle, agree together what “done” means, and use the lightest process that works. Specs still matter: states, edge cases and real content are where most handoff bugs hide.',
  '<p>Designers and developers share a goal but live different days. A finished file thrown over the wall arrives with decisions nobody can question and gaps nobody noticed.</p>' +
  compare('Two kinds of handoff',
    ('Baton pass', ['Final file, then a meeting', 'Engineers see it for the first time', '“Done” means the file is done', 'Questions arrive in the last week']),
    ('Conversation', ['Engineers shape it early', 'Constraints found while cheap', '“Done” agreed together', 'Questions asked while sketching']),
    'Moving engineering earlier is the single change most teams report helps.') +
  '<h4>Practices</h4>' +
  ul(['<strong>Shift left:</strong> engineers join critiques and early sketches, not only the final review.',
      '<strong>Agree a definition of done</strong> before handoff: which states, breakpoints, accessibility checks and content are included.',
      '<strong>Use the minimum viable process.</strong> Find the lightest set of steps that works for your team, not a heavy template.',
      '<strong>Work from the system.</strong> Use existing components and say plainly where a design departs from them, and why.']) +
  '<h4>What the spec must cover</h4>' +
  ul(['<strong>Every state:</strong> empty, loading, partial, error, success, disabled and read-only.',
      '<strong>Edge content:</strong> the longest name, zero items and a thousand, missing images, translations 30% longer.',
      '<strong>Behaviour:</strong> what happens on failure, on slow networks, on undo, and on the second visit.',
      '<strong>Accessibility:</strong> focus order, labels, keyboard use, contrast.']) +
  callout('A useful test', 'If an engineer could build it without asking you a question, the spec is complete. If they would have to guess, the guess is your design.') +
  see(('status-design', 'Fixing Bad Status Design'), ('c-hidden-disabled', 'Hidden, Disabled or Read-Only?'), ('p-systems', 'Design Systems That Last')) +
  sources(SRC['figma'], SRC['atom5']),
  'Bring engineers in early and agree what done means. The spec covers every state.'))

# 16 Workshops -----------------------------------------------------------------------
CH.append(article('p-workshops', 'Workshops That Close', 'Open, explore, close, and design for the last step', link('https://www.oreilly.com/library/view/gamestorming-2-0/9781098148072/ch10.html', 'Gamestorming 2.0, GV ↗'),
  'A good workshop has three movements: open up options, explore them, and close on a decision. Closing fails when the opening and exploring were weak, so design the whole arc for the decision you need. For a big question, a five-day sprint goes from goal to tested prototype.',
  '<p>Most bad workshops don’t fail at the sticky notes. They fail at the end, when the group has fifty ideas and no way to choose, and everyone leaves with a vague sense of progress.</p>' +
  flow('The shape of a workshop', [
      ('Open', 'Generate many options: ideas, observations, questions.'),
      ('Explore', 'Group, compare and build on them.'),
      ('Close', 'Choose, prioritise and commit to next steps.')],
    'An unsatisfying set of ideas refuses to close. If closing fails, look at how the space was opened.') +
  '<h4>Design it backwards</h4>' +
  ul(['<strong>Start from the decision</strong> you need at the end, then choose the opening that feeds it.',
      '<strong>Pick each exercise for its movement.</strong> Brainstorming opens; affinity mapping explores; voting and ranking close.',
      '<strong>Write every exercise the same way:</strong> object of play, number of players, duration, how to play, strategy, and how to run it online.',
      '<strong>Close with something at stake.</strong> In the $100 test, groups split an imaginary $100 across options; money holds attention better than points.']) +
  '<h4>The five-day sprint</h4>' +
  table(['Day', 'What happens'], [
    ['Monday', 'Agree a long-term goal, map the challenge, ask experts, choose a target'],
    ['Tuesday', 'Review existing ideas, sketch solutions alone, start recruiting customers'],
    ['Wednesday', 'Critique sketches, choose, storyboard'],
    ['Thursday', 'Build a realistic prototype of the surface customers see; write the interview script'],
    ['Friday', 'Test with customers and summarise what you learned']]) +
  '<p>Use a sprint for a critical question you need answered before an expensive commitment. Google’s open-source Design Sprint Kit collects methods and variations for shorter or different sprints.</p>' +
  callout('Silent first', 'Individual work before group discussion, as in a sprint’s solo sketching or a critique’s silent writing, collects every view before the loudest voice sets the frame.') +
  see(('c-critiques', 'Running Design Critiques'), ('honest-artifacts', 'Honest Artifacts and Alignment Workshops'), ('p-prototypes', 'Prototypes Sized to the Question')) +
  sources(SRC['game'], SRC['gv'], SRC['dsk']),
  'Design the workshop backwards from the decision. Open, explore, then close.'))

NEW = [
 ('p-hierarchy', 'Visual Hierarchy and Spacing', 'Decide what matters before how it looks', 'One primary thing per view. Group by spacing before you reach for a border.'),
 ('p-type', 'Type That Reads', 'Size, line spacing and line length', '45 to 90 characters a line, 120 to 145% line spacing, and one emphasis at a time.'),
 ('p-colour', 'Colour With a Job', 'Neutrals for content, colour for meaning', 'Neutral by default. Colour means something, and never says it alone.'),
 ('p-systems', 'Design Systems That Last', 'Patterns, shared language, an owner', 'A system is patterns, names and an owner. Without the owner it decays.'),
 ('p-ia', 'Information Architecture Without Jargon', 'Audit, card sort, tree test', 'Audit, sort, decide, test. Card sorts give ideas; tree tests give answers.'),
 ('p-content-design', 'Content Design Starts With a User Need', 'Who, what, why, and acceptance criteria', 'Start from who needs to do what, and why. Then decide whether it needs words at all.'),
 ('p-thumbs', 'Designing for Thumbs', 'Grips, accuracy and target spacing', 'Design for the centre and the edges differently. Space targets more at the top and bottom.'),
 ('p-prototypes', 'Prototypes Sized to the Question', 'Role, look and feel, implementation', 'Name the question first. Then build the cheapest prototype that answers it.'),
 ('p-handoff', 'Handoff Is a Conversation', 'Engineers early, a shared definition of done', 'Bring engineers in early and agree what done means. The spec covers every state.'),
 ('p-workshops', 'Workshops That Close', 'Open, explore, close; the five-day sprint', 'Design the workshop backwards from the decision. Open, explore, then close.')]

# anchors that chapters link to must exist
ids = set(re.findall(r'id="([^"]+)"', s)) | {n[0] for n in NEW}
missing = sorted({h for h in re.findall(r'href="#([^"]+)"', ''.join(CH)) if h not in ids})
assert not missing, missing

# chapters after the last discovery chapter
end = s.index('</article>', s.index('id="d-strategy"')) + len('</article>\n')
s = s[:end] + ''.join(CH) + s[end:]

# TOC
m = re.search(r'(<a href="#d-strategy" class="toc-entry">.*?</a>\n)', s, re.S)
toc = ''.join('    <a href="#%s" class="toc-entry"><span class="toc-entry-title">%s <span class="toc-new">New</span> <span class="toc-entry-sub">— %s</span></span><span class="toc-num">%d</span></a>\n' % (i, t, sub, n)
              for n, (i, t, sub, _) in enumerate(NEW, start=111))
s = s[:m.end()] + toc + s[m.end():]

# rules
m = re.search(r'(<li><a href="#d-strategy">.*?</li>)', s, re.S)
s = s[:m.end()] + ''.join('<li><a href="#%s">%s</a> <span class="rules-src">%s</span></li>' % (i, r, t) for i, t, _, r in NEW) + s[m.end():]

# cover strip: add marks to the Part VI group (the last group)
m = re.search(r'<div class="corpus" aria-hidden="true">.*?</div>', s, re.S)
blk = m.group(0)
k = blk.rfind('</span>')
blk2 = blk[:k] + '<i class="new"></i>' * len(NEW) + blk[k:]
s = s.replace(blk, blk2)
s = s.replace('<b>47 of 110 are new in this edition</b>', '<b>57 of 120 are new in this edition</b>')
s = s.replace('110 chapters: 91 distilled from Trevor Calabro’s newsletter (all 182 posts, 2023–2026, were read), 13 companion notes and 6 discovery chapters from other authors',
              '120 chapters: 91 distilled from Trevor Calabro’s newsletter (all 182 posts, 2023–2026, were read), 13 companion notes, and 16 Part VI chapters on discovery and the product craft from other authors')
s = s.replace('Giff Constable, Strategyzer, Erika Hall,', 'Giff Constable, Strategyzer, Matthew Butterick, Alla Kholmatova, Brad Frost, Nathan Curtis, Lisa Maria Marquis, NN/g, GOV.UK, Steven Hoober, Stephanie Houde and Charles Hill, Dave Gray and Sunni Brown, Erika Hall,')
fp = 'credited on each page.</p>\n  <p style="margin-top:8px">Part V companion notes draw on'
s = s.replace('Strategyzer and <em>The Real Startup Book</em>, credited on each page.',
              'Strategyzer, <em>The Real Startup Book</em>, <em>Refactoring UI</em>, Matthew Butterick, WCAG, Alla Kholmatova, Brad Frost, Nathan Curtis, Abby Covert, Lisa Maria Marquis, NN/g, GOV.UK, Steven Hoober, Houde and Hill, GV, Figma and <em>Gamestorming 2.0</em>, credited on each page.')

# see-also lines in existing chapters
def add_see(aid, html):
    global s
    a = s.index('id="%s"' % aid); e = s.index('</article>', a)
    k = s.rfind('<div class="remember-box">', a, e)
    s = s[:(k if k > 0 else e)] + html + '\n  ' + s[(k if k > 0 else e):]
add_see('nav-guide', see(('p-ia', 'Information Architecture Without Jargon')))
add_see('style-guides', see(('p-systems', 'Design Systems That Last')))
add_see('content-structure', see(('p-content-design', 'Content Design Starts With a User Need')))
add_see('c-critiques', see(('p-workshops', 'Workshops That Close')))

p.write_text(s, encoding='utf-8')
print('added', len(NEW), 'craft chapters')
