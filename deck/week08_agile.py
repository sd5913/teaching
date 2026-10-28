"""Agile/Scrum concepts and GitHub tracking for the group-project execution mark."""
from deckgen import Rect, T, INK, WHITE, PAPER, MUTED, LINE, BLUE, ORANGE, TEAL
from deckgen.layouts import content
from week08_visuals import canvas

MANIFESTO = 'https://agilemanifesto.org/'
PRINCIPLES = 'https://agilemanifesto.org/principles.html'
SCRUM = 'https://scrumguides.org/scrum-guide.html'
PROJECTS = 'https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects'
TEAM_TEMPLATE = 'https://github.com/orgs/sd5913/projects/1'


def manifesto():
    slide = canvas('AGILE / WEEK 1 REVISITED / 2001', 'The Agile Manifesto: four values',
        'Briefly recall the Week 1 craft slide, then apply its four values to a game/app team. '
        'These are preferences, not bans on tools, documentation, agreements or plans. '
        'Example: a playable prototype and a player observation can change the next task, '
        'while a README still helps another person run the prototype. '
        f'Four values quoted from {MANIFESTO}; the twelve principles are at {PRINCIPLES}.')
    for index, (left, right) in enumerate([
        ('Individuals and interactions', 'processes and tools'),
        ('Working software', 'comprehensive documentation'),
        ('Customer collaboration', 'contract negotiation'),
        ('Responding to change', 'following a plan'),
    ]):
        y = 350 + index * 120
        slide.els += [
            Rect(120, y - 15, 1680, 105, PAPER),
            T(150, y, 790, 75, left, 'semibold', 44, INK),
            T(970, y, 110, 75, 'over', 'body', 40, MUTED),
            T(1120, y, 650, 75, right, 'body', 40, INK),
        ]
    slide.els += [
        T(120, 870, 1680, 65, 'Both sides have value; the items on the left are valued more.',
          'body', 40, INK),
        T(120, 950, 1680, 40, f'[Read the Manifesto and its principles]({MANIFESTO})',
          'body', 30, BLUE),
    ]
    return slide


def learning_loop():
    slide = canvas('AGILE / ITERATIVE + INCREMENTAL', 'Deliver, learn, adapt.',
        'Iterative development improves a solution through repeated feedback. Incremental '
        'development adds usable pieces that work together. For a game: first a playable '
        'movement loop, then a collectible, then feedback; observe players and revise. '
        'Frequent delivery and a sustainable pace matter; Agile does not mean waiting '
        'until the deadline to integrate. Scrum makes this empirical loop explicit through '
        'transparency, inspection and adaptation: visible work, checking evidence, changing '
        f'the plan. Sources: {PRINCIPLES} and {SCRUM}#scrum-theory.')
    slide.els.append(T(120, 315, 1680, 65,
        'Iterative: improve with feedback. Incremental: add usable pieces.', 'body', 40, INK))
    for i, (head, detail) in enumerate([
        ('Plan', 'Choose a goal'), ('Build + test', 'Make it usable'),
        ('Review', 'Inspect the result'), ('Adapt', 'Update the plan'),
    ]):
        x = 120 + i * 440
        slide.els += [
            Rect(x, 435, 360, 240, PAPER),
            T(x + 24, 470, 312, 80, head, 'xbold', 44, INK),
            T(x + 24, 575, 312, 95, detail, 'body', 40, INK),
        ]
        if i < 3:
            slide.els.append(T(x + 370, 510, 60, 80, '→', 'xbold', 56, ORANGE))
    slide.els += [
        Rect(1620, 675, 5, 115, ORANGE),
        Rect(300, 785, 1325, 5, ORANGE),
        Rect(300, 710, 5, 80, ORANGE),
        T(270, 665, 70, 80, '↑', 'xbold', 56, ORANGE),
        Rect(570, 750, 785, 75, WHITE),
        T(590, 760, 745, 65, 'Feedback informs the next plan', 'body', 40, INK, align='c'),
        T(120, 875, 1680, 65, 'Transparency → Inspection → Adaptation',
          'semibold', 44, INK),
    ]
    return slide


def accountabilities():
    slide = canvas('SCRUM / THREE ACCOUNTABILITIES', 'Who is accountable?',
        'The 2020 Scrum Guide calls these three accountabilities; roles is a useful familiar '
        'word, but there is one self-managing, cross-functional Scrum Team. Product Owner '
        'maximizes value and orders the Product Backlog. Developers create a usable Increment, '
        'plan their work and uphold the Definition of Done. Scrum Master establishes Scrum '
        'and helps the team become effective, including causing impediments to be removed. '
        'Developers can include design, art and testing work, not just typing code. '
        'For the course, make responsibilities clear; the execution mark assesses evidence '
        f'of how the team works rather than job titles. Source: {SCRUM}#scrum-team.')
    for x, head, a, b in [
        (120, 'Product Owner', 'Maximise value', 'Order the backlog'),
        (700, 'Developers', 'Plan, build and test', 'Create a usable Increment'),
        (1280, 'Scrum Master', 'Help the team improve', 'Address impediments'),
    ]:
        slide.els += [
            Rect(x, 370, 520, 420, PAPER),
            T(x + 28, 405, 464, 110, head, 'xbold', 48, INK),
            T(x + 28, 550, 464, 90, a, 'body', 42, INK),
            T(x + 28, 665, 464, 110, b, 'body', 40, INK),
        ]
    slide.els.append(T(120, 860, 1680, 85,
        'One team shares responsibility for a useful result.', 'body', 42, INK))
    return slide


def artifacts():
    slide = canvas('SCRUM / ARTIFACTS + COMMITMENTS', 'From a goal to a usable Increment',
        'Product Backlog: an evolving ordered list of work needed to improve the product; '
        'its commitment is the Product Goal. Sprint Backlog: Sprint Goal (why), selected '
        'Product Backlog items (what), and an actionable delivery plan (how); commitment: '
        'Sprint Goal. Increment: integrated, verified, usable work; commitment: Definition '
        'of Done, the shared quality standard. An unfinished collection of files is not '
        'a usable Increment. Multiple Increments may be delivered during one Sprint; '
        f'the Sprint Review is not a release gate. Source: {SCRUM}#scrum-artifacts.')
    for x, width, head in [(150, 430, 'Artifact'), (620, 660, 'What it contains'), (1320, 450, 'Commitment')]:
        slide.els.append(T(x, 325, width, 60, head, 'semibold', 40, MUTED))
    for y, artifact, detail, commitment in [
        (420, 'Product Backlog', 'Ordered work to\nimprove the product', 'Product Goal'),
        (590, 'Sprint Backlog', 'Goal + selected work\n+ delivery plan', 'Sprint Goal'),
        (760, 'Increment', 'Usable, integrated,\nverified work', 'Definition of Done'),
    ]:
        slide.els += [
            Rect(120, y, 1680, 145, PAPER),
            T(150, y + 30, 430, 105, artifact, 'semibold', 42, INK),
            T(620, y + 24, 660, 110, detail, 'body', 40, INK),
            T(1320, y + 30, 450, 105, commitment, 'body', 42, INK),
        ]
    return slide


def sprint():
    slide = canvas('SCRUM / THE SPRINT + FOUR EVENTS', 'A Sprint contains the learning cycle.',
        'A Sprint is the containing event, fixed length of one month or less; a one-week '
        'cycle can fit this project. The Sprint Goal supplies focus while the delivery '
        'plan can adapt. Sprint Planning establishes why the Sprint is valuable, what '
        'can be Done and how to do it. The 15-minute Daily Scrum is for Developers to '
        'inspect progress toward the Sprint Goal and adapt the plan. Sprint Review '
        'inspects the product outcome with stakeholders and informs future adaptations. '
        'Sprint Retrospective improves quality and team effectiveness. Review concerns '
        'the product; retrospective concerns how the team works. The latter two are '
        f'different events. Source: {SCRUM}#scrum-events.')
    slide.els += [
        Rect(120, 350, 1680, 500, PAPER),
        T(150, 375, 1620, 70, 'SPRINT / fixed length / one month or less',
          'semibold', 44, INK),
    ]
    for i, (head, detail) in enumerate([
        ('Planning', 'Agree a goal;\nselect work'),
        ('Daily Scrum', '15 min daily\nInspect + adapt'),
        ('Review', 'Inspect result\nwith stakeholders'),
        ('Retrospective', 'Improve quality\nand teamwork'),
    ]):
        x = 150 + i * 415
        slide.els += [
            Rect(x, 490, 365, 300, WHITE),
            T(x + 20, 520, 325, 85, head, 'xbold', 44, INK),
            T(x + 20, 640, 325, 150, detail, 'body', 40, INK),
        ]
        if i < 3:
            slide.els.append(T(x + 368, 575, 45, 80, '→', 'xbold', 48, ORANGE))
    slide.els.append(T(120, 895, 1680, 65,
        'Review the product. Reflect on the process. Adapt the next Sprint.', 'body', 40, INK))
    return slide


def board():
    slide = canvas('GITHUB PROJECTS / ILLUSTRATIVE BOARD', 'Make the work visible in GitHub.',
        'This is an illustrative board, not a screenshot of a real class team. GitHub '
        'Projects has table, board and roadmap views and can track repository issues '
        'and pull requests. The board groups items by Status; Backlog and Review are '
        'custom statuses in this example. Use real issues for shared tasks, add '
        'assignees and link the PR and test evidence. A single-select Priority field '
        'and an Iteration field are optional. The Backlog status column alone is not '
        'the entire Scrum Product Backlog: selected work and its goal/plan need to '
        'be understood too. A board visualizes the work; it does not implement Scrum '
        f'on its own. Guide: {PROJECTS}.')
    for i, (status, number, task, owner) in enumerate([
        ('Backlog', '#15', 'Pause menu', 'Alice'),
        ('Todo', '#12', 'Start button', 'Bob'),
        ('In progress', '#13', 'Collect a star', 'Alice'),
        ('Review', '#14', 'Restart level', 'Bob'),
        ('Done', '#11', 'Player moves', 'Alice'),
    ]):
        x = 120 + i * 340
        slide.els += [
            T(x, 340, 320, 70, status, 'semibold', 42, INK),
            Rect(x, 425, 320, 3, TEAL if status == 'Done' else LINE),
            Rect(x, 465, 320, 280, PAPER),
            T(x + 22, 485, 276, 60, number, 'semibold', 40, BLUE),
            T(x + 22, 565, 276, 110, task, 'semibold', 42, INK),
            T(x + 22, 685, 276, 55, owner, 'body', 40, INK),
        ]
    slide.els += [
        T(120, 825, 1680, 65, 'Track Status + Assignee; add Priority and Iteration if useful.',
          'body', 42, INK),
        T(120, 915, 1680, 60, f'[GitHub Projects setup guide →]({PROJECTS})', 'body', 40, BLUE),
    ]
    return slide


def tutor_deliveries():
    slide = canvas('GROUP PROJECT / WEEKLY TUTOR REVIEWS', 'Bring a usable delivery each week.',
        'These are the remaining Thursday class-week dates, not appointments at a '
        'newly invented time. Students meet their assigned tutor in their scheduled '
        'tutorial slot that week; the tutor confirms the exact time. The course '
        'Project template contains dated draft cards and one-week iterations. '
        'At each review bring a usable Increment, test/playtest evidence and the '
        'main blocker. Record tutor feedback and the next goal with owners. '
        'Adapt each focus to the game, app or installation with the tutor. '
        'The final Canvas submission is a separate deadline, not a tutor meeting. '
        'These records support the existing 25% execution mark; there is no extra '
        f'grade component or Canvas upload. Template: {TEAM_TEMPLATE}.')
    slide.els.append(T(120, 295, 1680, 70,
        'Your assigned tutor / your scheduled tutorial slot that week', 'body', 40, INK))
    for i, (day, focus) in enumerate([
        ('05 Nov', 'First working interaction'),
        ('12 Nov', 'Integrated core experience'),
        ('19 Nov', 'Playtest and feedback'),
        ('26 Nov', 'Delivery candidate'),
        ('03 Dec', 'Final tutor delivery review'),
    ]):
        y = 390 + i * 92
        slide.els += [
            Rect(120, y, 1680, 80, PAPER),
            T(150, y + 12, 290, 65, day, 'xbold', 44, INK),
            T(490, y + 12, 1280, 65, focus, 'body', 42, INK),
        ]
    slide.els += [
        T(120, 875, 1680, 65, 'Canvas deadline: 06 Dec 2026 / 23:59 HKT',
          'semibold', 44, ORANGE),
        T(120, 955, 1680, 45,
          f'[Group Project 2026 template →]({TEAM_TEMPLATE})', 'body', 32, BLUE),
    ]
    return slide


def agile_slides(teamwork_url):
    return [
        content('AGILE / SCRUM / TOOLS', 'Three different kinds of support', [
            '**Agile:** values and principles for adaptive software development.',
            '**Scrum:** a framework for learning and delivering value in Sprints.',
            '**GitHub Projects:** a tool to track issues, ownership and progress.',
            'Use them to organise the next playable or usable part of your project.',
        ], body_size=42, notes='Twenty-minute block before the Git walkthrough. The four '
            'Manifesto values were introduced in Week 1; revisit them briefly and teach '
            'their application here. Quiz scope includes the values, iterative/incremental '
            'development, Scrum pillars, accountabilities, artifacts and commitments, '
            'Sprint/events and the purpose of the tracking tools. Scrum is a framework '
            'within the broader Agile landscape, and GitHub is one possible tool. '
            f'Sources: {MANIFESTO}, {SCRUM}, {PROJECTS}.'),
        manifesto(), learning_loop(), accountabilities(), artifacts(), sprint(), board(),
        content('GITHUB / ISSUES → PROJECT → PULL REQUEST', 'Set up your team tracking.', [
            f'**1 / Copy** [Group Project 2026]({TEAM_TEMPLATE}) into **sd5913**; name it for your team.',
            '**2 / Link** your repository; give teammates Project Write access.',
            '**3 / Plan** issues in weekly iterations; use the dated tutor review cards.',
            '**4 / Track** Status; link the PR, tests and review evidence.',
            'A PR description with **Closes #12** closes issue #12 on merge to the default branch.',
        ], body_size=42, notes='Demonstrate with prepared material, not a student-owned '
            'board. Personal-account Projects also exist; this course uses an sd5913 '
            'organization repository and Project for each group. In sd5913 > Projects > '
            'New project select the organization template Group Project 2026. It uses '
            'the iterative-development structure with one-week cycles, Current iteration '
            'and Next iteration views, a Team board and Delivery dates. Use the group '
            'copy rather than editing the shared template. Repository links and '
            'collaborators are not copied, so configure both for the new Project. '
            'Students first accept '
            'the org invitation using their registered account, then choose Owner: '
            'sd5913 when creating a public repository. Give teammates Write access to '
            'their own repository and separately to their Project. Set that Project\'s '
            'base access for other organization members to Read or No access. Link the '
            'Project from the repository and README; add its repository issues. '
            'For a task issue, describe intended behaviour, '
            'acceptance checks and who owns it. Shared Definition of Done might require '
            'teammate testing, integration, passing relevant checks and updated run '
            'instructions. Issue acceptance checks describe that feature; Definition '
            'of Done is the shared quality standard across Increments. Built-in project '
            'workflows can move closed issues or merged PRs to Done; inspect their actual '
            'configuration. Closing a card by itself is not evidence of quality. '
            'Other options include Trello, Notion or a shared Markdown task list, provided '
            'the work and weekly progress remain accessible from the repository. '
            f'{PROJECTS}; https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue'),
        tutor_deliveries(),
        content('GROUP PROJECT / EXECUTION / 25%', 'Show how your team makes progress.', [
            '**Plan:** ordered tasks, clear owners and a goal for the next cycle.',
            '**Build:** small, steady contributions and usable Increments.',
            '**Review:** show what works; record tests, feedback and blockers.',
            '**Adapt:** document weekly progress and the next improvement.',
            f'Link your board and progress notes from the README. [Teamwork guide →]({teamwork_url})',
        ], body_size=42, notes='This explains the existing Execution criterion: exactly '
            '25% of the group-project mark; the whole project is 40% of the course. '
            'The other shares remain creative idea 25% and code 50%. Assess the actual '
            'development process and evidence, not card totals, raw commit counts or '
            'ceremony attendance. A GitHub Project is recommended; an equivalent shared '
            'record is valid. Keep brief weekly goals, completed work, review evidence '
            'and the next adjustment. This is ongoing project documentation in the same '
            'repository, not an additional Canvas upload. Formal Scrum titles are not '
            'a new grading requirement.'),
        content('APPLY THE CONCEPTS', 'Does this count as an Increment?', [
            '**Team A:** ten closed issues, but the project does not run.',
            '**Team B:** one playable interaction, integrated and verified against the Definition of Done.',
            'Which team can demonstrate a usable Increment?',
            'Where do they inspect the product? Where do they improve teamwork?',
        ], body_size=42, notes='Give the room thirty seconds. Team A has no usable '
            'Increment merely because cards are closed. Team B can demonstrate the '
            'stated Increment; inspect the real evidence for its quality checks. '
            'Sprint Review inspects the product outcome with stakeholders. Sprint '
            'Retrospective improves quality and team effectiveness. Now connect a '
            'selected issue to Alice and Bob\'s branch/PR workflow.'),
    ]
