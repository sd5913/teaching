"""Course-specific diagrams for the Week 5 image and video lesson."""

from deckgen.figures import Canvas

PAPER = '#FAF8F4'
INK = '#000B1C'
TEAL = '#246E70'
ORANGE = '#E87835'
MUTED = '#5C6470'
LINE = '#D7D9D7'


def pixel_grid(name='week05-pixel-grid', w=940, h=520):
    """Show spatial axes, one pixel per cell, and three RGB values per pixel."""
    c = Canvas(w, h, bg=PAPER)
    x0, y0, cw, ch = 175, 105, 220, 150
    samples = [
        ('[255, 40, 20]', '#FF2814', '#FFFFFF'),
        ('[20, 200, 70]', '#14C846', INK),
        ('[30, 90, 240]', '#1E5AF0', '#FFFFFF'),
        ('[255, 210, 40]', '#FFD228', INK),
        ('[80, 80, 80]', '#505050', '#FFFFFF'),
        ('[240, 230, 215]', '#F0E6D7', INK),
    ]
    c.text(w / 2, 42, 'x = column (width)', 27, TEAL, anchor='middle', weight=700)
    c.text(72, 75, 'y', 24, TEAL, anchor='middle', weight=700, mono=True)
    c.text(72, 104, 'row', 21, MUTED, anchor='middle')

    for row in range(2):
        c.text(112, y0 + row * ch + ch / 2 + 8, str(row), 22, MUTED,
               anchor='middle', mono=True)
        for col in range(3):
            label, fill, foreground = samples[row * 3 + col]
            x, y = x0 + col * cw, y0 + row * ch
            c.rect(x, y, cw - 8, ch - 8, fill=fill, stroke='#FFFFFF', width=3)
            c.text(x + (cw - 8) / 2, y + (ch - 8) / 2 + 8, label, 21,
                   foreground, anchor='middle', mono=True, weight=700)
            c.text(x + (cw - 8) / 2, y + ch + 15, str(col), 20, MUTED,
                   anchor='middle', mono=True)

    # The cell at row 0, column 2 is one pixel; its three values are RGB channels.
    x, y = x0 + 2 * cw, y0
    c.rect(x - 3, y - 3, cw - 2, ch - 2, stroke=ORANGE, width=6)
    c.text(w / 2, 500, 'pixel[y][x] = [red, green, blue]', 24, INK,
           anchor='middle', mono=True)
    return c.finish(name)


def grayscale_grid(name='week05-grayscale-grid', w=940, h=520):
    """Map a small grid of brightness values to visible grayscale cells."""
    c = Canvas(w, h, bg=PAPER)
    x0, y0, cw, ch = 235, 105, 220, 150
    values = ((20, 80, 160), (240, 160, 80))
    c.text(w / 2, 42, 'column', 25, TEAL, anchor='middle', weight=700)
    c.text(80, 82, 'row', 22, TEAL, anchor='middle', weight=700)
    for row, values_row in enumerate(values):
        c.text(165, y0 + row * ch + ch / 2 + 8, str(row), 22, MUTED,
               anchor='middle', mono=True)
        for col, value in enumerate(values_row):
            shade = value
            fill = f'#{shade:02X}{shade:02X}{shade:02X}'
            foreground = '#FFFFFF' if value < 128 else INK
            x, y = x0 + col * cw, y0 + row * ch
            c.rect(x, y, cw - 8, ch - 8, fill=fill, stroke='#FFFFFF', width=3)
            c.text(x + (cw - 8) / 2, y + (ch - 8) / 2 + 8, str(value), 25,
                   foreground, anchor='middle', mono=True, weight=700)
            if row == 0:
                c.text(x + (cw - 8) / 2, y0 - 15, str(col), 20, MUTED,
                       anchor='middle', mono=True)
    c.text(w / 2, 500, 'one value at each row, column -> one shade', 24, INK,
           anchor='middle', mono=True)
    return c.finish(name)


def frame_sequence(name='week05-frame-sequence', w=1500, h=460):
    """Show a moving subject represented by ordered still frames."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    frame_w, frame_h, gap = 340, 240, 105
    x0, y0 = 35, 80
    positions = (75, 170, 265)
    for i, pos in enumerate(positions):
        x = x0 + i * (frame_w + gap)
        c.rect(x, y0, frame_w, frame_h, fill='#FFFFFF', stroke=teal, width=3)
        c.circle(x + pos, y0 + 115, 28, fill=ORANGE, stroke=INK, width=2)
        c.text(x + frame_w / 2, y0 + frame_h + 38, f'frame {i}', 23, INK,
               anchor='middle', mono=True, weight=700)
        if i < 2:
            ax = x + frame_w + 14
            c.line(ax, y0 + frame_h / 2, ax + gap - 28, y0 + frame_h / 2,
                   ORANGE, 4)
            c.line(ax + gap - 48, y0 + frame_h / 2 - 13,
                   ax + gap - 28, y0 + frame_h / 2, ORANGE, 4)
            c.line(ax + gap - 48, y0 + frame_h / 2 + 13,
                   ax + gap - 28, y0 + frame_h / 2, ORANGE, 4)
    c.text(w / 2, 425, 'frame index -> time; frame rate controls playback speed',
           24, teal, anchor='middle')
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
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'

    boxes = [
        (35, 100, 215, 100, 'text prompts', 'captions'),
        (310, 100, 250, 100, 'Text encoder', 'text vectors'),
        (35, 285, 215, 100, 'images', 'visual examples'),
        (310, 285, 250, 100, 'Image encoder', 'image vectors'),
    ]
    for x, y, bw, bh, heading, detail in boxes:
        c.rect(x, y, bw, bh, fill='#FFFFFF', stroke=teal, width=3)
        c.text(x + bw / 2, y + 43, heading, 22, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + bw / 2, y + 76, detail, 18, teal,
               anchor='middle', mono=False)

    # Both encoded inputs feed a matrix of relative text-image similarity scores.
    c.line(250, 150, 292, 150, orange, 4)
    c.line(273, 138, 292, 150, orange, 4)
    c.line(273, 162, 292, 150, orange, 4)
    c.line(250, 335, 292, 335, orange, 4)
    c.line(273, 323, 292, 335, orange, 4)
    c.line(273, 347, 292, 335, orange, 4)

    grid_x, grid_y, cell_w, cell_h = 850, 145, 92, 68
    c.text(grid_x + 138, 80, 'TEXT EMBEDDINGS', 19, teal,
           anchor='middle', weight=700)
    c.text(665, 416, 'IMAGE EMBEDDINGS', 17, teal,
           anchor='middle', weight=700)
    c.line(560, 150, 730, 150, orange, 4)
    c.line(730, 150, 730, 110, orange, 4)
    c.line(730, 110, 965, 110, orange, 4)
    c.line(953, 122, 965, 110, orange, 4)
    c.line(977, 122, 965, 110, orange, 4)
    c.line(560, 335, 800, 335, orange, 4)
    c.line(800, 335, 800, 250, orange, 4)
    c.line(800, 250, 850, 250, orange, 4)
    c.line(830, 238, 850, 250, orange, 4)
    c.line(830, 262, 850, 250, orange, 4)

    for row in range(3):
        for col in range(3):
            x = grid_x + col * cell_w
            y = grid_y + row * cell_h
            fill = '#DCEBE5' if row == col else '#F0E6D7'
            label = 'high' if row == col else 'lower'
            c.rect(x, y, cell_w - 6, cell_h - 6, fill=fill,
                   stroke='#FFFFFF', width=2)
            c.text(x + (cell_w - 6) / 2, y + 39, label, 16, ink,
                   anchor='middle', mono=False, weight=700)
        c.text(grid_x + row * cell_w + (cell_w - 6) / 2, 132,
               f'T{row + 1}', 18, ink, anchor='middle', mono=True)

    c.rect(1170, 170, 270, 150, fill='#FFF1E7', stroke=teal, width=3)
    c.text(1305, 224, 'rank pairs', 24, ink, anchor='middle', weight=700)
    c.text(1305, 265, 'higher score = closer match', 17, teal,
           anchor='middle', mono=False)
    c.text(988, 375, 'similarity scores', 17, teal,
           anchor='middle', mono=False)
    c.text(w / 2, 455, 'CLIP scores image-text pairs; it is not a generator.',
           23, ink, anchor='middle', mono=False)
    return c.finish(name)


def diffusion_training(name='week05-diffusion-training', w=1500, h=560):
    """Separate latent-space denoiser training from latent-space generation."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'
    x_positions = (40, 330, 620, 910, 1200)
    box_w, box_h = 220, 118

    c.text(40, 52, 'TRAIN', 25, teal, weight=700)
    training = [
        ('encode image', 'VAE encoder -> z0'),
        ('add noise', 'at timestep t'),
        ('sample zt', 'noisy latent'),
        ('U-Net', 'predicts noise'),
        ('compare', 'update weights'),
    ]
    for x, (heading, detail) in zip(x_positions, training):
        c.rect(x, 78, box_w, box_h, fill='#FFFFFF', stroke=teal, width=3)
        c.text(x + box_w / 2, 123, heading, 21, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + box_w / 2, 158, detail, 17, teal,
               anchor='middle', mono=False)
    for x in x_positions[:-1]:
        start, end = x + box_w + 6, x + 276
        c.line(start, 137, end, 137, orange, 4)
        c.line(end - 18, 125, end, 137, orange, 4)
        c.line(end - 18, 149, end, 137, orange, 4)

    c.text(w / 2, 260,
           'Training: known sampled noise is the target; its error updates model weights.',
           21, ink, anchor='middle', mono=False)
    c.text(40, 320, 'GENERATE', 25, teal, weight=700)
    generation = [
        ('random noise zT', 'starting latent'),
        ('U-Net x N', 'prompt-guided steps'),
        ('clean latent z0', 'final representation'),
        ('VAE decoder', 'latent to pixels'),
        ('RGB image', 'visible result'),
    ]
    for x, (heading, detail) in zip(x_positions, generation):
        c.rect(x, 346, box_w, box_h, fill='#FFFFFF', stroke=teal, width=3)
        c.text(x + box_w / 2, 391, heading, 20, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + box_w / 2, 426, detail, 17, teal,
               anchor='middle', mono=False)
    for x in x_positions[:-1]:
        start, end = x + box_w + 6, x + 276
        c.line(start, 405, end, 405, orange, 4)
        c.line(end - 18, 393, end, 405, orange, 4)
        c.line(end - 18, 417, end, 405, orange, 4)

    c.text(w / 2, 515,
           'Generation: weights stay fixed while the noisy latent changes each step.',
           20, ink, anchor='middle', mono=False)
    return c.finish(name)


def vae_path(name='week05-vae-path', w=1500, h=430):
    """Show encoding, a compact latent, and reconstruction."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'
    labels = [
        ('image x', 'input pixels'),
        ('encoder', 'mean + variance'),
        ('sample z', 'compact latent'),
        ('decoder', 'reconstructs'),
        ('image x-hat', 'reconstruction'),
    ]
    box_y, box_h, box_w, gap = 130, 145, 245, 50
    for i, (heading, detail) in enumerate(labels):
        x = 20 + i * (box_w + gap)
        fill = '#FFFFFF' if i % 2 == 0 else '#E8F0EF'
        c.rect(x, box_y, box_w, box_h, fill=fill, stroke=teal, width=3)
        c.text(x + box_w / 2, box_y + 58, heading, 25, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + box_w / 2, box_y + 101, detail, 20, teal, anchor='middle')
        if i < len(labels) - 1:
            ax = x + box_w + 8
            c.line(ax, box_y + box_h / 2, ax + gap - 18, box_y + box_h / 2,
                   orange, 4)
            c.line(ax + gap - 38, box_y + box_h / 2 - 12,
                   ax + gap - 18, box_y + box_h / 2, orange, 4)
            c.line(ax + gap - 38, box_y + box_h / 2 + 12,
                   ax + gap - 18, box_y + box_h / 2, orange, 4)
    c.text(w / 2, 360, 'The encoder models a distribution; a sampled z gives an approximate reconstruction.',
           23, ink, anchor='middle')
    c.text(w / 2, 398, 'Sampling a latent can make a new image; this is not the same as diffusion.',
           21, teal, anchor='middle')
    return c.finish(name)


def latent_diffusion(name='week05-latent-diffusion', w=1600, h=520):
    """Show one common text-conditioned latent-diffusion generation path."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'
    box_y, box_h, box_w, gap = 245, 145, 260, 54
    labels = [
        ('latent noise', 'random starting point'),
        ('U-Net x N', 'noise prediction'),
        ('clean latent', 'compact representation'),
        ('VAE decoder', 'map latent to pixels'),
        ('image', 'visible RGB output'),
    ]
    for i, (title, detail) in enumerate(labels):
        x = 20 + i * (box_w + gap)
        fill = '#FFFFFF' if i % 2 == 0 else '#E8F0EF'
        c.rect(x, box_y, box_w, box_h, fill=fill, stroke=teal, width=3)
        c.text(x + box_w / 2, box_y + 58, title, 27, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + box_w / 2, box_y + 104, detail, 19, teal, anchor='middle')
        if i < len(labels) - 1:
            ax = x + box_w + 8
            c.line(ax, box_y + box_h / 2, ax + gap - 18, box_y + box_h / 2,
                   orange, 4)
            c.line(ax + gap - 38, box_y + box_h / 2 - 12,
                   ax + gap - 18, box_y + box_h / 2, orange, 4)
            c.line(ax + gap - 38, box_y + box_h / 2 + 12,
                   ax + gap - 18, box_y + box_h / 2, orange, 4)

    c.rect(30, 50, 245, 105, fill='#FFF1E7', stroke=orange, width=3)
    c.text(152, 93, 'prompt', 25, ink, anchor='middle', mono=True, weight=700)
    c.text(152, 129, 'words as input', 18, teal, anchor='middle')
    c.rect(345, 50, 260, 105, fill='#FFF1E7', stroke=orange, width=3)
    c.text(475, 93, 'text encoder', 25, ink, anchor='middle', mono=True, weight=700)
    c.text(475, 129, 'text features', 18, teal, anchor='middle')
    c.line(275, 102, 345, 102, orange, 4)
    c.line(328, 90, 345, 102, orange, 4)
    c.line(328, 114, 345, 102, orange, 4)
    c.line(475, 155, 475, 235, orange, 4)
    c.line(463, 218, 475, 235, orange, 4)
    c.line(487, 218, 475, 235, orange, 4)
    c.text(650, 190, 'conditioning', 18, teal, anchor='middle')
    c.text(w / 2, 466, 'The prompt guides denoising; the decoder turns the final latent into pixels.',
           23, ink, anchor='middle')
    return c.finish(name)


def controlnet_canny(name='week05-controlnet-canny', w=1500, h=500):
    """Show an edge map as an extra structural condition for generation."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'
    box_y, box_h, box_w, gap = 205, 140, 280, 65
    labels = [
        ('source image', 'input photograph'),
        ('Canny edges', 'a structural guide'),
        ('ControlNet', 'extra conditioning'),
        ('new image', 'appearance varies'),
    ]
    for i, (heading, detail) in enumerate(labels):
        x = 30 + i * (box_w + gap)
        fill = '#FFF1E7' if i == 2 else '#FFFFFF'
        c.rect(x, box_y, box_w, box_h, fill=fill, stroke=teal, width=3)
        c.text(x + box_w / 2, box_y + 58, heading, 24, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + box_w / 2, box_y + 103, detail, 20, teal, anchor='middle')
        if i < len(labels) - 1:
            ax = x + box_w + 8
            c.line(ax, box_y + box_h / 2, ax + gap - 18, box_y + box_h / 2,
                   orange, 4)
            c.line(ax + gap - 38, box_y + box_h / 2 - 12,
                   ax + gap - 18, box_y + box_h / 2, orange, 4)
            c.line(ax + gap - 38, box_y + box_h / 2 + 12,
                   ax + gap - 18, box_y + box_h / 2, orange, 4)

    prompt_x = 720
    c.rect(prompt_x, 25, box_w, 105, fill='#E8F0EF', stroke=teal, width=3)
    c.text(prompt_x + box_w / 2, 65, 'text prompt', 24, ink,
           anchor='middle', mono=True, weight=700)
    c.text(prompt_x + box_w / 2, 101, 'describes appearance', 20, teal,
           anchor='middle')
    cx = prompt_x + box_w / 2
    c.line(cx, 130, cx, 185, orange, 4)
    c.line(cx - 12, 165, cx, 185, orange, 4)
    c.line(cx + 12, 165, cx, 185, orange, 4)
    c.text(w / 2, 430, 'Edges guide structure; the prompt guides appearance.',
           24, ink, anchor='middle')
    c.text(w / 2, 468, 'The output is a new candidate, not a pixel-perfect copy.',
           21, teal, anchor='middle')
    return c.finish(name)
