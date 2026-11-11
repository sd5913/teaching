"""Week 10's actual records and retrieval boundaries, at projection scale."""
from deckgen.figures import Canvas, INK, MUTED, ORANGE, TEAL, VIOLET

PAPER = '#FAF8F4'
WHITE = '#FFFFFF'


def text(c, x, y, value, size=44, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, anchor=anchor, weight=700)


def box(c, x, y, w, h, heading, rows, color=TEAL):
    c.rect(x, y, w, h, fill=WHITE, stroke=color, width=4)
    text(c, x + 28, y + 68, heading, 48, INK)
    for i, row in enumerate(rows):
        text(c, x + 28, y + 144 + 64 * i, row, 42)


def arrow(c, x1, y1, x2, y2, color=ORANGE):
    c.line(x1, y1, x2, y2, color=color, width=7)
    if abs(x2-x1) >= abs(y2-y1):
        dx = 1 if x2 >= x1 else -1
        c.poly([(x2,y2),(x2-dx*22,y2-14),(x2-dx*22,y2+14)],fill=color)
    else:
        dy = 1 if y2 >= y1 else -1
        c.poly([(x2,y2),(x2-14,y2-dy*22),(x2+14,y2-dy*22)],fill=color)


def four_states():
    c=Canvas(1600,720,bg=PAPER)
    box(c,30,25,740,300,'Handbook knowledge',['Shared passages + vectors','Versioned source on disk'],VIOLET)
    box(c,830,25,740,300,'Conversation history',['User + conversation','Ordered rows on disk'],TEAL)
    box(c,30,385,740,300,'Current model request',['Rules + history + evidence','Assembled for this turn'],ORANGE)
    box(c,830,385,740,300,'Spoken output',['A generated sound file','Check playback separately'],TEAL)
    return c.finish('week10-four-states')


def relations():
    c = Canvas(1600, 720, bg=PAPER)
    c.rect(30, 130, 430, 460, fill=WHITE, stroke=VIOLET, width=4)
    c.rect(770, 130, 800, 460, fill=WHITE, stroke=TEAL, width=4)
    text(c, 60, 205, 'user', 48)
    text(c, 800, 205, 'conversation', 48)
    for x, label in ((60, 'id'), (230, 'name'), (800, 'id'),
                     (930, 'owner_id'), (1220, 'title')):
        text(c, x, 290, label, 40, MUTED)
    for y, user_id, name in ((370, '1', 'Ada'), (530, '2', 'Bo')):
        text(c, 60, y, user_id, 44)
        text(c, 230, y, name, 44)
    for y, chat_id, owner_id, title in (
        (370, '3', '1', 'Handbook'), (450, '4', '1', 'Game notes'),
        (530, '5', '2', 'Leave'),
    ):
        text(c, 800, y, chat_id, 44)
        text(c, 930, y, owner_id, 44)
        text(c, 1220, y, title, 44)
    c.line(480, 355, 610, 355, VIOLET, 7)
    c.line(610, 355, 610, 435, VIOLET, 7)
    arrow(c, 610, 355, 750, 355, VIOLET)
    arrow(c, 610, 435, 750, 435, VIOLET)
    arrow(c, 480, 515, 750, 515, TEAL)
    text(c, 800, 680, 'Match conversation.owner_id to user.id.', 44, INK, 'middle')
    return c.finish('week10-related-records')


def mapping():
    c=Canvas(1600,720,bg=PAPER)
    text(c,800,70,'Object-Relational Mapper',48,INK,'middle')
    box(c,25,150,430,350,'Python',['Model methods','Query objects'],TEAL)
    box(c,585,150,430,350,'ORM / Peewee',['Build SQL','Bind values'],VIOLET)
    box(c,1145,150,430,350,'Database',['Execute SQL','Return rows'],ORANGE)
    arrow(c,470,345,570,345);arrow(c,1030,345,1130,345)
    arrow(c,1360,555,240,555,TEAL)
    text(c,800,630,'SELECT rows become new Python model instances.',44,INK,'middle')
    text(c,800,700,'The database stores data and enforces constraints.',42,INK,'middle')
    return c.finish('week10-model-to-row')


def keys():
    c=Canvas(1600,720,bg=PAPER)
    box(c,25,145,480,390,'Primary key',['Message.id = 7','Which exact row?'],VIOLET)
    box(c,560,145,480,390,'Foreign key',['conversation_id','Parent: 3','Which parent?'],TEAL)
    box(c,1095,145,480,390,'Lookup index',['conversation_id','+ id','Find + order rows'],ORANGE)
    text(c,800,645,'A reference, an identity and a search aid do different jobs.',42,INK,'middle')
    return c.finish('week10-keys-index')


def restart():
    c=Canvas(1600,720,bg=PAPER)
    box(c,25,170,430,360,'1. Process A',['Save values','Process stops'],TEAL)
    box(c,585,170,430,360,'2. SQLite',['ID: 3','Owner: 1'],VIOLET)
    text(c,613,442,'Title: Handbook',40)
    box(c,1145,170,430,360,'3. Process B',['Load ID: 3','New object'],ORANGE)
    arrow(c,470,350,570,350);arrow(c,1030,350,1130,350)
    text(c,800,640,'Change the title without saving. What reloads?',46,INK,'middle')
    return c.finish('week10-fresh-process')


def one_to_one():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 30, 150, 550, 380, 'User 1', ['Name: Ada'], VIOLET)
    box(c, 940, 150, 630, 380, 'Profile 6', [
        'user_id: 1', 'Display: AdaCreates'], TEAL)
    arrow(c, 600, 340, 920, 340)
    text(c, 760, 265, '1 : 1', 48, INK, 'middle')
    text(c, 1255, 605, 'user_id must be UNIQUE', 42, INK, 'middle')
    text(c, 800, 700, 'User: zero or one profile. Profile: exactly one user.', 42, INK, 'middle')
    return c.finish('week10-one-to-one')


def one_to_many():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 30, 215, 500, 260, 'User 1', ['Name: Ada'], VIOLET)
    box(c, 960, 30, 610, 260, 'Conversation 3', ['Owner: User 1'], TEAL)
    box(c, 960, 385, 610, 260, 'Conversation 4', ['Owner: User 1'], TEAL)
    c.line(550, 345, 740, 345, ORANGE, 7)
    c.line(740, 160, 740, 515, ORANGE, 7)
    arrow(c, 740, 160, 940, 160)
    arrow(c, 740, 515, 940, 515)
    text(c, 675, 95, '1 : many', 46, INK, 'middle')
    text(c, 800, 700, 'Each conversation has one owner; one owner can have many.', 42, INK, 'middle')
    return c.finish('week10-one-to-many')


def many_to_many():
    c = Canvas(1600, 720, bg=PAPER)
    for y1, y2 in ((160, 160), (160, 515), (515, 160)):
        c.line(550, y1, 1050, y2, ORANGE, 7)
    box(c, 30, 30, 500, 260, 'User 1', ['Ada'], VIOLET)
    box(c, 30, 385, 500, 260, 'User 2', ['Bo'], VIOLET)
    box(c, 1070, 30, 500, 260, 'Team 7', ['Lantern'], TEAL)
    box(c, 1070, 385, 500, 260, 'Team 9', ['Orbit'], TEAL)
    text(c, 800, 700, 'A user can join many teams; a team can contain many users.', 42, INK, 'middle')
    return c.finish('week10-many-to-many')


def junction():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 20, 180, 360, 365, 'User', ['1: Ada', '2: Bo'], VIOLET)
    box(c, 500, 110, 600, 440, 'Membership', [
        'user | team | role', '1    | 7    | lead',
        '2    | 7    | artist', '1    | 9    | artist'], ORANGE)
    box(c, 1220, 180, 360, 365, 'Team', ['7: Lantern', '9: Orbit'], TEAL)
    arrow(c, 400, 345, 480, 345)
    arrow(c, 1200, 345, 1120, 345)
    text(c, 440, 620, '1 : many', 40, INK, 'middle')
    text(c, 1160, 620, 'many : 1', 40, INK, 'middle')
    text(c, 800, 700, 'The relationship has its own record and attributes.', 44, INK, 'middle')
    return c.finish('week10-junction-records')


def self_reference():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 25, 180, 430, 365, 'Message 7', ['Lost card?', 'Reply to: none'], VIOLET)
    box(c, 585, 180, 430, 365, 'Message 8', ['Apply online.', 'Reply to: 7'], TEAL)
    box(c, 1145, 180, 430, 365, 'Message 9', ['What fee?', 'Reply to: 8'], ORANGE)
    arrow(c, 570, 345, 470, 345)
    arrow(c, 1130, 345, 1030, 345)
    text(c, 800, 640, 'A message refers to another record of the same type.', 44, INK, 'middle')
    return c.finish('week10-self-reference')


def schema():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 30, 110, 740, 455, 'Schema: allowed data', [
        'ID: integer, unique', 'Owner: valid User ID', 'Title: text, required'], VIOLET)
    box(c, 830, 110, 740, 455, 'Rows: actual data', [
        'ID | owner | title', '3  | 1     | Handbook',
        '4  | 1     | Game notes', '5  | 2     | Leave'], TEAL)
    text(c, 800, 660, 'The schema describes the structure and constraints.', 44, INK, 'middle')
    return c.finish('week10-schema-and-rows')


def sql_history():
    c = Canvas(800, 640, bg=PAPER)
    text(c, 35, 60, 'message / source IDs', 44)
    c.rect(25, 90, 750, 280, fill=WHITE, stroke=TEAL, width=4)
    text(c, 55, 145, 'id', 40, MUTED)
    text(c, 190, 145, 'conversation_id (FK)', 40, MUTED)
    for y, message_id, conversation_id in ((210, '7', '3'), (275, '8', '3'), (340, '9', '5')):
        if conversation_id == '3':
            c.rect(40, y - 43, 720, 58, fill=PAPER)
        text(c, 55, y, message_id, 44)
        text(c, 190, y, conversation_id, 44, INK if conversation_id == '3' else MUTED)
    arrow(c, 400, 385, 400, 425)
    text(c, 35, 485, 'Result / id + content', 44)
    text(c, 55, 550, '7 | Lost card?', 42)
    text(c, 55, 615, '8 | Apply online.', 42)
    return c.finish('week10-sql-history')


def sql_join():
    c = Canvas(800, 640, bg=PAPER)
    text(c, 35, 65, 'Bind: 1 (Ada)', 40, MUTED)
    text(c, 35, 145, 'Returned rows', 48)
    c.rect(25, 190, 750, 330, fill=WHITE, stroke=TEAL, width=4)
    for y, line in ((265, 'id | name | title'),
                    (365, '3  | Ada  | Handbook'),
                    (465, '4  | Ada  | Game notes')):
        text(c, 55, y, line, 42)
    text(c, 35, 620, 'Bo\'s conversation excluded.', 40)
    return c.finish('week10-sql-join')


def sql_update():
    c = Canvas(800, 640, bg=PAPER)
    text(c, 35, 65, "Bind: 'Game ideas', 3", 40, MUTED)
    box(c, 25, 110, 750, 170, 'Before / row 3', ['Owner 1 | Handbook'], VIOLET)
    arrow(c, 400, 300, 400, 350)
    box(c, 25, 375, 750, 170, 'After commit / row 3', ['Owner 1 | Game ideas'], TEAL)
    text(c, 35, 620, 'Same ID and owner; new title.', 40)
    return c.finish('week10-sql-update')


def orm_check():
    c = Canvas(800, 640, bg=PAPER)
    text(c, 35, 65, 'Fresh example', 44)
    text(c, 35, 130, 'Saved title: Handbook', 40)
    text(c, 35, 220, 'Another process loads row 3.', 40)
    text(c, 35, 280, 'Which title does it read?', 40)
    for y, choice in ((385, 'A / Game ideas'), (475, 'B / Handbook'),
                      (565, 'C / No row remains')):
        text(c, 35, y, choice, 44)
    return c.finish('week10-orm-check')


def database_taxonomy():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 30, 80, 500, 470, 'Relational', [
        'Rows + columns', 'Keys + joins', 'SQLite / D1', 'PostgreSQL'], TEAL)
    c.rect(600, 80, 970, 470, fill=WHITE, stroke=VIOLET, width=4)
    text(c, 630, 148, 'NoSQL / non-relational', 48)
    text(c, 630, 198, 'Common model families', 40, MUTED)
    for x, y, heading, shape in (
        (630, 220, 'Key-value', 'Key -> value'),
        (1100, 220, 'Document', 'Nested records'),
        (630, 380, 'Wide-column', 'Column families'),
        (1100, 380, 'Graph', 'Nodes + edges'),
    ):
        c.rect(x, y, 440, 140, fill=PAPER, stroke=VIOLET, width=3)
        text(c, x + 20, y + 50, heading, 44)
        text(c, x + 20, y + 106, shape, 40)
    c.rect(30, 590, 1540, 110, fill=WHITE, stroke=ORANGE, width=4)
    text(c, 800, 635, 'Vector databases specialize in similarity search.', 44, INK, 'middle')
    text(c, 800, 683, 'That capability can also be added to other databases.', 40, INK, 'middle')
    return c.finish('week10-database-taxonomy')


def word_embedding():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 25, 170, 430, 350, 'Word', ['cat'], TEAL)
    box(c, 585, 170, 430, 350, 'Word model', ['word2vec', 'Trained model'], VIOLET)
    box(c, 1145, 170, 430, 350, 'Embedding', ['A vector', 'Fixed length'], ORANGE)
    arrow(c, 470, 345, 570, 345)
    arrow(c, 1030, 345, 1130, 345)
    text(c, 800, 645, 'Related contexts can give similar vectors.', 44, INK, 'middle')
    return c.finish('week10-word-embedding')


def text_embeddings():
    c = Canvas(1600, 720, bg=PAPER)
    box(c, 25, 45, 580, 265, 'Question', [
        'What does a new', 'student card cost?'], TEAL)
    box(c, 25, 395, 580, 265, 'Passage', [
        'Replacement fee:', 'HK$150'], VIOLET)
    box(c, 735, 175, 430, 380, 'Same encoder', ['MiniLM', '384 numbers'], ORANGE)
    box(c, 1280, 45, 295, 265, 'Q vector', ['[...]', '384D'], TEAL)
    box(c, 1280, 395, 295, 265, 'P vector', ['[...]', '384D'], VIOLET)
    arrow(c, 625, 175, 715, 300)
    arrow(c, 625, 525, 715, 430)
    arrow(c, 1180, 300, 1260, 175)
    arrow(c, 1180, 430, 1260, 525)
    text(c, 800, 710, 'Same trained encoder. Two compatible 384D vectors.', 42, INK, 'middle')
    return c.finish('week10-text-embeddings')


def ingestion():
    c=Canvas(1600,720,bg=PAPER)
    box(c,25,155,430,395,'1. PDF',['2026/27','137 PDF pages','Hash checked'],VIOLET)
    box(c,585,155,430,395,'2. Extract',['PDF page 20','printed page 9','ID + text'],TEAL)
    box(c,1145,155,430,395,'3. Encoder',['MiniLM, pinned','384 numbers','Vector + cite'],ORANGE)
    arrow(c,470,350,570,350);arrow(c,1030,350,1130,350)
    text(c,800,650,'Six cited extracts, prepared before class.',40,INK,'middle')
    return c.finish('week10-pdf-to-vectors')


def ranking():
    c=Canvas(1600,720,bg=PAPER)
    text(c,45,85,'Query: the cost of replacing a lost student card',40)
    for i,(name,score) in enumerate([('Fee row, PDF p76',0.892566),('Replacement rule, PDF p20',0.737337)]):
        y=200+i*200
        text(c,45,y,name,46)
        c.rect(45,y+35,1300*score,70,fill=TEAL if i==0 else VIOLET)
        text(c,1410,y+88,f'{score:.3f}',46)
    text(c,45,670,'Cosine similarity is not a probability.',44)
    return c.finish('week10-real-ranking')


def search():
    c=Canvas(1600,720,bg=PAPER)
    box(c,25,150,430,390,'1. Question',['Same MiniLM','384D vector','No keyword swap'],TEAL)
    box(c,585,150,430,390,'2. Compare',['Cosine score','Six vectors','Rank candidates'],VIOLET)
    box(c,1145,150,430,390,'3. Inspect',['Passage text','PDF page + ID','Support?'],ORANGE)
    arrow(c,470,345,570,345);arrow(c,1030,345,1130,345)
    text(c,800,645,'Same dimension alone does not mean the same embedding space.',42,INK,'middle')
    return c.finish('week10-semantic-search')


def tool_loop():
    c=Canvas(1600,720,bg=PAPER)
    box(c,30,25,690,280,'1. Local model',['History + question','Compose a retrieval query'],TEAL)
    box(c,880,25,690,280,'2. Python tool',['retrieve_handbook(query)','Encode + search vectors'],VIOLET)
    box(c,880,405,690,280,'3. Tool result',['Source IDs + pages + text','Data sent back to model'],ORANGE)
    box(c,30,405,690,280,'4. Answer phase',['Answer + source IDs','Validate, format, save'],TEAL)
    arrow(c,740,170,860,170);arrow(c,1225,325,1225,385)
    arrow(c,860,550,740,550)
    return c.finish('week10-tool-loop')


def prompt():
    c=Canvas(1600,720,bg=PAPER)
    rows=[('1. Rules','Use evidence; unsupported means refuse',VIOLET),
          ('2. History','Last four complete pairs, this conversation',TEAL),
          ('3. Question','If I find the original later,\nshould I keep both?',ORANGE),
          ('4. Sources','Retrieved card passages + source IDs',TEAL)]
    for i,(name,value,color) in enumerate(rows):
        y=35+i*170;c.rect(30,y,1540,140,fill=WHITE,stroke=color,width=4)
        text(c,55,y+65,name,43,INK)
        for j,line in enumerate(value.split('\n')):
            text(c,420,y+53+j*55,line,40)
    return c.finish('week10-actual-context')


def speech():
    c=Canvas(1600,720,bg=PAPER)
    box(c,25,155,430,395,'1. Answer',['Source checked','Saved turn','Visible text'],TEAL)
    box(c,585,155,430,395,'2. Voice',['Kokoro / Week 6','PCM WAV data','No paid API'],VIOLET)
    box(c,1145,155,430,395,'3. Playback',['Browser audio','Hear / stop?','Check volume'],ORANGE)
    arrow(c,470,350,570,350);arrow(c,1030,350,1130,350)
    text(c,800,650,'Speech failure keeps the displayed answer and saved history.',44,INK,'middle')
    return c.finish('week10-speech-boundaries')
