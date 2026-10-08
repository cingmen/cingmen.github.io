#!/usr/bin/env python3
"""Generate 1200x630 OG image matching the site's dark + lime branding."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (10, 10, 10)        # #0a0a0a
FG = (240, 240, 240)     # #f0f0f0
DIM = (143, 143, 143)    # #8f8f8f
ACCENT = (204, 255, 0)   # #ccff00
LINE = (38, 38, 38)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def pick(candidates, size):
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()

heavy_paths = [
    "/System/Library/Fonts/Supplemental/Impact.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
]
mono_paths = [
    "/System/Library/Fonts/Menlo.ttc",
    "/System/Library/Fonts/Monaco.ttf",
    "/System/Library/Fonts/Menlo-Bold.ttf",
]

f_huge = pick(heavy_paths, 148)
f_med = pick(heavy_paths, 84)
f_mono = pick(mono_paths, 26)
f_mono_s = pick(mono_paths, 22)

pad = 72

# top nav line
d.text((pad, 54), "SECURE_ID://ROOT", font=f_mono, fill=FG)
w = d.textlength("[ MENU ]", font=f_mono)
d.text((W - pad - w, 54), "[ MENU ]", font=f_mono, fill=DIM)
d.line([(pad, 110), (W - pad, 110)], fill=LINE, width=2)

# kicker
d.text((pad, 160), "// OFFENSIVE SECURITY — THREAT INTELLIGENCE — RESEARCH",
       font=f_mono_s, fill=ACCENT)

# headline
d.text((pad - 6, 210), "CYBER", font=f_huge, fill=FG)
d.text((pad - 6, 348), "SECURITY", font=f_huge, fill=FG)
# outlined-style second line: draw lime text
d.text((pad - 6, 486), "& RESEARCHER", font=f_med, fill=ACCENT)

# bottom status
d.text((pad, H - 64), "[ STATUS: OPERATIONAL ]", font=f_mono_s, fill=DIM)
msg = "JOESAVAT DONOVAN"
w = d.textlength(msg, font=f_mono_s)
d.text((W - pad - w, H - 64), msg, font=f_mono_s, fill=FG)

# subtle grid dots on right side for texture
for gx in range(W - 360, W - 40, 40):
    for gy in range(150, 420, 40):
        d.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=(34, 34, 34))

img.save("og-image.png", optimize=True)
print("saved og-image.png", img.size)
