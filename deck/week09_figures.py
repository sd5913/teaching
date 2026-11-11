"""Actual Week 9 messages, rendered with the established course palette."""
from deckgen.figures import Canvas, INK, MUTED, ORANGE, TEAL

WHITE = '#FFFFFF'
PAPER = '#FAF8F4'


def text(c, x, y, value, size=44, color=INK, anchor='start'):
    c.text(x, y, value, size=size, color=color, mono=True, anchor=anchor)


def node(c, x, title, lines, width=420, y=130, height=330):
    c.rect(x, y, width, height, fill=PAPER, stroke=TEAL, width=2)
    text(c, x + 24, y + 65, title, 48)
    for i, line in enumerate(lines):
        text(c, x + 24, y + 155 + i * 65, line)


def arrow(c, x1, x2, y, label='', color=ORANGE):
    c.line(x1, y, x2, y, color, 7)
    sign = 1 if x2 > x1 else -1
    c.poly([(x2, y), (x2-sign*22, y-14), (x2-sign*22, y+14)], fill=color)
    if label:
        text(c, (x1+x2)/2, y-28, label, 40, anchor='middle')


def address():
    c = Canvas(1680, 640, bg=WHITE)
    values = [('http', '1 / scheme'), ('127.0.0.1', '2 / host'), ('8009', '3 / port'), ('/state', '4 / route')]
    for i, (value, label) in enumerate(values):
        x = i*425
        node(c, x, value, [label], width=405, y=155, height=280)
    text(c, 840, 560, 'One URL: http://127.0.0.1:8009/state', 46, anchor='middle')
    return c.finish('week09-url')


def layers():
    c = Canvas(1680, 640, bg=WHITE)
    rows = [('4 / Application', 'HTTP / WebSocket / JSON action'), ('3 / Transport', 'TCP stream / UDP datagrams'), ('2 / Address', 'IP: which machine?'), ('1 / Link', 'Wi-Fi / Ethernet / loopback')]
    for i, (name, detail) in enumerate(rows):
        y = 30+i*145
        c.rect(20, y, 1640, 120, fill=PAPER)
        text(c, 50, y+77, name, 46)
        text(c, 620, y+77, detail, 44)
    return c.finish('week09-layers')


def journey(stage=0):
    c = Canvas(1680, 640, bg=WHITE)
    changed = stage >= 1
    node(c, 0, 'Browser A', ['input: 25', 'x = 25' if stage >= 2 else 'x = 50'])
    node(c, 630, 'Python Scene', ['x = 25' if changed else 'x = 50', 'revision = 1' if changed else 'revision = 0'])
    node(c, 1260, 'Browser B', ['input: 50', 'x = 25' if stage >= 2 else 'x = 50'])
    if stage == 0:
        arrow(c, 430, 620, 320, '1 / send')
        text(c, 840, 560, '{"id":"a-1", "action":"set_x", "x":25}', 44, anchor='middle')
    elif stage == 1:
        text(c, 840, 560, 'Validate, then change the one authoritative Scene.', 44, anchor='middle')
    elif stage == 2:
        arrow(c, 1058, 1250, 320, '2 / state')
        arrow(c, 620, 430, 320, '2 / state', TEAL)
        text(c, 840, 560, '{"type":"state", "x":25, "revision":1}', 44, anchor='middle')
    else:
        arrow(c, 620, 430, 320, '3 / ack', TEAL)
        text(c, 840, 560, '{"type":"ack", "id":"a-1", "revision":1}', 44, anchor='middle')
    return c.finish(f'week09-journey-{stage}')


def framing():
    c = Canvas(1680, 640, bg=WHITE)
    node(c, 20, 'Application writes', ['red\\n', 'blue\\n'], width=570)
    node(c, 1090, 'Possible reads', ['red\\nblu', 'e\\n'], width=570)
    arrow(c, 610, 1070, 315, 'TCP bytes')
    text(c, 840, 565, 'Keep a buffer; extract a message at each newline.', 44, anchor='middle')
    return c.finish('week09-framing')


def uncertainty():
    c = Canvas(1680, 640, bg=WHITE)
    node(c, 0, 'A / no ack', ['result unknown', 'do not resend'])
    node(c, 630, 'Server', ['x = 73', 'action applied'])
    node(c, 1260, 'B / observed', ['x = 73', 'state received'])
    arrow(c, 1058, 1250, 320, 'state')
    text(c, 840, 560, 'Missing observation does not prove a missing action.', 44, anchor='middle')
    return c.finish('week09-uncertainty')


def network_growth():
    """Count possible undirected pairs, without claiming measured network value."""
    c = Canvas(1680, 640, bg=WHITE)
    groups = [
        (280, [(200, 280), (360, 280)], '2 nodes', '1 possible pair'),
        (840, [(840, 190), (725, 390), (955, 390)], '3 nodes', '3 possible pairs'),
        (1400, [(1295, 190), (1505, 190), (1295, 390), (1505, 390)], '4 nodes', '6 possible pairs'),
    ]
    for center, points, title, count in groups:
        text(c, center, 75, title, 48, anchor='middle')
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1:]:
                c.line(x1, y1, x2, y2, TEAL, 6)
        for x, y in points:
            c.circle(x, y, 31, fill=PAPER, stroke=ORANGE, width=5)
        text(c, center, 505, count, 40, anchor='middle')
    text(c, 840, 610, 'The idea: value grows roughly with n squared.', 44, anchor='middle')
    return c.finish('week09-network-growth')


def osi_layers():
    """Show all OSI names and their approximate four-layer Internet mapping."""
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 55, 48, 'OSI reference model', 44)
    text(c, 1000, 48, 'TCP/IP working model', 44)
    names = ['7 / Application: services', '6 / Presentation: formats',
             '5 / Session: dialogues', '4 / Transport: endpoints',
             '3 / Network: routing', '2 / Data link: frames',
             '1 / Physical: signals']
    for i, name in enumerate(names):
        y = 78 + i * 72
        c.rect(30, y, 705, 63, fill=PAPER)
        text(c, 55, y + 46, name, 40)
    groups = [('Application', 78, 207), ('Transport', 294, 63),
              ('Internet', 366, 63), ('Link', 438, 135)]
    for name, y, height in groups:
        c.rect(990, y, 650, height, fill=PAPER, stroke=TEAL, width=3)
        center = y + height / 2
        arrow(c, 760, 965, center, color=TEAL)
        text(c, 1020, center + 15, name, 44)
    text(c, 840, 625, 'A useful mapping, not seven separate installed programs.', 40, anchor='middle')
    return c.finish('week09-osi-layers')


def packet_delivery(mode='unicast'):
    """Consistent destination geometry for three network delivery patterns."""
    if mode not in {'unicast', 'broadcast', 'multicast'}:
        raise ValueError('mode must be unicast, broadcast or multicast')
    c = Canvas(1680, 640, bg=WHITE)
    captions = {
        'unicast': 'One addressed destination',
        'broadcast': 'All hosts in this local broadcast domain',
        'multicast': 'Members of the addressed group',
    }
    text(c, 840, 55, captions[mode], 44, anchor='middle')
    node(c, 30, 'Sender', ['one packet'], width=370, y=220, height=190)
    # The central branch represents network delivery, not an application server.
    arrow(c, 420, 770, 315, 'network')
    c.line(790, 150, 790, 480, MUTED, 4)
    recipients = [('A', 95), ('B', 260), ('C', 425)]
    active = {'A'} if mode == 'unicast' else {'A', 'B', 'C'} if mode == 'broadcast' else {'B', 'C'}
    for name, y in recipients:
        color = ORANGE if name in active else MUTED
        c.rect(1170, y, 470, 120, fill=PAPER, stroke=color, width=3)
        label = f'Host {name}'
        if mode == 'multicast':
            label += ' / joined' if name in active else ' / outside'
        text(c, 1194, y + 76, label, 40)
        if name in active:
            arrow(c, 810, 1145, y + 60, color=ORANGE)
        else:
            c.line(810, y + 60, 1145, y + 60, '#E1E1DE', 3)
    footer = ('IPv4 broadcast has a local scope.' if mode == 'broadcast' else
              'Group membership selects receivers.' if mode == 'multicast' else
              'Each WebSocket connection uses addressed endpoints.')
    text(c, 840, 625, footer, 40, anchor='middle')
    return c.finish(f'week09-{mode}')


def tcp_handshake():
    """Simplified sequence of the three-way TCP connection handshake."""
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 330, 62, 'Client', 48, anchor='middle')
    text(c, 1350, 62, 'Server', 48, anchor='middle')
    c.line(330, 100, 330, 550, TEAL, 5)
    c.line(1350, 100, 1350, 550, TEAL, 5)
    arrow(c, 340, 1340, 205, '1 / SYN')
    arrow(c, 1340, 340, 355, '2 / SYN + ACK', TEAL)
    arrow(c, 340, 1340, 505, '3 / ACK')
    text(c, 840, 625, 'Connection setup precedes application data.', 44, anchor='middle')
    return c.finish('week09-tcp-handshake')


def endpoint_connections():
    """Two distinct local TCP connections share one server listening port."""
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 840, 55, 'One server port can serve many connections', 44, anchor='middle')
    node(c, 30, 'Browser A', ['127.0.0.1:51001'], width=520, y=105, height=195)
    node(c, 30, 'Browser B', ['127.0.0.1:51002'], width=520, y=350, height=195)
    c.rect(1155, 150, 495, 350, fill=PAPER, stroke=TEAL, width=3)
    text(c, 1180, 220, 'Python server', 44)
    text(c, 1180, 310, '127.0.0.1:8009', 44)
    text(c, 1180, 410, 'TCP listener', 40)
    arrow(c, 570, 1135, 235, 'connection A')
    arrow(c, 570, 1135, 445, 'connection B')
    text(c, 840, 625, 'Socket: endpoint. Protocol: rules for messages.', 40, anchor='middle')
    return c.finish('week09-endpoint-connections')


def host_route():
    """Simplified next-hop decision for a /24 local network."""
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 840, 55, '192.168.1.23/24 on a local network', 44, anchor='middle')
    node(c, 30, 'This laptop', ['192.168.1.23', '/24 subnet'], width=450, y=195, height=290)
    node(c, 1180, 'Local peer', ['192.168.1.42'], width=470, y=95, height=190)
    node(c, 1180, 'Gateway', ['192.168.1.1'], width=470, y=365, height=190)
    arrow(c, 500, 1160, 230, 'same subnet')
    arrow(c, 500, 1160, 465, 'other destination')
    text(c, 840, 625, 'The routing table chooses the next hop.', 44, anchor='middle')
    return c.finish('week09-host-route')


def encapsulation():
    """A schematic small WebSocket action nested in network envelopes."""
    c = Canvas(1680, 640, bg=WHITE)
    boxes = [
        (30, 65, 1620, 505, 'Local-link frame / Ethernet or Wi-Fi'),
        (80, 140, 1520, 415, 'IP packet / destination address'),
        (130, 215, 1420, 325, 'TCP segment / connection and byte order'),
        (180, 290, 1320, 235, 'WebSocket message / application framing'),
        (230, 365, 1220, 145, 'JSON action'),
    ]
    for i, (x, y, width, height, label) in enumerate(boxes):
        c.rect(x, y, width, height, fill=PAPER if i % 2 == 0 else WHITE,
               stroke=TEAL, width=3)
        text(c, x + 24, y + 50, label, 40)
    text(c, 254, 480, '{"id":"a-1","action":"set_x","x":25}', 40, color=ORANGE)
    text(c, 840, 625, 'Schematic nesting; TCP may split or combine messages.', 40, anchor='middle')
    return c.finish('week09-encapsulation')


def request_response():
    """The real GET /state request and its HTTP response on one connection."""
    c = Canvas(1680, 640, bg=WHITE)
    text(c, 330, 62, 'Client', 48, anchor='middle')
    text(c, 1350, 62, 'Python server', 48, anchor='middle')
    c.line(330, 105, 330, 565, TEAL, 5)
    c.line(1350, 105, 1350, 565, TEAL, 5)
    arrow(c, 340, 1340, 215, '1 / GET /state')
    arrow(c, 1340, 340, 380, '2 / HTTP 200 + JSON', TEAL)
    text(c, 840, 470, '{"type":"state","x":50,"revision":0}', 40, anchor='middle')
    text(c, 840, 625, 'A snapshot describes state at the time of the response.', 40, anchor='middle')
    return c.finish('week09-request-response')
