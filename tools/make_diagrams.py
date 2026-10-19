#!/usr/bin/env python3
"""Generate 6 brand-consistent SVG diagrams replacing shot__box placeholders.

API:
  common(w, h, label) -> svg header string (remember to call defs())
  box(x, y, w, h, text, accent=False, fs=13) -> rect + centered mono text
  arrow(x1, y1, x2, y2, accent=False) -> line with arrowhead marker
  htext(x, y, text, ...) -> plain text helper
"""
import os

os.makedirs('assets/diagrams', exist_ok=True)

BG = '#0f0f0f'
FG = '#f0f0f0'
DIM = '#8f8f8f'
ACCENT = '#ccff00'
LINE = '#2a2a2a'
GRID = '#161616'
MONO = "'Space Mono','Andale Mono',monospace"
W, H = 900, 506  # 16:9


def common(label):
    grid = ''
    for x in range(56, W, 56):
        grid += f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{GRID}" stroke-width="1"/>'
    for y in range(56, H, 56):
        grid += f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{GRID}" stroke-width="1"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{MONO}">
<rect width="{W}" height="{H}" fill="{BG}"/>
{grid}
<rect x="0" y="0" width="{int(W * 0.22)}" height="4" fill="{ACCENT}"/>
<rect x="0" y="0" width="4" height="{int(H * 0.25)}" fill="{ACCENT}"/>
<text x="24" y="34" fill="{ACCENT}" font-size="12" letter-spacing="2">{label}</text>'''


DEFS = ('<defs>'
        f'<marker id="ahD" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{DIM}"/></marker>'
        f'<marker id="ahA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{ACCENT}"/></marker>'
        '</defs>')


def close():
    return '\n</svg>'


def box(x, y, w, h, label, accent=False, fs=13):
    stroke = ACCENT if accent else LINE
    if accent:
        fill, txt, sw = '#151a04', BG, 2
    else:
        fill, txt, sw = BG, FG, 1
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" '
           f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n')
    lines = label.split('\\n')
    lh = h / (len(lines) + 1)
    for i, ln in enumerate(lines):
        yy = y + lh * (i + 1) + fs * 0.35
        out += (f'<text x="{x + w / 2}" y="{yy:g}" text-anchor="middle" '
                f'fill="{txt}" font-size="{fs}" letter-spacing="1">{ln}</text>\n')
    return out


def arrow(x1, y1, x2, y2, accent=False):
    color = ACCENT if accent else DIM
    marker = 'ahA' if accent else 'ahD'
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="1.5" marker-end="url(#{marker})"/>')


def htext(x, y, text, color=FG, fs=13, anchor='start', ls=1):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{fs}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}">{text}</text>')


def save(name, body):
    path = f'assets/diagrams/{name}.svg'
    with open(path, 'w') as f:
        f.write(body)
    print('ok', path)


# ---- 01 / project-1: time-based payload confirmation ----
b = common('FIG.01 // TIME-BASED INJECTION — RESPONSE DELTA')
b += DEFS
# lane A: normal request
b += box(50, 120, 220, 64, 'BASELINE REQUEST', fs=13)
b += box(380, 120, 200, 64, 'DSP 0.1 s', fs=13, accent=False)
b += arrow(274, 152, 376, 152)
b += htext(640, 158, '200 OK — 0.10 s', color=DIM, fs=12)
b += arrow(584, 152, 634, 152)
# lane B: injected
b += box(50, 240, 220, 64, "PAYLOAD: WAITFOR\\nDELAY '0:0:4'--", fs=12, accent=True)
b += arrow(274, 272, 376, 272, accent=True)
b += box(380, 240, 200, 64, 'DSP 4.0 s', fs=13, accent=True)
b += arrow(584, 272, 634, 272, accent=True)
b += htext(640, 278, '200 OK — 4.09 s', color=ACCENT, fs=12)
# delta callout
b += box(50, 360, 530, 64, 'Δ RESPONSE ≈ 4.00 s ACROSS 20 RUNS (σ &lt; 0.06 s)', fs=12, accent=True)
b += htext(24, 476, 'constant delta proves controlled execution — reproducible across WAF rule sets',
           color=DIM, fs=11)
save('blackgate-1', b + close())

# ---- 02 / project-1: full kill chain ----
b = common('FIG.02 // KILL CHAIN — WAF BYPASS TO CROWN JEWELS')
b += DEFS
steps = [('EXTERNAL\\nACCESS', 30), ('WAF\\nBYPASS', 205), ('BLIND\\nSQLI', 380),
         ('JWT\\nREPLAY', 555), ('SSRF\\nPIVOT', 730)]
for i, (label, x) in enumerate(steps):
    accent = i in (1, 4)  # the two pivots that broke assumptions
    b += box(x, 150, 148, 78, label, accent=accent, fs=14)
    if i < len(steps) - 1:
        accent_link = i >= 1
        b += arrow(x + 152, 189, x + 171, 189, accent=accent_link)
b += arrow(804, 232, 804, 330, accent=True)
b += box(300, 330, 348, 74, 'CROWN-JEWEL SEGMENT\\n(vlan 10.8.0.0/22)', accent=True, fs=13)
b += htext(24, 476, 'each hop composites into full compromise despite per-node hardening', color=DIM, fs=11)
save('blackgate-2', b + close())

# ---- 03 / project-2: bloodhound attack path ----
b = common('FIG.01 // BLOODHOUND SHORTEST PATH — 3 HOPS TO DA')
b += DEFS
nodes = [('jdoe@CORP\\nworkstation session', 40, False),
         ('HELPDESK_GRP\\nnested local admin', 250, False),
         ('svc_backup\\nkerberoastable SPN', 480, False),
         ('DOMAIN ADMIN\\nkrbtgt rotable', 690, True)]
for label, x, acc in nodes:
    b += box(x, 120, 170, 78, label, accent=acc, fs=13)
b += arrow(214, 159, 246, 159)
b += arrow(444, 159, 476, 159)
b += arrow(674, 159, 686, 159, accent=True)
b += box(480, 260, 170, 78, 'KERBEROAST\\nTGS → offline crack', accent=True, fs=12)
b += arrow(565, 202, 565, 256, accent=True)
b += arrow(860, 199, 880, 199, accent=True)
b += htext(870, 226, 'DA', color=ACCENT, fs=12, anchor='middle')
b += htext(24, 476, 'path length 3 — the graph flattens the tiering the orgchart assumed existed', color=DIM, fs=11)
save('nightshade-1', b + close())

# ---- 04 / project-2: purple-team detection timeline ----
b = common('FIG.02 // PURPLE-TEAM DEBRIEF — TECHNIQUE VS DETECTION')
rows = [('DISCOVERY — LDAP insulinrecon', 'no alert — noise floor', DIM),
        ('KERBEROAST — TGS burst 4769', 'no alert — no rate rule', DIM),
        ('DCSYNC — proof of impact', 'SOC raised @ 4 min', ACCENT),
        ('KRBTGT RESET — deferred', 'change-board hold', DIM)]
y = 140
for tech, det, color in rows:
    dot = ACCENT if color == ACCENT else LINE
    b += f'<circle cx="60" cy="{y - 5}" r="6" fill="{dot}"/>'
    b += htext(80, y, tech, color=FG, fs=14)
    b += htext(560, y, det, color=color, fs=12)
    b += f'<line x1="40" y1="{y + 18}" x2="860" y2="{y + 18}" stroke="{LINE}" stroke-width="1"/>'
    y += 78
b += htext(560, y - 60, '2 / 4 techniques detected pre-debrief', color=DIM, fs=11)
b += htext(24, 476, '7 detection gaps logged — Sigma cover shipped same sprint', color=DIM, fs=11)
save('nightshade-2', b + close())

# ---- 05 / project-3: qemu detonation trace ----
b = common('FIG.01 // QEMU DETONATION — RECOVERED C2 HANDSHAKE')
b += DEFS
b += box(120, 110, 160, 50, 'BOT (qemu)', fs=13)
b += box(600, 110, 180, 50, 'C2 :4443', accent=True, fs=13)
lifex1, lifex2 = 200, 690
b += f'<line x1="{lifex1}" y1="160" x2="{lifex1}" y2="430" stroke="{GRID}" stroke-width="1" stroke-dasharray="4 6"/>'
b += f'<line x1="{lifex2}" y1="160" x2="{lifex2}" y2="430" stroke="{GRID}" stroke-width="1" stroke-dasharray="4 6"/>'
msgs = [
    ('SYN — prober /proc/self/status check', 210, DIM, False),
    ('TLV keep-alive 0x01 (first beacon)', 280, ACCENT, True),
    ('TLV directive 0x02 — !SCAN 10.0.0.0/8', 350, ACCENT, True),
    ('flood order 0x03 — udp amp list', 420, DIM, False),
]
for label, yy, color, alert in msgs:
    fwd = alert  # alert lines are C2 → bot
    if alert:
        b += arrow(lifex2, yy, lifex1, yy, accent=True)
    else:
        b += arrow(lifex1, yy, lifex2, yy)
    b += htext(450, yy - 8, label, color=color, fs=11, anchor='middle')
# labels ON the lifelines for direction clarity
b += htext(lifex1, 448, 'bot', color=DIM, fs=11, anchor='middle')
b += htext(lifex2, 448, 'c2', color=DIM, fs=11, anchor='middle')
b += htext(24, 476, 'plaintext TLV over TCP — directives reconstructable byte-for-byte from trace', color=DIM, fs=11)
save('botnet-1', b + close())

# ---- 06 / project-3: yara validation matrix ----
b = common('FIG.02 // YARA VALIDATION — CLUSTER HIT-RATE (n=74)')
clusters = [('A', 32, 1.0), ('B', 14, 1.0), ('C', 11, 1.0),
            ('D', 9, 0.90), ('E', 5, 1.0), ('F', 3, 1.0)]
baseline, hmax = 430, 200
bx = 90
for name, count, rate in clusters:
    bh = int(hmax * rate)
    top = baseline - bh
    weak = rate < 1.0
    bar_fill = ACCENT if not weak else '#5a5f45'
    b += f'<rect x="{bx}" y="{top}" width="70" height="{bh}" fill="{bar_fill}" opacity="{0.85 if not weak else 0.7}"/>'
    b += f'<rect x="{bx}" y="{top}" width="70" height="{bh}" fill="none" stroke="{ACCENT if not weak else LINE}"/>'
    b += htext(bx + 35, top - 12, str(count), color=FG, fs=14, anchor='middle')
    b += htext(bx + 35, baseline + 24, f'FAM-{name}', color=DIM, fs=12, anchor='middle')
    b += htext(bx + 35, baseline + 44, f'{int(rate * 100)}%', color=ACCENT if not weak else DIM, fs=11, anchor='middle')
    bx += 135
# axis
b += f'<line x1="60" y1="{baseline}" x2="850" y2="{baseline}" stroke="{LINE}" stroke-width="1"/>'
b += htext(600, 200, 'rule FLAG-bridge-D.v2 0.90 → 1.00 patched in corpus wave 2', color=DIM, fs=11, anchor='middle')
b += htext(24, 476, '9 rules × 400k public corpus = 0 false positives — shared loader skeleton covers 74/74', color=DIM, fs=11)
save('botnet-2', b + close())

# ---- 07 / writeup-1: reverse shell chain ----
b = common('FIG.01 // SMB RCE — ROOT SHELL ON THE NETCAT LISTENER')
b += DEFS
nodes = [('ATTACKER\nnc -lvnp 4444', 40, False), ('SMB :445\nunattend .bat write', 330, False),
         ('NT AUTHORITY\\SYSTEM\nreverse connect', 640, True)]
for label, x, acc in nodes:
    b += box(x, 140, 200, 78, label, accent=acc, fs=13)
b += arrow(244, 179, 326, 179)
b += arrow(534, 179, 636, 179, accent=True)
b += arrow(740, 222, 180, 340, accent=True)
b += box(120, 340, 400, 78, 'reviewer@lab:~$\n$ nc -lvnp 4444 → uid=0(root)', fs=13)
b += htext(24, 476, 'because SMB runs as SYSTEM, the write lands a root shell — no privesc hop required', color=DIM, fs=11)
save('writeup-1', b + close())

print('all diagrams generated')
