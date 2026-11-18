#!/usr/bin/env python3
"""Add Part VI (Discovery and the Product Craft) to the book: chapters, TOC, rail, rules, cover counts,
see-also links. Idempotent: skips chapters already present. Re-run book-progress.py afterwards."""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from bookfig import rows, flow, compare, matrix, tree

root = pathlib.Path(__file__).resolve().parent.parent
p = root / 'book' / 'ux-in-the-real-world.html'
s = p.read_text(encoding='utf-8')

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

def article(id_, tag, title, sub, source, summary, body, remember):
    return '''
<!-- %s -->
<article class="article" id="%s">
  <div class="article-meta">
    <span class="article-tag companion">%s</span>
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
''' % (id_, id_, tag, source, title, sub, summary, body, remember)

PT = 'https://www.producttalk.org/'
SRC = {
  'cdh': 'Teresa Torres, <em>Continuous Discovery Habits</em> (2021)',
  'ost': link(PT + 'opportunity-solution-trees.md', 'Torres, “Opportunity Solution Trees”'),
  'start': link(PT + 'getting-started-with-discovery.md', 'Torres, “Getting started with discovery”'),
  'prio': link(PT + 'prioritize-opportunities.md', 'Torres, “Prioritizing opportunities”'),
  'map': link(PT + 'opportunity-mapping.md', 'Torres, “Opportunity mapping”'),
  'source': link(PT + 'sourcing-opportunities.md', 'Torres, “Sourcing opportunities”'),
  'svpg': link('https://svpg.com/product-risk-taxonomies', 'Marty Cagan, “Product risk taxonomies”'),
  'perri': link('https://evansamek.substack.com/p/escaping-the-build-trap-by-melissa', 'Melissa Perri, <em>Escaping the Build Trap</em> (summary)'),
  'mom': link('https://www.ybrikman.com/blog/2023/03/29/the-mom-test/', 'Rob Fitzpatrick, <em>The Mom Test</em> (summary)'),
  'tth': link('https://giffconstable.com/2014/09/announcing-talking-to-humans-new-book/', 'Giff Constable, <em>Talking to Humans</em> (free)'),
  'amap': link('https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter', 'Strategyzer, “Assumptions mapping”'),
  'exp': link('https://www.strategyzer.com/library/designing-strong-experiments', 'Strategyzer, “Designing strong experiments”'),
  'rsb': link('https://kromatic.com/real-startup-book/4-evaluative-product-experiments/', '<em>The Real Startup Book</em> (free)'),
  'rumelt': link('https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-perils-of-bad-strategy', 'Richard Rumelt, “The perils of bad strategy” (McKinsey Quarterly, 2011)'),
}

chapters = []

# 1 ---------------------------------------------------------------------------
chapters.append(article('d-discovery-loop', 'Discovery', 'Continuous Discovery in One Page',
  'Weekly customer contact, by the people who build the product',
  link(PT + 'getting-started-with-discovery.md', 'Teresa Torres, Product Talk ↗'),
  'Continuous discovery means the team that builds the product talks to customers at least every week, in small research activities aimed at one outcome. The product manager, designer and engineer do it together. The work runs in a loop: outcome, opportunities, solutions, assumption tests.',
  '<p>Project research happens before a big decision and then stops. Continuous discovery runs alongside delivery, so every decision keeps meeting fresh evidence. The unit is small: one interview a week, one assumption tested, one branch of the map updated.</p>' +
  flow('The discovery loop', [
      ('Outcome', 'The change in customer behaviour the team is asked to drive.'),
      ('Opportunities', 'Needs, pain points and desires heard in customer stories.'),
      ('Solutions', 'About three ideas for one target opportunity.'),
      ('Assumption tests', 'Small checks of what must be true for an idea to work.')],
    'Each turn of the loop is small. What the tests teach sends you back to the map, not straight to the backlog.',
    loop='Results update the opportunity map') +
  '<h4>Who does it</h4>'
  '<p>The <strong>product trio</strong>: a product manager, a designer and an engineer. They interview together. When all three hear the same stories, they argue less about whose information is right and more about what to do.</p>'
  '<h4>The minimum habits</h4>' +
  ul(['<strong>A customer touchpoint every week.</strong> An interview, a test or a visit. Weekly is the floor, not the target.',
      '<strong>Automated recruiting.</strong> An invitation inside the product or on the site, so next week’s interview is already in the calendar.',
      '<strong>A one-page snapshot after every interview,</strong> shared with stakeholders. Showing your work builds trust faster than a quarterly readout.',
      '<strong>Refresh the opportunity map every three to four interviews.</strong>',
      '<strong>Test assumptions before you build.</strong> Story-map the idea and list what must be true. It takes 20 to 30 minutes.']) +
  '<h4>Where to start</h4>' +
  table(['Your situation', 'Signs', 'First step'], [
    ['Feature factory', 'Fixed roadmap, success counted in features shipped', 'Story-map one planned feature and list its hidden assumptions.'],
    ['Messy middle', 'New to OKRs or trios, mixed signals from leadership', 'Make one bright spot: the trio interviews together, with recruiting automated.'],
    ['Sliding back', 'Stakeholders under pressure ask for specific features', 'Share a snapshot after every interview, and the map, to rebuild trust.']]) +
  callout('Why it matters', 'It is the habit, not the method, that changes outcomes. Eleven habits make up the full practice, and teams can adopt them one at a time.') +
  see(('d-outcomes', 'Outcomes, Not Outputs'), ('d-interviews', 'Story-Based Interviews'), ('c-three-books', 'Three Sources, One Practice'), ('research-rigor', 'Research Rigor at Product Speed')) +
  sources(SRC['cdh'], SRC['start'], SRC['ost']),
  'Talk to customers every week, as a trio, about one outcome.'))

# 2 ---------------------------------------------------------------------------
chapters.append(article('d-outcomes', 'Discovery', 'Outcomes, Not Outputs',
  'Getting out of the build trap',
  link('https://svpg.com/product-risk-taxonomies', 'Cagan, Perri, Torres ↗'),
  'Outputs are what a team ships. Outcomes are what changes because of it: customer behaviour, and the business results that follow. Teams judged on outputs fall into the build trap. Discovery starts from a product outcome the team can move.',
  '<p>The build trap is measuring success by features shipped. Features are easy to count, so they become the goal. But a product has no value on its own; its value is what it does for customers, and the business gains only when that happens.</p>' +
  compare('What a team can be judged on',
    ('Outputs', ['Features shipped', 'Roadmap dates met', 'Story points closed', 'Releases per quarter']),
    ('Outcomes', ['More teams finish setup in week one', 'Fewer support tickets about billing', 'A segment keeps using the product', 'Less time to first value']),
    'Outputs are evidence of effort. Outcomes are evidence of value.') +
  '<h4>Three kinds of metric</h4>' +
  table(['Metric', 'Example', 'For discovery'], [
    ['Business outcome', 'Revenue, retention, cost to serve', 'Too far away: many teams and the market move it. Use it to choose product outcomes.'],
    ['Product outcome', 'Customer behaviour or sentiment in the product, such as teams that invite a colleague in week one', '<strong>The best fit.</strong> The team can move it, and it leaves room for many solutions.'],
    ['Traction metric', 'Use of one feature', 'Fine for optimising that feature. As a discovery goal it narrows the solutions to one.']]) +
  '<h4>From strategy to the team’s outcome</h4>' +
  flow('Where a team’s outcome comes from', [
      ('Strategic intent', 'A few goals for the next one to two years: grow or protect revenue, cut or avoid cost.'),
      ('Product initiatives', 'The customer problems to solve to reach an intent.'),
      ('Options', 'Candidate solutions, treated as bets, for each initiative.')],
    'Leaders set the intent and the why. Teams own the how. Dictating features at the top skips the step where evidence enters.') +
  '<h4>Four risks to check before building</h4>' +
  table(['Risk', 'Question', 'Who knows most'], [
    ['Value', 'Will customers buy it or choose to use it?', 'Customers and buyers'],
    ['Usability', 'Can people work out how to use it?', 'Users, through tests'],
    ['Feasibility', 'Can we build it with the time, skills and technology we have?', 'Engineers'],
    ['Viability', 'Does it work for the business: cost, sales, legal, ethics?', 'Stakeholders across the business']]) +
  callout('When someone asks for a feature', 'Ask which outcome it should move, and what you would see if it worked. If nobody can say, the request is an output looking for a reason.') +
  see(('c-tars', 'Measuring Feature Impact (TARS)'), ('pmf', 'Measuring Product-Market Fit'), ('d-strategy', 'Strategy You Can Test')) +
  sources(SRC['perri'], SRC['svpg'], SRC['ost'], SRC['cdh']),
  'Ship to move an outcome. A feature is a bet, not a result.'))

# 3 ---------------------------------------------------------------------------
chapters.append(article('d-interviews', 'Discovery', 'Story-Based Interviews',
  'Ask about the last time, not about the future',
  link(PT + 'sourcing-opportunities.md', 'Torres, Constable, Fitzpatrick ↗'),
  'People can’t predict what they’ll do, and they are polite about your ideas. Ask for one specific, recent story and dig into it step by step. Treat compliments, generalisations and feature requests as prompts to dig, not as evidence.',
  '<p>“Would you use this?” invites a guess. “Tell me about the last time you…” brings back what happened: who was there, what they tried, what it cost them. The details of a real story are what make the answers to who, what, why and how trustworthy.</p>' +
  compare('Questions that get stories',
    ('Instead of', ['Would you use a feature that…?', 'Is this a good idea?', 'How much would you pay?', 'Do you have this problem?']),
    ('Ask', ['Tell me about the last time you…', 'How do you handle this today?', 'What did it cost you last month?', 'What else have you tried?']),
    'Questions about the past and the present get facts. Questions about the future get guesses.') +
  '<h4>Dig out the story</h4>' +
  steps(['<strong>Set the scene.</strong> When was it, where were they, what happened just before?',
         '<strong>Keep them in the moment.</strong> Show that every detail matters. Ask what happened next until the story ends.',
         '<strong>Bring generalisations back.</strong> “I usually…” becomes “And last time, what did you do?”',
         '<strong>Don’t stop at a short answer.</strong> “I watched a show after dinner” is a start, not a story.',
         '<strong>Talk less.</strong> Listen for the parts they didn’t expect to mention.']) +
  '<h4>Three kinds of bad data</h4>' +
  table(['Signal', 'Sounds like', 'What to do'], [
    ['Compliments', '“That’s really cool.”', 'Ask what they do today and what it costs them.'],
    ['Generalisations and promises', '“I always…”, “I would definitely buy that.”', 'Ask for the last time it happened. Future promises are the most misleading data of all.'],
    ['Feature requests', '“You should add…”', 'Ask why they want it and what they do now. The need underneath is the opportunity.']]) +
  '<h4>When you are testing demand: look for commitment</h4>'
  '<p>Praise costs nothing. Real interest shows as something given up: <strong>time</strong> (another meeting, a trial), <strong>reputation</strong> (an introduction to a colleague) or <strong>money</strong> (a pre-order or a letter of intent). A conversation that ends in compliments and no next step taught you little.</p>'
  '<h4>Make it weekly</h4>' +
  ul(['<strong>Recruit automatically:</strong> an invitation in the product, a line in the onboarding email, a standing request to customer success.',
      '<strong>Interview as a trio</strong> when you can.',
      '<strong>Write a snapshot within the hour:</strong> a memorable quote, quick facts about the person, the story’s key moments, and the opportunities you heard.']) +
  callout('Common mistake', 'Selling when you should be listening, and speculating when you should be observing. If you hear yourself explaining the product, stop and ask about their last time instead.') +
  see(('interview-questions', 'Interview Questions That Work'), ('behavioral-evidence', 'Behavioral Evidence > Self-Reported Evidence'), ('c-b2b-research', 'Research Without User Access'), ('c-stakeholders', 'Interviewing Stakeholders')) +
  sources(SRC['cdh'], SRC['source'], SRC['start'], SRC['tth'], SRC['mom'], SRC['exp']),
  'Collect stories about the last time. Opinions about the future aren’t data.'))

# 4 ---------------------------------------------------------------------------
chapters.append(article('d-ost', 'Discovery', 'Opportunity Solution Trees',
  'Map what you heard before choosing what to build',
  link(PT + 'opportunity-solution-trees.md', 'Teresa Torres, Product Talk ↗'),
  'An opportunity solution tree puts the outcome at the top, the opportunities heard in interviews below it, solutions only under the one opportunity you choose, and assumption tests under each solution. Choose the target on size, market position, strategic fit and how much customers care. Leave effort out.',
  '<p>A flat backlog mixes needs of every size, some overlapping and some containing others, so nothing can be compared fairly. A tree sorts them: big needs break into smaller ones, and you choose at one level at a time.</p>' +
  tree('An opportunity solution tree',
       'Outcome: more teams finish setup in week 1',
       ['I don’t know where to start', 'I can’t get my team to join', 'Importing my data is slow'],
       ['Colleagues ignore my invite', 'I don’t know who should be invited'],
       ['Invite from a shared doc link', 'A reminder sent as me', 'Show the invite in Slack'],
       ['Do invites get opened?', 'Will they click a link?'],
       'One branch worked through. Solutions are compared under the target only; the rest of the tree waits.') +
  '<h4>What counts as an opportunity</h4>'
  '<p>An unmet customer need, pain point or desire, written as the customer might say it. Desires count, not only problems.</p>' +
  callout('The disguised-solution test', 'Could it be addressed in more than one way? If not, it’s a solution. “I need a calendar export” has one answer; “I need to see my schedule outside the app” has many. Ask “why?” to find the opportunity underneath.') +
  '<h4>Build the structure</h4>' +
  ul(['<strong>A child is part of its parent.</strong> Ask “what are other reasons why…?” to find its siblings.',
      '<strong>Siblings are distinct:</strong> you can address one without the others.',
      '<strong>Similar needs can be siblings under a shared parent.</strong> “Watch on a flight” and “watch on a train” both sit under “watch on the go”, because their constraints differ.',
      '<strong>Source opportunities from story interviews,</strong> not from memory. Tickets, sales calls and analytics suggest what to ask about; they aren’t opportunities on their own.']) +
  '<h4>Choose a target</h4>' +
  table(['Factor', 'Question'], [
    ['Size', 'How many customers does it affect, and how often?'],
    ['Market position', 'Does it close a gap with competitors or set us apart?'],
    ['Strategic fit', 'Does it serve the company’s vision and strategy?'],
    ['Customer importance', 'How much do customers care, and how happy are they with what they use now?']]) +
  '<p>Leave effort out: feasibility is tested later, and judging it now rules out good opportunities too early. Compare only the opportunities in one row, starting at the top, then move down within the winner. Treat the choice as a two-way door: if tests fail, step back up and choose again. Avoid scoring formulas; numbers on subjective judgements start to feel like facts.</p>'
  '<h4>Then the solutions</h4>'
  '<p>Brainstorm only for the target, never for the whole tree. Aim for about three ideas so you compare rather than defend one, and break each into the assumptions it depends on.</p>'
  '<h4>Keep it alive</h4>' +
  table(['When', 'What to do'], [
    ['Before the first tree', 'Have a clear outcome, a working theory of the customer, and three or four story interviews.'],
    ['Every 3–4 interviews', 'Revisit the tree. Most changes should add detail lower down; the top level settles.'],
    ['Still messy after 6–8 interviews', 'Check how you interview and synthesise, not the tree.'],
    ['Outcome changes direction', 'Start a new tree. A new target number for the same outcome isn’t a reason.']]) +
  '<h4>Common mistakes</h4>' +
  ul(['Inventing opportunities instead of hearing them.', 'Solutions dressed as opportunities.', 'Brainstorming across the whole tree.',
      'Chasing the latest interview or ticket.', 'Several outcomes at once, or one tree for the whole company.']) +
  see(('d-assumptions', 'Assumption Mapping and Testing'), ('fuzzy-middle', 'Escape the Fuzzy Middle')) +
  sources(SRC['cdh'], SRC['ost'], SRC['map'], SRC['prio']),
  'Map the problem space before you pick a solution. Compare three ideas, not one.'))

# 5 ---------------------------------------------------------------------------
chapters.append(article('d-assumptions', 'Discovery', 'Assumption Mapping and Testing',
  'Test the riskiest belief, as cheaply as the risk allows',
  link('https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter', 'Torres, Strategyzer, Kromatic ↗'),
  'Every solution rests on beliefs that might be wrong. List them by type, place them on importance and evidence, and test the important, unevidenced ones first. What people do is stronger evidence than what they say. Start with cheap tests and move to stronger ones as the signal improves.',
  '<h4>Find the assumptions</h4>'
  '<p>Story-map the idea as if it already existed: one row for each step the customer takes, and under each step what must be true for it to work. It takes 20 to 30 minutes and is useful even if you never run a test. Write each assumption as “We believe that…”, which keeps the team honest about being wrong.</p>' +
  table(['Type', 'The question', 'Example'], [
    ['Desirability', 'Do they want it?', 'Admins want colleagues to join in week one.'],
    ['Usability', 'Can they use it?', 'People find the invite button without help.'],
    ['Feasibility', 'Can we build it?', 'We can send invites from the customer’s own address.'],
    ['Viability', 'Does it work for the business?', 'More seats don’t raise our support cost.'],
    ['Ethics', 'Could it harm anyone?', 'Reminders don’t pressure people who said no.']]) +
  matrix('Which assumptions to test first', 'Evidence: none ← → strong', 'Importance',
         [('Important, some evidence', 'Watch. Look for evidence that would prove it wrong.'),
          ('Important, no evidence', 'Test first. If this is wrong, the idea fails and you would not know.'),
          ('Minor, some evidence', 'Leave it.'),
          ('Minor, no evidence', 'Note it. Test only if it becomes important.')],
         'Importance asks: if this belief is wrong, does the idea fail? Evidence means something observed, not who argues loudest.', hi=1) +
  '<h4>Choose the test</h4>' +
  table(['Strength', 'Evidence of', 'Examples'], [
    ['Weaker', 'What people say', 'Interviews, surveys, comprehension questions'],
    ['Stronger', 'What people do', 'Prototype tests, fake doors, Wizard of Oz, A/B tests'],
    ['Strongest', 'What people give up', 'Sign-ups that take effort, pre-orders, paid pilots']]) +
  ul(['<strong>Start cheap and weak,</strong> then move to stronger tests as the signal gets clearer. Several tests can check one assumption.',
      '<strong>Change one thing at a time.</strong> Extra variables make the result impossible to read.',
      '<strong>Write the pass line before the test,</strong> so the result can’t be argued afterwards.',
      '<strong>Define who you test with.</strong> The whole team should mean the same people.',
      '<strong>A badly built A/B test is weak evidence,</strong> and a well-run interview can be strong. The method sets the ceiling, not the result.']) +
  callout('An experiment library', '<em>The Real Startup Book</em>, free under Creative Commons, lists evaluative experiments with when to use each: dashboards, product-market fit surveys, paper and clickable prototypes, single-feature products, usability tests and Wizard of Oz.') +
  see(('ab-strategies', 'A/B Test Strategies That Work'), ('ab-mislead', 'Another Way A/B Tests Mislead'), ('fake-ai', 'The Dangerous Appeal of Fake AI Users'), ('d-outcomes', 'Outcomes, Not Outputs')) +
  sources(SRC['cdh'], SRC['start'], SRC['amap'], SRC['exp'], SRC['rsb'], SRC['svpg']),
  'Test the belief that would sink the idea, with the cheapest test that could prove it wrong.'))

# 6 ---------------------------------------------------------------------------
chapters.append(article('d-strategy', 'Discovery', 'Strategy You Can Test',
  'Diagnosis, guiding policy, coherent actions',
  link('https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-perils-of-bad-strategy', 'Richard Rumelt, McKinsey Quarterly ↗'),
  'A strategy names the core challenge, chooses an approach to it, and commits to actions that support each other. Bad strategy is fluff, goals dressed as strategy, problems left unnamed, or objectives nobody can reach. For product teams, the outcome and the opportunity tree are where strategy becomes testable.',
  '<p>Strategy is coherent action backed by an argument. Many “strategies” are lists of ambitions with no argument for how the obstacle will be beaten.</p>' +
  flow('The kernel of a strategy', [
      ('Diagnosis', 'What is the critical challenge? It simplifies the situation enough to act on.'),
      ('Guiding policy', 'The overall approach to that challenge. It rules many options out.'),
      ('Coherent actions', 'Concrete steps and resources that support the policy and each other.')],
    'A strategy missing any of the three is a wish, a slogan or a to-do list.') +
  '<h4>Four signs of bad strategy</h4>' +
  table(['Sign', 'Looks like', 'Example from the article'], [
    ['Fluff', 'Buzzwords that restate the obvious', 'A bank’s “customer-centric intermediation”, which means being a bank'],
    ['Not facing the problem', 'No named challenge, so nothing can be judged', 'A plan that ignored the inefficient plants and labour relations behind the decline'],
    ['Goals as strategy', 'A target with no plan to reach it', 'A “20/20 plan”: 20% growth and 20% margins'],
    ['Bad objectives', 'A sprawling list, or aims with no route', 'One city’s plan: 47 strategies and 178 action items']]) +
  '<h4>What good looks like</h4>'
  '<p>Nvidia diagnosed that it was losing the performance race. Its policy was to release faster chips at about three times the industry pace. Its actions fitted together: overlapping development teams, heavy simulation, and taking back control of its drivers.</p>'
  '<h4>Questions to ask of any roadmap</h4>' +
  ul(['What is the diagnosis? Which obstacle does this plan deal with?',
      'Which options does the guiding policy rule out? If none, it isn’t a policy.',
      'Do the actions reinforce each other, or compete for the same people?',
      'Which outcome will tell us it’s working, and when will we look?']) +
  callout('Why bad strategy persists', 'Choosing is hard, so plans keep every option. And filling in vision, mission and values templates produces rhetoric rather than a diagnosis.') +
  see(('d-outcomes', 'Outcomes, Not Outputs'), ('d-ost', 'Opportunity Solution Trees'), ('leader-traps', 'Four Traps That Block UX Leaders')) +
  sources(SRC['rumelt']),
  'A goal is not a strategy. Name the obstacle, choose how to beat it, act coherently.'))

NEW = [('d-discovery-loop', 'Continuous Discovery in One Page', 'Weekly customer contact, by the people who build the product', 'Talk to customers every week, as a trio, about one outcome.'),
       ('d-outcomes', 'Outcomes, Not Outputs', 'Getting out of the build trap', 'Ship to move an outcome. A feature is a bet, not a result.'),
       ('d-interviews', 'Story-Based Interviews', 'Ask about the last time, not about the future', 'Collect stories about the last time. Opinions about the future aren’t data.'),
       ('d-ost', 'Opportunity Solution Trees', 'Map what you heard before choosing what to build', 'Map the problem space before you pick a solution. Compare three ideas, not one.'),
       ('d-assumptions', 'Assumption Mapping and Testing', 'Test the riskiest belief, as cheaply as the risk allows', 'Test the belief that would sink the idea, with the cheapest test that could prove it wrong.'),
       ('d-strategy', 'Strategy You Can Test', 'Diagnosis, guiding policy, coherent actions', 'A goal is not a strategy. Name the obstacle, choose how to beat it, act coherently.')]

if 'id="part-vi"' in s:
    print('Part VI already present'); raise SystemExit

# chapters + divider before the archive guide
divider = '''
<!-- Part VI -->
<div class="chapter-divider companion-divider" id="part-vi">
  <p class="chapter-number">Part VI</p>
  <h2>Discovery and the Product Craft</h2>
  <p>From other sources. Continuous product discovery first; the product-design craft follows. Each chapter credits its sources and links to the earlier chapters it builds on.</p>
</div>
'''
anchor = '\n<!-- Archive guide -->'
assert s.count(anchor) == 1
s = s.replace(anchor, divider + ''.join(chapters) + anchor, 1)

# TOC
toc = '\n  <div class="toc-part">\n    <p class="toc-part-title">Part VI — Discovery and the Product Craft</p>\n'
for i, (id_, t, sub, _) in enumerate(NEW, start=105):
    toc += '    <a href="#%s" class="toc-entry"><span class="toc-entry-title">%s <span class="toc-new">New</span> <span class="toc-entry-sub">— %s</span></span><span class="toc-num">%d</span></a>\n' % (id_, t, sub, i)
toc += '  </div>\n'
m = re.search(r'(<a href="#c-hidden-disabled" class="toc-entry">.*?</a>\n  </div>\n)', s, re.S)
assert m
s = s[:m.end()] + toc + s[m.end():]

# rail
ra = '<li><a href="#appendix">'
assert s.count(ra) == 1
s = s.replace(ra, '<li><a href="#part-vi"><span class="rm"><i></i></span><span>Part VI. Discovery and craft</span></a></li>' + ra)

# rules
rp = '<div class="rules-part"><p class="rules-part-title">Appendix — Archive Guide</p>'
assert s.count(rp) == 1
rules = '<div class="rules-part"><p class="rules-part-title">Part VI — Discovery and the Product Craft</p><ol>' + ''.join(
    '<li><a href="#%s">%s</a> <span class="rules-src">%s</span></li>' % (i, r, t) for i, t, _, r in NEW) + '</ol></div>'
s = s.replace(rp, rules + rp)

# cover strip: a new group of marks, all new
m = re.search(r'(<div class="corpus" aria-hidden="true">.*?)(</div>)', s, re.S)
s = s[:m.start(2)] + '<span class="grp">' + '<i class="new"></i>' * len(NEW) + '</span>' + s[m.start(2):]
s = s.replace('<b>41 of 104 are new in this edition</b>', '<b>47 of 110 are new in this edition</b>')
s = s.replace('104 chapters: 91 distilled from Trevor Calabro’s newsletter (all 182 posts, 2023–2026, were read) and 13 companion notes from other authors',
              '110 chapters: 91 distilled from Trevor Calabro’s newsletter (all 182 posts, 2023–2026, were read), 13 companion notes and 6 discovery chapters from other authors')
s = s.replace('13 companion notes draw on Erika Hall,', '13 companion notes and the Part VI chapters draw on Teresa Torres, Marty Cagan, Melissa Perri, Richard Rumelt, Giff Constable, Strategyzer, Erika Hall,')
fp = '<p style="margin-top:8px">Part V companion notes draw on'
assert s.count(fp) == 1
s = s.replace(fp, '<p style="margin-top:8px">Part VI draws on Teresa Torres’s <em>Continuous Discovery Habits</em> and Product Talk, Marty Cagan (SVPG), Melissa Perri, Richard Rumelt, Giff Constable, Rob Fitzpatrick, Strategyzer and <em>The Real Startup Book</em>, credited on each page.</p>\n  ' + fp)

# see-also lines in existing chapters (before their remember box)
def add_see(aid, html):
    global s
    a = s.index('id="%s"' % aid); e = s.index('</article>', a)
    k = s.rfind('<div class="remember-box">', a, e)
    pos = k if k > 0 else e
    s = s[:pos] + html + '\n  ' + s[pos:]
add_see('interview-questions', see(('d-interviews', 'Story-Based Interviews')))
add_see('c-three-books', see(('d-discovery-loop', 'Continuous Discovery in One Page'), ('d-ost', 'Opportunity Solution Trees')))
add_see('c-tars', see(('d-outcomes', 'Outcomes, Not Outputs')))
add_see('c-b2b-research', see(('d-interviews', 'Story-Based Interviews'), ('d-assumptions', 'Assumption Mapping and Testing')))

p.write_text(s, encoding='utf-8')
print('added', len(NEW), 'chapters')
