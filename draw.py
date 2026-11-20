#!/usr/bin/env python3
"""Draw entry.png for news-image-20261120 by hand with PIL.

A newspaper infographic, 1024x1024: a header naming Friday 20 November
2026, and six story panels in a 2x3 grid. Every glyph is drawn from
PIL primitives (lines, arcs, polygons); no AI generation, no photos,
no external assets. Deterministic: same input, same bytes every run.

Usage: python3 draw.py [output-path]   (default: entry.png next to this file)
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 231)
NAVY = (29, 43, 74)
RED_RULE = (192, 57, 43)
CARD = (255, 253, 248)
CARD_BORDER = (216, 205, 184)
INK = (43, 43, 43)
MUTED = (200, 208, 224)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_DATE = font("DejaVuSans-Bold.ttf", 54)
F_SUB = font("DejaVuSans-Bold.ttf", 24)
F_KICKER = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 30)
F_BODY = font("DejaVuSans.ttf", 20)
F_FOOT = font("DejaVuSans.ttf", 17)


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines fitting `width` px."""
    lines = []
    line = ""
    for word in text.split():
        trial = word if not line else line + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_clock(d, cx, cy):
    d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], outline=WHITE, width=3)
    d.line([cx, cy, cx, cy - 11], fill=WHITE, width=3)
    d.line([cx, cy, cx + 9, cy + 5], fill=WHITE, width=3)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=WHITE)


def draw_spiral(d, cx, cy):
    for i, (r, a0, a1) in enumerate(
        [(20, 20, 320), (15, 110, 60), (10, 200, 150), (5, 290, 240)]
    ):
        d.arc([cx - r, cy - r, cx + r, cy + r], a0, a1, fill=WHITE, width=3)
    d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=WHITE)


def draw_scales(d, cx, cy):
    d.line([cx, cy - 18, cx, cy + 16], fill=WHITE, width=3)
    d.line([cx - 17, cy - 14, cx + 17, cy - 14], fill=WHITE, width=3)
    d.line([cx, cy + 16, cx - 8, cy + 16], fill=WHITE, width=3)
    d.line([cx, cy + 16, cx + 8, cy + 16], fill=WHITE, width=3)
    for sx in (cx - 17, cx + 17):
        d.line([sx, cy - 14, sx - 6, cy + 2], fill=WHITE, width=2)
        d.line([sx, cy - 14, sx + 6, cy + 2], fill=WHITE, width=2)
        d.polygon(
            [(sx - 9, cy + 2), (sx + 9, cy + 2), (sx, cy + 12)], fill=WHITE
        )


def draw_globe(d, cx, cy):
    d.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], outline=WHITE, width=3)
    d.arc([cx - 8, cy - 18, cx + 8, cy + 18], 0, 360, fill=WHITE, width=2)
    d.line([cx - 18, cy, cx + 18, cy], fill=WHITE, width=2)


def draw_probe(d, cx, cy):
    d.polygon(
        [
            (cx, cy - 18),
            (cx + 5, cy - 5),
            (cx + 18, cy),
            (cx + 5, cy + 5),
            (cx, cy + 18),
            (cx - 5, cy + 5),
            (cx - 18, cy),
            (cx - 5, cy - 5),
        ],
        fill=WHITE,
    )
    d.arc([cx - 23, cy - 9, cx + 23, cy + 9], 195, 345, fill=WHITE, width=2)


def draw_pad(d, cx, cy):
    d.rounded_rectangle(
        [cx - 20, cy - 9, cx + 20, cy + 13], radius=6, outline=WHITE, width=3
    )
    d.rectangle([cx - 13, cy - 2, cx - 5, cy + 2], fill=WHITE)
    d.rectangle([cx - 11, cy - 4, cx - 7, cy + 4], fill=WHITE)
    d.ellipse([cx + 7, cy - 4, cx + 11, cy], fill=WHITE)
    d.ellipse([cx + 13, cy + 2, cx + 17, cy + 6], fill=WHITE)


GLYPHS = {
    "clock": draw_clock,
    "spiral": draw_spiral,
    "scales": draw_scales,
    "globe": draw_globe,
    "probe": draw_probe,
    "pad": draw_pad,
}

# (kicker, headline, body, colour, glyph)
STORIES = [
    (
        "WASHINGTON  \u2022  IRAN",
        "Trump puts Iran decision off to 2027",
        "President Trump says he is in \u2018no rush\u2019 on new strikes on "
        "Iran: \u2018We\u2019ll see what happens after January 1.\u2019",
        (140, 43, 43),
        "clock",
    ),
    (
        "WEATHER  \u2022  ODISHA, INDIA",
        "Cyclone Akvan bears down on Odisha",
        "About 300,000 people are evacuated to shelters as the severe "
        "storm nears landfall near Gopalpur, due at noon today.",
        (154, 107, 0),
        "spiral",
    ),
    (
        "JUSTICE  \u2022  THE HAGUE",
        "Myanmar guilty of Rohingya genocide",
        "The UN\u2019s top court rules 9\u20136 that Myanmar committed "
        "genocide in its 2017 crackdown, killing about 10,000 Rohingya.",
        (31, 78, 121),
        "scales",
    ),
    (
        "CLIMATE  \u2022  ANTALYA, TURKEY",
        "COP31 reaches its closing day",
        "Climate talks are due to close today, still split over fossil "
        "fuels and tripling adaptation finance to $120bn a year.",
        (30, 107, 52),
        "globe",
    ),
    (
        "SPACE",
        "Voyager 1, a light-day from home",
        "NASA confirms Voyager 1 is the first craft more than a "
        "light-day from Earth \u2014 26 billion km \u2014 after 49 years "
        "in space.",
        (74, 43, 107),
        "probe",
    ),
    (
        "ENTERTAINMENT",
        "GTA 6 makes $1.84bn in a day",
        "Rockstar\u2019s new game passes the $1.8bn box-office run of "
        "The Odyssey in its first day, with about 19 million copies sold.",
        (15, 95, 107),
        "pad",
    ),
]


def draw_card(d, x0, y0, x1, y1, story):
    kicker, headline, body, colour, glyph = story
    d.rounded_rectangle(
        [x0, y0, x1, y1], radius=8, fill=CARD, outline=CARD_BORDER, width=1
    )
    # Colour bar across the top, rounded at the top corners.
    d.rounded_rectangle([x0, y0, x1, y0 + 16], radius=8, fill=colour)
    d.rectangle([x0, y0 + 8, x1, y0 + 16], fill=colour)
    # Pictogram disc.
    cx, cy = x0 + 52, y0 + 62
    d.ellipse([cx - 33, cy - 33, cx + 33, cy + 33], fill=colour)
    GLYPHS[glyph](d, cx, cy)
    # Kicker beside the disc.
    d.text((x0 + 98, y0 + 52), kicker, font=F_KICKER, fill=colour)
    # Headline, then body.
    inner_w = x1 - x0 - 40
    y = y0 + 104
    for line in wrap(d, headline, F_HEAD, inner_w):
        d.text((x0 + 20, y), line, font=F_HEAD, fill=INK)
        y += 36
    y += 6
    for line in wrap(d, body, F_BODY, inner_w):
        d.text((x0 + 20, y), line, font=F_BODY, fill=(51, 48, 42))
        y += 27


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png"
    )
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Header.
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((24, 16), "FRIDAY 20 NOVEMBER 2026", font=F_DATE, fill=WHITE)
    d.text(
        (24, 78),
        "THE WORLD IN ONE IMAGE  \u2022  SIX STORIES FROM ONE DAY",
        font=F_SUB,
        fill=MUTED,
    )
    d.rectangle([0, 118, W, 124], fill=RED_RULE)

    # Grid of six cards: 2 columns x 3 rows.
    margin, gap = 16, 16
    grid_top, grid_bottom = 140, 968
    cell_w = (W - 2 * margin - gap) // 2
    cell_h = (grid_bottom - grid_top - 2 * gap) // 3
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = margin + col * (cell_w + gap)
        y0 = grid_top + row * (cell_h + gap)
        draw_card(d, x0, y0, x0 + cell_w, y0 + cell_h, story)

    # Footer.
    d.rectangle([0, 968, W, H], fill=NAVY)
    d.text(
        (24, 976),
        "Friday\u2019s news as reported on 20 November 2026  \u2022  "
        "Sources: Reuters, BBC, The Hindu, AP, Sensor Tower, PTI",
        font=F_FOOT,
        fill=MUTED,
    )
    d.text(
        (24, 998),
        "Figures are as reported that day; claims that could not be "
        "confirmed are not stated as fact.",
        font=F_FOOT,
        fill=MUTED,
    )

    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
