"""Concrete revision diagrams in the existing course visual language."""
from deckgen.figures import Canvas

INK = '#000B1C'
TEAL = '#246E70'
ORANGE = '#E87835'
PAPER = '#FAF8F4'
MUTED = '#5C6470'


def arrow(c, start, end, y):
    c.line(start, y, end, y, color=ORANGE, width=8)
    c.poly([(end, y), (end - 24, y - 16), (end - 24, y + 16)], fill=ORANGE)


def node(c, x, y, width, heading, lines):
    c.rect(x, y, width, 300, fill='#FFFFFF', stroke=TEAL, width=3)
    c.text(x + 25, y + 72, heading, 48, INK, weight=700)
    for i, line in enumerate(lines):
        c.text(x + 25, y + 155 + i * 64, line, 42, MUTED)


def record_keys():
    c = Canvas(1600, 720, bg=PAPER)
    for x, heading, lines in [
        (0, '1 / Identity', ['Message.id = 13', 'primary key']),
        (550, '2 / Reference', ['parent: 7', 'foreign key']),
        (1100, '3 / Find rows', ['conversation_id', 'lookup index']),
    ]:
        node(c, x, 180, 500, heading, lines)
    c.text(800, 100, 'Message 13 belongs to conversation 7.', 50, INK, anchor='middle')
    c.text(800, 620, 'Which changes correctness? Which changes lookup cost?', 44, TEAL, anchor='middle')
    return c.finish('week13-record-keys')


def retrieval():
    c = Canvas(1600, 720, bg=PAPER)
    node(c, 0, 180, 460, '1 / Question', ['paraphrased text', 'same encoder'])
    node(c, 570, 180, 460, '2 / Similarity', ['compare vectors', 'rank candidates'])
    node(c, 1140, 180, 460, '3 / Source', ['page + passage', 'check relevance'])
    arrow(c, 480, 550, 340)
    arrow(c, 1050, 1120, 340)
    c.text(800, 100, 'Handbook / chunks / vectors + source IDs', 48, INK, anchor='middle')
    c.text(800, 620, 'A high similarity score is not a truth score.', 48, TEAL, anchor='middle')
    return c.finish('week13-retrieval')


def lifetimes():
    c = Canvas(1600, 720, bg=PAPER)
    for x, y, heading, lines in [
        (0, 0, 'Knowledge / persists', ['PDF chunks + vectors', 'versioned source IDs']),
        (830, 0, 'History / persists', ['ordered messages', 'scoped conversation']),
        (0, 390, 'Prompt / one call', ['question + chosen context', 'actually sent to the model']),
        (830, 390, 'Speech / output', ['synthesize answer text', 'check playback separately']),
    ]:
        node(c, x, y, 770, heading, lines)
    return c.finish('week13-lifetimes')


def feedback():
    c = Canvas(1600, 720, bg=PAPER)
    node(c, 0, 180, 460, '1 / Choose', ['goal + evidence', 'model chooses'])
    node(c, 570, 180, 460, '2 / Act', ['tool request', 'inspect result'])
    node(c, 1140, 180, 460, '3 / Check', ['behavior check', 'adapt or stop'])
    arrow(c, 480, 550, 340)
    arrow(c, 1050, 1120, 340)
    c.line(1370, 490, 1370, 570, color=TEAL, width=7)
    c.line(1370, 570, 230, 570, color=TEAL, width=7)
    c.line(230, 570, 230, 500, color=TEAL, width=7)
    c.poly([(230, 490), (212, 520), (248, 520)], fill=TEAL)
    c.rect(540, 535, 540, 65, fill=PAPER)
    c.text(800, 582, 'observe / adapt', 42, TEAL, anchor='middle')
    c.text(800, 100, 'Stop on success or a stated limit.', 50, INK, anchor='middle')
    c.text(800, 690, 'Compare: a fixed workflow follows its programmed steps.', 42, INK, anchor='middle')
    return c.finish('week13-feedback')


def reproduction():
    c = Canvas(1600, 720, bg=PAPER)
    node(c, 0, 180, 460, '1 / Fresh copy', ['shared revision', 'sample data'])
    node(c, 570, 180, 460, '2 / README', ['setup + run', 'no hidden steps'])
    node(c, 1140, 180, 460, '3 / Observe', ['normal input', 'boundary case'])
    arrow(c, 480, 550, 340)
    arrow(c, 1050, 1120, 340)
    c.text(800, 100, 'Give the next person the URL and starting point.', 48, INK, anchor='middle')
    c.text(800, 620, 'Record the actual result and the next fix.', 48, TEAL, anchor='middle')
    return c.finish('week13-reproduction')
