#!/usr/bin/env python3
"""Generate brand assets: the write-up OG card and the PWA/touch icons."""
import os

from PIL import Image, ImageDraw, ImageFont

BG = (10, 10, 10)
FG = (240, 240, 240)
DIM = (110, 110, 110)
ACCENT = (204, 255, 0)
GRID = (18, 18, 18)

HEAD = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
MONO = "/System/Library/Fonts/Supplemental/Andale Mono.ttf"

os.makedirs("assets/icons", exist_ok=True)


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def fit_text(draw, text, max_w, start_size, font_path):
    size = start_size
    face = font(font_path, size)
    while draw.textlength(text, font=face) > max_w and size > 10:
        size -= 2
        face = font(font_path, size)
    return face


def og_card(path, kicker, line1, line2, footer):
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    for x in range(0, w, 60):
        d.line([(x, 0), (x, h)], fill=GRID, width=1)
    for y in range(0, h, 60):
        d.line([(0, y), (w, y)], fill=GRID, width=1)
    d.rectangle([0, 0, int(w * 0.28), 4], fill=ACCENT)

    d.text((56, 84), kicker, fill=ACCENT, font=font(MONO, 22))
    f1 = fit_text(d, line1, w - 112, 118, HEAD)
    d.text((56, 158), line1, fill=FG, font=f1)
    f2 = fit_text(d, line2, w - 112, 118, HEAD)
    d.text((56, 158 + f1.size + 14), line2, fill=ACCENT, font=f2)
    d.text((56, h - 92), footer, fill=DIM, font=font(MONO, 20))
    img.save(path)
    print("og", path, img.size)


def icon(path, size):
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)
    pad = max(2, size // 32)
    d.rectangle([pad, pad, size - pad, size - pad], outline=(26, 26, 26), width=max(1, size // 128))
    cx = cy = size // 2
    ring = size * 0.30
    stroke = max(2, int(size * 0.055))
    d.ellipse([cx - ring, cy - ring, cx + ring, cy + ring], outline=ACCENT, width=stroke)
    dot = size * 0.075
    d.ellipse([cx - dot, cy - dot, cx + dot, cy + dot], fill=ACCENT)
    img.save(path)
    print("icon", path, img.size)


og_card(
    "assets/og-writeup-lame.png",
    "WRITE-UP // CTF - LINUX PRIVILEGE ESCALATION",
    "HTB - LAME",
    "SAMBA USERMAP TO ROOT",
    "JOESAVAT DONOVAN — SECURE_ID://ROOT",
)

icon("assets/icons/icon-192.png", 192)
icon("assets/icons/icon-512.png", 512)
icon("assets/icons/apple-touch-icon.png", 180)
