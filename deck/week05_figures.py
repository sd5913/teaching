"""Course-specific diagrams for the Week 5 image and video lesson."""

from deckgen.figures import Canvas

PAPER = '#FAF8F4'
INK = '#000B1C'
TEAL = '#246E70'
ORANGE = '#E87835'
MUTED = '#5C6470'
LINE = '#D7D9D7'


def model_stage(c, x, y, w, h, heading, detail, role='data', heading_size=36):
    """Narrowing/widening shapes distinguish encoding from decoding."""
    if role == 'encode':
        pts = [(x, y), (x + w, y + 22), (x + w, y + h - 22), (x, y + h)]
        fill = '#DCEBE5'
    elif role == 'decode':
        pts = [(x, y + 22), (x + w, y), (x + w, y + h), (x, y + h - 22)]
        fill = '#FFF1E7'
    else:
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
        fill = '#FFFFFF'
    c.poly(pts, fill=fill, stroke=TEAL, width=3)
    c.text(x + w / 2, y + h / 2 - 9, heading, heading_size, INK,
           anchor='middle', mono=False, weight=700)
    c.text(x + w / 2, y + h / 2 + 36, detail, 30, TEAL,
           anchor='middle', mono=False)


def pixel_grid(name='week05-pixel-grid', w=940, h=350):
    """Show spatial axes, one pixel per cell, and three RGB values per pixel."""
    c = Canvas(w, h, bg=PAPER)
    x0, y0, cw, ch = 175, 90, 220, 95
    samples = [
        ('[255,40,20]', '#FF2814', '#FFFFFF'),
        ('[20,200,70]', '#14C846', INK),
        ('[30,90,240]', '#1E5AF0', '#FFFFFF'),
        ('[255,210,40]', '#FFD228', INK),
        ('[80,80,80]', '#505050', '#FFFFFF'),
        ('[240,230,215]', '#F0E6D7', INK),
    ]
    c.text(w / 2, 42, 'x = column (width)', 27, TEAL, anchor='middle', weight=700)
    c.text(72, 52, 'y', 24, TEAL, anchor='middle', weight=700, mono=True)
    c.text(72, 82, 'row', 23, MUTED, anchor='middle', weight=700)

    for row in range(2):
        c.text(112, y0 + row * ch + ch / 2 + 8, str(row), 23, MUTED,
               anchor='middle', mono=True, weight=700)
        for col in range(3):
            label, fill, foreground = samples[row * 3 + col]
            x, y = x0 + col * cw, y0 + row * ch
            c.rect(x, y, cw - 8, ch - 8, fill=fill, stroke='#FFFFFF', width=3)
            c.text(x + (cw - 8) / 2, y + (ch - 8) / 2 + 8, label, 24,
                   foreground, anchor='middle', mono=True, weight=700)
            if row == 0:
                c.text(x + (cw - 8) / 2, y0 - 12, str(col), 23, MUTED,
                       anchor='middle', mono=True, weight=700)

    # The cell at row 0, column 2 is one pixel; its three values are RGB channels.
    x, y = x0 + 2 * cw, y0
    c.rect(x - 3, y - 3, cw - 2, ch - 2, stroke=ORANGE, width=6)
    c.text(w / 2, 330, 'pixel[y][x] = [red, green, blue]', 24, INK,
           anchor='middle', mono=True)
    return c.finish(name)


def grayscale_grid(name='week05-grayscale-grid', w=940, h=350):
    """Map a small grid of brightness values to visible grayscale cells."""
    c = Canvas(w, h, bg=PAPER)
    x0, y0, cw, ch = 235, 90, 220, 95
    values = ((20, 80, 160), (240, 160, 80))
    c.text(w / 2, 42, 'column', 25, TEAL, anchor='middle', weight=700)
    c.text(80, 82, 'row', 23, TEAL, anchor='middle', weight=700)
    for row, values_row in enumerate(values):
        c.text(165, y0 + row * ch + ch / 2 + 8, str(row), 23, MUTED,
               anchor='middle', mono=True, weight=700)
        for col, value in enumerate(values_row):
            shade = value
            fill = f'#{shade:02X}{shade:02X}{shade:02X}'
            foreground = '#FFFFFF' if value < 128 else INK
            x, y = x0 + col * cw, y0 + row * ch
            c.rect(x, y, cw - 8, ch - 8, fill=fill, stroke='#FFFFFF', width=3)
            c.text(x + (cw - 8) / 2, y + (ch - 8) / 2 + 8, str(value), 25,
                   foreground, anchor='middle', mono=True, weight=700)
            if row == 0:
                c.text(x + (cw - 8) / 2, y0 - 12, str(col), 23, MUTED,
                       anchor='middle', mono=True, weight=700)
    c.text(w / 2, 330, 'one value at each row, column -> one shade', 24, INK,
           anchor='middle', mono=True)
    return c.finish(name)


def frame_sequence(name='week05-frame-sequence', w=1500, h=460):
    """Show a moving subject represented by ordered still frames."""
    c = Canvas(w, h, bg=PAPER)
    frame_w, frame_h, gap = 370, 240, 130
    x0, y0 = 65, 70
    positions = (75, 185, 295)
    for i, pos in enumerate(positions):
        x = x0 + i * (frame_w + gap)
        c.rect(x, y0, frame_w, frame_h, fill='#FFFFFF', stroke=TEAL, width=3)
        c.circle(x + pos, y0 + 115, 28, fill=ORANGE, stroke=INK, width=2)
        c.text(x + frame_w / 2, y0 + frame_h + 45, f'frame {i}', 36, INK,
               anchor='middle', mono=True, weight=700)
        if i < 2:
            ax, end = x + frame_w + 16, x + frame_w + gap - 16
            c.line(ax, 190, end, 190, ORANGE, 4)
            c.line(end - 20, 177, end, 190, ORANGE, 4)
            c.line(end - 20, 203, end, 190, ORANGE, 4)
    c.text(w / 2, 425, 'Frame order gives time. Frame rate controls playback speed.',
           32, TEAL, anchor='middle', mono=False)
    return c.finish(name)


def frame_preview(name='week05-frame-preview', w=640, h=360):
    """Static first frame for the editable HTML sketch's PDF/PPTX fallback."""
    c = Canvas(w, h, bg=PAPER)
    c.circle(80, 180, 45, fill='#ED6D24')
    c.text(24, 40, 'frame 0', 26, INK, mono=False)
    return c.finish(name)


def clip_alignment(name='week05-clip-alignment', w=1500, h=500):
    """Show CLIP matching text and images in a shared representation space."""
    c = Canvas(w, h, bg=PAPER)
    for y, source, encoder, vector in (
        (90, 'captions', 'Text encoder', 'text vectors'),
        (285, 'images', 'Image encoder', 'image vectors'),
    ):
        c.rect(30, y, 225, 110, fill='#FFFFFF', stroke=TEAL, width=3)
        c.text(142.5, y + 66, source, 36, INK,
               anchor='middle', mono=False, weight=700)
        c.rect(310, y, 305, 110, fill='#FFFFFF', stroke=TEAL, width=3)
        c.text(462.5, y + 45, encoder, 36, INK,
               anchor='middle', mono=False, weight=700)
        c.text(462.5, y + 86, vector, 30, TEAL,
               anchor='middle', mono=False)
        c.line(267, y + 55, 297, y + 55, ORANGE, 4)
        c.line(281, y + 43, 297, y + 55, ORANGE, 4)
        c.line(281, y + 67, 297, y + 55, ORANGE, 4)

    # Columns represent text vectors, rows image vectors; diagonal pairs match.
    grid_x, grid_y, cell_w, cell_h = 860, 145, 108, 76
    c.text(1022, 69, 'Text vectors', 36, TEAL,
           anchor='middle', mono=False, weight=700)
    c.text(720, 423, 'Image vectors', 36, TEAL,
           anchor='middle', mono=False, weight=700)
    c.line(627, 145, 747, 145, ORANGE, 4)
    c.line(747, 145, 747, 96, ORANGE, 4)
    c.line(747, 96, 1022, 96, ORANGE, 4)
    c.line(1022, 96, 1022, 130, ORANGE, 4)
    c.line(1010, 112, 1022, 130, ORANGE, 4)
    c.line(1034, 112, 1022, 130, ORANGE, 4)
    c.line(627, 340, 777, 340, ORANGE, 4)
    c.line(777, 340, 777, 259, ORANGE, 4)
    c.line(777, 259, 846, 259, ORANGE, 4)
    c.line(828, 247, 846, 259, ORANGE, 4)
    c.line(828, 271, 846, 259, ORANGE, 4)

    for row in range(3):
        for col in range(3):
            x, y = grid_x + col * cell_w, grid_y + row * cell_h
            fill = '#DCEBE5' if row == col else '#F0E6D7'
            c.rect(x, y, cell_w - 6, cell_h - 6, fill=fill,
                   stroke='#FFFFFF', width=2)
            c.text(x + (cell_w - 6) / 2, y + 47,
                   'high' if row == col else 'low', 36, INK,
                   anchor='middle', mono=False, weight=700)
    c.text(1022, 420, 'similarity', 30, TEAL, anchor='middle', mono=False)
    c.rect(1230, 175, 245, 170, fill='#FFF1E7', stroke=TEAL, width=3)
    c.text(1352.5, 220, 'rank pairs', 36, INK,
           anchor='middle', mono=False, weight=700)
    c.text(1352.5, 267, 'high score:', 30, TEAL, anchor='middle', mono=False)
    c.text(1352.5, 308, 'closer match', 30, TEAL, anchor='middle', mono=False)
    c.text(w / 2, 478, 'CLIP matches images and text. It is not a generator.',
           32, INK, anchor='middle', mono=False)
    return c.finish(name)


def diffusion_training(name='week05-diffusion-training', w=1500, h=500):
    """Separate latent-space denoiser training from latent-space generation."""
    c = Canvas(w, h, bg=PAPER)
    x_positions = (20, 400, 780, 1160)
    box_w, box_h = 310, 130
    training = [
        ('VAE encoder', 'image to latent z0'),
        ('add noise', 'noisy latent zt'),
        ('U-Net', 'predict noise'),
        ('compare', 'prediction vs noise'),
    ]
    generation = [
        ('random noise zT', 'starting latent'),
        ('U-Net x N', 'clean latent z0'),
        ('VAE decoder', 'latent to pixels'),
        ('RGB image', 'visible result'),
    ]
    for section, title_y, box_y, stages in (
        ('TRAIN', 46, 70, training),
        ('GENERATE', 286, 310, generation),
    ):
        c.text(30, title_y, section, 36, TEAL, mono=False, weight=700)
        for x, (heading, detail) in zip(x_positions, stages):
            role = 'encode' if heading == 'VAE encoder' else 'decode' if heading == 'VAE decoder' else 'data'
            model_stage(c, x, box_y, box_w, box_h, heading, detail, role)
        for x in x_positions[:-1]:
            start, end, y = x + box_w + 12, x + 368, box_y + box_h / 2
            c.line(start, y, end, y, ORANGE, 4)
            c.line(end - 18, y - 12, end, y, ORANGE, 4)
            c.line(end - 18, y + 12, end, y, ORANGE, 4)
    c.text(w / 2, 254, 'Prediction error updates model weights.',
           32, INK, anchor='middle', mono=False)
    c.text(w / 2, 485, 'Generation changes the latent; model weights stay fixed.',
           32, INK, anchor='middle', mono=False)
    return c.finish(name)


def vae_path(name='week05-vae-path', w=1500, h=430):
    """Show encoding, a compact latent, and reconstruction."""
    c = Canvas(w, h, bg=PAPER)
    labels = [
        ('image x', 'input pixels'),
        ('encoder', 'mean + variance'),
        ('latent z', 'sample z'),
        ('decoder', 'rebuild pixels'),
        ('image x-hat', 'rebuilt pixels'),
    ]
    box_y, box_h, box_w, gap = 100, 150, 260, 40
    for i, (heading, detail) in enumerate(labels):
        x = 25 + i * (box_w + gap)
        role = 'encode' if heading == 'encoder' else 'decode' if heading == 'decoder' else 'data'
        model_stage(c, x, box_y, box_w, box_h, heading, detail, role)
        if i < len(labels) - 1:
            start, end, y = x + box_w + 9, x + box_w + gap - 10, box_y + box_h / 2
            c.line(start, y, end, y, ORANGE, 4)
            c.line(end - 17, y - 12, end, y, ORANGE, 4)
            c.line(end - 17, y + 12, end, y, ORANGE, 4)
    c.text(w / 2, 330, 'A VAE learns a compact representation and a path back to pixels.',
           32, INK, anchor='middle', mono=False)
    c.text(w / 2, 388, 'Sampling a latent can generate an image without diffusion.',
           30, TEAL, anchor='middle', mono=False)
    return c.finish(name)


def latent_diffusion(name='week05-latent-diffusion', w=1600, h=520):
    """Show the classic text-conditioned Stable Diffusion generation path."""
    c = Canvas(w, h, bg=PAPER)
    box_y, box_h, box_w, gap = 245, 145, 270, 50
    labels = [
        ('latent noise', 'random start'),
        ('U-Net x N', 'denoise steps'),
        ('clean latent', 'compact code'),
        ('VAE decoder', 'expand to pixels'),
        ('image', 'RGB output'),
    ]
    for i, (title, detail) in enumerate(labels):
        x = 25 + i * (box_w + gap)
        model_stage(c, x, box_y, box_w, box_h, title, detail,
                    'decode' if title == 'VAE decoder' else 'data', heading_size=40)
        if i < len(labels) - 1:
            start, end, y = x + box_w + 9, x + box_w + gap - 10, box_y + box_h / 2
            c.line(start, y, end, y, ORANGE, 4)
            c.line(end - 17, y - 12, end, y, ORANGE, 4)
            c.line(end - 17, y + 12, end, y, ORANGE, 4)
    c.rect(345, 45, 270, 115, fill='#FFF1E7', stroke=ORANGE, width=3)
    c.text(480, 91, 'text encoder', 39, INK,
           anchor='middle', mono=False, weight=700)
    c.text(480, 135, 'prompt vectors', 30, TEAL, anchor='middle', mono=False)
    c.line(480, 160, 480, 231, ORANGE, 4)
    c.line(468, 212, 480, 231, ORANGE, 4)
    c.line(492, 212, 480, 231, ORANGE, 4)
    c.text(w / 2, 467, 'Prompt conditioning guides denoising; the VAE decoder returns pixels.',
           32, INK, anchor='middle', mono=False)
    return c.finish(name)


def controlnet_canny(name='week05-controlnet-canny', w=1500, h=500):
    """Show an edge map as an extra structural condition for generation."""
    c = Canvas(w, h, bg=PAPER)
    box_y, box_h, box_w, gap = 220, 140, 310, 70
    labels = [
        ('source image', 'input photo'),
        ('Canny edges', 'structure guide'),
        ('ControlNet', 'conditions SD'),
        ('new image', 'new appearance'),
    ]
    for i, (heading, detail) in enumerate(labels):
        x = 25 + i * (box_w + gap)
        fill = '#FFF1E7' if i == 2 else '#FFFFFF'
        c.rect(x, box_y, box_w, box_h, fill=fill, stroke=TEAL, width=3)
        c.text(x + box_w / 2, box_y + 56, heading, 36, INK,
               anchor='middle', mono=False, weight=700)
        c.text(x + box_w / 2, box_y + 104, detail, 30, TEAL,
               anchor='middle', mono=False)
        if i < len(labels) - 1:
            start, end, y = x + box_w + 10, x + box_w + gap - 12, box_y + box_h / 2
            c.line(start, y, end, y, ORANGE, 4)
            c.line(end - 18, y - 12, end, y, ORANGE, 4)
            c.line(end - 18, y + 12, end, y, ORANGE, 4)
    c.rect(785, 25, box_w, 115, fill='#E8F0EF', stroke=TEAL, width=3)
    c.text(940, 71, 'text prompt', 36, INK,
           anchor='middle', mono=False, weight=700)
    c.text(940, 114, 'appearance', 30, TEAL, anchor='middle', mono=False)
    c.line(940, 140, 940, 206, ORANGE, 4)
    c.line(928, 187, 940, 206, ORANGE, 4)
    c.line(952, 187, 940, 206, ORANGE, 4)
    c.text(w / 2, 424, 'Edges guide structure. The prompt guides appearance.',
           32, INK, anchor='middle', mono=False)
    c.text(w / 2, 474, 'The output is a new image, not a pixel-perfect copy.',
           30, TEAL, anchor='middle', mono=False)
    return c.finish(name)
