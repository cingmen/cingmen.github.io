#!/usr/bin/env python3
"""Generate per-case-study thumbnails and OG images in the site's dark+lime brand."""
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('assets/thumbs', exist_ok=True)

BG = (10, 10, 10)
FG = (240, 240, 240)
DIM = (110, 110, 110)
ACCENT = (204, 255, 0)
LINE = (34, 34, 34)

HEAD = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
MONO = "/System/Library/Fonts/Supplemental/Andale Mono.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()

CASES = [
    ("work-1", "BLACKGATE", "PERIMETER BREACH", "CASE STUDY // 01 — WEB & NETWORK"),
    ("work-2", "OPERATION", "NIGHTSHADE", "CASE STUDY // 02 — AD RED TEAM"),
    ("work-3", "IOT BOTNET", "TELEMETRY STUDY", "CASE STUDY // 03 — MALWARE RESEARCH"),
]


def draw_base(w, h):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    # grid lines subtle
    for x in range(0, w, 60):
        d.line([(x, 0), (x, h)], fill=(18, 18, 18), width=1)
    for y in range(0, h, 60):
        d.line([(0, y), (w, y)], fill=(18, 18, 18), width=1)
    # top accent bar
    d.rectangle([0, 0, int(w * 0.28), 4], fill=ACCENT)
    return img, d


def fit_text(d, text, max_w, start_size, font_path):
    size = start_size
    f = font(font_path, size)
    while d.textlength(text, font=f) > max_w and size > 10:
        size -= 2
        f = font(font_path, size)
    return f


def make_thumb(name, l1, l2, kicker):
    W, H = 640, 400
    img, d = draw_base(W, H)
    # kicker
    kf = font(MONO, 13)
    d.text((32, 42), kicker, fill=ACCENT, font=kf)
    # headline two stacked lines
    hf1 = fit_text(d, l1, W - 64, 64, HEAD)
    hf2 = fit_text(d, l2, W - 64, 64, HEAD)
    d.text((32, 90), l1, fill=FG, font=hf1)
    y2 = 90 + hf1.size + 6
    d.text((32, y2), l2, fill=ACCENT, font=hf2)
    # corner tag
    tf = font(MONO, 12)
    tag = "// SECURE_ID:ROOT"
    tw = d.textlength(tag, font=tf)
    d.text((W - tw - 32, H - 42), tag, fill=DIM, font=tf)
    img.save(f"assets/thumbs/{name}.png")
    print("thumb", name, f"assets/thumbs/{name}.png")


def make_og(name, l1, l2, kicker):
    W, H = 1200, 630
    img, d = draw_base(W, H)
    kf = font(MONO, 22)
    d.text((56, 84), kicker, fill=ACCENT, font=kf)
    hf1 = fit_text(d, l1, W - 112, 128, HEAD)
    hf2 = fit_text(d, l2, W - 112, 128, HEAD)
    d.text((56, 160), l1, fill=FG, font=hf1)
    y2 = 160 + hf1.size + 12
    d.text((56, y2), l2, fill=ACCENT, font=hf2)
    tf = font(MONO, 20)
    by = "JOESAVAT DONOVAN — SECURE_ID://ROOT"
    d.text((56, H - 92), by, fill=DIM, font=tf)
    img.save(f"assets/{name}.png")
    print("og", name, f"assets/{name}.png")


for name, l1, l2, kicker in CASES:
    n_short1, n_short2 = l1[:18], l2[:18]
    make_thumb(name, l1, l2, kicker)
    make_og(f"og-{n_short1.lower().replace(' ', '-')}", l1, l2, kicker)
