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
    c=Canvas(1600,720,bg=PAPER)
    box(c,25,170,430,365,'User',['id: 1','name: Ada'],VIOLET)
    box(c,585,170,430,365,'Conversation',['id: 3','owner_id: 1'],TEAL)
    box(c,1145,170,430,365,'Message',['id: 7','conversation_id', '3'],ORANGE)
    arrow(c,470,345,570,345);arrow(c,1030,345,1130,345)
    text(c,520,580,'1 : many',40,INK,'middle')
    text(c,1080,580,'1 : many',40,INK,'middle')
    text(c,800,640,'References store IDs; they do not copy parent objects.',44,INK,'middle')
    return c.finish('week10-related-records')


def mapping():
    c=Canvas(1600,720,bg=PAPER)
    box(c,35,135,650,430,'Python object',['chat.id = 3','chat.owner_id = 1','chat.title = Handbook'],TEAL)
    box(c,915,135,650,430,'conversation row',['id | owner_id | title','3  | 1        | Handbook','in out/chat.sqlite'],VIOLET)
    arrow(c,710,305,890,305);text(c,800,260,'.save()',42,ORANGE,'middle')
    arrow(c,890,445,710,445,TEAL);text(c,800,520,'query',42,INK,'middle')
    text(c,800,650,'Method bodies remain in models.py.',46,INK,'middle')
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
    box(c,25,170,430,360,'1. Process A',['chat.save()','Exit Python'],TEAL)
    box(c,585,170,430,360,'2. SQLite file',['Saved ID','Saved title','Data remains'],VIOLET)
    box(c,1145,170,430,360,'3. Process B',['Query saved ID','New object'],ORANGE)
    arrow(c,470,350,570,350);arrow(c,1030,350,1130,350)
    text(c,800,640,'Same stored identity; a different running object.',46,INK,'middle')
    return c.finish('week10-fresh-process')


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
    box(c,585,155,430,395,'2. Voice',['eSpeak NG','PCM WAV file','No paid API'],VIOLET)
    box(c,1145,155,430,395,'3. Playback',['ffplay','Hear / stop?','Check device'],ORANGE)
    arrow(c,470,350,570,350);arrow(c,1030,350,1130,350)
    text(c,800,650,'Speech failure keeps the displayed answer and saved history.',44,INK,'middle')
    return c.finish('week10-speech-boundaries')
