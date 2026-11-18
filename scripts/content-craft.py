#!/usr/bin/env python3
"""Write the Product Craft module (10 articles) and add it to the manifest. Idempotent.
The correct option is listed first; the app shuffles options at runtime. Distractors are written
so the right answer is neither the longest nor an obvious short outlier."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent

def q(question, right, wrong, explain):
    return {"type": "single", "q": question, "options": [right] + wrong, "answer": 0, "explain": explain}
def card(title, text, tq):
    return {"title": title, "text": text, "try": tq}
A = []

A.append(dict(id='p-hierarchy', title='Visual Hierarchy and Spacing', icon='📐',
  summary='Three levels of emphasis, weight before size, and spacing from a fixed scale.',
  source='https://cdn.jsdelivr.net/npm/claude-code-skills@0.5.0/data/skills/ux-ui-design-system/references/refactoring-ui.md',
  intro='One primary thing per view. Group by spacing before you reach for a border.',
  learn=[
    card('Three levels', '**Primary:** the main action or information, one per view.\n**Secondary:** supporting content.\n**Tertiary:** metadata and hints.\n\nWhen everything is bold, nothing is.',
      q('How many primary actions per view?', 'One', ['Two, side by side', 'As many as the tasks need', 'One per section of the page'], 'One filled primary button; others are outlined or text.')),
    card('Weight and colour first', 'Make secondary text **lighter grey** or **lighter weight** before making it smaller.\n\nVisual emphasis and HTML structure are separate: an h2 doesn’t have to be big.',
      q('A label competes with the value next to it. First fix?', 'Make the label a lighter grey', ['Make the value much larger', 'Put a border around the value', 'Move the label into a tooltip'], 'De-emphasise the supporting part before enlarging the main one.')),
    card('A spacing scale', 'Base unit **4 or 8 px**: 4, 8, 12, 16, 24, 32, 48, 64, 96.\n\nForms: 4 px input to help text, 8 px label to input, **24 px between groups.**',
      q('Why space from a fixed scale?', 'Choices stay distinct and consistent', ['It loads faster in the browser', 'Screen readers rely on it', 'It removes the need for grids'], 'Values that grow apart stop near-identical gaps.')),
    card('Squint test', 'Start with **too much whitespace**, then remove.\n\nBlur your eyes: related items should merge into one shape, separate groups should stay apart. Space between groups must be larger than space inside them.',
      q('What should the squint test show?', 'Related items merge, groups stay apart', ['Every element is equally visible', 'Text stays readable when blurred', 'Colours keep enough contrast'], 'It checks grouping, not legibility.')),
  ],
  test=[
    q('Which is tertiary content?', 'A timestamp under a comment', ['The main call to action', 'The page’s key number', 'The body of the comment'], 'Metadata steps back.'),
    q('A secondary action should usually be:', 'An outlined or subtle button', ['A second filled button', 'A larger filled button', 'A link inside the page title'], 'Only the primary action is filled.'),
    q('A layout feels cramped. Best way to start?', 'Add generous space, then reduce', ['Add borders between all items', 'Shrink the font sizes a little', 'Remove the section headings'], 'Removing space from an airy layout works better than squeezing more in.'),
    q('Before adding a border, try:', 'A background change or more space', ['A thicker font for the label', 'A coloured icon in each corner', 'A drop shadow on every item'], 'Borders add lines to scan.'),
    q('Which layout can be dense?', 'A data table for daily users', ['A first-run onboarding screen', 'A marketing landing page', 'An empty state with one action'], 'Density suits repeated, expert work.'),
    q('Space between groups should be:', 'Larger than space inside them', ['Equal to space inside them', 'Smaller than space inside them', 'Set by the length of the labels'], 'Otherwise a label sits as close to the wrong field.'),
  ]))

A.append(dict(id='p-type', title='Type That Reads', icon='🔤',
  summary='Body size, line spacing and line length, plus a small type scale.',
  source='https://practicaltypography.com/summary-of-key-rules.html',
  intro='45 to 90 characters a line, 120 to 145% line spacing, and one emphasis at a time.',
  learn=[
    card('Body text first', 'Readers spend their time in body text.\n\nOn screen: **15–25 px** size, **120–145%** line spacing, **45–90 characters** a line, spaces included.',
      q('Which line length is comfortable?', 'About 70 characters', ['About 25 characters', 'About 130 characters', 'Any length the screen allows'], 'It sits inside the 45–90 range.')),
    card('A small scale', 'Pick from a scale such as 12, 14, 16, 18, 20, 24, 30, 36, 48 px.\n\nUse **two or three sizes per component**. Weights with a job: regular body, medium labels, semibold buttons, bold headings.',
      q('How many type sizes should one component use?', 'Two or three', ['Exactly one size', 'Five or six sizes', 'One per line of text'], 'Enough for hierarchy, few enough to stay calm.')),
    card('Emphasis', '**Bold or italic, sparingly and not together.**\nUnderline only links.\nAll caps for less than a line, with 5–12% extra letter spacing.',
      q('What should you underline?', 'Only links', ['Every heading on the page', 'Key words in a paragraph', 'Text you also make bold'], 'Underline signals a link.')),
    card('UI text is scanned', 'Reading rules come from long text. Interface text is scanned: **front-load** the words that matter and keep labels short.\n\nHelp pages and empty states still follow the reading rules.',
      q('Where do long-text reading rules still apply in a product?', 'Help pages and longer messages', ['Button labels and menu items', 'Icons and their tooltips', 'Table column headers'], 'Anything more than a couple of lines is read.')),
  ],
  test=[
    q('What line spacing suits body text?', '120–145% of the size', ['90–100% of the size', '200% of the size', 'The same as headings'], 'Tighter for headings, roomier for body.'),
    q('What body size range works on screen?', '15–25 px', ['9–12 px', '28–36 px', 'Whatever fits the layout'], 'Product UI body rarely goes below 16 px.'),
    q('Bold and italic together on one phrase:', 'Avoid it', ['Use it for key terms', 'Use it for all links', 'Use it in every heading'], 'One emphasis at a time.'),
    q('How should all-caps text be set?', 'Short, with a little extra letter spacing', ['Long, with tighter letter spacing', 'For whole paragraphs of warnings', 'Only in the body font’s light weight'], 'Less than a line, 5–12% extra spacing.'),
    q('Which is a typographic detail readers notice?', 'Straight quotes instead of curly ones', ['The colour of the scroll bar', 'The number of breakpoints used', 'Whether the CSS uses rem units'], 'Use curly quotes and real apostrophes.'),
    q('Wide screens most often break which rule?', 'Line length', ['Line spacing', 'Font weight', 'Letter spacing'], 'Long lines make the eye lose its place.'),
  ]))

A.append(dict(id='p-colour', title='Colour With a Job', icon='🎨',
  summary='Neutral scales, colour reserved for meaning, and contrast rules.',
  source='https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html',
  intro='Neutral by default. Colour means something, and never says it alone.',
  learn=[
    card('Roles, not swatches', '**Neutrals:** 9+ greys for text, borders, backgrounds.\n**Primary:** 5–7 shades for actions, links, selection.\n**Status:** success, warning, error, info, with text or an icon.',
      q('What should saturated colour be kept for?', 'Actions, links and status', ['Large background areas', 'Body text and headings', 'Borders between sections'], 'Then colour carries meaning when it appears.')),
    card('Contrast', '**Text:** 4.5:1.\n**Controls, their states and meaningful graphics:** 3:1 against what’s next to them.',
      q('A checkbox border against its background needs at least:', '3:1', ['1.5:1', '4.5:1 like body text', '7:1 for all controls'], 'Non-text contrast, WCAG 1.4.11.')),
    card('Never colour alone', 'Information shown by colour needs another cue: **text, a shape or an icon.**\n\nA red border alone doesn’t mark an error. Green for valid and red for invalid still need another cue.',
      q('How should an invalid field be marked?', 'Red border plus a message and icon', ['A red border on its own', 'A red background on its own', 'A slightly darker red label'], 'Colour must not be the only signal, WCAG 1.4.1.')),
    card('Greys with character', 'Tint greys slightly towards the brand hue.\n\nUse a grey from the scale for secondary text, not lower opacity, which shifts on coloured backgrounds.',
      q('Why avoid opacity for secondary text?', 'It changes on coloured backgrounds', ['Browsers don’t support it well', 'It always fails contrast checks', 'It makes text impossible to select'], 'A fixed grey stays predictable.')),
  ],
  test=[
    q('Minimum contrast for body text:', '4.5:1', ['2:1', '3:1', '10:1'], 'WCAG 1.4.3.'),
    q('How should links inside a paragraph stand out?', 'Underline, or 3:1 against the text', ['A different colour only', 'Bold weight only', 'A slightly larger size'], 'Colour alone isn’t enough.'),
    q('How many grey shades does a working palette need?', 'Nine or more', ['Exactly two', 'Three or four', 'Only black and white'], 'Text, borders and backgrounds need many steps.'),
    q('Two chart series differ only by hue. What to add?', 'Labels or patterns', ['A brighter palette', 'A darker background', 'A thicker chart border'], 'Check charts in greyscale.'),
    q('What does a mostly neutral screen make possible?', 'One colour shows what to do next', ['Faster loading of images', 'Fewer accessibility checks', 'No need for a type scale'], 'Colour stands out when it’s rare.'),
    q('A primary colour scale usually needs:', '5–7 shades', ['One exact shade', '2 shades', '15–20 shades'], 'For hover, pressed, selected and backgrounds.'),
  ]))

A.append(dict(id='p-systems', title='Design Systems That Last', icon='🧩',
  summary='Functional and perceptual patterns, atomic levels, governance and team models.',
  source='https://atomicdesign.bradfrost.com/chapter-5/',
  intro='A system is patterns, names and an owner. Without the owner it decays.',
  learn=[
    card('Two kinds of pattern', '**Functional:** the parts people use: buttons, fields, tables.\n**Perceptual:** how it feels: type, colour, spacing, motion, voice.\n\nA **shared language** names both, the same in design, code and conversation.',
      q('Which is a perceptual pattern?', 'Motion and timing', ['A date picker', 'A data table', 'A search field'], 'It shapes how everything feels.')),
    card('From parts to pages', '**Atoms** (inputs, buttons) → **molecules** (a search form) → **organisms** (a header) → **templates** (layouts) → **pages** (real content).\n\nReal content finds weak spots.',
      q('A label, input and button working as a search form is a:', 'Molecule', ['Atom', 'Template', 'Page'], 'A small group of atoms acting as one unit.')),
    card('Keep it alive', 'Run it as a **funded product**.\nWrite a **governance process**: request, change, approve, retire.\nRetire patterns with notice and a replacement.\nKeep design and code **in sync**.',
      q('What is the biggest threat to a design system?', 'Neglect', ['Too many components', 'Dark mode support', 'Design tokens'], 'Systems decay when nobody owns them.')),
    card('Team models', '**Solitary:** one team’s library, offered to others.\n**Centralised:** a dedicated system team.\n**Federated:** designers from several teams decide together.\n\nWhatever the model, someone writes decisions down.',
      q('A federated model’s main risk?', 'Slow decisions that get lost', ['One team’s needs dominate', 'No designers are involved', 'It can’t be documented'], 'Many voices, no single owner.')),
  ],
  test=[
    q('What makes a component library a design system?', 'Principles, names and rules for change', ['More components and variants', 'A dedicated Figma file', 'A public website'], 'The library is only one part.'),
    q('A homepage layout with no real content yet is a:', 'Template', ['Page', 'Organism', 'Molecule'], 'Pages are templates with real content.'),
    q('How should a pattern be retired?', 'With notice and a recommended replacement', ['Removed in the next release', 'Hidden from the documentation', 'Left in place but unsupported'], 'Teams need time to move.'),
    q('A solitary model’s main risk?', 'Its own team’s needs come first', ['Too many people decide', 'Nobody uses the library', 'Engineers aren’t involved'], 'Others fork it when it doesn’t fit.'),
    q('Who should a design system serve?', 'Designers, engineers, writers and PMs', ['Front-end engineers only', 'The design team only', 'New hires only'], 'Voice, principles and usage matter too.'),
    q('How do you start a design system?', 'A small pilot that shows value', ['A complete library before launch', 'A company-wide mandate first', 'A rebrand of the product'], 'Prove it, then ask for support.'),
  ]))

A.append(dict(id='p-ia', title='Information Architecture Without Jargon', icon='🗂️',
  summary='Structural audits, card sorting, tree testing and their benchmarks.',
  source='https://nngroup.com/articles/interpreting-tree-test-results/',
  intro='Audit, sort, decide, test. Card sorts give ideas; tree tests give answers.',
  learn=[
    card('In order', '**Audit** how it works today → **card sort** to learn how people group things → **decide** the structure → **tree test** it.\n\nCard sorting generates; tree testing evaluates.',
      q('What does a tree test do?', 'Checks people can find things in a structure', ['Shows how people would group content', 'Lists every page that exists today', 'Measures how fast pages load'], 'It evaluates a proposed or existing tree.')),
    card('Card sorting', '**Open sort:** people make and name groups. The default.\n**Closed:** your categories (a tree test is usually better).\n**15+** people for qualitative, **30–50** for quantitative. **30–50 cards.**',
      q('How many cards should a sort have?', 'About 30–50', ['About 5–10', 'About 100–150', 'Every page on the site'], 'More and people tire and dump the rest.')),
    card('Tree test metrics', '**Success:** reached a correct place.\n**Directness:** without backtracking.\n**First click:** where they expected it.\n**Destination:** where they ended up.',
      q('Clicks spread across several first options suggest:', 'Overlapping categories', ['A slow server', 'Too few participants', 'Labels that are too short'], 'The item could belong in several places.')),
    card('Benchmarks', 'Across 98 studies the median task success was **62%**.\nBelow 40% poor · 61–80% good · above 90% excellent.\n**Critical tasks: above 90%.** Comparing trees: about **50 people per tree**.',
      q('A checkout-critical task scores 75%. Verdict?', 'Not good enough for a critical task', ['Excellent for any task', 'Fine; above the median', 'Too low to measure'], 'Critical and revenue tasks should pass 90%.')),
  ],
  test=[
    q('How does a structural audit ID a page two levels down?', 'A decimal like 2.4.1', ['Its page title', 'Its URL length', 'The date it was added'], 'The ID shows its place in the hierarchy.'),
    q('Why avoid hybrid card sorts?', 'Fixed groups bias the rest', ['They take too long to run', 'Tools don’t support them', 'They need more than 100 people'], 'Use them only when sure of one or two categories.'),
    q('Menu labels often differ from page titles. What does it suggest?', 'Inconsistent publishing or a broken back end', ['The menu is too short', 'The site needs search', 'Users prefer short labels'], 'Track mismatches in the audit.'),
    q('What is directness?', 'Reaching the answer without backtracking', ['Choosing the shortest label', 'Finishing in under a minute', 'Clicking the first menu item'], 'Confident wrong turns are the worst failures.'),
    q('Why may real-world findability beat a tree test?', 'The test removes search and visual cues', ['Real users are more expert', 'Tree tests use fake content', 'Tree tests always time out'], 'The tree is shown bare.'),
    q('Most IA problems are really:', 'Naming problems', ['Server problems', 'Colour problems', 'Animation problems'], 'Agree the words before the boxes.'),
  ]))

A.append(dict(id='p-content-design', title='Content Design Starts With a User Need', icon='📝',
  summary='User needs as who, what and why, with acceptance criteria, before any writing.',
  source='https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/identify-user-needs/',
  intro='Start from who needs to do what, and why. Then decide whether it needs words at all.',
  learn=[
    card('The format', '**As a…** who, by their relationship to the task.\n**I need to…** a task.\n**So that…** why it matters.\n\nAs a carer, I need to get financial help, so that I can keep looking after the person I care for.',
      q('Which opening is valid?', 'As a carer', ['As a user', 'As a visitor', 'As everyone'], 'Name the role that makes the need specific.')),
    card('No solution inside', 'A need describes a goal, not a tool.\n\n“I need to use the benefits calculator” justifies a tool. “I need to know how much I could get” is a need.',
      q('Which is a real user need?', 'I need to know how much I could get', ['I need to use the benefits calculator', 'I need a PDF of the benefit rules', 'I need a chatbot to answer me'], 'The others name a solution.')),
    card('Acceptance criteria', 'What must be true for the need to be met.\n\nFor the carer: understand the allowance, check eligibility, apply, know the amount.\n\nRecord each need with its criteria, evidence and owner.',
      q('What do acceptance criteria describe?', 'What must happen for the need to be met', ['Who approved the content', 'How long the page should be', 'Which words are banned'], 'They make a need checkable.')),
    card('Need, plan, write, maintain', '**Identify** the need with evidence.\n**Plan** the amount, format and place, and check for duplicates.\n**Write** clearly.\n**Maintain** or archive.',
      q('What comes before writing?', 'Planning the format and place', ['Choosing the font', 'Writing the meta tags', 'Picking the illustrations'], 'Sometimes the answer is a sentence in the UI, or removing a page.')),
  ],
  test=[
    q('Which verb fits a user need best?', 'Apply', ['Be aware of', 'Feel', 'Browse'], 'Needs are tasks; “be aware of” only if it serves a task.'),
    q('When is “understand” acceptable in a need?', 'When the “so that” shows a task', ['Never, under any condition', 'Always, for policy pages', 'Only for legal content'], 'Understanding must serve a task.'),
    q('Where should needs be recorded?', 'With criteria, evidence and an owner', ['In the page footer', 'In the style guide', 'In the release notes'], 'So content can be checked and retired.'),
    q('Content design’s first question is:', 'What does someone need to do?', ['How should this page be worded?', 'How long can this page be?', 'Which template should we use?'], 'Wording comes after the need.'),
    q('A need is met elsewhere already. What do you do?', 'Don’t duplicate it', ['Write a better version anyway', 'Link to it from every page', 'Copy it into your section'], 'Planning checks for duplicates.'),
    q('Which free resource collects evidence for style decisions?', 'The Readability Guidelines', ['The Mom Test', 'Atomic Design', 'The Design Sprint Kit'], 'An open, evidence-based style project.'),
  ]))

A.append(dict(id='p-thumbs', title='Designing for Thumbs', icon='👍',
  summary='How people hold phones, where taps are accurate, and target spacing in millimetres.',
  source='https://uxmatters.com/mt/archives/2013/11/design-for-fingers-and-thumbs-instead-of-touch.php',
  intro='Design for the centre and the edges differently. Space targets more at the top and bottom.',
  learn=[
    card('Grips', 'Of 780 people touching their phones: **49% one hand, 36% cradled, 15% two hands.**\n\nGrips change every few seconds, so reach zones aren’t fixed.',
      q('About what share used one hand?', 'Half', ['Nine in ten', 'A quarter', 'One in ten'], '49% one-handed.')),
    card('Accuracy by zone', '**Centre:** most accurate.\n**Left and right:** slightly less, same for both hands.\n**Top and bottom:** least accurate, slowest, least confident.',
      q('Where are taps least accurate?', 'Top and bottom edges', ['The centre of the screen', 'Left edge for right-handers', 'Inside list rows'], 'Release-based taps drift at low thumb angles.')),
    card('Spacing in millimetres', '**Centre:** about **7 mm** apart.\n**Top and bottom:** **10–12 mm** between items.\n**Sides:** full-width list rows over small icons and checkboxes.',
      q('Targets in a bottom bar should be spaced about:', '10–12 mm apart', ['3–4 mm apart', '7 mm, same as centre', '20 mm or more apart'], 'Edges need more room.')),
    card('Practical rules', 'Keep tappable items away from tab bars.\nLeave room below the last list item.\nCheck smaller screens.\nTest on a real device in every grip.',
      q('Why leave room below the last list item?', 'So people can scroll it to a better spot', ['To fit an advert later', 'To meet a store requirement', 'To hide the tab bar'], 'It lets people self-correct.')),
  ],
  test=[
    q('Hoober’s later advice on thumb-reach drawings:', 'Disregard them; plan for accuracy', ['Use them for every layout', 'Apply them to tablets only', 'Mirror them for left-handers'], 'He withdrew the early drawings.'),
    q('How should rare or risky actions be placed?', 'Not in hard-to-hit edges just for reach', ['Always at the bottom edge', 'Always at the top corner', 'Next to the tab bar'], 'Accuracy matters more than reach.'),
    q('Which is the better side-of-screen control?', 'A full-width list row', ['A small checkbox', 'A tiny icon button', 'A 2 mm toggle'], 'Edges are less accurate.'),
    q('Misses near the bottom bar. Often the best fix?', 'More space around targets', ['Bigger icons only', 'A different colour', 'Removing labels'], 'Crowding causes misses.'),
    q('How many people were observed in total?', '1,333', ['80', '250', '10,000'], '780 of them were touching the screen.'),
    q('What should you check on smaller phones?', 'That targets aren’t squeezed', ['That colours look brighter', 'That fonts load faster', 'That animations run smoother'], 'A bar of five icons may fit only four.'),
  ]))

A.append(dict(id='p-prototypes', title='Prototypes Sized to the Question', icon='🧪',
  summary='Role, look and feel, and implementation prototypes, and why fidelity is the wrong first question.',
  source='https://creativetech.mat.ucsb.edu/readings/Prototypes_prototype.pdf',
  intro='Name the question first. Then build the cheapest prototype that answers it.',
  learn=[
    card('What it tests', '**Role:** what it does in someone’s life.\n**Look and feel:** what it’s like to use.\n**Implementation:** whether it can work.\n**Integration:** all three, built last.',
      q('A storyboard of a new service tests mostly:', 'Its role', ['Its implementation', 'Its look and feel', 'Its integration'], 'What it does in someone’s life.')),
    card('Fidelity isn’t completeness', 'Detail and polish don’t show how settled a design is.\n\nA rough sketch can answer a role question; a polished mockup can hide that nobody knows how it works.',
      q('What should you decide first?', 'The question it must answer', ['How polished it should be', 'Which tool to build it in', 'How many screens it needs'], 'Fidelity follows the question.')),
    card('Habits', 'Build **several**, with different tools, and throw them away.\nKnow your audience.\n**Say what it doesn’t answer.**',
      q('Why say what a prototype doesn’t answer?', 'Prototypes don’t explain their own purpose', ['It shortens the test sessions', 'Stakeholders ask for disclaimers', 'It avoids version-control conflicts'], 'Otherwise people judge it on the wrong things.')),
    card('Types for testing ideas', '**Paper:** flow and role.\n**Clickable:** navigation.\n**Realistic façade:** a whole idea in days.\n**Single-feature:** real use.\n**Wizard of Oz:** a person behind the curtain.',
      q('A service looks automated but a person does the work. This is:', 'Wizard of Oz', ['A clickable prototype', 'A paper prototype', 'An integration prototype'], 'Tests demand before building automation.')),
  ],
  test=[
    q('A technical spike on data performance tests:', 'Implementation', ['Role', 'Look and feel', 'Integration'], 'Whether and how it can work.'),
    q('When are integration prototypes built?', 'After focused ones answer their questions', ['At the very start', 'Instead of user tests', 'Only for marketing'], 'They are slow and hard to build.'),
    q('Testing comprehension with a beautiful mockup invites:', 'Comments on colour', ['Better task data', 'Faster sessions', 'Fewer participants'], 'Polish pulls attention to the surface.'),
    q('In a design sprint, Thursday’s prototype is:', 'A realistic surface customers see', ['A working production build', 'A set of paper sketches', 'A technical architecture'], 'Only the surface is built.'),
    q('How many prototypes should you build?', 'Several, for different questions', ['Exactly one, refined', 'One per stakeholder', 'None before research'], 'Different tools for different questions.'),
    q('What decides a prototype’s audience fit?', 'Who will see it and what they decide', ['The design tool licence', 'The number of screens', 'The brand colours'], 'A customer test and a leadership pitch differ.'),
  ]))

A.append(dict(id='p-handoff', title='Handoff Is a Conversation', icon='🤝',
  summary='Engineers in early, a shared definition of done, and specs that cover every state.',
  source='https://www.figma.com/reports/guide-to-handoff/',
  intro='Bring engineers in early and agree what done means. The spec covers every state.',
  learn=[
    card('Not a baton pass', 'A finished file thrown over the wall arrives with decisions nobody can question.\n\n**Shift left:** engineers join critiques and early sketches.',
      q('What does “shift left” mean here?', 'Engineers join earlier in design', ['Designs move to a left-aligned grid', 'Testing happens after launch', 'Handoff moves to the end of the sprint'], 'Constraints are found while cheap.')),
    card('Definition of done', 'Agree **before** handoff which states, breakpoints, accessibility checks and content are included.\n\nUse the **lightest process** that works.',
      q('When should the definition of done be agreed?', 'Before handoff, together', ['After the first bug report', 'By design alone', 'At the end of the quarter'], 'Shared expectations prevent late surprises.')),
    card('Every state', 'Empty, loading, partial, error, success, disabled, read-only.\nLongest name, zero items and a thousand, missing images, 30% longer translations.',
      q('Which is most often missing from specs?', 'Empty and error states', ['The happy path', 'The brand logo', 'The primary button'], 'Edge states are where handoff bugs hide.')),
    card('The test', 'If an engineer could build it **without asking a question**, the spec is complete.\n\nIf they would have to guess, the guess is your design.',
      q('An engineer has to guess a loading state. Whose design is it?', 'Effectively the engineer’s guess', ['The design system’s default', 'The product manager’s', 'Nobody’s; it won’t ship'], 'Unspecified states get designed by whoever builds them.')),
  ],
  test=[
    q('Handoff fails most when treated as:', 'A one-way baton pass', ['A shared conversation', 'An early collaboration', 'A review of the spec'], 'Questions arrive in the last week.'),
    q('What is a “minimum viable process”?', 'The lightest steps that work for your team', ['A heavy template for every project', 'No process at all', 'The process of the largest team'], 'Not a standard checklist.'),
    q('A design departs from the system. What to do?', 'Say where and why in the spec', ['Hide it in the file', 'Rebuild the system first', 'Ask engineers to notice'], 'Work from the system, explain departures.'),
    q('Which content edge case belongs in a spec?', 'A translation 30% longer', ['The designer’s favourite font', 'The meeting notes', 'The project codename'], 'Real content breaks layouts.'),
    q('Which accessibility items belong in a spec?', 'Focus order, labels, keyboard use', ['Brand colours only', 'Image file sizes only', 'Animation easing only'], 'Plus contrast.'),
    q('What single change do teams most report helps?', 'Bringing engineers in earlier', ['Longer handoff meetings', 'More detailed redlines', 'A new design tool'], 'Moving engineering earlier.'),
  ]))

A.append(dict(id='p-workshops', title='Workshops That Close', icon='🗳️',
  summary='Open, explore, close; designing backwards from the decision; the five-day sprint.',
  source='https://gv.com/sprint',
  intro='Design the workshop backwards from the decision. Open, explore, then close.',
  learn=[
    card('Three movements', '**Open:** generate options.\n**Explore:** group, compare, build.\n**Close:** choose and commit.\n\nAn unsatisfying set of ideas refuses to close.',
      q('Closing fails. Where should you look first?', 'How the space was opened and explored', ['The voting tool you used', 'The room booking', 'The length of the break'], 'Weak openings make closing impossible.')),
    card('Design backwards', 'Start from the **decision you need**, then pick the opening that feeds it.\nBrainstorming opens; affinity mapping explores; voting and ranking close.',
      q('Which exercise closes?', 'Dot voting', ['Brainstorming', 'Mind mapping', 'Affinity grouping'], 'Closing means choosing.')),
    card('The $100 test', 'Groups split an imaginary **$100** across options.\n\nMoney holds attention better than points or rankings.',
      q('Why use money in the $100 test?', 'It holds attention better than points', ['It matches the real budget', 'It is faster to count', 'It avoids any ties'], 'Something at stake sharpens choices.')),
    card('Five-day sprint', '**Mon:** goal, map, target.\n**Tue:** sketch alone, recruit.\n**Wed:** decide, storyboard.\n**Thu:** realistic prototype.\n**Fri:** test with customers.',
      q('What happens on Friday of a sprint?', 'Customer tests of the prototype', ['Sketching solutions', 'Choosing a target', 'Building production code'], 'Then summarise what you learned.')),
  ],
  test=[
    q('Which movement comes second?', 'Explore', ['Close', 'Open', 'Decide'], 'Open, explore, close.'),
    q('When is a sprint worth running?', 'A critical question before a costly commitment', ['Every two weeks as routine', 'For small copy changes', 'After launch, to celebrate'], 'Answer it before spending.'),
    q('Why sketch alone before discussing?', 'Every view is collected before anchoring', ['It saves printing costs', 'Facilitators prefer silence', 'It shortens the workshop'], 'The loudest voice doesn’t set the frame.'),
    q('A good game write-up includes:', 'Players, duration, how to play, strategy', ['Only the name and a photo', 'Only the materials list', 'Only who attended last time'], 'Plus how to run it online.'),
    q('Which free resource collects sprint methods?', 'Google’s Design Sprint Kit', ['The Mom Test', 'Practical Typography', 'Atomic Design'], 'Open-source methods and recipes.'),
    q('Fifty ideas and no way to choose means the workshop lacked:', 'A planned closing', ['Enough sticky notes', 'A bigger room', 'More participants'], 'Design for the last step.'),
  ]))

module = {"id": "craft", "name": "Product Craft", "icon": "📐", "week": "Module 14",
          "subtitle": "Hierarchy, type, colour, systems, IA, content, mobile, prototypes, handoff, workshops", "open": True, "articles": []}
for a in A:
    art = {"id": a['id'], "module": "craft", "title": a['title'], "icon": a['icon'], "intro": a['intro'],
           "topics": [{"id": "main", "title": a['title'], "learn": a['learn'], "test": a['test']}]}
    (root / 'content' / (a['id'] + '.json')).write_text(json.dumps(art, ensure_ascii=False, indent=1), encoding='utf-8')
    module['articles'].append({"id": a['id'], "title": a['title'], "icon": a['icon'], "summary": a['summary'],
                               "file": "content/%s.json" % a['id'], "source": a['source'], "q": len(a['test'])})
mp = root / 'content' / 'manifest.json'
m = json.loads(mp.read_text(encoding='utf-8'))
m['modules'] = [x for x in m['modules'] if x['id'] != 'craft'] + [module]
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('wrote', len(A), 'articles')

# ---- rebalance: lengthen or shorten options so the right answer isn't an obvious outlier ----
FIX = {
 'How many primary actions per view?': {'Two, side by side': 'Two', 'As many as the tasks need': 'Three', 'One per section of the page': 'Five'},
 'What should you underline?': {'Every heading on the page': 'Headings', 'Key words in a paragraph': 'Key words', 'Text you also make bold': 'Bold text'},
 'Bold and italic together on one phrase:': {'Use it for key terms': 'Use it often', 'Use it for all links': 'Use it for links', 'Use it in every heading': 'Use in headings'},
 'A checkbox border against its background needs at least:': {'4.5:1 like body text': '4.5:1', '7:1 for all controls': '7:1'},
 'What is the biggest threat to a design system?': {'Too many components': 'Too many parts', 'Dark mode support': 'Dark mode', 'Design tokens': 'Tokens'},
 'Which is a perceptual pattern?': {'A date picker': 'A date picker with a calendar grid'},
 'A federated model’s main risk?': {'It can’t be documented': 'It can’t be documented by any single team'},
 'What makes a component library a design system?': {'More components and variants': 'More components and variants for every case'},
 'Who should a design system serve?': {'Front-end engineers only': 'Front-end engineers who build the components only'},
 'How should a pattern be retired?': {'Left in place but unsupported': 'Left in place, unsupported and undocumented'},
 'About what share used one hand?': {'Nine in ten': '90%', 'A quarter': '25%', 'One in ten': '10%', 'Half': '49%'},
 'A storyboard of a new service tests mostly:': {'Its implementation': 'Its build', 'Its look and feel': 'Its looks', 'Its integration': 'All of it'},
 'A technical spike on data performance tests:': {'Look and feel': 'Look and feel only', 'Integration': 'Integration of all three'},
 'When are integration prototypes built?': {'Instead of user tests': 'Instead of running any user tests at all', 'Only for marketing': 'Only for marketing demos and sales pitches to clients'},
 'What should you decide first?': {'Which tool to build it in': 'Which design tool to build it in and share it from'},
 'Why say what a prototype doesn’t answer?': {'It avoids version-control conflicts': 'It avoids version-control conflicts between files'},
 'In a design sprint, Thursday’s prototype is:': {'A working production build': 'A working production build with real data'},
 'What decides a prototype’s audience fit?': {'The design tool licence': 'The design tool licence your company has bought'},
 'What is a “minimum viable process”?': {'A heavy template for every project': 'A heavy, standard template applied to every project'},
 'Which is most often missing from specs?': {'The primary button': 'The primary button and its hover style'},
 'An engineer has to guess a loading state. Whose design is it?': {'The design system’s default': 'The design system’s default, applied automatically'},
 'Which accessibility items belong in a spec?': {'Animation easing only': 'Animation easing curves and their durations only'},
 'What single change do teams most report helps?': {'More detailed redlines': 'More detailed redlines on every screen'},
 'Closing fails. Where should you look first?': {'The voting tool you used': 'The voting tool you used and how it was set up'},
 'Why use money in the $100 test?': {'It matches the real budget': 'It matches the real budget the team has to spend'},
 'What happens on Friday of a sprint?': {'Building production code': 'Building production code for the chosen idea'},
 'Which movement comes second?': {'Decide': 'Deciding on the outcome'},
 'When is a sprint worth running?': {'Every two weeks as routine': 'Every two weeks as a routine part of each cycle'},
 'Why sketch alone before discussing?': {'Facilitators prefer silence': 'Facilitators prefer a quiet room for the first hour'},
 'A good game write-up includes:': {'Only who attended last time': 'Only who attended last time and what they thought of it'},
}
import glob
used = set()
for f in glob.glob(str(root / 'content' / 'p-*.json')):
    art = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    for t in art['topics']:
        for qq in [c['try'] for c in t['learn']] + t['test']:
            if qq['q'] in FIX:
                used.add(qq['q'])
                qq['options'] = [FIX[qq['q']].get(o, o) for o in qq['options']]
    pathlib.Path(f).write_text(json.dumps(art, ensure_ascii=False, indent=1), encoding='utf-8')
assert not set(FIX) - used, set(FIX) - used
print('rebalanced', len(used))
