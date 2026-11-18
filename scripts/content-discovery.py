#!/usr/bin/env python3
"""Write the Continuous Discovery module (6 articles) and add it to the manifest. Idempotent.
The correct option is always listed first; the app shuffles options at runtime."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent

def q(question, right, wrong, explain):
    return {"type": "single", "q": question, "options": [right] + wrong, "answer": 0, "explain": explain}
def card(title, text, tq):
    return {"title": title, "text": text, "try": tq}

A = []

A.append(dict(id='d-discovery-loop', title='Continuous Discovery in One Page', icon='🔁',
  summary='Weekly customer contact by the product trio, in a loop from outcome to assumption tests.',
  source='https://www.producttalk.org/getting-started-with-discovery.md',
  intro='The team that builds the product talks to customers every week, together, aimed at one outcome.',
  learn=[
    card('What makes it continuous', 'Project research happens before a big decision and then stops.\n\n**Continuous discovery:** the team building the product has a customer touchpoint **at least every week**, in small activities aimed at one outcome.\n\nEvery decision keeps meeting fresh evidence.',
      q('What is the minimum cadence of customer contact?', 'Every week', ['Every sprint review', 'Before each release', 'Once a quarter'], 'Weekly is the floor, not the target.')),
    card('The product trio', 'A **product manager, a designer and an engineer** interview together.\n\nWhen all three hear the same stories, they argue less about whose information is right and more about what to do.',
      q('Why should the trio interview together?', 'They build a shared view from the same stories', ['It cuts the number of interviews needed', 'Engineers can answer technical questions live', 'Customers trust a bigger group more'], 'Shared evidence reduces arguments based on different information.')),
    card('The loop', '**Outcome** → **opportunities** heard in stories → about three **solutions** for one target → **assumption tests**.\n\nTest results send you back to the opportunity map, not straight to the backlog.',
      q('Where do assumption-test results go?', 'Back into the opportunity map', ['Straight into the delivery backlog', 'Into a quarterly research report', 'Into the next outcome target'], 'The loop closes on the map, which keeps the next choice informed.')),
    card('Habits to start with', '**Automate recruiting**, so next week’s interview is already booked.\n**Write a one-page snapshot** after each interview and share it.\n**Refresh the map** every three to four interviews.\n**Story-map an idea** to list its assumptions: 20 to 30 minutes.',
      q('What keeps weekly interviews from stalling?', 'Recruiting that runs on its own', ['A longer interview script', 'A dedicated research team', 'Interviewing only power users'], 'If recruiting is manual, the habit dies the first busy week.')),
    card('Where to start', '**Feature factory:** story-map one planned feature and list its hidden assumptions.\n**Messy middle:** make one bright spot: the trio interviews together.\n**Sliding back under pressure:** share snapshots and the map after every interview.',
      q('Stakeholders under pressure are asking for specific features again. First step?', 'Share a snapshot after every interview', ['Pause discovery until things calm down', 'Build the requested features first', 'Run a large survey to settle it'], 'Showing your work rebuilds trust in the evidence.')),
  ],
  test=[
    q('Which statement describes continuous discovery?', 'Small research activities every week, aimed at one outcome', ['A research phase before each new project', 'A quarterly study run by a research team', 'Customer feedback collected after each release'], 'It runs alongside delivery, not before it.'),
    q('Who is in the product trio?', 'Product manager, designer, engineer', ['Researcher, designer, data analyst', 'Product manager, sales lead, designer', 'Designer, engineer, customer success'], 'The people who decide and build the product.'),
    q('What is the order of the discovery loop?', 'Outcome, opportunities, solutions, tests', ['Solutions, tests, outcome, opportunities', 'Opportunities, outcome, tests, solutions', 'Tests, solutions, opportunities, outcome'], 'Start from the outcome; solutions come only after a target opportunity.'),
    q('How often should the opportunity map be refreshed?', 'Every three to four interviews', ['After every single interview', 'Once a quarter, with planning', 'Only when the outcome changes'], 'Often enough to stay current without chasing every story.'),
    q('A team works from a fixed roadmap and counts features shipped. Best first step?', 'Story-map one feature and list its assumptions', ['Rewrite the whole roadmap as outcomes', 'Hire a researcher before changing anything', 'Stop shipping until interviews start'], 'It needs no permission and shows the risk in the plan.'),
    q('How long does story-mapping an idea’s assumptions take?', 'About 20 to 30 minutes', ['About half a day', 'One full sprint', 'Two or three days'], 'Short enough to do for every idea.'),
  ]))

A.append(dict(id='d-outcomes', title='Outcomes, Not Outputs', icon='🎯',
  summary='Why counting features shipped traps teams, and which metric discovery should aim at.',
  source='https://svpg.com/product-risk-taxonomies',
  intro='Outputs are what you ship. Outcomes are what changes because of it.',
  learn=[
    card('The build trap', 'Teams measured on **features shipped** keep shipping and stop checking whether anything changed.\n\nA product has no value on its own. Value is what it does for customers; the business gains only when that happens.',
      q('Which of these is an outcome?', 'More teams finish setup in week one', ['Ten features shipped this quarter', 'Every roadmap date met on time', 'Story points closed per sprint'], 'It describes a change in customer behaviour.')),
    card('Three kinds of metric', '**Business outcome:** revenue, retention. Too far away for one team.\n**Product outcome:** customer behaviour in the product. **The best fit for discovery.**\n**Traction metric:** use of one feature. Narrows the solutions to one.',
      q('Which metric suits a discovery team best?', 'A product outcome', ['A business outcome', 'A traction metric', 'A delivery velocity metric'], 'The team can move it, and many solutions could.')),
    card('From strategy to the team', '**Strategic intent:** a few goals for one to two years.\n**Product initiatives:** customer problems to solve.\n**Options:** solutions, treated as bets.\n\nLeaders set the why. Teams own the how.',
      q('In this cascade, what are solutions treated as?', 'Bets', ['Commitments', 'Requirements', 'Milestones'], 'A solution is a bet that it will move the outcome.')),
    card('Four risks', '**Value:** will they choose it?\n**Usability:** can they use it?\n**Feasibility:** can we build it?\n**Viability:** does it work for the business, including legal and ethics?\n\nCheck them before building.',
      q('“Does it break our pricing or compliance rules?” Which risk is that?', 'Viability', ['Value', 'Usability', 'Feasibility'], 'Viability covers whether the business can support it.')),
  ],
  test=[
    q('What is the build trap?', 'Judging success by features shipped', ['Building before the design is final', 'Shipping too slowly to compete', 'Letting engineers choose the roadmap'], 'Outputs become the goal instead of the change they should cause.'),
    q('Which is a traction metric?', 'Weekly uses of the export button', ['Annual recurring revenue', 'Teams active after 30 days', 'Support cost per customer'], 'It tracks one feature, which suits optimising that feature.'),
    q('Why is a business outcome a poor discovery goal?', 'Too many teams and forces move it', ['It cannot be measured precisely', 'Leaders rarely care about it', 'It changes every single week'], 'A team can’t see its own effect on it.'),
    q('Someone asks for a feature. What should you ask first?', 'Which outcome it should move', ['How soon they need it', 'Which competitor has it', 'How many engineers it needs'], 'If nobody can say, it is an output looking for a reason.'),
    q('Who is usually best placed to judge feasibility?', 'Engineers', ['Customers', 'Sales', 'Leadership'], 'They know the time, skills and technology available.'),
    q('What should leaders set in outcome-led work?', 'The intent and the why', ['The features and the dates', 'The designs and the copy', 'The sprint plan and estimates'], 'Teams own how to reach it.'),
  ]))

A.append(dict(id='d-interviews', title='Story-Based Interviews', icon='🗣️',
  summary='Ask about the last time, dig out the story, and spot compliments and promises as bad data.',
  source='https://www.producttalk.org/sourcing-opportunities.md',
  intro='Ask for one specific, recent story. Opinions about the future aren’t data.',
  learn=[
    card('Why stories', '“Would you use this?” invites a guess.\n“Tell me about the last time you…” brings back what happened.\n\nThe details of a real story make the who, what, why and how trustworthy.',
      q('Which question collects a story?', 'Tell me about the last time you exported a report', ['Would you use a faster export?', 'How often do you usually export?', 'What would your ideal export look like?'], 'It anchors the answer in one real event.')),
    card('Dig it out', '**Set the scene:** when, where, what happened just before.\n**Keep them in the moment;** ask what happened next.\n**Bring generalisations back:** “I usually…” → “And last time?”\n**Don’t stop at a short answer.**',
      q('They say “I usually check it every morning.” Best follow-up?', 'And the last time you checked it, what happened?', ['Why do you check it every morning?', 'Would you like a daily summary instead?', 'How long does that usually take you?'], 'Return to one specific instance.')),
    card('Three kinds of bad data', '**Compliments:** “That’s really cool.”\n**Generalisations and promises:** “I always…”, “I would definitely buy that.”\n**Feature requests:** “You should add…”\n\nEach is a prompt to dig, not evidence.',
      q('“I would definitely buy that.” What is it?', 'A future promise, the least reliable data', ['Strong evidence of demand', 'A sign to start building', 'A useful price signal'], 'Ask what they do today and what it costs them.')),
    card('Commitment', 'When you’re testing demand, interest shows as something given up:\n**time** (a trial, another meeting), **reputation** (an introduction), **money** (a pre-order).\n\nCompliments and no next step taught you little.',
      q('Which response shows real interest?', 'They introduce you to their manager', ['They say the idea is brilliant', 'They promise to try it someday', 'They ask for more features'], 'An introduction costs them reputation.')),
    card('Make it weekly', '**Recruit automatically:** an in-product invite, a line in onboarding.\n**Interview as a trio.**\n**Write a snapshot within the hour:** a quote, quick facts, the story’s moments, the opportunities heard.',
      q('What goes in an interview snapshot?', 'A quote, the story’s moments, the opportunities', ['A transcript of the whole interview', 'A feature list for the roadmap', 'A score for the participant'], 'One page, written while the story is fresh.')),
  ],
  test=[
    q('Why ask about the past rather than the future?', 'People can’t predict what they’ll do', ['Past questions are quicker to answer', 'Future questions upset participants', 'Past behaviour is easier to quantify'], 'Predictions are guesses; stories are facts.'),
    q('Instead of “How much would you pay?”, ask:', 'What did this problem cost you last month?', ['Would you pay a monthly fee for it?', 'Is our price higher than you expected?', 'Which price tier would you choose?'], 'Real costs reveal what solving it is worth.'),
    q('A participant suggests a feature. What next?', 'Ask why they want it and what they do now', ['Add it to the backlog with their name', 'Explain why it can’t be built', 'Ask them to rank it against others'], 'The need underneath is the opportunity.'),
    q('Which is a commitment of money?', 'A pre-order', ['A positive review', 'A second interview', 'An introduction to a colleague'], 'Money, time and reputation are the three kinds.'),
    q('What is the classic interviewer mistake?', 'Selling when you should be listening', ['Asking too many follow-up questions', 'Taking notes during the interview', 'Interviewing with a colleague'], 'If you hear yourself explaining the product, switch back to their story.'),
    q('When should the snapshot be written?', 'Within the hour', ['At the end of the week', 'After all interviews are done', 'Before the next planning cycle'], 'Details fade fast.'),
  ]))

A.append(dict(id='d-ost', title='Opportunity Solution Trees', icon='🌳',
  summary='Map opportunities from interviews under an outcome, choose one target, then compare solutions.',
  source='https://www.producttalk.org/opportunity-solution-trees.md',
  intro='Map what you heard before choosing what to build.',
  learn=[
    card('The structure', '**Outcome** at the top.\n**Opportunities** below it: needs, pain points and desires from interviews.\n**Solutions** only under the target opportunity.\n**Assumption tests** under each solution.',
      q('Where do solutions go on the tree?', 'Only under the target opportunity', ['Directly under the outcome', 'Under every opportunity', 'Beside the assumption tests'], 'Brainstorming across the whole tree spreads the team thin.')),
    card('Disguised solutions', 'An opportunity can be addressed in **more than one way**. If there’s only one way, it’s a solution.\n\n“I need a calendar export” → a solution.\n“I need to see my schedule outside the app” → an opportunity.\n\nAsk “why?” to find what’s underneath.',
      q('Which is an opportunity, not a solution?', 'I lose track of deadlines across projects', ['I need a Gantt chart view', 'Add email reminders for deadlines', 'Give me a deadline widget'], 'It can be solved many ways.')),
    card('Parents, children, siblings', 'A **child is part of its parent.** Ask “what are other reasons why…?”\n**Siblings are distinct:** you can address one without the others.\n“Watch on a flight” and “watch on a train” share the parent “watch on the go”.',
      q('Why are “watch on a flight” and “watch on a train” siblings?', 'Their constraints differ under one parent', ['They are the same opportunity', 'One is a solution to the other', 'They belong to different outcomes'], 'Offline viewing matters on planes; trains may have data.')),
    card('Choose a target', '**Size:** how many, how often.\n**Market position:** catch up or stand out.\n**Strategic fit.**\n**Customer importance** and satisfaction today.\n\n**Leave effort out.** Compare one row at a time. It’s a two-way door.',
      q('Which factor should you leave out when choosing a target?', 'Effort to build', ['How many customers it affects', 'Fit with company strategy', 'How much customers care'], 'Feasibility is tested later; judging it now rules out good options.')),
    card('Keep it alive', 'Before the first tree: a clear outcome and **three or four story interviews.**\nRevisit **every 3–4 interviews.**\nStill messy after **6–8**? Check how you interview.\nNew tree only when the outcome **changes direction.**',
      q('When do you start a new tree?', 'When the outcome changes direction', ['When the target number changes', 'Every quarter, with planning', 'After every eight interviews'], 'A new number for the same outcome keeps the same tree.')),
  ],
  test=[
    q('Where should opportunities come from?', 'Story-based customer interviews', ['The team’s brainstorm', 'The support ticket queue alone', 'Competitor feature lists'], 'Tickets and analytics suggest what to ask about; they aren’t opportunities on their own.'),
    q('How many solutions should you compare for a target?', 'About three', ['Just one, done well', 'As many as possible', 'Exactly two, A versus B'], 'Comparing stops the team defending its first idea.'),
    q('Why avoid scoring formulas for opportunities?', 'Numbers make judgements look like facts', ['They take too long to calculate', 'Stakeholders find them confusing', 'They favour small opportunities'], 'It discourages revisiting a wrong call.'),
    q('How should opportunities be compared?', 'One row of the tree at a time', ['All of them in one ranked list', 'By the number of requests', 'By how quickly they can ship'], 'Compare like with like, then go deeper within the winner.'),
    q('Which is a common tree mistake?', 'One tree for the whole company', ['A tree with only one outcome', 'Revisiting it every few interviews', 'Keeping effort out of targeting'], 'A company-wide view needs a KPI tree or an experience map instead.'),
    q('What is needed before the first tree?', 'An outcome and three or four story interviews', ['A full research report', 'A prioritised feature backlog', 'Approval from every stakeholder'], 'Without stories, the opportunities are invented.'),
  ]))

A.append(dict(id='d-assumptions', title='Assumption Mapping and Testing', icon='🧪',
  summary='List what must be true, test the important unevidenced beliefs first, and prefer evidence of behaviour.',
  source='https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter',
  intro='Test the belief that would sink the idea, with the cheapest test that could prove it wrong.',
  learn=[
    card('Find the assumptions', 'Story-map the idea as if it already existed: each step the customer takes, and under it **what must be true.**\n\nWrite each as **“We believe that…”**',
      q('Why write assumptions as “We believe that…”?', 'It keeps the team open to being wrong', ['It makes them easier to measure', 'Stakeholders expect that format', 'It turns them into requirements'], 'A belief invites a test; a statement invites a defence.')),
    card('Five types', '**Desirability:** do they want it?\n**Usability:** can they use it?\n**Feasibility:** can we build it?\n**Viability:** does it work for the business?\n**Ethics:** could it harm anyone?',
      q('“Reminders won’t pressure people who said no.” Which type?', 'Ethics', ['Desirability', 'Usability', 'Viability'], 'It asks whether the idea could cause harm.')),
    card('Importance × evidence', 'Place each assumption on two questions:\n**If it’s wrong, does the idea fail?**\n**Do we have observed evidence?**\n\nTest the **important, unevidenced** corner first.',
      q('Which assumption do you test first?', 'Important, with no evidence', ['Minor, with no evidence', 'Important, with strong evidence', 'Minor, with some evidence'], 'If it’s wrong, the idea fails and you wouldn’t know.')),
    card('Evidence strength', '**Weaker:** what people say (interviews, surveys).\n**Stronger:** what people do (prototype tests, fake doors, A/B tests).\n**Strongest:** what they give up (effortful sign-ups, pre-orders).\n\nStart cheap, then move up as the signal improves.',
      q('Which gives the strongest evidence?', 'A paid pilot', ['A survey of intent', 'A customer interview', 'A focus group'], 'Giving something up is the clearest signal.')),
    card('Run it well', '**Change one thing at a time.**\n**Write the pass line before the test.**\n**Define who you test with.**\n\nA badly built A/B test is weak evidence; a well-run interview can be strong.',
      q('When should the pass line be written?', 'Before the test runs', ['After seeing the first results', 'When the test is half done', 'Only if results are unclear'], 'Otherwise the result can be argued either way.')),
  ],
  test=[
    q('How long does story-mapping assumptions take?', 'About 20 to 30 minutes', ['About one full day', 'Roughly one sprint', 'Two hours per step'], 'Cheap enough to do for every idea.'),
    q('“Admins want colleagues to join in week one.” Which type?', 'Desirability', ['Feasibility', 'Viability', 'Usability'], 'It’s about whether they want it.'),
    q('What counts as evidence on the evidence axis?', 'Something observed', ['The most senior opinion', 'The loudest argument', 'A confident estimate'], 'Not who argues loudest.'),
    q('Why start with cheap, weaker tests?', 'They kill bad ideas before costly tests', ['Strong tests are always unreliable', 'Stakeholders prefer cheap tests', 'Weak tests give final answers'], 'Move to stronger tests as the signal improves.'),
    q('Why change only one thing per test?', 'Extra variables make results unreadable', ['It makes the test shorter', 'Participants prefer simple tests', 'Tools allow only one variable'], 'You can’t tell which change caused the result.'),
    q('Which free book lists evaluative experiments?', 'The Real Startup Book', ['The Mom Test', 'Escaping the Build Trap', 'Good Strategy / Bad Strategy'], 'It’s Creative Commons and lists when to use each experiment.'),
  ]))

A.append(dict(id='d-strategy', title='Strategy You Can Test', icon='♟️',
  summary='Diagnosis, guiding policy, coherent actions, and four signs of bad strategy.',
  source='https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-perils-of-bad-strategy',
  intro='A goal is not a strategy. Name the obstacle, choose how to beat it, act coherently.',
  learn=[
    card('The kernel', '**Diagnosis:** the critical challenge.\n**Guiding policy:** the overall approach. It rules options out.\n**Coherent actions:** steps and resources that support each other.\n\nMissing one, it’s a wish, a slogan or a to-do list.',
      q('What does a guiding policy do?', 'Rules many options out', ['Lists every planned feature', 'Sets the revenue target', 'Assigns work to each team'], 'A policy that rules nothing out isn’t a policy.')),
    card('Four signs of bad strategy', '**Fluff:** buzzwords restating the obvious.\n**Not facing the problem:** no named challenge.\n**Goals as strategy:** a target with no route.\n**Bad objectives:** sprawling lists or unreachable aims.',
      q('“20% growth and 20% margins.” Which sign?', 'A goal dressed as strategy', ['Fluff', 'A guiding policy', 'A coherent action'], 'It says where, not how.')),
    card('A good example', 'A chip maker diagnosed it was **losing the performance race.**\nPolicy: release faster chips at about **three times** the industry pace.\nActions: overlapping teams, heavy simulation, control of its drivers.',
      q('Why do those actions count as coherent?', 'They all serve the same policy', ['They were cheap to fund', 'Each team chose its own', 'They were planned quarterly'], 'Actions that reinforce each other.')),
    card('Ask it of any roadmap', 'What is the diagnosis?\nWhich options does the policy rule out?\nDo the actions reinforce each other?\nWhich outcome tells us it’s working, and when do we look?',
      q('A roadmap rules out nothing. What does that suggest?', 'There is no real guiding policy', ['The strategy is very flexible', 'The team is well aligned', 'The goals are ambitious'], 'Choosing means saying no.')),
  ],
  test=[
    q('What are the three parts of the kernel?', 'Diagnosis, guiding policy, coherent actions', ['Vision, mission, values', 'Goals, metrics, deadlines', 'Strengths, weaknesses, threats'], 'Templates of vision and values produce rhetoric, not a diagnosis.'),
    q('“Customer-centric intermediation” is an example of:', 'Fluff', ['A guiding policy', 'A diagnosis', 'A coherent action'], 'Stripped down, it means being a bank.'),
    q('A city plan had 47 strategies and 178 actions. Which sign?', 'Bad objectives', ['Fluff', 'A sharp diagnosis', 'Coherent action'], 'A sprawling list isn’t a choice.'),
    q('Why does bad strategy persist?', 'Choosing is hard, so plans keep every option', ['Good strategy is too expensive', 'Leaders lack the data needed', 'Teams resist all planning'], 'Avoiding a choice feels safer than making one.'),
    q('Where does strategy become testable for a product team?', 'In its outcome and opportunity tree', ['In the annual budget', 'In the brand guidelines', 'In the release notes'], 'The outcome says what should change; the tree shows the bets.'),
    q('What is a strategy, in one line?', 'Coherent action backed by an argument', ['An ambitious target for the year', 'A list of planned initiatives', 'A statement of company values'], 'It must explain how the obstacle will be beaten.'),
  ]))

module = {"id": "discovery", "name": "Continuous Discovery", "icon": "🔁", "week": "Module 13",
          "subtitle": "Weekly customer contact, opportunity trees and assumption tests", "open": True, "articles": []}
for a in A:
    art = {"id": a['id'], "module": "discovery", "title": a['title'], "icon": a['icon'], "intro": a['intro'],
           "topics": [{"id": "main", "title": a['title'], "learn": a['learn'], "test": a['test']}]}
    (root / 'content' / (a['id'] + '.json')).write_text(json.dumps(art, ensure_ascii=False, indent=1), encoding='utf-8')
    module['articles'].append({"id": a['id'], "title": a['title'], "icon": a['icon'], "summary": a['summary'],
                               "file": "content/%s.json" % a['id'], "source": a['source'], "q": len(a['test'])})

mp = root / 'content' / 'manifest.json'
m = json.loads(mp.read_text(encoding='utf-8'))
m['modules'] = [x for x in m['modules'] if x['id'] != 'discovery'] + [module]
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('wrote', len(A), 'articles')

# ---- rebalance: make sure the right answer isn't simply the longest or shortest option ----
FIX = {
 'Why write assumptions as “We believe that…”?': {'It makes them easier to measure': 'It makes every assumption easier to measure later'},
 'Why start with cheap, weaker tests?': {'Stakeholders prefer cheap tests': 'Stakeholders always prefer the cheapest test available'},
 'Why change only one thing per test?': {'Participants prefer simple tests': 'Participants find tests with one change easier to follow'},
 'Why should the trio interview together?': {'Engineers can answer technical questions live': 'Engineers can answer the technical questions live during the call'},
 'What keeps weekly interviews from stalling?': {'A dedicated research team': 'A dedicated research team that books everything'},
 'Which statement describes continuous discovery?': {'Customer feedback collected after each release': 'Customer feedback collected and reviewed after each major release'},
 'How often should the opportunity map be refreshed?': {'Once a quarter, with planning': 'Once a quarter, together with roadmap planning'},
 'A team works from a fixed roadmap and counts features shipped. Best first step?': {'Hire a researcher before changing anything': 'Hire a dedicated researcher before changing anything else'},
 'How long does story-mapping an idea’s assumptions take?': {'Two or three days': 'Two or three full working days'},
 'How long does story-mapping assumptions take?': {'Two hours per step': 'Around two hours for every step in the map'},
 'Which question collects a story?': {'What would your ideal export look like?': 'What would your ideal export look like if you could design it?'},
 'They say “I usually check it every morning.” Best follow-up?': {'Would you like a daily summary instead?': 'Would you like us to send you a daily summary instead of that?'},
 '“I would definitely buy that.” What is it?': {'Strong evidence of demand': 'Strong evidence of demand you can plan the roadmap around'},
 'Which response shows real interest?': {'They promise to try it someday': 'They promise to try it as soon as it launches someday'},
 'What goes in an interview snapshot?': {'A transcript of the whole interview': 'A full transcript of the whole interview, word for word'},
 'Instead of “How much would you pay?”, ask:': {'Is our price higher than you expected?': 'Is our planned price higher or lower than you expected it to be?'},
 'A participant suggests a feature. What next?': {'Add it to the backlog with their name': 'Add it to the backlog straight away, with their name attached'},
 'Which is a commitment of money?': {'A pre-order': 'A pre-order paid in advance'},
 'What is the classic interviewer mistake?': {'Taking notes during the interview': 'Taking detailed notes during the interview itself'},
 'Where do solutions go on the tree?': {'Under every opportunity': 'Under every opportunity, so nothing is missed'},
 'Which is an opportunity, not a solution?': {'Add email reminders for deadlines': 'Add email reminders for every upcoming project deadline'},
 'Why are “watch on a flight” and “watch on a train” siblings?': {'They belong to different outcomes': 'They belong to two different outcomes on separate trees'},
 'When do you start a new tree?': {'Every quarter, with planning': 'Every quarter, together with the planning cycle'},
 'Where should opportunities come from?': {'The support ticket queue alone': 'The support ticket queue on its own, sorted by volume'},
 'How many solutions should you compare for a target?': {'Just one, done well': 'Just one', 'As many as possible': 'Ten or more', 'Exactly two, A versus B': 'Two, A vs B'},
 'Why avoid scoring formulas for opportunities?': {'They take too long to calculate': 'They take far too long to calculate for every opportunity'},
 'What is needed before the first tree?': {'Approval from every stakeholder': 'Formal approval from every stakeholder involved in the product'},
 'Which of these is an outcome?': {'Every roadmap date met on time': 'Every single roadmap date met on time this year'},
 'In this cascade, what are solutions treated as?': {'Bets': 'Bets on moving the outcome', 'Commitments': 'Fixed commitments', 'Requirements': 'Signed-off requirements', 'Milestones': 'Dated milestones'},
 'Which is a traction metric?': {'Teams active after 30 days': 'Share of teams still active 30 days after signing up'},
 'Why is a business outcome a poor discovery goal?': {'It cannot be measured precisely': 'It cannot be measured precisely enough to be useful'},
 'Someone asks for a feature. What should you ask first?': {'How many engineers it needs': 'How many engineers it will need to build it'},
 '“20% growth and 20% margins.” Which sign?': {'Fluff': 'Fluff and buzzwords', 'A guiding policy': 'A clear guiding policy', 'A coherent action': 'A set of coherent actions'},
 'Why do those actions count as coherent?': {'They were planned quarterly': 'They were planned together in quarterly reviews'},
 'A roadmap rules out nothing. What does that suggest?': {'The strategy is very flexible': 'The strategy is very flexible and ready for change'},
 'What are the three parts of the kernel?': {'Strengths, weaknesses, threats': 'Strengths, weaknesses, opportunities, threats'},
 '“Customer-centric intermediation” is an example of:': {'Fluff': 'Fluff', 'A guiding policy': 'A policy', 'A diagnosis': 'A diagnosis', 'A coherent action': 'An action'},
 'Why does bad strategy persist?': {'Good strategy is too expensive': 'Good strategy is too expensive for most companies to produce'},
 'Where does strategy become testable for a product team?': {'In the annual budget': 'In the annual budget and its quarterly forecasts'},
 'What is a strategy, in one line?': {'A list of planned initiatives': 'A list of the planned initiatives for the year ahead'},
}
import glob
used = set()
for f in glob.glob(str(root / 'content' / 'd-*.json')):
    art = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    for t in art['topics']:
        for qq in [c['try'] for c in t['learn']] + t['test']:
            if qq['q'] in FIX:
                used.add(qq['q'])
                qq['options'] = [FIX[qq['q']].get(o, o) for o in qq['options']]
    pathlib.Path(f).write_text(json.dumps(art, ensure_ascii=False, indent=1), encoding='utf-8')
missing = set(FIX) - used
assert not missing, missing
print('rebalanced', len(used))
