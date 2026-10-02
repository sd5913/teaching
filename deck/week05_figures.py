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


def gan_adversaries(name='week05-gan-adversaries', w=1500, h=500):
    """Contrast real examples and generated samples at a discriminator."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'
    boxes = [
        (35, 65, 280, 'training examples', 'real images'),
        (35, 310, 280, 'random latent', 'new starting values'),
        (405, 310, 280, 'generator', 'makes a sample'),
        (775, 310, 280, 'generated sample', 'candidate image'),
        (775, 65, 280, 'discriminator', 'compares examples'),
        (1145, 65, 300, 'real / generated?', 'a training signal'),
    ]
    for x, y, width, heading, detail in boxes:
        c.rect(x, y, width, 125, fill='#FFFFFF', stroke=teal, width=3)
        c.text(x + width / 2, y + 52, heading, 22, ink,
               anchor='middle', mono=True, weight=700)
        c.text(x + width / 2, y + 88, detail, 20, teal, anchor='middle')

    # Real and generated samples are both presented to the discriminator.
    c.line(315, 127, 760, 127, orange, 4)
    c.line(740, 115, 760, 127, orange, 4)
    c.line(740, 139, 760, 127, orange, 4)
    c.line(1055, 127, 1125, 127, orange, 4)
    c.line(1105, 115, 1125, 127, orange, 4)
    c.line(1105, 139, 1125, 127, orange, 4)
    c.line(315, 372, 390, 372, orange, 4)
    c.line(370, 360, 390, 372, orange, 4)
    c.line(370, 384, 390, 372, orange, 4)
    c.line(685, 372, 760, 372, orange, 4)
    c.line(740, 360, 760, 372, orange, 4)
    c.line(740, 384, 760, 372, orange, 4)
    c.line(915, 310, 915, 190, orange, 4)
    c.line(903, 210, 915, 190, orange, 4)
    c.line(927, 210, 915, 190, orange, 4)
    c.text(w / 2, 475, 'Both networks learn from the competition; neither is a human art judge.',
           23, ink, anchor='middle')
    return c.finish(name)


def vae_path(name='week05-vae-path', w=1500, h=430):
    """Show encoding, a compact latent, and reconstruction."""
    c = Canvas(w, h, bg=PAPER)
    teal = '#246E70'
    orange = '#E87835'
    ink = '#000B1C'
    labels = [
        ('image x', 'input pixels'),
        ('encoder', 'compresses'),
        ('latent z', 'compact code'),
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
    c.text(w / 2, 360, 'A VAE learns a useful latent representation and a path back to pixels.',
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
        ('latent noise', 'noisy start'),
        ('denoiser x N', 'refine over steps'),
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

    c.rect(390, 50, 410, 105, fill='#FFF1E7', stroke=orange, width=3)
    c.text(595, 93, 'text encoder', 27, ink, anchor='middle', mono=True, weight=700)
    c.text(595, 129, 'prompt -> text representation', 20, teal, anchor='middle')
    c.line(595, 155, 595, 195, orange, 4)
    c.line(595, 195, 464, 195, orange, 4)
    c.line(464, 195, 464, 235, orange, 4)
    c.line(452, 216, 464, 235, orange, 4)
    c.line(476, 216, 464, 235, orange, 4)
    c.text(w / 2, 466, 'The prompt guides denoising; the decoder turns the final latent into pixels.',
           23, ink, anchor='middle')
    return c.finish(name)
